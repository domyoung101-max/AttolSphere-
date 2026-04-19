# ATOLLSPHERE SESSION STATE

## Edition 030 Evening Sweep Handoff · 18 April 2026 · 2227 GMT (2327 BST)

## SESSION STATE UPDATED · 18 April 2026 · 2227 GMT · Post-Ed030 Evening Sweep

-----

## CURRENT EDITION

- Last completed: Edition 030 · Evening Sweep · 18 April 2026 · 2227 GMT (2327 BST)
- Prior edition: Edition 029 · Evening Sweep · 18 April 2026 · 1800 GMT (CORRECTED — PMM Entry 012)
- Next: Edition 031 · GL U lapse trigger 0401 GMT 19 April — T-1.5 HOURS. Lebanon 72-hr window 2200 GMT 19 April — T-21.5 HOURS.
- War Day: 51 (18 April 2026)
- Ceasefire expiry: ~0000 GMT 22 April — T-3.5 DAYS
- Hormuz: RE-CLOSED 18 April — Gate 5 Case B active and deepened

-----

## PMM Entry 012

Ed029 published with incorrect timestamp "19 April 2026 · 1954 GMT · War Day 52." Correct timestamp: 18 April 2026 · 1800 GMT (1900 BST) · War Day 51. All intelligence correct and stands unchanged. Only date/time/war day header was in error. Erratum included in Ed030 PDF. Chronology locked: Ed028 Late Afternoon = 1611 GMT 18 Apr; Ed029 = 1800 GMT 18 Apr; Ed030 = 2227 GMT 18 Apr; Ed031 = 19 Apr post-0401 GMT.

-----

## CALIBRATION MAP — Ed030 Evening

|Hypothesis|Ed029              |Ed030                    |Basis                                                       |
|----------|-------------------|-------------------------|------------------------------------------------------------|
|H-A1      |72–82%             |**72–82% CARRY**         |No formal announcement. Iranian sources: Monday.            |
|H-A2      |7–12%              |**8–14% UP**             |Trump "may not extend." Hormuz friction.                    |
|H-A3      |45–60%             |**38–52% DOWN**          |Trump "may not extend" direct counter-signal. PROVISIONAL.  |
|H-B1      |22–38% GATE 5      |**18–32% DOWN**          |Azizi SNSC endorsement. Three kinetic incidents.            |
|H-B2      |18–28%             |**22–35% UP**            |Mein Schiff 4. Container ship hit. IRGC active kinetic mode.|
|H-B3      |26–34% PARTIAL     |**26–34% PARTIAL CARRY** |Paris confirmed. Northwood this week. No timeline.          |
|H-C1      |60–72%             |**60–72% CARRY**         |No barrage. Hour 27. T-21.5 hours.                          |
|H-C2      |13–20%             |**13–20% CARRY**         |IDF violations ongoing.                                     |
|H-C3      |8–16%              |**8–16% CARRY**          |No barrage. Trump prohibition active.                       |
|H-D2      |NEAR-CONFIRMED T-5H|**NEAR-CONFIRMED T-1.5H**|No instrument at 2227 GMT. Resolves 0401 GMT.               |
|H-D3      |5–10%              |**3–7% DOWN**            |T-1.5 hours. Falling.                                       |
|H-E1      |38–52%             |**35–48% DOWN**          |IRGC kinetic incidents weaken restraint signal.             |
|H-E2      |38–52%             |**40–55% UP DOMINANT**   |IRGC active kinetic mode. GL U T-1.5H. H-E2 dominant.       |
|H-E3      |10–15%             |**10–15% CARRY**         |Abdollahi stale.                                            |

-----

# BAYESIAN LAYER INSTRUCTIONS

**MANDATORY:** After updating hypothesis probabilities each sweep, perform these calculations step-by-step. All results go into the tables below.

## Step 1: Update Causal Edges (Exponential Smoothing)

For each causal edge identified in this sweep's Tier 1-2 sources:
- New weight = (0.7 × old weight) + (0.3 × signal strength)
- Signal strength is between -1 and 1 (negative = inverse relationship)
- If no new evidence for an edge, keep existing weight
- Update the Causal Edges table below

## Step 2: Calculate Delta Statistics

