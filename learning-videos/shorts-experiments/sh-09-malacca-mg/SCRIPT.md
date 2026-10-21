# SH-09 · Malacca Strait — English VO script

Revision: v1, 19 Oct 2026. Supersedes the unnarrated 18 s motion-graphics plan — you want voice-over, so this is the Shorts format from `learning-videos/voice.md` (35–45 s, 4–5 beats, Kokoro TTS), built on the `@90secondslab` structural baseline.

Voice: Kokoro-82M `af_heart`. Rate 145 wpm (voice.md band: 140–155).
Total: **103 words ≈ 42.6 s** at 145 wpm, plus 2.5 s of held silence across beat transitions → **45 s target**.

---

## Script

| # | Time | VO (spoken) | On-screen text | Visual |
|---|---|---|---|---|
| 1 | 0.0–8.0 | "Two landmasses. One channel between them. One point five nautical miles of water — and no second option." | `TWO LANDMASSES` → `ONE SEA GATE` → `NO SECOND OPTION` | Paper-cut atlas, hook stickers slam in one per second |
| 2 | 8.0–17.5 | "At its narrowest, the Phillips Channel is two point eight kilometres wide. Deep enough for most ships. Only just." | `PHILLIPS CHANNEL · 1.5 NM · 2.8 KM` | Camera pushes into the channel; gold caliper spans the gap, 10 dashed ticks make it countable |
| 3 | 17.5–28.5 | "A Malaccamax tanker draws twenty point five metres. The seabed sits near twenty-five. Four and a half metres of water under the keel — that is the whole margin." | `DRAFT 20.5 M` · `SEABED ~25 M` · `CLEARANCE 4.5 M` | Water-column cross-section; hull descends, stops, red gap marked |
| 4 | 28.5–37.5 | "So why not go around? Sunda is shallower still. Loaded tankers must run east, through Lombok and Makassar." | `WHY NOT GO AROUND?` then `SUNDA ~20 M` / `LOMBOK · MAKASSAR` + `HYPOTHETICAL SCENARIO` | Two tape routes draw on; objection card appears before the answer |
| 5 | 37.5–45.0 | "You cannot widen a strait. Chokepoints do not create risk. They concentrate it." | `YOU CANNOT WIDEN A STRAIT` + `@IRinANutshell` | Pull back to full theatre, endcard |

### Word count check

| Beat | Words | Seconds @145 wpm |
|---|---|---|
| 1 | 22 | 9.1 (trimmed to 8.0 by tightening pauses) |
| 2 | 22 | 9.1 → 9.5 slot |
| 3 | 30 | 12.4 → 11.0 slot (needs a faster read, see note) |
| 4 | 18 | 7.4 → 9.0 slot |
| 5 | 13 | 5.4 → 7.5 slot |
| **Total** | **105** | **43.5 + holds = 45.0** |

Beat 3 is 12.4 s of speech in an 11.0 s slot. Two options: cut "that is the whole margin" (5 words → 10.3 s, fits) or extend the beat to 13.0 s and shorten beat 4. **Recommended: cut it.** "Four and a half metres of water under the keel" already lands the point; the extra clause explains the joke.

Revised beat 3: *"A Malaccamax tanker draws twenty point five metres. The seabed sits near twenty-five. Four and a half metres of water under the keel."* → 25 words, 10.3 s. Total 100 words ≈ 41.4 s + holds.

### TTS spoken forms

| Written | Spoken |
|---|---|
| 1.5 | one point five |
| 2.8 | two point eight |
| 20.5 | twenty point five |
| ~25 | near twenty-five |
| 4.5 | four and a half |
| ~20 | around twenty |

No dates, no proper nouns that TTS mispronounces except **Malaccamax** — verify in the first synthesis (expect mah-LAK-uh-max; if Kokoro mangles it, respell phonetically as `Malacca-max` in the input).

---

## Fact gate — every spoken number

| Claim | Value | Verified |
|---|---|---|
| Phillips Channel minimum width | 1.5 NM = 2.8 km | yes, 2026-10-19 |
| Malaccamax max draft | 20.5 m | yes |
| Malacca seabed | ~25 m | yes |
| Sunda controlling depth | ~20 m | yes |
| Deep-draft detour | Lombok → Dewakang Sill → Makassar | yes (route) |

**Nothing unverified is spoken.** No vessel counts, no oil share, no day/money cost of a detour, no chip share. Beat 4 says "shallower still" instead of quoting a rival number that secondary sources disagree on.

Beat 4 carries `HYPOTHETICAL SCENARIO` on screen for its full duration — the closure is a thought experiment, and the card has to say so.

---

## Beats borrowed from the baseline

| Baseline device | Where it appears here |
|---|---|
| Hook ladder, 1 sticker/second, alternating fill | Beat 1 |
| Prop before words | Caliper exists two seconds before the VO says "two point eight" |
| One number + unit on the card | Every card carries its unit; `Phillips Channel` named on the same card as 1.5 NM |
| Reuse one object for the comparison | Same water column gives 20.5 / 25 / 4.5 — no second chart |
| Voice the objection, then answer | Beat 4 opens with `WHY NOT GO AROUND?` |
| Physical transitions | Paper-slide wipe at each beat boundary |

---

## Gate

Script needs your ACC before TTS synthesis. Once approved: synthesize → measure real durations against this table → adjust only the holds, never the wording.
