# ATOLLSPHERE ARCHITECTURE v1.2.1

## LS AI Systems · Internal · Not for Distribution

### VERSION HISTORY

|VERSION|DATE  |SUMMARY                                                                                                                                                                                                                                                                                   |
|-------|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|v1.1.2 |09 Apr|GMT timestamp mandate, ESCALATING-PROVISIONAL 120-min late-watch, TQL Tier 3 flag                                                                                                                                                                                                         |
|v1.1.3 |10 Apr|18 feeds formalised by tier, actor/Navigator language removed                                                                                                                                                                                                                             |
|v1.2.0 |11 Apr|C3 patch (silence/ambiguity pre-assignment), Bypass Override Protocol, status_history mandate, SYSTEM_CHANGE_LOG created                                                                                                                                                                  |
|v1.2.1 |11 Apr|Gate 0.5 (source independence), H1 saturation check, WATCH/PARTIAL/AMBIGUOUS disconfirmation rule, New Signal Check (PCP Step 1.5), Part 2 claim-type labelling, Wikipedia usage rule, confidence calibration audit schedule, Analytical Improvement Log added to SYSTEM_CHANGE_LOG format|

-----

## 1. PLATFORM IDENTITY

- **Product:** AtollSphere — GSINT intelligence brief platform
- **Parent:** LS AI Systems
- **Tagline:** SMARTER AI PREDICTION SYSTEMS
- **Operator:** UK-based. BST (UTC+1).
- **Timestamp standard:** GMT primary. BST in parentheses only. Offset calculated programmatically. Manual input prohibited.
- **Master template:** build_1.1.0.py v1.2.1
- **Logos:** ls_logo_v2.png · atollsphere_logo_v2.png

-----

## 2. REASONING GOVERNANCE PROTOCOL

|RULE  |NAME                    |REQUIREMENT                                                                                                                                                                   |
|------|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Rule 1|DEPENDENCY RESOLUTION   |Before generating any response, every interconnected constraint must be resolved. Pattern-matched summaries not acceptable.                                                   |
|Rule 2|COHERENCE UNDER PRESSURE|Every analytical section must pass a quality gate.                                                                                                                            |
|Rule 3|EVIDENCE WEIGHT LADDER  |Claims calibrated to source strength. Four-tier hierarchy governs this.                                                                                                       |
|Rule 4|NO RHETORICAL HEDGING   |No disclaimers or preambles. Uncertainty expressed through evidentiary tiering only.                                                                                          |
|Rule 5|CLAIM-TYPE TRANSPARENCY |Facts, inferences, and predictions must be distinguishable within analytical prose. Conflation of these three types is a named failure mode. See Section 4 Part 2 requirement.|

**Execution checklist — non-negotiable per response:**

1. Evidence tier assignment — every source cited must have tier stated
1. Source independence check — corroboration confirmed as upstream-independent before treating as multiply-verified (Gate 0.5)
1. Mechanism vs resemblance distinction — every connection drawn must be classified
1. Claim-type labelling — FACT / INFERENCE / PREDICTION distinguished in Part 2 drafting
1. Domain quality assessment — every analytical section closes with plain statement of whether evidence supports conclusion structurally or at surface level only

-----

## 3. SOURCING FRAMEWORK — 18 NAMED FEEDS BY TIER

### TIER 1 — Primary Source (5 feeds)

1. Trump Truth Social / White House official statements
1. CENTCOM public affairs
1. IDF official statements
1. Iran SNSC / IRNA (named attribution)
1. Named government spokesperson statements (Araghchi X, Leavitt presser, etc.)

### TIER 2 — High-Authority Secondary (7 feeds)

1. Reuters
1. AP
1. Bloomberg
1. Al Jazeera
1. NBC News live updates
1. CBS News live updates
1. NPR

### TIER 3 — Watch / Corroboration Required (4 feeds)

1. Tasnim News Agency (IRGC-linked)
1. Mehr News Agency (Iranian state, unattributed)
1. WANA News Agency
1. House of Saud / Conflict Pulse (specialist analysis)

### TIER 4 — Editorial Assembly (2 feeds)

1. Wikipedia — Iran war timeline
1. ACLED conflict monitor

**Sweep requirement:** All 18 feeds checked before any analytical content written (PCP Step 1). Fewer than 18 feeds swept = bypass declared with justification and risk per Rule 1.

