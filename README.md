# Vagrant Story HD Fonts & UI

An 8× texture pack for **DuckStation · Vagrant Story USA (SLUS-01040)**.
Sharper dialogue, menus and HUD text, guided by the original lettering.

## Choose your edition

<!-- downloads:start -->
**v0.11 beta**

| Edition | What changes | Android | Desktop |
| --- | --- | --- | --- |
| **HD Fonts** | Dialogue, menus, HUD, combat and boss-results text; original pixel artwork | [ZIP](https://github.com/diodiogod/vagrant-story-hd-dialogue-font/releases/download/v0.11-beta/vagrant-story-fonts-v0.11-android.zip) | [ZIP](https://github.com/diodiogod/vagrant-story-hd-dialogue-font/releases/download/v0.11-beta/vagrant-story-fonts-v0.11-desktop.zip) |
| **HD Fonts + UI Art** · WIP | The same fonts, plus material badges, body silhouettes, controller prompts, menu markers, arrows and expressions, and WIP equipment/category badges | [ZIP](https://github.com/diodiogod/vagrant-story-hd-dialogue-font/releases/download/v0.11-beta/vagrant-story-ui-art-v0.11-android.zip) | [ZIP](https://github.com/diodiogod/vagrant-story-hd-dialogue-font/releases/download/v0.11-beta/vagrant-story-ui-art-v0.11-desktop.zip) |
<!-- downloads:end -->

Both editions share the same fonts. The original pixel art is part of the game's
character, so our sprite interpretations stay optional. [Art direction](docs/ART-DIRECTION.md).

![HD dialogue and edition comparison](assets/cover-v0.7.png)

## What's new

- HD boss-results headings, score digits, bonus labels and rank names.
- Included in both editions; existing UI artwork stays unchanged.

**Rough font/text progress: 90%.** Remaining menu icons and decoration are still in progress.
[Roadmap](docs/COVERAGE.md) · [Release notes](RELEASE-NOTES.md) · [Visual changelog](CHANGELOG.md).

## Install

**Install one edition.** When switching, remove the previous replacement files
first—importing another ZIP does not remove its artwork. [Switching editions](docs/INSTALL.md#switching-editions).

### Android

1. Download your edition's **Android ZIP** and leave it zipped.
2. Stop the game, then use **Transfer Data → ZIP file → Import**. Choose **Textures** if asked.
3. Enable **Texture Cache** and **Texture Replacements** with a hardware renderer.
4. Set **Texture Filtering** and **Sprite Texture Filtering** to **Nearest Neighbor**.
5. Restart the game. Try 4×/5× internal resolution.

**Android 0.1-8969:** turn off **PGXP Geometry Correction** for this game to avoid
distorted menu letters. [Compatibility](docs/PGXP.md).

### Desktop

Extract your edition's **Desktop ZIP** into DuckStation's `textures` folder,
giving you `textures/SLUS-01040/replacements/`. Enable **Texture Cache** and
**Texture Replacements**, set **both texture filters to Nearest Neighbor**,
and restart the game. [Installation help](docs/INSTALL.md).

## Screenshots

![Equipment menu with v0.9 HD fonts, badges, cursor and controller prompt](assets/equipment-v0.9.png)

![Dialogue font comparison](assets/style-comparison.png)

[UI borders](docs/images/compact-ui-labels-v0.4.png) · [Menu heights](docs/images/font-heights-preview.png) · [Save labels](docs/images/save-labels-preview.png)

[Boss results](docs/images/results-v0.11.png) · [Combat text](docs/images/combat-labels-v0.5.png) · [Word spacing](docs/images/combat-spacing-v0.5.png) · [Fixed labels and popups](docs/images/fixed-labels-v0.5.png) · [Affinity signs](docs/images/affinity-signs-v0.5.png)

[Material badges](docs/images/material-badges-v0.6.png) · [Body silhouettes](docs/images/body-silhouettes-v0.7.png)

[Category tabs](docs/images/categories-v0.9.png) · [Equipment and grips](docs/images/equipment-v0.9.png)

[Controller buttons](docs/images/controller-buttons-v0.9.png) · [EQP, SET and attention !](docs/images/menu-markers-v0.9.png) · [Arrows and expressions](docs/images/arrows-expressions-v0.8.png)

## More

[Visual changelog](CHANGELOG.md) · [Coverage and roadmap](docs/COVERAGE.md) · [Compatibility](docs/PGXP.md) · [Testing](docs/TESTING.md) · [Method and credits](docs/CREDITS.md)

Earlier dialogue-only downloads remain in [older releases](https://github.com/diodiogod/vagrant-story-hd-dialogue-font/releases).

For bug reports, include a screenshot, edition, game serial, DuckStation version
and device/renderer settings.

Unofficial fan project. Art direction and interpretation by
[diodiogod](https://github.com/diodiogod). Original art belongs to its rights
holders. No game, BIOS or emulator included.
