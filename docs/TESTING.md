# Testing

## Unreleased source

The current preview's neutral glow was checked in the Windows memory-card load
scene: all 6,873,424 pixels outside the shared white text areas match the
preceding preview. The comparison includes DATA, LOAD and the save-location name.
The original palette and all visible replacement pixels are grayscale.

Before adding glow, MAP/SAVE/CLEAR/TIME and HP/MP surrounds passed the same
load-scene check against v0.3, with 7,690,007 pixels outside their cells unchanged.
HP/MP/RISK also passed a HUD comparison, with 7,727,216 outside pixels unchanged.
Those label/HUD PNGs are unchanged in the glow preview. WT is source-reviewed only.

NO. and the save-time colon are visible in that load scene. The new pack has
not been tested on Android. Other uses of the shared white palette need review.

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