**Gate 0.4 Resolution Protocol (v1.1.1):**

- HIGH incentive + Tier 1 → mandatory Gate 0.2 search
- No competing primary found → downgrade to Tier 2 for all confidence calibration
- Note: “Tier 1 — downgraded to Tier 2 (HIGH incentive, no competing primary per Gate 0.2)”

**Wikipedia Usage Rule (v1.2.1):**
Wikipedia forward-looking timeline data (future session dates, predicted outcomes, post-sweep developments) is Tier 4 — directional corroboration only. Hard constraints:

- Cannot be the sole or primary support for any hypothesis probability range
- Cannot satisfy Gate 0.3 (source-to-claim traceability) for any forward-looking claim
- Cannot be used to justify a confidence level that Tier 1/2 evidence alone would not support
- Any finding relying on Wikipedia forward data must pass the Tier 4 dependency test in TQL Part 4 (Section 4)
- Gate 0.4 must note: Wikipedia is editorial assembly of the same Tier 1/2 feeds already swept, plus potential forward projection by editors. Treat as Tier 4 with HIGH editorial incentive uncertainty — not neutral aggregation

-----

## 4. CDIT ANALYTICAL FRAMEWORK (v1.2.1)

### GATE 0 — PRE-INTAKE FACT VERIFICATION

All five checks mandatory on every row before any fact enters Part 1.

|GATE|NAME                        |REQUIREMENT                                                                                                                                                                                                                                                                                                                                                                                                                    |VERSION        |
|----|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
|0.1 |TEMPORAL CURRENCY           |Current as of sweep timestamp (GMT)? If outdated: flag “STATUS AS OF [DATE TIME GMT] — VERIFY BEFORE PUB.”                                                                                                                                                                                                                                                                                                                     |v1.0.4 / v1.1.2|
|0.2 |COMPETING PRIMARY SOURCE    |Second primary party characterise event differently? If yes: SEPARATE Part 1 rows. Never merge. MANDATORY when Gate 0.4 flags HIGH incentive on Tier 1.                                                                                                                                                                                                                                                                        |v1.0.4 / v1.1.1|
|0.3 |SOURCE-TO-CLAIM TRACEABILITY|Traceable to named source? If not: mark “CARRY-FORWARD FROM EDITION [N] — NOT RE-VERIFIED.” Wikipedia forward-looking claims cannot satisfy this gate regardless of named attribution.                                                                                                                                                                                                                                         |v1.0.4 / v1.2.1|
|0.4 |SOURCE INCENTIVE ANALYSIS   |(a) What does source gain if believed? (b) Incentive structure? (c) Deception plausible? Flag: “Incentive: [low/medium/high] — [rationale]”                                                                                                                                                                                                                                                                                    |v1.1.0 / v1.1.1|
|0.5 |SOURCE INDEPENDENCE CHECK   |Are sources treating a fact as multiply-corroborated drawing from independent primary observations? If two or more sources share an upstream feed (e.g. multiple outlets citing same Kpler data, same wire report, same government statement), treat as SINGLE-SOURCE regardless of outlet count. Flag: “Upstream: [named feed or INDEPENDENT].” Multiple echoes of a single source do not constitute independent verification.|v1.2.1         |

### MANDATORY CASE SEQUENCE

