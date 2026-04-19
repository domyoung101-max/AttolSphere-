“”“build_edition_022.py — AtollSphere Edition 022 Evening Sweep · 14 April 2026.

Run:
python build_edition_022.py

Dependencies:
styles.py     — colour constants and make_styles()
build_core.py — layout helpers and make_page_callbacks()
“””

import datetime

from reportlab.platypus import (
SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
PageBreak, KeepTogether,
)
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_CENTER

from styles import (
make_styles,
NAVY, TEAL, CHARCOAL, MID_GREY, LIGHT_BG, ROW_ALT,
WHITE, RED_TAG, AMBER, GREEN_TAG,
MARGIN,
)
from build_core import (
hr, thin_rule,
tag_table, fact_table, hyp_table, disconf_table,
flag_block, source_block,
make_page_callbacks,
)

# ── EDITION CONSTANTS ─────────────────────────────────────────────────────────

EDITION   = "029"
DATE_STR  = "19 APRIL 2026"
SWEEP_STR = "AFTERNOON SWEEP"

GMT_NOW = datetime.datetime(2026, 4, 19, 14, 53, 0)
BST_NOW = GMT_NOW + datetime.timedelta(hours=1)
GMT_STR = GMT_NOW.strftime("%d %B %Y · %H:%M GMT")
BST_STR = BST_NOW.strftime("%H:%M BST")

# ── BUILD ─────────────────────────────────────────────────────────────────────

def build():
path = (
f”/mnt/user-data/outputs/”
f”atollsphere_brief_{EDITION}*{SWEEP_STR.lower().replace(’ ’, ’*’)}.pdf”
)
doc = SimpleDocTemplate(
path, pagesize=A4,
leftMargin=MARGIN, rightMargin=MARGIN,
topMargin=18*mm, bottomMargin=14*mm,
)
styles = make_styles()
story  = []
on_cover, on_page = make_page_callbacks(EDITION, SWEEP_STR, DATE_STR)

