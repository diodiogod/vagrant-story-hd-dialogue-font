# Preparing a release

After integrating reviewed textures and updating the changelog, run:

```powershell
python tools/bump_version.py --date YYYY-MM-DD
python tools/package_release.py
```

The bump command reads `verification.json`. It promotes `X.Y-preview` to
`X.Y-beta`; otherwise it advances the minor version. It updates release metadata,
current download links, installation counts and the pack's ABOUT file. Historical
release sections and evidence are retained. Run it once per release.

Review the notes and comparisons, verify archive hashes and import paths, then
commit and push the release commit and annotated tag. Create a draft GitHub
prerelease, verify its uploaded assets, and publish it. No game data is included.
