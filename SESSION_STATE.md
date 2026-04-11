# ATOLLSPHERE SESSION STATE

## Paste this at the start of every new Sonnet chat session.

-----

## INTER-EDITION INTELLIGENCE CHECK — EXECUTE BEFORE STEP 0

**Claude: before fetching ARCHITECTURE.md, execute the following live checks in order and record findings in this block. This is mandatory pre-session work, not optional.**

1. Fetch https://ofac.treasury.gov/selected-general-licenses-issued-ofac — confirm whether GL 134B (Russia-related) appears on the register. Record: ISSUED or NOT ISSUED, and timestamp.
1. Search for Islamabad talks outcome — any joint communique, agreed framework, delegation departure, or continuation into Day 3 confirmed since 0100 GMT 12 April. Record: COMMUNIQUE / DEPARTURE / CONTINUING / NO UPDATE.
1. Search for new IRGC strikes on USN mine clearance vessels in Hormuz, or on Saudi Aramco infrastructure (especially Yanbu Red Sea terminal) — since 0100 GMT 12 April. Record: USN STRUCK / NEW ARAMCO STRIKE / NO NEW STRIKE.
1. Search for Hormuz transit volume update (Kpler or MarineTraffic) — any material change from weekend figure of ~10-11 ships/day. Record finding with source.
1. Search for ceasefire violation reports, kinetic events (US, Iran, or Israeli), or delegation departure from Islamabad since 0100 GMT 12 April. Record finding.

Record all five findings here before proceeding to STEP 0. If a finding materially changes a case status tag, note it explicitly — it may trigger a Bypass Override for that case in Edition 021.

**EDITION 021 PRIORITY ALERTS (check these first within each check above):**