|ELEMENT                     |FUNCTION       |REQUIREMENT                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|CASE BANNER                 |tag_table()    |Letter, title, one of 9 status tags, one of 4 confidence levels. dominant_hyp_prob_upper <60% → confidence capped at MEDIUM.                                                                                                                                                                                                                                                                                                                                                            |
|PREDICTION LOG UPDATE       |pred_update()  |OPTIONAL. Only when prior PRED-NNN-X affected. Multi-state outcome required.                                                                                                                                                                                                                                                                                                                                                                                                            |
|PART 1 — FACT TABLE         |fact_table()   |Two columns: fact (117mm) / source attribution (46mm). Gate 0 all five checks on every row including Gate 0.5.                                                                                                                                                                                                                                                                                                                                                                          |
|PART 2 — INCONGRUITY        |Paragraph body |MANDATORY. Each heuristic finding must open with claim-type label: [FACT], [INFERENCE], or [PREDICTION]. AFC closing element mandatory and must label its own claims. INFERENCE closing paragraph must summarise which findings are factual observations versus inferential connections — these must not be blurred. Ends with domain quality assessment as a distinct labelled block separate from prose above. Subject to bypass ceiling. H1 saturation check applies (see Section 6).|
|PART 3 — HYPOTHESIS SET     |hyp_table()    |Minimum 2 hypotheses. Each carries probability estimate. Asymmetric weighting allowed. Extract dominant_hyp_prob_upper for tag_table() validation. Where any hypothesis relies on Tier 4 data, corroboration legs must be explicitly separated: Leg 1 (Tier 1/2 only) and Leg 2 (Tier 4 directional). Leg 1 must independently sustain the stated probability range. If it cannot, reduce the range.                                                                                    |
|PART 4 — TRUTH QUALITY CHECK|tql_block()    |MANDATORY. Names: (1) assumptions; (2) fragile fact with tier; (3) high-impact uncertainty; (4) Tier 4 dependency test — if any hypothesis relies on Tier 4 data, explicitly state whether Tier 1/2 evidence alone sustains the probability range [Yes/No + one sentence]. Tier 3/4 fragile fact raises TQL WARNING. Tag decision is analytical judgement — automatic tag changes prohibited.                                                                                           |
|PART 5 — DISCONFIRMATION    |disconf_table()|CONFIRMS/CONTRADICTS pairs. Multi-state outcome. Gate 5 Framing Revision Trigger required.                                                                                                                                                                                                                                                                                                                                                                                              |
|FORWARD FLAG                |flag_block()   |One prediction per case. Must pass all 5 criteria (C1–C5). Numbered sequentially.                                                                                                                                                                                                                                                                                                                                                                                                       |

### DEFERRED OUTCOME DISCONFIRMATION RULE (v1.2.1)

Any prediction assigned WATCH, PARTIAL, or AMBIGUOUS outcome must include an explicit statement in TQL Part 4 answering: “What evidence would have produced CONTRADICTED instead of this outcome?” This statement is mandatory — it cannot be omitted. Its purpose is to prevent escape-hatch assignment of deferred outcomes without genuine analytical accountability.

-----

## 5. FORMAT GOVERNANCE — RULE 1 (v1.1.1)

**No CDIT section may be SILENTLY bypassed.**

**Declared Bypass Protocol:**

- (a) BYPASS DECLARED: [Section name]
- (b) JUSTIFICATION: [One sentence]
- (c) RISK: [One sentence — analytical risk of omission]

**Bypass Ceiling (v1.1.1):** Maximum ONE declared bypass per Case per Edition.

**Bypass Ceiling Reached Protocol:**

- (a) BYPASS CEILING REACHED: [Case] — [Edition]
- (b) SECTIONS AFFECTED: [list]
- (c) DISPOSITION: defer to next Edition OR reduce to WATCH tag

**Named failure modes:**

- “Theatre of Rigor” — skeleton appearance prioritised over consistent execution
- “Claim-Type Conflation” — facts, inferences, and predictions presented in undifferentiated prose, creating false certainty
- “Source Amplification” — treating multiple downstream echoes of a single upstream source as independent corroboration
- “Escape-Hatch Assignment” — using WATCH, PARTIAL, AMBIGUOUS, or DIRECTIONAL labels to preserve preferred narrative when disconfirmation evidence is present

-----

## 6. SIX HEURISTICS (H1–H6)

|H |NAME                    |ANALYTICAL QUESTION                                                                          |
|--|------------------------|---------------------------------------------------------------------------------------------|
|H1|INCENTIVE MISMATCH      |Who benefits from this narrative being believed? Does stated motive match observable outcome?|
|H2|TIMING CONVERGENCE      |Why now? What concurrent events explain or exploit this timing?                              |
|H3|BENEFICIARY ASYMMETRY   |Who gains disproportionately vs who appears to be acting?                                    |
|H4|NARRATIVE VS OUTCOME GAP|Do both parties’ accounts agree? Can both outcomes be true simultaneously?                   |
|H5|STRUCTURAL CONTRADICTION|Do stated positions contain claims that cannot simultaneously be true?                       |
|H6|SUPPRESSED INTERSECTION |Are two developments sharing a common actor, motive, or dependency not being named?          |

**H1 Saturation Check (v1.2.1):** If H1 fires across three or more cases in a single edition, Part 2 of each H1-affected case must include one explicit sentence asking: “Is H1 the correct heuristic here, or is the framework pattern-matching to a preferred explanation?” The analyst must answer this question — it cannot be left implicit. The purpose is to prevent H1 from becoming a default conclusion rather than a genuine analytical finding. Consistent H1 firing across all cases in multiple consecutive editions should trigger a framework review.

