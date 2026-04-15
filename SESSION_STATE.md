# ATOLLSPHERE SESSION STATE

## Edition 022 → 023 handoff · Last sweep ~2334 GMT 14 April 2026 · Session resumed 1012 GMT 15 April 2026

-----

## PLATFORM

- Product: AtollSphere · Parent: LS AI Systems · Operator: UK-based, BST (UTC+1)
- Architecture: v1.2.1 · GMT primary · War day: 48 (as of 15 April 2026 1012 GMT)
- CDN note: raw.githubusercontent.com serving v1.1.3. SESSION_STATE.md is governing document. Apply v1.2.1 in full.

-----

## CURRENT EDITION

- Last completed: Edition 022 Evening Sweep · 14 April 2026 · ~2334 GMT
- Next: Edition 023 · GL U expiry trigger 19 April — T-4 days from session resume · Run immediately if IRGC kinetic action confirmed
- Current time at session resume: 1012 GMT 15 April 2026 (BST 1112)

-----

## PDF OUTPUT RULE — MANDATORY (AI-005, IN FORCE ED022)

Every sweep MUST produce a formatted PDF brief as the sweep output.

- The PDF is the ONLY output format. Analysis is NOT resolved in chat.
- PDF format must match the Ed021 reference template exactly (see ARCHITECTURE SPEC below).
- PDF generation is integrated into the sweep — not a separate step.
- Output path: /mnt/user-data/outputs/atollsphere_edition_0NN.pdf
- The build script (build_ed0NN.py) must be updated each edition with the metadata block at the top.

Failure modes to avoid:

- DO NOT write analysis as chat text and then offer to produce a PDF.
- DO NOT produce a PDF that deviates from the architecture spec below.
- DO NOT run a sweep without also producing the PDF.

-----

## PDF ARCHITECTURE SPEC — v1.2.1 REFERENCE (Ed021 is canonical)

These are mandatory structural requirements. Any deviation is a build fault and must be corrected before the session state is updated.

### Page size and margins

- A4 (210 x 297 mm)
- Margins: 15mm left, 15mm right, 14mm top, 14mm bottom
- Usable width: 180mm

### Cover page (page 1) — mandatory elements in order

1. Top confidential stripe: dark navy bar, white 7pt text: CONFIDENTIAL — For Editorial Review Only · AtollSphere · LS AI Systems
1. Title block (NO duplication):
- Line 1: ATOLLSPHERE — Helvetica-Bold 28pt, navy
- Line 2: GSINT INTELLIGENCE BRIEF — Helvetica 14pt, mid-grey
- Line 3: EDITION NNN · EVENING SWEEP — Helvetica-Bold 18pt, navy
- Line 4: DD MONTH YYYY · WAR DAY NN — Helvetica 11pt, mid-grey
- Line 5: Sweep: ~HHMM GMT (BST HHMM) — DD/DD MONTH YYYY — Helvetica-Oblique 9pt, mid-grey
1. Horizontal rule
1. Stats bar — TWO ROWS: labels row first, numbers row second
- Row 1 (labels): CASES ACTIVE | OPEN PREDICTIONS | CRITICAL WINDOWS | ARCHITECTURE
- Row 2 (numbers): N | N | N | v1.2.1
- Light grey background, navy grid
1. Priority alerts section: dark navy header bar, then red bold bullet points
1. Case summary table: CASE | TITLE | TAG | CONF columns
1. PageBreak — cover must never bleed onto page 2
1. NO header bar on cover page
1. NO footer bar on cover page

### Interior pages (page 2 onwards) — mandatory elements

Running header bar (top of every interior page):

- Dark navy bar, white Helvetica-Bold 7pt
- Text: LS AI SYSTEMS    ATOLLSPHERE BRIEF · EDITION NNN · EVENING SWEEP · DD MONTH YYYY

Running footer bar (bottom of every interior page):