- GL 134B: 15 April trigger is NOW 3 DAYS AWAY. Any issuance resolves PRED-008-D. Absence by 15 April = PRED-008-D ESCALATING CONFIRMED.
- USN mine clearance vessels in Hormuz: kinetic engagement = immediate Case B/E ESCALATING CRITICAL reassessment. Non-engagement = H-E1 dominance upgrade.
- Islamabad Day 3: PRED-017-A window closes 14 April. Communique, departure, or extension-without-document all require assessment.
- PRED-020-B forward flag: USN-IRGC binary observable — kinetic or non-kinetic response within 24-48 hours of Ed020 sweep.

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
├── SESSION_STATE.md             # active session state — plain, no Claude Code block
├── SOURCE_REGISTRY.json         # v1.4.0 — 44 sources, Gate 0.5 fields added
├── SYSTEM_CHANGE_LOG.md         # Entries 001, AI-001, AI-002, AI-003, AI-004
├── build_core.py                # includes get_source_info() function
├── build_edition.py
├── build_master.py
└── styles.py
```

-----

## CURRENT EDITION

- Last completed: Edition 020 Morning Sweep — 12 April 2026 (sweep timestamp ~0100 GMT)
- Next: Edition 021 Evening Sweep — 12 April 2026 (run before 2000 BST / 1900 GMT)
- Critical window: Islamabad Day 3 — PRED-017-A window closes 14 April
- Critical window: GL 134B — 15 April trigger now 3 days away
- Critical window: USN mine clearance / IRGC response — 24-48 hour binary observable
- War day: 45

-----

## ACTIVE CASES — POST-EDITION 020 STATUS

|Case|Title                                                                                            |Tag                |Confidence|Post-Ed020 Status                                                                                                                                                                                                                                                                                                                                                                                                  |
|----|-------------------------------------------------------------------------------------------------|-------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|A   |Islamabad Process — Day 2 Active / Written Texts Exchanged / Stalemate on Hormuz                 |ESCALATING         |MEDIUM    |Talks extended past midnight (~0100 GMT). Written texts exchanged — highest format yet. Stalemate on Hormuz sovereignty. No communique. No departure. PRED-017-A PENDING. Window closes 14 April. H-A2 dominant (40-55%): talks continue past 14 April without communique.                                                                                                                                         |
|B   |Hormuz — Franchise Operational / USN Mine Clearance Active / Weekend Transit Below Threshold     |ESCALATING         |HIGH      |Weekend Day 4-5: 10-11 ships/day (MarineTraffic/Kpler, AIS single-source). Highest since March. USN guided-missile destroyers in Hormuz (mine clearance) — first since war began. Iran threatened attack, accused US of ceasefire violation. Qatar maritime resumption Sun 0600 (Gulf, not Hormuz). PRED-018-B on track CONFIRMED. PRED-020-B binary observable pending.                                           |
|C   |Lebanon / Hezbollah — Op Eternal Darkness / Hezbollah Strikes Ashdod / Washington Talks Confirmed|ESCALATING         |HIGH      |1,953+ killed (Health Ministry 10 Apr — carry-forward). Op Eternal Darkness ongoing. Relative lull in Beirut 10-11 Apr. Hezbollah struck Ashdod naval base 10 Apr. Washington talks confirmed for next week (State Dept). Lebanon PM postponed Washington trip 11 Apr. PRED-017-C window 15 April. H-C3 collapse risk 10-15%.                                                                                      |
|D   |India Oil Waiver — GL 134A Lapsed / GL 134B Absent / 15 April Trigger T-3 Days                   |ESCALATING         |HIGH      |GL 134A lapsed 1201 EDT 11 April CONFIRMED. GL 134B NOT on OFAC register at ~0030 GMT 12 April (direct fetch). GL U active through 19 April (7 days remaining at Ed020). 15 April trigger: 3 days away. H-D2 dominant (55-70%).                                                                                                                                                                                    |
|E   |Saudi Aramco — IRGC Control Persists / 1.3M bpd Officially Disclosed / April Liftings Restricted |ESCALATING CRITICAL|HIGH      |No new Yanbu strike at Ed020 sweep. PRED-018-E PENDING. NEW Ed020: Aramco officially disclosed 1.3M bpd production loss (11 April) — 600K bpd upstream field loss, 700K bpd Petroline throughput loss. Aramco restricted April liftings to Arab Light from Yanbu only — first explicit wartime supply allocation. USN Hormuz entry creates IRGC escalation trigger. PRED-020-E binary observable pending 24-72 hrs.|

-----

## PREDICTION LOG — OPEN PREDICTIONS ONLY

|Ref       |Flag                                                                                                                                                                                          |Window                                            |Status                                                                                                                                                                                                                                                                                          |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|PRED-001-A|Futures volume anomaly / BETS OFF Act / Section 122 CIT                                                                                                                                       |CIT proceedings ongoing                           |PENDING. No update Ed020. CONTRADICTED condition: CIT drops Section 122 challenge entirely.                                                                                                                                                                                                     |
|PRED-002-B|Iran-Oman Hormuz protocol into ceasefire language — toll model emerging                                                                                                                       |Monitor Islamabad                                 |WATCH. Oman formal coordination not confirmed. Qatar maritime resumption (Gulf, not Hormuz) does not constitute Oman protocol. CONTRADICTED condition: Oman formally denies any transit coordination role.                                                                                      |
|PRED-005-A|Section 122 CIT oral arguments                                                                                                                                                                |No date confirmed                                 |PENDING. No update Ed020.                                                                                                                                                                                                                                                                       |
|PRED-006-A|GCC emergency meeting post-UNSC veto                                                                                                                                                          |Post-ceasefire                                    |WATCH. No GCC emergency meeting announced. Saudi FM bilateral call with Iranian FM is not GCC convening. CONTRADICTED condition: GCC formally declines to convene.                                                                                                                              |
|PRED-008-B|Houthi BAM threat not activated                                                                                                                                                               |Monitor                                           |DE-ESCALATING. BAM not activated at Ed020 sweep. CONTRADICTED condition: IRGC announces BAM closure or confirmed BAM shipping strike.                                                                                                                                                           |
|PRED-008-D|India oil waiver — GL 134A lapsed 11 April; GL U expires 19 April                                                                                                                             |15 April (GL 134B trigger); 19 April (GL U expiry)|ESCALATING. GL 134A lapsed confirmed. GL 134B NOT on OFAC register at Ed020 sweep (~0030 GMT 12 Apr). 15 April: no GL 134B = ESCALATING CONFIRMED. CONTRADICTED condition: GL 134B issued before 15 April.                                                                                      |
|PRED-015-A|Formal ceasefire extension 14+ days beyond 22 April announced by US and Iran before 22 April                                                                                                  |22 April 2026                                     |PENDING. LOW-MEDIUM probability. Islamabad talks active. No extension announced. CONTRADICTED condition: US or Iran formally terminates ceasefire before 22 April without extension.                                                                                                            |
|PRED-017-A|Islamabad proximity talks produce written joint communique or agreed framework document by 14 April 2026                                                                                      |12-14 April 2026                                  |PENDING. Day 2: written texts exchanged, talks past midnight, no communique. Stalemate on Hormuz sovereignty confirmed. H-A2 dominant. Window closes 14 April. CONTRADICTED = departure without document before 14 April. AMBIGUOUS = talks continue past 14 April, no communique, no departure.|
|PRED-017-C|Israel agrees verifiable pause or reduction in Lebanon strikes at or before 15 April Washington talks                                                                                         |15 April 2026                                     |PENDING. Op Eternal Darkness ongoing. Relative lull in Beirut 10-11 Apr but southern Lebanon/Bekaa continuing. Washington talks confirmed but Lebanon PM postponed trip. CONTRADICTED = Israel formally states no reduction regardless of talks outcome.                                        |
|PRED-018-B|Hormuz daily transit volume fails to reach 15 ships/day at any point before 15 April                                                                                                          |15 April 2026                                     |PENDING. Weekend: 10-11/day (highest since March, AIS single-source). Still below threshold. Iran halted traffic 9 Apr then partially resumed. USN mine clearance creates uncertainty. On track toward CONFIRMED. CONTRADICTED = >15/day for 3+ consecutive days before 15 April.               |
|PRED-018-E|IRGC conducts follow-on strike on Saudi Aramco Yanbu Red Sea terminal before 22 April ceasefire expiry                                                                                        |22 April 2026                                     |PENDING. No new Yanbu strike at Ed020 sweep. USN Hormuz entry creates escalation trigger. PRED-020-E binary observable pending. CONTRADICTED = Abqaiq repaired and Yanbu terminal confirms full unrestricted operations before 22 April.                                                        |
|PRED-019-A|If Islamabad talks produce no communique by 14 April and both delegations remain without departure, AtollSphere flags PRED-017-A AMBIGUOUS and assesses whether structural extension warranted|14 April 2026                                     |PENDING. NEW — issued Ed020. Monitors continuation-without-document scenario.                                                                                                                                                                                                                   |
|PRED-020-B|USN mine clearance vessels in Hormuz: kinetic IRGC response OR non-engagement — binary observable within 24-48 hours of Ed020 sweep                                                           |13-14 April 2026                                  |PENDING. NEW — issued Ed020. Highest-priority short-window flag. CONFIRMED (kinetic): IRGC attacks USN vessels = Case B/A/E ESCALATING CRITICAL reassessment. CONFIRMED (non-kinetic): no IRGC response = H-E1 dominance upgrade, ceasefire tolerance signal.                                   |
|PRED-020-C|Washington Israel-Lebanon-US talks (15 April) produce verifiable commitment by Israel to pause/reduce Lebanon strikes OR conclude without commitment                                          |15 April 2026                                     |PENDING. NEW — issued Ed020. Lebanon PM postponement is early downside signal.                                                                                                                                                                                                                  |
|PRED-020-D|GL 134B not on OFAC register by 15 April = PRED-008-D ESCALATING CONFIRMED; triggers new forward flag for 19 April GL U expiry                                                                |15 April 2026                                     |PENDING. NEW — issued Ed020. T-3 days from Ed020 sweep.                                                                                                                                                                                                                                         |
|PRED-020-E|USN mine clearance creates IRGC escalation decision point — kinetic IRGC response (Case E CONFIRMED escalation) or non-response by 15 April (H-E1 dominance upgrade)                          |13-15 April 2026                                  |PENDING. NEW — issued Ed020. Overlaps with PRED-020-B.                                                                                                                                                                                                                                          |

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

## H1 SATURATION — STANDING FLAG — UPDATED EDITION 020

H1 fired on all five cases in both Edition 019 and Edition 020. In Edition 021, each Part 2 must explicitly ask: “Is H1 the correct heuristic here, or is the framework pattern-matching?” Answer required before proceeding.

Edition 020 H1 audit finding: H6 (Suppressed Intersection) is analytically primary in Cases B, D, and E. The USN Hormuz mine clearance operation is the single event creating H6 intersections across all five cases simultaneously. H1 saturation flag remains active through Edition 025 calibration audit.

-----

## KEY ANALYTICAL FINDINGS — CUMULATIVE THROUGH EDITION 020

### Edition 020 — New Findings (Morning Sweep ~0100 GMT 12 April)

- Islamabad talks extended past midnight into Day 2. Written texts exchanged — highest format of engagement in the war. Both delegations remain in Islamabad at sweep. Stalemate confirmed on Hormuz sovereignty. Iran’s four non-negotiable conditions include full Hormuz sovereignty, complete war reparations, unconditional asset release, and durable West-Asia ceasefire. No communique. PRED-017-A moving toward AMBIGUOUS (H-A2 dominant, 40-55%).
- USN guided-missile destroyers entered Hormuz 11 April — first US vessels in strait since war began. CENTCOM: mine clearance operation. Iran threatened attack; formally accused US of ceasefire violation. Iranian state TV and Pakistani source denied any US vessel passed through. Highest-stakes kinetic development of Edition 020. PRED-020-B binary observable: 24-48 hours.
- Hormuz transit weekend uptick: 10-11 ships/day Saturday-Sunday (MarineTraffic/Kpler via Daily Sabah). Highest since early March. Still well below 15/day disconfirmation threshold. AIS single-source constraint applies. Iran halted traffic 9 April post-Lebanon strikes then partially resumed.
- Qatar Ministry of Transport: Full maritime navigation resumption announced Sunday 0600 — Persian Gulf only, not Hormuz. Does not constitute Hormuz freedom of navigation or Oman protocol.
- Aramco 1.3M bpd disclosure (11 April): Officially confirmed — 600K bpd upstream field loss, 700K bpd Petroline throughput loss. Supersedes Ed018 Bloomberg “limited damage” characterisation. Aramco restricted April liftings to Arab Light from Yanbu only — first explicit wartime supply allocation.
- GL 134B confirmed NOT ISSUED at ~0030 GMT 12 April (direct OFAC page fetch). 15 April trigger: 3 days. H-D2 dominant (55-70%).
- No new IRGC Yanbu/Aramco strike since 1600 GMT 11 April. PRED-018-E PENDING.
- Lebanon: 1,953+ killed (carry-forward — likely higher given continued strikes). Hezbollah struck Ashdod naval base 10 April in response to Op Eternal Darkness. Relative lull in Beirut 10-11 April. Washington talks confirmed for next week (State Dept). Lebanon PM postponed Washington trip 11 April.
- H1 saturation audit (Ed020): H6 analytically dominant in Cases B, D, E. USN Hormuz entry is the single-event H6 intersection across all five cases.
- Five new forward flags issued: PRED-019-A, PRED-020-B, PRED-020-C, PRED-020-D, PRED-020-E.
- New signal check (PCP Step 1.5): Five signals assessed — none met new case threshold.

### Edition 019 — Key Findings (Evening Sweep 1600 GMT 11 April)

- Islamabad talks confirmed as at least partially DIRECT — first US-Iran direct high-level engagement since 1979. No communique at 1600 GMT.
- GL 134B NOT issued at Ed019 sweep. GL 134A lapsed 1201 EDT 11 April. H6 suppressed intersection flagged.
- Hormuz Day 4: ~handful to ~10 ships/day. AIS single-source constraint flagged. PRED-018-B on track toward CONFIRMED.
- No new IRGC Yanbu strike at Ed019 sweep. Lebanon: 1,953+ killed. H-C3 at 10-15%.
- H1 saturation check introduced. PCP Step 1.5 first execution. Gate 0.5 operationalised. Claim-type labelling applied.

### Edition 018 — Key Findings (Morning Sweep 1221 GMT 11 April)

- PRED-017-E CONFIRMED — CRITICAL: Abqaiq struck 8 April. ESA satellite imagery confirmed.
- GL 134A lapsed 1201 EDT 11 April confirmed. GL 134B not on OFAC register at sweep.
- Islamabad talks commenced 11 April. Proximity format. Both delegations arrived.
- Hormuz Day 3: 2 ships. 600+ large vessels stranded. IRGC mine hazard confirmed. Toll model: $2M/tanker.
- New forward flags: PRED-018-B and PRED-018-E.

### Edition 017 — Key Findings

- Islamabad Day 1 active. US: Vance, Witkoff, Kushner. Iran: Ghalibaf, Araghchi, Hemmati, Ahmadian. 71 personnel.
- Ghalibaf: “We have goodwill but we do not trust.” Preconditions assessed performative.
- Hormuz: 5-9 transits/day vs 135 pre-war. Toll model operational.
- IRGC attack 7-8 April was coordinated campaign — Petroline (-700K b/d), Manifa (-300K b/d), Satorp, Ras Tanura, Samref, Riyadh refineries, Juaymah.

### Edition 016 — Key Findings

- GL 134A lapse anticipated. Extension agreed in principle but never formalised.
- Iran controls both Hormuz and Petroline simultaneously — structural leverage maximum.
- OFAC staffing constraint: licensing division at 22 of 40 staff (CARRY-FORWARD — not re-verified Ed020).

### Edition 015 — Key Findings

- PRED-014-A CONFIRMED — ceasefire extended, talks continued May/June per Wikipedia forward record.
- Hemmati in delegation — sanctions relief on economic track.
- Downblending vs dismantlement is the single binary determining whether permanent agreement is possible.

### Edition 014 — Key Findings

- Ghalibaf preconditions: Lebanon ceasefire AND asset release (~$7bn frozen).
- Hormuz franchise confirmed: 15/day cap, Larak corridor, IRGC approval, fees up to $2M/tanker.
- Hajj-Hormuz convergence: ceasefire expires 22 April, zero Iranian pilgrims in Saudi Arabia — no IRGC domestic cost.

-----

## CARRY-FORWARD FACTS — NOT RE-VERIFIED AT ED020

|Fact                                                           |Last Verified |Edition                                      |
|---------------------------------------------------------------|--------------|---------------------------------------------|
|Abqaiq damage extent (ESA imagery)                             |8 April 2026  |Ed018                                        |
|SAMREF Yanbu drone strike (3 April, minimal operational impact)|3-4 April 2026|Ed017                                        |
|400+ large vessels stranded figure                             |~10 April 2026|Ed018 (revised from 600+)                    |
|Saudi March export avg 4.355M bpd (Kpler)                      |30 March 2026 |Ed019 (carry-forward)                        |
|OFAC staffing at 22 of 40                                      |Ed016 origin  |Ed016                                        |
|Yanbu 3.9M bpd week of 30 March (Kpler)                        |30 March 2026 |Ed019 (carry-forward)                        |
|Lebanon total killed at 1,953+                                 |10 April 2026 |Ed019/Ed020 — figure higher by Ed021         |
|GL U active through 19 April                                   |Ed019         |Ed019 (carry-forward — not re-verified Ed020)|

-----

## NEXT EDITION TRIGGERS — PRIORITY ORDER FOR EDITION 021

|Timing          |Trigger                                                   |Action                                                                                                                    |
|----------------|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
|IMMEDIATE       |PRED-020-B: USN mine clearance kinetic/non-kinetic outcome|If IRGC attacks USN: Case B/A/E ESCALATING CRITICAL joint reassessment. If no attack by 13-14 Apr: H-E1 dominance upgrade.|
|IMMEDIATE       |GL 134B on OFAC register                                  |Resolve PRED-008-D CONTRADICTED; assess H6 suppressed intersection                                                        |
|EVENING 12 APRIL|Islamabad Day 2 outcome / Day 3 beginning                 |PRED-017-A primary trigger. Window closes 14 April.                                                                       |
|EVENING 12 APRIL|New IRGC Aramco/Yanbu strike                              |PRED-018-E activation / PRED-020-E resolution                                                                             |
|EVENING 12 APRIL|Hormuz transit volume update                              |PRED-018-B monitoring. Qatar maritime resumption follow-through check.                                                    |
|EVENING 12 APRIL|Ceasefire violation reports / kinetic event               |Case A/B/E tag review. USN mine clearance update.                                                                         |
|13-14 APRIL     |PRED-017-A window closing                                 |Communique / departure / AMBIGUOUS classification                                                                         |
|15 APRIL        |GL 134B trigger                                           |No GL 134B by 15 April = PRED-008-D ESCALATING CONFIRMED                                                                  |
|15 APRIL        |Washington Israel-Lebanon talks                           |PRED-017-C / PRED-020-C trigger                                                                                           |
|19 APRIL        |GL U expiry                                               |Second waiver window closes                                                                                               |
|22 APRIL        |Ceasefire expiry                                          |PRED-015-A resolution                                                                                                     |
|WATCH           |Oman formal Hormuz coordination                           |Upgrade PRED-002-B to DEVELOPING                                                                                          |
|WATCH           |Abqaiq repair status confirmed                            |Resolve Case E H-E1 or H-E2; re-verify carry-forward                                                                      |
|WATCH           |Israeli Lebanon strike intensity change                   |Case C tag review; PRED-017-C early signal                                                                                |

-----

## SOURCE REGISTRY

- SOURCE_REGISTRY.json v1.4.0 — 44 sources registered
- 18 core mandatory sweep feeds (mandatory_sweep: true)
- 26 supplementary feeds
- Gate 0.5 fields per entry: upstream_dependency and independent_origination

Critical Gate 0.5 findings (standing — applied from Ed019):

- AIS cluster (MarineTraffic, Kpler, S&P Global, Windward) — shared AIS network — single-source for transit volume
- Iranian state media cluster (IRNA, IRIB, Mehr, WANA, Press TV, Fars, Tasnim) — shared editorial apparatus — single-source
- Reuters and AP are originating wires — all citing outlets are downstream, not independent
- Wikipedia and ACLED are downstream of same Tier 1/2 feeds already swept

-----

## ARCHITECTURE PATCHES

### v1.2.1 — COMMITTED 11 April 2026

Gate 0.5, claim-type labelling, Leg 1/Leg 2 split, Tier 4 dependency test, deferred outcome disconfirmation rule, H1 saturation check, calibration audit at Edition 025, PCP Step 1.5, Wikipedia usage rule (Sections 3 and 16), SYSTEM_CHANGE_LOG Entry Type B, four new named failure modes, PDF visual template updated, architecture change control section added.

NOTE on raw CDN lag: Repository blob view confirmed v1.2.1 on 11 April 2026. raw.githubusercontent.com CDN was serving v1.1.3 at time of Ed019 and Ed020 sessions due to caching lag. If raw fetch returns v1.1.3, treat SESSION_STATE.md as governing document and apply all v1.2.1 rules in full. Do not delay the build pending CDN update.

-----

## OPEN BUILD TASKS

- [ ] Upload logo files to repository — atollsphere_logo_v2.png and ls_logo_v2.png
- [ ] Claude Code: patch build_core.py — logos in PDF header and cover
- [ ] Claude Code: patch build_core.py — update get_source_info() to read upstream_dependency and independent_origination from SOURCE_REGISTRY.json v1.4.0
- [ ] Claude Code: patch build_core.py — Gate 0.5 upstream flag in fact table source attribution column
- [ ] Claude Code: patch build_core.py — Leg 1/Leg 2 sub-row rendering in hypothesis tables
- [ ] Claude Code: patch build_core.py — domain quality assessment as distinct styled block at close of Part 2
- [ ] Claude Code: patch build_core.py — upstream_dependency in sources section (grey italic)
- [ ] Update PREDICTION_LOG.json in repository — current through Edition 020 (repo version stale at Edition 013)
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

Step 1 — Sweep: Fetch all 18 named core feeds (mandatory_sweep: true in SOURCE_REGISTRY.json). Gate 0.1-0.5 applied to all candidate facts. Gate 0.5 upstream dependency checked before treating any fact as multiply-corroborated. Fewer than 18 feeds swept = bypass declared.

Step 1.5 — New Signal Check: Mandatory paragraph before prediction reconciliation: “Is there any development in this sweep that does not fit any existing case and cannot be addressed within one?” If yes: assess against new case threshold. Cannot be bypassed.

Step 2 — Prediction Log Reconciliation: Every open prediction assessed. Five-state outcome assigned to closed windows. WATCH/PARTIAL/AMBIGUOUS assignments must state what evidence would have produced CONTRADICTED. No silent drops.

Step 3 — Case Continuity Check: (a) status tag still accurate? (b) hypothesis set overtaken? (c) Forward Flag window expired?

Step 4 — Full CDIT on every case — NO SILENT BYPASSES:

- Part 1: Fact table with Gate 0.1-0.5 on every row. Source attribution column includes tier AND upstream dependency.
- Part 2: Each heuristic finding opens with [FACT], [INFERENCE], or [PREDICTION]. H1 saturation check mandatory. AFC mandatory. Domain quality assessment = distinct labelled block.
- Part 3: Minimum 2 hypotheses. dominant_hyp_prob_upper <60% = MEDIUM cap. Leg 1/Leg 2 split mandatory where Tier 4 data involved.
- Part 4: (1) assumptions; (2) fragile fact with tier; (3) high-impact uncertainty; (4) Tier 4 dependency test.
- Part 5: CONFIRMS/CONTRADICTS pairs. Gate 5 Framing Revision Trigger required.

Step 5 — Forward Flag: One per case. All C1-C5 criteria. Five-state pre-assignment mandatory. Wikipedia cannot satisfy C3 as sole or primary evidence.

Step 6 — Build PDF: Read build_core.py and styles.py from repository before building. Output to /mnt/user-data/outputs/ and present. Inline prose or markdown does NOT constitute a valid edition.

### END-OF-SWEEP OUTPUT RULE — MANDATORY FROM EDITION 020:

After the PDF is built and presented, Claude must produce a second output file. This is the Claude Code handoff document. It contains two sections in order and is output as a single .md file.

SECTION 1 — CLAUDE CODE INSTRUCTIONS. Generate this fresh each sweep using the template below, filling in the correct edition number throughout:

-----

You are working on the AtollSphere GSINT intelligence brief platform. Read this entire document before taking any action.

STEP 1 — Fetch and read all live files before making any changes. Fetch and read in full:
ARCHITECTURE.md: https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/ARCHITECTURE.md
SYSTEM_CHANGE_LOG.md: https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/SYSTEM_CHANGE_LOG.md
SOURCE_REGISTRY.json: https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/SOURCE_REGISTRY.json
PREDICTION_LOG.json: https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/PREDICTION_LOG.json
build_core.py: https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/build_core.py
styles.py: https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/styles.py
build_edition.py: https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/build_edition.py
build_master.py: https://raw.githubusercontent.com/domyoung101-max/AttolSphere-/main/build_master.py
Do not take any further action until all eight files have been read in full.

STEP 2 — The SESSION_STATE.md below contains full platform state for Edition [NNN]. Treat ACTIVE CASES, PREDICTION LOG, and KEY ANALYTICAL FINDINGS as ground truth. Update PREDICTION_LOG.json, commit this SESSION_STATE.md, and push all changes. Commit after each step individually.

STEP 3 — Update PREDICTION_LOG.json. Add new forward flags with all required fields. Update statuses. Set outcomes for resolved predictions. Append to status_history for any changed prediction. Never delete existing entries. Never overwrite historical status_history entries.
Commit message: “Edition [NNN] — PREDICTION_LOG.json updated”

STEP 4 — Commit the SESSION_STATE.md in Section 2 of this document exactly as given. Do not modify its content.
Commit message: “Edition [NNN] — SESSION_STATE.md updated for next sweep”

STEP 5 — Verify. Confirm all commits pushed. Report every change made to PREDICTION_LOG.json. Flag anything that could not be completed and explain why.

CONSTRAINTS: Commit after each step. Do not modify ARCHITECTURE.md, SYSTEM_CHANGE_LOG.md, SOURCE_REGISTRY.json, or build files unless explicitly instructed. Do not change analytical content. Flag any conflicts before resolving.

## [SECTION 1 ENDS]

SECTION 2 — UPDATED SESSION_STATE.md. This is the plain session state for the next sweep. Paste the full updated SESSION_STATE.md here exactly as it will be committed to GitHub. No Claude Code instructions. No headers other than the standard SESSION_STATE headers.

## [SECTION 2 ENDS]

The handoff document filename must be: claude_code_handoff_edition_[NNN].md where [NNN] is the edition just completed.

This document is consumed once by Claude Code and is NOT committed to GitHub. What Claude Code commits to GitHub is only the plain SESSION_STATE.md content from Section 2.

SESSION_STATE.md on GitHub must always remain plain — no Claude Code instructions embedded. The handoff document is ephemeral.

The cycle is:
GitHub (plain SESSION_STATE.md) → you paste into Sonnet → sweep runs → PDF output → claude_code_handoff_edition_[NNN].md output → you paste into Claude Code → Claude Code commits to GitHub → repeat.

### OTHER INSTRUCTIONS:

- Architecture version is v1.2.1 — all rules in ARCHITECTURE.md v1.2.1 are in force
- Entry 001 and AI-001 through AI-004 are all active
- Edition 021 is the evening sweep for 12 April — primary focus: USN-IRGC binary outcome, Islamabad Day 2/3, GL 134B status
- First sweep tasks: (1) PRED-020-B USN mine clearance outcome; (2) OFAC register GL 134B; (3) Islamabad statement/departure/continuation
- Calibration audit scheduled for Edition 025 — track prediction accuracy from Ed019 forward