**Heuristic Performance Tracking (HPT):** Commences Edition 020. Each edition from 020 onwards records which heuristics fired, on which cases, and with what outcome correlation.

-----

## 7. FIVE-CRITERIA PREDICTION STANDARD (v1.1.0)

|C |CRITERION                            |REQUIREMENT                                                                                                                                                                                        |
|--|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|C1|EXPLICITLY FORWARD-LOOKING           |Describes future event, not current conditions.                                                                                                                                                    |
|C2|SPECIFIC AND NAMED                   |Names specific actor, action, or measurable metric.                                                                                                                                                |
|C3|GENUINELY FALSIFIABLE AND UNAMBIGUOUS|Opposite must be possible, meaningful, AND unambiguous. Silence/absence/delay alone require co-condition. Wikipedia forward-looking data cannot satisfy this criterion as sole or primary evidence.|
|C4|NOT DERIVABLE FROM EXTRAPOLATION     |Requires specific observable trigger or decision point.                                                                                                                                            |
|C5|ANALYTICALLY VALUABLE                |Must: (a) resolve live uncertainty; (b) affect a decision; or (c) differentiate hypotheses in ways that change framing.                                                                            |

-----

## 8. STATUS TAGS (9) — v1.1.3

|TAG                   |COLOUR  |HEX    |DEFINITION                                                                                                                                                   |
|----------------------|--------|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
|ESCALATING            |RED     |#B83232|Active threat to framing.                                                                                                                                    |
|ESCALATING-PROVISIONAL|AMBER   |#C47D1A|Tier 3-only. Standard: 90 min (06:01–23:59 GMT). Late-watch: 120 min (00:00–06:00 GMT). Cannot stack with declared bypass. Downgrades to WATCH if unverified.|
|DEVELOPING            |AMBER   |#C47D1A|Signal present and evolving.                                                                                                                                 |
|NEW                   |TEAL    |#3DBDB0|First appearance.                                                                                                                                            |
|ELEVATED              |NAVY    |#1B2A4A|Rising significance above baseline.                                                                                                                          |
|STABLE                |GREEN   |#2C7A4B|Conditions not materially changing.                                                                                                                          |
|RESOLVED              |MID-GREY|#8A8A8A|Case closed.                                                                                                                                                 |
|DE-ESCALATING         |DK-GREEN|#4A7C4E|Prior escalation reduced.                                                                                                                                    |
|WATCH                 |PURPLE  |#6B3FA0|Peripheral signal.                                                                                                                                           |

-----

## 9. CONFIDENCE LEVELS — CALIBRATED RANGES (v1.1.1 / v1.2.1)

|LABEL     |RANGE |MEANING                                                                                                 |COLOUR       |
|----------|------|--------------------------------------------------------------------------------------------------------|-------------|
|HIGH      |70–90%|Evidence strongly supports. Multiple Tier 1/2 sources. Independent corroboration confirmed via Gate 0.5.|GREEN #2C7A4B|
|MEDIUM    |55–70%|Evidence supports but material uncertainty remains.                                                     |AMBER #C47D1A|
|LOW-MEDIUM|40–55%|Mixed signals. Competing interpretations viable.                                                        |AMBER #C47D1A|
|LOW       |25–40%|Insufficient evidence. Hypothesis speculative.                                                          |RED #B83232  |

**Constraint (v1.1.1):** If dominant hypothesis probability_range upper bound is below 60%, confidence banner CANNOT exceed MEDIUM. Hard validation rule.

**HIGH confidence additional constraint (v1.2.1):** HIGH confidence requires Gate 0.5 confirmation that corroborating sources are upstream-independent. If all corroborating sources share a single upstream feed, confidence is capped at MEDIUM regardless of outlet count.

**Calibration Audit Schedule (v1.2.1):** At Edition 025, and every tenth edition thereafter, the operator must review the distribution of confidence levels assigned across all completed editions. If HIGH has been assigned to more than 60% of cases across any ten-edition window, the HIGH threshold definition must be reviewed and tightened. This audit is mandatory and cannot be bypassed. Log findings in SYSTEM_CHANGE_LOG as an Analytical Improvement entry.

-----

## 10. PREDICTION OUTCOME STATES (v1.1.0 / v1.2.1)

