# Preparing a release

After integrating reviewed textures and updating the changelog, run:

```powershell
python tools/bump_version.py --date YYYY-MM-DD
python tools/package_release.py
python -m unittest discover -s tools -p "test_*.py"
```

The bump command reads `verification.json`. It promotes `X.Y-preview` to
`X.Y-beta`; otherwise it advances the minor version. It updates release metadata,
the two-edition download table and the source collection's ABOUT file. Historical
release sections and evidence are retained. Run it once per release.

The packager uses `editions.json` to build four complete ZIPs: HD Fonts and
HD Fonts + UI Art, each for Android and desktop. It checks shared font identity,
file hashes, dimensions, importer paths and archive contents. Outputs and
SHA256SUMS stay ignored under `release-assets/`. The source texture folder is
the superset; installing it directly includes the optional artwork.

Review the notes, comparisons and archives before publishing. When publication
is authorized, commit and push, create the annotated tag and a draft GitHub
prerelease, upload the four ZIPs and SHA256SUMS, verify them, then publish.
Preparation does not push, tag or create a GitHub release. No game data is included.
