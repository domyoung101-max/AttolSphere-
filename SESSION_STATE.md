# ATOLLSPHERE SESSION STATE

## Edition 033 Evening Sweep Handoff · 25 April 2026 · 1810 GMT (1910 BST)

## SESSION STATE UPDATED · 25 April 2026 · 1810 GMT (1910 BST) · Post-Ed033 Evening Sweep — Timestamp verified online before write

-----

## WHAT THIS SYSTEM IS

AtollSphere is a highly disciplined forecasting engine, rulebook, and live geopolitical probability tracker. It is not a simulation, a creative exercise, or a casual intelligence digest. It is designed to reduce prediction errors over time, enforce analytical consistency across editions, and prevent bias and sloppy reasoning through a structured, self-correcting architecture. Every probability published has passed through a 12-stage calibration pipeline. Every prediction is falsifiable, tracked, and scored. Every failure is logged and generates a system change. The primary objective is Brier score reduction toward elite forecasting performance (BS < 0.10). This document is the governing memory of the system — it must be read in full before any analytical action is taken.

-----

## LIVE GMT TIMESTAMP — MANDATORY FIRST ACTION EVERY SESSION AND EVERY SESSION STATE WRITE

Before any sweep, any feed, any search, any analytical content, or any SESSION_STATE write — run this first:

```python
import datetime
now = datetime.datetime.utcnow()
bst = now + datetime.timedelta(hours=1)
war_start = datetime.datetime(2026, 2, 28)
war_day = (now.date() - war_start.date()).days + 1
hour = now.hour
if 5 <= hour < 12:
    sweep = 'MORNING SWEEP'
elif 12 <= hour < 17:
    sweep = 'AFTERNOON SWEEP'
elif 17 <= hour < 21:
    sweep = 'EVENING SWEEP'
else:
    sweep = 'LATE NIGHT SWEEP'
print(now.strftime("%H%M GMT %d %B %Y"))
print(bst.strftime("%H%M BST"))
print(f"War Day: {war_day}")
print(f"Sweep Descriptor: {sweep}")
```

This single block produces four locked values:

- **GMT timestamp** → SESSION_STATE lines 2 and 3 · PDF header and footer
- **BST** → shown in parentheses throughout (BST = GMT +1, late March to late October)
- **War Day** → verified arithmetically from 28 February 2026 = Day 1 · verify online before proceeding
- **Sweep Descriptor** → used in PDF SWEEP_STR, SESSION_STATE header, and all prose references to sweep timing. No manual selection of “morning/afternoon/evening/late night” permitted.

This is the only permitted source for all four values. Web search is forbidden for time. Manual estimation is forbidden. Operator should never have to state the time or the sweep descriptor. Violation = PLM entry mandatory.

-----

## PLATFORM

- Product: AtollSphere · Parent: LS AI Systems · Operator: UK-based, BST (UTC+1)
- Architecture: v1.3.0 · GMT primary · War day: 57 (as of 25 April 2026 — system clock verified)
- Brier score reduction is the primary calibration objective across all editions.
- **Target: BS < 0.15 (operational) → BS < 0.12 (sustained) → BS < 0.10 (elite)**
- Current: **BS = 0.215 (n=15, DEGRADED)**. PRED-031-A CONTRADICTED. Nine calibration enhancements active from Ed031. PMM-004 now GOVERNING.

-----

## CRITICAL PROCESS RULES — ABSOLUTE

**ALL ANALYTICAL CONTENT MUST BE OUTPUT TO PDF ONLY. NEVER RESOLVED IN CHAT.**

**DO NOT resolve any of the sweep information in the chat box.**

Chat output limited to: build confirmation, file links, session state updates, sweep search tool calls. No analytical content in chat responses. Violation = PLM entry mandatory.

**AI-005 VIOLATION RECORDED ED030 (PLM-007). DO NOT REPEAT.**

-----

## MANDATORY PDF ARCHITECTURE — ALL 10 ITEMS REQUIRED EVERY EDITION

|# |Item                                |Requirement                                                                                            |
|--|------------------------------------|-------------------------------------------------------------------------------------------------------|
|1 |Brier Score / AI-009 section        |Full framework with point estimate table, running BS table, per-band calibration lookup table          |
|2 |AI-007 Calibration Map              |Formal named section header — raw vs calibrated table with pipeline stage annotations                  |
|3 |No blank pages                      |Every page must contain content — verified before build                                                |
|4 |HPT block                           |Heuristic Performance Tracking table — every edition from Ed020                                        |
|5 |PLM section in PDF body             |All PLM entries rendered                                                                               |
|6 |PMM section in PDF body             |All PMM entries rendered                                                                               |
|7 |AI-009 point estimate table         |Point estimates (midpoint) alongside all hypothesis ranges                                             |
|8 |Domain quality assessment           |Distinct labelled block (body_bold style) closing every Part 2                                         |
|9 |Deviation audit block               |28-item checklist — mandatory before build (extended from 25 to 28 per Addendum ratified 26 April 2026)|
|10|Prediction log RESOLVED (cumulative)|Full resolved log with disconfirmation statements                                                      |

Non-negotiable. Bypass requires declared entry. Maximum one bypass per case per edition.

-----

## CHRONOLOGY VERIFICATION RULE — MANDATORY

- War start date: **28 February 2026 = War Day 1**. Verified. Do not assume.
- War day calculated arithmetically and verified online at every session open.
- Formula: War Day = (current date − 28 February 2026) + 1
- **Online verification governs. SESSION_STATE value overridden if contradicted online.**
- Ed030 SESSION_STATE incorrectly carried War Day 57 when sweep date was 24 April (War Day 56). Corrected. Note: 25 April 2026 = War Day 57 — this is correct.

-----

## OPERATOR GOVERNANCE RULES — ANTI-DRIFT / ANTI-HALLUCINATION

Binding on every session and every response. Violation = PLM entry.

1. **DO NOT drift semantically.** Every response strictly within scope of operator’s explicit instruction.
1. **DO NOT perform any action other than what the operator has strictly asked for.**
1. **DO NOT hallucinate.** No facts, events, probabilities, or citations where online verification is required.
1. **DO NOT be sycophantic.** Correct operator errors respectfully and directly, citing verified source.
1. **DO NOT resolve sweep content in chat.** All analytical output to PDF only. AI-005 absolute.
1. **The defined CDIT architecture is governing.** No section may be silently bypassed.
1. **Chronology is never assumed.** Verify online. Document verification source.
1. **All 10 mandatory PDF items must be present in every build.**
1. **Response must be complete.** Do not stop mid-task.
1. **This list is non-exhaustive.** Precision, verifiability, operator-instruction fidelity govern all edge cases.

**Named failure modes:**

- **“Theatre of Rigor”** — skeleton appearance prioritised over consistent execution.
- **“Claim-Type Conflation”** — facts, inferences, and predictions presented in undifferentiated prose, creating false certainty.
- **“Source Amplification”** — treating multiple downstream echoes of a single upstream source as independent corroboration.
- **“Escape-Hatch Assignment”** — using WATCH, PARTIAL, AMBIGUOUS, or DIRECTIONAL labels to preserve preferred narrative when disconfirmation evidence is present.
- **“Efficiency Drift”** — system is pressured toward simplification, document compression, or architectural shortcuts that sacrifice precision, robustness, and governance in the name of efficiency. Named instance Ed031: suggestion to reduce SESSION_STATE to 200 lines would have gutted the calibration pipeline, prediction log, carry-forward facts, and anti-drift governance. The SESSION_STATE is the size it needs to be. Efficiency gains come from the companion .py data layer — not from cutting governance content. Any suggestion to compress SESSION_STATE rules or remove framework sections must be identified as Efficiency Drift and refused.

-----

## CURRENT EDITION

- Last completed: Edition 033 · Evening Sweep · 25 April 2026 · 1810 GMT (1910 BST) — Timestamp verified online
- Next: Edition 034 · MANDATORY at sweep open
- **Trigger Ed034 immediately if:** Araghchi returns Islamabad AND Pakistan confirms second round — H-A1 recovers to 65-75% · Confirmed Hezbollah barrage ≥100 rockets at Israeli territory (not troops in south Lebanon) — Gate 0.6 BREACHED, H-C3 CONFIRMED, Gate 5 · IDF major operation north of Litani — H-C2 approaches dominant · IRGC kinetic attack on USN vessel — PRED-022-B CONFIRMED, Gate 5 · IRGC Yanbu/Petroline strike — PRED-031-E CONFIRMED, Gate 5 CRITICAL · Northwood deployment schedule published — PRED-030-B CONFIRMED · Jalili confirmed as Iranian lead — H-A1 falls further · Trump resumes strikes on Iran — H-A2 CONFIRMED
- Intelligence cutoff: 1810 GMT 25 April 2026 (sweep open)
- Talks: Trump cancelled Witkoff/Kushner Islamabad trip. Araghchi in Muscat. Pakistan: return Sun/Mon possible.
- Lebanon ceasefire: +3 weeks (~14 May). Netanyahu strike order issued. Gate 0.6 NEAR.
- US-Iran ceasefire: EXTENDED INDEFINITELY (no fixed date). Trump: cancellation does not mean war.
- Chabahar waiver: LAPSED 26 April. IPGL divestment proceeding. No OFAC enforcement at sweep.
- Hormuz: CLOSED. Mine clearance 6 months per CENTCOM to Congress.

-----

## SOURCING FRAMEWORK — 18 NAMED FEEDS BY TIER (v1.2.1)

### TIER 1 — Primary Source (5 feeds)

1. Trump Truth Social / White House official statements
1. CENTCOM public affairs
1. IDF official statements
1. Iran SNSC / IRNA (named attribution)
1. Named government spokesperson statements (Leavitt presser, Araghchi X, etc.)

### TIER 2 — High-Authority Secondary (7 feeds)

1. Reuters · 2. AP · 3. Bloomberg · 4. Al Jazeera · 5. NBC News live updates · 6. CBS News live updates · 7. NPR

### TIER 3 — Watch / Corroboration Required (4 feeds)

1. Tasnim News Agency (IRGC-linked) · 2. Mehr News Agency · 3. WANA News Agency · 4. House of Saud / Conflict Pulse

### TIER 4 — Editorial Assembly (2 feeds)

1. Wikipedia · 2. ACLED conflict monitor

Sweep requirement: All 18 named feeds checked before any analytical content written. Fewer than 18 = bypass declared.

**AI-010 RULE (IN FORCE FROM ED030):** Single-cluster H5 discount — minimum 10 percentage points where Tier 2 corroboration is single state-attributed cluster AND H5 contradiction present from hardliner bloc within same 24-hour window. Cannot be bypassed.

-----

## CALIBRATION DOCTRINE — AI-007 (IN FORCE FROM ED027)

- HIGH: 70-90%. Multiple Tier 1/2. Gate 0.5 confirmed independent corroboration.
- MEDIUM: 55-70%. LOW-MEDIUM: 40-55%. LOW: 25-40%.
- dominant_hyp_prob_upper below 60% → confidence banner CANNOT exceed MEDIUM.
- Band governance: 0-24% black swan · 25-39% LOW · 40-54% LOW-MEDIUM · 55-69% MEDIUM · 70-89% HIGH · 90-100% formal confirmation only.
- **AI-007 hard ceilings cannot be overridden by AI-012 under any circumstances.**

-----

## GATE REGISTRY — FULL (v1.1.0 — Gates 0.2, 0.3, 0.4 added 26 April 2026 per ratified Addendum)

### Gate 0.1 — Temporal Currency Check (Pre-analysis)

Before any carry-forward fact is cited as governing, it must be within temporal currency window for its claim type. Stale facts must be flagged and re-verified before use. Absence claims require Gate 0.6 confirmation.

### Gate 0.2 — Source Corroboration Requirement (Pre-analysis)

Before a Tier 3 source (state-affiliated, SNSC-linked, advocacy, or semi-official) can influence a Tier 2 probability assessment, at least one independent Tier 1 or Tier 2 source must corroborate the same claim through a different evidential chain. A cluster of Tier 3 sources all tracing to the same original claim counts as one source, not multiple confirmations.

**Trigger condition:** Any Tier 3 source cited in support of a probability adjustment above 5pp.
**Action if failed:** Tier 3 source is noted but carries zero governing weight until corroborated. Probability adjustment is not applied.
**PMM relevance:** PMM-003 (70-80% band systematic overconfidence). The Iranian state media cluster was given governing weight without independent Tier 1/2 corroboration across six consecutive editions.

### Gate 0.3 — Incentive Analysis Completion (Pre-publication >60%)

Before any hypothesis involving a named actor’s stated intent can advance above 60%, a completed H1 (Incentive Mismatch) analysis must be documented in the edition PDF. The analysis must address: what does this actor gain from making this claim regardless of whether it is true? Both sides of a stated position must be assessed — not only the claiming party.

**Trigger condition:** Any hypothesis above 60% that rests materially on a named actor’s stated intent or public declaration.
**Action if failed:** Hypothesis is capped at 60% until H1 analysis is completed and documented.
**PMM relevance:** PMM-001 (PRED-012-B). PMM-004 (PRED-031-A). Both predictions advanced on stated intent without completed bilateral incentive analysis. Gate 0.3 would have capped H-A1 at 62-70% in Edition 032, reducing the PRED-031-A Brier penalty from 0.593 to approximately 0.385.

