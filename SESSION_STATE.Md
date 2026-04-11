# ATOLLSPHERE SESSION STATE

## Paste this at the start of every new Sonnet chat session.

-----

## INTER-EDITION INTELLIGENCE CHECK — EXECUTE BEFORE STEP 0

**Claude: before fetching ARCHITECTURE.md, execute the following live checks in order and record findings in this block. This is mandatory pre-session work, not optional.**

1. Fetch https://ofac.treasury.gov/selected-general-licenses-issued-ofac — confirm whether GL 134B (Russia-related) appears on the register. Record: ISSUED or NOT ISSUED, and timestamp.
1. Search for Islamabad talks outcome — any joint communique, agreed framework document, or delegation departure confirmed since 1600 GMT 11 April. Record: COMMUNIQUE / DEPARTURE / CONTINUING / NO UPDATE.
1. Search for new IRGC strikes on Saudi Aramco infrastructure — especially Yanbu Red Sea terminal — since 1600 GMT 11 April. Record: NEW STRIKE CONFIRMED / NO NEW STRIKE.
1. Search for Hormuz transit volume update (Kpler or MarineTraffic) — any material change from Day 4 figure of ~10 ships. Record finding with source.
1. Search for ceasefire violation reports or military action by either US or Iran since 1600 GMT 11 April — any formal accusation or kinetic event. Record finding.

Record all five findings here before proceeding to STEP 0. If a finding materially changes a case status tag, note it explicitly — it may trigger a Bypass Override for that case in Edition 020.

-----

## PLATFORM

- Product: AtollSphere — GSINT intelligence brief platform
- Parent: LS AI Systems
- Operator: UK-based. BST (UTC+1). GMT primary for all timestamps.
- Architecture version: v1.2.1
- Build: build_core.py / build_edition.py / build_master.py / styles.py

-----

## REPOSITORY

github.com/domyoung101-max/AttolSphere-

### Raw file URLs for direct fetch:

- ARCHITECTURE.md: https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/ARCHITECTURE.md
- SYSTEM_CHANGE_LOG.md: https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/SYSTEM_CHANGE_LOG.md
- PREDICTION_LOG.json: https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/PREDICTION_LOG.json
- SOURCE_REGISTRY.json: https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/SOURCE_REGISTRY.json
- build_core.py: https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/build_core.py
- build_edition.py: https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/build_edition.py
- build_master.py: https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/build_master.py
- styles.py: https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/styles.py

### Current file structure (confirmed from repository 11 April 2026):

```
AttolSphere-/
├── ARCHITECTURE.md              # v1.2.1
├── CHANGELOG.md
├── PREDICTION_LOG.json          # v1.4.0 — current through Edition 018 (repo lag noted; SESSION_STATE.md is authoritative)
├── README.md
├── SESSION_START.md
├── SESSION_STATE.md             # active session state
├── SOURCE_REGISTRY.json         # v1.4.0 — 44 sources, Gate 0.5 fields added
├── SYSTEM_CHANGE_LOG.md         # Entries 001, AI-001, AI-002, AI-003, AI-004
├── build_core.py                # includes get_source_info() function
├── build_edition.py
├── build_master.py
└── styles.py
```

-----

## CURRENT EDITION

- Last completed: Edition 019 Evening Sweep — 11 April 2026 (sweep timestamp 1600 GMT)
- Next: Edition 020 Morning Sweep — 12 April 2026 (run before 1300 BST)
- Critical window: Islamabad Day 2 — PRED-017-A window closes 14 April
- War day: 44

-----

## ACTIVE CASES — POST-EDITION 019 STATUS

