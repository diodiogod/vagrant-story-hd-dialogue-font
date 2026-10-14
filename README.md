# Vagrant Story Original Style HD Dialogue Font

An 8x dialogue font texture pack for **DuckStation** and **Vagrant Story USA,
SLUS-01040**. Reconstructed from the original glyph shapes to retain the game's
italic lettering, broad capitals and small-cap dialogue style with sharper edges.

**[Download v0.2 beta](https://github.com/diodiogod/vagrant-story-hd-dialogue-font/releases/tag/v0.2-beta)**

- [Android ZIP Import](https://github.com/diodiogod/vagrant-story-hd-dialogue-font/releases/download/v0.2-beta/vagrant-story-font-v0.2-android.zip) — import directly; leave zipped.
- [Desktop texture pack](https://github.com/diodiogod/vagrant-story-hd-dialogue-font/releases/download/v0.2-beta/vagrant-story-font-v0.2-desktop.zip) — extract into DuckStation's textures folder.

![Windows gameplay test](assets/windows-dialogue-v0.2.png)

## Status: v0.2 beta

- 123 reconstructed glyphs: digits, capitals, small capitals, accents and punctuation.
- Seven original palette variants supported.
- Original character advances, line wrapping and game image unchanged.
- Windows: observed in two opening-scene dialogue bubbles on DuckStation
  0.1-12083-g00e299795, 5x internal resolution.
- Android: ZIP import and sharp dialogue rendering confirmed by the maintainer
  on 0.1-8969-g611bb8fb4 with both texture filters set to **Nearest Neighbor**.
  The device model was not recorded; this is a user-reported test, not a
  full-game or all-device compatibility claim.
- Menus using the other font table and controller icons retain their original art.
- This is not a complete playthrough test or a guarantee for other regions.

The reconstruction interprets the original small bitmaps; it does not recover
an unavailable original high-resolution master.

## Install on Android

1. Download **vagrant-story-font-v0.2-android.zip** from the
   release assets and copy it to your phone. **Leave it zipped.**
2. Fully stop the running game in DuckStation.
3. Open **Transfer Data → ZIP file → Import** and select that ZIP file.
4. Choose **Textures** if import categories are offered. The archive contains
   exactly seven font images, with no settings, memory cards or save states.
5. In the game's graphics settings, enable **Texture Cache** and **Texture
   Replacements**. Use a hardware renderer, such as Vulkan, and your usual
   internal resolution (4x/5x recommended for viewing the sharper letters).
6. Set **Texture Filtering → Nearest Neighbor** and **Sprite Texture Filtering
   → Nearest Neighbor**. Set both: this was necessary for the successful test
   on Android 0.1-8969.
7. Start the game again and check a fully visible dialogue bubble.

The ZIP's internal layout is:

```text
textures/
  SLUS-01040/
    replacements/
      (seven PNG files)
```

The first archive folder must be `textures`: an extra outer folder causes the
ZIP importer to find no matching files. The direct-import layout and accepted
PNG file type were verified against the original Android 0.1-8969 APK.
The maintainer confirmed successful import and rendering on this Android build.
The importer does not accept the pack's optional dumping/configuration YAML;
this archive contains the seven images only. Its texture identifiers work
without that YAML. Enable the cache and replacements in the app as above.

## Install on desktop

Download the standard ZIP, then place its **SLUS-01040** folder inside the
DuckStation data directory's **textures** folder. Enable Texture Cache and
Texture Replacements, use a hardware renderer, and restart the game.
Set both **Texture Filtering** and **Sprite Texture Filtering** to
**Nearest Neighbor** for the intended crisp appearance.

Texture dumping and VRAM Write Replacements are not required by this pack.

This texture pack can be used alongside an independent PPF weapon/control mod.
Another disc patch that changes the native font needs separate compatibility
testing. Disable texture replacements to return to the native lettering.

## Troubleshooting

- **Imported but the font looks wrong or blurry:** set both Texture Filtering
  and Sprite Texture Filtering to Nearest Neighbor, then restart the game.
  The Android test only worked as intended after both were reset to Nearest.
- **No importable files were found:** select the Android ZIP Import download
  using ZIP file import, with no extraction. Its first folder is `textures`.
- **The font remains unchanged:** check USA serial SLUS-01040, a hardware
  renderer, Texture Cache and Texture Replacements, then restart the game.
- This pack replaces dialogue lettering; native-looking menu text is expected.

## Roadmap

- Reconstruct the **menu font in HD with the same fidelity to the original**.
  This is planned future work and is not included in v0.2.
- Refine individual glyphs, spacing or palette cases reported during gameplay.
- Gather more device/renderer and later-game dialogue testing before a stable release.

## Comparison and method

![Controlled comparison, not an emulator screenshot](assets/style-comparison.png)

The glyphs were reconstructed with AI-assisted image editing in five batches
of 20 and one batch of 23, then reviewed beside the original glyphs and fitted
to their original dimensions. The style direction was reviewed and approved
by the pack maintainer. Exact image-editing prompts are in
[editing-prompts.json](editing-prompts.json).

Texture IDs, palette IDs, PNG dimensions, original glyph bounds, untargeted
cells and archive integrity were checked. [verification.json](verification.json)
distinguishes these asset checks from the limited gameplay test.

## Credits and related projects

- Original Vagrant Story game art and typography: Square / original rights holders.
- Font direction, selection and Windows/Android gameplay testing:
  [diodiogod](https://github.com/diodiogod).
- Image reconstruction and pack tooling: AI assistance through OpenAI Codex
  and its built-in image-editing tool.
- Font layout research: [HilltopWorks/VagrantStory-Font](https://github.com/HilltopWorks/VagrantStory-Font).
- Character mapping and renderer research: [rood-reverse](https://github.com/ser-pounce/rood-reverse).
- Emulator and texture replacement: [DuckStation](https://github.com/stenzek/duckstation/wiki/Texture-Replacement).

Other Vagrant Story font mods and HD packs exist, including Hilltop's font
patch and [1vierock's Beetle PSX HD pack](https://www.vierockhd.com/ps1/vagrant-story-hd).
This project makes no claim to be the first HD font modification.

This is an unofficial fan modification. Original game material is not claimed
as newly owned work. No game image, BIOS or emulator is distributed here.

## Feedback

Report the game region/serial, DuckStation version, device/renderer, and the
dialogue or character affected. A screenshot of a spacing, accent, colour or
missing-glyph problem helps identify the specific texture or glyph to refine.
