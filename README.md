# Vagrant Story HD Fonts & UI

An 8× texture pack for **DuckStation · Vagrant Story USA (SLUS-01040)**.
Sharper dialogue, menus and HUD text, guided by the original lettering.

## Choose your edition

Readability and redrawing artwork are different goals. Keep the original pixel
art with **HD Fonts**, or try our optional sprite interpretations with
**HD Fonts + UI Art**. Both include the same fonts.

<!-- downloads:start -->
**v0.7 beta**

| Edition | What changes | Android | Desktop |
| --- | --- | --- | --- |
| **HD Fonts** | Dialogue, menus, HUD and combat text; original pixel artwork | [ZIP](https://github.com/diodiogod/vagrant-story-hd-dialogue-font/releases/download/v0.7-beta/vagrant-story-fonts-v0.7-android.zip) | [ZIP](https://github.com/diodiogod/vagrant-story-hd-dialogue-font/releases/download/v0.7-beta/vagrant-story-fonts-v0.7-desktop.zip) |
| **HD Fonts + UI Art** · WIP | Same fonts, plus material badges and body silhouettes | [ZIP](https://github.com/diodiogod/vagrant-story-hd-dialogue-font/releases/download/v0.7-beta/vagrant-story-ui-art-v0.7-android.zip) | [ZIP](https://github.com/diodiogod/vagrant-story-hd-dialogue-font/releases/download/v0.7-beta/vagrant-story-ui-art-v0.7-desktop.zip) |
<!-- downloads:end -->

The pixel art is part of the game's character. The art edition offers another
look, based on our interpretation; it is unfinished, with buttons and other
icons still to come. [Art direction](docs/ART-DIRECTION.md).

![HD dialogue and edition comparison](assets/cover-v0.7.png)

![Dialogue font comparison](assets/style-comparison.png)

**Install one edition.** When switching, remove the previous replacement files
first—importing another ZIP does not remove its artwork. [Switching editions](docs/INSTALL.md#switching-editions).

## Install

**Android:** leave the ZIP zipped. Stop the game, then use
**Transfer Data → ZIP file → Import** and choose **Textures** if asked.

**Desktop:** extract the ZIP into DuckStation's `textures` folder, giving you
`textures/SLUS-01040/replacements/`.

Enable **Texture Cache** and **Texture Replacements** with a hardware renderer.
Set **Texture Filtering** and **Sprite Texture Filtering** to **Nearest Neighbor**,
then restart the game. Try 4×/5× internal resolution.

**Android 0.1-8969:** turn off **PGXP Geometry Correction** for this game to avoid
distorted menu letters. [Compatibility](docs/PGXP.md) · [Installation help](docs/INSTALL.md).

Font/text progress: **roughly 90%**. [Coverage and roadmap](docs/COVERAGE.md).
Earlier dialogue-only downloads remain in [older releases](https://github.com/diodiogod/vagrant-story-hd-dialogue-font/releases).

[Visual changelog](CHANGELOG.md) · [Release notes](RELEASE-NOTES.md) · [Testing](docs/TESTING.md) · [Method and credits](docs/CREDITS.md)

Unofficial fan project. Art direction and interpretation by
[diodiogod](https://github.com/diodiogod). Original art belongs to its rights
holders. No game, BIOS or emulator included.
