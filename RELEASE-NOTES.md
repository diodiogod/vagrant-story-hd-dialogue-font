# v0.10 beta — Two more blue icons

### Added

- Two blue UI-art icons using the supplied **version-one** designs: a plant/root-style motif (`item-000-096.png`) and a key-style motif (`item-064-096.png`).

### Changed

- The README equipment screenshot now shows the v0.9 artwork.

HD Fonts remains unchanged at **101 PNGs**. HD Fonts + UI Art has **163 PNGs**;
all 161 previously released textures are unchanged. Artwork remains a work in
progress. The two new sprites retain their original source-cell bindings;
their natural-gameplay uses are unconfirmed.

Art direction and interpretation by diodiogod.

The two new icons passed controlled Windows rendering checks at native and 2x
size. Android device testing remains pending.

Install one complete edition for your platform. Android: import the ZIP without
extracting it through **Transfer Data → ZIP file → Import**, then restart.
Keep both texture filters on **Nearest Neighbor**.

---

# v0.9 beta — Menu artwork progress

- Adds all eight controller prompts: Triangle, Square, Circle, Cross, L1, R1, L2 and R2.
- Adds equipment and grip artwork for Short Grip, Long Grip, Polearm Grip, Crossbow Bolt, Axe & Mace, Great Axe, Staff, Heavy Mace, Helm, Breast Armor, Leggings, Glove / Bare Hands, Accessory and Gem.
- Adds Weapons, Blades, Armor, Gems, Misc and Options category artwork and refreshes Grips / Shields. All eight tabs have orange selected and turquoise inactive states.
- Adds EQP / SET markers and the separate attention **!** symbol.
- Includes an additional Misc source graphic; its natural-gameplay use remains unconfirmed.

Menu artwork remains **a work in progress**. Unfinished sprites retain their
original artwork. Art direction and interpretation by diodiogod; designs combine
local-model work and manual Photoshop editing.

**HD Fonts:** unchanged, 101 PNGs. **HD Fonts + UI Art:** 161 PNGs.
Both editions remain available for Android and desktop. The arrows, paper
balloons, heart and emphasis marks from v0.8 are retained.

All 44 new or updated palette variants passed controlled Windows Vulkan
renderer checks, with no changed pixels outside their draw regions. Source
masters are preserved. The three newest designs and final release archive
still need Android device testing; earlier test reports remain separate.

Install one complete edition. When returning to HD Fonts, remove the previous
artwork files first. [Visual changelog](CHANGELOG.md) · [Testing](docs/TESTING.md).

---

# v0.8 beta — Badge artwork in progress

- **Dagger:** new black silhouette on the turquoise beveled badge.
- **Sword:** scimitar silhouette sized for the regular Sword slot.
- **Great Sword:** separate large-blade silhouette in its correct category slot.
- **Polearm:** spear silhouette with the maintainer's selected details.
- **Crossbow:** diagonal crossbow silhouette on the turquoise equipment badge.
- **Shield:** shield silhouette on the turquoise equipment badge.
- **Grips category:** the maintainer-approved hilt design on the round badge, with gold selected and turquoise inactive variants.
- **Shields category:** round shield badge with gold selected and turquoise inactive variants.
- **Diagonal cursor:** illuminated 3D shape with a visible underside and dark border.
- **Up arrow:** curved arrow-tip silhouette with a continuous gradient.
- **Normal speech bubble:** maintainer-supplied paper texture and black outline.
- **Low speech bubble:** maintainer-supplied wide paper bubble.
- **Spiky speech bubble:** maintainer-supplied burst shape and paper texture.
- **Heart:** maintainer-selected red heart with its white outline.
- **Emphasis marks:** selected three-stroke design with a thicker black border.

Badge artwork remains a work in progress; unfinished icons keep their original
artwork. The badge designs combine the maintainer's local-model generation,
selection/inpainting and manual Photoshop editing.

HD Fonts stays unchanged at 101 PNGs. HD Fonts + UI Art contains 121 PNGs.
The maintainer tested the supplied Android art package and reported it working
well on 2026-10-24. Desktop renderer and package checks also passed.

Install one complete edition. Remove old art files when switching to HD Fonts.

---

# v0.7 beta — Two editions

- **HD Fonts:** the shared dialogue, menu, HUD and combat lettering, with original pixel artwork.
- **HD Fonts + UI Art:** the same fonts, plus HD material badges and new body-status silhouettes.
- Both body poses use maintainer-painted artwork, with opaque black borders and preserved health colours.