|OUTCOME STATE|WHEN TO USE                                           |
|-------------|------------------------------------------------------|
|CONFIRMED    |Prediction clearly and unambiguously realised.        |
|CONTRADICTED |Opposite clearly realised. → PMM triggered.           |
|PARTIAL      |Named elements confirmed, others not.                 |
|AMBIGUOUS    |Evidence both sides. Cannot classify.                 |
|UNRESOLVABLE |Window closed, insufficient evidence. → PMM triggered.|

**Deferred outcome rule (v1.2.1):** PARTIAL, AMBIGUOUS, and WATCH assignments are not neutral. Each must be accompanied by an explicit statement of what evidence would have produced CONTRADICTED. This is recorded in TQL Part 4 item (4) and in the prediction log entry. Without this statement the assignment is invalid and must be reclassified or the prediction rewritten.

-----

## 11. POST-MORTEM MODULE (PMM) — v1.1.1

Triggered on CONTRADICTED or UNRESOLVABLE only. NOT on CONFIRMED, PARTIAL, or AMBIGUOUS.

**Format:**

```
POST-MORTEM: [pred_ref] — [outcome_state]
WHAT FAILED: [what_failed]
WHY: [why_failed]
SYSTEM CHANGE: [specific change — "Be more careful" does not qualify]
HEURISTIC IMPLICATED: [H[N] — misapplication]
```

**HEURISTIC_IMPLICATED:** When populated, triggers mandatory CROSS-CASE HEURISTIC REVIEW note in next edition Situation Overview for all active cases.

-----

## 12. PRODUCTION CONTINUITY PROTOCOL (v1.2.1)

|STEP|NAME                         |REQUIREMENT                                                                                                                                                                                                                                                                                                                                                                                             |
|----|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|1   |SWEEP BEFORE WRITING         |All 18 named feeds swept before any analytical content written. Gate 0 applied to all candidate facts first. Gate 0.5 applied to all candidate corroboration.                                                                                                                                                                                                                                           |
|1.5 |NEW SIGNAL CHECK             |Before prediction reconciliation, write one explicit paragraph asking: “Is there any development in this sweep that does not fit any existing case and cannot be addressed within one?” If yes: assess against new case threshold (Step 4). This step is mandatory and cannot be bypassed. Its purpose is to prevent novel developments from being forced into existing case frames or silently dropped.|
|2   |PREDICTION LOG RECONCILIATION|All open predictions assessed before any new case opened. Each assigned five-state outcome. Expired windows formally closed. Any WATCH, PARTIAL, or AMBIGUOUS assignment must include explicit disconfirmation statement per Section 10.                                                                                                                                                                |
|3   |CASE CONTINUITY CHECK        |For each carried-forward case: (a) status tag still accurate? (b) hypothesis set overtaken? (c) Forward Flag window expired?                                                                                                                                                                                                                                                                            |
|4   |NEW CASE THRESHOLD           |New case only if: (a) signal not addressable within existing case; (b) at least one H1–H6 applies; (c) testable Forward Flag meeting C1–C5 can be stated.                                                                                                                                                                                                                                               |
|5   |MASTER TEMPLATE LOCK         |Structural changes to build_1.1.0.py only. Any change requires patch document at next version increment.                                                                                                                                                                                                                                                                                                |
|6   |PREDICTION LOG GOVERNANCE    |Cumulative PRED-NNN-X numbering. Each entry records: edition of origin, flag text, current status, confidence at time of prediction, heuristics applied, dominant disconfirmation condition, confirming/contradicting evidence, five-state outcome. No silent drops.                                                                                                                                    |

-----

## 13. PDF OUTPUT MANDATE (v1.1.3 / v1.2.1)

Sweep output MUST be delivered as a compiled PDF using build_1.1.0.py matching the visual template. Inline prose or markdown does not constitute a valid edition. The build function must be run and the rendered document presented.

**Visual template requirements:**

- Navy header bar with edition/date/sweep designation
- Teal 2mm strip at top of cover
- Cover page with edition stats and case/flag counts
- Case banners: tag_table() with status colour coding
- Fact tables: two-column, alternating row background. Gate 0.5 upstream flag displayed in source attribution column.
- Hypothesis set: equal-width columns, teal dividers. Tier 4 dependency legs (Leg 1 / Leg 2) rendered as distinct sub-rows where applicable.
- TQL WARNING rendered in red italic (afc_note style) before tql_head
- Domain quality assessment rendered as a distinct labelled block at the close of Part 2 — not as a final prose sentence embedded in heuristic analysis
- Disconfirmation table: CONFIRMS (green) / CONTRADICTS (red) on navy header
- Forward flags in teal flag_head style
- Sources section: tier label in teal, incentive in amber, upstream dependency in grey italic
- Light background footer bar with page number

