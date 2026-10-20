"""Build both complete editions for Android/desktop. Outputs: release-assets/."""
from datetime import date
from pathlib import Path
import hashlib
import json
import re
import struct
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PNG_NAME = re.compile(r'texpage-STP4-[0-9A-F]{16}-[0-9A-F]{16}-64x256-(\d+)-(\d+)-(\d+)x(\d+)-P0-15\.png')
ANDROID_PREFIX = 'textures/SLUS-01040/replacements/'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def fingerprint(files):
    return digest(json.dumps(sorted(files.items())).encode())


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def accepts_android(name):
    return name.startswith(ANDROID_PREFIX) and bool(PNG_NAME.fullmatch(name[len(ANDROID_PREFIX):]))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def edition_files(manifest, selection):
    records = manifest['files']
    expected = {r['filename']:r['sha256'] for r in records}
    require(len(expected) == len(records) == manifest['pngs'], 'Invalid asset count')
    require(fingerprint(expected) == manifest['pack_fingerprint'], 'Invalid pack fingerprint')
    groups = selection['groups']
    flat = [name for names in groups.values() for name in names]
    require(len(flat) == len(set(flat)), 'Asset belongs to multiple groups')
    require(set(flat) == set(expected), 'Unclassified or unknown asset')
    require(set(selection['editions']) == {'fonts', 'ui-art'}, 'Expected two editions')
    require(selection['editions']['fonts']['groups'] == ['fonts'], 'Fonts edition contains artwork')
    require(selection['editions']['ui-art']['groups'] == ['fonts', 'ui-art'], 'Incomplete UI-art edition')
    result = {}
    for key, edition in selection['editions'].items():
        names = [n for group in edition['groups'] for n in groups[group]]
        result[key] = {n:expected[n] for n in names}
        recorded = manifest['editions'][key]
        require(len(names) == recorded['pngs'], f'Wrong {key} asset count')
        require(fingerprint(result[key]) == recorded['pack_fingerprint'], f'Wrong {key} fingerprint')
    require(result['ui-art'] == expected, 'UI-art edition must contain the complete pack')
    return result


def validate(root=ROOT):
    manifest = read_json(root/'verification.json')
    selection = read_json(root/'editions.json')
    editions = edition_files(manifest, selection)
    expected = editions['ui-art']
    repl = root/'textures/SLUS-01040/replacements'
    actual = {p.name:digest(p.read_bytes()) for p in repl.iterdir() if p.is_file()}
    require(actual == expected, 'Texture files differ from the reviewed manifest')
    require(all(p.is_file() for p in repl.iterdir()), 'Unexpected directory in replacements')
    for name in expected:
        match = PNG_NAME.fullmatch(name)
        require(match is not None, f'Invalid replacement filename: {name}')
        data = (repl/name).read_bytes()
        require(data[:16] == b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR', f'Invalid PNG: {name}')
        _, _, width, height = map(int, match.groups())
        require(struct.unpack('>II',data[16:24]) == (width*8,height*8), f'Wrong 8x size: {name}')
    old = read_json(root/'docs/v0.2/verification.json')
    require(len(old['files']) == 7, 'Missing original dialogue manifest')
    require(all(editions['fonts'].get(r['filename']) == r['sha256'] for r in old['files']), 'Published dialogue changed')
    reference = manifest.get('shared_fonts_reference')
    if reference:
        prior = read_json(root/reference['manifest'])
        font_reference = {r['filename']:r['sha256'] for r in prior['files'] if r['filename'] not in reference['excluded_art_files']}
        require(editions['fonts'] == font_reference, 'Shared fonts differ from the reviewed release')
    example = ANDROID_PREFIX + next(iter(expected))
    require(accepts_android(example), 'Valid Android path rejected')
    for invalid in ['ExtraFolder/'+example, example.removeprefix('textures/'), 'textures/SLUS-01040/config.yaml',
                    ANDROID_PREFIX+'../'+example.rsplit('/',1)[-1], ANDROID_PREFIX+'extra/'+example.rsplit('/',1)[-1]]:
        require(not accepts_android(invalid), 'Invalid Android payload accepted')
    return manifest, selection, editions


def about(manifest, edition, count):
    return (f"Vagrant Story USA SLUS-01040 — {edition['name']}\n"
            f"v{manifest['package_version']} beta: {count} PNGs at 8x.\n{edition['description']}\n"
            'Install one complete edition. Remove the previous replacements folder when switching.\n'
            'Both texture filters: Nearest Neighbor. Android 8969: PGXP Geometry Correction off per game.\n'
            'No game, BIOS, saves or emulator included.\n').encode('utf-8')


def build(root=ROOT):
    manifest, selection, editions = validate(root)
    version = manifest['package_version']
    require(re.fullmatch(r'[0-9]+\.[0-9]+',version), 'Invalid package version')
    release_date = date.fromisoformat(manifest['date'])
    require(1980 <= release_date.year <= 2107, 'Release date outside ZIP range')
    out = root/'release-assets'
    out.mkdir(exist_ok=True)
    result = []
    for key, files in editions.items():
        for platform in ('android','desktop'):
            prefix = 'textures/SLUS-01040/' if platform == 'android' else 'SLUS-01040/'
            payload = {prefix+'replacements/'+n:(root/'textures/SLUS-01040/replacements'/n).read_bytes() for n in sorted(files)}
            if platform == 'desktop':
                payload[prefix+'config.yaml'] = (root/'textures/SLUS-01040/config.yaml').read_text(encoding='utf-8').encode('utf-8')
                payload[prefix+'ABOUT.txt'] = about(manifest,selection['editions'][key],len(files))
            else:
                require(all(map(accepts_android,payload)), 'Invalid Android layout')
            path = out/f'vagrant-story-{key}-v{version}-{platform}.zip'
            with zipfile.ZipFile(path,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
                for name, data in sorted(payload.items()):
                    info = zipfile.ZipInfo(name,date_time=(*release_date.timetuple()[:3],0,0,0))
                    info.compress_type = zipfile.ZIP_DEFLATED
                    info.create_system = 3
                    info.external_attr = 0o100644 << 16
                    archive.writestr(info,data,compresslevel=9)
            with zipfile.ZipFile(path) as archive:
                require(archive.testzip() is None, 'ZIP CRC failure')
                require(len(archive.namelist()) == len(payload) and set(archive.namelist()) == set(payload), 'Wrong ZIP entries')
                require(all(archive.read(n) == d for n,d in payload.items()), 'ZIP contents changed')
            result.append(dict(name=path.name,edition=key,platform=platform,pngs=len(files),bytes=path.stat().st_size,
                               sha256=digest(path.read_bytes()),pack_fingerprint=fingerprint(files)))
    report = dict(version=manifest['version'],status='Validated release packages',shared_fonts_identical=True,
                  dialogue_unchanged=True,android_import_path_controls_passed=True,archives=result)
    (out/'SHA256SUMS.txt').write_text(''.join(f"{a['sha256']}  {a['name']}\n" for a in result),encoding='utf-8')
    (out/'packages.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    return report


if __name__ == '__main__':
    print(json.dumps(build(),indent=2))