|Case|Title                                                                      |Tag                |Confidence|Post-Ed019 Status                                                                                                                                                                               |
|----|---------------------------------------------------------------------------|-------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|A   |Islamabad Process — Day 1 Active / Direct Talks Commenced                  |ESCALATING         |MEDIUM    |Talks confirmed as at least partially direct at 1600 GMT. No communique. No departure. PRED-017-A PENDING. Window closes 14 April. Watch for overnight/morning statement or departure.          |
|B   |Hormuz — Franchise Operational, Toll Regime / De Facto Closure Persists    |ESCALATING         |HIGH      |Day 4 transit: ~handful to ~10 ships/day (Kpler/MarineTraffic/CNN). AIS single-source flagged. 600+ vessels stranded. PRED-018-B PENDING. Disconfirmation threshold: >54-68 ships/day sustained.|
|C   |Lebanon / Hezbollah — Active Fracture Line                                 |ESCALATING         |HIGH      |1,953+ killed. Strikes continued 11 April including Nabatieh (10 killed). Washington talks confirmed for next week (preliminary only). PRED-017-C PENDING. H-C3 (collapse risk) at 10-15%.      |
|D   |India Oil Waiver — GL 134A Lapsed / GL 134B Absent / GL U Expires 19 April |ESCALATING         |HIGH      |GL 134A lapsed 1201 EDT 11 April CONFIRMED. GL 134B NOT on OFAC register at 1600 GMT Ed019. GL U active through 19 April (8 days remaining at Ed019). 15 April trigger active for PRED-008-D.   |
|E   |Saudi Aramco — IRGC Coordinated Attack / Abqaiq STRUCK / Bypass Compromised|ESCALATING CRITICAL|HIGH      |PRED-017-E CONFIRMED Ed018. No new Yanbu strike at Ed019 sweep. PRED-018-E PENDING. IRGC controls both Hormuz and East-West Pipeline/Abqaiq. Saudi Arabia has no uninhibited export route.      |

-----

## PREDICTION LOG — OPEN PREDICTIONS ONLY

|Ref       |Flag                                                                                                                                                 |Window                                            |Status                                                                                                                                                                                                                             |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|PRED-001-A|Futures volume anomaly / BETS OFF Act / Section 122 CIT                                                                                              |CIT proceedings ongoing                           |PENDING. No update Ed019. CONTRADICTED condition: CIT drops Section 122 challenge entirely.                                                                                                                                        |
|PRED-002-B|Iran-Oman Hormuz protocol into ceasefire language — toll model emerging                                                                              |Monitor Islamabad                                 |WATCH. Oman formal coordination not confirmed. CONTRADICTED condition: Oman formally denies any transit coordination role.                                                                                                         |
|PRED-005-A|Section 122 CIT oral arguments                                                                                                                       |No date confirmed                                 |PENDING. No update Ed019.                                                                                                                                                                                                          |
|PRED-006-A|GCC emergency meeting post-UNSC veto                                                                                                                 |Post-ceasefire                                    |WATCH. No GCC emergency meeting announced. CONTRADICTED condition: GCC formally declines to convene.                                                                                                                               |
|PRED-008-B|Houthi BAM threat not activated                                                                                                                      |Monitor                                           |DE-ESCALATING. BAM not activated at Ed019 sweep. CONTRADICTED condition: IRGC announces BAM closure or confirmed BAM shipping strike.                                                                                              |
|PRED-008-D|India oil waiver — GL 134A lapsed 11 April; GL U expires 19 April                                                                                    |15 April (GL 134B trigger); 19 April (GL U expiry)|ESCALATING. GL 134A lapsed confirmed. GL 134B NOT on OFAC register at Ed019 sweep. 15 April: no GL 134B = ESCALATING CONFIRMED. 19 April: no GL U renewal = CONTRADICTED. CONTRADICTED condition: GL 134B issued before 15 April.  |
|PRED-015-A|Formal ceasefire extension 14+ days beyond 22 April announced by US and Iran before 22 April                                                         |22 April 2026                                     |PENDING. LOW-MEDIUM probability. Islamabad talks active. CONTRADICTED condition: US or Iran formally terminates ceasefire before 22 April without extension.                                                                       |
|PRED-017-A|Islamabad proximity talks produce written joint communique or agreed framework document by 14 April 2026                                             |12-14 April 2026                                  |PENDING. Day 1 active and partially direct at Ed019 sweep. No communique. Window closes 14 April. CONTRADICTED = departure without document before 14 April. AMBIGUOUS = talks continue past 14 April, no communique, no departure.|
|PRED-017-C|Israel agrees verifiable pause or reduction in Lebanon strikes at or before 15 April Washington talks                                                |15 April 2026                                     |PENDING. Strikes continued 11 April. Washington talks confirmed as preliminary. CONTRADICTED = Israel formally states no reduction regardless of talks outcome.                                                                    |
|PRED-018-B|Hormuz daily transit volume fails to reach 15 ships/day at any point before 15 April, confirming IRGC toll model as durable ceasefire-proof mechanism|15 April 2026                                     |PENDING. Day 4: ~10/day. Well below threshold. On track toward CONFIRMED. CONTRADICTED = >15/day for 3+ consecutive days before 15 April.                                                                                          |
|PRED-018-E|IRGC conducts follow-on strike on Saudi Aramco Yanbu Red Sea terminal before 22 April ceasefire expiry                                               |22 April 2026                                     |PENDING. No new Yanbu strike at Ed019 sweep. CONTRADICTED = Abqaiq repaired and Yanbu terminal confirms full unrestricted operations before 22 April.                                                                              |