Choose one complete edition for Android or desktop. **Remove the previous
pack's artwork files when switching to HD Fonts**, including when upgrading
from v0.6. [Installation](docs/INSTALL.md#switching-editions).

Font assets are unchanged from v0.6. UI artwork remains optional and unfinished.
[Art direction](docs/ART-DIRECTION.md) · [Comparisons](CHANGELOG.md) · [Testing](docs/TESTING.md).

---

# v0.6 beta — Original Style HD Fonts

- HD material initials for Wood, Leather, Bronze, Iron, Hagane, Silver and Damascus.
- Reviewed metallic shading, thick dark borders and original-sized sprite footprints.
- Includes the combat/status text and sharp affinity-popup +/− signs developed for v0.5.

**103 PNGs at 8x.** The preceding 101 font files are unchanged.
[Visual comparisons](CHANGELOG.md).

Import the **Android ZIP** without extracting it, or extract the **Desktop ZIP**
into DuckStation's textures folder. Keep both texture filters on **Nearest
Neighbor**. On Android **0.1-8969**, disable **PGXP Geometry Correction** per game.

All seven badges passed Windows rendering checks at native and enlarged sizes;
the equipment menu was checked too. The new badges still need Android testing.
[Installation](docs/INSTALL.md) · [Testing and known issues](docs/TESTING.md).

---

# v0.5 development — included in v0.6

- 66 more text sprites: combat/status notices, equipment and affinity popups, and interaction labels.
- Sharper BATTLE MODE, WAITING for COMMAND, WORKSHOP, NUM., Locked, Container, Open and Unlockable.
- Native colours, dark surrounds and animation dimming retained; word spacing checked in the renderer.
- Sharp affinity-popup +/− signs with square dark borders.

**101 PNGs at 8x.** Dialogue and non-text artwork are unchanged.
[Visual comparisons](CHANGELOG.md).

Import the **Android ZIP** through **Transfer Data → ZIP file → Import** without extracting it.
Extract the **Desktop ZIP** into DuckStation's textures folder. Published v0.2–v0.4
packs can be upgraded by import; remove obsolete experimental replacements first.

Keep **both texture filters on Nearest Neighbor**. On Android **0.1-8969**, disable
**PGXP Geometry Correction** for this game. The new text passed controlled Windows
render checks. The maintainer tested the preceding package on Android; the
popup-sign correction and broader gameplay checks remain pending there.

The INFORMATION ghost remains unresolved. Tutorial/loading/results text and a
few rare symbols are planned next. [Testing](docs/TESTING.md) · [Installation](docs/INSTALL.md).

---

# v0.4 beta — Original Style HD Fonts

- Added sharp MAP, SAVE, CLEAR and TIME labels.
- Restored dark surrounds on HP, MP, RISK and WT.
- Added a soft grayscale glow to white menu text, including save names.
- Corrected menu spacing, baselines and character heights; refined compact UI font metrics.
- Restored native dark borders on all 36 compact UI letters and digits.

**59 PNGs at 8x.** The seven dialogue textures are unchanged.
[Visual comparisons](CHANGELOG.md).

Import the Android ZIP through **Transfer Data → ZIP file → Import**, without
extracting it. Extract the desktop ZIP into DuckStation's textures folder.
Published v0.2/v0.3 installations can be upgraded by import; remove obsolete
experimental replacements first. [Installation](docs/INSTALL.md).

Set **both texture filters to Nearest Neighbor**. On Android **0.1-8969**, keep
**PGXP Geometry Correction off** for this game. This version was checked in
selected Windows scenes; its complete payload has not been tested on Android.

The faint native-text ghost under INFORMATION remains unresolved. Other fixed
labels and rare glyphs still need work. [Testing and known issues](docs/TESTING.md).

---

# v0.3 beta — Original Style HD Fonts

The dialogue pack now includes menus and selected HUD/UI text: **51 replacement PNGs**.

- 145 menu glyphs; the 123 dialogue glyphs from v0.2 are unchanged.
- HD small/large digits with dark borders, compact UI letters and fixed labels.
- Sharper punctuation, unknown-value marks, NO., save colon and round HP/MP separator.
- New screenshots, installation tips and a roadmap. Rough font/text progress: 80%.

**Set both texture filters to Nearest Neighbor.** On Android **0.1-8969**,
disable **PGXP Geometry Correction for Vagrant Story** to avoid menu-letter
artifacts. Windows 0.1-12083 passed the tested menu with PGXP on.
[Compatibility details](docs/PGXP.md).

Import the **Android ZIP** through Transfer Data without extracting it.
Extract the **Desktop ZIP** into DuckStation's textures folder. Remove old
experimental UI replacements before upgrading; published v0.2 can be upgraded
by import.

USA SLUS-01040 only. Some fixed labels and rare glyphs remain native; testing
is limited to selected scenes. The four new unknown/save sprites still need
natural-scene checks. [Coverage](docs/COVERAGE.md) · [Testing](docs/TESTING.md).

[Previous v0.2 notes](docs/v0.2/RELEASE-NOTES.md).
