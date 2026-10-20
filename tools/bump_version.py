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
                    status=f'v{package} beta prepared locally; unpublished')
    android_path = ROOT/'verification-android-import.json'
    android = json.loads(android_path.read_text(encoding='utf-8'))
    android.update(version=version, status=f'v{package} beta prepared locally; unpublished',
                   archive_hashes=f'GitHub release {tag}: SHA256SUMS.txt')
    count = manifest['pngs']
    readme = (ROOT/'README.md').read_text(encoding='utf-8')
    start, end = '<!-- downloads:start -->', '<!-- downloads:end -->'
    if readme.count(start) != 1 or readme.count(end) != 1:
        raise ValueError('Missing unique README download table markers')
    selections = json.loads((ROOT/'editions.json').read_text(encoding='utf-8'))
    lines = [start, f'**v{package} beta**', '',
             '| Edition | What changes | Android | Desktop |',
             '| --- | --- | --- | --- |']
    for key, edition in selections['editions'].items():
        label = f"**{edition['name']}**" + (' · WIP' if key == 'ui-art' else '')
        scope = ('Dialogue, menus, HUD and combat text; original pixel artwork' if key == 'fonts'
                 else 'Same fonts, plus material badges and body silhouettes')
        base = f'https://github.com/diodiogod/vagrant-story-hd-dialogue-font/releases/download/{tag}/vagrant-story-{key}-v{package}'
        lines.append(f'| {label} | {scope} | [ZIP]({base}-android.zip) | [ZIP]({base}-desktop.zip) |')
    lines.append(end)
    readme = readme[:readme.index(start)] + '\n'.join(lines) + readme[readme.index(end)+len(end):]
    install = (ROOT/'docs/INSTALL.md').read_text(encoding='utf-8')
    install = re.sub(r'^Published downloads:.*$', f'Published downloads: **v{package} beta, {count} PNGs**.', install, count=1, flags=re.M)
    install = re.sub(r'vagrant-story-font-v\d+\.\d+-(android|desktop)\.zip', lambda m: f'vagrant-story-font-v{package}-{m[1]}.zip', install)
    install = re.sub(r'exactly \d+ texture PNGs', f'exactly {count} texture PNGs', install)
    install = re.sub(r'\(\d+ PNG files\)', f'({count} PNG files)', install)
    about = (
        f'Vagrant Story USA SLUS-01040 — HD Fonts & UI\n'
        f'v{package} beta source collection: {count} PNGs at 8x.\n'
        'Use a release ZIP to select HD Fonts or HD Fonts + UI Art.\n'
        'The source collection includes optional badges and body silhouettes.\n'
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
