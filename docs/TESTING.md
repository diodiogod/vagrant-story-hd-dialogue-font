# Testing

## Unreleased source

Menu metrics are checked across 145 glyphs and all 21,025 pairs at the game's
original advances. The compact UI bank is checked across 36 glyphs and 1,296
pairs, including native kerning. Cap height, x-height and baseline are checked
separately. Accents, descenders and old-style HUD figures retain their roles.
The [height comparisons](../CHANGELOG.md) are font-sheet specimens.

Current Windows rendering was reviewed on the status page with DuckStation
0.1-12083, Vulkan at 5x, both filters Nearest and PGXP on. This is limited scene
coverage. Full-bank rendering and the new pack on Android remain unverified.

**Known issue:** INFORMATION can show faint native lettering underneath the HD
heading after a framebuffer copy. The pack keeps transparency; it does not mask
the background with black. The exact emulator-side cause is still unresolved.

Earlier save-label, HUD-border and neutral-glow scene checks are preserved below.
Their pixel-equality results apply to those earlier pack fingerprints. The
dialogue and old-style HUD digit PNGs are unchanged by the metric corrections.

[Save-label measurements](evidence/save-labels.json) ·
[HUD measurements](evidence/hud-borders.json) ·
[Glow measurements](evidence/save-name-glow.json) · [Visual changelog](../CHANGELOG.md)

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
