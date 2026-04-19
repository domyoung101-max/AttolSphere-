import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
)
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_CENTER

from styles import (
    make_styles,
    NAVY,
    TEAL,
    CHARCOAL,
    MID_GREY,
    LIGHT_BG,
    ROW_ALT,
    WHITE,
    RED_TAG,
    AMBER,
    GREEN_TAG,
    PURPLE,
    DK_GREEN,
    MARGIN,
    PAGE_W,
    PAGE_H,
)

from build_core import (
    hr,
    thin_rule,
    tag_table,
    fact_table,
    hyp_table,
    disconf_table,
    flag_block,
    source_block,
    make_page_callbacks,
)

EDITION = "029"
DATE_STR = "19 APRIL 2026"
SWEEP_STR = "AFTERNOON SWEEP"

GMT_NOW = datetime.datetime(2026, 4, 19, 14, 55, 0)
BST_NOW = GMT_NOW + datetime.timedelta(hours=1)
GMT_STR = GMT_NOW.strftime("%d %B %Y · %H:%M GMT")
BST_STR = BST_NOW.strftime("%H:%M BST")


def build():
    path = f"/mnt/user-data/outputs/atollsphere_edition_{EDITION}_afternoon_sweep.pdf"

    doc = SimpleDocTemplate(
        path,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=18 * mm,
        bottomMargin=14 * mm,
    )

    styles = make_styles()
    story = []
    on_cover, on_page = make_page_callbacks(EDITION, SWEEP_STR, DATE_STR)

    # COVER
    story.append(Spacer(1, 28 * mm))

    stats = Table(
        [
            [
                Paragraph("EDITION", styles["cover_label"]),
                Paragraph("DATE", styles["cover_label"]),
                Paragraph("SWEEP", styles["cover_label"]),
                Paragraph("DAY", styles["cover_label"]),
                Paragraph("STATUS", styles["cover_label"]),
            ],
            [
                Paragraph(EDITION, styles["cover_value"]),
                Paragraph(DATE_STR, styles["cover_value"]),
                Paragraph(SWEEP_STR, styles["cover_value"]),
                Paragraph("WAR DAY 52", styles["cover_value"]),
                Paragraph("ESCALATING", styles["cover_value"]),
            ],
        ],
        colWidths=[35 * mm] * 5,
    )

    stats.setStyle(
        TableStyle(
            [
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("LINEABOVE", (0, 0), (-1, 0), 0.5, TEAL),
                ("LINEBELOW", (0, -1), (-1, -1), 0.5, TEAL),
            ]
        )
    )
    story.append(stats)
    story.append(Spacer(1, 10 * mm))

    story.append(
        Paragraph(
            "Second Round Still Unscheduled. Lebanon 72-Hour Window Holds. GL U Lapse Confirmed.",
            styles["cover_title"],
        )
    )
    story.append(Spacer(1, 8 * mm))

    counts = Table(
        [
            [
                Paragraph(
                    "<b>5</b><br/><font size=7>CASES</font>",
                    ParagraphStyle(
                        "cnt",
                        fontName="Helvetica-Bold",
                        fontSize=20,
                        textColor=NAVY,
                        alignment=TA_CENTER,
                    ),
                ),
                Paragraph(
                    "<b>3</b><br/><font size=7>ESCALATING</font>",
                    ParagraphStyle(
                        "cnt2",
                        fontName="Helvetica-Bold",
                        fontSize=20,
                        textColor=RED_TAG,
                        alignment=TA_CENTER,
                    ),
                ),
                Paragraph(
                    "<b>2</b><br/><font size=7>CONFIRMED THIS CYCLE</font>",
                    ParagraphStyle(
                        "cnt3",
                        fontName="Helvetica-Bold",
                        fontSize=20,
                        textColor=AMBER,
                        alignment=TA_CENTER,
                    ),
                ),
                Paragraph(
                    "<b>4</b><br/><font size=7>LIVE WINDOWS</font>",
                    ParagraphStyle(
                        "cnt4",
                        fontName="Helvetica-Bold",
                        fontSize=20,
                        textColor=TEAL,
                        alignment=TA_CENTER,
                    ),
                ),
            ]
        ],
        colWidths=[43.5 * mm] * 4,
    )

    counts.setStyle(
        TableStyle(
            [
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LINEAFTER", (0, 0), (2, 0), 0.5, colors.HexColor("#D0D8E0")),
            ]
        )
    )
    story.append(counts)
    story.append(PageBreak())

    # SITUATION OVERVIEW
    story.append(Paragraph("SITUATION OVERVIEW", styles["section_head"]))
    story.append(hr())
    story.append(
        Paragraph(
            f"{DATE_STR} · {SWEEP_STR} · {GMT_STR} ({BST_STR})",
            styles["small_bold"],
        )
    )
    story.append(Spacer(1, 2 * mm))
    story.append(
        Paragraph(
            "This build opens from the corrected Ed028 Late Afternoon session baseline. "
            "Case A remains strong but unresolved because no formal second-round announcement naming date, venue, and agenda has appeared. "
            "Case C has moved materially: the Lebanon 72-hour window closed without a major Hezbollah barrage or large-scale Israeli strike, "
            "so the relevant monitoring predictions are now resolved as CONFIRMED.",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "Case D remains operationally settled: GL U is treated as lapsed and confirmed absent at OFAC, with no successor or wind-down instrument carried into this state. "
            "Case B remains fragile rather than resolved because Hormuz narrative signals still exceed hard operational confirmation. "
            "Case E remains open, with no new follow-on IRGC strike on Yanbu or Petroline confirmed in this carried-forward state.",
            styles["body"],
        )
    )

    story.append(Paragraph("PCP STEP 1.5 — NEW SIGNAL CHECK", styles["section_head"]))
    story.append(
        Paragraph(
            "[MANDATORY — AI-003] No new case opened in this build state. "
            "The key developments since the prior baseline fit within existing cases: unresolved second-round diplomacy remains in Case A; "
            "Lebanon ceasefire durability remains in Case C; GL U lapse remains in Case D; Hormuz fragility remains in Case B; "
            "and Yanbu/Petroline follow-on strike risk remains in Case E.",
            styles["body"],
        )
    )

    story.append(Paragraph("H1 SATURATION CHECK — STANDING RULE (AI-003)", styles["section_head"]))
    story.append(
        Paragraph(
            "H1 is not load-bearing in this edition state. "
            "H6 remains primary across the system; H5 remains active in Case A; H4 remains primary in Case B; "
            "and Case C is now governed mainly by ceasefire durability and absence-of-escalation thresholds rather than narrative incentives.",
            styles["body"],
        )
    )

    story.append(Paragraph("AI-007 CALIBRATION MAP — CURRENT GOVERNING BANDS", styles["section_head"]))
    story.append(
        Paragraph(
            "No new raw-to-calibrated correction is introduced inside this draft build. "
            "The governing probabilities are carried from the corrected session baseline and remain subject to live re-verification at sweep execution.",
            styles["body"],
        )
    )

    calib = Table(
        [
            ["Hypothesis", "Current Band", "Status Note"],
            ["H-A1", "72–82%", "NEAR-CONFIRMED (PROVISIONAL); no formal second-round announcement"],
            ["H-C1", "58–70%", "Operational pause / ceasefire durability remains dominant"],
            ["H-C3", "10–18%", "Escalation risk reduced; no major barrage or large-scale strike"],
            ["H-D2", "97–99%", "CONFIRMED; GL U lapse carried forward"],
            ["H-E2", "35–48%", "Open risk; no fresh trigger confirmed in carried state"],
        ],
        colWidths=[28 * mm, 28 * mm, 120 * mm],
    )
    calib.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 7.5),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("LINEBELOW", (0, 1), (-1, -1), 0.3, colors.HexColor("#D0D8E0")),
                ("BACKGROUND", (0, 2), (-1, 2), ROW_ALT),
                ("BACKGROUND", (0, 4), (-1, 4), ROW_ALT),
            ]
        )
    )
    story.append(calib)
    story.append(hr())

    # CLOSED WINDOW CLASSIFICATIONS
    story.append(Paragraph("CLOSED WINDOW CLASSIFICATIONS", styles["section_head"]))
    story.append(
        Paragraph(
            "PRED-026-C / PRED-028-C: CONFIRMED. "
            "The Israel-Lebanon 72-hour monitoring window closed without a major Hezbollah barrage or a large-scale Israeli strike in Lebanon. "
            "Violations remained sub-escalatory within the carried-forward record.",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "PRED-022-C / PRED-023-B / PRED-026-D: CONFIRMED (carry-forward). "
            "GL U remains treated as lapsed, with no successor or wind-down instrument in the governing state baseline.",
            styles["body"],
        )
    )
    story.append(hr())

    # CASE A
    story.append(
        tag_table(
            "A",
            "Second Round / Ceasefire / No Formal Announcement Yet",
            "ESCALATING",
            "HIGH",
            None,
            styles,
        )
    )
    story.append(
        Paragraph(
            "Heuristics: H5 (Structural Contradiction) · H6 (Suppressed Intersection)",
            styles["heuristic_line"],
        )
    )
    story.append(Paragraph("PART 1 — FACTUAL ELEMENTS", styles["section_head"]))
    story.append(
        fact_table(
            [
                (
                    "Pakistan and Iranian officials continued to say that no date had yet been fixed for the second round of US-Iran talks. "
                    "This means expectation remains live, but formal announcement threshold is not met.",
                    "Carry-forward from session baseline; Tier 1/2 sweep summary. [FACT]",
                ),
                (
                    "White House and Trump signalling remained supportive of a likely second round, but the governing state explicitly treats this as expectation rather than formal confirmation.",
                    "Carry-forward from session baseline. Incentive distortion noted. [FACT]",
                ),
                (
                    "No formal instrument extending the ceasefire had been published in the governing state.",
                    "Carry-forward from session baseline. [FACT]",
                ),
            ],
            styles,
        )
    )

    story.append(Paragraph("PART 2 — OBSERVED INCONGRUITY", styles["section_head"]))
    story.append(
        Paragraph(
            "FACT: Momentum toward a second round is real, but the formal threshold remains unmet. "
            "This creates a calibration problem: rhetorical momentum is high, evidentiary closure is not.",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "INFERENCE: H5 remains primary because the structural contradiction between red lines is unresolved. "
            "H6 remains active because the same unresolved diplomatic state interacts with Hormuz, GL U, and Yanbu risk.",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "AFC: The strongest steelman for H-A1 is that the parties still appear to want a second round before the ceasefire forcing function expires.",
            styles["afc_note"],
        )
    )
    story.append(
        Paragraph(
            "INFERENCE: H1 is not load-bearing here; H5 and H6 remain the real explanatory frame.",
            styles["infer"],
        )
    )
    story.append(
        Paragraph(
            "Domain quality: strong enough to sustain a high provisional band, but not strong enough to permit formal confirmation.",
            styles["small"],
        )
    )

    story.append(Paragraph("PART 3 — HYPOTHESIS SET", styles["section_head"]))
    story.append(
        hyp_table(
            [
                {
                    "heading": "H-A1: SECOND ROUND HELD BEFORE 22 APRIL — NEAR-CONFIRMED (PROVISIONAL)",
                    "probability_range": "72–82%",
                    "body": "Strong expectation remains, but no formal date/venue/agenda announcement has yet appeared in the governing state.",
                },
                {
                    "heading": "H-A2: TALKS FAIL / CEASEFIRE LAPSES",
                    "probability_range": "5–10%",
                    "body": "Breakdown risk remains present through unresolved enrichment and sanctions contradictions, but no fresh breakdown trigger has overtaken H-A1.",
                },
                {
                    "heading": "H-A3: CEASEFIRE FORMALLY EXTENDED",
                    "probability_range": "45–60%",
                    "body": "Possible, but still provisional because no formal extension instrument is present.",
                },
            ],
            styles,
        )
    )

    story.append(Paragraph("PART 4 — TRUTH QUALITY CHECK", styles["section_head"]))
    story.append(
        Paragraph(
            "1. Key assumption: The diplomatic momentum reflected in official signalling still corresponds to a real path toward a second round rather than narrative management alone.",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "2. Fragile fact: The absence of a formal second-round announcement is decisive; if a named date, venue, and agenda were published, H-A1 would move materially higher.",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "3. High-impact uncertainty: Whether a formal second-round announcement appears before the ceasefire deadline.",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "4. Tier 4 dependency test: YES — the dominant hypothesis still holds without Tier 4 support because the probability is sustained by carry-forward Tier 1/2 reporting and formal-threshold logic.",
            styles["body"],
        )
    )

    story.append(Paragraph("PART 5 — DISCONFIRMATION", styles["section_head"]))
    story.append(
        disconf_table(
            [
                ("Formal second-round announcement with date, venue, and agenda", "Ceasefire lapses without round or extension"),
                ("Second round actually begins before 22 April", "Iran formally exits the process"),
                ("Formal extension instrument published", "Escalatory trigger overtakes diplomacy"),
            ],
            "Gate 5 trigger: formal diplomatic collapse or ceasefire lapse without extension requires full Case A reframe.",
            styles,
        )
    )

    story.extend(
        flag_block(
            "PRED-029-A",
            1,
            "Monitor whether a formal second-round announcement appears before ceasefire expiry. "
            "Five-state outcome remains tied to named date, venue, and agenda — not expectation alone.",
            "Formal named announcement = CONFIRMED. No announcement by lapse = CONTRADICTED or overtaken by ceasefire outcome.",
            styles,
        )
    )
    story.append(hr())

    # CASE B
    story.append(
        tag_table(
            "B",
            "Hormuz — Conditional Opening / Fragility Still Active",
            "ESCALATING",
            "MEDIUM",
            None,
            styles,
        )
    )
    story.append(
        Paragraph(
            "Case B remains open and fragile. Narrative movement toward selective opening exists, but sustained transit and governance confirmation remain incomplete.",
            styles["body"],
        )
    )
    story.append(hr())

    # CASE C
    story.append(
        tag_table(
            "C",
            "Lebanon — 10-Day Ceasefire Holding / 72-Hour Window Closed",
            "STABLE",
            "MEDIUM",
            None,
            styles,
        )
    )
    story.append(
        Paragraph(
            "Heuristics: H3 (Beneficiary Asymmetry) · H5 (Structural Contradiction)",
            styles["heuristic_line"],
        )
    )
    story.append(Paragraph("PART 1 — FACTUAL ELEMENTS", styles["section_head"]))
    story.append(
        fact_table(
            [
                (
                    "The 10-day Israel-Lebanon ceasefire remained in force in the governing state, with violations described as sub-escalatory rather than framework-breaking.",
                    "Carry-forward baseline. [FACT]",
                ),
                (
                    "The 72-hour monitoring window closed without a major Hezbollah barrage or a large-scale Israeli strike in Lebanon.",
                    "Prediction resolution basis in updated session baseline. [FACT]",
                ),
                (
                    "Trump's PROHIBITED signal remained part of the suppressor logic in the current state, though sustainability still requires monitoring.",
                    "Carry-forward baseline. [FACT]",
                ),
            ],
            styles,
        )
    )

    story.append(Paragraph("PART 2 — OBSERVED INCONGRUITY", styles["section_head"]))
    story.append(
        Paragraph(
            "FACT: The framework held through the first major monitoring window, but only with sub-escalatory violations still present.",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "INFERENCE: H-C1 now has the stronger position because operational pause is not total peace, but enough suppression exists to keep collapse risk lower.",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "AFC: The strongest case against H-C1 is that ceasefire text and political pressure can still unravel quickly if either side escalates beyond current violation levels.",
            styles["afc_note"],
        )
    )
    story.append(
        Paragraph(
            "INFERENCE: H1 is not primary here; the actual question is whether operational suppression survives repeated violations.",
            styles["infer"],
        )
    )
    story.append(
        Paragraph(
            "Domain quality: sufficient to classify the 72-hour window as passed, but not sufficient to treat the theatre as settled.",
            styles["small"],
        )
    )

    story.append(Paragraph("PART 3 — HYPOTHESIS SET", styles["section_head"]))
    story.append(
        hyp_table(
            [
                {
                    "heading": "H-C1: FRAMEWORK LEADS TO OPERATIONAL PAUSE",
                    "probability_range": "58–70%",
                    "body": "The ceasefire framework continues to suppress major escalation despite violations.",
                },
                {
                    "heading": "H-C2: FRAMEWORK WITHOUT FULL OPERATIONAL IMPACT",
                    "probability_range": "15–22%",
                    "body": "The framework survives, but military posture and local pressure continue to limit real de-escalation.",
                },
                {
                    "heading": "H-C3: HEZBOLLAH ESCALATION / FRAMEWORK COLLAPSE",
                    "probability_range": "10–18%",
                    "body": "Still live, but lowered because the first key window passed without major escalation.",
                },
            ],
            styles,
        )
    )

    story.append(Paragraph("PART 4 — TRUTH QUALITY CHECK", styles["section_head"]))
    story.append(
        Paragraph(
            "1. Key assumption: Sub-escalatory violations remain bounded and do not convert into a major barrage or large-scale strike.",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "2. Fragile fact: The classification depends on the absence of a qualifying major violation during the 72-hour window.",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "3. High-impact uncertainty: Whether Trump's prohibition signal remains politically binding if Netanyahu pressure intensifies.",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "4. Tier 4 dependency test: YES — the dominant hypothesis survives without Tier 4 because the key logic is the absence of major escalation and the carried ceasefire state.",
            styles["body"],
        )
    )

    story.append(Paragraph("PART 5 — DISCONFIRMATION", styles["section_head"]))
    story.append(
        disconf_table(
            [
                ("Ceasefire continues with only bounded violations", "Major Hezbollah barrage into Israel"),
                ("No large-scale Israeli strike in Lebanon", "Large-scale Israeli strike breaks framework"),
                ("Trump prohibition signal remains operative", "Explicit reversal of the prohibition signal"),
            ],
            "Gate 5 trigger: major barrage or large-scale strike requires full Case C reframe.",
            styles,
        )
    )

    story.extend(
        flag_block(
            "PRED-029-C",
            2,
            "Monitor whether the ceasefire remains in force beyond the initial 72-hour success window. "
            "Any major barrage or large-scale strike would reset the framework immediately.",
            "Major escalation = CONFIRMED collapse pathway. Continued bounded violations = carry H-C1.",
            styles,
        )
    )
    story.append(hr())

    # CASE D
    story.append(
        tag_table(
            "D",
            "India Oil Waiver — GL U Lapsed",
            "RESOLVED",
            "HIGH",
            None,
            styles,
        )
    )
    story.append(
        Paragraph(
            "H-D2 remains CONFIRMED in the governing state: GL U lapsed, with no successor or wind-down instrument carried in the baseline.",
            styles["body"],
        )
    )
    story.append(hr())

    # CASE E
    story.append(
        tag_table(
            "E",
            "Saudi Aramco / Yanbu — Follow-On Strike Risk Open",
            "ESCALATING",
            "MEDIUM",
            None,
            styles,
        )
    )
    story.append(
        Paragraph(
            "No new confirmed follow-on IRGC strike on Yanbu or Petroline is carried in this baseline. "
            "Risk remains open, but not newly resolved in this draft build state.",
            styles["body"],
        )
    )
    story.append(hr())

    # PRIORITIES
    story.append(Paragraph("CRITICAL WINDOWS / NEXT PRIORITIES", styles["section_head"]))
    story.append(
        Paragraph(
            "1. Formal second-round announcement check. "
            "2. Lebanon ceasefire durability beyond the first 72 hours. "
            "3. Hormuz AIS verification and SNSC confirmation. "
            "4. Any IRGC kinetic response to USN. "
            "5. Any IRGC follow-on strike on Yanbu/Petroline.",
            styles["body"],
        )
    )

    # SOURCES
    story.append(Paragraph("SOURCES", styles["section_head"]))
    story.extend(
        source_block(
            [
                {
                    "name": "SESSION_STATE-3-2.md",
                    "tier": "CANONICAL",
                    "category": "Active continuity baseline",
                    "body": "Current governing case state, calibration map, mandatory sweep actions, and prediction status for Ed029 opening.",
                },
                {
                    "name": "ARCHITECTURE.md v1.2.1",
                    "tier": "CANONICAL",
                    "category": "Constitutional rules",
                    "body": "Build rules, case structure, CDIT gates, prediction standards, calibration doctrine integration, and PDF sequence requirements.",
                },
                {
                    "name": "styles.py",
                    "tier": "IMPLEMENTATION",
                    "category": "Visual style baseline",
                    "body": "Colour constants and paragraph style factory used by the per-edition script.",
                },
                {
                    "name": "build_core.py",
                    "tier": "IMPLEMENTATION",
                    "category": "Layout helper baseline",
                    "body": "Reusable ReportLab table builders, flag blocks, source blocks, and page callback helpers.",
                },
            ],
            styles,
        )
    )

    story.append(Spacer(1, 4 * mm))
    story.append(
        Paragraph(
            f"AtollSphere Brief Edition {EDITION} · {SWEEP_STR} · {DATE_STR} · build_edition_029.py",
            styles["footer"],
        )
    )

    doc.build(story, onFirstPage=on_cover, onLaterPages=on_page)
    print(f"Built {path}")


if __name__ == "__main__":
    build()
