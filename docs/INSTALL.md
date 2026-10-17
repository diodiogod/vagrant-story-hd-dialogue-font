# Installation and troubleshooting

Published downloads: **v0.6 beta, 103 PNGs**.

## Android

1. Download **vagrant-story-font-v0.6-android.zip** from the release assets and
   copy it to your phone. **Leave it zipped.**
2. Fully stop the running game in DuckStation.
3. Open **Transfer Data → ZIP file → Import** and select the ZIP.
4. Choose **Textures** if import categories are offered. The archive contains
   exactly 103 texture PNGs, without settings, memory cards or save states.
5. In the game's graphics settings, enable **Texture Cache** and
   **Texture Replacements**. Use a hardware renderer, such as Vulkan, and your
   preferred internal resolution; 4x/5x makes the sharper lettering easier to see.
6. Set **Texture Filtering → Nearest Neighbor** and
   **Sprite Texture Filtering → Nearest Neighbor**. Set both.
7. On **Android 0.1-8969-g611bb8fb4**, disable **PGXP Geometry Correction** in
   **Vagrant Story's per-game settings**. See [PGXP compatibility](PGXP.md).
8. Start the game again and check dialogue and a menu.

The Android ZIP's internal layout is:

```text
textures/
  SLUS-01040/
    replacements/
      (103 PNG files)
```

The first folder must be `textures`; an extra outer folder can produce
“No importable files were found.” The layout and accepted image types were
checked against Android 0.1-8969's importer. That importer does not recognize
`config.yaml`, so the Android archive contains images only. The texture IDs
work without that optional file.

Published v0.2 through v0.4 packs can be upgraded by importing this ZIP.
If you installed one of our **experimental menu/UI packs**, back it up and
start with a clean `textures/SLUS-01040/replacements` folder: some old rectangle
filenames were replaced, and importing a ZIP does not remove obsolete files.
Avoid combining overlapping packs for the same fonts.

## Desktop

Stop the game. Extract **vagrant-story-font-v0.6-desktop.zip**, then place its
**SLUS-01040** folder in the DuckStation data directory's **textures** folder.
Enable Texture Cache and Texture Replacements with a hardware renderer.
Set both **Texture Filtering** and **Sprite Texture Filtering** to
**Nearest Neighbor**, then restart the game.

Back up an existing replacement folder before replacing an experimental or
overlapping pack. Texture dumping and VRAM Write Replacements are not required.
Disable texture replacements to return to native lettering.

For local edits, DuckStation's texture-reload command can refresh replacements
without rebooting the game.

An independent PPF weapon/control mod can be used alongside this pack. A disc
patch that changes the native font needs separate compatibility testing.


## Troubleshooting

- **No importable files:** import the Android ZIP without extracting it. Its first folder must be `textures`.
- **Blurry letters:** set both texture filters to Nearest Neighbor and restart.
- **Bands or offset menu text:** see [PGXP compatibility](PGXP.md).
- **Unchanged font:** check USA serial SLUS-01040, hardware rendering, Texture Cache and Texture Replacements.