For each hypothesis that changed this sweep:
- Δp = new_prob - old_prob (use midpoint of percentage range)
- Add Δp to the last_5 array (drop the oldest value)
- New mean = sum of last_5 ÷ 5
- New std = square root of [(sum of (each Δp - mean)²) ÷ 4]
- Update the Delta Statistics table below

## Step 3: Detect Change Points (2-Sigma)

For each hypothesis with a new Δp:
- If std > 0:
    z_score = (Δp - mean) ÷ std
- Else: z_score = 0
- If |z_score| > 2.0:
    Add to Change Points Log with sweep number and z_score
- Do not duplicate entries for the same sweep/hypothesis

## Step 4: Update Correlation Matrix (Shrinkage)

Maintain probability history for each case's primary hypothesis:
- Case A: H-A1 (use midpoint: 0.77)
- Case B: H-B2 (use midpoint: 0.285)
- Case C: H-C1 (use midpoint: 0.66)
- Case D: H-D2 (use midpoint: 0.95)
- Case E: H-E2 (use midpoint: 0.475)

For each pair of cases (e.g., A&B, A&C, B&E, etc.):
- If at least 3 sweeps of history exist:
    observed_correlation = Pearson correlation of the two probability streams
- Else: observed_correlation = 0.5

Apply shrinkage:
- confidence = min(1.0, n_sweeps ÷ 20)
- final_correlation = (confidence × observed) + ((1-confidence) × 0.5)
- Diagonal values (case with itself) = 1.00

Update the Correlation Matrix table below.

## Step 5: Cross-Case Propagation

If Case B (H-B2) probability changed this sweep:
- delta_B = new_H-B2 - old_H-B2
- corr_B_E = correlation(B, E) from matrix
- expected_delta_E = corr_B_E × delta_B
- If |expected_delta_E| > 0.05:
    Flag in edition output: "PROPAGATION ALERT: Case B movement suggests H-E2 should move by X. Review before finalizing."

## Step 6: Calibration Update (Brier Score)

For each resolved prediction this sweep (forward flag that resolved to CONFIRMED or CONTRADICTED):
- brier = (predicted_prob - actual_outcome)²
    - actual_outcome = 1 if event occurred, 0 if not
- old_ema = current EMA Brier for that family
- new_ema = (0.9 × old_ema) + (0.1 × brier)
- Update Band Factor based on new_ema:
    - <0.05: factor = 0.8 (narrow bands by 20%)
    - 0.05-0.10: factor = 0.9 (narrow by 10%)
    - 0.10-0.20: factor = 1.0 (no change)
    - 0.20-0.30: factor = 1.2 (widen by 20%)
    - >0.30: factor = 1.5 (widen by 50%)
- Increment N by 1

## Step 7: Apply Band Adjustments to Edition Output

For each hypothesis family (H-A, H-B, H-C, H-D, H-E):
- Original low and high from Calibration Map
- Midpoint = (low + high) ÷ 2
- Half-width = (high - low) ÷ 2
- New half-width = half-width × band_factor
- Adjusted low = max(0, midpoint - new half-width)
- Adjusted high = min(1, midpoint + new half-width)
- Round to nearest whole percentage
- Output adjusted ranges in the edition PDF

## Step 8: Update Sweep History

Add this sweep's probabilities to the Sweep History table:
- H-A1 (midpoint)
- H-B2 (midpoint)
- H-C1 (midpoint)
- H-D2 (midpoint)
- H-E2 (midpoint)
- Keep only last 10 sweeps (drop oldest if over 10)

-----

# BAYESIAN LAYER TABLES

## Causal Edges

| Cause | Effect | Weight | Last Updated |
|-------|--------|--------|--------------|
| IRGC_kinetic_incidents | Hormuz_closure | 0.85 | Ed030 |
| Hormuz_closure | Oil_price_disruption | 0.92 | Ed030 |
| Trump_may_not_extend | Ceasefire_extension_H_A3 | -0.67 | Ed030 |
| GL_U_lapse | H_E2_probability | 0.68 | Ed030 |
| Azizi_SNSC_statement | H_B1_ceiling | -0.71 | Ed030 |
| Mein_Schiff_4_threat | H_B2_probability | 0.74 | Ed030 |
| Lebanon_IDF_shelling | Hezbollah_barrage_H_C3 | 0.34 | Ed030 |