-----

## 14. TIMESTAMP MANDATE (v1.1.2)

```python
import datetime
GMT_NOW = datetime.datetime.utcnow()
BST_OFFSET = datetime.timedelta(hours=1)
BST_NOW = GMT_NOW + BST_OFFSET  # display only, never primary
```

Timestamps in all editions: GMT primary. BST in parentheses only. Manual timestamp entry prohibited. All sweep timestamps generated programmatically.

-----

## 15. SYSTEM CHANGE LOG FORMAT (v1.2.1)

SYSTEM_CHANGE_LOG.md records two distinct entry types. Both are permanent. Neither is deleted or overwritten.

### Entry Type A — PMM-TRIGGERED RULE CHANGE

Triggered by CONTRADICTED or UNRESOLVABLE prediction outcome. Format:

|FIELD               |CONTENT                                             |
|--------------------|----------------------------------------------------|
|ENTRY TYPE          |PMM-TRIGGERED                                       |
|PMM REF             |The prediction reference that triggered the PMM     |
|OUTCOME STATE       |CONTRADICTED or UNRESOLVABLE                        |
|HEURISTIC IMPLICATED|Which of H1–H6 was misapplied                       |
|WHAT FAILED         |One sentence                                        |
|RULE CHANGE         |The specific new rule — vague changes do not qualify|
|SECTION AFFECTED    |Which ARCHITECTURE.md section was patched           |
|IN FORCE FROM       |Edition number                                      |

### Entry Type B — ANALYTICAL IMPROVEMENT

Triggered by external review, operator analysis, red-team critique, or internal quality review. Does not require a failed prediction. Format:

|FIELD           |CONTENT                                                                                                                    |
|----------------|---------------------------------------------------------------------------------------------------------------------------|
|ENTRY TYPE      |ANALYTICAL IMPROVEMENT                                                                                                     |
|IMPROVEMENT REF |Sequential AI-NNN numbering                                                                                                |
|SOURCE          |What triggered the improvement (e.g. “ChatGPT external review Ed017”, “Red-team critique Ed018”, “Operator analysis Ed018”)|
|WHAT CHANGED    |One sentence describing the analytical or structural change                                                                |
|RULE CHANGE     |The specific new rule or constraint added                                                                                  |
|SECTION AFFECTED|Which ARCHITECTURE.md section was patched                                                                                  |
|IN FORCE FROM   |Edition number                                                                                                             |

-----

## 16. WIKIPEDIA USAGE RULE (v1.2.1)

Restated here for clarity as a standalone section given its cross-cutting impact.

Wikipedia is retained in the source registry as Tier 4. Its legitimate and constrained role:

- **Permitted:** Directional corroboration of process-level claims (talks are continuing, a session occurred) where Tier 1/2 sources independently confirm the same direction
- **Permitted:** Historical timeline reference for completed events where no incentive distortion applies
- **Not permitted:** Load-bearing support for hypothesis probability ranges
- **Not permitted:** Satisfying Gate 0.3 for any forward-looking claim
- **Not permitted:** Justifying a confidence level that Tier 1/2 evidence alone would not support
- **Not permitted:** Forward-looking claims about future session dates or predicted outcomes unless independently corroborated by Tier 1/2

Gate 0.4 assessment for Wikipedia must always note: “Editorial assembly of Tier 1/2 feeds already swept plus potential editor forward-projection. Upstream independence not confirmed. Treat as single editorial synthesis, not independent verification.”

-----

## 17. ARCHITECTURE CHANGE CONTROL

All patches to this document must be:

1. Logged in SYSTEM_CHANGE_LOG.md with entry type (PMM-Triggered or Analytical Improvement)
1. Version-incremented in the header (minor patch = third digit; structural change = second digit)
1. Referenced in the active SESSION_STATE.md pending patch list until committed to the repository via Claude Code

**Pending as of v1.2.1:** No further patches pending. SESSION_STATE Ed019 pending patch list cleared by this commit.