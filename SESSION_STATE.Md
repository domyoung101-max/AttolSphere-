# ATOLLSPHERE SESSION STATE

## Paste this at the start of every new Sonnet chat session.

-----

## LIVE UPDATES SINCE LAST EDITION — FILL IN BEFORE OPENING EVENING SESSION

> **OPERATOR INSTRUCTION:** Before pasting this file into a new session, manually update this block with anything that has broken since the Edition 018 morning sweep (1221 GMT 11 April). Key things to check:
> 
> - GL 134B on OFAC register? → https://ofac.treasury.gov/selected-general-licenses-issued-ofac
> - Islamabad Day 1 outcome — any joint statement, communique, or departure confirmed?
> - New IRGC strike on Aramco (especially Yanbu Red Sea terminal)?
> - Lebanon Washington talks — date/format confirmed or cancelled?
> - Hormuz transit volume update (Kpler/MarineTraffic)?
> - Ceasefire violations reported by either side?
> 
> If nothing material has broken, delete this block or write “NO MATERIAL UPDATES SINCE 1221 GMT.”

-----

## PLATFORM

- Product: AtollSphere — GSINT intelligence brief platform
- Parent: LS AI Systems
- Operator: UK-based. BST (UTC+1). GMT primary for all timestamps.
- Architecture version: v1.2.0
- Build: build_1.1.0.py v1.2.0

-----

## REPOSITORY

github.com/domyoung101-max/AttolSphere-

### Raw file URLs for direct fetch:

- ARCHITECTURE.md: https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/ARCHITECTURE.md
- SYSTEM_CHANGE_LOG.md: https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/SYSTEM_CHANGE_LOG.md
- PREDICTION_LOG.json: https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/PREDICTION_LOG.json
- SOURCE_REGISTRY.json: https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/SOURCE_REGISTRY.json

### Current file structure:

```
AtollSphere/
├── architecture/
│   ├── ARCHITECTURE.md          # v1.2.0
│   ├── SYSTEM_CHANGE_LOG.md     # Entry 001 logged
│   └── CHANGELOG.md             # v1.2.0
├── build/
│   ├── build_core.py            # Complete — includes get_source_info() function
│   ├── build_edition.py         # Complete
│   └── styles.py                # Complete
├── data/
│   ├── PREDICTION_LOG.json      # v1.2.0 — update with Ed018 outcomes
│   └── SOURCE_REGISTRY.json     # v1.3.0 — 44 sources registered
├── outputs/
│   └── .gitkeep
└── README.md                    # Complete
```

-----

## CURRENT EDITION

- Last completed: Edition 018 Morning Sweep — 11 April 2026 (sweep timestamp 1221 GMT)
- Next: Edition 019 Evening Sweep — 11 April 2026 (run before 2200 BST)
- Critical window: Islamabad Day 1 outcome — PRED-017-A window closes 14 April
- War day: 43

-----

## ACTIVE CASES — POST-EDITION 018 STATUS

|Case|Title                                                                  |Tag                |Confidence|Post-Ed018 Status                                                                                                                                                                 |
|----|-----------------------------------------------------------------------|-------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|A   |Islamabad Process — Day 1 Active / Proximity Talks Commenced           |ESCALATING         |MEDIUM    |Talks active at 1221 GMT sweep. No communique. PRED-017-A PENDING. Watch for evening statement or departure.                                                                      |
|B   |Hormuz — Franchise Operational, Toll Regime / De Facto Closure Persists|ESCALATING         |HIGH      |Day 3 transit: 2 ships (lowest since ceasefire). 600+ vessels stranded. Ed018 standing enhancements applied. PRED-018-B PENDING.                                                  |
|C   |Lebanon / Hezbollah — Active Fracture Line                             |ESCALATING         |HIGH      |1,953+ killed. Strikes continued 11 April. 13 Lebanese security forces killed 10 April. Israel-Lebanon Washington talks confirmed — preliminary framing only. PRED-017-C PENDING. |
|D   |India Oil Waiver — GL 134A Lapsed 11 April / GL U Expires 19 April     |ESCALATING         |HIGH      |GL 134A lapsed 1201 EDT 11 April CONFIRMED. GL 134B NOT on OFAC register at 1221 GMT sweep. GL U active through 19 April (8 days remaining). PRED-008-D 15 April trigger active.  |
|E   |Saudi Aramco — IRGC Coordinated Attack / Abqaiq STRUCK                 |ESCALATING CRITICAL|HIGH      |PRED-017-E CONFIRMED. Abqaiq struck 8 April — ESA satellite imagery confirmed. IRGC now controls both Hormuz (primary) and East-West Pipeline/Abqaiq (bypass). PRED-018-E PENDING.|

