# Font coverage and roadmap — v0.3 beta

Updated 2026-10-15. The pack contains 51 PNGs at 8x native resolution.
Coverage describes reconstructed assets, separately from where they were tested.

## Rough progress estimate

**Rough progress: 80% of planned font/text work.** Other UI artwork comes later.

| Group | Reconstructed | Remaining work |
| --- | --- | --- |
| Dialogue bank | 123 glyphs, seven palettes; v0.2 unchanged | Low opening quote, long dash and plus remain native; broader dialogue/palette testing |
| Menu bank | 145 glyphs in the selected smooth design | Music note, Lv. and tilde; broader title/save/name-entry testing |
| Value numbers | 10 small and 10 large digits; dark surround restored | More natural scenes and palette cases |
| Unknown values | Small and large source designs | Natural game-screen validation |
| Compact UI alphabet | 26 capitals, 10 digits, 16 punctuation marks | Broader natural-screen and Android testing |
| Fixed labels | HP, MP, RISK, WT, COMMAND, MENU, WARNING, HELP, CAUTION, CHECK, INFORMATION, INFO | Other baked text listed below |
| Save text | NO. and save-time colon source designs | Natural game-screen validation |
| Current/max separator | Round dot with dark surround | Artist's intended dot/diamond shape remains ambiguous |
| CPU-composited text | Rendering path identified | Investigate text that may bypass ordinary glyph replacement |

The source audit also identified 24 confirmed native text rectangles before
the punctuation update, plus 26 additional text labels by visual inspection.
These are overlapping work lists, not a complete denominator; some of the
confirmed rectangles are now reconstructed. Palette copies are not separate
restoration targets.

## Next: remaining text

1. Restore the fixed-image TIME, SAVE, CLEAR and MAP labels. A word drawn with
   the shared alphabet can already be sharp while a separate baked copy is native.
2. Audit WAITING for COMMAND, EXIT FACTORY, SET EQUIP, WORKSHOP and other fixed words.
3. Restore remaining baked equipment/body/class/element labels such as WEAPONS,
   SHIELD, R.ARM, L.ARM, HEAD, BODY and LEGS. Some live body-part names already
   use the restored alphabet; their separate image copies do not.
4. Finish the six mapped rare menu/dialogue cells listed above.
5. Review equipment/status, workshop, combat messages, title/save/load, name entry,
   maps and later-game scenes, including selected, disabled and coloured text.

For each batch: compare a small native/HD specimen, check common height,
baseline, bearings, counters and stroke weight, preserve the entire dark
surround, then test actual rendering and unaffected graphics. Source hashes
and matching bounds alone do not prove visual fidelity.

## Later: other UI artwork

Body/limb silhouettes, equipment/condition/affinity icons, controller prompts,
arrows, bars and panel decoration need careful individual remakes. They are
not included in the current font work or progress estimate. World and character
textures are outside this project's current scope.

## Test coverage

Selected Windows dialogue, menu, workshop and HUD scenes were inspected with
DuckStation 0.1-12083, Vulkan 5x and both filters Nearest. Matching-frame tests
checked preservation outside selected edited text. Sixteen compact symbols
were visible in a controlled real-renderer test. Small/large unknown values,
NO. and save-time colon remain source-reviewed only.

The maintainer reports expanded-menu use on Android 0.1-8969 and the PGXP
compatibility issue. This is not a complete phone playthrough or a capture
bound to every final file hash. See [PGXP compatibility](PGXP.md) and the
[verification summary](../verification.json).
