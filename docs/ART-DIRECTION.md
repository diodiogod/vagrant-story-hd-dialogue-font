# Two editions, one font project

The font work aims to make Vagrant Story easier to read while retaining the
character of its lettering: shapes, proportions, spacing, colours and contrast.
Small bitmaps leave room for interpretation, so the result is a reconstruction,
not a recovered original HD font.

Redrawing a sprite involves a different choice. Smooth edges can change the
feel of an image, and the original pixel art is a valid preference. We keep
those changes optional rather than making them a requirement for clearer text.

| | HD Fonts | HD Fonts + UI Art |
| --- | --- | --- |
| Dialogue, menu, HUD and combat text | Shared HD fonts | Same HD fonts |
| Numbers, punctuation and readable +/− signs | HD | HD |
| Material badges (W, L, B, I, H, S, D) | Original | Reinterpreted |
| Body-status silhouettes | Original | Manually painted HD sprites |
| Selected equipment/category badges, arrows and expressions | Original | Reviewed HD artwork; badges WIP |
| Remaining icons, buttons and decoration | Original | Original until individually reviewed |
| World and character textures | Original | Original |

The material initials are treated as badges: their colour, bevel and backing
make them artwork as well as letters. The map's compass lettering also stays
with the artwork rather than the readability work.

## Direction for UI artwork

Keep the original pose, footprint and visual role. Use the detail needed to
recognize the shape at its actual game size. The body diagrams use flat fills
and black outlines; the material badges use graphic metallic shading. Neither
is presented as proof of what the original artists intended.

The art edition is a work in progress. Buttons, controller prompts and other
icons need their own review. Future art changes stay in this edition; font
improvements remain shared. Comparisons go in the [visual changelog](../CHANGELOG.md).

## Releases

Each version offers two complete alternatives, each for Android and desktop.
They come from one shared asset collection and explicit selection manifest,
so font fixes stay synchronized. Users install one edition at a time.

Earlier releases remain available unchanged, including dialogue-only versions.
v0.6 predates the split and includes material badges. To return to original
graphics, use the current HD Fonts package and [remove the old artwork files](INSTALL.md#switching-editions).