-----

## PREDICTION LOG — OPEN PREDICTIONS ONLY

|Ref       |Flag                                                                                                                                                 |Window                                            |Status                                                                                                                                                                                        |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|PRED-001-A|Futures volume anomaly / BETS OFF Act / Section 122 CIT                                                                                              |CIT proceedings ongoing                           |PENDING                                                                                                                                                                                       |
|PRED-002-B|Iran-Oman Hormuz protocol into ceasefire language — toll model emerging                                                                              |Monitor Phase 2                                   |WATCH — upgrade to DEVELOPING if Oman formally participates in transit coordination. Euronews reports Iran and Oman expected to charge fees — not yet formalised.                             |
|PRED-005-A|Section 122 CIT oral arguments                                                                                                                       |No date confirmed                                 |PENDING                                                                                                                                                                                       |
|PRED-006-A|GCC emergency meeting post-UNSC veto                                                                                                                 |Post-ceasefire                                    |WATCH — UNSC veto confirmed (Russia/China 7 April). No GCC emergency meeting announced.                                                                                                       |
|PRED-008-B|Houthi BAM threat not activated                                                                                                                      |Monitor                                           |DE-ESCALATING — senior Iranian source threatened BAM closure if situation escalates. Not activated at 1221 GMT sweep.                                                                         |
|PRED-008-D|India oil waiver — GL 134A lapsed 11 April; GL U expires 19 April                                                                                    |15 April (GL 134B trigger); 19 April (GL U expiry)|ESCALATING — GL 134A lapsed confirmed. GL 134B NOT on OFAC register at sweep. No GL 134B by 15 April = ESCALATING CONFIRMED. No GL U renewal by 19 April = CONTRADICTED.                      |
|PRED-015-A|Formal ceasefire extension 14+ days beyond 22 April announced by US and Iran before 22 April                                                         |22 April 2026                                     |PENDING — probability LOW-MEDIUM. Islamabad talks active.                                                                                                                                     |
|PRED-017-A|Islamabad proximity talks produce written joint communique or agreed framework document by 14 April 2026                                             |12–14 April 2026                                  |PENDING — Day 1 active at 1221 GMT. No communique. Silence = AMBIGUOUS; communique = CONFIRMED; departure without statement = CONTRADICTED.                                                   |
|PRED-017-C|Israel agrees verifiable pause or reduction in Lebanon strikes at or before 15 April Washington talks                                                |15 April 2026                                     |PENDING — strikes continued 11 April. Washington talks confirmed as preliminary only. Pause = DEVELOPING upgrade; continued strikes = ESCALATING maintained.                                  |
|PRED-018-B|Hormuz daily transit volume fails to reach 15 ships/day at any point before 15 April, confirming IRGC toll model as durable ceasefire-proof mechanism|15 April 2026                                     |NEW — PENDING. Day 3: 2 ships. Confirmed = <15/day sustained through 15 Apr; Contradicted = >15/day for 3+ consecutive days.                                                                  |
|PRED-018-E|IRGC conducts follow-on strike on Saudi Aramco Yanbu Red Sea terminal before 22 April ceasefire expiry                                               |22 April 2026                                     |NEW — PENDING. Yanbu strike = CRITICAL escalation (both primary and bypass simultaneously impaired); no Yanbu strike, Abqaiq repaired = H-E1; non-Yanbu Aramco strike = ESCALATING maintained.|