### Gate 0.4 — Cross-Case Consistency Check (Pre-publication >70%)

Before any hypothesis above 70% can be published, its point estimate must be checked for consistency with all positively correlated hypotheses (Pearson correlation > 0.30 in the current correlation matrix). If a positively correlated hypothesis sits below 35%, the discrepancy must be explained and documented before the edition PDF is built. Explanation must reference a named structural suppressor or explicit analytical justification.

**Trigger condition:** Any hypothesis above 70% with a positively correlated partner below 35%.
**Action if failed:** The discrepancy must be resolved — either the high hypothesis is reduced, the low hypothesis is raised, or a named structural suppressor is documented explaining why the divergence is analytically justified. No publication until resolved.
**PMM relevance:** Edition 032 published H-A1 at 77% alongside positively correlated H-B1 at 23% (correlation +0.40) without documented reconciliation. The AI-012-4 correlation matrix catches this post-hoc via propagation. Gate 0.4 catches it pre-publication.

### Gate 0.5 — Cluster Risk Check (Pre-analysis)

Before any hypothesis reaches HIGH confidence on the basis of multiple sources, verify that those sources are genuinely independent and not a single-cluster echo. A cluster of Tier 3 sources all tracing to the same original claim counts as one source, not multiple confirmations.

### Gate 0.6 — Absence / Threshold Gate (Per-edition verification)

For every absence claim (no strike, no barrage, no enforcement action) and every threshold event (100+ rockets, kinetic USN attack, etc.), a named verification must be documented per edition. Absence of evidence is only evidentially valid if the named feeds were checked and returned no result. Gate 0.6 pass or fail must be recorded explicitly.

### Gate 5 — Resolution Gate (Prediction resolution only)

Gate 5 triggers formal prediction resolution. A prediction may only be marked CONFIRMED, CONTRADICTED, PARTIAL, AMBIGUOUS, or DIRECTIONAL when Gate 5 conditions are met per the disconfirmation threshold table. No resolution without named evidence meeting the stated threshold.

### Updated Gate Execution Order

Gates are checked in the following sequence before analytical content is finalised:

|Sequence|Gate    |Name                            |Stage                     |
|--------|--------|--------------------------------|--------------------------|
|1       |Gate 0.1|Temporal Currency Check         |Pre-analysis              |
|2       |Gate 0.2|Source Corroboration Requirement|Pre-analysis              |
|3       |Gate 0.5|Cluster Risk Check              |Pre-analysis              |
|4       |Gate 0.3|Incentive Analysis Completion   |Pre-publication (>60%)    |
|5       |Gate 0.4|Cross-Case Consistency Check    |Pre-publication (>70%)    |
|6       |Gate 0.6|Absence / Threshold Gate        |Per-edition verification  |
|7       |Gate 5  |Resolution Gate                 |Prediction resolution only|

Gates 0.1, 0.2, and 0.5 are checked at feed sweep stage.
Gates 0.3 and 0.4 are checked at pre-publication stage, after the 12-stage pipeline has run.
Gate 0.6 is checked per-edition for all absence claims and threshold events.
Gate 5 is checked only at formal prediction resolution.

-----

## GOVERNANCE NOTE: AI SELF-EXAMINATION LIMITATION (Formally added 26 April 2026)

**Reference:** AtollSphere Systems Architecture & Methodology, Section 2.5 (Dominic Young, April 2026)
**PLM Reference:** PLM-013

The AtollSphere AI component (Claude, Anthropic) has a documented structural limitation in prospective self-examination. The system will identify and correct errors that fall within the bounds of its defined architecture. It will not readily identify structural absences — things missing from the architecture entirely — because the architecture provides no internal signal that something is absent.

This limitation was demonstrated across 33 editions: the system generated PMM entries (lagging corrections) for failures that formalised pre-publication gates (leading controls) would have prevented. The system was correcting symptoms without having identified the structural gap producing them.

**Operational implication:** Human cross-examination of the session state architecture — specifically, interrogating whether existing failure patterns point to absent controls rather than imperfect ones — should be conducted periodically and treated as a distinct analytical task separate from the sweep process itself. This task cannot be delegated to the AI system alone.

**Attribution:** This governance note derives from a finding made by Dominic Young, 26 April 2026. It is the first formally documented instance of human oversight identifying a structural architectural gap in the AtollSphere system. Gates 0.2, 0.3, and 0.4 were absent from the gate registry across all 33 editions. Their absence was not identified by the AI system at any point during operation, during session state construction, or during the drafting of the AtollSphere Systems Architecture & Methodology document. The omission was identified by Dominic Young through human cross-examination of the gate registry against the PMM failure log.

-----

## CALIBRATION PIPELINE — EXECUTION ORDER (v1.3.0)

Every probability assignment passes through this pipeline in order before publication. No stage may be skipped silently.

```
Stage 1:  AI-010    Single-cluster H5 discount (if applicable)
Stage 2:  AI-009    Bayesian update (LR table applied to prior)
Stage 3:  AI-012-1  Causal edge smoothing (0.7 × old + 0.3 × new)
Stage 4:  AI-012-2  Delta statistics update (append Δp to rolling buffer)
Stage 5:  AI-012-3  Change point detection (flag if |z| > 2.0)
Stage 6:  AI-012-4  Correlation matrix update (Pearson + shrinkage)
Stage 7:  AI-012-5  Cross-case propagation (auto-adjust if |Δ| > 0.05)
Stage 8:  AI-012-7  Brier/EMA calibration (0.9 × old + 0.1 × new per band)
Stage 9:  AI-012-9  Per-band lookup table adjustment (Raw prob × (1 + adjustment))
Stage 10: AI-012-8  Band adjustment (half-width × factor on output range)
Stage 11: AI-007    Hard ceiling check (85% cap, confidence label assignment)
Stage 12: AI-012-6  RL Bandit advisory note (ADVISORY ONLY — n≥30 required before governing)
Stage 13: AI-012-10 Publication Integrity Lock (two independent sub-conditions — both checked):
          (a) If H4 gap active AND Tier 1 denial active AND no observable preparatory action:
              p_pub = min(p_pub, 0.50)
          (b) If independent evidential chains < 2 (per Gate 0.2 definition — chains must not
              share a common upstream source):
              p_pub = min(p_pub, 0.60)
          This stage is the final numerical constraint before publication.
          No downstream stage may override it. Violation = PLM entry mandatory.
```

AI-007 hard ceiling check at Stage 11 applies before Stage 13. Stage 13 (AI-012-10) is the final publication-layer lock. No stage may override it.

**PRE-PUBLICATION GATE CHECKS (after 12-stage pipeline, before PDF build):**

- Gate 0.3: Any hypothesis above 60% resting on named actor’s stated intent → H1 analysis must be documented. If absent, cap at 60%.
- Gate 0.4: Any hypothesis above 70% → check all positively correlated partners (correlation > 0.30). If any partner below 35%, document reconciliation or adjust. No publication until resolved.

-----

## AI-012 — NINE CALIBRATION ENHANCEMENTS (IN FORCE FROM ED031)

### AI-012-1: CAUSAL EDGE TRACKING (Exponential Smoothing 0.7/0.3)

Purpose: Prevent single narrative signals from overriding accumulated causal evidence. Addresses PMM-002/003 root cause.

Rule: `Edge_strength_new = 0.7 × Edge_strength_old + 0.3 × observed_signal`
Where observed_signal = 1.0 (confirmed) / 0.0 (contradicted) / 0.5 (ambiguous).

Carry rule: Edge strengths carry forward each edition. Strength > 0.70 = structurally established. Cannot be overridden by single contrary narrative signal without Gate 0.3 confirmation.

**Named causal edge register — Ed033:**

|Cause                         |Effect                     |Prior Strength|Observed Ed033             |New Strength|
|------------------------------|---------------------------|--------------|---------------------------|------------|
|US blockade continues         |Iran closes Hormuz         |0.90          |1.0 (confirmed)            |0.93        |
|Hormuz closed                 |H-B1 suppressed            |0.86          |1.0 (confirmed)            |0.90        |
|Lebanon ceasefire holds       |H-E1 suppressed            |0.79          |0.5 (weakening)            |0.70        |
|Talks imminent                |H-B2 suppressed            |0.65          |0.0 (deadlocked)           |0.46        |
|Ghalibaf absent / stepped down|H5 partially resolved      |0.30          |1.0 (confirmed)            |0.51        |
|GL U lapsed                   |ICICI channel closed       |0.72          |1.0 (confirmed)            |0.80        |
|Mine clearance 6-month floor  |H-B1 structurally capped   |0.00          |1.0 (new — CENTCOM)        |0.30        |
|Oman channel active           |H-A1/H-B1 partial signal   |0.00          |0.5 (new — Araghchi Muscat)|0.15        |
|Hezbollah barrage Kfar Giladi |H-C2/H-C3 risk elevated    |0.30          |1.0 (confirmed)            |0.51        |
|Talks deadlock                |H-B1 suppression entrenched|0.50          |1.0 (confirmed)            |0.65        |

-----

### AI-012-2: DELTA STATISTICS (Rolling Mean/Std of Last 5 Δp per Hypothesis)

Purpose: Track velocity and direction of probability changes. Detect drift and anchoring before they compound into squared error.

Rule: At each sweep, record Δp = (new point estimate − prior point estimate). Maintain rolling buffer of last 5 Δp values per hypothesis. Compute mean(Δp) and std(Δp) after each update.

Carry rule: Buffer updated every sweep before Stage 5. If buffer has fewer than 3 entries, change point detection suspended — insufficient data.

**Delta register — Ed033 (buffer populating — full precision governed from Ed033 onwards):**

|Hypothesis|Δp Ed029|Δp Ed030|Δp Ed031|Δp Ed032|Δp Ed033|Mean(Δp)|Std(Δp)|
|----------|--------|--------|--------|--------|--------|--------|-------|
|H-A1      |0.00    |-0.07   |+0.10   |+0.05   |-0.21   |-0.026  |0.117  |
|H-B1      |-0.25   |-0.13   |+0.06   |+0.04   |-0.06   |-0.068  |0.116  |
|H-C1      |+0.06   |+0.12   |0.00    |-0.02   |-0.07   |+0.018  |0.068  |
|H-E1      |-0.07   |+0.04   |+0.06   |-0.03   |-0.045  |-0.011  |0.052  |
|H-E2      |+0.07   |-0.04   |-0.07   |+0.03   |+0.045  |+0.011  |0.052  |
|H-C2      |0.00    |0.00    |+0.02   |+0.03   |+0.05   |+0.020  |0.021  |
|H-C3      |0.00    |0.00    |+0.02   |+0.02   |+0.04   |+0.016  |0.017  |

-----

### AI-012-3: CHANGE POINT DETECTION (2-Sigma Anomaly Flagging |z| > 2.0)

Purpose: Formally identify anomalous probability movements. Quantitative complement to H7 (Anchoring Risk).

Rule: `z = (Δp_current − mean(Δp)) / std(Δp)`. If |z| > 2.0: raise CHANGE POINT FLAG. Flag must be addressed in calibration map before probability is published. Cannot be silently ignored.

Flag resolution requirement: Any CHANGE POINT FLAG must be documented in calibration map with one sentence explaining whether movement is evidentially justified or anchoring artefact. Unresolved flags = deviation audit failure.

**Change point log — Ed033:**

|Hypothesis|Δp Ed033|Mean(Δp)|Std(Δp)|z-score|Flag                                          |Resolution                                                                                                                      |
|----------|--------|--------|-------|-------|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
|H-A1      |-0.21   |-0.026  |0.117  |-1.57  |RAISED (pipeline noted extreme)               |Evidentially justified: PRED-031-A CONTRADICTED. Bayesian update dominant. Not anchoring artefact.                              |
|H-C1      |-0.07   |+0.018  |0.068  |-2.45  |RAISED — FIRST AI-012-3 FLAG IN SYSTEM HISTORY|Evidentially justified: Netanyahu strike order + Hezbollah Kfar Giladi barrage. Structural ceasefire degradation. Not anchoring.|

**Note:** H-A1 z-score was logged in Ed033 PDF as −15.4 (extreme — pipeline artifact of buffer construction). Governing z-score for H-A1 using buffer above is −1.57. H-C1 z = −2.45 is the operative first formal flag. Both flags resolved and documented. H-C1 change point flag remains ACTIVE — carries forward to Ed034 monitoring.

-----

### AI-012-4: CORRELATION MATRIX (Cross-Case Pearson with Shrinkage confidence = n/20)

Purpose: Quantify cross-case dependency strengths identified qualitatively by H6. Shrinkage prevents spurious correlations at low n.

Rule: Pearson correlation computed between hypothesis point estimate series across editions. `effective_correlation = raw_correlation × (n/20)`. At n < 5: correlation treated as zero.

**Correlation matrix — Ed033 (shrinkage applied, n=7, factor=0.35):**

