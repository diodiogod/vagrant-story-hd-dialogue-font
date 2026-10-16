"""Prepare the next beta's metadata and current download/install references."""
from pathlib import Path
from datetime import date
import argparse
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')


def main(release_date):
    manifest = json.loads((ROOT/'verification.json').read_text(encoding='utf-8'))
    match = re.fullmatch(r'(\d+)\.(\d+)-(preview|beta)', manifest['version'])
    if not match:
        raise ValueError('Expected an X.Y-preview or X.Y-beta version')
    major, minor = int(match[1]), int(match[2])
    if match[3] != 'preview':
        minor += 1
    package = f'{major}.{minor}'
    version, tag = package+'-beta', 'v'+package+'-beta'
    manifest.update(version=version, package_version=package, date=release_date.isoformat(),
                    status=f'v{package} beta release')
    android_path = ROOT/'verification-android-import.json'
    android = json.loads(android_path.read_text(encoding='utf-8'))
    android.update(version=version, status=f'v{package} beta release',
                   archive_hashes=f'GitHub release {tag}: SHA256SUMS.txt')
    count = manifest['pngs']
    readme = (ROOT/'README.md').read_text(encoding='utf-8')
    downloads = f'**v{package} beta:** [Android ZIP](https://github.com/diodiogod/vagrant-story-hd-dialogue-font/releases/download/{tag}/vagrant-story-font-v{package}-android.zip) · [Desktop ZIP](https://github.com/diodiogod/vagrant-story-hd-dialogue-font/releases/download/{tag}/vagrant-story-font-v{package}-desktop.zip) · [Release notes](RELEASE-NOTES.md)'
    readme, n = re.subn(r'^\*\*v\d+\.\d+ beta:\*\*.*$', downloads, readme, count=1, flags=re.M)
    if n != 1:
        raise ValueError('Missing current README download line')
    install = (ROOT/'docs/INSTALL.md').read_text(encoding='utf-8')
    install = re.sub(r'^Published downloads:.*$', f'Published downloads: **v{package} beta, {count} PNGs**.', install, count=1, flags=re.M)
    install = re.sub(r'vagrant-story-font-v\d+\.\d+-(android|desktop)\.zip', lambda m: f'vagrant-story-font-v{package}-{m[1]}.zip', install)
    install = re.sub(r'exactly \d+ texture PNGs', f'exactly {count} texture PNGs', install)
    install = re.sub(r'\(\d+ PNG files\)', f'({count} PNG files)', install)
    about = (
        f'Vagrant Story USA SLUS-01040 — Original Style HD Fonts\n'
        f'v{package} beta: {count} PNGs at 8x.\n'
        'Dialogue, menus, selected HUD/UI text and save labels.\n'
        'Native-style UI borders; soft grayscale fringe on the white menu font.\n'
        'See README and docs for installation, comparisons and known issues.\n'
        'Android 8969: PGXP off per-game; both texture filters Nearest Neighbor.\n'
        'No game image, executable, BIOS, saves or emulator included.\n')
    # Validate the planned edits before writing any version-bearing files.
    write_json(ROOT/'verification.json', manifest)
    write_json(android_path, android)
    (ROOT/'README.md').write_text(readme, encoding='utf-8')
    (ROOT/'docs/INSTALL.md').write_text(install, encoding='utf-8')
    (ROOT/'textures/SLUS-01040/ABOUT.txt').write_text(about, encoding='utf-8')
    print(json.dumps(dict(version=version, tag=tag, package_version=package,
                          date=release_date.isoformat(), pngs=count), indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', type=date.fromisoformat, required=True)
    main(parser.parse_args().date)