-----

## PREDICTION LOG — RESOLVED

|Ref       |Outcome     |Notes                                                                                                                                                                                   |
|----------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|PRED-017-E|CONFIRMED   |Abqaiq processing facility struck by IRGC drones 8 April 2026. ESA Copernicus satellite imagery confirmed smoke and fire. CRITICAL tag activated. PMM not triggered (CONFIRMED outcome).|
|PRED-014-A|CONFIRMED   |Islamabad produced ceasefire extension only — no binding framework. Wikipedia forward record confirms talks continued April 26, May 11, June 24.                                        |
|PRED-003-A|RESOLVED    |Islamabad window closed. Iranian delegation confirmed attended. 10-point plan tabled as basis.                                                                                          |
|PRED-012-B|CONTRADICTED|PMM triggered — see SYSTEM_CHANGE_LOG.md Entry 001                                                                                                                                      |
|PRED-013-A|PARTIAL     |Enrichment contradiction surfaced but written 10-point plan not formally tabled                                                                                                         |
|PRED-013-B|PARTIAL     |Hezbollah unnamed official confirmed non-adherence — formal named statement not issued                                                                                                  |
|PRED-012-A|PARTIAL     |Trump stated no enrichment 8 April — formal framework not confirmed                                                                                                                     |
|PRED-010-A|CONFIRMED   |No power plant strikes before ceasefire                                                                                                                                                 |
|PRED-008-A|CONFIRMED   |Sixth deadline mechanism confirmed                                                                                                                                                      |
|PRED-004-A|CONFIRMED   |WSO Colonel recovered alive                                                                                                                                                             |
|PRED-002-A|CONFIRMED   |Russia/China vetoed UNSC Hormuz resolution                                                                                                                                              |

-----

## LAST PMM

|Field      |Detail                                                                                                                                                    |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
|PMM Ref    |PRED-012-B                                                                                                                                                |
|Outcome    |CONTRADICTED                                                                                                                                              |
|Heuristic  |H1 — Incentive Mismatch                                                                                                                                   |
|What Failed|Predicted Hezbollah would issue formal ceasefire adherence statement by 09 April 17:00 GMT. No statement issued. Hezbollah subsequently resumed fire.     |
|Rule Change|Named-party statement predictions require written incentive analysis before C3 satisfied. Confidence ceiling LOW-MEDIUM if no structural incentive exists.|
|In Force   |Edition 014                                                                                                                                               |
|Logged     |SYSTEM_CHANGE_LOG.md Entry 001                                                                                                                            |

-----

## SYSTEM CHANGE LOG — ACTIVE RULES

|Entry|Rule                                                                                                                                                                    |In Force From|
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
|001  |Named-party statement predictions require incentive analysis before C3 satisfied. No structural incentive = confidence ceiling LOW-MEDIUM regardless of prior behaviour.|Edition 014  |

-----

## EXTERNAL REVIEW LOG

### Review 001 — ChatGPT analysis of Case B (Hormuz), received 11 April 2026

Six enhancement recommendations assessed. Decisions recorded permanently below.