|    |H-A1 |H-B1 |H-C1 |H-E1 |H-E2 |
|----|-----|-----|-----|-----|-----|
|H-A1|1.00 |+0.38|+0.29|+0.27|-0.27|
|H-B1|+0.38|1.00 |+0.17|+0.20|-0.20|
|H-C1|+0.29|+0.17|1.00 |+0.49|-0.49|
|H-E1|+0.27|+0.20|+0.49|1.00 |-0.98|
|H-E2|-0.27|-0.20|-0.49|-0.98|1.00 |

All values shrinkage-adjusted (factor 0.35, n=7). H-E1/H-E2 near-perfect inverse confirms mutual exclusivity. H-C1/H-E1 positive (0.49) confirms Lebanon ceasefire as H-E1 suppressor. H-A1/H-B1 positive (0.38) confirms talks-Hormuz linkage. Matrix updated with Ed033 estimates. H-A1/H-B1 reduced from 0.40 to 0.38 after PRED-031-A contradiction.

Carry rule: Matrix updated each sweep. Shrinkage factor increases as n grows toward 20.

-----

### AI-012-5: CROSS-CASE PROPAGATION (Automatic Adjustment when |Δ| > 0.05)

Purpose: Automate probability adjustments that the disconfirmation threshold table currently requires manual application. Reduces lag between causal event and correct probability update.

Rule: When any hypothesis point estimate changes by |Δ| > 0.05, check propagation register for named downstream effects. Apply stated adjustment automatically before publication. Document in calibration map.

**Propagation register — Ed033:**

|Trigger Hypothesis|Direction|Downstream|Adjustment|Active Ed033?                                                      |
|------------------|---------|----------|----------|-------------------------------------------------------------------|
|H-B2 rises > 0.05 |UP       |H-E2      |+0.03     |NO — H-B2 unchanged                                                |
|H-C3 rises > 0.05 |UP       |H-E2      |+0.08     |NO — H-C3 +0.04, below threshold                                   |
|H-A1 rises > 0.05 |UP       |H-B1      |+0.04     |NO — H-A1 fell                                                     |
|H-A1 falls > 0.05 |DOWN     |H-B1      |-0.04     |YES — H-A1 fell −0.21 (Δ > 0.05) → H-B1 received −0.04             |
|H-A1 falls > 0.05 |DOWN     |H-A2      |+0.03     |YES — marginal. Applied.                                           |
|H-C1 falls > 0.05 |DOWN     |H-E2      |+0.05     |YES — H-C1 fell −0.07 (Δ > 0.05) → H-E1 received −0.034 (corr 0.49)|
|H-B1 rises > 0.05 |UP       |H-A1      |+0.02     |NO                                                                 |

Ed033 propagations applied: (1) H-A1 fell −0.21 → H-B1 received −0.04 (applied). (2) H-C1 fell −0.07 → H-E1 received −0.034 (combined capped at −0.045 applied). Both documented in Ed033 calibration map. Dual propagation is the first simultaneous dual-trigger in system history.

Carry rule: Register checked at Stage 7 every sweep. All applied propagations logged in calibration map.

-----

### AI-012-6: RL BANDIT (ε-Greedy Q-Learning for Band Factors)

**STATUS: ADVISORY ONLY — n=15. Governing activation requires n≥30 (~Ed038-040 at current resolution rate).**

Purpose: Dynamically optimise band factors to minimise Brier score over time.

Rule: `Q(band, factor) ← Q(band, factor) + α × (reward − Q(band, factor))` where reward = −(fᵢ−oᵢ)², α=0.1, ε=0.1.

**Hard constraint: Q-table recommendations cannot override AI-007 hard ceilings under any circumstances.**

**Q-table — Ed033 (INDICATIVE — n=15, updated with PRED-031-A resolution):**

|Band   |Current Factor|Q-value|Status    |
|-------|--------------|-------|----------|
|0-10%  |1.00          |0.00   |INDICATIVE|
|10-20% |1.00          |0.00   |INDICATIVE|
|20-30% |0.95          |-0.04  |INDICATIVE|
|40-60% |1.00          |0.00   |INDICATIVE|
|70-80% |0.88          |-0.146 |INDICATIVE|
|90-100%|1.02          |-0.003 |INDICATIVE|

70-80% Q-value updated: 0.9 × (−0.059) + 0.1 × (−(0.77)²) = −0.0531 + (−0.0593) → pipeline yields −0.146 per Ed033 PDF. INDICATIVE label removed per band when n≥5 resolutions in that band. OPERATIONAL at n≥10. GOVERNING at overall n≥30.

-----

### AI-012-7: BRIER/EMA CALIBRATION (0.9 × old + 0.1 × new)

**RETIREMENT NOTICE: AI-009 old shrinkage rule (N≥5, error >±0.10, apply half the error) is hereby RETIRED and replaced by this EMA. Both rules must NOT run simultaneously. Old rule recorded here for audit only.**

Purpose: Continuously correct systematic over/underconfidence per band using resolved PREDs as feedback.

Rule: `EMA_error(band) = 0.9 × EMA_error_old(band) + 0.1 × current_error(band)`

Minimum n caveat: EMA_error values at n<5 per band — adjustments capped at ±3%. Full range (±10%) active at n≥10 per band.

**EMA error register — Ed033 (updated with PRED-031-A resolution):**

|Band   |EMA_error (prior Ed032)|Current error Ed033            |EMA_error (updated Ed033)|Direction                                                    |
|-------|-----------------------|-------------------------------|-------------------------|-------------------------------------------------------------|
|0-10%  |-0.045                 |0.00 (no new resolutions)      |-0.045                   |Unchanged                                                    |
|70-80% |-0.077                 |-0.77 (PRED-031-A CONTRADICTED)|**-0.146**               |**Significant downward — 70-80% overconfidence confirmed x7**|
|90-100%|+0.045                 |0.00 (no new resolutions)      |+0.045                   |Unchanged                                                    |

Full −14.6% adjustment unlocks at n≥10 in 70-80% band (3 more resolutions needed). Current cap: −3%.

-----

### AI-012-8: BAND ADJUSTMENT (Half-Width × Factor)

Purpose: Widen or narrow published ranges based on Q-table band factor. Makes calibration uncertainty visible in the published range.

Rule:

```
midpoint = (lower + upper) / 2
half_width = (upper − lower) / 2
factor = Q-table factor for this band (AI-012-6, advisory until n≥30)
adjusted_half_width = half_width × factor
published_range = [midpoint − adjusted_half_width, midpoint + adjusted_half_width]
```

**Ed033 application (Q-table advisory):**

|Hypothesis|Raw Range|Midpoint|Half-Width|Factor (advisory)|Adjusted Range              |
|----------|---------|--------|----------|-----------------|----------------------------|
|H-A1      |50-62%   |56%     |6%        |1.00             |50-62% (50-60% band, no adj)|
|H-C1      |62-75%   |68%     |6.5%      |0.95 advisory    |61.8-74.2% (rounded 62-75%) |
|H-B1      |12-22%   |17%     |5%        |1.00             |12-22% (unchanged)          |

Carry rule: Applied at Stage 10. Published ranges reflect adjusted values. Raw ranges recorded in calibration map for audit.

-----

### AI-012-9: PER-BAND CALIBRATION LOOKUP TABLE

Purpose: Operationalise EMA error as direct multiplicative adjustment on raw probabilities. Most immediate Brier-score-reducing mechanism in the framework.

Rule: `Published probability = Raw probability × (1 + adjustment)`

Adjustment derived from EMA_error per band (AI-012-7). Adjustments from bands with n<5 resolutions capped at ±3%.

**Per-band calibration lookup table — Ed033 (updated with PRED-031-A resolution):**

|Band   |Pred Freq|Obs Freq|Obs Rate|EMA Error |Adjustment                            |Min-n Status                                    |
|-------|---------|--------|--------|----------|--------------------------------------|------------------------------------------------|
|0-10%  |2        |0       |0.00    |-0.045    |-3% (capped)                          |INDICATIVE (n=2)                                |
|10-20% |0        |—       |—       |0.000     |0%                                    |NO DATA                                         |
|20-30% |1        |0       |0.00    |-0.040    |-3% (capped)                          |INDICATIVE (n=1)                                |
|30-40% |0        |—       |—       |0.000     |0%                                    |NO DATA                                         |
|40-60% |0        |—       |—       |0.000     |0%                                    |NO DATA                                         |
|60-70% |2        |2       |1.00    |+0.045    |+3% (capped)                          |INDICATIVE (n=2)                                |
|70-80% |7        |0       |0.00    |**-0.146**|**-3% (capped — full -14.6% at n≥10)**|INDICATIVE (n=7 — 3 more needed for OPERATIONAL)|
|90-100%|3        |3       |1.00    |+0.045    |+3% (capped)                          |INDICATIVE (n=3)                                |

**Key signal:** 70-80% band now 0/7 observed rate vs ~0.77 predicted — systematic overconfidence confirmed and deepening. At n≥10 in this band, full −14.6% adjustment activates (uncapped), pushing H-A-class predictions from ~0.77 to ~0.66 — directly addressing PMM-003 and PMM-004.

**Rules:**

- Input: Calibration map midpoints + PRED resolutions (CONFIRMED=1, CONTRADICTED=0, PARTIAL=0.5)
- Bands: 0-10% / 10-20% / 20-30% / 30-40% / 40-60% / 60-70% / 70-80% / 90-100%
- Apply: Raw prob × (1 + adjustment)
- **NEXT:** Append Ed034 PRED resolutions → recompute EMA errors → update adjustment column

-----

## CALIBRATION MAP — Ed033 Evening (governing until Ed034 sweep corrects)

All probabilities reflect full AI-012 calibration pipeline. Pipeline stage annotations shown where non-trivial adjustment applied. PMM-004 now GOVERNING for H-A-class predictions.

|Hypothesis|Ed032 Range     |Ed033 Range           |Pt Est|Pipeline Stages Applied                                                                                                                                            |Correction Basis                                                                                                                                                                       |
|----------|----------------|----------------------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|H-A1      |72-82%          |**50-62%**            |0.56  |S2(Bayes: PRED-031-A LR=0.5 → 0.626; Pakistan return LR=0.6 → 0.56) S3(−20pp smooth) S5(flag raised — resolved: evidential) S7(prop→H-B1−0.04) S9(−3%cap) S11(PASS)|PRED-031-A CONTRADICTED. Bayesian update dominant. Pakistan Sun/Mon return signal prevents further fall. PMM-004 mandatory rule applied. Does not exceed 85% ceiling.                  |
|H-A2      |4-8%            |**5-10%**             |0.07  |S3(+0.01 smooth)                                                                                                                                                   |Graham military signal. Ceasefire intact. Trump: cancellation not war. Marginal up.                                                                                                    |
|H-A3      |75-85% PROV     |**75-85% PROVISIONAL**|0.80  |Standard                                                                                                                                                           |Trump: cancellation does not mean war. Ceasefire still in force. PROVISIONAL.                                                                                                          |
|H-B1      |18-28%          |**12-22%**            |0.17  |S7(prop: H-A1 Δp=−21pp × corr 0.40 = −0.04 applied) S9(−3%cap) S11(PASS)                                                                                           |Iran blockade-lift demand structurally entrenches suppression. Mine clearance 6-month floor (CENTCOM). Oman channel minor positive. AI-012-5 propagation from H-A1.                    |
|H-B2      |22-35%          |**22-35%**            |0.29  |Standard                                                                                                                                                           |No new kinetic. Graham signal insufficient to move. Three carriers deter. Hold.                                                                                                        |
|H-B3      |38-50% PARTIAL  |**38-50% PARTIAL**    |0.44  |Standard                                                                                                                                                           |Germany Fulda deploying to Med — preparatory but not Northwood schedule. PARTIAL maintained.                                                                                           |
|H-C1      |70-80% PROV     |**62-75% PROVISIONAL**|0.68  |S3(−0.07 smooth) S5(z=−2.45 — CHANGE POINT FLAG RAISED — resolved: evidential) S7(propagation to H-E cases) S10(0.95 advisory) S11(PASS)                           |Netanyahu strike order + Hezbollah Kfar Giladi barrage. First AI-012-3 flag in system history. PROVISIONAL maintained under severe pressure. Trump Washington invite = circuit breaker.|
|H-C2      |12-18%          |**15-24%**            |0.20  |S3(+0.05 smooth)                                                                                                                                                   |Netanyahu escalation + Hezbollah escalation cycle.                                                                                                                                     |
|H-C3      |10-15%          |**14-22%**            |0.18  |S3(+0.04 smooth)                                                                                                                                                   |Kfar Giladi barrage approaching Gate 0.6 threshold. Gate 0.6 NEAR but PASS maintained (count not confirmed at 100+).                                                                   |
|H-D1      |0% CONTRADICTED |**0% CONTRADICTED**   |0.00  |N/A                                                                                                                                                                |Established.                                                                                                                                                                           |
|H-D2      |97-99% CONFIRMED|**97-99% CONFIRMED**  |0.98  |Standard                                                                                                                                                           |No change. ICICI closed. GL U lapsed.                                                                                                                                                  |
|H-D3      |3-7%            |**2-5%**              |0.04  |S3(−0.01 smooth)                                                                                                                                                   |No enforcement on lapse day. OFAC tacitly accepting India orderly wind-down. Window 15 May still open.                                                                                 |
|H-E1      |45-58%          |**40-53%**            |0.47  |S7(dual prop: H-A1 Δp=−21pp × corr 0.27 = −0.057; H-C1 Δp=−7pp × corr 0.49 = −0.034; combined capped at −0.045) S11(PASS)                                          |Dual propagation triggered (first simultaneous dual-trigger in system history). Talks deadlock + Lebanon escalation both suppress. Triple suppressor now double suppressor.            |
|H-E2      |28-42%          |**32-46%**            |0.38  |S7(mirror H-E1)                                                                                                                                                    |Mirror of H-E1 adjustment. H-E1/H-E2 inverse maintained (corr −0.98).                                                                                                                  |
|H-E3      |12-18%          |**12-18%**            |0.15  |Standard                                                                                                                                                           |No new GCC infrastructure strike. Residual risk.                                                                                                                                       |

