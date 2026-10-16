"""Validate the checked-in font payload and build deterministic release ZIPs.

Run with Python 3.10+: python tools/package_release.py
Outputs are ignored by Git under release-assets/. No game data is required.
"""

from pathlib import Path
import hashlib
import json
import re
import struct
import zipfile
from datetime import date


ROOT = Path(__file__).resolve().parents[1]
PNG_NAME = re.compile(
    r"texpage-STP4-[0-9A-F]{16}-[0-9A-F]{16}-64x256-"
    r"(\d+)-(\d+)-(\d+)x(\d+)-P0-15\.png"
)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def accepts_android(name):
    # Strict subset of the inspected 8969 importer's supported image paths.
    return name.startswith("textures/SLUS-01040/replacements/") and bool(
        PNG_NAME.fullmatch(name.rsplit("/", 1)[-1])
    )


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    manifest = json.loads((ROOT / "verification.json").read_text(encoding="utf-8"))
    count = manifest["pngs"]
    version = manifest.get("package_version", "0.3")
    release_date = date.fromisoformat(manifest["date"])
    require(1980 <= release_date.year <= 2107, "Release date outside ZIP range")
    require(re.fullmatch(r"[0-9]+\.[0-9]+(?:-[a-z0-9]+)?", version), "Invalid package version")
    records = manifest["files"]
    expected = {f["filename"]: f["sha256"] for f in records}
    repl = ROOT / "textures/SLUS-01040/replacements"
    actual = {p.name: digest(p.read_bytes()) for p in repl.iterdir() if p.is_file()}
    require(len(records) == len(expected) == count and count > 0, "Invalid file count")
    require(actual == expected, "Texture files differ from the reviewed manifest")
    fingerprint = digest(json.dumps(sorted(expected.items())).encode())
    require(fingerprint == manifest["pack_fingerprint"], "Pack fingerprint differs")

    for name in expected:
        match = PNG_NAME.fullmatch(name)
        require(match is not None, f"Invalid replacement filename: {name}")
        data = (repl / name).read_bytes()
        require(data[:16] == b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR", f"Invalid PNG: {name}")
        _, _, width, height = map(int, match.groups())
        require(struct.unpack(">II", data[16:24]) == (width * 8, height * 8), f"Wrong 8x size: {name}")

    old = json.loads((ROOT / "docs/v0.2/verification.json").read_text(encoding="utf-8"))
    require(len(old["files"]) == 7, "Missing old dialogue manifest")
    for entry in old["files"]:
        require(expected.get(entry["filename"]) == entry["sha256"], "Published dialogue changed")

    example = "textures/SLUS-01040/replacements/" + next(iter(expected))
    require(accepts_android(example), "Valid Android path rejected")
    for invalid in ["ExtraFolder/" + example, example.removeprefix("textures/"),
                    "textures/SLUS-01040/config.yaml"]:
        require(not accepts_android(invalid), "Invalid Android payload accepted")

    out = ROOT / "release-assets"
    out.mkdir(exist_ok=True)
    result = []
    for platform in ("android", "desktop"):
        prefix = "textures/SLUS-01040/" if platform == "android" else "SLUS-01040/"
        payload = {prefix + "replacements/" + n: (repl / n).read_bytes() for n in sorted(expected)}
        if platform == "desktop":
            for name in ("config.yaml", "ABOUT.txt"):
                # Canonical LF text keeps archives identical across Git checkouts.
                payload[prefix + name] = (ROOT / "textures/SLUS-01040" / name).read_text(
                    encoding="utf-8"
                ).encode("utf-8")
        else:
            require(len(payload) == count and all(map(accepts_android, payload)), "Invalid import layout")
        path = out / f"vagrant-story-font-v{version}-{platform}.zip"
        with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for name, data in sorted(payload.items()):
                info = zipfile.ZipInfo(name, date_time=(*release_date.timetuple()[:3], 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                archive.writestr(info, data, compresslevel=9)
        with zipfile.ZipFile(path) as archive:
            require(archive.testzip() is None, "ZIP CRC failure")
            require(set(archive.namelist()) == set(payload), "Wrong ZIP contents")
            for name, data in payload.items():
                require(archive.read(name) == data, f"ZIP payload changed: {name}")
        result.append(dict(name=path.name, bytes=path.stat().st_size, sha256=digest(path.read_bytes())))

    (out / "SHA256SUMS.txt").write_text(
        "".join(f"{a['sha256']}  {a['name']}\n" for a in result), encoding="utf-8"
    )
    print(json.dumps(dict(pack_fingerprint=fingerprint, pngs=count,
                          dialogue_unchanged=True, archives=result), indent=2))


if __name__ == "__main__":
    main()