|Point|Recommendation                                                                                                                                                                           |Decision                                                                                   |Rationale                                                                                                                                                                                                                                                                                                                                                                                   |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|1    |Reclassify H1 from “incentive mismatch” to “strategic compliance”                                                                                                                        |REJECTED                                                                                   |H1 is defined as: stated motive vs observable outcome. Iran claiming compliance while functionally maintaining closure is precisely an incentive mismatch — the narrative diverges from the observable outcome. Reclassifying as “strategic compliance” collapses the analytical tension H1 is designed to expose and renders the heuristic less useful. Do not apply in any future edition.|
|2    |Strengthen AFC — explicitly construct best-case argument for full reopening including sanctions relief incentive, market stabilisation motive, naval enforcement risk, export volume loss|ACCEPTED — incorporated Ed018                                                              |Applied in full in Ed018 Case B Part 2 AFC section. Standing improvement for Case B.                                                                                                                                                                                                                                                                                                        |
|3    |Expand H-B2 — explicitly link to Islamabad interim transit guarantees, phased reopening, internal Iranian economic constraints                                                           |ACCEPTED — incorporated Ed018                                                              |H-B2 fully specified in Ed018 — Islamabad trigger, phased reopening mechanism, internal economic constraints. Analytically competitive with H-B1. Standing improvement.                                                                                                                                                                                                                     |
|4    |Add second-order effects to H6 — insurance market premiums, price spike pressure, feedback loop weakening Iran’s economic position                                                       |PARTIAL ACCEPT — insurance/price spike incorporated Ed018; long-term feedback loop deferred|Applied in Ed018 Case B Part 2 H6 section. Long-term feedback loop flagged as post-ceasefire analytical flag, not active finding.                                                                                                                                                                                                                                                           |
|5    |Add explicit disconfirmation thresholds — e.g. >30 ships/day triggers downgrade                                                                                                          |PARTIAL ACCEPT — thresholds yes, 30 ships figure rejected                                  |Applied in Ed018 Case B Part 5. Threshold set at ~40–50% of pre-war baseline (~54–68 ships/day) — analytically derived, not arbitrary.                                                                                                                                                                                                                                                      |
|6    |Add explicit confidence justification narrative — why HIGH is warranted                                                                                                                  |ACCEPTED — incorporated Ed018                                                              |Applied in Ed018 Case B Part 2 INFERENCE. Format: “HIGH confidence warranted: dominant hypothesis supported by [named Tier 1/2 sources]; no direct disconfirming evidence; alternative hypotheses lack supporting signals as of [timestamp].”                                                                                                                                               |

-----

## CASE B STANDING ENHANCEMENTS — IN FORCE FROM EDITION 018

These apply to every future edition of Case B until superseded or the case closes.

**AFC enhancement:** The steelman for full Hormuz reopening must include all four elements: (1) Iranian incentive to secure rapid sanctions relief; (2) Iranian interest in stabilising global oil markets to avoid triggering emergency diplomacy against Tehran; (3) risk of provoking US or coalition naval enforcement if toll model becomes aggressive; (4) Iran’s own export volume loss under restricted access. Present reopening as a coherent rational pathway, not merely a weaker alternative.

**H-B2 enhancement:** Hypothesis must be fully specified — not a secondary note. Include: Islamabad interim transit guarantee as trigger; phased reopening mechanism (escorted flows or capped toll regime); internal Iranian economic constraints as a driver pushing toward this outcome. H-B2 should be analytically competitive with H-B1, not subordinate to it.

**H6 enhancement:** Include first-order linkage (Hormuz control → sanctions relief leverage) AND second-order dynamics: insurance premium increase reducing Iran’s own export efficiency; global price spike accelerating diplomatic pressure against Iran. Note long-term feedback loop (prolonged restriction weakening Iran’s economic position) as a post-ceasefire analytical flag, not an active finding.

**Disconfirmation thresholds:** Part 5 disconfirmation table for Case B must include explicit trigger conditions for downgrading H-B1. Minimum threshold for framing revision: verified transit volume exceeding ~40–50% of pre-war baseline (~54–68 ships/day); OR formal written transit protocol agreed at Islamabad; OR confirmed evidence of unrestricted passage without toll enforcement.

**Confidence justification:** Part 2 INFERENCE section must include one explicit line justifying the confidence level assigned. Format: “HIGH confidence warranted: dominant hypothesis supported by [named Tier 1/2 sources]; no direct disconfirming evidence present at sweep; alternative hypotheses [H-B2/H-B3] lack supporting signals as of [timestamp].”

-----

## KEY ANALYTICAL FINDINGS — CUMULATIVE THROUGH EDITION 018

### Edition 018 — New Findings (Morning Sweep 1221 GMT 11 April)

