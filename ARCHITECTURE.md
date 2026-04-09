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
| PART 5 — DISCONFIRMATION | disconf​​​​​​​​​​​​​​​​
