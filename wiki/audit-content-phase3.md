---
type: report
title: Content Audit — Phase 3 (Academic Substance)
status: remediated
date: 2026-10-12
tags:
  - audit
  - content
---

# Content Audit — Phase 3: Academic Substance

Three-phase content audit of the IR Study Companion curriculum (~332k words, 157 content chapters).

- **Phase 1** (structural integrity) — DONE, commit `5c5caad`.
- **Phase 2** (answer-key integrity + option-position bias) — DONE, commit `94e6730`.
- **Phase 3** (academic substance) — this report. 157 chapters reviewed by 6 parallel auditors (4 axes: accuracy, depth, attribution, coverage); every FAIL independently reproduced by the orchestrator before remediation.

## Verdict summary

| Verdict | Chapters | % |
|---|---|---|
| PASS | 122 | 78% |
| MINOR | 22 | 14% |
| FAIL (fixed) | 13 | 8% |
| **Total** | **157** | |

## FAIL findings — all fixed this session

| # | Chapter | Axis | Defect → Fix |
|---|---|---|---|
| 1 | `_chapters/012-modern-world-history/160-birth-prc.md` | attribution | Fabricated source "The Podgorskis" → re-expressed in course voice, attribution removed |
| 2 | `_chapters/013-indonesia-political-perspective/020-political-institution.md` | accuracy | Inverted constitutional chronology (1959 called parliamentary) → 1945 presidential; 1950–59 parliamentary; 1959 decree reinstated 1945; direct election 2004 |
| 3 | `_chapters/013-indonesia-political-perspective/030-evolution-party.md` | accuracy | 1945 called parliamentary; 1955 parties miscategorised; Megawati called Suharto's successor; "3 parties 2004" → corrected all four |
| 4 | `_chapters/023-theories-of-international-relations/060-dependency-theory.md` | attribution | "Marx's theory of imperialism" → Leninist theory of imperialism + dependency (Prebisch/Frank/Amin) |
| 5 | `_chapters/032-diplomacy-and-international-politics/020-history-diplomacy.md` | accuracy | Dante/Petrarch/Boccaccio called 15th-c resident ambassadors → 14th-c ad-hoc envoys; Richelieu 1600 → 1624–42 |
| 6 | `_chapters/041-foreign-policy-of-developed-countries/010-history-evolution-fpa.md` | accuracy | FPA emerging late 1980s, journal 1991 → 1950s–60s; journal 2005 (ISA) |
| 7 | `_chapters/043-international-political-economy-of-development/060-dev-china-india-chile-african-arab.md` | depth | Identical 7-point boilerplate ×5 regions → region-specific histories |
| 8 | `_chapters/045-international-organization-in-international-relations/030-evolution-IO.md` | accuracy | Danube 1856 "after" 1870–71 war; council 1838 "after" 1853–56 war → dates re-aligned |
| 9 | `_chapters/045-international-organization-in-international-relations/060-IMF-world-bank.md` | coverage | Title promises World Bank; body IMF-only → added full World Bank Group section |
| 10 | `_chapters/046-global-economic-architecture/030-economic-hegemony.md` | accuracy | China largest GDP / US largest PPP (inverted) → US nominal, China PPP |
| 11 | `_chapters/050-wto-and-trade-diplomacy/020-transformation-diplomacy-trade.md` | coverage | "Three transformations" never stated → three explicit transformations |
| 12 | `_chapters/050-wto-and-trade-diplomacy/040-evolution-global-trade.md` | coverage | "Silk Road" title, no Silk Road; duplicated 010/020 → full historical-evolution narrative |
| 13 | `_chapters/050-wto-and-trade-diplomacy/060-judicial-procedure-wto.md` | accuracy | WTO/NAFTA can "override domestic law" → rulings obligate conformity, retaliation on non-compliance |

## MINOR findings — outstanding (not yet remediated)