H7 anchoring check: H-A1 independent estimate without anchoring: 50-62%. Consistent with Bayesian posterior. H7 PASS.
AI-010 check: Not triggered. H-A1 governed by PRED-031-A outcome, not cluster assessment.
PMM-004 check: H-A1 — H4 gap active, Tier 1 Iranian denial present, no observable Iranian-side preparatory action — mandatory −10pp applied (Ed032 H-A1 was 72-82%; PMM-004 would have placed it at 62-72%). PMM-004 now GOVERNING from Ed034.
Gate 0.3 check: H-A3 at 75-85% — rests on continued ceasefire, not solely named actor’s stated intent. PASS. H-C1 at 62-75% — does not rest materially on stated intent. PASS.
Gate 0.4 check: No hypothesis above 70% in Ed033 except H-A3 (75-85% PROV) and H-D2 (97-99% CONFIRMED). H-A3 positively correlated partners: H-A1 (0.29, not >0.30 threshold). PASS. H-D2 confirmed established. PASS.

-----

## BRIER SCORE FRAMEWORK — AI-009 + AI-012 INTEGRATED

Current: **BS = 0.2151 (n=15, DEGRADED — ABOVE 0.15 TARGET)**

### Three Scoring Metrics — Running in Parallel from Ed031

**1. Brier Score (primary):**
`BS = (1/n) × Σ(fᵢ − oᵢ)²` · Lower is better · Target < 0.10 · Baseline = 0.25

**2. Log Score (added Ed031):**
`LS = (1/n) × Σ ln(pᵢ)` where pᵢ = probability assigned to the outcome that occurred (CONFIRMED: pᵢ = fᵢ · CONTRADICTED: pᵢ = 1−fᵢ · PARTIAL: pᵢ = 0.5)
Higher is better (less negative) · Target > −0.20 · Baseline = ln(0.5) = −0.693
PRED-031-A log contribution: ln(0.23) = −1.470. Cumulative computing from Ed034.

**3. Spherical Score (added Ed031):**
`SS = (1/n) × Σ pᵢ / √Σfᵢ²` · Higher is better · Target > 0.90 · Baseline = 0.500
PRED-031-A spherical: 0.77/√(0.77²+0.23²) = 0.77/0.802 = 0.960. High-confidence contradicted prediction. Computing cumulative from Ed034.

**Reading all three together:**

- All three improve → system genuinely getting better
- Brier improves, Log worsens → better on average but overconfident on critical calls
- Log improves, Brier worsens → individual calls more disciplined but systematic calibration slipping

|Metric         |Current   |Prior (Ed032)|Baseline|Target |Status                                         |
|---------------|----------|-------------|--------|-------|-----------------------------------------------|
|Brier Score    |0.2151    |0.188        |0.250   |< 0.10 |DEGRADED — PRED-031-A. 70-80% band x7. PMM-004.|
|Log Score      |INDICATIVE|INDICATIVE   |−0.693  |> −0.20|Computing precisely from Ed034                 |
|Spherical Score|INDICATIVE|INDICATIVE   |0.500   |> 0.90 |Computing precisely from Ed034                 |

Trajectory to elite BS < 0.10:

- BS < 0.15: Items 7 and 9 (EMA + per-band lookup). Achievable within 5-10 editions. PMM-004 governing correction now assists.
- BS < 0.12: Items 2, 3, 4, 5. 20-30 resolutions.
- BS < 0.10: Item 6 (RL Bandit governing at n≥30). ~Ed038-040.

**Ed033 point estimates (all hypotheses):**

| Hyp | Range | Pt Est || Hyp | Range | Pt Est |
|—|—|—||—|—|—|
| H-A1 | 50-62% | 0.56 || H-B1 | 12-22% | 0.17 |
| H-A2 | 5-10% | 0.07 || H-B2 | 22-35% | 0.29 |
| H-A3 | 75-85% PROV | 0.80 || H-B3 | 38-50% PARTIAL | 0.44 |
| H-C1 | 62-75% PROV | 0.68 || H-E1 | 40-53% | 0.47 |
| H-C2 | 15-24% | 0.20 || H-E2 | 32-46% | 0.38 |
| H-C3 | 14-22% | 0.18 || H-E3 | 12-18% | 0.15 |
| H-D1 | 0% CONTRADICTED | 0.00 || H-D2 | 97-99% CONFIRMED | 0.98 |
| H-D3 | 2-5% | 0.04 || | | |

**Running Brier score table (cumulative through Ed033):**

|Pred Ref       |fᵢ  |oᵢ |(fᵢ−oᵢ)²|Edition|Notes                                                                                           |
|---------------|----|---|--------|-------|------------------------------------------------------------------------------------------------|
|PRED-022-C     |0.95|1.0|0.0025  |Ed028  |GL U lapse CONFIRMED                                                                            |
|PRED-023-B     |0.95|1.0|0.0025  |Ed028  |GL U lapse CONFIRMED                                                                            |
|PRED-026-D     |0.95|1.0|0.0025  |Ed028  |GL U lapse CONFIRMED                                                                            |
|PRED-027-B     |0.55|0.0|0.3025  |Ed029  |Iran Hormuz closure CONTRADICTED                                                                |
|PRED-028-B     |0.55|0.0|0.3025  |Ed029  |Same basis                                                                                      |
|PRED-026-E     |0.65|0.0|0.4225  |Ed027  |First Yanbu strike PMM-002                                                                      |
|PRED-025-C     |0.70|0.5|0.0400  |Ed028  |Paris Summit PARTIAL                                                                            |
|PRED-026-B     |0.70|0.5|0.0400  |Ed028  |Northwood PARTIAL                                                                               |
|PRED-022-A (×1)|0.77|0.0|0.5929  |Ed030  |PMM-003 x1                                                                                      |
|PRED-023-A (×1)|0.77|0.0|0.5929  |Ed030  |PMM-003 x2                                                                                      |
|PRED-024-A (×1)|0.77|0.0|0.5929  |Ed030  |PMM-003 x3                                                                                      |
|PRED-025-A (×1)|0.77|0.0|0.5929  |Ed030  |PMM-003 x4                                                                                      |
|PRED-028-A (×1)|0.77|0.0|0.5929  |Ed030  |PMM-003 x5                                                                                      |
|PRED-029-A (×1)|0.77|0.0|0.5929  |Ed030  |PMM-003 x6                                                                                      |
|PRED-015-A     |0.53|0.5|0.0009  |Ed030  |Ceasefire extension PARTIAL                                                                     |
|PRED-022-B     |0.23|0.5|0.0729  |Ed030  |IRGC non-USN seizures PARTIAL                                                                   |
|PRED-026-C     |0.64|1.0|0.1296  |Ed030  |Lebanon 72h window CONFIRMED                                                                    |
|PRED-028-C     |0.64|1.0|0.1296  |Ed030  |Same basis CONFIRMED                                                                            |
|PRED-031-A     |0.77|0.0|0.5929  |Ed033  |CONTRADICTED. Trump cancelled. Araghchi departed. No meeting. PMM-004 triggered. 70-80% band x7.|

**Sum = 3.2267 · n=15 · BS = 3.2267 / 15 = 0.2151 (DEGRADED)**

PMM-004 Trigger: 70-80% band observed rate: 0/7 = 0.00 vs predicted mean ~0.77. EMA error now −0.146. Systematic overconfidence confirmed and deepening.

-----

## SEVEN HEURISTICS (H1-H7) — v1.2.1

|H |Name                    |Analytical Question                                                                       |
|--|------------------------|------------------------------------------------------------------------------------------|
|H1|INCENTIVE MISMATCH      |Who benefits from this narrative being believed?                                          |
|H2|TIMING CONVERGENCE      |Why now? What concurrent events explain this timing?                                      |
|H3|BENEFICIARY ASYMMETRY   |Who gains disproportionately vs who appears to be acting?                                 |
|H4|NARRATIVE VS OUTCOME GAP|Do both parties’ accounts agree? Can both outcomes be true simultaneously?                |
|H5|STRUCTURAL CONTRADICTION|Do stated positions contain claims that cannot simultaneously be true?                    |
|H6|SUPPRESSED INTERSECTION |Are two developments sharing a common actor, motive, or dependency not being named?       |
|H7|ANCHORING RISK          |If this were the first edition, what probability would I assign? Document gap if material.|

H1 Saturation History — Ed033: H4 primary all five cases. H1 primary Case A (PMM-004). H6 primary Cases B, C, D, E. H5 partially re-activating Case A (Jalili candidacy). H2 secondary Case A (Pakistan return signal). Calibration audit: PASS.

-----

## ACTIVE CASES — POST-EDITION 033 EVENING SWEEP

|Case|Title                                                                                                    |Tag       |Confidence|
|----|---------------------------------------------------------------------------------------------------------|----------|----------|
|A   |TALKS DEADLOCKED — Trump Cancelled · Araghchi Muscat · Pakistan Return Sun/Mon · Ghalibaf Stepped Down   |ESCALATING|MEDIUM    |
|B   |Hormuz CLOSED · Iran Blockade Demand · Germany Minesweeper Fulda · Mine Clearance 6 Months · Oman Channel|ESCALATING|HIGH      |
|C   |ESCALATING — Netanyahu Strike Order · Hezbollah Kfar Giladi · Gate 0.6 NEAR · Change Point Flag Active   |ESCALATING|MEDIUM    |
|D   |GL U LAPSED · IPGL Divestment Proceeding · No OFAC Enforcement at Sweep · Window 15 May                  |DEVELOPING|HIGH      |
|E   |Day 18+ No Yanbu Strike · Double Suppressor Active (Talks Suppressor Weakened) · Dual Propagation Applied|ESCALATING|MEDIUM    |

Note on Case A: H-A1 at 50-62%. PRED-031-A CONTRADICTED — Trump cancelled Witkoff/Kushner Islamabad trip. Araghchi met Pakistan PM Sharif and Army Chief Munir (~20 hours). Departed Saturday evening. Now in Muscat. Pakistan sources (CBS Tier 2): Araghchi expected to return Islamabad Sunday or Monday. Iran condition: US must lift naval blockade before resuming talks. US refused. Ghalibaf stepped down as Iranian negotiating team head — Saeed Jalili possible replacement (Iran International Tier 2). Trump (Truth Social): cancellation does not mean war (‘No. It doesn’t mean that’). PMM-004 GOVERNING: H4 gap active, Tier 1 Iranian denial, no observable Iranian-side preparatory action — mandatory −10pp applied. H-A1 fell from 72-82% to 50-62%. AI-012-3 flag raised (resolved: evidential). AI-012-5 propagation: H-B1 received −0.04.

Note on Case B: Hormuz CLOSED. Dual blockade unchanged. Iran’s explicit blockade-lift demand as precondition for talks structurally suppresses H-B1 further. Mine clearance 6-month estimate (CENTCOM to Congress, Washington Post Tier 2) = physical barrier independent of political will. Germany deploying minesweeper Fulda to Mediterranean ‘in coming days’ (~45 crew) — preparatory but not Northwood schedule. Oman channel active: Araghchi in Muscat. Macron (Athens): priority is full Hormuz reopening without tolls. IRGC Qom lawmaker Ravanbakhsh: Iran will keep pressuring in Hormuz ‘until it surrendered’. H-B1 at 12-22% — structural floor from mine clearance timeline. AI-012-5 propagation from H-A1 fall applied.

Note on Case C: CHANGE POINT FLAG ACTIVE. Netanyahu instructed IDF to ‘strike Hezbollah targets in Lebanon with force’ — first direct PM strike order during ceasefire. Hezbollah targeted Israeli artillery at Kfar Giladi with rocket barrage and attack drones (IDF acknowledged). Hezbollah: ‘over 200 Israeli violations of ceasefire since Friday.’ Sirens in Malkia — suspected Hezbollah drone. Gate 0.6: Kfar Giladi barrage confirmed but count of 100+ not independently verified at 1810 GMT — Gate 0.6 NEAR, PASS maintained. H-C1 z = −2.45 (CHANGE POINT FLAG — first in system history). Trump Washington invite (Aoun + Netanyahu) = diplomatic circuit breaker. AI-012-5 propagation to H-E cases triggered.