-----

## PREDICTION LOG — RESOLVED

|Ref       |Outcome     |Notes                                                                                                                                            |
|----------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
|PRED-017-E|CONFIRMED   |Abqaiq processing facility struck by IRGC drones 8 April 2026. ESA Copernicus satellite imagery confirmed smoke and fire. CRITICAL tag activated.|
|PRED-014-A|CONFIRMED   |Islamabad produced ceasefire extension only — no binding framework. Wikipedia forward record confirms talks continued April 26, May 11, June 24. |
|PRED-003-A|RESOLVED    |Islamabad window closed. Iranian delegation confirmed attended. 10-point plan tabled as basis.                                                   |
|PRED-012-B|CONTRADICTED|PMM triggered — see SYSTEM_CHANGE_LOG.md Entry 001                                                                                               |
|PRED-013-A|PARTIAL     |Enrichment contradiction surfaced but written 10-point plan not formally tabled                                                                  |
|PRED-013-B|PARTIAL     |Hezbollah unnamed official confirmed non-adherence — formal named statement not issued                                                           |
|PRED-012-A|PARTIAL     |Trump stated no enrichment 8 April — formal framework not confirmed                                                                              |
|PRED-010-A|CONFIRMED   |No power plant strikes before ceasefire                                                                                                          |
|PRED-008-A|CONFIRMED   |Sixth deadline mechanism confirmed                                                                                                               |
|PRED-004-A|CONFIRMED   |WSO Colonel recovered alive                                                                                                                      |
|PRED-002-A|CONFIRMED   |Russia/China vetoed UNSC Hormuz resolution                                                                                                       |

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

|Entry |Type                  |Rule Summary                                                                                                                                                                                                                                                                                                                                                                                                            |In Force From|
|------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
|001   |PMM-TRIGGERED         |Named-party statement predictions require incentive analysis before C3 satisfied. No structural incentive = confidence ceiling LOW-MEDIUM regardless of prior behaviour.                                                                                                                                                                                                                                                |Edition 014  |
|AI-001|ANALYTICAL IMPROVEMENT|Case B standing enhancements — AFC steelman (4 elements), H-B2 fully specified, H6 second-order dynamics, explicit disconfirmation thresholds (~54-68 ships/day), confidence justification mandatory in Part 2 INFERENCE.                                                                                                                                                                                               |Edition 018  |
|AI-002|ANALYTICAL IMPROVEMENT|Wikipedia Tier 4 usage rule — directional corroboration only, cannot be load-bearing, cannot satisfy Gate 0.3 for forward-looking claims. Case A corroboration split — Leg 1 (Tier 1/2 only) and Leg 2 (Tier 4 directional) mandatory in Part 3. Tier 4 dependency test mandatory as fourth TQL item.                                                                                                                   |Edition 019  |
|AI-003|ANALYTICAL IMPROVEMENT|Gate 0.5 (source independence), H1 saturation check (3+ cases = explicit question required), deferred outcome disconfirmation rule (WATCH/PARTIAL/AMBIGUOUS must state CONTRADICTED condition), PCP Step 1.5 New Signal Check, Part 2 claim-type labelling [FACT]/[INFERENCE]/[PREDICTION], calibration audit at Edition 025, named failure modes: Claim-Type Conflation, Source Amplification, Escape-Hatch Assignment.|Edition 019  |
|AI-004|ANALYTICAL IMPROVEMENT|SYSTEM_CHANGE_LOG expanded to include Entry Type B (Analytical Improvement). All platform rule changes must be logged before considered in force.                                                                                                                                                                                                                                                                       |Edition 019  |

