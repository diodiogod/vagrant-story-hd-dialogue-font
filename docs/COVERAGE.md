# Font coverage and roadmap

Updated 2026-10-17. v0.6 beta: 103 PNGs, all at 8x.
Coverage describes reconstructed assets, separately from where they were tested.

## Rough progress estimate

**Rough progress: 90% of planned font/text work.** Other UI artwork comes later.

| Group | Reconstructed | Remaining work |
| --- | --- | --- |
| Dialogue bank | 123 glyphs, seven palettes; v0.2 unchanged | Low opening quote, long dash and plus remain native; broader dialogue/palette testing |
| Menu bank | 145 glyphs in the selected smooth design | Music note, Lv. and tilde; broader title/save/name-entry testing |
| Value numbers | 10 small and 10 large digits; dark surround restored | More natural scenes and palette cases |
| Unknown values | Small and large source designs | Natural game-screen validation |
| Compact UI alphabet | 26 capitals, 10 digits with restored native surrounds; 16 punctuation marks | Broader natural-screen and Android testing |
| Fixed labels | HP, MP, RISK, WT, COMMAND, MENU, WARNING, HELP, CAUTION, CHECK, INFORMATION, INFO, TIME, SAVE, CLEAR, MAP | Other baked text listed below; remaining fixed-label surround review; WT surround needs a natural-scene check |
| New fixed words and popups | 66 sprites: notices/interactions, equipment/body/affinity popups, combat/status and spell labels | Natural-event, remaining palette and Android checks |
| Affinity popup signs | Separate +/− with square native-colour surrounds | Android confirmation of this correction |
| Material initials | All seven, with metallic shading, dark borders and native-sized footprints | Broader natural equipment scenes and Android testing |
| Save text | NO. and save-time colon, captured in the memory-card load scene | Broader save/load testing |
| Current/max separator | Round dot with dark surround | Artist's intended dot/diamond shape remains ambiguous |
| CPU-composited text | Rendering path identified | Investigate text that may bypass ordinary glyph replacement |

## Next: remaining text

1. Tutorial copies, loading messages, time-attack/results and rank/score sheets.
2. Lv., tilde, low opening quote, long dash and plus in the remaining rare cells.
3. Natural combat/workshop/title/save/name-entry scenes and Android testing.
4. WT's natural-scene surround check and the INFORMATION framebuffer ghost.

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

All seven material initials were checked in 14 Windows draw instances at native
and enlarged sizes, with no changes outside those regions. The normal equipment
screen shows Hagane H. Their Android check remains pending.

All 66 new sprites appeared in controlled Windows renderer tests, including
coloured affinity popups and two combat-text phases. Matching-frame comparisons
show no changed pixels outside the edited text quads. Natural events, every
palette and a full playthrough remain unverified.

Selected Windows dialogue, menu, workshop and HUD scenes were inspected with
DuckStation 0.1-12083, Vulkan 5x and both filters Nearest. Matching-frame tests
checked preservation outside selected edited text. Sixteen compact symbols
were visible in a controlled real-renderer test. Small/large unknown values remain source-reviewed only. NO. and the save-time
colon are visible in the new memory-card load capture.

The maintainer reports expanded-menu use on Android 0.1-8969 and the PGXP
compatibility issue. This is not a complete phone playthrough or a capture
bound to every final file hash. See [PGXP compatibility](PGXP.md) and the
[verification summary](../verification.json).