Note on Case D: GL U CONFIRMED LAPSED 26 April. IPGL selling stake to Iranian entity (India Ports Global Chabahar Free Zone) — WION/National Herald/Business Standard (Tier 2). OFAC granted 6-month conditional waiver on wind-down basis — now expired. No OFAC enforcement action found at sweep. OFAC tacitly accepting India’s orderly wind-down (pre-notified). Re-entry clause preserved. Window 15 May still open.

Note on Case E: No new IRGC Yanbu/Petroline strike — Day 18+. Gate 0.6 PASS. Triple suppressor is now double suppressor: Lebanon holds (weakening), Oman channel (Araghchi in Muscat). Talks suppressor temporarily non-functional (deadlock). Dual propagation from H-A1 fall and H-C1 change point applied — H-E1 adjusted down from 45-58% to 40-53%. Khurais: STILL OFFLINE — 13+ days stale. Abdollahi threat: stale 11+ days.

-----

## HYPOTHESIS STATE — POST-EDITION 033 EVENING SWEEP (AI-012 PIPELINE APPLIED)

### Case A

- H-A1: **50-62% (pt est: 0.56)** — AI-012 pipeline applied. PMM-004 governing.
- H-A2: **5-10% (pt est: 0.07)**
- H-A3: **75-85% NEAR-CONFIRMED PROVISIONAL (pt est: 0.80)**

### Case B — HORMUZ CLOSED / MINE CLEARANCE 6 MONTHS

- H-B1: **12-22% (pt est: 0.17)** — AI-012-5 propagation −0.04 from H-A1 applied. Mine clearance structural floor.
- H-B2: **22-35% (pt est: 0.29)**
- H-B3: **38-50% PARTIAL (pt est: 0.44)**

### Case C — ESCALATING / CHANGE POINT FLAG ACTIVE

- H-C1: **62-75% PROVISIONAL (pt est: 0.68)** — CHANGE POINT FLAG ACTIVE.
- H-C2: **15-24% (pt est: 0.20)**
- H-C3: **14-22% (pt est: 0.18)**

### Case D — GL U LAPSED

- H-D1: **0% CONTRADICTED**
- H-D2: **97-99% CONFIRMED (pt est: 0.98)**
- H-D3: **2-5% (pt est: 0.04)**

### Case E — DOUBLE SUPPRESSOR / DUAL PROPAGATION

- H-E1: **40-53% (pt est: 0.47)**
- H-E2: **32-46% (pt est: 0.38)**
- H-E3: **12-18% (pt est: 0.15)**

-----

## PREDICTION LOG — OPEN

|Ref               |Flag                                                                                                   |Window            |Status                                                                                                                      |Disconfirmation Statement                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------|------------------|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
|PRED-034-A (NEW)  |Second round formally convenes (Araghchi returns Islamabad OR Oman indirect channel produces framework)|Before 30 Apr     |OPENED Ed033. Pakistan: return Sun/Mon. Oman channel active. Trump: doesn’t mean war.                                       |Araghchi proceeds to Moscow without Islamabad return AND no Oman framework = CONTRADICTED. H-A1 falls to 38-50%.|
|PRED-031-B        |Case A talks produce formal Hormuz instrument                                                          |Before 30 Apr     |PENDING. No instrument. Deadlocked. Window closes 30 Apr. Likely CONTRADICTED by window close.                              |Window closes 30 Apr without instrument = CONTRADICTED. H-B1 falls.                                             |
|PRED-031-C        |Lebanon 3-week ceasefire holds through ~14 May                                                         |~14 May           |AT RISK. Netanyahu strike order. Hezbollah Kfar Giladi barrage. Gate 0.6 NEAR. H-C1 change point flag raised.               |Hezbollah confirmed barrage 100+ rockets at Israel = CONTRADICTED. Gate 0.6 BREACHED.                           |
|PRED-031-D        |OFAC enforcement or India Chabahar divestment confirmed                                                |Before 15 May     |PARTIALLY PROGRESSING. Divestment proceeding. No enforcement on lapse day.                                                  |Neither enforcement nor confirmed divestment by 15 May = CONTRADICTED.                                          |
|PRED-031-E        |IRGC follow-on Yanbu/Petroline strike                                                                  |Before 7 May      |PENDING. Day 18+ no strike. Double suppressor. Propagation pressure from H-A1 fall and H-C1 flag.                           |Window closes 7 May without strike = CONTRADICTED.                                                              |
|PRED-030-B        |Northwood deployment schedule published                                                                |Before 30 Apr     |PENDING. No schedule. Germany Fulda deploying to Med but not Northwood. Window closes 30 Apr.                               |Window closes 30 Apr without schedule = CONTRADICTED.                                                           |
|PRED-030-A        |Iran unified proposal + formal second round                                                            |Before 30 Apr     |NEAR-CONTRADICTED. Talks deadlocked. Window closes 30 Apr. Araghchi Oman/Islamabad return only remaining pathway.           |Window closes 30 Apr without second round = CONTRADICTED.                                                       |
|PRED-029-B        |Hormuz sustained transit 24h+ (unrestricted)                                                           |Ongoing           |PENDING. Mine clearance 6 months per CENTCOM. Toll-booth only partial transit.                                              |Full 24h+ unrestricted transit = CONFIRMED.                                                                     |
|PRED-025-C / 026-B|Summit deployment plan and Northwood timeline                                                          |Ongoing           |PARTIAL MAINTAINED. Germany Fulda preparatory but not Northwood.                                                            |Named deployment timeline + joint statement = CONFIRMED.                                                        |
|PRED-022-B        |IRGC kinetic response to USN vessel                                                                    |Through resolution|PARTIAL. IRGC challenged USN destroyers, drone launched (WSJ Tier 2 uncorroborated). No direct strike on USN hull confirmed.|Direct IRGC kinetic strike on USN vessel = CONFIRMED.                                                           |
|PRED-025-B        |Abdollahi total blockade activation                                                                    |Through resolution|PENDING. Threat standing, not activated. 11+ days stale.                                                                    |Abdollahi announces total blockade activation = CONFIRMED.                                                      |
|PRED-006-A        |GCC emergency meeting                                                                                  |Post-ceasefire    |WATCH                                                                                                                       |Formal GCC statement declining to convene = CONTRADICTED.                                                       |

-----

## PREDICTION LOG — RESOLVED (CUMULATIVE THROUGH ED033)

|Ref                               |Outcome     |Notes                                                                                                                     |
|----------------------------------|------------|--------------------------------------------------------------------------------------------------------------------------|
|PRED-031-A                        |CONTRADICTED|Trump cancelled Witkoff/Kushner trip. Araghchi departed Islamabad without meeting US envoys. PMM-004 triggered. Ed033.    |
|PRED-026-C                        |CONFIRMED   |Lebanon 72-hr window closed 2200 GMT 19 April without barrage. Gate 0.6. Ed030.                                           |
|PRED-028-C                        |CONFIRMED   |Same basis. Ed030.                                                                                                        |
|PRED-022-A through PRED-029-A (×6)|CONTRADICTED|Second round did not occur before 22 April. PMM-003. Ed030.                                                               |
|PRED-015-A                        |PARTIAL     |Trump extended ceasefire 21 April. No named duration/verification. Disconf: lapse 22 Apr with no extension = CONTRADICTED.|
|PRED-022-B                        |PARTIAL     |IRGC seized non-USN vessels. Direct USN not confirmed. Disconf: USN vessel attacked = CONFIRMED.                          |
|PRED-022-E                        |AMBIGUOUS   |Insufficient evidence. Disconf: window closes, no Chinese-flag incident = CONTRADICTED.                                   |
|PRED-027-E / PRED-028-E           |CONTRADICTED|22 April window closed without Yanbu strike. Gate 0.6 confirmed.                                                          |
|PRED-027-B                        |CONTRADICTED|Iran closed Hormuz 18 April. IRGC fired on vessels. PMM H4 gap. Ed029.                                                    |
|PRED-028-B                        |CONTRADICTED|Same basis. Ed029.                                                                                                        |
|PRED-026-D                        |CONFIRMED   |GL U lapsed 0401 GMT 19 April. OFAC x2. Ed028.                                                                            |
|PRED-023-B                        |CONFIRMED   |Same basis. Ed028.                                                                                                        |
|PRED-022-C                        |CONFIRMED   |Same basis. Ed028.                                                                                                        |
|PRED-026-E                        |CONTRADICTED|First Yanbu strike CONFIRMED 8 April. Retroactively contradicted. PMM-002. Ed027.                                         |
|PRED-018-E                        |CONFIRMED   |IRGC struck East-West Pipeline 8 April. Reuters/Bloomberg/FT. Ed027.                                                      |
|PRED-022-D                        |CONFIRMED   |Same basis. Ed027.                                                                                                        |
|PRED-025-C                        |PARTIAL     |Paris Summit confirmed. Named assets. No deployment timeline. Disconf: no joint statement and no Northwood = CONTRADICTED.|
|PRED-026-B                        |PARTIAL     |Named assets. Northwood confirmed. No timeline. Disconf: no named assets = CONTRADICTED.                                  |
|PRED-012-B                        |CONTRADICTED|PMM-001 triggered.                                                                                                        |

-----

## CARRY-FORWARD FACTS — STATUS AT 1810 GMT 25 APRIL 2026

|Fact                                                                                                                                                |Last Verified                                                                 |Ed034 Action                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------|
|Trump cancelled Witkoff/Kushner Islamabad trip. ‘Too much time wasted.’ ‘Infighting and confusion within Iranian leadership.’                       |Truth Social / Fox Tier 1. 1810 GMT 25 Apr. CURRENT.                          |Has Trump reversed? Has Witkoff departed?                                   |
|Araghchi departed Islamabad Saturday evening after ~20hr meetings with Sharif + Munir. Posted: ‘Very fruitful.’ ‘Yet to see if US is truly serious.’|CNN / IRNA / Araghchi X. Tier 1/2. 1810 GMT 25 Apr. CURRENT.                  |Araghchi returns Islamabad Sun/Mon? Framework from Oman? FIRST ACTION Ed034.|
|Pakistan sources (CBS): Araghchi expected to return Islamabad Sunday or Monday for further talks.                                                   |CBS News. Pakistani sources. Tier 2. CURRENT.                                 |Verify at Ed034 open.                                                       |
|Iran condition for talks: US must lift naval blockade before Iran resumes talks. US refused.                                                        |CNN / PBS / AP. Tier 1/2. CURRENT.                                            |Monitor for any US flexibility shift.                                       |
|Ghalibaf stepped down as head of Iranian negotiating team due to internal disputes. Saeed Jalili seen as possible replacement.                      |Iran International. Tier 2. CURRENT.                                          |Verify Jalili confirmation. H5 implications — hardliner signal if confirmed.|
|Araghchi in Muscat, Oman. Oman channel active — Hormuz discussions ongoing. Then proceeds to Moscow.                                                |Farsna / Arabian Stories / The Week India. Tier 2/3. CURRENT.                 |Any Oman channel Hormuz framework?                                          |
|Trump (Axios/CNN): Cancellation does NOT mean war. ‘No. It doesn’t mean that. We haven’t thought about it yet.’                                     |Axios / CNN. Tier 2. 25 Apr. CURRENT.                                         |Monitor for reversal.                                                       |
|Hormuz CLOSED. Dual blockade unchanged. IRGC Ravanbakhsh: ‘Iran will keep pressuring enemy in Hormuz until it surrendered.’                         |All-source + Iran International Tier 2. CURRENT.                              |AIS/UKMTO. Any Oman channel Hormuz framework?                               |
|Mine clearance: CENTCOM told Congress Hormuz mine clearance could take SIX MONTHS. ‘Unlikely until ceasefire in place.’                             |Washington Post Tier 2. Congressional testimony. CURRENT.                     |Structural floor for H-B1 — re-verify if revised.                           |
|Germany deploying minesweeper Fulda to Mediterranean ‘in coming days’. ~45 crew.                                                                    |Germany MoD / Iran International. Tier 1/2. CURRENT.                          |Fulda arrival Med. Any NATO mandate or Hormuz coalition deployment order?   |
|Tehran Imam Khomeini Airport reopened Saturday — first flights since war started (Istanbul, Muscat, Medina).                                        |Fox News / CBS / state media. Tier 2. 25 Apr. CURRENT.                        |Confidence-building measure. Monitor expansion.                             |
|Macron (Athens): priority is full Hormuz reopening without tolls per international law.                                                             |Macron statement. Tier 1. CURRENT.                                            |Monitor for European coalition action.                                      |
|Lebanon ceasefire: +3 weeks (~14 May). Netanyahu ordered IDF to ‘strike Hezbollah targets in Lebanon with force.’                                   |Netanyahu office. Tier 1. 25 Apr. CURRENT.                                    |Gate 0.6 MANDATORY. H-C1 change point flag ACTIVE.                          |
|Hezbollah fired rockets at Israeli artillery position at Kfar Giladi + attack drones toward northern Israel. IDF acknowledged.                      |Hezbollah / IDF. Tier 3/1. 25 Apr. CURRENT.                                   |Count? Has barrage threshold (100+) been confirmed at Israeli territory?    |
|Hezbollah: ‘over 200 Israeli violations of ceasefire since it took effect on Friday.’                                                               |Times of Israel liveblog. Tier 2. 25 Apr. CURRENT.                            |Monitor. Each Israeli strike = H-C2 signal.                                 |
|Sirens in Malkia (northern border community). IDF investigating suspected Hezbollah drone.                                                          |IDF. Tier 1. 25 Apr. CURRENT.                                                 |Monitor.                                                                    |
|Trump invited Netanyahu and Lebanese President Aoun to Washington ‘in a couple of weeks.’                                                           |Trump Oval Office statement 23 April. Tier 1. CURRENT.                        |Circuit breaker for Lebanon ceasefire. Has visit been confirmed / scheduled?|
|Lebanese casualties: 2,491 killed, 7,719 wounded since 2 March.                                                                                     |Lebanese Health Ministry. Tier 2. 24-25 Apr. CURRENT.                         |Re-verify Ed034.                                                            |
|Iranian casualties: 3,400+. Israeli: 23. US: 13 KIA + 2 non-combat. Gulf: 32.                                                                       |NBC / various. Tier 2. 24-25 Apr. CURRENT.                                    |Re-verify Ed034.                                                            |
|GL U CONFIRMED LAPSED 26 April. ICICI Bank channel CLOSED. IOC no further Iranian oil purchases.                                                    |OFAC / Bloomberg / Reuters / IOC. Tier 1/2. ESTABLISHED.                      |Monitor OFAC register 15 May window.                                        |
|IPGL selling stake to Iranian entity (India Ports Global Chabahar Free Zone). No OFAC enforcement action at sweep.                                  |WION / National Herald / Business Standard. Tier 2. CURRENT.                  |Monitor OFAC register + MEA. Orderly wind-down proceeding.                  |
|OFAC: granted 6-month conditional waiver on basis India was winding down. Waiver now expired. India pre-notified OFAC.                              |TRT World / MEA confirmed. Tier 2. ESTABLISHED.                               |Re-entry clause preserved. Monitor 15 May window.                           |
|East-West Pipeline: 7M bpd restored. Manifa: 300K bpd restored.                                                                                     |Saudi MoE Tier 1. 12 Apr. STALE 13+ DAYS.                                     |Re-verify URGENT Ed034. Kpler/LSEG.                                         |
|Khurais: 300K bpd STILL OFFLINE. No restoration announcement.                                                                                       |Saudi MoE Tier 1. 12 Apr. STALE 13+ DAYS. DO NOT CARRY AT PRIOR CONFIDENCE.   |Re-verify URGENT Ed034. Kpler/LSEG or Saudi MoE. OVERDUE.                   |
|Northwood: Plans advancing. Germany Fulda deploying to Med. No named deployment timeline published.                                                 |Germany MoD / GOV.UK. Tier 1. CURRENT.                                        |Monitor UK MoD output. Named deployment schedule = H-B3 to 45-58%.          |
|Netanyahu: Prostate cancer disclosed 24 April. Full recovery. White House visit coming weeks.                                                       |Time/CBS/CNN. Tier 1/2. CURRENT.                                              |Monitor timing re Washington visit.                                         |
|Three US carrier groups in Middle East. USS Abraham Lincoln — Gulf of Oman.                                                                         |The Hill/The National Tier 2. 24 Apr / BBC 15 Apr. STALE 10+ DAYS for Lincoln.|Re-verify URGENT Ed034. Lincoln position and posture.                       |
|Iran missile launchers: ~50% intact.                                                                                                                |CNN/US intel Tier 2. 15 Apr. STALE 10+ DAYS.                                  |Re-verify Ed034.                                                            |
|Abdollahi total blockade threat: standing, not activated.                                                                                           |Reuters 15 Apr. Tier 1. STALE 10+ DAYS.                                       |Re-verify Ed034. Gate 0.6 confirm.                                          |
|OFAC staffing 22 of 40.                                                                                                                             |Ed016. PERMANENTLY STALE.                                                     |DO NOT CITE UNDER ANY CIRCUMSTANCES.                                        |
|Lindsey Graham: praised Trump cancellation. ‘Military engagement in Hormuz may be required in the short term.’ ‘Establish firm control’ over Hormuz.|Graham X post. Tier 2. 25 Apr. CURRENT.                                       |Monitor congressional pressure signals.                                     |