*(Add new edges as they appear in sources)*

## Change Points Log

| Sweep | Hypothesis | Z-Score | Primary Driver |
|-------|------------|---------|----------------|
| Ed029 | H-B1 | -1.7 | Azizi SNSC endorsement |
| Ed029 | H-B2 | +1.9 | Mein Schiff 4 threat |
| Ed030 | H-A3 | -2.1 | Trump "may not extend" |

*(Add new change points when |z-score| > 2.0)*

## Calibration Metrics

| Family | EMA Brier | Band Factor | N Resolved |
|--------|-----------|-------------|------------|
| H-A | 0.09 | 0.9 | 12 |
| H-B | 0.14 | 1.1 | 8 |
| H-C | 0.11 | 1.0 | 6 |
| H-D | 0.06 | 0.85 | 4 |
| H-E | 0.14 | 1.1 | 8 |

*(Update when predictions resolve)*

## Correlation Matrix (Cases A-E)

|   | A | B | C | D | E |
|---|---|---|---|---|---|
| A | 1.00 | 0.67 | 0.12 | 0.08 | 0.71 |
| B | 0.67 | 1.00 | 0.09 | 0.23 | 0.84 |
| C | 0.12 | 0.09 | 1.00 | 0.05 | 0.14 |
| D | 0.08 | 0.23 | 0.05 | 1.00 | 0.19 |
| E | 0.71 | 0.84 | 0.14 | 0.19 | 1.00 |

**Metadata:** Confidence = 0.30 (n_sweeps=6, cap at 20) | Prior = 0.5 | Window = 10 sweeps

*(Recalculate each sweep using last 10 sweeps of history)*

## Delta Statistics

| Hypothesis | Mean Δp | Std Δp | Last 5 Δp |
|------------|---------|--------|-----------|
| H-A1 | 0.00 | 0.02 | [0.00, 0.00, 0.00, 0.00, 0.00] |
| H-A2 | +0.015 | 0.01 | [0.01, 0.02, 0.01, 0.015, 0.015] |
| H-A3 | -0.075 | 0.05 | [0.02, -0.03, -0.05, -0.075, -0.04] |
| H-B1 | -0.05 | 0.04 | [-0.02, -0.03, -0.04, -0.05, -0.03] |
| H-B2 | +0.055 | 0.04 | [0.02, 0.03, 0.04, 0.055, 0.03] |
| H-B3 | 0.00 | 0.02 | [0.00, 0.00, 0.00, 0.00, 0.00] |
| H-C1 | 0.00 | 0.01 | [0.00, 0.00, 0.00, 0.00, 0.00] |
| H-C2 | 0.00 | 0.01 | [0.00, 0.00, 0.00, 0.00, 0.00] |
| H-C3 | 0.00 | 0.01 | [0.00, 0.00, 0.00, 0.00, 0.00] |
| H-D2 | 0.00 | 0.01 | [0.00, 0.00, 0.00, 0.00, 0.00] |
| H-D3 | -0.025 | 0.02 | [-0.01, -0.02, -0.02, -0.025, -0.01] |
| H-E1 | -0.035 | 0.03 | [-0.01, -0.02, -0.03, -0.035, -0.02] |
| H-E2 | +0.025 | 0.03 | [0.01, 0.02, 0.02, 0.025, 0.02] |
| H-E3 | 0.00 | 0.01 | [0.00, 0.00, 0.00, 0.00, 0.00] |

*(Update each sweep for hypotheses that changed)*

## Sweep History (Last 10 probabilities for correlation)

| Sweep | H-A1 | H-B2 | H-C1 | H-D2 | H-E2 |
|-------|------|------|------|------|------|
| Ed021 | 0.75 | 0.20 | 0.65 | 0.90 | 0.40 |
| Ed022 | 0.76 | 0.21 | 0.66 | 0.92 | 0.42 |
| Ed023 | 0.74 | 0.22 | 0.65 | 0.91 | 0.41 |
| Ed024 | 0.77 | 0.20 | 0.66 | 0.93 | 0.43 |
| Ed025 | 0.75 | 0.23 | 0.65 | 0.92 | 0.42 |
| Ed026 | 0.76 | 0.22 | 0.66 | 0.94 | 0.44 |
| Ed027 | 0.77 | 0.24 | 0.65 | 0.93 | 0.43 |
| Ed028 | 0.76 | 0.23 | 0.66 | 0.95 | 0.45 |
| Ed029 | 0.77 | 0.23 | 0.66 | 0.95 | 0.45 |
| Ed030 | 0.77 | 0.285 | 0.66 | 0.95 | 0.475 |

