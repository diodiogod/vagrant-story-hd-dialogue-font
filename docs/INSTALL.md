# Installation and troubleshooting

Choose **HD Fonts** (101 PNGs) or **HD Fonts + UI Art** (104 PNGs).
Both are complete packages for Vagrant Story USA **SLUS-01040**; install one.
Use the matching Android or desktop download from the [README](../README.md).

## Android

1. Stop the game. If switching editions or upgrading an experimental pack,
   [remove the previous replacements](#switching-editions) first.
2. Download the Android ZIP and **leave it zipped**.
3. Open **Transfer Data → ZIP file → Import** and select it. Choose **Textures**
   if import categories are offered.
4. Enable **Texture Cache** and **Texture Replacements** with a hardware
   renderer such as Vulkan.
5. Set **Texture Filtering** and **Sprite Texture Filtering** to
   **Nearest Neighbor**. Try 4×/5× internal resolution.
6. On **Android 0.1-8969-g611bb8fb4**, disable **PGXP Geometry Correction** in
   Vagrant Story's per-game settings. [Compatibility details](PGXP.md).
7. Restart the game.

Android archives contain images only, with this layout:

```text
textures/
  SLUS-01040/
    replacements/
      (the chosen edition's PNGs)
```

The first folder must be `textures`. An extra wrapper can produce
“No importable files were found.” The layout and accepted image types were
checked against Android 0.1-8969's importer. Its ZIP importer does not accept
`config.yaml`; that optional file is excluded from Android downloads.

## Desktop

Stop the game. Extract the desktop ZIP and put its **SLUS-01040** folder inside
DuckStation's data directory under **textures**. The resulting path must be
`textures/SLUS-01040/replacements/`.

Enable Texture Cache and Texture Replacements with a hardware renderer. Set
both texture filters to **Nearest Neighbor**, then restart. Texture dumping
and VRAM Write Replacements are not required.

For local edits, DuckStation's texture-reload command can refresh replacements
without rebooting the game.

## Switching editions

**Importing or extracting a ZIP adds and overwrites files; it does not remove
the other edition's artwork.** This also applies when moving from v0.6, which
already included HD material badges.

1. Stop the game and back up your existing replacement folder.
2. Remove the previous pack's files from `textures/SLUS-01040/replacements/`.
   If the folder contains only this pack, replace the whole folder with a clean
   one. Preserve unrelated mods separately.
3. Install the chosen edition and restart the game.

On Android, use your existing file-access method or an emulator export/import
workflow that lets you remove the old texture files. Importing the fonts ZIP
over the art ZIP alone will leave its badges and silhouettes installed.

Both editions share the same 101 font files. The art edition adds 20 optional
texture files. To return to HD Fonts, remove every file in the `ui-art` group of
[editions.json](../editions.json), or replace this pack's folder with a clean
Fonts installation. The three-file removal list from v0.7 is no longer sufficient.

The [edition manifest](../editions.json) records the exact selection. Avoid
combining overlapping font packs. Disable Texture Replacements to return to
the game's original textures.

An independent PPF weapon/control mod can be used alongside this pack. A disc
patch that changes the native font needs separate compatibility testing.

## Troubleshooting

- **No importable files:** select the Android ZIP without extracting it; its first folder must be `textures`.
- **Artwork remains after switching:** remove the old artwork files; ZIP import does not uninstall them.
- **Blurry letters:** set both texture filters to Nearest Neighbor and restart.
- **Bands or offset menu text:** see [PGXP compatibility](PGXP.md).
- **Unchanged font:** check the USA serial, hardware renderer, Texture Cache and Texture Replacements.

For a bug report, include a screenshot, edition, game serial, emulator version,
device/renderer and PGXP/filter settings.
