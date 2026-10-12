# Austria Mapping Short — V2 design review

Status: DESIGN REVIEW ONLY. Await user ACC before audio, animation and master render.

## Scope
A new experimental 9:16 Short, isolated from V1. Original English narration, chronological map storytelling and restrained visual comedy. Not a claim of matching Madmam or guaranteeing virality.

## Verified diagnosis and corrections
- V1 uses a portrait-centered projection, not the landscape generator inspected separately. Its Austria path is approximately 275 px wide before camera transformation; eyes span about 50 px. The previous landscape-registration diagnosis was unsupported.
- V1 Spain extends beyond the left viewport (bbox x=-281 to 175), so the marriage-expansion payoff is cropped.
- The apparent black sixth cell in the contact sheet is tile padding, not a black frame in the source; a direct sample at 30.5s contains the map.
- Full-sentence captions persist for 4–6 seconds. Map fill changes alone provide little visual causality.
- Current map boundaries are modern. They must not be presented as accurate medieval territorial boundaries. Carinthia is not equivalent to modern Slovenia. Election as emperor does not mean ownership of the entire empire.
- The 976-to-1156 interval is 180 years, not 270. Carinthia's acquisition belongs to 1335, not Rudolf's 1278 action.

## Concept
**Title:** Austria's other weapon: marriage.
**Visual thesis:** A small base becomes a dynasty's network. Conquest earns one decisive beat; marriage receives the contrasting comic payoff.
**Map contract:** Use modern geography only as a visibly labelled locator. Show documented historical acquisitions with pins and dates rather than coloring entire modern states as medieval possessions. True historical boundary fills require a separately sourced dataset.
**Target:** approximately 35–40 seconds; actual runtime measured after synthesis.

## Proposed English script and shot plan
| Time target | Narration | Visual / action |
|---|---|---|
| 0–3s | Austria had a weapon armies couldn't copy: a family tree. | Tight locator close-up on Austria. Sword slides aside; branching family line takes its place. Caption: A FAMILY TREE. |
| 3–7s | In 976, it was a frontier march. In 1156, a duchy. | Two dated pins, 976 then 1156. Border-watch silhouette replaces itself with a ducal crown. Caption chunks follow each clause. |
| 7–12s | Then Rudolf of Habsburg became king of the Romans in 1273. | Election seal lands with a short paper click. Do not recolor the whole Holy Roman Empire as his property. |
| 12–17s | Victory in 1278 brought Austria and Styria under Habsburg control. | Tight local locator. Austria and Styria pins connect. One short battle graphic, then decisive still hold. |
| 17–21s | Carinthia followed in 1335. But conquest wasn't the whole strategy. | New dated pin. Sword exits; empty family branch is left hanging for the next reveal. |
| 21–29s | A marriage in 1477 connected the dynasty to the Burgundian inheritance. Later marriages helped bring the Spanish crowns into the family. | Locator pulls west, fitting destinations fully inside the safe area. Rings connect family branches. Inheritance label, not indiscriminate modern-country fills. |
| 29–36s | The map changed because the family tree did. Sometimes, the wedding was the power move. | Pull back to the completed network. Character glances at the sword, then nudges it offscreen. Hold final line briefly; no sales CTA. |

## Layout / timing rules
- No title pills, glass cards, persistent HUD, sunglasses or decorative glow.
- Subject and expression dominate close-ups. Character scale is independent of map zoom; test at phone-sized preview.
- One focal event per shot. Frame-based deterministic motion only; no CSS transitions.
- Cuts and bounded 8–14-frame camera moves separate events; camera holds during important clauses.
- Captions: 2–6 words per phrase, timed to recorded clause segments. Never claim word alignment from proportional estimates.
- Reserve rightmost 160 px and bottom 350 px from essential content. Caption band around y=1320–1490, verified with a platform-UI overlay.
- Historical dates and labels remain English. Modern-geography locator label stays visible whenever modern boundaries appear.
- Sound: original generated paper/ring/sword foley, quiet under narration, no unlicensed reference audio.

## Fact-check gate before production
Verify 976 march, 1156 duchy, Rudolf's 1273 title, 1278 battle/control distinction, 1335 Carinthia, 1477 marriage and Burgundian inheritance, and Spanish dynastic succession against identifiable sources. Wording above is a proposed script, not a completed historical audit.

## Production after ACC
1. Source audit and lock original script.
2. Synthesize short clauses; record exact sample-based timing.
3. Implement V2 composition without overwriting V1.
4. Render close-up, transition and payoff previews; inspect critically with vision tooling.
5. Render draft MP4, extract actual output samples and inspect transitions, framing, caption/audio timing and full destination coverage.
6. Run TypeScript and repository tests. Record remaining limitations; deliver as prototype, not guaranteed viral output.

## Acceptance criteria
- Spain/Burgundian locator destinations not clipped.
- No present-day state outline falsely described as historical possession.
- Distinct readable expressions at mobile scale.
- Visual actions depict the narrated cause, not merely color changes.
- No unsupported 100% reference-match or quality claims.
