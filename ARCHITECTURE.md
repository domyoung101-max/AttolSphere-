# ATOLLSPHERE ARCHITECTURE v1.1.3
## LS AI Systems · Internal · Not for Distribution

### VERSION HISTORY
| VERSION | DATE | SUMMARY |
|---|---|---|
| v1.1.2 | 09 Apr | GMT timestamp mandate, ESCALATING-PROVISIONAL 120-min late-watch, TQL Tier 3 flag |
| v1.1.3 | 10 Apr | 18 feeds formalised by tier, actor/Navigator language removed |

---

## 1. PLATFORM IDENTITY
- **Product:** AttolSphere — GSINT intelligence brief platform
- **Parent:** LS AI Systems
- **Tagline:** SMARTER AI PREDICTION SYSTEMS
- **Operator:** UK-based. BST (UTC+1).
- **Timestamp standard:** GMT primary. BST in parentheses only. Offset calculated programmatically. Manual input prohibited.
- **Master template:** build_1.1.0.py v1.1.3
- **Logos:** ls_logo_v2.png · atollsphere_logo_v2.png

---

## 2. REASONING GOVERNANCE PROTOCOL

| RULE | NAME | REQUIREMENT |
|---|---|---|
| Rule 1 | DEPENDENCY RESOLUTION | Before generating any response, every interconnected constraint must be resolved. Pattern-matched summaries not acceptable. |
| Rule 2 | COHERENCE UNDER PRESSURE | Every analytical section must pass a quality gate. |
| Rule 3 | EVIDENCE WEIGHT LADDER | Claims calibrated to source strength. Four-tier hierarchy governs this. |
| Rule 4 | NO RHETORICAL HEDGING | No disclaimers or preambles. Uncertainty expressed through evidentiary tiering only. |

**Execution checklist — non-negotiable per response:**
1. Evidence tier assignment — every source cited must have tier stated
2. Mechanism vs resemblance distinction — every connection drawn must be classified
3. Domain quality assessment — every analytical section closes with plain statement of whether evidence supports conclusion structurally or at surface level only

---

## 3. SOURCING FRAMEWORK — 18 NAMED FEEDS BY TIER

### TIER 1 — Primary Source (5 feeds)
1. Trump Truth Social / White House official statements
2. CENTCOM public affairs
3. IDF official statements
4. Iran SNSC / IRNA (named attribution)
5. Named government spokesperson statements (Araghchi X, Leavitt presser, etc.)

### TIER 2 — High-Authority Secondary (7 feeds)
6. Reuters
7. AP
8. Bloomberg
9. Al Jazeera
10. NBC News live updates
11. CBS News live updates
12. NPR

### TIER 3 — Watch / Corroboration Required (4 feeds)
13. Tasnim News Agency (IRGC-linked)
14. Mehr News Agency (Iranian state, unattributed)
15. WANA News Agency
16. House of Saud / Conflict Pulse (specialist analysis)

### TIER 4 — Editorial Assembly (2 feeds)
17. Wikipedia — Iran war timeline
18. ACLED conflict monitor

**Sweep requirement:** All 18 feeds checked before any analytical content written (PCP Step 1). Fewer than 18 feeds swept = bypass declared with justification and risk per Rule 1.

**Gate 0.4 Resolution Protocol (v1.1.1):**
- HIGH incentive + Tier 1 → mandatory Gate 0.2 search
- No competing primary found → downgrade to Tier 2 for all confidence calibration
- Note: "Tier 1 — downgraded to Tier 2 (HIGH incentive, no competing primary per Gate 0.2)"

---

## 4. CDIT ANALYTICAL FRAMEWORK (v1.1.3)

### GATE 0 — PRE-INTAKE FACT VERIFICATION
All four checks mandatory on every row before any fact enters Part 1.

| GATE | NAME | REQUIREMENT | VERSION |
|---|---|---|---|
| 0.1 | TEMPORAL CURRENCY | Current as of sweep timestamp (GMT)? If outdated: flag "STATUS AS OF [DATE TIME GMT] — VERIFY BEFORE PUB." | v1.0.4 / v1.1.2 |
| 0.2 | COMPETING PRIMARY SOURCE | Second primary party characterise event differently? If yes: SEPARATE Part 1 rows. Never merge. MANDATORY when Gate 0.4 flags HIGH incentive on Tier 1. | v1.0.4 / v1.1.1 |
| 0.3 | SOURCE-TO-CLAIM TRACEABILITY | Traceable to named source? If not: mark "CARRY-FORWARD FROM EDITION [N] — NOT RE-VERIFIED." | v1.0.4 |
| 0.4 | SOURCE INCENTIVE ANALYSIS | (a) What does source gain if believed? (b) Incentive structure? (c) Deception plausible? Flag: "Incentive: [low/medium/high] — [rationale]" | v1.1.0 / v1.1.1 |

### MANDATORY CASE SEQUENCE