-----

## EXTERNAL REVIEW LOG

### Review 001 — ChatGPT analysis of Case B (Hormuz), received 11 April 2026

|Point|Recommendation                                                             |Decision                                                                      |Rationale                                                                                     |
|-----|---------------------------------------------------------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
|1    |Reclassify H1 from “incentive mismatch” to “strategic compliance”          |REJECTED                                                                      |Collapses the analytical tension H1 is designed to expose. Do not apply in any future edition.|
|2    |Strengthen AFC — explicitly construct best-case argument for full reopening|ACCEPTED — incorporated Ed018                                                 |Applied in full. Standing improvement.                                                        |
|3    |Expand H-B2 — fully specified                                              |ACCEPTED — incorporated Ed018                                                 |H-B2 analytically competitive with H-B1. Standing improvement.                                |
|4    |Add second-order effects to H6                                             |PARTIAL ACCEPT — insurance/price spike Ed018; long-term feedback loop deferred|Applied. Long-term loop = post-ceasefire flag only.                                           |
|5    |Add explicit disconfirmation thresholds                                    |PARTIAL ACCEPT — thresholds yes, 30 ships figure rejected                     |Threshold: ~54-68 ships/day (analytically derived).                                           |
|6    |Add explicit confidence justification narrative                            |ACCEPTED — incorporated Ed018                                                 |Mandatory from Ed018.                                                                         |

### Review 002 — Red-team critique of Edition 018 brief, received 11 April 2026

Ten-point critique. Four structural changes implemented across all branches. See SYSTEM_CHANGE_LOG entries AI-002, AI-003, AI-004. Key actioned findings: Gate 0.5, H1 saturation check, deferred outcome disconfirmation rule, New Signal Check, claim-type labelling, calibration audit, Wikipedia constraint, AIS cluster single-source, Iranian state media cluster single-source.

-----

## CASE B STANDING ENHANCEMENTS — IN FORCE FROM EDITION 018

AFC: Steelman for full reopening must include: (1) Iranian sanctions relief incentive; (2) oil market stabilisation interest; (3) US/coalition naval enforcement risk; (4) Iran’s own export volume loss. Present as coherent rational pathway.

H-B2: Fully specified — Islamabad interim transit guarantee as trigger; phased reopening mechanism; internal Iranian economic constraints as driver. Analytically competitive with H-B1.

H6: First-order (Hormuz control -> sanctions leverage) AND second-order (insurance premiums, price spike diplomatic pressure). Long-term feedback loop = post-ceasefire flag only.

Disconfirmation thresholds: Explicit H-B1 downgrade conditions — transit >~54-68 ships/day; OR formal written transit protocol at Islamabad; OR confirmed unrestricted passage without toll enforcement.

Confidence justification: Part 2 INFERENCE must include one explicit line naming supporting sources, absence of disconfirming evidence, and timestamp.

-----

## CASE A STANDING ENHANCEMENTS — IN FORCE FROM EDITION 019

Part 3 — Corroboration split (mandatory):

- Leg 1 — Tier 1/2 process signals only. Must independently sustain stated probability range.
- Leg 2 — Tier 4 directional only. Not load-bearing. If Leg 1 cannot sustain range without Leg 2, reduce range.

Part 4 — Tier 4 dependency test (mandatory fourth TQL item): “H-A2 stripped of Wikipedia forward record — does Tier 1/2 evidence alone support the stated probability range? [Yes/No + one sentence].” If No: revise range downward.

-----