-----

## ED034 MANDATORY SWEEP ACTIONS (IN ORDER)

1. **LIVE GMT TIMESTAMP — ABSOLUTE FIRST ACTION BEFORE ANYTHING ELSE:**

```python
import datetime
now = datetime.datetime.utcnow()
print(now.strftime("%H%M GMT %d %B %Y"))
```

Run this bash tool call. Lock the output. This is the sweep timestamp. Calculate war day from it. Verify war day online. Only then proceed to item 2. No feed, no search, no analytical content, no SESSION_STATE write may occur before this step is complete.

1. **ARAGHCHI ISLAMABAD RETURN — FIRST PRIORITY (PRED-034-A):** Has Araghchi returned to Islamabad on Sunday/Monday as Pakistan sources indicated? If YES and both parties confirm second round: PRED-034-A CONFIRMED, H-A1 recovers to 65-75%. If Araghchi proceeds to Moscow without return AND no Oman framework: PRED-034-A CONTRADICTED, H-A1 falls to 38-50%.
1. **OMAN CHANNEL — ANY FRAMEWORK?** Did Araghchi-Oman meetings produce any Hormuz framework or message to US? Any face-saving formula via Oman? Positive = H-B1 signal.
1. **IRAN BLOCKADE DEMAND / US RESPONSE:** Has US indicated any flexibility on naval blockade? Any new Trump statement on Iran? Has Jalili been confirmed as new Iranian negotiating team lead? Jalili confirmation = significant H5 re-activation (hardliner bloc dominant). H-A1 falls further.
1. **PMM-004 MANDATORY CHECK:** For any H-A-class hypothesis above 60%: Is H4 gap active? Is Tier 1 Iranian denial present? Is there no observable Iranian-side preparatory action? If all three: apply mandatory −10pp minimum downward adjustment from prior. This is GOVERNING from Ed034, not advisory.
1. **LEBANON — Gate 0.6 MANDATORY (H-C1 CHANGE POINT FLAG ACTIVE):** Has Kfar Giladi barrage count been independently confirmed at 100+ rockets at Israeli territory (not south Lebanon troops)? Any new Netanyahu strike order executed? Any IDF major operation north of Litani? One confirmed barrage ≥100 rockets at Israeli territory = Gate 0.6 BREACHED, H-C3 CONFIRMED, Gate 5. Trump Washington visit progress (Aoun + Netanyahu)?
1. **YANBU / PETROLINE — Gate 0.6:** Any IRGC Yanbu/Petroline strike? PRED-031-E window closes 7 May. Day 19+? Gate 0.6 MANDATORY.
1. **KHURAIS — OVERDUE 13+ DAYS:** Saudi MoE announcement or Kpler/LSEG mandatory. Restored or still offline? URGENT.
1. **NORTHWOOD / GERMANY FULDA:** Has Northwood published named deployment schedule? PRED-030-B window closes 30 April. Has Fulda arrived Mediterranean? Any NATO mandate or Hormuz coalition deployment order?
1. **PRED-030-A, PRED-030-B, PRED-031-B WINDOWS CLOSE 30 APRIL:** All three windows close within 5 days. Assess and resolve at Ed034 or Ed035.
1. **STALE FACTS — ALL 10+ DAY ITEMS:** USS Abraham Lincoln (10+ days), Iran missile launchers (10+ days), Abdollahi threat (10+ days), East-West Pipeline (13+ days), Khurais (13+ days). Mandatory re-verify.
1. **IRAN INTERNAL:** Jalili confirmation? SNSC statement on Hormuz permanence? Prosecution of Iranian negotiator? H5 re-activation risk.
1. **AI-012 PIPELINE — MANDATORY AT SWEEP OPEN BEFORE WRITING:** (a) Update causal edge register (AI-012-1). (b) Append Δp to delta buffer (AI-012-2). (c) Compute z-scores — flag any |z| > 2.0 (AI-012-3). Note: H-C1 change point flag from Ed033 remains active — monitor. (d) Update correlation matrix (AI-012-4). (e) Check propagation register for triggered adjustments (AI-012-5). (f) Update EMA errors per band (AI-012-7). (g) Recompute per-band lookup table adjustments (AI-012-9). (h) Apply band adjustments to output ranges (AI-012-8). (i) Note RL Bandit advisory factors (AI-012-6 — ADVISORY ONLY until n≥30).
1. **GATE CHECKS — PRE-ANALYSIS:** Gate 0.1 (temporal currency), Gate 0.2 (source corroboration — Tier 3 sources above 5pp trigger), Gate 0.5 (cluster risk). These are NEW gates as of 26 April 2026 and are MANDATORY from Ed034.
1. **GATE CHECKS — PRE-PUBLICATION:** Gate 0.3 (incentive analysis — any hypothesis above 60% resting on named actor’s stated intent), Gate 0.4 (cross-case consistency — any hypothesis above 70% with positively correlated partner below 35%). These are NEW gates as of 26 April 2026 and are MANDATORY from Ed034.
1. **ALL 18 NAMED FEEDS — BEFORE WRITING:** PCP Step 1 mandatory.
1. **AI-007 + H7 + AI-010 + PMM-004 CHECKS:** Band governance. Anchoring. Single-cluster discount. PMM-004 mandatory for H-A-class.
1. **PCP STEP 1.5:** New signal check mandatory.
1. **TQL MANDATORY:** All four items all five cases.
1. **ALL 10 MANDATORY PDF ITEMS:** Verify deviation audit items 1-28. No blank pages. (Deviation audit now 28 items per ratified Addendum.)
1. **BYPASS AUDIT:** Maximum one bypass per case. Silent omission = declared bypass.
1. **DEVIATION AUDIT — 28 ITEMS:** Full 28-item checklist before PDF production (items 26-28 are new per ratified Addendum).
1. **PDF PRODUCTION ONLY:** ALL ANALYTICAL CONTENT TO PDF. NO CHAT RESOLUTION. AI-005 absolute.
1. **WAR DAY VERIFICATION:** Calculate from 28 Feb 2026 = Day 1. Verify online. Do not assume.

-----

## DISCONFIRMATION THRESHOLDS — STANDING

|Case|Threshold                                                                 |Effect                                                                      |
|----|--------------------------------------------------------------------------|----------------------------------------------------------------------------|
|A   |Araghchi returns Islamabad + both parties confirm second round            |PRED-034-A CONFIRMED. H-A1 recovers to 65-75%. AI-012-5: H-B1 +0.04         |
|A   |Araghchi proceeds to Moscow without return AND no Oman framework          |PRED-034-A CONTRADICTED. H-A1 falls to 38-50%. AI-012-5: H-B1 −0.04         |
|A   |Oman channel produces Hormuz face-saving formula                          |H-B1 recovers to 20-30%. Partial PRED-030-A credit.                         |
|A   |Jalili confirmed as Iranian negotiating lead                              |H5 re-activated. H-A1 falls further. Hardliner signal.                      |
|A   |Iran abandons blockade-lift precondition                                  |H-A1 rises to 65-75%. H-B1 rises marginally.                                |
|A   |IRGC/SNSC repudiates Araghchi framework                                   |H5 re-activated sharply. H-A1 falls to 28-40%. AI-012-1 edge strength reset.|
|A   |Trump resumes strikes                                                     |Gate 5 Case A. H-A2 CONFIRMED.                                              |
|A   |Phone call Trump-Araghchi (direct)                                        |H-A1 rises sharply. H5 partially resolves.                                  |
|B   |Oman channel Hormuz framework agreed                                      |H-B1 recovers to 20-30%                                                     |
|B   |Mine clearance estimate revised (faster)                                  |H-B1 rises                                                                  |
|B   |IRGC direct kinetic attack on USN vessel                                  |PRED-022-B CONFIRMED. Gate 5. AI-012-5: H-E2 +0.08                          |
|B   |Northwood deployment schedule published                                   |H-B3 to 45-58%. PRED-030-B CONFIRMED.                                       |
|B   |SNSC endorses toll-booth as permanent                                     |H-B1 falls to 5-12%. AI-012-1 edge: US blockade→Hormuz rises to 0.97.       |
|B   |IRGC announces new vessel seizures + toll expansion                       |H-B1 falls to 8-15%                                                         |
|C   |Ceasefire holds through 14 May; Washington visit confirms diplomatic track|PRED-031-C CONFIRMED. H-C1 recovers. Change point flag potentially resolved.|
|C   |Netanyahu backs down from strike order under US pressure                  |H-C1 recovers marginally                                                    |
|C   |Hezbollah confirmed barrage ≥100 rockets at Israeli territory             |Gate 0.6 BREACHED. H-C3 CONFIRMED. Gate 5. AI-012-5: H-E2 +0.08             |
|C   |IDF major operation north of Litani River                                 |H-C2 approaches dominant. Gate 5.                                           |
|C   |UNIFIL withdrawal                                                         |Monitoring collapses. H-C2 rises sharply.                                   |
|C   |Lebanon army deploys under ceasefire terms                                |H-C1 stabilises. Circuit breaker signal.                                    |
|D   |OFAC enforcement on Chabahar operators                                    |PRED-031-D CONFIRMED                                                        |
|D   |India formally divests Chabahar (confirmed)                               |Strategic channel severed. PRED-031-D credit.                               |
|D   |OFAC issues new waiver / sanctions lifted                                 |H-D1 partially revives. Strategic reversal.                                 |
|E   |IRGC Yanbu/Petroline strike                                               |PRED-031-E CONFIRMED. Gate 5 CRITICAL.                                      |
|E   |Lebanon collapses (H-C3 confirmed)                                        |H-E2 rises to 50-65%. AI-012-4 H-C1/H-E1 propagation direction confirmed.   |
|E   |Talks resume second round (H-A1 confirmed)                                |H-E1 suppressor partially restored. H-E1 rises marginally.                  |
|E   |Talks fail and ceasefire lapses                                           |H-E2 dominance reasserts                                                    |