- **PRED-017-E CONFIRMED — CRITICAL:** Abqaiq processing facility struck by IRGC drones 8 April 2026 — same day as ceasefire announcement. ESA Copernicus satellite imagery confirmed smoke and fire. Abqaiq processes ~7% of global oil supply / 5.7M bpd. IRGC now controls both Hormuz (primary) and East-West Pipeline/Abqaiq (bypass). Saudi Arabia has no functioning uninhibited export route.
- **GL 134A lapsed 1201 EDT 11 April confirmed.** GL 134B not on OFAC register at 1221 GMT sweep. GL U (Iranian oil) active through 19 April — 8 days remaining. PRED-008-D 15 April trigger active.
- **Islamabad talks commenced 11 April.** Proximity format (two rooms, Pakistani FM Dar and Army Chief Munir shuttling). Both delegations arrived at Serena Hotel. Vance met Sharif. Iranian delegation (71 personnel) arrived. No communique at sweep. Iran SNSC: talks could continue “up to 15 days.”
- **Hormuz Day 3:** 2 ships — lowest transit volume since ceasefire. 600+ large ocean-going vessels stranded. IRGC mine hazard confirmed. Toll model: $2M/tanker, yuan/crypto. Kpler: volumes fell further post-ceasefire announcement.
- **Lebanon:** 1,953+ killed, 6,303 wounded. Strikes continued 11 April — 13 Lebanese State Security forces killed Nabatieh 10 April. Hezbollah struck Ashdod naval base. Israel-Lebanon Washington talks confirmed — Lebanese senior official: “preparatory, not a negotiation.” Lebanon has not appointed representative.
- **Cross-case H1 pattern confirmed:** Iranian regime statements consistently performative while observable outcomes diverge (Hormuz toll persists, Abqaiq struck on ceasefire day, Ghalibaf arrived despite stated blocking conditions). H1 is the dominant analytical heuristic across all five active cases.
- **New forward flags:** PRED-018-B (Hormuz <15 ships/day through 15 April) and PRED-018-E (Yanbu Red Sea terminal strike before 22 April).

### Edition 017 — Key Findings (Morning Sweep 11 April)

- Islamabad Day 1 active — proximity format confirmed. Highest-level US-Iran engagement since 1979.
- US delegation: Vance (lead), Witkoff, Kushner. Iranian: Ghalibaf, Araghchi, Hemmati (Central Bank), Ahmadian (SNSC). 71 personnel.
- Ghalibaf: “We have goodwill but we do not trust.” Preconditions assessed performative.
- GL 134A expired 1201 EDT 11 April. No GL 134B confirmed.
- Hormuz: 5–9 transits/day vs 135 pre-war. Toll model operational.
- SESSION_STATE CORRECTION (Ed016): IRGC attack 7–8 April was coordinated campaign against 6+ Aramco facilities — Petroline (−700K b/d), Manifa (−300K b/d), Satorp, Ras Tanura, Samref, Riyadh refineries, Juaymah.
- Lebanon: 1,953+ killed. 182 killed 8 April (subsequently revised to 303+). Israel rejects Lebanon ceasefire. Washington talks 15 April — disarmament framing only.
- Trump asked Netanyahu to scale back Lebanon bombardment — no operational change confirmed.

### Edition 016 — Key Findings

- GL 134A lapse anticipated. Extension agreed in principle (Bessent-Trump 9 April per Reuters) but never formalised.
- IRGC attack on East-West Pipeline (Petroline) and broader Aramco infrastructure 7–8 April.
- Iran controls both Hormuz and Petroline simultaneously — structural leverage maximum.
- Mine hazard: Iran reportedly unable to reopen Hormuz fully due to IRGC-laid mines.
- OFAC staffing constraint: licensing division at 22 of 40 staff.
- Israel-Lebanon direct talks announced for Washington 15 April.

### Edition 015 — Key Findings