| # | Chapter | Axis | Issue |
|---|---|---|---|
| 1 | `_chapters/010-Introduction-to-IR/040-basic-liberalism.md` | accuracy | Claims League of Nations members had automatic obligation to provide military support, whereas Article 16(2) limited Council to recommending troop contributions. |
| 2 | `_chapters/012-modern-world-history/070-twenty-year-crisis.md` | accuracy | Claims League Council made decisions by majority vote, contradicting Covenant Article 5(1) unanimity requirement and internal text. |
| 3 | `_chapters/012-modern-world-history/120-domino-cold-war.md` | accuracy | Anachronistically asserts NATO was created in April 1949 to counterbalance Warsaw Pact, which was not established until May 1955. |
| 4 | `_chapters/012-modern-world-history/150-decolonization.md` | accuracy | Claims 1947 Madagascar uprising was against French Vichy rule, whereas Vichy regime collapsed in 1944 and Madagascar was liberated in 1942. |
| 5 | `_chapters/013-indonesia-political-perspective/050-electoral-indonesia.md` | accuracy | Claims DPD seat allocation depends on population; Article 22C(2) mandates equal representation (4 members) per province. |
| 6 | `_chapters/013-indonesia-political-perspective/060-democracy-indonesia.md` | accuracy | Erroneously claims 1957 local administration law eliminated local assemblies and heads of government. |
| 7 | `_chapters/013-indonesia-political-perspective/070-women-indonesia.md` | accuracy | Claims elections were held every 5 years after 1955, and misstates the 30% quota as reserving parliamentary seats rather than candidate lists. |
| 8 | `_chapters/013-indonesia-political-perspective/080-religion-society.md` | accuracy | Contradicts earlier section by claiming 2010 Medan mayoral election rivals Sofyan Tan and Rahudman Harahap aligned together. |
| 9 | `_chapters/021-international-political-economy/040-GATT.md` | accuracy | Comparison table asserts GATT had no dispute settlement mechanism despite Articles XXII/XXIII panel practice. |
| 10 | `_chapters/021-international-political-economy/050-TPP-RCEP.md` | accuracy | Falsely claims TPP lacked explicit SME mechanisms despite dedicated Chapter 19. |
| 11 | `_chapters/021-international-political-economy/060-trade-politics.md` | accuracy | Inverts Sector Model assumption, asserting factors of production are mobile between industries within a country. |
| 12 | `_chapters/022-introduction-to-security-studies/060-peace-operations.md` | accuracy | Cites colonial partition of Bengal and Dayton-brokered Bosnian statehood as rebel ethnic military victories. |
| 13 | `_chapters/031-international-relations-research-method/020-research-method-ir-study.md` | accuracy | Mischaracterizes classical realist Hans Morgenthau as positivist in orientation emulating natural sciences, whereas Morgenthau was a traditionalist critic of positivism. |
| 14 | `_chapters/033-foreign-policy-analysis-in-international-relations/040-factors-fpdm.md` | accuracy | False factual claim attributing 9/11 terrorism to North Korea in George W. Bush post-9/11 speech |
| 15 | `_chapters/041-foreign-policy-of-developed-countries/050-australia-foreign-policy.md` | accuracy | Outdated factual claim stating Liberal Party is current party in government (ALP in power since May 2022) |
| 16 | `_chapters/041-foreign-policy-of-developed-countries/070-japan-foreign-policy.md` | accuracy | Geographical error stating Yasukuni Shrine is located in 'Yasukuni, Japan' (located in Chiyoda, Tokyo) |
| 17 | `_chapters/042-international-law-issues-and-international-dispute-settlement/050-io-law.md` | accuracy | UN Charter domestic jurisdiction clause Article 2(7) erroneously placed in Chapter V instead of Chapter I |
| 18 | `_chapters/042-international-law-issues-and-international-dispute-settlement/060-territory-law.md` | coverage | Falkland Islands maritime/island dispute cited under International Boundary Rivers section heading |
| 19 | `_chapters/042-international-law-issues-and-international-dispute-settlement/091-IC-tribunal.md` | accuracy | Erroneously states parties are not obligated to comply with ICJ rulings, contradicting UN Charter Art 94(1) |
| 20 | `_chapters/042-international-law-issues-and-international-dispute-settlement/092-force-law.md` | accuracy | Claims UNSC Resolution 688 authorized member states to use force/intervene in Iraq; 688 had no Chapter VII force authorization |
| 21 | `_chapters/043-international-political-economy-of-development/050-asian-model.md` | coverage | Off-topic drift into US domestic demographic diversity of Asian Americans within chapter on Asian development model |
| 22 | `_chapters/045-international-organization-in-international-relations/050-UN-security.md` | accuracy | Factual date errors: claims UN General Assembly adopted Arms Trade Treaty in 2006 (adopted 2013) and ICTY established in 1994 (established 1993). |

## Verification (post-remediation)

- pytest 369/369 PASS
- Jekyll build OK
- Every FAIL fix re-checked by orchestrator via grep + re-read
- 13 files changed, all under `_chapters/`; frontmatter/slug/quiz/flashcard Liquid untouched

## MINOR remediation (2026-10-12)

All 22 MINOR findings were corrected in a second pass (3 file-disjoint workstreams). Fixes: League Art 16(2) Council-recommendation not automatic obligation (010/040); League Council unanimity per Art 5(1) (012/070); NATO 1949 not countering a 1955 Warsaw Pact (012/120); post-Vichy Malagasy uprising (012/150); DPD equal representation per Art 22C(2) (013/050); UU 1/1957 expanded local councils (013/060); 1955→1971 election gap + 30% as candidate-list quota (013/070); Medan rivals not aligned (013/080); GATT had Art XXII/XXIII dispute settlement (021/040); TPP had an SME chapter (021/050); Ricardo-Viner = specific/immobile factors (021/060); Bengal partition / Dayton Bosnia are not ethnic rebel military victories (022/060); Morgenthau = traditionalist critic of positivism (031/020); post-9/11 rhetoric not "North Korea as cause" (033/040); ALP in government since May 2022 (041/050); Yasukuni in Chiyoda, Tokyo (041/070); Art 2(7) is in Chapter I (042/050); Falklands moved to Island & Maritime Disputes (042/060); ICJ rulings binding per Art 94(1) (042/091); UNSCR 688 not Chapter VII / no force authorization (042/092); US-demographics digression replaced with developmental-state model (043/050); ATT 2013 and ICTY 1993 (045/050).

Verification: pytest 369/369 PASS · Jekyll build OK · 22 files changed, all under `_chapters/`; every fix re-checked by orchestrator via grep + context read.
