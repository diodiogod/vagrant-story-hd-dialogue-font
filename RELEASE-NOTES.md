# v0.5 beta — Original Style HD Fonts

- 66 more text sprites: combat/status notices, equipment and affinity popups, and interaction labels.
- Sharper BATTLE MODE, WAITING for COMMAND, WORKSHOP, NUM., Locked, Container, Open and Unlockable.
- Native colours, dark surrounds and animation dimming retained; word spacing checked in the renderer.

**101 PNGs at 8x.** Dialogue and non-text artwork are unchanged.
[Visual comparisons](CHANGELOG.md).

Import the **Android ZIP** through **Transfer Data → ZIP file → Import** without extracting it.
Extract the **Desktop ZIP** into DuckStation's textures folder. Published v0.2–v0.4
packs can be upgraded by import; remove obsolete experimental replacements first.

Keep **both texture filters on Nearest Neighbor**. On Android **0.1-8969**, disable
**PGXP Geometry Correction** for this game. The new text passed controlled Windows
render checks; Android and broader gameplay checks remain pending.

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