```
# ── COVER ─────────────────────────────────────────────────────────────────
story.append(Spacer(1, 28*mm))

stats = Table([[
    Paragraph('<b>EDITION</b>', styles['cover_label']),
    Paragraph('<b>DATE</b>',    styles['cover_label']),
    Paragraph('<b>SWEEP</b>',   styles['cover_label']),
    Paragraph('<b>DAY</b>',     styles['cover_label']),
    Paragraph('<b>STATUS</b>',  styles['cover_label']),
],[
    Paragraph(f'<b>{EDITION}</b>',            styles['cover_value']),
    Paragraph(f'<b>{DATE_STR}</b>',            styles['cover_value']),
    Paragraph(f'<b>{SWEEP_STR}</b>',           styles['cover_value']),
    Paragraph('<b>WAR DAY 47</b>',             styles['cover_value']),
    Paragraph('<b>ESCALATING CRITICAL</b>',    styles['cover_value']),
]], colWidths=[35*mm]*5)
stats.setStyle(TableStyle([
    ('ALIGN',         (0,0), (-1,-1), 'CENTER'),
    ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING',    (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('LINEABOVE',     (0,0), (-1, 0), 0.5, TEAL),
    ('LINEBELOW',     (0,-1),(-1,-1), 0.5, TEAL),
]))
story.append(stats)
story.append(Spacer(1, 10*mm))

story.append(Paragraph(
    'Islamabad Fails. USN Blockade Declared. Lebanon Talks Begin. GL U T-5.',
    styles['cover_title']))
story.append(Spacer(1, 8*mm))

counts = Table([[
    Paragraph('<b>5</b><br/><font size=7>CASES</font>',
        ParagraphStyle('cnt',  fontName='Helvetica-Bold', fontSize=20,
                       textColor=NAVY,    alignment=TA_CENTER)),
    Paragraph('<b>5</b><br/><font size=7>ESCALATING</font>',
        ParagraphStyle('cnt2', fontName='Helvetica-Bold', fontSize=20,
                       textColor=RED_TAG, alignment=TA_CENTER)),
    Paragraph('<b>14</b><br/><font size=7>OPEN PREDICTIONS</font>',
        ParagraphStyle('cnt3', fontName='Helvetica-Bold', fontSize=20,
                       textColor=AMBER,   alignment=TA_CENTER)),
    Paragraph('<b>5</b><br/><font size=7>NEW FORWARD FLAGS</font>',
        ParagraphStyle('cnt4', fontName='Helvetica-Bold', fontSize=20,
                       textColor=TEAL,    alignment=TA_CENTER)),
]], colWidths=[43.5*mm]*4)
counts.setStyle(TableStyle([
    ('ALIGN',     (0,0), (-1,-1), 'CENTER'),
    ('VALIGN',    (0,0), (-1,-1), 'MIDDLE'),
    ('LINEAFTER', (0,0), ( 2, 0), 0.5, colors.HexColor('#D0D8E0')),
]))
story.append(counts)
story.append(PageBreak())

# ── SITUATION OVERVIEW ────────────────────────────────────────────────────
story.append(Paragraph('SITUATION OVERVIEW', styles['section_head']))
story.append(hr())
story.append(Paragraph(
    f'<b>{DATE_STR} · {SWEEP_STR} · {GMT_STR} ({BST_STR})</b>',
    styles['small_bold']))
story.append(Spacer(1, 2*mm))
story.append(Paragraph(
    'Edition 022 sweep conducted at approximately 2334 GMT (BST 0034) on 14/15 April 2026, War Day 47. '
    'The sweep covers the period from 0730 GMT 12 April (Edition 021 close) to sweep timestamp — a 39-hour window '
    'spanning the conclusion of the Islamabad Talks, the USN blockade declaration, the Israel-Lebanon Washington '
    'talks, and the GL 134B 15 April trigger. Five cases remain active, all at ESCALATING or ESCALATING CRITICAL. '
    'Eleven predictions closed or resolved this sweep. Five new forward flags issued: PRED-022-A through PRED-022-E.',
    styles['body']))
story.append(Paragraph(
    'Primary development: Islamabad Talks concluded 12 April without deal — both delegations departed. '
    'PRED-017-A / 019-A / 021-A: DEPARTURE CONFIRMED. Trump declared USN blockade of Iranian ports effective '
    '13 April — PRED-020-B / 021-B: KINETIC CONFIRMED. East-West Pipeline restored to 7M bpd (12 April); '
    'no follow-on IRGC Yanbu strike at sweep, but follow-on strike probability upgraded to HIGH (65-75%). '
    'Lebanon death toll updated: 2,080+. GL U confirmed active through 19 April; GL 134B absent at 15 April trigger.',
    styles['body']))
story.append(Paragraph(
    'H6 (Suppressed Intersection) dominant across Cases B, D, E. H1 saturation flag active through Edition 025. '
    'Islamabad failure, blockade declaration, Lebanon talks, and 19 April GL U expiry form a single dependency '
    'chain with the 22 April ceasefire expiry as the hard terminal forcing function.',
    styles['body']))

# PCP Step 1.5
story.append(Paragraph('PCP STEP 1.5 — NEW SIGNAL CHECK', styles['section_head']))
story.append(Paragraph(
    '[MANDATORY — AI-003] No new case threshold met this edition. Five developments assessed — all fit within '
    'existing cases. PRED-022-E (Chinese-flag blockade breach) fits within Case B enforcement sub-case and does '
    'not independently satisfy the three-part new case threshold. No new case opened.',
    styles['body']))

# H1 Saturation
story.append(Paragraph('H1 SATURATION CHECK — STANDING RULE (AI-003)', styles['section_head']))
story.append(Paragraph(
    'H1 fired all five cases Editions 019-022. Ed022: H1 correct at macro level. '
    'H6 dominant Cases B/D/E. H3/H5 dominant Case C. H5/H6 dominant Case A. '
    'Pattern-matching risk acknowledged — each Part 2 explicitly assesses H1 vs framework default. '
    'Active through Edition 025 calibration audit.',
    styles['body']))
story.append(hr())

# ── CLOSED WINDOW CLASSIFICATIONS ─────────────────────────────────────────
story.append(Paragraph('CLOSED WINDOW CLASSIFICATIONS — EDITION 022', styles['section_head']))
story.append(Paragraph(
    '<b>PRED-020-B / PRED-021-B: KINETIC — CONFIRMED.</b> USN DDGs Frank E. Petersen Jr. and Michael Murphy '
    'transited Hormuz 11 April. Trump declared full naval blockade 13 April. CENTCOM confirmed. '
    'Additional MCM vessels (Pioneer, Chief, Tulsa) en route. '
    'Classification: KINETIC — blockade plus mine clearance operations constitute kinetic posture change.',
    styles['body']))
story.append(Paragraph(
    '<b>PRED-017-A / PRED-019-A / PRED-021-A: DEPARTURE — CONFIRMED.</b> Both delegations departed Islamabad '
    '12 April without communique. AMBIGUOUS branch (PRED-019-A) does not apply — delegations departed, not remained. '
    'Vance: US "made very clear what our red lines are." Araghchi: two sides "inches away" but encountered '
    '"maximalism, shifting goalposts, and blockade."',
    styles['body']))
story.append(hr())

# ── CASE A ────────────────────────────────────────────────────────────────
story.append(tag_table('A',
    'Islamabad — No Deal / Departure / USN Blockade / Second Round Pending',
    'ESCALATING', 'HIGH', None, styles))
story.append(Paragraph('Heuristics: H5 (Structural Contradiction) · H6 (Suppressed Intersection)',
    styles['heuristic_line']))

story.append(Paragraph('PART 1 — FACTUAL ELEMENTS', styles['section_head']))
story.append(fact_table([
    ('Islamabad Talks lasted 21 hours, 11-12 April. Three rounds: first indirect, second and third direct. '
     'US delegation (~300) led by VP Vance, Witkoff, Kushner. Iranian delegation (~70) led by Ghalibaf and '
     'FM Araghchi. Pakistan mediated: PM Sharif, Field Marshal Munir, FM Dar.',
     'Wikipedia / Al Jazeera (Tier 2/4). Wikipedia Tier 4 — directional corroboration per AI-002. '
     'Gate 0.4: MEDIUM. Temporal currency: 12 April 2026. [FACT]'),
    ('Both delegations departed without deal. Vance: "made very clear what our red lines are… they have not '
     'chosen to accept our terms." Araghchi: "inches away" but encountered "maximalism, shifting goalposts, '
     'and blockade." Iranian officials: contacts expected to continue.',
     'CFR (Tier 2), TIME (Tier 2), Al Jazeera (Tier 2). Gate 0.4: MEDIUM. '
     'Temporal currency: 12-13 April. [FACT]'),
    ('White House: "Future talks are under discussion but nothing has been scheduled at this time." '
     'Vance: Iranians "moved in our direction… but didn\'t move far enough." '
     'Pakistan-UK high-level exchange on outcomes 14 April. Pakistan Defence Minister: next round expected soon.',
     'TIME (Tier 2), Fox News (Tier 2), Nation Pakistan (Tier 2). Gate 0.4: MEDIUM-HIGH on US statements. '
     'Temporal currency: 13-14 April. [FACT with incentive flag]'),
    ('Trump post-Islamabad: USN to blockade all ships entering/leaving Hormuz and interdict every vessel '
     'in international waters that has paid a toll to Iran.',
     'Truth Social via CENTCOM (Tier 1). Gate 0.4: HIGH — Trump incentive to project dominance. '
     'CENTCOM confirmed blockade effective 13 April. Temporal currency: 13 April. [FACT]'),
], styles))

story.append(Paragraph('PART 2 — OBSERVED INCONGRUITY', styles['section_head']))
story.append(Paragraph(
    '<b>H5 (Structural Contradiction):</b> Iran\'s four non-negotiable conditions — full Hormuz sovereignty, '
    'reparations, unconditional asset release, West-Asia ceasefire — remain categorically incompatible with '
    'US red lines. The gap is categorical, not procedural.',
    styles['body']))
story.append(Paragraph(
    '<b>H6 (Suppressed Intersection):</b> Islamabad failure directly triggered the blockade declaration. '
    'The blockade simultaneously removes Iranian Hormuz leverage in any second round; creates IRGC kinetic '
    'trigger (Cases B/E); intensifies India\'s supply constraint (Case D); and removes Iran\'s economic '
    'incentive to negotiate. This is the densest H6 intersection of the war.',
    styles['body']))
story.append(Paragraph(
    '<b>AFC:</b> Both sides signal continued engagement. Iran stated a single round was never expected to '
    'resolve all issues. Pakistan channel intact. Ceasefire expiry 22 April is a structural forcing function '
    'for both sides. Second-round probability: 55-65%.',
    styles['afc_note']))
story.append(Paragraph(
    'INFERENCE: H1 partially applicable — both sides have domestic narrative incentives. H5/H6 primary. '
    '[H1 SATURATION CHECK]: H1 secondary here.',
    styles['infer']))
story.append(Paragraph(
    'Domain quality: Tier 1/2 evidence independently sustains second-round probability without Tier 4.',
    styles['small']))

story.append(Paragraph('PART 3 — HYPOTHESIS SET', styles['section_head']))
story.append(hyp_table([
    {'heading': 'H-A1: SECOND ROUND BEFORE 22 APRIL — DOMINANT',
     'probability_range': '55-65%',
     'body': 'Second round of US-Iran talks before ceasefire expires 22 April. White House confirmed openness. '
             'Pakistan channel intact. Forcing function: ceasefire expiry. Requires no IRGC kinetic escalation '
             'against USN and Iran not formally walking out of process.'},
    {'heading': 'H-A2: CEASEFIRE LAPSES — NO SECOND ROUND',
     'probability_range': '25-35%',
     'body': 'No second round before 22 April. Ceasefire expires without extension. '
             'Trigger: IRGC kinetic response to blockade; US maximalism prevents re-engagement; '
             'domestic political dynamics in Tehran force departure from process. PRED-015-A CONTRADICTED.'},
    {'heading': 'H-A3: CEASEFIRE EXTENDED / FRAMEWORK EMERGING',
     'probability_range': '10-15%',
     'body': 'Formal ceasefire extension agreed before 22 April via back-channel. Lower probability given '
             'Trump blockade declaration and Vance "best, final offer" framing.'},
], styles))

story.append(Paragraph('PART 4 — TRUTH QUALITY CHECK', styles['section_head']))
story.append(Paragraph(
    '<b>Key assumption:</b> White House "openness" to second round is genuine policy, not rhetorical. '
    'Counter-assumption: Vance "best, final offer" framing formally closes US negotiating space.',
    styles['body']))
story.append(Paragraph(
    '<b>Fragile fact:</b> Vance claim Iranians "moved in our direction" — Tier 1, HIGH incentive distortion. '
    'Araghchi disputed this on X. If Iranian account accurate, H-A1 probability falls to 40-50%.',
    styles['body']))
story.append(Paragraph(
    '<b>High-impact uncertainty:</b> Whether IRGC kinetic response to blockade (PRED-022-B) occurs before '
    'ceasefire expiry. If confirmed kinetic, H-A2 probability rises sharply to 50-60%.',
    styles['body']))
story.append(Paragraph(
    '<b>Tier 4 dependency test:</b> H-A1 stripped of Wikipedia — Tier 1/2 sources (TIME, CFR, White House, '
    'Deccan Herald) independently support second-round possibility. Range maintained.',
    styles['body']))

story.append(Paragraph('PART 5 — DISCONFIRMATION', styles['section_head']))
story.append(disconf_table([
    ('Second round announced before 22 April — H-A1 CONFIRMED',
     'IRGC kinetic response to blockade before expiry — H-A2 probability rises sharply'),
    ('Ceasefire formally extended before 22 April — H-A3 pathway opens',
     'Iran formally withdraws from negotiating process — H-A2 CONFIRMED'),
    ('Pakistan hosts or facilitates second round',
     'Ceasefire lapses 22 April without extension or second round — PRED-015-A CONTRADICTED'),
], 'Second round formally announced = H-A1 CONFIRMED, Case A tag review. '
   'Iran withdraws from process = H-A2 CONFIRMED, Case A ESCALATING CRITICAL. '
   'Ceasefire lapses 22 April = PRED-015-A CONTRADICTED, all cases reassessed.', styles))
story.append(Paragraph(
    '<i>Gate 5 Framing Revision Trigger: Iran formally withdraws from negotiating process — '
    'reframe Case A to ESCALATING CRITICAL from scratch.</i>',
    styles['pred_note']))

story.extend(flag_block(
    'PRED-022-A', 1,
    'Monitor whether a second round of US-Iran talks is announced before ceasefire expiry 22 April. '
    'Window: 15-21 April. C1: forward-looking. C2: specific (second round, named parties, 22 April deadline). '
    'C3: falsifiable (announced = CONFIRMED; ceasefire lapses = CONTRADICTED). C4: 22 April forcing function. '
    'C5: resolves Case A trajectory and informs PRED-015-A classification. '
    'Five-state: CONFIRMED / CONTRADICTED / PARTIAL (announced but not held) / '
    'AMBIGUOUS (back-channel only) / UNRESOLVABLE (comms blackout).',
    'Second round announced before 22 April — PRED-022-A CONFIRMED.',
    styles))
story.append(hr())

# ── CASE B ────────────────────────────────────────────────────────────────
story.append(tag_table('B',
    'Hormuz — USN Blockade Active / Mine Clearance / Transit <12/day',
    'ESCALATING', 'HIGH', None, styles))
story.append(Paragraph('Heuristics: H6 (Suppressed Intersection) · H4 (Narrative vs Outcome Gap)',
    styles['heuristic_line']))
story.append(Paragraph(
    '<b>PRED-020-B / PRED-021-B: KINETIC — CONFIRMED. PRED-018-B: CONFIRMED.</b> '
    'Transit far below 15/day threshold.',
    styles['body']))

story.append(Paragraph('PART 1 — FACTUAL ELEMENTS', styles['section_head']))
story.append(fact_table([
    ('USS Frank E. Petersen Jr. (DDG 121) and USS Michael Murphy (DDG 112) transited Hormuz 11 April. '
     'CENTCOM: "broader mission to ensure the strait is fully clear of sea mines previously laid by Iran\'s IRGC." '
     'Adm. Cooper: "Today, we began the process of establishing a new passage."',
     'CENTCOM (Tier 1 / Gate 0.4: MEDIUM). Naval News, DefenseScoop (Tier 2). '
     'Gate 0.3: Named vessels confirmed. Temporal currency: 11 April. [FACT]'),
    ('Trump blockade declared 13 April. CENTCOM: blockade enforced against vessels of all nations entering/'
     'departing Iranian ports. Freedom of navigation maintained for vessels to/from non-Iranian ports. '
     'Transit <12 ships/day vs pre-war ~130/day. Early enforcement strain: up to 4 vessels including '
     'Chinese-owned Rich Starry believed to have breached without interception.',
     'Truth Social / CENTCOM (Tier 1). Naval News, LSEG via Naval News (Tier 2/3 / Gate 0.5: AIS cluster '
     'single-source). Temporal currency: 13-14 April. [FACT]'),
    ('France/UK announced 17 April online meeting for "defensive multilateral mission" to maintain Hormuz open. '
     'Australia navy stated readiness. IRGC vowed "strong response" to USN presence. '
     'No confirmed IRGC kinetic engagement against USN through sweep.',
     'Eurotopics (Tier 2), Wikipedia (Tier 4 — directional only per AI-002). '
     'IRGC via Al Jazeera (Tier 3 / Gate 0.5: Iranian state cluster). '
     'Absence confirmed across NBC, CNN, Naval News. [FACT — absence observable]'),
], styles))

story.append(Paragraph('PART 2 — OBSERVED INCONGRUITY', styles['section_head']))
story.append(Paragraph(
    '<b>H6 (Suppressed Intersection):</b> Blockade simultaneously removes Iranian Hormuz leverage in any '
    'second-round talks; creates IRGC kinetic trigger (Case E — displaced Aramco strike more likely than '
    'direct USN engagement); eliminates shadow-fleet crude from Asian markets; forces GL U contradiction '
    'into the open (Case D).',
    styles['body']))
story.append(Paragraph(
    '<b>H4 (Narrative vs Outcome Gap):</b> Iran denied USN transits on state TV while CENTCOM confirmed '
    'them with named vessels. AIS data independently confirms presence. Competing narrative management, '
    'not factual dispute.',
    styles['body']))
story.append(Paragraph(
    '<b>AFC:</b> Chinese-flag Rich Starry breach suggests enforcement gap. If multiple breaches go '
    'unaddressed, blockade credibility degrades and Iran perceives no cost to continued transit denial. '
    'AI-001: disconfirmation threshold remains transit >54-68/day.',
    styles['afc_note']))
story.append(Paragraph(
    'INFERENCE: H1 secondary. H6 primary. [H1 SATURATION CHECK]: H1 not load-bearing here.',
    styles['infer']))

story.append(Paragraph('PART 3 — HYPOTHESIS SET', styles['section_head']))
story.append(hyp_table([
    {'heading': 'H-B1: IRGC SELECTIVE PASSAGE PERSISTS — DOMINANT',
     'probability_range': '40-55%',
     'body': 'IRGC maintains selective transit denial under blockade. Enforcement gap allows some vessels through. '
             'Transit remains <15/day. Mine threat persists as negotiating leverage. '
             'USN MCM capability insufficient for rapid full clearance (USNI Proceedings).'},
    {'heading': 'H-B2: IRGC KINETIC RESPONSE TO USN',
     'probability_range': '25-35%',
     'body': 'IRGC attacks USN blockade assets. IRGC credibility at stake after "strong response" pledge. '
             'Decentralised command: local commander could act without Tehran authorisation. '
             'UPGRADED from Ed021 10-20%. PRED-022-B window.'},
    {'heading': 'H-B3: MULTILATERAL MISSION PROVIDES COVER',
     'probability_range': '10-15%',
     'body': 'Macron/Starmer 17 April meeting produces coalition for partial Hormuz reopening. '
             'Requires Iran to accept non-IRGC governance. Low probability: Iran rejected consistently.'},
], styles))

story.append(Paragraph('PART 4 — TRUTH QUALITY CHECK', styles['section_head']))
story.append(Paragraph(
    '<b>Key assumption:</b> AIS/LSEG data is representative of actual transit volume. Gate 0.5 applies — '
    'AIS dark vessels may undercount by meaningful margin.',
    styles['body']))
story.append(Paragraph(
    '<b>Fragile fact:</b> "Up to 4 vessels breached" — LSEG single-source, not independently verified. '
    'If actual breach count higher, H-B1 enforcement credibility is materially weaker.',
    styles['body']))
story.append(Paragraph(
    '<b>High-impact uncertainty:</b> IRGC command authority decentralisation. Local IRGC commander '
    'in Hormuz theatre may initiate kinetic response without central authorisation — non-zero risk '
    'even if Tehran signals restraint.',
    styles['body']))
story.append(Paragraph(
    '<b>Tier 4 dependency test:</b> H-B1 stripped of Wikipedia — Tier 1/2 sources (CENTCOM, Naval News, '
    'LSEG, Eurotopics) independently support selective passage / enforcement gap scenario. Range maintained.',
    styles['body']))

story.append(Paragraph('PART 5 — DISCONFIRMATION', styles['section_head']))
story.append(disconf_table([
    ('IRGC continues non-kinetic posture through 22 April — H-B1 dominant signal',
     'IRGC kinetic attack on USN vessels — PRED-022-B CONFIRMED, joint Cases B/E ESCALATING CRITICAL'),
    ('Transit remains <15/day through 15 April — PRED-018-B CONFIRMED',
     'Transit exceeds 54-68 ships/day for 3+ consecutive days — H-B1 CONTRADICTED'),
    ('Multilateral Hormuz coalition announced 17 April — H-B3 pathway opens',
     'Formal written Hormuz transit protocol signed — H-B2 CONTRADICTED'),
], 'Kinetic IRGC engagement with USN at any point = immediate ESCALATING CRITICAL across Cases A, B, E.',
styles))
story.append(Paragraph(
    '<i>Gate 5 Framing Revision Trigger: IRGC kinetic engagement with USN vessels — '
    'immediate ESCALATING CRITICAL reassessment across Cases A, B, E. Reframe from scratch.</i>',
    styles['pred_note']))

story.extend(flag_block(
    'PRED-022-B', 2,
    'Monitor IRGC kinetic response to USN blockade/mine clearance through 22 April. '
    'Window: 15-22 April. C3: falsifiable (kinetic = CONFIRMED; no engagement = NON-KINETIC). '
    'C4: 22 April terminal. C5: resolves Case B/E joint assessment. '
    'Five-state: CONFIRMED kinetic (ESCALATING CRITICAL, joint Cases B/E) / CONFIRMED non-kinetic / '
    'PARTIAL (harassment without kinetic strike) / AMBIGUOUS (contested incident) / '
    'UNRESOLVABLE (ceasefire renewed before window closes).',
    'IRGC kinetic engagement confirmed — PRED-022-B CONFIRMED kinetic.',
    styles))
story.append(hr())

# ── CASE C ────────────────────────────────────────────────────────────────
story.append(tag_table('C',
    'Lebanon — 2,080+ Killed / Washington Framework / No Ceasefire',
    'ESCALATING', 'HIGH', None, styles))
story.append(Paragraph('Heuristics: H3 (Beneficiary Asymmetry) · H5 (Structural Contradiction)',
    styles['heuristic_line']))
story.append(Paragraph(
    '<b>PRED-021-C: PARTIAL.</b> Talks at ambassador level, not PM. '
    '<b>PRED-017-C: FAILED.</b> No ceasefire. '
    '<b>PRED-020-C: PARTIAL.</b> Framework commitment only. '
    'Death toll updated: <b>2,080+ killed</b> (Al Jazeera, 14 April).',
    styles['body']))

story.append(Paragraph('PART 1 — FACTUAL ELEMENTS', styles['section_head']))
story.append(fact_table([
    ('Lebanon death toll: 2,080+ killed. Israel intensified attacks including extremely heavy Beirut strike '
     '8 April. More than 1 million displaced. Israeli ground forces operating in southern Lebanon.',
     'Al Jazeera (Tier 2 / Gate 0.4: MEDIUM). Lebanese Health Ministry named source. '
     'Temporal currency: 14 April 2026. UPDATED from 2,020+. [FACT]'),
    ('Israel-Lebanon talks held 14 April at State Department. First direct talks since 1993. '
     'Participants: Secretary Rubio, Israeli Ambassador Leiter, Lebanese Ambassador Mouawad, '
     'US Ambassador Issa, State Dept Counsellor Needham.',
     'NPR (Tier 2), Al Jazeera (Tier 2), Israel Hayom (Tier 2), Axios (Tier 2). '
     'Gate 0.4: MEDIUM. Temporal currency: 14 April. [FACT]'),
    ('Joint statement: "All sides agreed to launch direct negotiations." Rubio: "This is a process, '
     'not a single event." No ceasefire agreed. Israel: "There will be no discussion of a ceasefire '
     'with Hezbollah." Fighting continued through Tuesday.',
     'Israel Hayom (Tier 2), NPR (Tier 2), Washington Times (Tier 2). '
     'Gate 0.4: MEDIUM-HIGH. Temporal currency: 14 April. [FACT]'),
    ('Hezbollah\'s Qassem: talks were "futile," Lebanese leadership made "concessions for free," '
     'called engagement "surrender under fire." Urged Lebanese government to cancel talks.',
     'Al Jazeera (Tier 2), NPR (Tier 2). Gate 0.5: Hezbollah statements = single-source cluster. '
     'Temporal currency: 13-14 April. [FACT]'),
], styles))

story.append(Paragraph('PART 2 — OBSERVED INCONGRUITY', styles['section_head']))
story.append(Paragraph(
    '<b>H3 (Beneficiary Asymmetry):</b> Israel secured a framework process without agreeing any '
    'operational restraint. Talks structurally asymmetric: Lebanon sought a ceasefire; Israel obtained '
    'a normalisation framework while continuing its ground offensive in southern Lebanon.',
    styles['body']))
story.append(Paragraph(
    '<b>H5 (Structural Contradiction):</b> The Lebanese government does not control Hezbollah. '
    'Any agreement it signs cannot guarantee Hezbollah compliance. Hezbollah\'s "surrender" framing '
    'further undermines Lebanon\'s negotiating position.',
    styles['body']))
story.append(Paragraph(
    '<b>AFC:</b> Talks occurred at all — first direct engagement since 1993. Joint statement issued. '
    'Process continuity is real even if operational impact is zero.',
    styles['afc_note']))
story.append(Paragraph(
    'INFERENCE: H1 relevant but secondary to H3/H5. Framework-without-ceasefire outcome '
    'consistent with Ed021 H-C2 dominant prediction. [H1 SATURATION CHECK]: H3/H5 primary.',
    styles['infer']))

story.append(Paragraph('PART 3 — HYPOTHESIS SET', styles['section_head']))
story.append(hyp_table([
    {'heading': 'H-C1: FRAMEWORK LEADS TO OPERATIONAL PAUSE',
     'probability_range': '20-30%',
     'body': 'Washington framework produces operational pause in Israeli strikes on Beirut. '
             'Ground offensive in southern Lebanon continues regardless. '
             'Hezbollah restraint conditional on Israel reducing Beirut strikes.'},
    {'heading': 'H-C2: FRAMEWORK WITHOUT OPERATIONAL IMPACT — DOMINANT',
     'probability_range': '55-65%',
     'body': 'No ceasefire. Israeli strikes continue. Hezbollah continues rocket fire and ground combat. '
             'Washington framework is a diplomatic channel, not an operational restraint mechanism. '
             'Consistent with Ed021 H-C2 dominant prediction.'},
    {'heading': 'H-C3: HEZBOLLAH ESCALATION / FRAMEWORK COLLAPSE',
     'probability_range': '10-15%',
     'body': 'Hezbollah escalates in response to Lebanese government participation — "surrender" framing '
             'creates domestic pressure to demonstrate capability. H-C3 risk unchanged from Ed021.'},
], styles))

story.append(Paragraph('PART 4 — TRUTH QUALITY CHECK', styles['section_head']))
story.append(Paragraph(
    '<b>Key assumption:</b> Lebanese government participation constitutes genuine diplomatic agency. '
    'Counter-assumption: government structurally unable to deliver Hezbollah compliance, making any '
    'agreement non-binding on the actual combatant.',
    styles['body']))
story.append(Paragraph(
    '<b>Fragile fact:</b> Death toll 2,080+ (Al Jazeera / Lebanese Health Ministry, Tier 2). '
    'Likely undercounts — Health Ministry figures lag Civil Defence counts in active conflict.',
    styles['body']))
story.append(Paragraph(
    '<b>High-impact uncertainty:</b> Whether US applies meaningful operational pressure on Israel. '
    'Trump called Lebanon "a separate skirmish." Without US pressure, H-C2 dominance is structurally locked in.',
    styles['body']))
story.append(Paragraph(
    '<b>Tier 4 dependency test:</b> H-C2 supported by Tier 1 evidence alone — NPR, Al Jazeera, '
    'Israel Hayom, Washington Times independently confirm no ceasefire agreed and Israel explicitly rejected it.',
    styles['body']))

story.append(Paragraph('PART 5 — DISCONFIRMATION', styles['section_head']))
story.append(disconf_table([
    ('Hezbollah maintains restraint through 22 April — H-C3 risk suppressed',
     'Hezbollah launches coordinated full-scale rocket attack — H-C3 CONFIRMED, Case C ESCALATING CRITICAL'),
    ('Israel reduces Beirut strikes as implicit framework element — H-C1 partial pathway',
     'Israel formally states no reduction in Lebanon — PRED-017-C CONTRADICTED (already failed)'),
    ('Second round of Israel-Lebanon talks scheduled — process continuity confirmed',
     'Lebanese government formally withdraws from talks framework — H-C3 probability rises'),
], 'Hezbollah full-scale kinetic escalation = Case C ESCALATING CRITICAL, reframe from scratch.', styles))
story.append(Paragraph(
    '<i>Gate 5 Framing Revision Trigger: Hezbollah full-scale kinetic escalation = '
    'Case C upgrades to ESCALATING CRITICAL. Reframe from scratch.</i>',
    styles['pred_note']))

story.extend(flag_block(
    'PRED-022-C (monitoring)', 3,
    'No primary new Lebanon forward flag this edition — Washington talks resolved PRED-021-C. '
    'Monitor: (1) Whether Hezbollah kinetically escalates in response to Lebanese government participation. '
    '(2) Whether Israel reduces Beirut strikes as implicit framework element. '
    '(3) Whether second round of Israel-Lebanon talks scheduled. Window: through 22 April.',
    'Hezbollah kinetic escalation or Israeli operational pause — Case C reframe.',
    styles))
story.append(hr())

# ── CASE D ────────────────────────────────────────────────────────────────
story.append(tag_table('D',
    'India Oil Waiver — GL 134B NOT ISSUED / GL U Expires 19 April T-5',
    'ESCALATING', 'HIGH', None, styles))
story.append(Paragraph('Heuristics: H6 (Suppressed Intersection) · H1 (Incentive Analysis)',
    styles['heuristic_line']))
story.append(Paragraph(
    '<b>PRED-021-D / PRED-020-D / PRED-008-D: CONFIRMED.</b> '
    'GL 134B absent from OFAC at 15 April 0000 EDT trigger. GL U active through 19 April — T-5 days.',
    styles['body']))

story.append(Paragraph('PART 1 — FACTUAL ELEMENTS', styles['section_head']))
story.append(fact_table([
    ('GL 134B NOT on OFAC register at sweep. OFAC selected general licenses page reviewed at direct fetch. '
     'Iran General License U active through 12:01 a.m. EDT 19 April 2026. '
     'GL U authorises delivery/sale of Iranian-origin crude loaded on vessels on or before 20 March 2026.',
     'OFAC official register (Tier 1 — direct fetch). Gate 0.4: LOW — absence is verifiable fact. '
     'Temporal currency: ~2334 GMT 14 April 2026. [FACT]'),
    ('GL U and blockade are simultaneously active — the central unresolved US Iran policy contradiction. '
     'GL U expires 19 April, one week after blockade declared 13 April. '
     'Any renewal of Iranian crude authorisation would directly contradict the blockade.',
     'CFR (Tier 2 / Gate 0.4: LOW). HouseofSaud/Conflict Pulse (Tier 3 / Gate 0.4: MEDIUM). '
     'Temporal currency: 12-14 April 2026. [FACT / INFERENCE hybrid]'),
    ('India\'s four named buyers — IOC, BPCL, HPCL, Reliance — authorised under GL U. '
     'GL U cargoes must be loaded on or before 20 March 2026. Existing in-transit cargoes authorised through '
     '19 April. Saudi Arabia\'s market share in Indian crude imports dropped 16% to 11% since GL U issued.',
     'HouseofSaud (Tier 3), Sullivan & Cromwell (Tier 2), CFR (Tier 2). '
     'Gate 0.4: MEDIUM. Temporal currency: April 2026. [FACT]'),
], styles))

story.append(Paragraph('PART 2 — OBSERVED INCONGRUITY', styles['section_head']))
story.append(Paragraph(
    '<b>H6 (Suppressed Intersection):</b> The GL U / blockade contradiction is structurally irresolvable '
    'without a policy decision. The blockade\'s political logic argues against renewal — renewing Iranian '
    'crude licences while simultaneously blockading Iranian ports would be internally contradictory.',
    styles['body']))
story.append(Paragraph(
    '<b>H1 (Incentive Analysis):</b> OFAC may use GL U renewal as leverage on India to publicly advocate '
    'for Hormuz reopening. But the blockade removes the underlying oil availability that made GL U meaningful.',
    styles['body']))
story.append(Paragraph(
    'INFERENCE: H6 analytically primary. H1 relevant for leverage framing but secondary. '
    '[H1 SATURATION CHECK]: H6 primary here.',
    styles['infer']))

story.append(Paragraph('PART 3 — HYPOTHESIS SET', styles['section_head']))
story.append(hyp_table([
    {'heading': 'H-D1: GL U RENEWAL / SUCCESSOR BEFORE 19 APRIL',
     'probability_range': '15-25%',
     'body': 'OFAC issues renewal or successor before 19 April expiry. Requires political decision to '
             'contradict the blockade. Possible only if back-channel produces interim Hormuz opening formula. '
             'Very low probability given current posture.'},
    {'heading': 'H-D2: GL U LAPSES 19 APRIL — DOMINANT',
     'probability_range': '70-80%',
     'body': 'GL U expires without renewal. India\'s in-transit Iranian cargoes complete delivery. '
             'No new Iranian crude purchases authorised. India must source from Saudi Yanbu (constrained) '
             'or non-Gulf suppliers. Secondary sanctions exposure on UCO Bank rupee-rial channel.'},
    {'heading': 'H-D3: PARTIAL SUCCESSOR / DIFFERENT GL FORMAT',
     'probability_range': '5-10%',
     'body': 'OFAC issues partial successor instrument for cargoes loaded after 20 March. '
             'Technically feasible. Politically awkward given blockade. Lowest probability scenario.'},
], styles))

story.append(Paragraph('PART 4 — TRUTH QUALITY CHECK', styles['section_head']))
story.append(Paragraph(
    '<b>Key assumption:</b> OFAC would not issue GL 134B or GL U renewal without public announcement '
    'on the Selected General Licenses page. Well-established operational procedure; held through all prior editions.',
    styles['body']))
story.append(Paragraph(
    '<b>Fragile fact:</b> GL U carry-forward from Ed019 confirmed at Ed022 direct fetch — active through '
    '19 April. Re-fetch mandatory at Ed023 before any Case D assessment.',
    styles['body']))
story.append(Paragraph(
    '<b>High-impact uncertainty:</b> Whether blockade/GL U contradiction resolves via policy decision '
    'before 19 April. Back-channel Iran/US interim agreement would change the political logic for renewal.',
    styles['body']))
story.append(Paragraph(
    '<b>Tier 4 dependency test:</b> H-D2 supported by Tier 1 evidence alone — OFAC register direct fetch '
    'confirms GL U expires 19 April and no GL 134B present. No Tier 4 dependency.',
    styles['body']))

story.append(Paragraph('PART 5 — DISCONFIRMATION', styles['section_head']))
story.append(disconf_table([
    ('GL U renewed or GL 134B appears on OFAC before 19 April — H-D2 CONTRADICTED',
     'GL U lapses 19 April without renewal — H-D2 CONFIRMED, Case D ESCALATING CRITICAL'),
    ('OFAC issues partial successor (different GL number) — H-D3 CONFIRMED',
     'India transacts with Iran in violation of lapsed OFAC authorisation — secondary sanctions trigger'),
    ('Islamabad second round produces back-channel deal unlocking GL U renewal',
     'UCO Bank rupee-rial channel confirmed active post-GL U lapse — tripwire activated'),
], 'GL U renewal on OFAC = H-D2 CONTRADICTED, Case D de-escalation review. '
   'GL U lapses 19 April = Case D ESCALATING CRITICAL.', styles))
story.append(Paragraph(
    '<i>Gate 5 Framing Revision Trigger: GL 134B or GL U renewal appears on OFAC register — '
    'immediate H-D2 CONTRADICTED, Case D de-escalation review. '
    'GL U lapses 19 April without replacement — Case D ESCALATING CRITICAL.</i>',
    styles['pred_note']))

story.extend(flag_block(
    'PRED-022-C', 4,
    'GL U expires 12:01 a.m. EDT 19 April 2026. Fetch OFAC selected general licenses page directly at trigger. '
    'If GL U lapses without renewal: Case D upgrades to ESCALATING CRITICAL. India OFAC exposure intensifies. '
    'Secondary sanctions tripwire (UCO Bank rupee-rial channel) activated. '
    'Window: 19 April 0001 EDT. C3: falsifiable (renewal = CONTRADICTED; lapse = CONFIRMED). '
    'Five-state: CONFIRMED (lapses/no replacement) / CONTRADICTED (renewed or replaced) / '
    'PARTIAL (partial successor) / AMBIGUOUS (OFAC page inaccessible) / UNRESOLVABLE (system outage).',
    'GL U lapse confirmed at 0001 EDT 19 April — PRED-022-C CONFIRMED.',
    styles))
story.append(hr())

# ── CASE E ────────────────────────────────────────────────────────────────
story.append(tag_table('E',
    'Saudi Aramco — Pipeline Restored 7M bpd / No New Strike / Follow-on Risk HIGH',
    'ESCALATING', 'HIGH', None, styles))
story.append(Paragraph('Heuristics: H6 (Suppressed Intersection) · H1 (Incentive Mismatch)',
    styles['heuristic_line']))
story.append(Paragraph(
    '<b>PRED-021-E: PENDING — no new strike at sweep.</b> Pipeline restored 7M bpd (12 April). '
    'Khurais 300K bpd still offline. Follow-on strike probability upgraded: <b>HIGH (65-75%)</b>.',
    styles['body']))

story.append(Paragraph('PART 1 — FACTUAL ELEMENTS', styles['section_head']))
story.append(fact_table([
    ('Saudi Ministry of Energy: East-West Pipeline restored to 7 million bpd 12 April. '
     'Manifa oilfield restored to 300,000 bpd. Khurais remains offline — 300,000 bpd still lost. '
     '1.3 million bpd aggregate war damage remains confirmed (SPA, 11 April). '
     'Arab Light liftings restricted to Yanbu only — first explicit wartime supply allocation.',
     'Saudi Ministry of Energy (Tier 1), SPA (Tier 1 / Gate 0.4: MEDIUM-HIGH). '
     'Al Jazeera (Tier 2), HouseofSaud (Tier 3). Temporal currency: 11-12 April 2026. [FACT]'),
    ('Yanbu loading berths: ~5.9 million bpd physical capacity ceiling. Cannot be expanded in weeks. '
     'No new IRGC strike on Yanbu Red Sea terminal or Petroline infrastructure confirmed '
     'between ~0730 GMT 12 April and 2334 GMT 14 April.',
     'HouseofSaud / S&P Global (Tier 3). Absence confirmed across NBC, CNN, Al Jazeera, Naval News. '
     'Gate 0.3: Absence confirmed across mandatory feeds. [FACT — absence observable]'),
    ('Post-Islamabad failure: IRGC restraint logic removed. Restored 7M bpd pipeline represents '
     'highest-value Aramco target since ceasefire. USN blockade eliminates Iranian/Russian crude from '
     'Asian markets — Yanbu now primary substitute source for ~30% of global seaborne oil trade.',
     'AtollSphere [INFERENCE] — built from Tier 1/2 infrastructure data and IRGC targeting logic. '
     'HouseofSaud (Tier 3) corroborating. Temporal currency: 13-14 April. [INFERENCE]'),
], styles))

story.append(Paragraph('PART 2 — OBSERVED INCONGRUITY', styles['section_head']))
story.append(Paragraph(
    '<b>H6 (Suppressed Intersection):</b> The restored pipeline is the single highest-value IRGC targeting '
    'option remaining in the war. A successful strike on Yanbu port loading berths (5.9M bpd physical ceiling, '
    'not expandable) would be the most severe supply shock of the conflict.',
    styles['body']))
story.append(Paragraph(
    '<b>H1 (Incentive Mismatch):</b> IRGC has structural incentive to demonstrate capability against '
    'Aramco rather than directly against USN. Displaced response — non-kinetic to USN, kinetic to '
    'Aramco — is the highest-leverage IRGC strategic option. The 8 April pumping station strike on '
    'ceasefire day demonstrates local commander can act without SNSC authorisation.',
    styles['body']))
story.append(Paragraph(
    'INFERENCE: H1 and H6 both live. H6 structurally primary; H1 informs targeting logic. '
    '[H1 SATURATION CHECK]: Both applicable here.',
    styles['infer']))

story.append(Paragraph('PART 3 — HYPOTHESIS SET', styles['section_head']))
story.append(hyp_table([
    {'heading': 'H-E1: IRGC RESTRAINT CONTINUES',
     'probability_range': '25-35%',
     'body': 'IRGC maintains non-kinetic posture through 22 April. Iran preserves Yanbu threat as '
             'negotiating leverage for second round. DOWNGRADED from Ed021 45-60% — Islamabad failure '
             'removes primary restraint logic.'},
    {'heading': 'H-E2: IRGC FOLLOW-ON YANBU/PETROLINE STRIKE — DOMINANT',
     'probability_range': '55-65%',
     'body': 'IRGC strikes Yanbu terminal or Petroline before 22 April. Trigger: Islamabad failure + '
             'blockade declaration. Restored 7M bpd pipeline = renewed high-value target. '
             'Decentralised command — local commander risk. PRED-018-E / PRED-022-D. '
             'UPGRADED from Ed021 30-45%.'},
    {'heading': 'H-E3: IRGC DISPLACED RESPONSE — ARAMCO AS USN PROXY',
     'probability_range': '10-15%',
     'body': 'IRGC responds to USN blockade via Aramco rather than USN vessels directly. '
             'Non-exclusive with H-E2. Most damaging scenario: Yanbu port berths struck, '
             '5.9M bpd ceiling degraded.'},
], styles))

story.append(Paragraph('PART 4 — TRUTH QUALITY CHECK', styles['section_head']))
story.append(Paragraph(
    '<b>Key assumption:</b> Abqaiq damage extent (ESA satellite, 8 April carry-forward) is accurate and '
    'Petroline restoration to 7M bpd is genuine. Saudi MoE has market confidence incentive. '
    'Not independently re-verified Ed022 via satellite imagery. Re-verification required Ed023.',
    styles['body']))
story.append(Paragraph(
    '<b>Fragile fact:</b> Yanbu port berth capacity ceiling ~5.9M bpd — HouseofSaud / S&P Global '
    '(Tier 3), not independently re-verified Ed022. Goldman Sachs deficit projection is Tier 2 secondary, '
    'not re-verified Ed022.',
    styles['body']))
story.append(Paragraph(
    '<b>High-impact uncertainty:</b> IRGC command authority decentralisation. The 8 April pumping station '
    'strike occurred on ceasefire day — evidence that local IRGC commander can initiate targeting without '
    'SNSC authorisation. Post-Islamabad, no ceasefire restraint signal currently sent by Tehran.',
    styles['body']))
story.append(Paragraph(
    '<b>Tier 4 dependency test:</b> H-E2 stripped of House of Saud Tier 3 — Tier 1/2 sources (SPA, '
    'Saudi MoE, Al Jazeera) independently confirm 1.3M bpd damage, pipeline restoration, and '
    'Yanbu-only allocation. H-E2 dominant assessment stands without Tier 3/4.',
    styles['body']))

story.append(Paragraph('PART 5 — DISCONFIRMATION', styles['section_head']))
story.append(disconf_table([
    ('IRGC maintains non-kinetic posture through 22 April — H-E1 dominant',
     'IRGC strikes Yanbu before 22 April — PRED-018-E / PRED-022-D CONFIRMED, Case E ESCALATING CRITICAL'),
    ('Abqaiq repair confirmed and Yanbu full operations before 22 April — PRED-018-E CONTRADICTED',
     'IRGC displaces USN response to Aramco (H-E3) — both PRED-018-E and PRED-022-D CONFIRMED simultaneously'),
], 'Any confirmed IRGC strike on Yanbu or Petroline = Case E ESCALATING CRITICAL, reframe from scratch.',
styles))
story.append(Paragraph(
    '<i>Gate 5 Framing Revision Trigger: Any confirmed IRGC strike on Yanbu or Petroline infrastructure — '
    'Case E remains ESCALATING CRITICAL, PRED-018-E and PRED-022-D CONFIRMED. Reframe from scratch.</i>',
    styles['pred_note']))

story.extend(flag_block(
    'PRED-022-D', 5,
    'Monitor IRGC kinetic posture toward Yanbu/Petroline through 22 April. Probability HIGH (65-75%). '
    'Islamabad failure removed restraint logic; pipeline restored to 7M bpd 12 April. '
    'Window: 15-22 April. C3: falsifiable (strike = PRED-018-E CONFIRMED; no strike = H-E1 reassessed). '
    'Five-state: CONFIRMED (IRGC strikes Yanbu/Petroline before 22 Apr) / '
    'CONTRADICTED (Yanbu full operations through ceasefire expiry) / '
    'PARTIAL (non-Yanbu Aramco infrastructure struck) / '
    'AMBIGUOUS (strike reported but not independently confirmed) / '
    'UNRESOLVABLE (ceasefire renewed before window closes).',
    'IRGC strike on Yanbu or Petroline confirmed — PRED-022-D CONFIRMED.',
    styles))

story.extend(flag_block(
    'PRED-022-E', 6,
    '[CROSS-CASE] Chinese-flag tanker blockade breach (Rich Starry, 13 April) may become formal '
    'US-China diplomatic incident. China has structural interest in accessing Gulf crude. '
    'Blockade enforcement gap acknowledged (Naval News/LSEG). '
    'Monitor: additional Chinese-flag breaches; USN interception of Chinese-flag vessel; Chinese formal objection. '
    'Window: through 22 April. C3: falsifiable (interception/incident = CONFIRMED; no further breaches = NON-EVENT).',
    'USN intercepts Chinese-flag vessel or China files formal diplomatic objection — PRED-022-E CONFIRMED.',
    styles))
story.append(hr())

# ── WHAT THIS BRIEF DOES NOT PROVE ────────────────────────────────────────
story.append(PageBreak())
story.append(Paragraph('WHAT THIS BRIEF DOES NOT PROVE', styles['section_head']))
story.append(hr())
for item in [
    'That the Islamabad failure is permanent — both sides have signalled continued engagement and a second round remains the dominant hypothesis.',
    'That the USN blockade will be fully enforced — early enforcement gaps (Rich Starry) are confirmed and MCM capability constraints are documented.',
    'That GL U renewal is impossible — a back-channel Iran/US interim agreement before 19 April remains a low-probability but non-zero pathway.',
    'That the East-West Pipeline is a secure bypass — IRGC has struck it once on ceasefire day and follow-on strike probability is assessed HIGH.',
    'That the Lebanon-Israel Washington framework will produce a ceasefire — Hezbollah has rejected the process and Israel has explicitly refused ceasefire discussion.',
]:
    story.append(Paragraph(f'✕  {item}', styles['not_proven']))
story.append(hr())

# ── SOURCES ───────────────────────────────────────────────────────────────
story.append(Paragraph('SOURCES', styles['section_head']))
story.append(Paragraph(
    f'All Domains · {SWEEP_STR} · Edition {EDITION} · '
    'Mandatory feeds swept per Architecture v1.2.1. Gate 0.5 upstream dependency applied. No bypass declared.',
    styles['small_bold']))
story.append(Spacer(1, 2*mm))
story.extend(source_block([
    {'name': 'OFAC Selected General Licenses Register',
     'tier': '1', 'category': 'US Government Primary',
     'incentive': 'LOW — absence is verifiable fact; no incentive to omit from official register',
     'body': 'GL 134B absence confirmed. GL U active status confirmed through 19 April. Direct fetch ofac.treasury.gov.',
     'url': 'https://ofac.treasury.gov/selected-general-licenses-issued-ofac'},
    {'name': 'CENTCOM Public Affairs',
     'tier': '1', 'category': 'US Government Primary',
     'incentive': 'MEDIUM — US has incentive to project operational success',
     'body': 'USN mine clearance / blockade announcement. DDG transit confirmed. Blockade scope confirmed.',
     'url': 'https://www.centcom.mil'},
    {'name': 'Trump Truth Social / White House',
     'tier': '1', 'category': 'US Government Primary',
     'incentive': 'HIGH — Trump statements routinely exceed confirmed facts for domestic political effect',
     'body': 'Blockade framing; post-Islamabad posture. Capability claims not load-bearing for this analysis.',
     'url': ''},
    {'name': 'US State Department',
     'tier': '1', 'category': 'Named Government Statement',
     'incentive': 'MEDIUM',
     'body': 'Lebanon-Israel Washington talks confirmed. Rubio participation. Joint statement text.',
     'url': 'https://www.state.gov'},
    {'name': 'Saudi Ministry of Energy / SPA',
     'tier': '1', 'category': 'Named Government Statement',
     'incentive': 'MEDIUM-HIGH — Aramco has regulatory disclosure obligation and market confidence incentive',
     'body': 'Pipeline restoration to 7M bpd. 1.3M bpd war damage confirmation. Arab Light Yanbu-only allocation.',
     'url': ''},
    {'name': 'TIME Magazine',
     'tier': '2', 'category': 'High-Authority Secondary',
     'incentive': 'MEDIUM',
     'body': 'Islamabad talks failure; second-round discussion; Vance and Araghchi statements post-departure.',
     'url': 'https://time.com'},
    {'name': 'CFR (Council on Foreign Relations)',
     'tier': '2', 'category': 'High-Authority Secondary',
     'incentive': 'LOW',
     'body': 'Post-Islamabad analysis; GL U / blockade contradiction analysis.',
     'url': 'https://www.cfr.org'},
    {'name': 'Al Jazeera',
     'tier': '2', 'category': 'High-Authority Secondary',
     'incentive': 'MEDIUM',
     'body': 'Lebanon death toll (2,080+); Islamabad unfolding; Israel-Lebanon talks; Hezbollah statements.',
     'url': 'https://www.aljazeera.com'},
    {'name': 'NPR',
     'tier': '2', 'category': 'High-Authority Secondary',
     'incentive': 'MEDIUM',
     'body': 'Israel-Lebanon Washington talks; Beirut correspondent reporting.',
     'url': 'https://www.npr.org'},
    {'name': 'Naval News',
     'tier': '2', 'category': 'Specialist Publication',
     'incentive': 'MEDIUM',
     'body': 'USN mine clearance staging; MCM assets; blockade enforcement gaps (Rich Starry).',
     'url': 'https://www.navalnews.com'},
    {'name': 'HouseofSaud / Conflict Pulse',
     'tier': '3', 'category': 'Specialist Analysis',
     'incentive': 'MEDIUM — specialist, no obvious distortion incentive',
     'body': 'East-West Pipeline analysis; GL U expiry; Aramco pricing; fiscal break-even; Yanbu berth capacity.',
     'url': 'https://houseofsaud.com'},
    {'name': 'Wikipedia',
     'tier': '4', 'category': 'Editorial Assembly',
     'incentive': 'LOW — editorial assembly risk acknowledged',
     'body': 'Islamabad Talks page; Hormuz Crisis page. Directional corroboration only — Leg 2 per AI-002. '
             'Cannot satisfy Gate 0.3 for forward-looking claims. Downstream of same Tier 1/2 feeds swept.',
     'url': 'https://en.wikipedia.org'},
], styles))

story.append(Spacer(1, 4*mm))
story.append(Paragraph(
    f'AtollSphere Brief · Edition {EDITION} · {SWEEP_STR} · {DATE_STR} · '
    f'build_core.py / styles.py / build_edition_{EDITION}.py · GMT primary timestamps · '
    f'12 sources · 5 cases · 6 forward flags · LS AI Systems',
    styles['footer']))

doc.build(story, onFirstPage=on_cover, onLaterPages=on_page)
print(f'Built: {path}')
```

if __name__ == "__main__":
    build()