*(Add new sweep, drop oldest — keep exactly 10 rows)*

-----

## CRITICAL WINDOWS

|Window                                  |Status                         |Action                                                                        |
|----------------------------------------|-------------------------------|------------------------------------------------------------------------------|
|GL U lapse — 0401 GMT 19 April          |**T-1.5 HOURS — IMMINENT**     |OFAC fetch mandatory at trigger. PRED series resolve. H-E reversion activates.|
|Lebanon 72-hr window — 2200 GMT 19 April|**T-21.5 HOURS — CRITICAL**    |Gate 0.3 CNN/NBC/AJ/JP. PRED series resolve.                                  |
|Second round — Monday Islamabad         |NEAR-CONFIRMED PROVISIONAL     |Iranian sources only. No US confirmation. Mandatory Ed031.                    |
|Hormuz re-closure — IRGC posture        |ACTIVE — Gate 5 Case B         |AIS re-verify. SNSC statement. USN kinetic = PRED-022-B CONFIRMED.            |
|Ceasefire expiry — ~0000 GMT 22 April   |T-3.5 DAYS                     |Extension or second round required.                                           |
|IRGC follow-on Yanbu/Petroline          |ELEVATED — H-E2 40–55% DOMINANT|Gate 0.3 each sweep. GL U T-1.5H. Lebanon T-21.5H.                            |
|Khurais re-verification                 |OVERDUE 6 DAYS                 |Saudi MoE or Kpler MANDATORY Ed031.                                           |
|Northwood summit                        |THIS WEEK                      |Named schedule = H-B3 rises to 35–45%.                                        |

-----

## ED031 MANDATORY SWEEP ACTIONS

1. OFAC FETCH 0401 GMT 19 APRIL — FIRST ACTION. PRED-022-C/023-B/026-D/029-D/030-D resolve.
2. LEBANON 72-HR WINDOW 2200 GMT 19 APRIL — Gate 0.3. PRED-029-C/026-C/028-C/030-C resolve.
3. SECOND ROUND STATUS — Formal announcement since 2227 GMT?
4. HORMUZ AIS RE-VERIFY — Post re-closure data. SNSC statement. USN response.
5. TRUMP CEASEFIRE EXTENSION POSITION.
6. IRGC YANBU/PETROLINE — Gate 0.3. Strike = PRED series CONFIRMED.
7. IRGC KINETIC USN — Any kinetic = PRED-022-B CONFIRMED, ESCALATING CRITICAL.
8. KHURAIS RE-VERIFY — Saudi MoE or Kpler. Stale 7 days at Ed031.
9. NORTHWOOD OUTPUT — Named schedule = H-B3 rises.
10. AI-007 CALIBRATION CHECK — Band governance before publication.
11. PCP STEP 1.5 — New signal check.
12. TQL MANDATORY — All four items all five cases.
13. **BAYESIAN LAYER EXECUTION** — Run Steps 1-8 above before generating output.
14. PDF: EDITION="031", DATE_STR="19 APRIL 2026", GMT_NOW correct.

-----

## PREDICTION LOG — OPEN