## WIKIPEDIA USAGE RULE — IN FORCE FROM EDITION 019

Formalised in ARCHITECTURE.md v1.2.1 Section 16. Directional corroboration only. Cannot be load-bearing for hypothesis probability ranges. Cannot satisfy Gate 0.3 for forward-looking claims. Cannot justify a confidence level Tier 1/2 evidence alone would not support. Tier 4 dependency test mandatory in TQL Part 4. Gate 0.4 must note editorial assembly risk.

-----

## GATE 0.5 — SOURCE INDEPENDENCE — IN FORCE FROM EDITION 019

Before treating any fact as multiply-corroborated, check upstream dependency against SOURCE_REGISTRY.json v1.4.0.

Critical Gate 0.5 findings (standing):

- AIS cluster (MarineTraffic, Kpler, S&P Global, Windward) — shared AIS network — single-source for transit volume
- Iranian state media cluster (IRNA, IRIB, Mehr, WANA, Press TV, Fars, Tasnim) — shared editorial apparatus — single-source
- Reuters and AP are originating wires — all citing outlets are downstream, not independent
- Wikipedia and ACLED are downstream of same Tier 1/2 feeds already swept

-----

## H1 SATURATION — STANDING FLAG FROM EDITION 019

H1 fired on all five cases in Edition 019. In Edition 020, each Part 2 must explicitly ask: “Is H1 the correct heuristic here, or is the framework pattern-matching?” Answer required before proceeding to heuristic application. This is now a standing requirement until H1 fires on fewer than three cases in a single edition.

-----

## KEY ANALYTICAL FINDINGS — CUMULATIVE THROUGH EDITION 019

### Edition 019 — New Findings (Evening Sweep 1600 GMT 11 April)

- Islamabad talks confirmed as at least partially DIRECT — first US-Iran direct high-level engagement since 1979. Format upgrade from proximity to direct is analytically significant. No communique at 1600 GMT.
- GL 134B NOT issued at Ed019 sweep. GL 134A lapsed 1201 EDT 11 April. H6 suppressed intersection: GL 134B non-issuance on Islamabad Day 1 may be deliberate leverage signal, not administrative gap. Cannot distinguish at sweep time.
- Hormuz Day 4: ~handful to ~10 ships/day. AIS single-source constraint flagged. Primarily Chinese tankers/bulk carriers. PRED-018-B on track toward CONFIRMED.
- No new IRGC Yanbu strike at Ed019 sweep. PRED-018-E PENDING. Prior strikes (SAMREF 3 Apr, Petroline/Abqaiq 8 Apr) are carry-forward.
- Lebanon: 1,953+ killed. Nabatieh strikes 11 April killed 10 including three emergency workers. Washington talks (Israel-Lebanon) confirmed for next week, framed as preliminary by Lebanese source.
- H1 saturation check introduced: Five of five cases triggered H1. Framework pattern-matching risk now a standing flag requiring explicit per-case assessment each edition.
- PCP Step 1.5 (New Signal Check) first execution: Three signals assessed — none met new case threshold. South Korea envoy to Iran (Case B addressable), three Iranian nationals ICE custody (domestic enforcement, no case threshold met), Pope Leo XIV condemnation (noise).
- Gate 0.5 operationalised in fact tables: AIS single-source and Iranian state media single-source flagged in source attribution column on every relevant row.
- Claim-type labelling [FACT]/[INFERENCE]/[PREDICTION] applied across all five case Part 2 sections.
- Deferred outcome disconfirmation conditions stated for all eleven open predictions.

### Edition 018 — Key Findings (Morning Sweep 1221 GMT 11 April)

- PRED-017-E CONFIRMED — CRITICAL: Abqaiq struck 8 April. ESA satellite imagery confirmed.
- GL 134A lapsed 1201 EDT 11 April confirmed. GL 134B not on OFAC register at sweep.
- Islamabad talks commenced 11 April. Proximity format. Both delegations arrived.
- Hormuz Day 3: 2 ships. 600+ large vessels stranded. IRGC mine hazard confirmed. Toll model: $2M/tanker.
- Lebanon: 1,953+ killed. Strikes continued 11 April.
- New forward flags: PRED-018-B and PRED-018-E.