- Dark navy bar, white Helvetica 7pt
- Text (SINGLE COMBINED LINE): CONFIDENTIAL — For Editorial Review Only · AtollSphere · LS AI Systems · smarter ai prediction systems · Page N
- This is a SINGLE LINE — not split across two rows

### Time format rule

- GMT always stated first, BST in parentheses
- Format: ~HHMM GMT (BST HHMM) — e.g., ~2334 GMT (BST 0034)
- Applies to sweep timestamp on cover, situation overview, and any time reference in the document

### Section structure (interior, in order)

1. SITUATION OVERVIEW
1. STEP 2 — PREDICTION LOG RECONCILIATION (including CLOSED WINDOW CLASSIFICATIONS)
1. H1 SATURATION CHECK — STANDING RULE
1. CASE A through CASE E (each with Parts 1-6)
1. PREDICTION LOG — RESOLUTIONS THIS EDITION
1. NEW FORWARD FLAGS
1. CARRY-FORWARD FACTS
1. CRITICAL WINDOWS — NEXT EDITION PRIORITIES
1. SOURCES

### Case section structure (Parts 1-6)

Each case opens with a case sub-header bar (navy, tag colour-coded by status) then:

- PART 1 — FACT TABLE (two-column: FACT | SOURCE — TIER · GATE 0)
- PART 2 — INCONGRUITY ANALYSIS (prose, with [FACT]/[INFERENCE]/[PREDICTION] labels, H1 saturation check, AFC steelman)
- PART 3 — HYPOTHESIS SET (three-column hypothesis box with label, probability, body text)
- PART 4 — TRUTH QUALITY CHECK (TQL table: #, TYPE, ASSESSMENT)
- PART 5 — DISCONFIRMATION (two-column: CONFIRMS | CONTRADICTS)
- PART 6 — FORWARD FLAG (flag box with FLAG NNN-X · PRED-NNN-X header)

### Build script architecture (updated Ed022)

- Core layout library: `build_core.py` — do not modify per edition
- Style constants: `styles.py` — do not modify per edition
- Per-edition script: `build_edition_NNN.py` — copy from `build_edition.py` template each edition
- Imports: `from build_core import hr, thin_rule, tag_table, fact_table, hyp_table, disconf_table, flag_block, source_block, make_page_callbacks`
- Imports: `from styles import make_styles, NAVY, TEAL, CHARCOAL, MID_GREY, LIGHT_BG, ROW_ALT, WHITE, RED_TAG, AMBER, GREEN_TAG, MARGIN`

Update these constants at the top of each per-edition script:

```
EDITION   = "023"
DATE_STR  = "DD MONTH YYYY"
SWEEP_STR = "EVENING SWEEP"
GMT_NOW   = datetime.datetime(YYYY, M, D, HH, MM, 0)
```

Output path resolves automatically from EDITION and SWEEP_STR constants.

### Deviation audit (required before finalising each session state)

Before writing the session state, Claude must check ALL of the following:

1. Are all interior pages carrying the running header bar?
1. Is the footer a single combined line on all interior pages only (none on cover)?
1. Is the cover title block free of duplicated strings?
1. Does the stats bar show labels first, numbers second (2-row layout)?
1. Does the cover end with a PageBreak so it never bleeds to p2?
1. Is the time format GMT-first, BST-in-parens?
1. Was analysis output to PDF only — not resolved in chat first?

If ANY check fails: rebuild before updating session state.

-----

## CRITICAL WINDOWS — STATUS AT 2334 GMT 14 APRIL

|Window                                            |Status  |Action                                                                    |
|--------------------------------------------------|--------|--------------------------------------------------------------------------|
|GL U expiry — 19 April                            |T-5 DAYS|PRED-022-C binary. Fetch OFAC directly at 0001 EDT 19 April.              |
|Ceasefire expiry — 22 April                       |T-8 DAYS|PRED-015-A / PRED-022-A. Watch for second-round announcement or extension.|
|IRGC kinetic response to USN blockade             |ROLLING |PRED-022-B. Monitor CENTCOM, UKMTO, IRGC channels.                        |
|Follow-on Yanbu / East-West Pipeline strike       |ROLLING |PRED-022-D. HIGH probability (65-75%). Pipeline restored 7M bpd.          |
|US-China blockade friction (Rich Starry precedent)|ROLLING |PRED-022-E. NEW. Monitor Chinese-flag vessel breaches.                    |
|Macron/Starmer Hormuz coalition meeting — 17 April|T-3 DAYS|Assess whether multilateral mission materialises.                         |

-----

## ACTIVE CASES — POST-EDITION 022

|Case|Title                                                                   |Tag                |Confidence|
|----|------------------------------------------------------------------------|-------------------|----------|
|A   |Islamabad — No Deal / Departure / USN Blockade / Second Round Pending   |ESCALATING         |HIGH      |
|B   |Hormuz — USN Blockade Active / Mine Clearance / Transit <12/day         |ESCALATING         |HIGH      |
|C   |Lebanon — 2,080+ Killed / Washington Framework / No Ceasefire           |ESCALATING         |HIGH      |
|D   |India Oil Waiver — GL 134B NOT ISSUED / GL U Expires 19 April T-5       |ESCALATING         |HIGH      |
|E   |Saudi Aramco — Pipeline Restored 7M bpd / No New Strike / Follow-on HIGH|ESCALATING CRITICAL|HIGH      |

-----

## PREDICTION LOG — OPEN

|Ref       |Flag                                                           |Window          |Status                                         |
|----------|---------------------------------------------------------------|----------------|-----------------------------------------------|
|PRED-001-A|Futures / BETS OFF Act / Section 122 CIT                       |CIT ongoing     |PENDING                                        |
|PRED-002-B|Iran-Oman Hormuz protocol                                      |Monitor         |WATCH                                          |
|PRED-005-A|Section 122 CIT oral arguments                                 |No date         |PENDING                                        |
|PRED-006-A|GCC emergency meeting                                          |Post-ceasefire  |WATCH                                          |
|PRED-008-B|Houthi BAM not activated                                       |Monitor         |DE-ESCALATING                                  |
|PRED-015-A|Formal ceasefire extension before 22 April                     |22 April        |PENDING — No extension announced               |
|PRED-018-E|IRGC follow-on strike on Yanbu before 22 April                 |22 April        |PENDING — No new strike at Ed022 sweep         |
|PRED-020-E|IRGC kinetic or non-kinetic by 15 April                        |15 April        |PENDING — window closes; classify at Ed023 open|
|PRED-021-E|IRGC Aramco/Yanbu posture through 15 April                     |15 April        |PENDING — window closes; classify at Ed023 open|
|PRED-022-A|Second round US-Iran talks before 22 April                     |15-21 April     |PENDING — Nothing scheduled at sweep           |
|PRED-022-B|IRGC kinetic response to USN blockade                          |Through 22 April|PENDING — IRGC vowed response; not executed    |
|PRED-022-C|GL U renewal or successor by 19 April                          |19 April        |PENDING — Low probability (15-25%)             |
|PRED-022-D|IRGC follow-on Yanbu / Petroline strike before 22 April        |Through 22 April|PENDING — HIGH probability (65-75%)            |
|PRED-022-E|Chinese-flag tanker breach becomes US-China diplomatic incident|Through 22 April|PENDING — Rich Starry precedent logged         |

MANDATORY FIRST ACTION ED023: Classify PRED-020-E and PRED-021-E (windows closed 15 April) before any case analysis proceeds.

-----

## PREDICTION LOG — RESOLVED (CUMULATIVE)

|Ref       |Outcome     |Notes                                                                                 |
|----------|------------|--------------------------------------------------------------------------------------|
|PRED-017-A|RESOLVED    |No communique. Both delegations departed Islamabad 12 April.                          |
|PRED-017-C|FAILED      |No Israel ceasefire agreement by 15 April. Op Eternal Darkness continues.             |
|PRED-019-A|RESOLVED    |AMBIGUOUS branch not triggered. Delegations departed, not remained.                   |
|PRED-020-B|KINETIC     |USN DDG transits (11 Apr) + blockade declaration (13 Apr) = kinetic posture confirmed.|
|PRED-020-C|PARTIAL     |Washington talks: framework commitment only. No verifiable ceasefire.                 |
|PRED-020-D|CONFIRMED   |GL 134B absent OFAC at 15 April 0000 EDT trigger.                                     |
|PRED-021-A|RESOLVED    |Departure branch confirmed. Consistent with PRED-017-A / PRED-019-A.                  |
|PRED-021-B|KINETIC     |Formal closure of PRED-020-B binary. Same basis.                                      |
|PRED-021-C|PARTIAL     |Talks at ambassador level, not PM. Confirmation branch: PARTIAL.                      |
|PRED-021-D|CONFIRMED   |GL 134B absent OFAC at 15 April 0000 EDT trigger.                                     |
|PRED-018-B|CONFIRMED   |Hormuz transit far below 15/day threshold throughout window.                          |
|PRED-017-E|CONFIRMED   |Abqaiq struck 8 April. ESA confirmed. (Prior edition.)                                |
|PRED-014-A|CONFIRMED   |Ceasefire extension only. Talks April 26, May 11, June 24. (Prior edition.)           |
|PRED-003-A|RESOLVED    |Iranian delegation attended. 10-point plan tabled. (Prior edition.)                   |
|PRED-012-B|CONTRADICTED|PMM — Entry 001. (Prior edition.)                                                     |
|PRED-013-A|PARTIAL     |Enrichment contradiction surfaced; written plan not formally tabled. (Prior edition.) |
|PRED-013-B|PARTIAL     |Hezbollah unnamed official confirmed non-adherence. (Prior edition.)                  |
|PRED-012-A|PARTIAL     |Trump stated no enrichment; formal framework not confirmed. (Prior edition.)          |
|PRED-010-A|CONFIRMED   |No power plant strikes before ceasefire. (Prior edition.)                             |
|PRED-008-A|CONFIRMED   |Sixth deadline mechanism confirmed. (Prior edition.)                                  |
|PRED-004-A|CONFIRMED   |WSO Colonel recovered alive. (Prior edition.)                                         |
|PRED-002-A|CONFIRMED   |Russia/China vetoed UNSC Hormuz resolution. (Prior edition.)                          |

-----

## KEY FINDINGS — EDITION 022 (~2334 GMT 14 APRIL)

- Islamabad concluded without deal. Both delegations departed 12 April. No communique. PRED-017-A / 019-A / 021-A: DEPARTURE CONFIRMED.
- USN blockade declared 13 April. DDGs Frank E. Petersen Jr. and Michael Murphy in Persian Gulf. Early enforcement gap: up to 4 vessels (including Chinese-owned Rich Starry) breached without interception.
- No IRGC kinetic response to USN confirmed at sweep. IRGC vowed strong response. PRED-022-B pending.
- Lebanon Washington talks completed 14 April. First Israel-Lebanon direct talks since 1993. Joint statement: all sides agreed to launch direct negotiations. No ceasefire. PRED-017-C: FAILED. PRED-021-C: PARTIAL. PRED-020-C: PARTIAL.
- GL 134B NOT ISSUED at 15 April trigger. GL U active through 19 April only. PRED-020-D / PRED-021-D: CONFIRMED.
- East-West Pipeline restored 7M bpd (12 April). Khurais 300K bpd still offline. No new IRGC Yanbu strike confirmed Ed021 to Ed022. Follow-on strike probability: HIGH (65-75%).
- Lebanon death toll updated: 2,080+ killed (Al Jazeera, 14 April). Prior 2,020+ superseded.
- Five new forward flags: PRED-022-A through PRED-022-E.

-----

## CARRY-FORWARD FACTS — NOT RE-VERIFIED SINCE ED022

|Fact                                                    |Last Verified|Note                                                             |
|--------------------------------------------------------|-------------|-----------------------------------------------------------------|
|Abqaiq damage extent (ESA satellite)                    |12 April     |Pipeline restored. Khurais 300K bpd offline. ESA not re-verified.|
|Lebanon killed: 2,080+                                  |14 April     |Al Jazeera. Likely higher — re-verify Ed023.                     |
|GL U active through 19 April                            |14 April     |OFAC direct fetch Ed022. MUST fetch again at 19 April trigger.   |
|OFAC staffing 22 of 40                                  |Ed016        |STALE — do not cite under any circumstances.                     |
|Hormuz transit less than 12/day                         |14 April     |AIS/UKMTO single-source. Re-verify Ed023.                        |
|Aramco Arab Light Yanbu-only liftings                   |11 April     |SPA confirmed. Re-verify Ed023.                                  |
|East-West Pipeline capacity: 7M bpd                     |12 April     |Saudi MoE confirmed restoration. Re-verify Ed023.                |
|Yanbu port berth capacity ceiling: approx 5.9M bpd      |Ed022        |HouseofSaud / S&P Global. Not independently re-verified Ed022.   |
|USN MCM assets: Pioneer, Chief (Sasebo), Tulsa (Bahrain)|14 April     |Naval News. Re-verify Ed023 — vessels en route.                  |

-----

## SYSTEM CHANGE LOG — ACTIVE RULES

|Entry |Rule Summary                                                                                                                                                                                                                                                                                                                                |In Force|
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
|001   |Named-party statement predictions require incentive analysis before C3. LOW-MEDIUM ceiling if no structural incentive.                                                                                                                                                                                                                      |Ed014   |
|AI-001|Case B standing: AFC steelman, H-B2 specified, H6 second-order, disconfirmation thresholds (~54-68/day), confidence justification mandatory.                                                                                                                                                                                                |Ed018   |
|AI-002|Wikipedia Tier 4 only. Leg 1/Leg 2 split mandatory Case A. Tier 4 dependency test mandatory TQL item 4.                                                                                                                                                                                                                                     |Ed019   |
|AI-003|Gate 0.5, H1 saturation check, PCP Step 1.5, claim-type labelling [FACT]/[INFERENCE]/[PREDICTION], calibration audit Ed025, four named failure modes.                                                                                                                                                                                       |Ed019   |
|AI-004|All rule changes logged before in force.                                                                                                                                                                                                                                                                                                    |Ed019   |
|AI-005|PDF brief mandatory at sweep completion. Analysis output to PDF ONLY — not resolved in chat. Format must match Ed021 reference template exactly. Deviation audit mandatory before session state update.                                                                                                                                     |Ed022   |
|AI-006|PART 4 TQL ASSESSMENT mandatory in every case every edition. Four items required: (1) Key assumption, (2) Fragile fact, (3) High-impact uncertainty, (4) Tier 4 dependency test. Ed022 omitted TQL across Cases B-E — logged as error, restored. Omission in any future edition = build fault requiring rebuild before session state update.|Ed023   |

-----

## H1 SATURATION — STANDING FLAG

H1 fired all five cases Editions 019-022. Each Part 2 must explicitly ask: Is H1 correct here or is the framework pattern-matching? Ed022 findings: H6 dominant Cases B/D/E. H3/H5 dominant Case C. H5/H6 dominant Case A. Active through Ed025.

-----

## GATE 0.5 — STANDING CONSTRAINTS

- AIS cluster (MarineTraffic, Kpler, S&P Global, Windward, UKMTO) — single-source for transit volume
- Iranian state media cluster (IRNA, IRIB, Mehr, WANA, PressTV, Fars, Tasnim) — single-source
- Reuters and AP are originating wires — citing outlets are downstream, not independent
- Wikipedia and ACLED — downstream of Tier 1/2 feeds already swept
- LSEG shipping data — single-source for vessel breach/transit counts; treat as AIS cluster

-----

## HYPOTHESIS STATE — POST-EDITION 022

### Case A (Islamabad / Second Round)

- H-A1: Second round before 22 April — 55-65% (DOMINANT)
- H-A2: Ceasefire lapses, no second round — 25-35%
- H-A3: Ceasefire extended / framework emerging — 10-15%

### Case B (Hormuz / Blockade)

- H-B1: IRGC selective passage persists under blockade — 40-55% (DOMINANT)
- H-B2: IRGC kinetic response to USN — 25-35% (UPGRADED from Ed021 10-20%)
- H-B3: Multilateral mission provides partial resolution cover — 10-15%

### Case C (Lebanon)

- H-C1: Framework leads to operational pause — 20-30%
- H-C2: Framework without operational impact — 55-65% (DOMINANT)
- H-C3: Hezbollah escalation / framework collapse — 10-15%

### Case D (India Oil Waiver)

- H-D1: GL U renewal / successor before 19 April — 15-25%
- H-D2: GL U lapses 19 April without renewal — 70-80% (DOMINANT)
- H-D3: Partial successor / different GL format — 5-10%

### Case E (Saudi Aramco / Yanbu)

- H-E1: IRGC restraint continues — 25-35% (DOWNGRADED from Ed021 45-60%)
- H-E2: IRGC follow-on Yanbu / Petroline strike before 22 April — 55-65% (DOMINANT — UPGRADED from Ed021 30-45%)
- H-E3: IRGC displaced response to Aramco as USN proxy — 10-15%

-----

## ED023 MANDATORY SWEEP ACTIONS (IN ORDER)

1. PRED-020-E / PRED-021-E CLOSE FIRST: Both windows closed 15 April. Classify kinetic or non-kinetic before any case analysis proceeds. If IRGC kinetic action against USN confirmed: immediate ESCALATING CRITICAL across Cases B/E.
1. OFAC GL U fetch: Confirm GL U status at 0001 EDT 19 April. If lapsed: Case D ESCALATING CRITICAL. PRED-022-C classify.
1. Yanbu / Petroline: Verify no new IRGC strike. If strike confirmed: PRED-018-E and PRED-022-D CONFIRMED.
1. Lebanon death toll: Re-verify. Likely exceeds 2,080+.
1. Hormuz transit volume: Re-verify AIS single-source. Note blockade enforcement gaps. Apply UKMTO as cross-check.
1. Second round talks: Any announcement before 22 April = PRED-022-A CONFIRMED. Check White House, Iranian FM, Pakistan PM channels.
1. Macron/Starmer 17 April Hormuz coalition: Assess outputs. Any multilateral mission commitment = material Case B development.
1. Rich Starry / blockade breach: Track additional Chinese-flag breaches. PRED-022-E.
1. PCP Step 1.5: New signal check — does any development exceed new case threshold?
1. DEVIATION AUDIT: Before producing PDF, check all seven structural tests in the ARCHITECTURE SPEC above. Fix any faults before finalising.
1. PDF PRODUCTION: Generate formatted PDF brief using updated build script. Output to /mnt/user-data/outputs/atollsphere_edition_023.pdf. Present file. DO NOT resolve analysis in chat.

-----

## DISCONFIRMATION THRESHOLDS — STANDING

|Case|Threshold                                                |Effect                                        |
|----|---------------------------------------------------------|----------------------------------------------|
|B   |Transit more than 54-68 ships/day for 3+ consecutive days|H-B1 CONTRADICTED — full reopening scenario   |
|B   |Formal written Hormuz transit protocol                   |H-B2 CONTRADICTED, PRED-018-B CONTRADICTED    |
|E   |Abqaiq / Yanbu confirmed full operations before 22 April |PRED-018-E CONTRADICTED                       |
|A   |Iran formally withdraws from negotiating process         |H-A2 probability rises sharply                |
|D   |GL U renewed or successor issued                         |H-D2 CONTRADICTED, Case D de-escalation review|