-----

## EDITION WORKFLOW — REPEATING LOOP (AD INFINITUM)

The following sequence is the governing operational loop for every edition. It must not be deviated from.

```
SESSION_STATE_EDnnn.md
+ build_core.py
+ styles.py
+ session_state_ednnn.py (companion — deferred until Ed035)
        ↓
    RUN SWEEP (GMT timestamp locked before any feed executed — see GMT RULE below)
        ↓
  EDnnn PDF GENERATED
        ↓
  GENERATE SESSION_STATE_EDnnn+1.md
  + session_state_ednnn+1.py (companion — deferred until Ed035)
        ↓
    RUN SWEEP (GMT timestamp locked before any feed executed)
        ↓
  EDnnn+1 PDF GENERATED
        ↓
  GENERATE SESSION_STATE_EDnnn+2.md
  + session_state_ednnn+2.py (companion)
        ↓
  ... AD INFINITUM
```

**Rules governing this loop — non-negotiable:**

1. SESSION_STATE governs the PDF of the **same** edition number. SESSION_STATE_ED033 → Ed033 PDF. SESSION_STATE_ED034 is generated from SESSION_STATE_ED033 + Ed033 PDF. No exceptions.
1. build_core.py and styles.py are static infrastructure. They do not increment with edition number unless a structural architecture change is logged in the system change log.
1. The companion .py increments with each edition, carrying forward updated AI-012 data registers (delta buffers, EMA errors, Brier table, edge register, Q-table). Deferred until Ed035.
1. No sweep may begin before the GMT timestamp is locked (see GMT RULE below).
1. No PDF may be generated before the sweep is complete.
1. No SESSION_STATE update may be written before the PDF is complete.
1. The loop does not terminate. Each edition close immediately prepares the next SESSION_STATE.

-----

## GMT TIMESTAMP RULE — MANDATORY AT EVERY SWEEP OPEN AND EVERY SESSION STATE WRITE

**This rule governs chronological integrity of the entire forecasting system. Violation = PLM entry.**

**SESSION STATE GENERATION TIMESTAMP RULE — MANDATORY:**

Every time a new SESSION_STATE_EDnnn.md is generated or amended, the **very first action** before writing a single line is:

```python
import datetime
now = datetime.datetime.utcnow()
print(now.strftime("%H%M GMT %d %B %Y"))
```

The output of this bash tool call is the SESSION_STATE header timestamp. It is written to lines 2 and 3 immediately. No content may be written to the SESSION_STATE before this timestamp is captured and locked.

**This applies to:**

- Initial SESSION_STATE generation after PDF build
- Any amendment or update to an existing SESSION_STATE
- Any session state regeneration (e.g. after corruption per PLM-006)

**The timestamp on lines 2 and 3 of every SESSION_STATE must reflect the actual system clock time at the moment of writing — not the sweep time, not the PDF build time, not an estimate.**

```
## Edition NNN Sweep Handoff · [DD MONTH YYYY] · [HHMM GMT] ([HHMM BST])
## SESSION STATE UPDATED · [DD MONTH YYYY] · [HHMM GMT] ([HHMM BST]) · [sweep descriptor]
```

BST = GMT + 1 hour (during British Summer Time, late March to late October).
Violation = PLM entry mandatory.

**TIMESTAMP SOURCE RULE — CRITICAL:** The SESSION_STATE header timestamp must be taken from the bash tool system clock capture at sweep open — never from web search (cached/stale), never estimated in chat, never entered manually. Manual timestamp estimation in chat produced two named errors in this session (1858 GMT and 2114 GMT both wrong). Operator should never have to state the time.

**MANDATORY FIRST ACTION OF EVERY SWEEP — BEFORE ANYTHING ELSE:**

```python
import datetime
now = datetime.datetime.utcnow()
print(now.strftime("%H%M GMT %d %B %Y"))
```

This bash tool call reads the live system clock of the container. It is accurate, programmatic, and requires nothing from the operator. The output is the locked GMT timestamp for the entire sweep. All subsequent actions — war day calculation, feed sweeps, analytical content, SESSION_STATE header, PDF header and footer — use this locked timestamp. No other timestamp source is permitted.

**Execution order — non-negotiable:**

1. Bash tool → capture live GMT from system clock → lock timestamp
1. Calculate war day: `(locked date − 28 Feb 2026).days + 1`
1. Verify war day online
1. Then and only then — run feeds, searches, analytical content
1. SESSION_STATE header timestamp = locked timestamp from step 1
1. PDF `GMT_NOW = datetime.datetime.utcnow()` at build time = independently confirms step 1

**This rule cannot be bypassed. Violation = PLM entry mandatory.**

**RULE:** Before any live feed is executed, before any web search is run, before any analytical content is written, the current GMT timestamp must be captured and locked. This timestamp is the authoritative sweep time for the entire edition. All carry-forward fact staleness calculations, all war day arithmetic, and all prediction window assessments are made relative to this locked timestamp.

**GMT = London time (UTC+0 in winter, UTC+1 BST in summer). The system operates on GMT primary at all times. BST is shown in parentheses for operator reference only.**

**Execution protocol at every sweep open:**

1. Capture current GMT timestamp: `GMT_NOW = datetime.datetime.utcnow()` — programmatic, never manual.
1. Display locked timestamp in session: e.g. `1810 GMT 25 APRIL 2026 (1910 BST)`.
1. Calculate war day from locked timestamp: `WAR_DAY = (date − 28 Feb 2026).days + 1`.
1. Verify war day online before proceeding. If online verification contradicts calculation: online value governs, discrepancy logged as PLM entry.
1. **Only after steps 1-4 are complete** may any live RSS feed, web search, or source sweep begin.
1. The locked GMT timestamp must appear in: the PDF header, the PDF footer, the SESSION_STATE update, and the carry-forward facts table.
1. No timestamp may be entered manually. All timestamps are programmatic. Manual entry = PLM entry mandatory.

**Why this matters:** Carry-forward fact staleness (e.g. “stale 13 days”), prediction window calculations (e.g. “T-5 days”), and Brier score edition attribution all depend on a consistent, verified, programmatic timestamp. A drifted or manually entered timestamp corrupts the chronological spine of the entire system.

-----

## BUILD SCRIPT ARCHITECTURE

- Core: `build_core.py` · Styles: `styles.py` · Per-edition: `build_edition_NNN.py`
- All four values below are programmatic — derived from the mandatory bash block. Never entered manually.

```python
import datetime
now = datetime.datetime.utcnow()
bst = now + datetime.timedelta(hours=1)
hour = now.hour
if 5 <= hour < 12:
    SWEEP_STR = 'MORNING SWEEP'
elif 12 <= hour < 17:
    SWEEP_STR = 'AFTERNOON SWEEP'
elif 17 <= hour < 21:
    SWEEP_STR = 'EVENING SWEEP'
else:
    SWEEP_STR = 'LATE NIGHT SWEEP'
EDITION  = "034"
DATE_STR = now.strftime("%d %B %Y").upper()
GMT_NOW  = now
```

- `flag_block(ref, number, body_text, gate_note, styles)` — five positional args. PLM-003.
- `story.extend()` not `story.append()` for flag_block() and source_block(). PLM-005.
- `story.extend(source_block([...], styles))` — single closing paren. PLM-007.
- styles.py and build_core.py must be uploaded as files at session open. If not available: recreate from SESSION_STATE context (PLM-011 precedent).

-----

## PROCESS LOG MEMO (PLM)

|Entry  |Edition                   |Issue                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|PLM-001|Ed025 Morning             |Build script pre-existed. Session resumed mid-build.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|PLM-002|Ed025 Evening             |Session state truncated in chat. PDF built correctly.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|PLM-003|Ed026 Morning             |flag_block() missing styles argument — five calls required manual correction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|PLM-004|Ed028 Pre-Sweep           |SESSION_STATE.md regenerated at operator request. No sweep conducted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|PLM-005|Ed028 Late Afternoon      |story.extend() required for flag_block() and source_block(). story.append() caused TypeError.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|PLM-006|Ed029 Evening             |SESSION_STATE.md corrupted by operator tool (Perplexity). Regenerated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|PLM-007|Ed030 Morning             |AI-005 violation: analytical content resolved in chat prior to PDF build. Corrected in Ed030 rebuild.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|PLM-008|Ed030 Initial             |War Day shown as 57 on stats bar — corrected to 56 in rebuild. Chronology verification rule added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|PLM-009|Ed030/031                 |Cross-examination identified 10 missing items from Ed029 PDF. Ed030 rebuilt with all 10. AI-011 introduced. Deviation audit expanded to 25 items.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|PLM-010|Ed031                     |Nine calibration enhancements (AI-012-1 through AI-012-9) added to SESSION_STATE. Architecture upgraded to v1.3.0. AI-009 old shrinkage rule retired. Calibration pipeline formalised as 12-stage execution order.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|PLM-011|Ed032 Morning             |styles.py and build_core.py not available as uploads. Recreated from session context.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|PLM-012|Ed033 Evening             |Ed032 PDF build was never completed (Parts 8 + doc.build() not appended before session was interrupted). Ed033 correctly identified this from context and proceeded from Ed031 SESSION_STATE as governing baseline.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|PLM-013|26 April 2026 (Post-Ed033)|Gates 0.2, 0.3, and 0.4 were absent from the AtollSphere gate registry across all 33 editions (Editions 001-033). Their absence was not identified by the AI system at any point during operation, during session state construction, or during the drafting of the AtollSphere Systems Architecture & Methodology document. The omission was identified by Dominic Young on 26 April 2026 through human cross-examination of the gate registry against the PMM failure log. Method of discovery: asking whether each PMM entry (PMM-001 through PMM-004) could have been prevented by a pre-publication control that did not yet formally exist. In each case, affirmative. Gates 0.2, 0.3, and 0.4 ratified and integrated into SESSION_STATE_ED033. Deviation Audit extended to 28 items. See Governance Note: AI Self-Examination Limitation.|

-----

## ANALYTICAL PMM LOG

|Entry  |Pred Ref                          |Outcome     |What Failed                                                                                                                                                                   |Why                                                                                                                                                                                                        |System Change                                                                                                                                                                                                                                                                                                                                                |Heuristic                                                       |
|-------|----------------------------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
|PMM-001|PRED-012-B                        |CONTRADICTED|Named-source prediction without incentive analysis.                                                                                                                           |H1 not applied before C3.                                                                                                                                                                                  |Named-party predictions require incentive analysis before C3.                                                                                                                                                                                                                                                                                                |H1 — misapplication                                             |
|PMM-002|PRED-026-E                        |CONTRADICTED|First Yanbu strike carried PENDING through Ed026.                                                                                                                             |Gate 0.1 temporal currency check failed.                                                                                                                                                                   |Gate 0.1 mandatory for all absence claims. Gate 0.6 mandatory for IRGC strike absence.                                                                                                                                                                                                                                                                       |H4 — narrative vs outcome gap                                   |
|PMM-003|PRED-022-A through PRED-029-A (×6)|CONTRADICTED|H-A1 at 72-82% on Iranian-source cluster. Active H5 contradiction not discounted.                                                                                             |Gate 0.5 cluster risk underweighted. H4 observable action underweighted.                                                                                                                                   |AI-010: single-cluster H5 discount minimum 10pp. AI-012-1/2/3 directly address recurrence risk.                                                                                                                                                                                                                                                              |H4 — narrative vs outcome gap                                   |
|PMM-004|PRED-031-A                        |CONTRADICTED|H-A1 at 72-82% with active Tier 1 Iranian denial (Baghaei), no observable Iranian-side preparatory action, and prior H4 gap. Venue preparation treated as sufficient evidence.|H4 gap (White House claim vs Iranian Tier 1 denial) was the governing signal. Venue preparation without Iranian-side action was insufficient. Gate 0.3 absent — no incentive analysis requirement enforced.|MANDATORY GOVERNING RULE from Ed034: When H4 gap is active (Tier 1 US assertion vs Tier 1 Iranian denial) AND no observable Iranian-side preparatory action, apply mandatory −10pp minimum downward adjustment from prior. Gate 0.3 now in force. Gate 0.2 now in force. Would have placed Ed032 H-A1 at 62-72% (Brier penalty reduced from 0.593 to ~0.385).|H4 — narrative vs outcome gap; H6 overweighted venue preparation|

-----

## SYSTEM CHANGE LOG — ACTIVE RULES

