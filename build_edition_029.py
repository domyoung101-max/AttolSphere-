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


def tql_block(item1, item2, item3, item4, styles):
    return [
        Paragraph("PART 4 — TRUTH QUALITY CHECK", styles["section_head"]),
        Paragraph(f"1. Key assumption: {item1}", styles["body"]),
        Paragraph(f"2. Fragile fact: {item2}", styles["body"]),
        Paragraph(f"3. High-impact uncertainty: {item3}", styles["body"]),
        Paragraph(f"4. Tier 4 dependency test: {item4}", styles["body"]),
    ]


def add_case(
    story,
    case_letter,
    title,
    tag,
    confidence,
    heuristics,
    facts,
    incongruity_paras,
    hypotheses,
    tql_items,
    disconf_rows,
    gate5_note,
    flag_ref,
    flag_number,
    flag_body,
    flag_gate_note,
    styles,
):
    story.append(tag_table(case_letter, title, tag, confidence, None, styles))
    story.append(Paragraph(f"Heuristics: {heuristics}", styles["heuristic_line"]))

    story.append(Paragraph("PART 1 — FACT TABLE", styles["section_head"]))
    story.append(fact_table(facts, styles))

    story.append(Paragraph("PART 2 — INCONGRUITY ANALYSIS", styles["section_head"]))
    for text, style_name in incongruity_paras:
        story.append(Paragraph(text, styles[style_name]))

    story.append(Paragraph("PART 3 — HYPOTHESIS SET", styles["section_head"]))
    story.append(hyp_table(hypotheses, styles))

    story.extend(tql_block(*tql_items, styles))

    story.append(Paragraph("PART 5 — DISCONFIRMATION", styles["section_head"]))
    story.append(disconf_table(disconf_rows, gate5_note, styles))
    story.append(Paragraph(gate5_note, styles["pred_note"]))

    story.extend(
        flag_block(
            flag_ref,
            flag_number,
            flag_body,
            flag_gate_note,
            styles,
        )
    )
    story.append(hr())


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
            "Second Round Still Unscheduled. Lebanon 72-Hour Window Closing. GL U Lapse Confirmed.",
            styles["cover_title"],
        )
    )
    story.append(
        Paragraph(
            "Edition 029 build state from corrected Ed028 Late Afternoon baseline.",
            styles["cover_sub"],
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
                    "<b>4</b><br/><font size=7>ESCALATING</font>",
                    ParagraphStyle(
                        "cnt2",
                        fontName="Helvetica-Bold",
                        fontSize=20,
                        textColor=RED_TAG,
                        alignment=TA_CENTER,
                    ),
                ),
                Paragraph(
                    "<b>2</b><br/><font size=7>CONFIRMED CARRIES</font>",
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
            "Case A remains strong but unresolved because no formal second-round announcement naming date, venue, and agenda had been confirmed in the governing state. "
            "Case B remains fragile because Hormuz opening narrative still outruns sustained transit confirmation and SNSC formalisation.",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "Case C remains materially improved but not settled: the 72-hour Lebanon monitoring window was the critical near-term suppressor, "
            "with no major Hezbollah barrage or large-scale Israeli strike present in the carried-forward baseline. "
            "Case D remains formally settled in the opposite direction: GL U lapse is treated as confirmed and H-D2 remains the dominant resolved state.",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "Case E remains open after the earlier Yanbu/Petroline strike cycle because reversion triggers from GL U lapse are active, "
            "while no fresh follow-on IRGC strike has yet been confirmed in the governing baseline. "
            "The architecture therefore still requires full five-case treatment rather than short-form compression.",
            styles["body"],
        )
    )

    story.append(Paragraph("PCP STEP 1.5 — NEW SIGNAL CHECK", styles["section_head"]))
    story.append(
        Paragraph(
            "[MANDATORY — AI-003] No new case is opened in this draft build state. "
            "All material developments remain absorbable inside the existing five-case frame: second-round diplomacy in Case A, Hormuz opening fragility and multilateral maritime response in Case B, "
            "Lebanon ceasefire durability in Case C, GL U lapse in Case D, and Yanbu/Petroline follow-on strike risk in Case E.",
            styles["body"],
        )
    )

    story.append(Paragraph("H1 SATURATION CHECK — STANDING RULE", styles["section_head"]))
    story.append(
        Paragraph(
            "H1 is not the load-bearing explanatory frame in this edition state. "
            "H5 remains primary in Case A, H4 and H5 remain central in Case B, H3 and H5 dominate Case C, "
            "formal instrument logic dominates Case D, and reversion-trigger plus escalation-chain logic dominates Case E.",
            styles["body"],
        )
    )

    story.append(Paragraph("AI-007 CALIBRATION MAP — EDITION CORRECTIONS", styles["section_head"]))
    story.append(
        Paragraph(
            "No fresh raw-to-calibrated correction is introduced inside this build draft. "
            "The current governing bands are carried from the Ed028 Late Afternoon calibration map and remain provisional until live Ed029 sweep verification is completed.",
            styles["body"],
        )
    )

    calib = Table(
        [
            ["Hypothesis", "Raw / Prior Frame", "Current Calibrated Band", "Correction Basis"],
            ["H-A1", "Ed028 carry", "72–82%", "No formal second-round announcement; near-confirmed remains provisional."],
            ["H-B3", "Raw 28–36%", "26–34% PARTIAL", "Paris Summit / GOV.UK Joint Statement confirms initiative, not deployment."],
            ["H-C1", "Raw 60–72%", "58–70%", "Trump PROHIBITED signal and absent Gate 0.3 collapse triggers."],
            ["H-C3", "Raw 12–20%", "10–18%", "Reduced by suppressor logic and absent barrage / strike trigger."],
            ["H-D2", "Direct formal evidence", "97–99% CONFIRMED", "Two OFAC fetches with no GL U, GL 134B, or wind-down instrument."],
            ["H-E2", "Ed028 carry", "35–48%", "GL U reversion active; no new strike yet; Lebanon partial suppressor."],
        ],
        colWidths=[24 * mm, 32 * mm, 34 * mm, 90 * mm],
    )
    calib.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 7),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("LINEBELOW", (0, 1), (-1, -1), 0.3, colors.HexColor("#D0D8E0")),
                ("BACKGROUND", (0, 2), (-1, 2), ROW_ALT),
                ("BACKGROUND", (0, 4), (-1, 4), ROW_ALT),
                ("BACKGROUND", (0, 6), (-1, 6), ROW_ALT),
            ]
        )
    )
    story.append(calib)
    story.append(
        Paragraph(
            "Band governance note: H-D2 is the only hypothesis above 85% and is justified by explicit formal evidence in the governing state: two independent OFAC fetches confirming GL U lapse conditions.",
            styles["pred_note"],
        )
    )
    story.append(hr())

    # CLOSED WINDOW CLASSIFICATIONS / PREDICTION RESOLUTIONS
    story.append(Paragraph("CLOSED WINDOW CLASSIFICATIONS / PREDICTION RESOLUTIONS", styles["section_head"]))
    story.append(
        Paragraph(
            "PRED-022-C / PRED-023-B / PRED-026-D remain CONFIRMED in carry-forward state. "
            "The governing baseline treats GL U as lapsed with no successor or wind-down instrument.",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "Lebanon 72-hour logic remains the critical threshold in this build state, but this draft keeps the classification in the carried-forward architecture rather than inventing a new unsupported closure event beyond the governing baseline.",
            styles["body"],
        )
    )
    story.append(hr())

    # CASE A
    add_case(
        story=story,
        case_letter="A",
        title="Second Round / Ceasefire / No Formal Announcement Yet",
        tag="ESCALATING",
        confidence="HIGH",
        heuristics="H5 (Structural Contradiction) · H6 (Suppressed Intersection)",
        facts=[
            (
                "Pakistan and Iranian officials continued to indicate that no formal date had yet been fixed for a second round of US-Iran talks. [FACT]",
                "Carry-forward session baseline; Tier 1/2 summary — GATE 0.",
            ),
            (
                "White House and Trump signalling remained supportive of a likely second round, but the governing state treats this as expectation rather than formal confirmation. [FACT]",
                "Carry-forward session baseline; incentive distortion noted — GATE 0.",
            ),
            (
                "No formal ceasefire extension instrument had been published in the governing state baseline. [FACT]",
                "Carry-forward session baseline — GATE 0.",
            ),
        ],
        incongruity_paras=[
            (
                "[FACT] Momentum toward a second round is real, but the formal threshold remains unmet. Narrative expectation is therefore higher than evidentiary closure.",
                "body",
            ),
            (
                "[INFERENCE] H5 remains primary because the enrichment and sanctions contradiction has not been structurally resolved. H6 remains active because this diplomatic branch intersects directly with Hormuz, GL U, and Yanbu risk.",
                "body",
            ),
            (
                "AFC steelman: the strongest case for H-A1 is that all principal actors still appear to prefer a second round before the ceasefire forcing function expires.",
                "afc_note",
            ),
            (
                "[INFERENCE] H1 is not load-bearing in this case; structural contradiction and cross-case dependency remain the governing explanatory frame.",
                "infer",
            ),
        ],
        hypotheses=[
            {
                "heading": "H-A1: SECOND ROUND HELD BEFORE 22 APRIL — NEAR-CONFIRMED (PROVISIONAL)",
                "probability_range": "72–82%",
                "body": "Strong expectation persists, but no formal named date, venue, and agenda threshold has yet been satisfied in the governing state.",
            },
            {
                "heading": "H-A2: TALKS FAIL / CEASEFIRE LAPSES",
                "probability_range": "5–10%",
                "body": "Breakdown risk remains real through unresolved enrichment and sanctions contradictions, but no fresh dominant trigger has displaced H-A1.",
            },
            {
                "heading": "H-A3: CEASEFIRE FORMALLY EXTENDED",
                "probability_range": "45–60%",
                "body": "Possible but still provisional because no signed public extension instrument is present in the carried-forward state.",
            },
        ],
        tql_items=(
            "Diplomatic signalling still maps to a real second-round path rather than narrative management alone.",
            "The absence of a formal second-round announcement remains the decisive limiting fact.",
            "Whether a named second-round announcement appears before the ceasefire forcing function bites.",
            "YES — the dominant hypothesis can still stand without Tier 4 support because formal-threshold logic and carried Tier 1/2 reporting are sufficient.",
        ),
        disconf_rows=[
            ("Formal second-round announcement with date, venue, and agenda", "Ceasefire lapses without round or extension"),
            ("Second round actually begins before 22 April", "Iran formally exits the process"),
            ("Formal extension instrument published", "Escalatory trigger overtakes diplomacy"),
        ],
        gate5_note="Gate 5 trigger: formal diplomatic collapse or ceasefire lapse without extension requires full Case A reframe.",
        flag_ref="PRED-029-A",
        flag_number=1,
        flag_body=(
            "Monitor whether a formal second-round announcement appears before ceasefire expiry. "
            "Five-state resolution remains tied to named date, venue, and agenda rather than expectation alone."
        ),
        flag_gate_note="Formal named announcement = CONFIRMED. No announcement by lapse = CONTRADICTED or overtaken by ceasefire outcome.",
        styles=styles,
    )

    # CASE B
    add_case(
        story=story,
        case_letter="B",
        title="Hormuz — Conditional Opening / Paris Summit / AIS Fragility",
        tag="ESCALATING",
        confidence="HIGH",
        heuristics="H4 (Operational-Evidence Gap) · H5 (Structural Contradiction)",
        facts=[
            (
                "Araghchi announced Hormuz as 'completely open' in the prior state, but the same baseline records AIS traffic still below 10% of pre-crisis norms. [FACT]",
                "Carry-forward session baseline; Tier 1 plus directional Tier 4 aggregation — GATE 0 / 0.5.",
            ),
            (
                "USN blockade pressure remained active while SNSC formal confirmation remained absent in the governing state. [FACT]",
                "Carry-forward session baseline — GATE 0.",
            ),
            (
                "The 51-nation Paris Summit / GOV.UK Joint Statement formally launched a Hormuz maritime initiative and confirmed Northwood planning for next week. [FACT]",
                "Carry-forward session baseline; GOV.UK Tier 1 — GATE 0.",
            ),
        ],
        incongruity_paras=[
            (
                "[FACT] The narrative says opening; the operational picture says fragility. Formal initiative-building has advanced faster than verified normalisation of transit.",
                "body",
            ),
            (
                "[INFERENCE] H4 is primary because operational confirmation lags rhetoric. H5 remains active because Araghchi's opening claim, Ghalibaf's closure threat, and active US pressure do not sit cleanly together.",
                "body",
            ),
            (
                "AFC steelman: the best case for H-B1 is that selective, coordinated opening is real but highly throttled, which explains both rhetorical openness and low traffic.",
                "afc_note",
            ),
            (
                "[INFERENCE] H1 is not explanatory here; the key issue is the gap between declared openness and verified maritime normalisation.",
                "infer",
            ),
        ],
        hypotheses=[
            {
                "heading": "H-B1: HORMUZ CONDITIONALLY OPEN / SUSTAINABILITY UNVERIFIED",
                "probability_range": "55–70%",
                "body": "The strait may be functionally selective rather than fully normalised; transit is possible in principle but still constrained in practice.",
            },
            {
                "heading": "H-B2: IRGC KINETIC RESPONSE TO USN",
                "probability_range": "10–20%",
                "body": "Still a live branch, but suppressors remain active and no fresh dominant trigger has broken above baseline.",
            },
            {
                "heading": "H-B3: MULTILATERAL MARITIME MISSION COMMITS FORCE STRUCTURE",
                "probability_range": "26–34% PARTIAL",
                "body": "The initiative is formally launched and Northwood planning is confirmed, but deployment structure remains incomplete.",
            },
        ],
        tql_items=(
            "Selective opening can exist without visible traffic recovery approaching pre-crisis norms.",
            "AIS weakness remains the central fragile fact because it blocks any clean claim of sustained reopening.",
            "Whether SNSC, independent media verification, or verified traffic recovery removes the fragility gap.",
            "YES — but only partially; the dominant reading still depends primarily on formal and operational indicators above Tier 4 rhetoric.",
        ),
        disconf_rows=[
            ("Sustained verified transit recovery", "AIS remains near-crisis floor"),
            ("SNSC or equivalent formal confirmation", "SNSC reversal or closure order"),
            ("Northwood planning converts into named operational schedule", "Initiative remains declaratory without force structure"),
        ],
        gate5_note="Gate 5 trigger: SNSC reversal, verified closure, or IRGC-USN kinetic engagement requires full Case B reframe.",
        flag_ref="PRED-029-B",
        flag_number=2,
        flag_body=(
            "Monitor Hormuz AIS recovery, SNSC formal status, and whether the Paris Summit initiative gains concrete operational structure. "
            "The central issue is not rhetoric alone but whether verified maritime behaviour changes."
        ),
        flag_gate_note="Verified sustained transit + formal confirmation = strengthens H-B1/H-B3. SNSC reversal or kinetic escalation = collapse of current frame.",
        styles=styles,
    )

    # CASE C
    add_case(
        story=story,
        case_letter="C",
        title="Lebanon — 10-Day Ceasefire / Trump Prohibition / Fragile Suppression",
        tag="ELEVATED",
        confidence="HIGH",
        heuristics="H3 (Beneficiary Asymmetry) · H5 (Structural Contradiction)",
        facts=[
            (
                "A 10-day Israel-Lebanon ceasefire was in force in the governing state, but violations were described as sub-escalatory rather than framework-breaking. [FACT]",
                "Carry-forward session baseline — GATE 0.",
            ),
            (
                "Trump's PROHIBITED signal entered the governing state as a suppressor on major Israeli offensive action. [FACT]",
                "Carry-forward session baseline — GATE 0.",
            ),
            (
                "No major Hezbollah barrage and no large-scale Israeli strike in Lebanon had been confirmed in the governing state at the relevant threshold. [FACT]",
                "Carry-forward session baseline; Gate 0.3 absent — GATE 0.",
            ),
        ],
        incongruity_paras=[
            (
                "[FACT] The framework is holding, but not cleanly. Violations remain present while collapse triggers remain absent.",
                "body",
            ),
            (
                "[INFERENCE] H-C1 leads because bounded violations plus political suppression are still enough to keep major collapse risk below the dominant band. H-C3 survives because the theatre is not settled.",
                "body",
            ),
            (
                "AFC steelman: the strongest case against H-C1 is that repeated sub-escalatory violations can still become a sudden major barrage or strike once suppressors weaken.",
                "afc_note",
            ),
            (
                "[INFERENCE] H1 is not primary here. The decisive question is whether suppression remains operationally durable under repeated stress.",
                "infer",
            ),
        ],
        hypotheses=[
            {
                "heading": "H-C1: FRAMEWORK LEADS TO OPERATIONAL PAUSE",
                "probability_range": "58–70%",
                "body": "The ceasefire framework continues to suppress major escalation despite bounded violations and continuing tension.",
            },
            {
                "heading": "H-C2: FRAMEWORK WITHOUT FULL OPERATIONAL IMPACT",
                "probability_range": "15–22%",
                "body": "The framework persists but military posture and local pressure prevent a full operational de-escalation effect.",
            },
            {
                "heading": "H-C3: HEZBOLLAH ESCALATION / FRAMEWORK COLLAPSE",
                "probability_range": "10–18%",
                "body": "Still live, but reduced because the major collapse threshold had not been crossed in the carried-forward baseline.",
            },
        ],
        tql_items=(
            "Sub-escalatory violations remain bounded and do not convert into major exchange.",
            "The absence of a qualifying barrage or large-scale strike is the key fragile fact.",
            "Whether Trump's prohibition effect remains durable under counter-pressure and battlefield friction.",
            "YES — the dominant hypothesis survives without Tier 4 support because the decisive logic is absence of collapse triggers plus carried suppressor structure.",
        ),
        disconf_rows=[
            ("Ceasefire continues with bounded violations", "Major Hezbollah barrage into Israel"),
            ("No large-scale Israeli strike in Lebanon", "Large-scale Israeli strike breaks framework"),
            ("Trump prohibition logic remains operative", "Explicit reversal of the prohibition signal"),
        ],
        gate5_note="Gate 5 trigger: major barrage or large-scale strike requires full Case C reframe.",
        flag_ref="PRED-029-C",
        flag_number=3,
        flag_body=(
            "Monitor whether the Lebanon framework remains intact beyond the initial suppressor window. "
            "Any major barrage or large-scale strike resets the case immediately."
        ),
        flag_gate_note="Major escalation = CONFIRMED collapse pathway. Continued bounded violations = carry H-C1.",
        styles=styles,
    )

    # CASE D
    add_case(
        story=story,
        case_letter="D",
        title="India Oil Waiver — GL U Confirmed Lapsed",
        tag="ESCALATING",
        confidence="HIGH",
        heuristics="Formal-Instrument Logic · H6 (Cross-Case Reversion Impact)",
        facts=[
            (
                "Two independent OFAC fetches in the governing state found no GL U, no GL 134B, and no wind-down instrument. [FACT]",
                "Carry-forward session baseline; direct OFAC evidence — GATE 0.",
            ),
            (
                "H-D2 is marked CONFIRMED and H-D1 is marked CONTRADICTED in the governing state. [FACT]",
                "Carry-forward session baseline — GATE 0.",
            ),
            (
                "GL U lapse activates reversion triggers affecting Case E and wider sanctions exposure logic. [FACT]",
                "Carry-forward session baseline — GATE 0.",
            ),
        ],
        incongruity_paras=[
            (
                "[FACT] This case is analytically asymmetric because the evidentiary burden is now overwhelmingly formal rather than inferential.",
                "body",
            ),
            (
                "[INFERENCE] The main remaining work is not to debate whether GL U lapsed, but to assess downstream system effects: India sourcing adjustments, sanctions exposure, and reversion into Case E escalation logic.",
                "body",
            ),
            (
                "AFC steelman: the only meaningful residual counter-case would be a retroactive or successor instrument emerging after the OFAC checks, but the governing state treats that as residual only.",
                "afc_note",
            ),
            (
                "[INFERENCE] H1 is irrelevant here; direct formal-evidence logic governs the case.",
                "infer",
            ),
        ],
        hypotheses=[
            {
                "heading": "H-D1: GL U RENEWED",
                "probability_range": "0% — CONTRADICTED",
                "body": "Eliminated in the governing state by two independent OFAC checks showing no renewal instrument.",
            },
            {
                "heading": "H-D2: GL U LAPSES 19 APRIL",
                "probability_range": "97–99% — CONFIRMED",
                "body": "Explicitly supported by direct formal evidence in the carried-forward baseline.",
            },
            {
                "heading": "H-D3: WIND-DOWN / RETROACTIVE INSTRUMENT",
                "probability_range": "1–3%",
                "body": "Residual branch only; no such instrument was found in either governing fetch.",
            },
        ],
        tql_items=(
            "The governing OFAC fetches accurately captured the operative sanctions state.",
            "Any later retroactive instrument would be the only fragile point, but it is residual rather than dominant.",
            "Whether downstream compliance and sourcing reactions accelerate faster than expected.",
            "YES — completely. This case stands on formal evidence rather than Tier 4 dependency.",
        ),
        disconf_rows=[
            ("No GL U / no GL 134B / no wind-down instrument", "Later appearance of a valid successor or retroactive instrument"),
            ("H-D2 already classified CONFIRMED", "Formal document contradicting lapse state"),
            ("Reversion triggers active downstream", "No meaningful downstream operational effect appears"),
        ],
        gate5_note="Gate 5 trigger: valid retroactive or successor sanctions instrument requires full Case D reframe.",
        flag_ref="PRED-029-D",
        flag_number=4,
        flag_body=(
            "Monitor whether any retroactive or successor sanctions instrument appears and whether India-linked exposure channels adjust under the lapsed-waiver state."
        ),
        flag_gate_note="Successor instrument = reframe. No instrument + downstream disruption = stronger carry on confirmed lapse effects.",
        styles=styles,
    )

    # CASE E
    add_case(
        story=story,
        case_letter="E",
        title="Saudi Aramco / Yanbu — Follow-On Strike Risk After Reversion Trigger",
        tag="ESCALATING",
        confidence="HIGH",
        heuristics="Gate 5 Reframe Logic · H6 (Cross-System Escalation Chain)",
        facts=[
            (
                "Earlier Yanbu / East-West Pipeline strike activity was already confirmed in the governing baseline, with pipeline restoration later reported. [FACT]",
                "Carry-forward session baseline — GATE 0.",
            ),
            (
                "Khurais restoration remained stale in the governing state and required urgent re-verification for Ed029. [FACT]",
                "Carry-forward session baseline — GATE 0.",
            ),
            (
                "GL U lapse reversion triggers were explicitly activated for Case E, while no fresh follow-on IRGC strike had yet been confirmed in the governing baseline. [FACT]",
                "Carry-forward session baseline — GATE 0.",
            ),
        ],
        incongruity_paras=[
            (
                "[FACT] The case sits between a confirmed prior strike cycle and an unconfirmed follow-on phase. Restoration signals exist, but some infrastructure-state claims remain stale.",
                "body",
            ),
            (
                "[INFERENCE] H-E1 and H-E2 remain open because the sanctions-triggered reversion logic increases pressure even without a fresh kinetic event. The absence of a new strike prevents premature closure.",
                "body",
            ),
            (
                "AFC steelman: the strongest de-risking argument is that restoration plus Lebanon suppressor effects continue to hold and that the strike cycle does not immediately recur.",
                "afc_note",
            ),
            (
                "[INFERENCE] H1 is not explanatory here; the core issue is whether confirmed prior escalation plus fresh sanctions pressure cascades into a new Saudi energy strike branch.",
                "infer",
            ),
        ],
        hypotheses=[
            {
                "heading": "H-E1: NEW FOLLOW-ON IRGC STRIKE ON SAUDI ENERGY TARGETS",
                "probability_range": "42–55%",
                "body": "Still materially live because prior strike precedent exists and reversion triggers are active, but no new strike has yet been confirmed.",
            },
            {
                "heading": "H-E2: PRESSURE RISES WITHOUT IMMEDIATE NEW STRIKE",
                "probability_range": "35–48%",
                "body": "The most operationally plausible carry branch if reversion pressure remains elevated but kinetic follow-on remains delayed.",
            },
            {
                "heading": "H-E3: DE-ESCALATION / NO FOLLOW-ON MATERIALISATION",
                "probability_range": "10–15%",
                "body": "Possible but still minority because prior confirmed strike history and reversion logic keep the case elevated.",
            },
        ],
        tql_items=(
            "GL U lapse materially increases pressure pathways that can feed follow-on Saudi energy targeting logic.",
            "Khurais status is the most fragile factual gap because stale infrastructure-state claims distort the case if left unreverified.",
            "Whether reversion pressure translates into a new kinetic event or stalls below strike threshold.",
            "YES — but with caution; the case still needs renewed hard verification on infrastructure condition before any sharper banding.",
        ),
        disconf_rows=[
            ("New strike indicators, targeting signals, or fresh Saudi disruption", "No new strike indicators while restoration holds"),
            ("GL U reversion pressure remains active", "Key reversion pathway loses operational significance"),
            ("Khurais remains impaired or uncertain", "Fresh authoritative restoration confirmation closes infrastructure gap"),
        ],
        gate5_note="Gate 5 trigger: confirmed new Saudi energy strike or authoritative restoration evidence requires full Case E reframe.",
        flag_ref="PRED-029-E",
        flag_number=5,
        flag_body=(
            "Monitor whether GL U reversion pressure produces a fresh Saudi energy strike branch, and re-verify Khurais status before carrying infrastructure impairment assumptions forward."
        ),
        flag_gate_note="Confirmed new strike = escalation confirmation. Fresh restoration evidence = reduce impairment-driven pressure logic.",
        styles=styles,
    )

    # CARRY-FORWARD FACTS
    story.append(Paragraph("CARRY-FORWARD FACTS", styles["section_head"]))
    story.append(
        fact_table(
            [
                (
                    "H-A1 remains in the 72–82% provisional carry band because no formal second-round announcement threshold had been satisfied in the governing state. [FACT]",
                    "SESSION_STATE carry-forward — TIER CANONICAL · GATE 0",
                ),
                (
                    "H-B3 remains PARTIAL at 26–34% because the Paris Summit initiative is confirmed but force structure is not. [FACT]",
                    "SESSION_STATE carry-forward — TIER CANONICAL · GATE 0",
                ),
                (
                    "H-C1 remains 58–70% and H-C3 remains 10–18% under suppressor logic and absent collapse triggers. [FACT]",
                    "SESSION_STATE carry-forward — TIER CANONICAL · GATE 0",
                ),
                (
                    "H-D2 remains 97–99% CONFIRMED on direct formal evidence. [FACT]",
                    "SESSION_STATE carry-forward — TIER CANONICAL · GATE 0",
                ),
                (
                    "Case E remains open with reversion triggers active and no fresh strike confirmed in the governing baseline. [FACT]",
                    "SESSION_STATE carry-forward — TIER CANONICAL · GATE 0",
                ),
            ],
            styles,
        )
    )
    story.append(hr())

    # CRITICAL WINDOWS
    story.append(Paragraph("CRITICAL WINDOWS — NEXT EDITION PRIORITIES", styles["section_head"]))
    story.append(
        Paragraph(
            "1. Formal second-round announcement check: named date, venue, and agenda threshold. "
            "2. Lebanon ceasefire durability and any qualifying major barrage or large-scale strike. "
            "3. Hormuz AIS recovery, SNSC status, and whether the Paris Summit initiative acquires operational structure. "
            "4. Any retroactive or successor sanctions instrument affecting the GL U lapse state. "
            "5. Khurais re-verification and any evidence of follow-on IRGC targeting against Saudi energy assets.",
            styles["body"],
        )
    )
    story.append(hr())

    # PREDICTION LOG — OPEN
    story.append(Paragraph("PREDICTION LOG — OPEN", styles["section_head"]))
    story.append(
        fact_table(
            [
                ("PRED-029-A — Formal second-round announcement before ceasefire forcing point. [PREDICTION]", "OPEN"),
                ("PRED-029-B — Hormuz conditional opening gains verified operational support or fractures. [PREDICTION]", "OPEN"),
                ("PRED-029-C — Lebanon framework holds beyond suppressor window without major collapse trigger. [PREDICTION]", "OPEN"),
                ("PRED-029-D — No successor sanctions instrument appears after confirmed GL U lapse state. [PREDICTION]", "OPEN"),
                ("PRED-029-E — Reversion pressure does or does not convert into fresh Saudi energy strike activity. [PREDICTION]", "OPEN"),
            ],
            styles,
        )
    )
    story.append(hr())

    # SOURCES
    story.append(Paragraph("SOURCES", styles["section_head"]))
    story.extend(
        source_block(
            [
                {
                    "name": "SESSION_STATE-3-2.md",
                    "tier": "CANONICAL",
                    "category": "Active continuity baseline",
                    "body": "Current governing case state, calibrated hypothesis bands, critical windows, and Ed029 opening requirements.",
                },
                {
                    "name": "styles.py",
                    "tier": "IMPLEMENTATION",
                    "category": "Visual style baseline",
                    "body": "Colour constants, page geometry, and paragraph style factory used by the edition builder.",
                },
                {
                    "name": "build_core.py",
                    "tier": "IMPLEMENTATION",
                    "category": "Layout helper baseline",
                    "body": "Reusable table builders, flowable helpers, forward-flag block, source block, and page callbacks.",
                },
                {
                    "name": "ARCHITECTURE.md v1.2.1",
                    "tier": "CANONICAL",
                    "category": "PDF architecture rules",
                    "body": "Mandatory section order, case structure, and build audit requirements inherited by this edition script.",
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