### Edition 017 — Key Findings

- Islamabad Day 1 active. US: Vance, Witkoff, Kushner. Iran: Ghalibaf, Araghchi, Hemmati, Ahmadian. 71 personnel.
- Ghalibaf: “We have goodwill but we do not trust.” Preconditions assessed performative.
- GL 134A expired 1201 EDT 11 April. No GL 134B confirmed.
- Hormuz: 5-9 transits/day vs 135 pre-war. Toll model operational.
- SESSION_STATE CORRECTION (Ed016): IRGC attack 7-8 April was coordinated campaign — Petroline (-700K b/d), Manifa (-300K b/d), Satorp, Ras Tanura, Samref, Riyadh refineries, Juaymah.
- Lebanon: 1,953+ killed. 303+ killed 8 April single day record.

### Edition 016 — Key Findings

- GL 134A lapse anticipated. Extension agreed in principle but never formalised.
- Iran controls both Hormuz and Petroline simultaneously — structural leverage maximum.
- OFAC staffing constraint: licensing division at 22 of 40 staff (CARRY-FORWARD — not re-verified Ed019).

### Edition 015 — Key Findings

- PRED-014-A CONFIRMED — ceasefire extended, talks continued May/June per Wikipedia forward record.
- Hemmati in delegation — sanctions relief on economic track.
- Downblending vs dismantlement is the single binary determining whether permanent agreement is possible.

### Edition 014 — Key Findings

- Ghalibaf preconditions: Lebanon ceasefire AND asset release (~$7bn frozen).
- Hormuz franchise confirmed: 15/day cap, Larak corridor, IRGC approval, fees up to $2M/tanker.
- Hajj-Hormuz convergence: ceasefire expires 22 April, zero Iranian pilgrims in Saudi Arabia — no IRGC domestic cost.

-----

## CARRY-FORWARD FACTS — NOT RE-VERIFIED AT ED019

The following facts were carried forward from earlier editions and were NOT independently re-verified at the Ed019 1600 GMT sweep. Must be re-verified at Ed020 or flagged “CARRY-FORWARD FROM EDITION [N] — NOT RE-VERIFIED” in the Part 1 fact table:

|Fact                                                           |Last Verified |Edition              |
|---------------------------------------------------------------|--------------|---------------------|
|Abqaiq damage extent (ESA imagery)                             |8 April 2026  |Ed018                |
|SAMREF Yanbu drone strike (3 April, minimal operational impact)|3-4 April 2026|Ed017                |
|600+ large vessels stranded figure                             |~10 April 2026|Ed018                |
|Saudi March export avg 4.355M bpd (Kpler)                      |30 March 2026 |Ed019 (carry-forward)|
|OFAC staffing at 22 of 40                                      |Ed016 origin  |Ed016                |
|Yanbu 3.9M bpd week of 30 March (Kpler)                        |30 March 2026 |Ed019 (carry-forward)|

-----

## NEXT EDITION TRIGGERS — PRIORITY ORDER FOR EDITION 020

|Timing          |Trigger                                    |Action                                                  |
|----------------|-------------------------------------------|--------------------------------------------------------|
|IMMEDIATE       |GL 134B on OFAC register                   |Resolve PRED-008-D; assess H6 suppressed intersection   |
|MORNING 12 APRIL|Islamabad Day 2 outcome / communique       |PRED-017-A primary trigger. Window closes 14 April      |
|MORNING 12 APRIL|New IRGC Aramco strike — especially Yanbu  |PRED-018-E activation                                   |
|MORNING 12 APRIL|Hormuz transit volume update (Day 5)       |PRED-018-B monitoring                                   |
|MORNING 12 APRIL|Ceasefire violation reports / kinetic event|Case A/E tag review                                     |
|12-14 APRIL     |Islamabad Day 2-3 / communique or departure|PRED-017-A window closes 14 April                       |
|15 APRIL        |Washington Israel-Lebanon talks            |PRED-017-C trigger                                      |
|15 APRIL        |GL 134B trigger                            |No GL 134B by 15 April = PRED-008-D ESCALATING CONFIRMED|
|19 APRIL        |GL U expiry                                |Second waiver window closes                             |
|22 APRIL        |Ceasefire expiry                           |PRED-015-A resolution                                   |
|WATCH           |Oman formal Hormuz coordination            |Upgrade PRED-002-B to DEVELOPING                        |
|WATCH           |Abqaiq repair status confirmed             |Resolve Case E H-E1 or H-E2                             |
|WATCH           |Israeli Lebanon strike intensity change    |Case C tag review; PRED-017-C early signal              |