|Ref                               |Flag                            |Window             |Status                                                |
|----------------------------------|--------------------------------|-------------------|------------------------------------------------------|
|PRED-027-B/028-B                  |Hormuz AIS 48h+                 |18 April           |**CONTRADICTED** — Hormuz closed 18 April. Ed029.     |
|PRED-022-C/023-B/026-D/029-D/030-D|GL U lapse                      |0401 GMT 19 April  |**NEAR-CONFIRMED T-1.5H**                             |
|PRED-029-C/026-C/028-C/030-C      |Lebanon 72-hr window            |2200 GMT 19 April  |MONITORING — T-21.5H                                  |
|PRED-030-A/029-A series           |Second round                    |22 April           |PENDING — Iranian sources: Monday. No US confirmation.|
|PRED-022-B                        |IRGC kinetic vs USN             |22 April           |PENDING — Three non-USN incidents 18 April.           |
|PRED-030-E/029-E/028-E/027-E      |IRGC follow-on Yanbu/Petroline  |22 April           |PENDING — H-E2 40–55% dominant.                       |
|PRED-030-B/029-B                  |Hormuz posture                  |Ongoing            |MONITORING — Gate 5 active.                           |
|PRED-015-A                        |Ceasefire extension             |22 April           |PROVISIONAL — Trump "may not extend."                 |
|PRED-025-C/026-B                  |Summit assets + timeline        |Northwood this week|PARTIAL                                               |
|PRED-025-B                        |IRGC total Gulf/Red Sea blockade|22 April           |PENDING                                               |
|PRED-022-E                        |Chinese-flag / US-China         |22 April           |PARTIAL                                               |

-----

## CARRY-FORWARD FACTS — 2227 GMT 18 APRIL 2026

|Fact                                                                                             |Last Verified                                |Ed031 Action                                        |
|-------------------------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------------------|
|Lebanon killed: 2,196+ / wounded: 7,185+                                                         |17 April — Lebanese Health Ministry (Tier 1).|Re-verify Ed031.                                    |
|GL U: expires 0401 GMT 19 April. No retroactive instrument at 2227 GMT.                          |2227 GMT 18 April — OFAC (Tier 1).           |OFAC FETCH MANDATORY 0401 GMT.                      |
|Hormuz: RE-CLOSED 18 April. Sanmar Herald fired on. Mein Schiff 4 threatened. Container ship hit.|2227 GMT 18 April — UKMTO Tier 1. CURRENT.   |AIS re-verify. SNSC statement. USN response monitor.|
|Lebanon ceasefire: Hour 27. Sub-escalatory IDF violations. No Hezbollah barrage.                 |2227 GMT 18 April — Gate 0.3. CURRENT.       |72-hr window closes 2200 GMT 19 April.              |
|Khurais: 300K bpd OFFLINE — STALE 6 DAYS. DO NOT CARRY AT PRIOR CONFIDENCE.                      |12 April — Saudi MoE (Tier 1).               |KHURAIS RE-VERIFY URGENT. Mandatory Ed031.          |
|East-West Pipeline: 7M bpd restored.                                                             |12 April — Saudi MoE (Tier 1). Stale.        |Re-verify Ed031.                                    |
|USN blockade: 19 vessels turned back. No US ships attacked.                                      |18 April — CENTCOM (Tier 1). CURRENT.        |Re-verify Ed031.                                    |
|Paris Summit: 51-nation Hormuz Initiative. Northwood this week.                                  |17 April — GOV.UK (Tier 1).                  |Northwood output mandatory Ed031.                   |
|Trump "PROHIBITED" Lebanon: sustained. Self-defence carveout.                                    |18 April — Truth Social (Tier 1).            |Monitor sustainability.                             |
|OFAC staffing 22 of 40.                                                                          |Ed016 — PERMANENTLY STALE.                   |DO NOT CITE UNDER ANY CIRCUMSTANCES.                |

-----

## BAYESIAN METADATA

| Parameter | Value | Description |
|-----------|-------|-------------|
| causal_decay_rate | 0.7 | Exponential smoothing for edge weights |
| anomaly_threshold | 2.0 | Standard deviations for change-point detection |
| correlation_window | 10 | Sweeps used for cross-case correlation |
| correlation_confidence | 0.30 | Current confidence (n_sweeps=6, cap at 20) |
| correlation_prior | 0.5 | Shrinkage target for low-confidence correlations |
| brier_ema_alpha | 0.9 | Exponential moving average for calibration |
| band_adjustment_active | true | Apply calibration factors to probability ranges |
| cross_case_propagation | true | Flag when expected delta > 0.05 |
| last_full_calibration | Ed030 | Most recent calibration audit |

-----

*SESSION_STATE.md · AtollSphere · LS AI Systems · Bayesian-Enhanced Edition · 18 April 2026 · 2227 GMT (2327 BST) · v2.0 · All Bayesian Instructions Self-Contained*