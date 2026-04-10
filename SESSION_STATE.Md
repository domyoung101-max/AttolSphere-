# ATOLLSPHERE SESSION STATE
## Paste this at the start of every new Sonnet chat session.

---

## PLATFORM
- Product: AtollSphere — GSINT intelligence brief platform
- Parent: LS AI Systems
- Operator: UK-based. BST (UTC+1). GMT primary for all timestamps.
- Architecture version: v1.2.0
- Build: build_1.1.0.py v1.2.0

---

## REPOSITORY
github.com/domyoung101-max/AttolSphere-

### Current file structure (target — not yet fully implemented):
AtollSphere/
├── architecture/
│   ├── ARCHITECTURE.md          # v1.2.0
│   ├── SYSTEM_CHANGE_LOG.md     # Entry 001 logged
│   └── CHANGELOG.md             # Pending creation
├── build/
│   ├── build_core.py            # Pending refactor
│   ├── build_edition.py         # Pending refactor
│   └── styles.py                # Pending refactor
├── data/
│   ├── PREDICTION_LOG.json      # v1.2.0 — updated Ed014
│   └── SOURCE_REGISTRY.json     # Pending creation
├── outputs/
│   └── .gitkeep
└── README.md                    # Pending creation

---

## CURRENT EDITION
- Last completed: Edition 014 Morning Sweep — 10 April 2026
- Next: Edition 014 Evening Sweep OR Edition 015 Morning Sweep
- War day: 42

---

## ACTIVE CASES — EDITION 014

| Case | Title | Tag | Confidence |
|---|---|---|---|
| A | Islamabad Talks — Preconditions vs Talks Proceeding | ESCALATING | MEDIUM |
| B | Hormuz — IRGC Franchise Model Confirmed | ESCALATING | HIGH |
| C | Lebanon / Hezbollah — Active Conflict Zone | ESCALATING | HIGH |
| D | Abqaiq / Saudi Energy Infrastructure | ESCALATING | HIGH |
| E | Mojtaba Khamenei — Iran Won Declaration | NEW | LOW-MEDIUM |
| F | India Oil Waiver — 19 April Expiry | DEVELOPING | MEDIUM |

---

## PREDICTION LOG — OPEN PREDICTIONS ONLY

| Ref | Flag | Window | Status |
|---|---|---|---|
| PRED-001-A | Futures volume anomaly / BETS OFF Act / Section 122 CIT | CIT proceedings ongoing | PENDING |
| PRED-002-B | Iran-Oman Hormuz protocol into ceasefire language | Monitor Islamabad | WATCH |
| PRED-003-A | Araghchi 10-point plan / Islamabad window | Islamabad 10 April | ELEVATED |
| PRED-005-A | Section 122 CIT oral arguments | No date confirmed | PENDING |
| PRED-006-A | GCC emergency meeting post-UNSC veto | Post-ceasefire | WATCH |
| PRED-008-B | Houthi BAM threat not activated | Monitor | DE-ESCALATING |
| PRED-008-D | India oil waiver expires 19 April | 19 April 2026 | WATCH |
| PRED-014-A | Islamabad produces ceasefire extension only — no binding framework | Islamabad session 10 April | PENDING |

---

## LAST PMM

| Field | Detail |
|---|---|
| PMM Ref | PRED-012-B |
| Outcome | CONTRADICTED |
| Heuristic | H1 — Incentive Mismatch |
| Rule Change | Named-party statement predictions require written incentive analysis before C3 satisfied. Confidence ceiling LOW-MEDIUM if no structural incentive exists. |
| In Force | Edition 014 |
| Logged | SYSTEM_CHANGE_LOG.md Entry 001 |

---

## SYSTEM CHANGE LOG — ACTIVE RULES

| Entry | Rule | In Force From |
|---|---|---|
| 001 | Named-party statement predictions require incentive analysis before C3 satisfied. No structural incentive = confidence ceiling LOW-MEDIUM. | Edition 014 |

---

## ARCHITECTURE PATCHES — v1.2.0
All four patches applied. Summary:
- C3 updated: silence, partial compliance, strategic ambiguity must be pre-assigned before window opens
- Bypass Override Protocol added: Tier 1/2 fact resets ceiling for that case only
- status_history added to prediction log schema
- SYSTEM_CHANGE_LOG.md created and referenced in Section 17

---

## OPEN BUILD TASKS
- [ ] Refactor build_master.py into build_core.py / build_edition.py / styles.py
- [ ] Create SOURCE_REGISTRY.json
- [ ] Create CHANGELOG.md
- [ ] Create README.md
- [ ] Commit all v1.2.0 files to GitHub
- [ ] Backfill status_history for Editions 001-012 when log data available

---

## SESSION INSTRUCTIONS FOR CLAUDE
- Do not re-explain the platform — treat this state file as ground truth
- Architecture version is v1.2.0 — apply all rules at that version
- PMM rule from Entry 001 is active — apply to all new predictions
- If asked to build an edition: fetch all 18 feeds, run full CDIT, build PDF via ReportLab
- If asked to patch architecture: update this SESSION_STATE.md to reflect changes
- If asked to commit to GitHub: flag that Claude Code is required for that step