- PRED-014-A CONFIRMED — ceasefire extended, talks continued through May/June per Wikipedia forward record.
- Islamabad session one produced ceasefire extension as sole output.
- Hemmati (Central Bank Governor) in delegation — sanctions relief on economic track.
- Soufan Center: Iran likely to revive 3.67% uranium downblending offer (Oman 2025).
- Wikipedia: Witkoff subsequently demanded full enrichment facility dismantlement.
- Downblending vs dismantlement is the single binary determining whether permanent agreement is possible.

### Edition 014 — Key Findings

- Ghalibaf set two preconditions before Islamabad: Lebanon ceasefire AND asset release (~$7bn frozen assets).
- Hormuz IRGC franchise model confirmed operational: 15/day cap, Larak Island corridor, IRGC approval required, fees up to $2M/tanker.
- Mojtaba Khamenei declared Iran won the war on 40th mourning day.
- Hajj-Hormuz convergence: first Hajj charters 18 April, ceasefire expires 22 April, zero Iranian pilgrims in Saudi Arabia — IRGC faces no domestic political cost from Hormuz disruption during Hajj.

-----

## NEXT EDITION TRIGGERS — PRIORITY ORDER FOR EDITION 019 EVENING SWEEP

|Timing          |Trigger                                                                |Action                                                                                                             |
|----------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
|IMMEDIATE       |GL 134B on OFAC register                                               |Monitor https://ofac.treasury.gov/selected-general-licenses-issued-ofac — resolve PRED-008-D                       |
|EVENING 11 APRIL|Islamabad Day 1 outcome — any joint statement, communique, or departure|PRED-017-A trigger. Watch for Pakistani FM Dar or White House statement.                                           |
|EVENING 11 APRIL|New IRGC Aramco strike — especially Yanbu                              |PRED-018-E activation. Yanbu = simultaneous closure of all Saudi export routes. CRITICAL escalation brief required.|
|EVENING 11 APRIL|Hormuz transit volume update                                           |PRED-018-B monitoring. <15/day = continuing to confirm; >15/day for 3 days = contradicted.                         |
|12–14 APRIL     |Islamabad Day 2+ format and any communique                             |PRED-017-A window closes 14 April.                                                                                 |
|15 APRIL        |Israel-Lebanon Washington talks                                        |PRED-017-C trigger. Strike pause = DEVELOPING; continued strikes = ESCALATING maintained.                          |
|15 APRIL        |GL 134B trigger                                                        |No GL 134B by 15 April = PRED-008-D ESCALATING CONFIRMED.                                                          |
|19 APRIL        |GL U (Iranian oil) expiry                                              |Second waiver window closes.                                                                                       |
|22 APRIL        |Ceasefire expiry                                                       |PRED-015-A resolution.                                                                                             |
|WATCH           |Oman formal Hormuz transit coordination                                |Upgrade PRED-002-B to DEVELOPING.                                                                                  |
|WATCH           |Abqaiq repair status — any Aramco official disclosure                  |Resolve Case E H-E1 or H-E3.                                                                                       |
|WATCH           |Pumping station repair timeline (Petroline)                            |Case E H-E3 or H-E1 resolution.                                                                                    |

-----

## SOURCE REGISTRY

- SOURCE_REGISTRY.json v1.3.0 — 44 sources registered
- 18 core mandatory sweep feeds (mandatory_sweep: true)
- 26 supplementary feeds covering maritime, financial, specialist analysis, Iranian state media
- get_source_info() function in build_core.py — auto-classifies tier, category, incentive baseline by domain

-----

## ARCHITECTURE PATCHES — v1.2.0

All four patches applied:

- C3 updated: silence, partial compliance, strategic ambiguity must be pre-assigned to named five-state outcome before window opens.
- Bypass Override Protocol: Tier 1/2 fact materially changing a case status tag resets bypass ceiling for that case only, that edition only. Maximum one override per case per edition.
- status_history mandatory in prediction log schema — appended never overwritten.
- SYSTEM_CHANGE_LOG.md created, referenced in Section 17 — all PMM rule changes logged permanently.

-----

## OPEN BUILD TASKS