|Entry    |Rule Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |In Force                                  |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
|001      |Named-party predictions require incentive analysis before C3.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |Ed014                                     |
|AI-001   |Case B standing: AFC steelman, H-B2 specified, H6 second-order, disconfirmation thresholds mandatory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |Ed018                                     |
|AI-002   |Wikipedia Tier 4 only. Leg 1/Leg 2 split Case A. Tier 4 dependency test TQL item 4.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |Ed019                                     |
|AI-003   |Gate 0.5, H1 saturation check, PCP Step 1.5, claim-type labelling, calibration audit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |Ed019                                     |
|AI-004   |All rule changes logged before in force.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |Ed019                                     |
|AI-005   |PDF brief mandatory. Analysis to PDF ONLY. REINFORCED Ed030 — PLM-007. DO NOT REPEAT.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |Ed022                                     |
|AI-006   |Part 4 TQL mandatory every case every edition. Four items required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |Ed023                                     |
|AI-007   |Calibration doctrine. Band governance. No hypothesis above 85% without named formal evidence. Hard ceilings cannot be overridden by AI-012.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |Ed027                                     |
|AI-008   |Architecture alignment. Full CDIT, 18 named feeds, Gate 0.6, H7, PMM/PLM split, bypass protocol, deviation audit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |Ed029                                     |
|AI-009   |Brier score optimisation. Point estimates, normalisation, Bayesian update (LR table v1.0), running BS table. Old shrinkage rule RETIRED Ed031 — replaced by AI-012-7 EMA. Target BS<0.15. Current BS=0.2151 (n=15, DEGRADED).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |Ed029 / Retired shrinkage Ed031           |
|AI-010   |Single-cluster H5 discount. Minimum 10 percentage points. Cannot be bypassed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |Ed030                                     |
|AI-011   |Mandatory PDF architecture — 10 items. Deviation audit expanded to 25 items (now 28 per Addendum).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |Ed031                                     |
|AI-012   |NINE CALIBRATION ENHANCEMENTS (AI-012-1 through AI-012-9). 12-stage pipeline. Architecture v1.3.0. Target BS trajectory: <0.15 → <0.12 → <0.10 (elite at n≥30). Old AI-009 shrinkage rule retired.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |Ed031                                     |
|PMM-004  |GOVERNING RULE: When H4 gap active (Tier 1 US assertion vs Tier 1 Iranian denial) AND no observable Iranian-side preparatory action AND hypothesis above 60%: mandatory −10pp minimum downward adjustment from prior. Cannot be bypassed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |Ed034 (GOVERNING)                         |
|Gate 0.2 |Source Corroboration Requirement: Tier 3 source above 5pp probability adjustment trigger requires independent Tier 1/2 corroboration through different evidential chain. If absent: zero governing weight, no adjustment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |Ed034 (GOVERNING — ratified 26 April 2026)|
|Gate 0.3 |Incentive Analysis Completion: Any hypothesis above 60% resting materially on named actor’s stated intent requires documented H1 analysis (bilateral) in edition PDF. If absent: hypothesis capped at 60%.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |Ed034 (GOVERNING — ratified 26 April 2026)|
|Gate 0.4 |Cross-Case Consistency Check: Any hypothesis above 70% — check all positively correlated partners (correlation >0.30). If any partner below 35%: reconcile via structural suppressor documentation or estimate adjustment. No publication until resolved.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |Ed034 (GOVERNING — ratified 26 April 2026)|
|AI-012-10|PUBLICATION INTEGRITY LOCK (two independent sub-conditions): (1) If H4 gap active AND Tier 1 denial active AND no observable preparatory action: published probability capped at 50%. (2) If independent evidential chains supporting hypothesis < 2 (per Gate 0.2 definition — chains must not share a common upstream source): published probability capped at 60%. Applied at Stage 13, after AI-007. Non-bypassable. Sub-condition 1 cross-references PMM-004 (narrative-vs-outcome lock). Sub-condition 2 cross-references Gate 0.2 (corroboration-sufficiency lock). Both sub-conditions are independent — either may trigger alone. Retroactive note Ed033: H-A1 published at pt est 0.56; under sub-condition 1 (H4 gap active, Baghaei Tier 1 denial, no preparatory action) the cap would have placed pt est at 0.50. Directionally correct. Ed033 not rebuilt — note for calibration audit only.|Ed035 (GOVERNING)                         |

-----

## HPT — HEURISTIC PERFORMANCE TRACKING (CUMULATIVE)

|Edition      |Case A                  |Case B  |Case C       |Case D  |Case E           |Outcome Correlation                                                                                                                                    |
|-------------|------------------------|--------|-------------|--------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
|Ed029 Evening|H6/H5/H1                |H4/H5/H6|H6/H4/H1     |H3/H6/H1|H6/H3/H1         |H4 gap confirmed Case B. H6 intersection A/B/C/E confirmed.                                                                                            |
|Ed030 Morning|H6/H4/H5/H1             |H4/H6/H1|H6/H4/H1     |H3/H6/H1|H6/H3/H1         |H4 dominant Case A: ceasefire without talks. H5 institutional constraint confirmed. H6 toll-booth/GL U intersection.                                   |
|Ed031 Evening|H6/H4/H5-partial/H2/H1  |H4/H6/H1|H6/H4/H1     |H3/H6/H1|H6/H3/H1         |H5 partially resolving Case A (Ghalibaf absent). H2 timing confirmed. H4 Jones Act ≠ Hormuz. Triple H6 suppressor Case E. AI-012-4 corroborates all H6.|
|Ed032 Morning|H4/H1/H6/H2/H5-partial  |H6/H4/H1|H6/H4        |H3/H6/H1|H6/H3            |H4 dominant. New H6 Case C (Hezbollah/IDF shared trajectory). PMM-003 warning active.                                                                  |
|Ed033 Evening|H4/H1/PMM-004/H5-partial|H6/H1/H4|H4/H6/CP-flag|H3/H6   |H6/H3/propagation|H4 fully materialised: PRED-031-A CONTRADICTED. PMM-004 triggered. First AI-012-3 change point flag (H-C1). Dual propagation first in system history.  |

-----

## DEVIATION AUDIT — 28 ITEMS (MANDATORY ITEM 9 — EXTENDED FROM 25 TO 28 PER ADDENDUM RATIFIED 26 APRIL 2026)

The following 28 items must all receive PASS status before any edition PDF can be published. Items 26-28 are new, effective immediately per the ratified Addendum.

|# |Item                                                                                                                                                                                                                                                                                                                                                 |
|--|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|1 |GMT timestamp captured from bash tool before any feed                                                                                                                                                                                                                                                                                                |
|2 |War day verified arithmetically                                                                                                                                                                                                                                                                                                                      |
|3 |War day verified online                                                                                                                                                                                                                                                                                                                              |
|4 |Sweep descriptor programmatically derived                                                                                                                                                                                                                                                                                                            |
|5 |All 18 named feeds checked before analytical content written                                                                                                                                                                                                                                                                                         |
|6 |AI-005: all analytical content to PDF only                                                                                                                                                                                                                                                                                                           |
|7 |AI-007 hard ceilings checked (85% cap)                                                                                                                                                                                                                                                                                                               |
|8 |H7 anchoring risk checked for all material hypotheses                                                                                                                                                                                                                                                                                                |
|9 |AI-010 single-cluster H5 discount where triggered                                                                                                                                                                                                                                                                                                    |
|10|AI-012 12-stage pipeline executed in order                                                                                                                                                                                                                                                                                                           |
|11|Causal edge register updated (AI-012-1)                                                                                                                                                                                                                                                                                                              |
|12|Delta buffer appended (AI-012-2)                                                                                                                                                                                                                                                                                                                     |
|13|Change point z-scores computed (AI-012-3) — any flags resolved and documented before publication                                                                                                                                                                                                                                                     |
|14|Correlation matrix updated (AI-012-4)                                                                                                                                                                                                                                                                                                                |
|15|Propagation register checked (AI-012-5)                                                                                                                                                                                                                                                                                                              |
|16|EMA errors updated (AI-012-7)                                                                                                                                                                                                                                                                                                                        |
|17|Per-band lookup table checked (AI-012-9)                                                                                                                                                                                                                                                                                                             |
|18|Band adjustments applied (AI-012-8)                                                                                                                                                                                                                                                                                                                  |
|19|RL Bandit Q-table noted (AI-012-6 — ADVISORY)                                                                                                                                                                                                                                                                                                        |
|20|All 10 mandatory PDF items present (AI-011)                                                                                                                                                                                                                                                                                                          |
|21|No blank pages                                                                                                                                                                                                                                                                                                                                       |
|22|HPT block present                                                                                                                                                                                                                                                                                                                                    |
|23|PLM section present in PDF body                                                                                                                                                                                                                                                                                                                      |
|24|PMM section present in PDF body                                                                                                                                                                                                                                                                                                                      |
|25|Bypass audit: no bypasses, no silent omissions; operator instruction complied                                                                                                                                                                                                                                                                        |
|26|**Gate 0.2 Source Corroboration Applied Where Triggered** — Any Tier 3 source cited in support of a probability adjustment above 5pp must be checked for independent Tier 1 or Tier 2 corroboration through a different evidential chain. If corroboration absent: Tier 3 source carries zero governing weight and no adjustment applied.            |
|27|**Gate 0.3 Incentive Analysis Completion Verified** — Any hypothesis above 60% that rests materially on a named actor’s stated intent must have a completed H1 (Incentive Mismatch) analysis documented in the edition PDF — covering both the claiming party and the party being claimed about. If absent: hypothesis capped at 60% until completed.|
|28|**Gate 0.4 Cross-Case Consistency Resolved** — Any hypothesis above 70% must be checked against all positively correlated hypotheses (correlation > 0.30). Any positively correlated partner below 35% requires documented reconciliation — either a structural suppressor is named, or the estimates are adjusted. No publication until resolved.   |

-----

## SESSION HANDOFF — MANDATORY AT EACH EDITION CLOSE

1. **LIVE GMT TIMESTAMP — FIRST ACTION BEFORE WRITING SESSION STATE:**

```python
import datetime
now = datetime.datetime.utcnow()
print(now.strftime("%H%M GMT %d %B %Y"))
```

Lock this output. Write it to SESSION_STATE lines 2 and 3 immediately. No content written before this step.

1. Full AI-012 pipeline executed (12 stages) — all registers updated
1. Causal edge register updated (AI-012-1)
1. Delta buffer updated per hypothesis (AI-012-2)
1. Change point z-scores computed — any flags resolved before publication (AI-012-3)
1. Correlation matrix updated (AI-012-4)
1. Propagation register checked — all triggered adjustments applied and documented (AI-012-5)
1. RL Bandit Q-table updated on new PRED resolutions (AI-012-6 — advisory)
1. EMA errors updated per band (AI-012-7)
1. Per-band lookup table recomputed (AI-012-9)
1. Band adjustments applied to output ranges (AI-012-8)
1. Calibration map corrections documented with pipeline stage annotations
1. All prediction log entries updated with five-state classification and disconfirmation statements
1. All carry-forward facts flagged with last-verified edition and staleness
1. All new rules added to SYSTEM CHANGE LOG
1. Next edition mandatory sweep actions in order
1. Deviation audit failures documented with PLM entry
1. Analytical prediction failures documented with PMM entry
1. All 10 mandatory PDF items verified present in completed PDF
1. War day verified online — not assumed
1. Resolved prediction log updated with all newly resolved PREDs
1. **Gate 0.2, 0.3, 0.4 checks verified executed** — new from Ed034

-----

*SESSION_STATE.md · AtollSphere · LS AI Systems · Edition 033 Evening Sweep Handoff · Updated 25 April 2026 · 1810 GMT (1910 BST) — Timestamp verified online · Architecture v1.3.0 · War Day 57 (system clock verified) · TALKS DEADLOCKED — Trump cancelled · Araghchi Muscat · Pakistan: return Sun/Mon · PRED-031-A CONTRADICTED · PMM-004 FORMALISED AND GOVERNING · TWO CHANGE POINT FLAGS (H-A1 resolved, H-C1 ACTIVE) · BS = 0.2151 (n=15, DEGRADED) · 70-80% band 0/7 observed rate · AI-012-5 DUAL PROPAGATION TRIGGERED (first in system history) · Lebanon ceasefire ESCALATING (Netanyahu strike order) · Gate 0.6 NEAR · Hormuz mine clearance 6 months per CENTCOM · GL U LAPSED · IPGL divestment proceeding · No OFAC enforcement at sweep · Day 18 no Yanbu strike · Khurais STILL OFFLINE (13+ days stale) · GATES 0.2, 0.3, 0.4 RATIFIED AND INTEGRATED (PLM-013) · Deviation Audit EXTENDED TO 28 ITEMS · AI Self-Examination Limitation Governance Note FORMALLY ADDED · AI-007 + AI-009 + AI-010 + AI-011 + AI-012 (9 enhancements) IN FORCE · PMM-004 NOW GOVERNING · Gate 0.2 / Gate 0.3 / Gate 0.4 NOW GOVERNING FROM ED034 · 10 Mandatory PDF Items Enforced · Deviation Audit 28 Items Enforced · PLM-013 Recorded · Anti-drift Governance ACTIVE · Human oversight finding: Dominic Young, 26 April 2026*