-----

## SOURCE REGISTRY

- SOURCE_REGISTRY.json v1.4.0 — 44 sources registered
- 18 core mandatory sweep feeds (mandatory_sweep: true)
- 26 supplementary feeds
- Gate 0.5 fields per entry: upstream_dependency and independent_origination
- get_source_info() function in build_core.py — auto-classifies tier, category, incentive baseline, upstream dependency by domain

Critical Gate 0.5 findings (standing — applied from Ed019):

- AIS cluster (MarineTraffic, Kpler, S&P Global, Windward) — shared AIS network — single-source for transit volume
- Iranian state media cluster (IRNA, IRIB, Mehr, WANA, Press TV, Fars, Tasnim) — shared editorial apparatus — single-source
- Reuters and AP are originating wires — all citing outlets are downstream, not independent
- Wikipedia and ACLED are downstream of same Tier 1/2 feeds already swept

-----

## ARCHITECTURE PATCHES

### v1.2.1 — COMMITTED 11 April 2026

Gate 0.5, claim-type labelling, Leg 1/Leg 2 split, Tier 4 dependency test, deferred outcome disconfirmation rule, H1 saturation check, calibration audit at Edition 025, PCP Step 1.5, Wikipedia usage rule (Sections 3 and 16), SYSTEM_CHANGE_LOG Entry Type B, four new named failure modes, PDF visual template updated, architecture change control section added.

NOTE on raw CDN lag: Repository blob view confirmed v1.2.1 on 11 April 2026 (screenshot confirmed). raw.githubusercontent.com CDN was serving v1.1.3 at time of Ed019 session due to caching lag. If raw fetch returns v1.1.3, treat SESSION_STATE.md as governing document and apply v1.2.1 rules in full.

### No further patches pending.

-----

## OPEN BUILD TASKS

- [ ] Upload logo files to repository — atollsphere_logo_v2.png and ls_logo_v2.png
- [ ] Claude Code: patch build_core.py — logos in PDF header and cover
- [ ] Claude Code: patch build_core.py — update get_source_info() to read upstream_dependency and independent_origination from SOURCE_REGISTRY.json v1.4.0
- [ ] Claude Code: patch build_core.py — Gate 0.5 upstream flag in fact table source attribution column
- [ ] Claude Code: patch build_core.py — Leg 1/Leg 2 sub-row rendering in hypothesis tables
- [ ] Claude Code: patch build_core.py — domain quality assessment as distinct styled block at close of Part 2
- [ ] Claude Code: patch build_core.py — upstream_dependency in sources section (grey italic)
- [ ] Update PREDICTION_LOG.json in repository — current through Edition 019 (repo version stale at Edition 013)
- [ ] Backfill status_history and confidence_at_prediction for Editions 001-012 when log data available

-----

## NAMED FAILURE MODES — IN FORCE FROM EDITION 019

- Theatre of Rigor — skeleton structure without consistent execution
- Claim-Type Conflation — facts, inferences, predictions in undifferentiated prose
- Source Amplification — downstream echoes of single upstream treated as independent corroboration
- Escape-Hatch Assignment — WATCH/PARTIAL/AMBIGUOUS used to preserve preferred narrative

-----

## SESSION INSTRUCTIONS FOR CLAUDE — READ CAREFULLY BEFORE ANY ACTION

### STEP 0 — FETCH ARCHITECTURE AND BUILD FILES BEFORE ANYTHING ELSE:

Fetch these files in order before any other action:

1. Fetch ARCHITECTURE.md from https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/ARCHITECTURE.md — read in full
1. Fetch SYSTEM_CHANGE_LOG.md from https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/SYSTEM_CHANGE_LOG.md — apply all active rules
1. Fetch build_core.py from https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/build_core.py — read before building any PDF
1. Fetch styles.py from https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/styles.py — read before building any PDF
1. Confirm v1.2.1 rules understood before proceeding

If raw CDN returns v1.1.3: Note the lag, treat SESSION_STATE.md as governing document, apply all v1.2.1 rules as specified in this document. Do not delay the build pending CDN update.

Do not build any edition until all five files have been fetched and read.

### TO BUILD AN EDITION — EXACT SEQUENCE MANDATORY:

Step 1 — Sweep: Fetch all 18 named core feeds (mandatory_sweep: true in SOURCE_REGISTRY.json). Gate 0.1-0.5 applied to all candidate facts. Gate 0.5 upstream dependency checked against SOURCE_REGISTRY.json v1.4.0 before treating any fact as multiply-corroborated. Fewer than 18 feeds swept = bypass declared.

Step 1.5 — New Signal Check: Mandatory paragraph before prediction reconciliation: “Is there any development in this sweep that does not fit any existing case and cannot be addressed within one?” If yes: assess against new case threshold. Cannot be bypassed.

Step 2 — Prediction Log Reconciliation: Every open prediction assessed. Five-state outcome assigned to closed windows. WATCH/PARTIAL/AMBIGUOUS assignments must state what evidence would have produced CONTRADICTED. No silent drops.

Step 3 — Case Continuity Check: (a) status tag still accurate? (b) hypothesis set overtaken? (c) Forward Flag window expired?

Step 4 — Full CDIT on every case — NO SILENT BYPASSES:

- Part 1: Fact table with Gate 0.1-0.5 on every row. Source attribution column includes tier AND upstream dependency. “Upstream: [named feed or INDEPENDENT].”
- Part 2: Each heuristic finding opens with [FACT], [INFERENCE], or [PREDICTION]. H1 saturation check mandatory (5 of 5 cases triggered H1 in Ed019 — standing flag active). If H1 fires on 3+ cases this edition, each H1-affected Part 2 must ask: “Is H1 the correct heuristic here, or is the framework pattern-matching?” AFC mandatory — label its own claims. Domain quality assessment = distinct labelled block, not embedded prose.
- Part 3: Minimum 2 hypotheses. dominant_hyp_prob_upper <60% = MEDIUM cap. Where Tier 4 data involved: Leg 1 (Tier 1/2 only, must independently sustain range) and Leg 2 (Tier 4 directional only) mandatory.
- Part 4: (1) assumptions; (2) fragile fact with tier; (3) high-impact uncertainty; (4) Tier 4 dependency test if any hypothesis relies on Tier 4 data. WATCH/PARTIAL/AMBIGUOUS must state CONTRADICTED condition.
- Part 5: CONFIRMS/CONTRADICTS pairs. Gate 5 Framing Revision Trigger required.

Step 5 — Forward Flag: One per case. All C1-C5 criteria. Five-state pre-assignment mandatory. Wikipedia cannot satisfy C3 as sole or primary evidence.

Step 6 — Build PDF: Read build_core.py and styles.py from repository before building. ARCHITECTURE.md Section 13 visual template. Output to /mnt/user-data/outputs/ and present. Inline prose or markdown does NOT constitute a valid edition.

### OTHER INSTRUCTIONS:

- Architecture version is v1.2.1 — all rules in ARCHITECTURE.md v1.2.1 are in force
- Entry 001 and AI-001 through AI-004 are all active
- Edition 020 is the morning sweep for 12 April — primary focus: Islamabad Day 2 outcome and GL 134B status
- First sweep task: OFAC register (GL 134B) and Islamabad statement/departure status
- If asked to commit files to GitHub: flag that Claude Code is required for that step
- Calibration audit scheduled for Edition 025 — track prediction accuracy from Ed019 forward