| ELEMENT | FUNCTION | REQUIREMENT |
|---|---|---|
| CASE BANNER | tag_table() | Letter, title, one of 9 status tags, one of 4 confidence levels. dominant_hyp_prob_upper <60% → confidence capped at MEDIUM. |
| PREDICTION LOG UPDATE | pred_update() | OPTIONAL. Only when prior PRED-NNN-X affected. Multi-state outcome required. |
| PART 1 — FACT TABLE | fact_table() | Two columns: fact (117mm) / source attribution (46mm). Gate 0 all four checks on every row. |
| PART 2 — INCONGRUITY | Paragraph body | MANDATORY. Names heuristics applied (H1–H6). AFC closing element. Ends with INFERENCE and domain quality assessment. Subject to bypass ceiling. |
| PART 3 — HYPOTHESIS SET | hyp_table() | Minimum 2 hypotheses. Each carries probability estimate. Asymmetric weighting allowed. Extract dominant_hyp_prob_upper for tag_table() validation. |
| PART 4 — TRUTH QUALITY CHECK | tql_block() | MANDATORY. Names: (1) assumptions; (2) fragile fact with tier; (3) high-impact uncertainty. Tier 3/4 fragile fact raises TQL WARNING. Tag decision is analytical judgement — automatic tag changes prohibited. |
| PART 5 — DISCONFIRMATION | disconf_table() | CONFIRMS/CONTRADICTS pairs. Multi-state outcome. Gate 5 Framing Revision Trigger required. |
| FORWARD FLAG | flag_block() | One prediction per case. Must pass all 5 criteria (C1–C5). Numbered sequentially. |

---

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

**Named failure mode:** "Theatre of Rigor" — skeleton appearance prioritised over consistent execution.

---

## 6. SIX HEURISTICS (H1–H6)

| H | NAME | ANALYTICAL QUESTION |
|---|---|---|
| H1 | INCENTIVE MISMATCH | Who benefits from this narrative being believed? Does stated motive match observable outcome? |
| H2 | TIMING CONVERGENCE | Why now? What concurrent events explain or exploit this timing? |
| H3 | BENEFICIARY ASYMMETRY | Who gains disproportionately vs who appears to be acting? |
| H4 | NARRATIVE VS OUTCOME GAP | Do both parties' accounts agree? Can both outcomes be true simultaneously? |
| H5 | STRUCTURAL CONTRADICTION | Do stated positions contain claims that cannot simultaneously be true? |
| H6 | SUPPRESSED INTERSECTION | Are two developments sharing a common actor, motive, or dependency not being named? |

**NOTE:** Heuristic Performance Tracking (HPT) deferred to Edition 020.

---

## 7. FIVE-CRITERIA PREDICTION STANDARD (v1.1.0)

| C | CRITERION | REQUIREMENT |
|---|---|---|
| C1 | EXPLICITLY FORWARD-LOOKING | Describes future event, not current conditions. |
| C2 | SPECIFIC AND NAMED | Names specific actor, action, or measurable metric. |
| C3 | GENUINELY FALSIFIABLE AND UNAMBIGUOUS | Opposite must be possible, meaningful, AND unambiguous. Silence/absence/delay alone require co-condition. |
| C4 | NOT DERIVABLE FROM EXTRAPOLATION | Requires specific observable trigger or decision point. |
| C5 | ANALYTICALLY VALUABLE | Must: (a) resolve live uncertainty; (b) affect a decision; or (c) differentiate hypotheses in ways that change framing. |

---

## 8. STATUS TAGS (9) — v1.1.3

| TAG | COLOUR | HEX | DEFINITION |
|---|---|---|---|
| ESCALATING | RED | #B83232 | Active threat to framing. |
| ESCALATING-PROVISIONAL | AMBER | #C47D1A | Tier 3-only. Standard: 90 min (06:01–23:59 GMT). Late-watch: 120 min (00:00–06:00 GMT). Cannot stack with declared bypass. Downgrades to WATCH if unverified. |
| DEVELOPING | AMBER | #C47D1A | Signal present and evolving. |
| NEW | TEAL | #3DBDB0 | First appearance. |
| ELEVATED | NAVY | #1B2A4A | Rising significance above baseline. |
| STABLE | GREEN | #2C7A4B | Conditions not materially changing. |
| RESOLVED | MID-GREY | #8A8A8A | Case closed. |
| DE-ESCALATING | DK-GREEN | #4A7C4E | Prior escalation reduced. |
| WATCH | PURPLE | #6B3FA0 | Peripheral signal. |

---

## 9. CONFIDENCE LEVELS — CALIBRATED RANGES (v1.1.1)

| LABEL | RANGE | MEANING | COLOUR |
|---|---|---|---|
| HIGH | 70–90% | Evidence strongly supports. Multiple Tier 1/2 sources. | GREEN #2C7A4B |
| MEDIUM | 55–70% | Evidence supports but material uncertainty remains. | AMBER #C47D1A |
| LOW-MEDIUM | 40–55% | Mixed signals. Competing interpretations viable. | AMBER #C47D1A |
| LOW | 25–40% | Insufficient evidence. Hypothesis speculative. | RED #B83232 |

**Constraint (v1.1.1):** If dominant hypothesis probability_range upper bound is below 60%, confidence banner CANNOT exceed MEDIUM. Hard validation rule.

---

## 10. PREDICTION OUTCOME STATES (v1.1.0)

| OUTCOME STATE | WHEN TO USE |
|---|---|
| CONFIRMED | Prediction clearly and unambiguously realised. |
| CONTRADICTED | Opposite clearly realised. → PMM triggered. |
| PARTIAL | Named elements confirmed, others not. |
| AMBIGUOUS | Evidence both sides. Cannot classify. |
| UNRESOLVABLE | Window closed, insufficient evidence. → PMM triggered. |

---

## 11. POST-MORTEM MODULE (PMM) — v1.1.1

Triggered on CONTRADICTED or UNRESOLVABLE only. NOT on CONFIRMED, PARTIAL, or AMBIGUOUS.

**Format:**