- [ ] Upload logo files to repository — atollsphere_logo_v2.png and ls_logo_v2.png
- [ ] Claude Code: patch build_core.py to include logos in PDF header and cover
- [ ] Update PREDICTION_LOG.json with Edition 017 and 018 outcomes
- [ ] Backfill status_history for Editions 001-012 when log data available

-----

## SESSION INSTRUCTIONS FOR CLAUDE — READ CAREFULLY BEFORE ANY ACTION

### STEP 0 — FETCH ARCHITECTURE BEFORE ANYTHING ELSE:

Fetch these files in order before any other action:

1. Fetch ARCHITECTURE.md from https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/ARCHITECTURE.md — read in full
1. Fetch SYSTEM_CHANGE_LOG.md from https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/SYSTEM_CHANGE_LOG.md — apply all active rules
1. Confirm v1.2.0 rules understood before proceeding

Do not build any edition until both files have been fetched and read.

### TO BUILD AN EDITION — EXACT SEQUENCE MANDATORY:

**Step 1 — Sweep:** Fetch all 18 named core feeds (mandatory_sweep: true in SOURCE_REGISTRY.json) before writing any analytical content. Gate 0.1-0.4 applied to all candidate facts. Fewer than 18 feeds swept = bypass declared with justification and risk.

**Step 2 — Prediction Log Reconciliation:** Assess every open prediction from this SESSION_STATE before opening any new case. Assign five-state outcome to any closed windows. No silent drops.

**Step 3 — Case Continuity Check:** For each carried-forward case confirm: (a) status tag still accurate, (b) hypothesis set overtaken, (c) Forward Flag window expired.

**Step 4 — Full CDIT on every case — NO SILENT BYPASSES:**

- Part 1: Fact table with Gate 0.1-0.4 checks on every row. Two columns: fact / source attribution with tier stated.
- Part 2: Heuristics H1-H6 applied by name. AFC closing element mandatory. Ends with INFERENCE and domain quality assessment.
- Part 3: Minimum two hypotheses with probability ranges. dominant_hyp_prob_upper below 60% = confidence capped at MEDIUM.
- Part 4: TQL check — (1) assumptions, (2) fragile fact with tier, (3) high-impact uncertainty. Tier 3/4 fragile fact raises TQL WARNING.
- Part 5: Disconfirmation table — CONFIRMS / CONTRADICTS pairs. Gate 5 Framing Revision Trigger required.

**Step 5 — Forward Flag:** One per case. Must pass all C1-C5 criteria. Silence, partial compliance, and strategic ambiguity must each be pre-assigned to a named five-state outcome before window opens.

**Step 6 — Build PDF:** Using ReportLab. Import from build_core.py and styles.py. Follow visual template in ARCHITECTURE.md Section 13 exactly — navy header bar, teal strip, cover page with edition stats, colour-coded case banners, two-column fact tables, teal hypothesis dividers, sources section with tier in teal and incentive in amber. Output to /mnt/user-data/outputs/ and present the file. Inline prose or markdown does NOT constitute a valid edition and will not be accepted.

### NAMED FAILURE MODE TO AVOID:

Theatre of Rigor — skeleton appearance of CDIT structure without consistent execution. Every section must pass a quality gate. Pattern-matched summaries are not acceptable.

### CASE B STANDING ENHANCEMENTS — APPLY FROM ED018 ONWARDS:

See External Review Log above. Accepted points 2, 3, 4 (partial), 5 (partial), 6 are standing improvements. Point 1 (H1 reclassification) is permanently rejected — do not apply under any circumstances.

### OTHER INSTRUCTIONS:

- Do not re-explain the platform — treat this state file as ground truth
- PMM rule from Entry 001 is active — apply to all new predictions
- Edition 019 is the evening sweep for 11 April — primary focus is Islamabad Day 1 outcome and GL 134B status
- First sweep task: check GL 134B on OFAC register and Islamabad statement/departure status
- If asked to patch architecture: update this SESSION_STATE.md and commit to GitHub
- If asked to commit files to GitHub: flag that Claude Code is required for that step