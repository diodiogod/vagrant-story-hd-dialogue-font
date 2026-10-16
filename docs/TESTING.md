# Testing

## v0.5 beta

All 66 new text sprites appeared in controlled DuckStation 0.1-12083 Vulkan
captures at 5x, both filters Nearest, PGXP on. Tests cover 37 combat/status
sprites in steady and bright phases, 20 native word combinations, a Full/HP
adjacency control, and HP +264 / MP −999.

The earlier 29 fixed words were checked too: nine notice quads and 13 calls to
the native affinity-popup routine, covering all 20 equipment/attribute labels
in blue or orange. Pixels outside the text quads match exactly in all four
before/after pairs. These are controlled specimens, not naturally triggered
events or a complete playthrough. All palette uses remain untested.

The maintainer then tested the supplied Android package and reported good
results, with a blurry affinity +. Those separate +/− sprites were still native.
Their correction changes four palette PNGs; the other 97 stay byte-identical.
Thirteen Windows popup instances match outside the sign quads, including the
words and values. The corrected signs use square corners and flat terminals;
their Android check is pending. [Comparison](images/affinity-signs-v0.5.png).

All 46 new/updated rectangle lookup hashes pass the VRAM-word check. Fifteen
regression tests cover transcription, spacing, borders and specific glyph repairs.
The 55 unchanged v0.4 files retain their earlier evidence; four NUM. rectangles
were updated and 42 PNGs added. Dialogue is unchanged.

[Combat render summary](evidence/combat-render-validation.json) ·
[Fixed-label check](evidence/combat-fixed-labels-audit.json) ·
[Comparisons](../CHANGELOG.md).

## v0.4 beta

Menu metrics are checked across 145 glyphs and all 21,025 pairs at the game's
original advances. The compact UI bank is checked across 36 glyphs and 1,296
pairs, including native kerning. Cap height, x-height and baseline are checked
separately. Accents, descenders and old-style HUD figures retain their roles.
The [height comparisons](../CHANGELOG.md) are font-sheet specimens.

The final payload was compared against native and previous HD text on the
equipment page in DuckStation 0.1-12083, Vulkan at 5x, both filters Nearest and
PGXP on. All 144 compact-character/palette surround checks pass; the six static
affinity gauges match the preceding pack across 79,165 pixels. Complete-border
checks cover the four small packing adjustments needed for I/L/X/Y.

The earlier height revision also passed a status-page check; its menu-font
PNGs are unchanged in this release. These are limited scenes. Full-bank rendered
coverage and the complete v0.4 payload on Android remain unverified.

**Known issue:** INFORMATION can show faint native lettering underneath the HD
heading after a framebuffer copy. The pack keeps transparency; it does not mask
the background with black. The exact emulator-side cause is still unresolved.

Earlier save-label, HUD-border and neutral-glow scene checks are preserved below.
Their pixel-equality results apply to those earlier pack fingerprints. The
dialogue and old-style HUD digit PNGs are unchanged by the metric corrections.

[Save-label measurements](evidence/save-labels.json) ·
[HUD measurements](evidence/hud-borders.json) ·
[Glow measurements](evidence/save-name-glow.json) ·
[Compact UI comparison](evidence/compact-ui-renderer.json) · [Visual changelog](../CHANGELOG.md)

## Published v0.3

Windows checks used DuckStation **0.1-12083-g00e299795**, Vulkan at 5x with
both filters Nearest. Selected dialogue, menu, workshop and HUD scenes were
reviewed. Sixteen compact punctuation marks were checked in a controlled
renderer specimen: all 881,876 pixels outside the two text windows were
identical to the preceding pack. A normal HUD/menu frame was also unchanged
by that punctuation update. These checks apply to those scenes and settings.

The maintainer has used the expanded menu pack on **Android 0.1-8969** and
reported the PGXP problem and workaround. Device model and a hash-bound phone
capture were not recorded. Earlier dialogue ZIP import and rendering were
also confirmed on that build. This is limited testing, not all-device or
full-game certification.

The two unknown-value marks, NO. and save-time colon have reviewed source
proofs, but their normal game screens still need capture/testing. Rare glyphs,
some palette effects, title/save/name-entry screens and later-game usage need
broader coverage. Other regions and translations are not verified.

[Verification summary](../verification.json) ·
[Android import details](../verification-android-import.json) ·
[Coverage and remaining work](COVERAGE.md)
