“””
ATOLLSPHERE · EDITION 013 · MORNING SWEEP · 09 APRIL 2026
build_edition_013.py — per-edition build script
References: build_1.1.0.py v1.1.2
GMT_NOW: 2026-04-08 23:34 UTC  (00:34 BST 09 April 2026)
“””

import datetime
from reportlab.platypus import (
SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT

# ── TIMESTAMP (v1.1.2 mandate) ───────────────────────────────────────────────

GMT_NOW = datetime.datetime(2026, 4, 8, 23, 34, 0)
BST_NOW = GMT_NOW + datetime.timedelta(hours=1)
GMT_STR = GMT_NOW.strftime(”%d %B %Y · %H:%M GMT”)
BST_STR = BST_NOW.strftime(”%H:%M BST”)

# ── COLOUR CONSTANTS ─────────────────────────────────────────────────────────

NAVY      = colors.HexColor(”#1B2A4A”)
TEAL      = colors.HexColor(”#3DBDB0”)
CHARCOAL  = colors.HexColor(”#3D3D3D”)
MID_GREY  = colors.HexColor(”#8A8A8A”)
LIGHT_BG  = colors.HexColor(”#F2F2F0”)
ROW_ALT   = colors.HexColor(”#F7F9FB”)
WHITE     = colors.white
RED_TAG   = colors.HexColor(”#B83232”)
AMBER     = colors.HexColor(”#C47D1A”)
GREEN_TAG = colors.HexColor(”#2C7A4B”)
PURPLE    = colors.HexColor(”#6B3FA0”)
DK_GREEN  = colors.HexColor(”#4A7C4E”)
MARGIN    = 18 * mm
PAGE_W, PAGE_H = A4

# ── STYLES ───────────────────────────────────────────────────────────────────

def make_styles():
s = {}
s[‘cover_title’] = ParagraphStyle(‘cover_title’,
fontName=‘Helvetica-Bold’, fontSize=18, textColor=NAVY,
alignment=TA_CENTER, spaceAfter=6)
s[‘cover_sub’] = ParagraphStyle(‘cover_sub’,
fontName=‘Helvetica’, fontSize=10, textColor=CHARCOAL,
alignment=TA_CENTER, spaceAfter=4)
s[‘cover_meta’] = ParagraphStyle(‘cover_meta’,
fontName=‘Helvetica’, fontSize=8.5, textColor=CHARCOAL,
alignment=TA_CENTER, spaceAfter=3)
s[‘cover_label’] = ParagraphStyle(‘cover_label’,
fontName=‘Helvetica-Bold’, fontSize=7.5, textColor=MID_GREY,
alignment=TA_CENTER)
s[‘cover_value’] = ParagraphStyle(‘cover_value’,
fontName=‘Helvetica-Bold’, fontSize=9, textColor=NAVY,
alignment=TA_CENTER, spaceAfter=2)
s[‘section_head’] = ParagraphStyle(‘section_head’,
fontName=‘Helvetica-Bold’, fontSize=7.5, textColor=TEAL,
spaceBefore=8, spaceAfter=3)
s[‘body’] = ParagraphStyle(‘body’,
fontName=‘Helvetica’, fontSize=8.5, textColor=CHARCOAL,
alignment=TA_JUSTIFY, spaceAfter=4, leading=12)
s[‘body_bold’] = ParagraphStyle(‘body_bold’,
fontName=‘Helvetica-Bold’, fontSize=8.5, textColor=CHARCOAL,
spaceAfter=3)
s[‘small’] = ParagraphStyle(‘small’,
fontName=‘Helvetica’, fontSize=7.5, textColor=MID_GREY, spaceAfter=2)
s[‘small_bold’] = ParagraphStyle(‘small_bold’,
fontName=‘Helvetica-Bold’, fontSize=7.5, spaceAfter=2)
s[‘hyp_head’] = ParagraphStyle(‘hyp_head’,
fontName=‘Helvetica-Bold’, fontSize=7.5, textColor=NAVY)
s[‘pred_note’] = ParagraphStyle(‘pred_note’,
fontName=‘Helvetica-Oblique’, fontSize=7.5,
textColor=MID_GREY, leftIndent=8, spaceAfter=3)
s[‘correction_note’] = ParagraphStyle(‘correction_note’,
fontName=‘Helvetica-Oblique’, fontSize=7.5,
textColor=RED_TAG, leftIndent=8, spaceAfter=3)
s[‘afc_note’] = ParagraphStyle(‘afc_note’,
fontName=‘Helvetica-Oblique’, fontSize=7.5,
textColor=RED_TAG, leftIndent=8, spaceAfter=3)
s[‘tql_head’] = ParagraphStyle(‘tql_head’,
fontName=‘Helvetica-Bold’, fontSize=7.5,
textColor=NAVY, spaceBefore=4, spaceAfter=2)
s[‘flag_head’] = ParagraphStyle(‘flag_head’,
fontName=‘Helvetica-Bold’, fontSize=8, textColor=TEAL, spaceAfter=2)
s[‘footer’] = ParagraphStyle(‘footer’,
fontName=‘Helvetica’, fontSize=6.5, textColor=MID_GREY,
alignment=TA_CENTER)
s[‘source_tier’] = ParagraphStyle(‘source_tier’,
fontName=‘Helvetica-Bold’, fontSize=7, textColor=TEAL)
s[‘infer’] = ParagraphStyle(‘infer’,
fontName=‘Helvetica-Bold’, fontSize=8.5, textColor=CHARCOAL,
spaceAfter=4, leading=12)
s[‘heuristic_line’] = ParagraphStyle(‘heuristic_line’,
fontName=‘Helvetica-Oblique’, fontSize=7, textColor=MID_GREY,
spaceAfter=4)
s[‘not_proven’] = ParagraphStyle(‘not_proven’,
fontName=‘Helvetica’, fontSize=8, textColor=CHARCOAL,
leftIndent=10, spaceAfter=3)
return s

# ── HELPERS ──────────────────────────────────────────────────────────────────

def hr(width=‘100%’):
return HRFlowable(width=width, thickness=0.5, color=TEAL,
spaceAfter=5, spaceBefore=5)

def thin_rule():
return HRFlowable(width=‘100%’, thickness=0.3,
color=colors.HexColor(’#D0D8E0’),
spaceAfter=2, spaceBefore=2)

def tag_table(case_letter, title, tag, confidence, st, styles):
tag_colors = {
‘ESCALATING’:             (RED_TAG,   WHITE),
‘ESCALATING-PROVISIONAL’: (AMBER,     WHITE),
‘DEVELOPING’:             (AMBER,     WHITE),
‘NEW’:                    (TEAL,      WHITE),
‘ELEVATED’:               (NAVY,      WHITE),
‘STABLE’:                 (GREEN_TAG, WHITE),
‘RESOLVED’:               (MID_GREY,  WHITE),
‘DE-ESCALATING’:          (DK_GREEN,  WHITE),
‘WATCH’:                  (PURPLE,    WHITE),
}
conf_map = {
‘HIGH’:       (GREEN_TAG, ‘70–90%’),
‘MEDIUM’:     (AMBER,     ‘55–70%’),
‘LOW-MEDIUM’: (AMBER,     ‘40–55%’),
‘LOW’:        (RED_TAG,   ‘25–40%’),
}
tag_bg, tag_fg = tag_colors.get(tag, (MID_GREY, WHITE))
conf_bg, conf_range = conf_map.get(confidence, (MID_GREY, ‘’))

```
case_cell = Paragraph(f'<b>CASE {case_letter}</b>',
    ParagraphStyle('cc', fontName='Helvetica-Bold', fontSize=8,
                   textColor=WHITE))
title_cell = Paragraph(f'<b>{title}</b>',
    ParagraphStyle('tc', fontName='Helvetica-Bold', fontSize=8,
                   textColor=NAVY))
tag_cell = Paragraph(f'<b>{tag}</b>',
    ParagraphStyle('tgc', fontName='Helvetica-Bold', fontSize=7.5,
                   textColor=tag_fg, alignment=TA_CENTER))
conf_cell = Paragraph(f'<b>{confidence}</b><br/><font size=6>{conf_range}</font>',
    ParagraphStyle('cfc', fontName='Helvetica-Bold', fontSize=7.5,
                   textColor=WHITE, alignment=TA_CENTER))

tbl = Table([[case_cell, title_cell, tag_cell, conf_cell]],
            colWidths=[22*mm, 95*mm, 35*mm, 22*mm])
tbl.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (0,0), NAVY),
    ('BACKGROUND', (1,0), (1,0), LIGHT_BG),
    ('BACKGROUND', (2,0), (2,0), tag_bg),
    ('BACKGROUND', (3,0), (3,0), conf_bg),
    ('VALIGN',     (0,0), (-1,-1), 'MIDDLE'),
    ('LEFTPADDING',(0,0), (-1,-1), 5),
    ('RIGHTPADDING',(0,0),(-1,-1), 5),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING',(0,0),(-1,-1), 5),
    ('LINEBELOW',  (0,0), (-1,-1), 1, TEAL),
]))
return tbl
```

def fact_table(rows, styles):
“”“rows = [(fact_text, source_attribution), …]”””
header = [
Paragraph(’<b>FACT</b>’, ParagraphStyle(‘fh’, fontName=‘Helvetica-Bold’,
fontSize=7, textColor=WHITE)),
Paragraph(’<b>SOURCE — TIER · GATE 0</b>’, ParagraphStyle(‘sh’,
fontName=‘Helvetica-Bold’, fontSize=7, textColor=WHITE)),
]
table_rows = [header]
for fact, source in rows:
table_rows.append([
Paragraph(fact, ParagraphStyle(‘fb’, fontName=‘Helvetica’,
fontSize=7.5, leading=10, textColor=CHARCOAL)),
Paragraph(source, ParagraphStyle(‘sb’, fontName=‘Helvetica-Oblique’,
fontSize=7, leading=9.5, textColor=MID_GREY)),
])
tbl = Table(table_rows, colWidths=[117*mm, 57*mm])
style = [
(‘BACKGROUND’, (0,0), (-1,0), NAVY),
(‘VALIGN’,     (0,0), (-1,-1), ‘TOP’),
(‘LEFTPADDING’,(0,0), (-1,-1), 5),
(‘RIGHTPADDING’,(0,0),(-1,-1), 5),
(‘TOPPADDING’, (0,0), (-1,-1), 4),
(‘BOTTOMPADDING’,(0,0),(-1,-1), 4),
(‘LINEBELOW’,  (0,1), (-1,-1), 0.3, colors.HexColor(’#D0D8E0’)),
]
for i in range(1, len(table_rows)):
if i % 2 == 0:
style.append((‘BACKGROUND’, (0,i), (-1,i), ROW_ALT))
tbl.setStyle(TableStyle(style))
return tbl

def hyp_table(hypotheses, styles):
“”“hypotheses = [{‘heading’: str, ‘body’: str, ‘probability_range’: str}, …]”””
n = len(hypotheses)
col_w = 174*mm / n
headers = []
bodies  = []
for h in hypotheses:
headers.append(
Paragraph(f’<b>{h[“heading”]}</b><br/>’
f’<font size=6 color="#{TEAL.hexval()[2:]}">{h[“probability_range”]}</font>’,
ParagraphStyle(‘hh’, fontName=‘Helvetica-Bold’, fontSize=7.5,
textColor=NAVY, leading=11)))
bodies.append(
Paragraph(h[‘body’],
ParagraphStyle(‘hb’, fontName=‘Helvetica’, fontSize=7.5,
leading=10, textColor=CHARCOAL)))
tbl = Table([headers, bodies], colWidths=[col_w]*n)
line_cmds = []
for i in range(1, n):
line_cmds.append((‘LINEAFTER’, (i-1,0), (i-1,-1), 0.5, TEAL))
tbl.setStyle(TableStyle([
(‘BACKGROUND’,    (0,0), (-1,0), LIGHT_BG),
(‘VALIGN’,        (0,0), (-1,-1), ‘TOP’),
(‘LEFTPADDING’,   (0,0), (-1,-1), 6),
(‘RIGHTPADDING’,  (0,0), (-1,-1), 6),
(‘TOPPADDING’,    (0,0), (-1,-1), 5),
(‘BOTTOMPADDING’, (0,0), (-1,-1), 5),
(‘BOX’,           (0,0), (-1,-1), 0.5, TEAL),
] + line_cmds))
return tbl

def disconf_table(rows, revision_trigger, styles):
header = [
Paragraph(’<b>CONFIRMS</b>’, ParagraphStyle(‘ch’, fontName=‘Helvetica-Bold’,
fontSize=7.5, textColor=GREEN_TAG)),
Paragraph(’<b>CONTRADICTS</b>’, ParagraphStyle(‘cth’, fontName=‘Helvetica-Bold’,
fontSize=7.5, textColor=RED_TAG)),
]
table_rows = [header]
for conf, contra in rows:
table_rows.append([
Paragraph(f’■ {conf}’, ParagraphStyle(‘cr’, fontName=‘Helvetica’,
fontSize=7.5, leading=10, textColor=CHARCOAL)),
Paragraph(f’■ {contra}’, ParagraphStyle(‘ctr’, fontName=‘Helvetica’,
fontSize=7.5, leading=10, textColor=CHARCOAL)),
])
tbl = Table(table_rows, colWidths=[87*mm, 87*mm])
tbl.setStyle(TableStyle([
(‘BACKGROUND’,   (0,0), (-1,0), NAVY),
(‘TEXTCOLOR’,    (0,0), (-1,0), WHITE),
(‘VALIGN’,       (0,0), (-1,-1), ‘TOP’),
(‘LEFTPADDING’,  (0,0), (-1,-1), 6),
(‘RIGHTPADDING’, (0,0), (-1,-1), 6),
(‘TOPPADDING’,   (0,0), (-1,-1), 4),
(‘BOTTOMPADDING’,(0,0), (-1,-1), 4),
(‘LINEAFTER’,    (0,0), (0,-1),  0.5, TEAL),
(‘LINEBELOW’,    (0,1), (-1,-1), 0.3, colors.HexColor(’#D0D8E0’)),
]))
return tbl

def flag_block(ref, number, body_text, gate_note, styles):
flowables = []
flowables.append(Paragraph(f’<b>FLAG {number} · {ref}</b>’,
styles[‘flag_head’]))
flowables.append(Paragraph(body_text, styles[‘body’]))
flowables.append(Paragraph(f’<i>Gate note: {gate_note}</i>’,
styles[‘pred_note’]))
return flowables

def source_block(sources, styles):
flowables = []
for i, s in enumerate(sources, 1):
flowables.append(Paragraph(
f’SOURCE {i} — {s[“name”]}’,
ParagraphStyle(‘sn’, fontName=‘Helvetica-Bold’, fontSize=7.5,
textColor=NAVY, spaceBefore=4)))
flowables.append(Paragraph(
f’TIER {s[“tier”]} — {s[“category”]}’,
styles[‘source_tier’]))
flowables.append(Paragraph(s[‘body’], styles[‘small’]))
if s.get(‘incentive’):
flowables.append(Paragraph(
f’Incentive: {s[“incentive”]}’,
ParagraphStyle(‘inc’, fontName=‘Helvetica-Oblique’,
fontSize=7, textColor=AMBER)))
if s.get(‘url’):
flowables.append(Paragraph(s[‘url’], styles[‘small’]))
flowables.append(thin_rule())
return flowables

# ── PAGE TEMPLATES ───────────────────────────────────────────────────────────

EDITION = “013”
DATE_STR = “09 APRIL 2026”
SWEEP_STR = “EVENING SWEEP”

def on_cover(canvas, doc):
canvas.saveState()
# Teal strip top
canvas.setFillColor(TEAL)
canvas.rect(0, PAGE_H - 4*mm, PAGE_W, 4*mm, fill=1, stroke=0)
# Navy footer bar
canvas.setFillColor(NAVY)
canvas.rect(0, 0, PAGE_W, 14*mm, fill=1, stroke=0)
canvas.setFont(‘Helvetica’, 6.5)
canvas.setFillColor(MID_GREY)
canvas.drawCentredString(PAGE_W/2, 5*mm,
“CONFIDENTIAL — For Editorial Review Only · AttolSphere · LS AI Systems”)
canvas.restoreState()

def on_page(canvas, doc):
canvas.saveState()
# Navy header bar
canvas.setFillColor(NAVY)
canvas.rect(0, PAGE_H - 13*mm, PAGE_W, 13*mm, fill=1, stroke=0)
canvas.setFont(‘Helvetica-Bold’, 7)
canvas.setFillColor(TEAL)
canvas.drawString(MARGIN, PAGE_H - 8*mm, “LS”)
canvas.setFillColor(WHITE)
canvas.setFont(‘Helvetica’, 6.5)
canvas.drawString(MARGIN + 8*mm, PAGE_H - 8*mm, “AI SYSTEMS”)
canvas.setFont(‘Helvetica’, 6.5)
canvas.drawRightString(PAGE_W - MARGIN, PAGE_H - 8*mm,
f”ATOLLSPHERE BRIEF · EDITION {EDITION} · {SWEEP_STR} · {DATE_STR}”)
# Light footer
canvas.setFillColor(LIGHT_BG)
canvas.rect(0, 0, PAGE_W, 9*mm, fill=1, stroke=0)
canvas.setFont(‘Helvetica’, 6.5)
canvas.setFillColor(MID_GREY)
canvas.drawCentredString(PAGE_W/2, 3*mm,
f”CONFIDENTIAL — For Editorial Review Only · AttolSphere · LS AI Systems”
f” · smarter ai prediction systems · Page {doc.page}”)
canvas.restoreState()

# ── BUILD ────────────────────────────────────────────────────────────────────

def build():
path = “/mnt/user-data/outputs/atollsphere_brief_013_morning.pdf”
doc = SimpleDocTemplate(path, pagesize=A4,
leftMargin=MARGIN, rightMargin=MARGIN,
topMargin=18*mm, bottomMargin=14*mm)
styles = make_styles()
story  = []

```
# ── COVER ─────────────────────────────────────────────────────────────────
story.append(Spacer(1, 28*mm))

# Stats row
stats = Table([[
    Paragraph(f'<b>EDITION</b>', styles['cover_label']),
    Paragraph(f'<b>DATE</b>',    styles['cover_label']),
    Paragraph(f'<b>SWEEP</b>',   styles['cover_label']),
    Paragraph(f'<b>DAY</b>',     styles['cover_label']),
    Paragraph(f'<b>STATUS</b>',  styles['cover_label']),
],[
    Paragraph(f'<b>{EDITION}</b>',          styles['cover_value']),
    Paragraph(f'<b>{DATE_STR}</b>',          styles['cover_value']),
    Paragraph(f'<b>{SWEEP_STR}</b>',         styles['cover_value']),
    Paragraph(f'<b>39 OF THE IRAN WAR</b>',  styles['cover_value']),
    Paragraph(f'<b>ESCALATING (DOMINANT)</b>', styles['cover_value']),
]], colWidths=[35*mm]*5)
stats.setStyle(TableStyle([
    ('ALIGN',        (0,0), (-1,-1), 'CENTER'),
    ('VALIGN',       (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING',   (0,0), (-1,-1), 4),
    ('BOTTOMPADDING',(0,0), (-1,-1), 4),
    ('LINEABOVE',    (0,0), (-1,0),  0.5, TEAL),
    ('LINEBELOW',    (0,-1),(-1,-1), 0.5, TEAL),
]))
story.append(stats)
story.append(Spacer(1, 10*mm))

story.append(Paragraph(
    "Ceasefire Day 1: Truce Announced,<br/>Lebanon Excluded, Hormuz Still Closed",
    styles['cover_title']))
story.append(Spacer(1, 8*mm))

# Case/flag counts
counts = Table([[
    Paragraph('<b>6</b><br/><font size=7>CASES</font>',
        ParagraphStyle('cnt', fontName='Helvetica-Bold', fontSize=20,
                       textColor=NAVY, alignment=TA_CENTER)),
    Paragraph('<b>3</b><br/><font size=7>ESCALATING</font>',
        ParagraphStyle('cnt2', fontName='Helvetica-Bold', fontSize=20,
                       textColor=RED_TAG, alignment=TA_CENTER)),
    Paragraph('<b>2</b><br/><font size=7>DEVELOPING</font>',
        ParagraphStyle('cnt3', fontName='Helvetica-Bold', fontSize=20,
                       textColor=AMBER, alignment=TA_CENTER)),
    Paragraph('<b>3</b><br/><font size=7>FORWARD FLAGS</font>',
        ParagraphStyle('cnt4', fontName='Helvetica-Bold', fontSize=20,
                       textColor=TEAL, alignment=TA_CENTER)),
]], colWidths=[43.5*mm]*4)
counts.setStyle(TableStyle([
    ('ALIGN',  (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('LINEAFTER', (0,0), (2,0), 0.5, colors.HexColor('#D0D8E0')),
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
    "Edition 013 opens on the first full day of a fragile two-week US-Iran ceasefire, "
    "announced by Trump on 8 April approximately two hours before his self-imposed deadline. "
    "The ceasefire was brokered by Pakistan and accepted by Iran on the basis of Trump describing "
    "Iran's 10-point plan as 'a workable basis on which to negotiate.' The truce is immediately "
    "under strain on three fronts: (1) Israel has declared Lebanon excluded from the ceasefire "
    "and conducted its largest Beirut strikes of the conflict on 8 April; (2) Iranian missiles "
    "and drones continued striking Gulf states for hours after the ceasefire announcement — "
    "94 drones and 30 missiles recorded across Kuwait, UAE, Bahrain, Qatar, and Saudi Arabia; "
    "(3) Lavan Island oil refinery and Sirri Island crude facilities were struck at approximately "
    "06:30 GMT on 8 April — eight hours into the ceasefire — with no party claiming "
    "responsibility. Iran has framed both (2) and (3) as ceasefire violations. The IRGC warned "
    "it retains its 'finger on the trigger.' Islamabad talks are confirmed for 10 April, "
    "with Vance leading the US delegation and Ghalibaf leading Iran's.",
    styles['body']))

# Prediction log update — italics grey
story.append(Paragraph(
    "<i>Prediction Log update — PRED-012-A: Trump stated on 8 April 'there will be no enrichment "
    "of uranium' — Tier 1 named statement. Window specified pre-Islamabad public position. "
    "PRED-012-A status: PARTIAL. C3 satisfied; formal enrichment framework for talks not yet "
    "confirmed. No PMM triggered.</i>",
    styles['pred_note']))
story.append(Paragraph(
    "<i>Prediction Log update — PRED-012-B: Hezbollah reportedly halted fire early 8 April "
    "(Reuters — Tier 2). No formal Al Manar / Al Mayadeen statement confirmed at sweep time "
    "(23:34 GMT). Window open until 09 April 17:00 GMT. Status: PENDING.</i>",
    styles['pred_note']))

story.append(hr())

# ── CASE A ────────────────────────────────────────────────────────────────
story.append(tag_table('A',
    'Islamabad Talks / Iran-US Nuclear & Peace Framework',
    'DEVELOPING', 'MEDIUM', None, styles))
story.append(Paragraph(
    'Heuristics: H1 (Incentive Mismatch) · H2 (Timing Convergence) · H4 (Narrative vs Outcome Gap) · H5 (Structural Contradiction)',
    styles['heuristic_line']))

story.append(Paragraph('PART 1 — FACTUAL ELEMENTS', styles['section_head']))
story.append(fact_table([
    ("US-Iran two-week ceasefire announced by Trump ~22:00 GMT 8 April; contingent on 'complete, immediate and safe opening' of Hormuz.",
     "Trump Truth Social — Tier 1 · 0.1✓ 0.2✓ 0.3✓ · 0.4 Incentive: HIGH — frames as 'total victory'; self-serving. Gate 0.2 mandatory."),
    ("Iran SNSC confirmed ceasefire on basis of 10-point plan. Araghchi: 'safe passage through Hormuz will be possible through coordination with Iran's Armed Forces and with due consideration of technical limitations.'",
     "SNSC via WANA / Araghchi X — Tier 1 · 0.4 Incentive: HIGH — Iran frames as forcing US to accept its plan. Competing primary. Downgraded: Tier 1 → Tier 2 for calibration (HIGH incentive, competing primary per Gate 0.2)."),
    ("Islamabad talks confirmed 10 April. Vance (+ Witkoff, Kushner) leading US delegation; Ghalibaf leading Iran. White House confirmed via Leavitt presser; previous reports had suggested Friday.",
     "White House / Leavitt — Tier 1 · ISNA — Tier 2 · Times of Israel — Tier 2 · 0.4 Incentive: LOW-MEDIUM."),
    ("Trump 8 April: 'There will be no enrichment of uranium' and US will 'dig up and remove all of the deeply buried Nuclear Dust.' Also: 'We are, and will be, talking Tariff and Sanctions relief with Iran.'",
     "Trump Truth Social — Tier 1 · 0.4 Incentive: HIGH — domestic audience signalling. Enrichment absolute; sanctions relief comment in tension with maximalist framing."),
    ("Iran SNSC (via Tasnim) characterises ceasefire as US accepting: Iranian Hormuz control, enrichment rights, lifting all UNSC/IAEA resolutions, US force withdrawal, full compensation.",
     "Tasnim (IRGC-linked) — Tier 3 · TQL WARNING [v1.1.2]: Fragile fact — Tier 3 source. Tag decision held pending Part 4."),
    ("Iran UN Ambassador Bahreini (Reuters): 'We are not putting any trust in the other side. Our military forces are keeping their preparedness.'",
     "Reuters — Tier 2 · 0.4 Incentive: MEDIUM — diplomatic signalling for domestic and international audience."),
    ("Vance: ceasefire is a 'fragile truce'; Lebanon 'not included'; warned Iran of 'serious consequences' if deal falls apart.",
     "NBC News live blog / White House — Tier 1/2 · 0.4 Incentive: MEDIUM."),
], styles))

story.append(Paragraph('PART 2 — OBSERVED INCONGRUITY', styles['section_head']))
story.append(Paragraph(
    "<b>H1 (Incentive Mismatch):</b> Both sides claim the ceasefire as victory on irreconcilable terms. "
    "Trump says Iran capitulated; Iran's SNSC says it forced the US to accept its 10-point plan. "
    "Both cannot simultaneously be true. The incentive for both parties to project domestic strength "
    "is maximal. The ceasefire text — not yet publicly confirmed in binding form — is the only arbiter, "
    "and it has not been released.",
    styles['body']))
story.append(Paragraph(
    "<b>H2 (Timing Convergence):</b> The ceasefire was struck approximately 90 minutes before Trump's "
    "own publicly stated deadline. The extreme time compression produced an agreement before either "
    "party had resolved core disputes — Lebanon scope, Hormuz control modalities, enrichment. "
    "Agreements reached under artificial deadline pressure with unresolved core disputes have a "
    "documented pattern of rapid breakdown.",
    styles['body']))
story.append(Paragraph(
    "<b>H5 (Structural Contradiction):</b> Iran's 10-point plan includes Iranian control and fee "
    "collection at Hormuz. Trump stated the ceasefire is contingent on 'complete, immediate and safe "
    "opening' of Hormuz. These two conditions are structurally incompatible unless 'opening' is "
    "defined to include Iranian-administered toll passage — which no US official has confirmed.",
    styles['body']))
story.append(Paragraph(
    "<b>AFC:</b> The fact most weakening the current framing — Iran's IRGC explicitly continued "
    "Operation True Promise 4 wave-numbering through and past the ceasefire without any reference "
    "to a suspension. An organisation that does not acknowledge the ceasefire in its own operational "
    "sequencing is not bound by it in practice.",
    styles['afc_note']))
story.append(Paragraph(
    "INFERENCE: The ceasefire is real as a political artefact — both principals have stated it. "
    "It is not yet real as an operational outcome. The Islamabad talks on 10 April will be the first "
    "test of whether the definitional gaps on Lebanon, Hormuz modalities, and enrichment are "
    "bridgeable, or whether the ceasefire is a framework for a second breakdown.",
    styles['infer']))
story.append(Paragraph(
    "Domain quality: Evidence supports conclusion structurally. Multiple Tier 1 sources with "
    "conflicting characterisations. Gap between political announcements and operational reality "
    "is documented, not inferred.",
    styles['small']))

story.append(Paragraph('PART 3 — HYPOTHESIS SET', styles['section_head']))
story.append(hyp_table([
    {'heading': 'HYPOTHESIS A — Workable Framework',
     'probability_range': '45–55%',
     'body': 'Iran and US have privately agreed on enough points that Islamabad produces a draft framework. '
             'Enrichment is bridged through procedural language. Lebanon handled in parallel track. '
             'Hormuz opens within 48h of Islamabad. Ceasefire holds for full two weeks.'},
    {'heading': 'HYPOTHESIS B — Structural Collapse',
     'probability_range': '45–55%',
     'body': 'Lebanon exclusion triggers Iranian exit from deal. Lavan/Sirri attribution dispute or '
             'second strike breaks ceasefire before Islamabad. IRGC operational autonomy produces '
             'action Tehran cannot contain. Two-week window expires without binding framework.'},
], styles))

story.append(Paragraph('PART 4 — TRUTH QUALITY CHECK', styles['section_head']))
story.append(Paragraph(
    '<b>TQL WARNING [v1.1.2]:</b> Fragile fact sourced from Tier 3 (Tasnim/SNSC characterisation '
    'of what US accepted). Tag decision is an analytical judgement. Automatic tag changes are prohibited.',
    styles['afc_note']))
story.append(Paragraph(
    '<b>Assumptions:</b> (1) Araghchi retains authority to bind Iran\'s armed forces — IRGC autonomous '
    'command structure (documented, ACLED) makes this assumption fragile. '
    '(2) Trump will not issue a new ultimatum before 10 April in response to ongoing Gulf attacks or Lavan strikes.',
    styles['body']))
story.append(Paragraph(
    '<b>Fragile fact:</b> Iran\'s SNSC claim that the US accepted all 10 points "in principle" — '
    'Source: Tasnim — Tier 3 — Risk: If false, Iran enters Islamabad with publicly stated '
    'expectations the US has not accepted, producing immediate breakdown.',
    styles['body']))
story.append(Paragraph(
    '<b>High-impact uncertainty:</b> Whether Trump\'s absolute "no enrichment" position and Iran\'s '
    'demand for enrichment rights can be reconciled through procedural language. This is the single '
    'binary that determines whether a permanent agreement is possible — Impact if unresolved: '
    'entire Islamabad framework collapses on first substantive session.',
    styles['body']))

story.append(Paragraph('PART 5 — DISCONFIRMATION', styles['section_head']))
story.append(disconf_table([
    ("Trump called Iran's plan 'workable basis' — language upgrade from 'significant step' (6 April)",
     "Trump simultaneously stated 'no enrichment' as absolute; Iran's plan explicitly includes enrichment rights"),
    ("Both delegations confirmed for Islamabad — logistics proceeding",
     "IRGC continued wave-numbering through ceasefire; did not acknowledge suspension"),
    ("Araghchi confirmed Hormuz safe passage 'possible through coordination'",
     "Coordination language = Iranian control language; not 'complete, immediate and safe opening'"),
], "If Islamabad talks suspended, postponed, or either delegation withdraws before formal session — full reframe required.", styles))
story.append(Paragraph(
    '<i>Gate 5 Framing Revision Trigger: If either delegation withdraws before Islamabad session begins — reframe from scratch.</i>',
    styles['pred_note']))

story.extend(flag_block('PRED-013-A', 1,
    "Iran's delegation at Islamabad will formally table a written version of the 10-point plan "
    "explicitly including uranium enrichment rights, causing the US to issue a public statement "
    "that enrichment is a 'red line' before talks conclude on 10 April.",
    "Falsification: Iran tables plan omitting enrichment language, OR talks conclude without US red-line statement. "
    "C1✓ C2✓ C3✓ C4✓ C5✓ — resolves whether Islamabad is substantive negotiation or face-saving delay.",
    styles))
story.append(hr())

# ── CASE B ────────────────────────────────────────────────────────────────
story.append(tag_table('B',
    'Hezbollah / Lebanon Ceasefire Scope',
    'ESCALATING', 'HIGH', None, styles))
story.append(Paragraph(
    'Heuristics: H1 (Incentive Mismatch) · H3 (Beneficiary Asymmetry) · H5 (Structural Contradiction)',
    styles['heuristic_line']))

story.append(Paragraph('PART 1 — FACTUAL ELEMENTS', styles['section_head']))
story.append(fact_table([
    ("Netanyahu: ceasefire 'does not include Lebanon.' IDF launched 'largest coordinated strike' of current conflict 8 April — 100+ Hezbollah targets. Lebanese Red Cross: 80+ killed, 200+ wounded in Beirut alone.",
     "Netanyahu X — Tier 1 · Lebanese Red Cross — Tier 2 · 0.4 Incentive: HIGH for Netanyahu — Lebanon exclusion serves Israeli operational goal. Downgraded to Tier 2 for calibration."),
    ("Pakistan PM Sharif: ceasefire 'effective immediately everywhere, including Lebanon and elsewhere.'",
     "Sharif X — Tier 1 · 0.4 Incentive: MEDIUM — Pakistan has invested mediator credibility."),
    ("Iran SNSC 10-point plan includes 'stopping the war on all fronts, including against the heroic Lebanese Islamic resistance.' IRGC threatened 'regret-inducing response' if Lebanon strikes continue.",
     "SNSC via Tasnim — Tier 3 · IRGC Telegram — Tier 3 · TQL WARNING [v1.1.2]: Tier 3 sources. Tag decision held."),
    ("Vance: 'I think the Iranians thought that the ceasefire included Lebanon, and it just didn't. We never made that promise.'",
     "NBC News live blog — Tier 1/2 · 0.4 Incentive: MEDIUM — frames Iran as misunderstanding; consistent with US legal separation of Lebanon track."),
    ("Hezbollah reportedly halted fire early 8 April per Reuters. No formal statement at sweep. 'Expected to issue formal statement in due course.' PRED-012-B window open until 09 April 17:00 GMT.",
     "Reuters — Tier 2 · 0.1: Status unconfirmed at 23:34 GMT."),
    ("Lebanon health ministry: 89 killed, 700 wounded in Israeli strikes 8 April. Israel: military chief 'will continue to utilise every operational opportunity' against Hezbollah.",
     "Lebanon health ministry — Tier 2 · IDF statement — Tier 1 · 0.4 Incentive: LOW for health ministry figures."),
], styles))

story.append(Paragraph('PART 2 — OBSERVED INCONGRUITY', styles['section_head']))
story.append(Paragraph(
    "<b>H5 (Structural Contradiction):</b> The ceasefire cannot simultaneously exclude Lebanon "
    "(Netanyahu, Vance) and include Lebanon (Pakistan, France, Iran). These are mutually exclusive "
    "legal characterisations of the same document. The contradiction is not interpretive — it is definitional.",
    styles['body']))
story.append(Paragraph(
    "<b>H3 (Beneficiary Asymmetry):</b> Hezbollah is in a strategic trap (Israel Hayom analysis, 8 April): "
    "if it honours the ceasefire it abandons its stated demands; if it does not, it faces Israel alone "
    "without Iranian military backing. The party gaining most from Lebanon's exclusion is Israel — "
    "continued operational freedom against Hezbollah while US suspends Iran strikes.",
    styles['body']))
story.append(Paragraph(
    "<b>AFC:</b> Fact most weakening the ESCALATING tag — Hezbollah reportedly halted fire early "
    "8 April without a formal statement, suggesting operational compliance even without public commitment. "
    "If Hezbollah is de facto honouring the ceasefire despite Israeli strikes, ESCALATING may be "
    "premature for this case specifically.",
    styles['afc_note']))
story.append(Paragraph(
    "INFERENCE: Lebanon is the immediate fracture line of the ceasefire. Israel will not stop strikes; "
    "Iran has built cessation of Lebanon attacks into its 10-point plan; Hezbollah has not formally "
    "committed either way. The Islamabad talks on 10 April are the only venue where Lebanon scope "
    "can be addressed — and they open with this unresolved.",
    styles['infer']))
story.append(Paragraph(
    "Domain quality: Evidence supports conclusion structurally. Four primary parties characterise "
    "the same agreement differently. This is not ambiguity — it is documented definitional disagreement.",
    styles['small']))

story.append(Paragraph('PART 3 — HYPOTHESIS SET', styles['section_head']))
story.append(hyp_table([
    {'heading': 'HYPOTHESIS A — Lebanon Forced Into Separate Track',
     'probability_range': '35–45%',
     'body': 'Islamabad talks produce a Lebanon sub-framework. Hezbollah de facto observes ceasefire '
             'while negotiations proceed. Israel reduces Beirut strike tempo under US pressure. '
             'Lebanon scope resolved in Islamabad Phase 2 language.'},
    {'heading': 'HYPOTHESIS B — Lebanon Breaks the Ceasefire',
     'probability_range': '55–65%',
     'body': 'Israel continues strikes at current tempo. IRGC executes threatened "regret-inducing '
             'response." Iran formally exits ceasefire citing Lebanon violation. Islamabad talks '
             'suspended or begin under active hostilities. Ceasefire collapses within 72h.'},
], styles))

story.append(Paragraph('PART 4 — TRUTH QUALITY CHECK', styles['section_head']))
story.append(Paragraph(
    '<b>Assumptions:</b> (1) Hezbollah remains operationally deferential to Iran\'s political '
    'leadership — its autonomous command capability post-2024 weakening makes this uncertain. '
    '(2) Israel will not conduct a ground operation in Lebanon during the two-week window.',
    styles['body']))
story.append(Paragraph(
    '<b>Fragile fact:</b> Hezbollah "halted fire" 8 April — Source: Reuters — Tier 2 — '
    'Risk: Single-outlet characterisation without Hezbollah primary confirmation. '
    'PRED-012-B window still open.',
    styles['body']))
story.append(Paragraph(
    '<b>High-impact uncertainty:</b> Whether the US privately assured Iran that Israel would '
    'reduce Lebanon operations — and whether Netanyahu was informed. '
    'Impact if unresolved: determines whether the ceasefire breakdown is a misunderstanding '
    'or a deliberate Israeli freelancing decision.',
    styles['body']))

story.append(Paragraph('PART 5 — DISCONFIRMATION', styles['section_head']))
story.append(disconf_table([
    ("Hezbollah halted fire early 8 April per Reuters — de facto operational compliance",
     "No formal Hezbollah statement — PRED-012-B window still open at sweep"),
    ("Macron, Pakistan, Egypt, France all state Lebanon IS included — political pressure on Israel building",
     "Netanyahu doubled down 8 April — IDF chief stated will 'utilise every operational opportunity'"),
    ("Lebanon foreign ministry welcomed ceasefire — government seeks inclusion",
     "Israel issued evacuation order for Tyre 8 April — strike operations continuing"),
], "If Iran formally withdraws from ceasefire citing Lebanon — reframe entire architecture. All cases re-evaluated.", styles))
story.append(Paragraph(
    '<i>Gate 5 Framing Revision Trigger: Iranian formal withdrawal from ceasefire citing Lebanon violation — reframe from scratch.</i>',
    styles['pred_note']))

story.extend(flag_block('PRED-013-B', 2,
    "Hezbollah will issue a formal statement by 09 April 17:00 GMT stating it will not "
    "observe the ceasefire unless Israel halts Lebanon strikes — falling short of PRED-012-B "
    "window which required a ceasefire adherence statement.",
    "Falsification: Hezbollah issues statement of adherence to ceasefire OR issues no statement before window closes. "
    "C1✓ C2✓ C3✓ C4✓ C5✓ — differentiates between de facto compliance and active rejection.",
    styles))
story.append(hr())

# ── CASE C ────────────────────────────────────────────────────────────────
story.append(tag_table('C',
    'Strait of Hormuz — Transit Volume & Control Modalities',
    'ESCALATING', 'HIGH', None, styles))
story.append(Paragraph(
    'Heuristics: H1 (Incentive Mismatch) · H4 (Narrative vs Outcome Gap) · H5 (Structural Contradiction)',
    styles['heuristic_line']))

story.append(Paragraph('PART 1 — FACTUAL ELEMENTS', styles['section_head']))
story.append(fact_table([
    ("Bloomberg ship-tracking: just 3 ships observed leaving Hormuz on 8 April. Normal volume: ~135 ships/day. 800+ freighters stuck inside Gulf. Iranian media: passage for tankers remains blocked after Lebanon attacks.",
     "Bloomberg — Tier 2 · 0.1✓ Current as of sweep. 0.4 Incentive: LOW — Bloomberg tracking data, not advocacy."),
    ("Maersk: 'The ceasefire may create transit opportunities, but it does not yet provide full maritime certainty.' Hapag-Lloyd CEO: 'too early to judge' — estimates 6 weeks to normal network even if some vessels clear soon. ~1,000 merchant ships stuck in Gulf.",
     "Euronews / Maersk statement — Tier 2 · Hapag-Lloyd CEO — Tier 2 · 0.4 Incentive: LOW."),
    ("Araghchi: safe passage 'possible through coordination with Iran's Armed Forces and with due consideration of technical limitations.' Regional officials: Iran and Oman expected to charge transit fees.",
     "Araghchi X — Tier 1 · Euronews — Tier 2 · 0.4 Incentive: HIGH — 'coordination' and 'technical limitations' language preserves Iranian gating authority."),
    ("Windward data (IndexBox): 11 ships through Hormuz on 5 April. Much traffic linked to Iran's own exports. Omani corridor emerging as alternative — consistent small daily traffic.",
     "IndexBox / Windward — Tier 2 · 0.1: Data from 5 April — 4 days prior to sweep. Flag: STATUS AS OF 05 APRIL GMT — VERIFY."),
    ("Trump: ceasefire contingent on 'complete, immediate and safe opening' of Hormuz. IRGC naval commander: Hormuz will 'never return to its previous state' for US and Israel.",
     "Trump Truth Social — Tier 1 · IRGC statement via Press TV — Tier 3 · 0.2: Competing primaries. Separate rows."),
], styles))

story.append(Paragraph('PART 2 — OBSERVED INCONGRUITY', styles['section_head']))
story.append(Paragraph(
    "<b>H5 (Structural Contradiction):</b> Trump's ceasefire condition requires 'complete, immediate "
    "and safe opening.' Araghchi's confirmation requires 'coordination with Iran's Armed Forces' and "
    "accounts for 'technical limitations.' Proposed transit fees further contradict free-passage "
    "framing. These are irreconcilable characterisations of what Hormuz compliance means.",
    styles['body']))
story.append(Paragraph(
    "<b>H1 (Incentive Mismatch):</b> Iran's IRGC naval commander stated Hormuz will 'never return "
    "to its previous state' — a permanent strategic doctrine change, not a temporary wartime posture. "
    "If this reflects actual policy rather than rhetoric, the ceasefire's central condition cannot "
    "be met even if Iran wishes to comply.",
    styles['body']))
story.append(Paragraph(
    "<b>AFC:</b> The fact most weakening the ESCALATING tag — major container carriers successfully "
    "passed through Hormuz in late March 2026 (maritimenews.com), suggesting the strait is not "
    "physically impassable but operationally gated. If Iran uses 'coordination' to grant selective "
    "passage, it retains control while claiming compliance — a possible face-saving resolution.",
    styles['afc_note']))
story.append(Paragraph(
    "INFERENCE: Hormuz is not physically closed — it is franchise-operated by Iran. The ceasefire "
    "condition as stated by Trump (complete, immediate, safe opening) is incompatible with the "
    "condition as accepted by Iran (coordination-gated passage with potential fees). This gap "
    "will surface at Islamabad on 10 April as the first operational test of the ceasefire's terms.",
    styles['infer']))
story.append(Paragraph(
    "Domain quality: Evidence supports conclusion structurally. Bloomberg tracking data, carrier "
    "statements, and competing official characterisations all documented.",
    styles['small']))

story.append(Paragraph('PART 3 — HYPOTHESIS SET', styles['section_head']))
story.append(hyp_table([
    {'heading': 'HYPOTHESIS A — Coordination-Gated Opening (Partial)',
     'probability_range': '50–60%',
     'body': 'Iran operationally permits passage for non-US/Israel-linked vessels under "coordination" '
             'framework. Volume rises from ~3/day toward 30–50/day within 72h. '
             'Trump accepts this as compliance; IRGC retains de facto gating authority. '
             'Fee structure quietly drops or is deferred to final agreement.'},
    {'heading': 'HYPOTHESIS B — Hormuz Remains Effectively Closed',
     'probability_range': '40–50%',
     'body': 'Lebanese attacks continue → Iran suspends Hormuz coordination. '
             'IRGC operational autonomy prevents political leadership from implementing passage. '
             'Volume remains <10 ships/day through Islamabad window. '
             'Ceasefire condition unmet; Trump faces pressure to reimpose deadline.'},
], styles))

story.append(Paragraph('PART 4 — TRUTH QUALITY CHECK', styles['section_head']))
story.append(Paragraph(
    '<b>Assumptions:</b> (1) IRGC naval forces will follow political leadership direction on '
    'Hormuz — autonomous command structure documented by ACLED makes this uncertain. '
    '(2) Iran and Oman transit fee plan has not already been operationalised before Islamabad.',
    styles['body']))
story.append(Paragraph(
    '<b>Fragile fact:</b> Windward volume data showing 11 ships on 5 April — Source: IndexBox/Windward — Tier 2 — '
    'Risk: Data is 4 days old; post-ceasefire volume may have shifted significantly. '
    'Bloomberg 3-ship figure (8 April) is more current but covers only first hours post-announcement.',
    styles['body']))
story.append(Paragraph(
    '<b>High-impact uncertainty:</b> Whether IRGC naval command will operationally honour '
    'political leadership\'s Hormuz coordination commitment. '
    'Impact if unresolved: determines whether ceasefire condition is met or broken within 24h of Islamabad.',
    styles['body']))

story.append(Paragraph('PART 5 — DISCONFIRMATION', styles['section_head']))
story.append(disconf_table([
    ("Container carriers successfully transited Hormuz late March — physical passage possible",
     "Only 3 ships observed leaving 8 April — post-ceasefire volume remains near-zero"),
    ("Araghchi confirmed coordination mechanism exists for passage",
     "Iranian media reported tanker passage 'remains blocked' after Lebanon attacks"),
    ("Omani corridor emerging as functional alternative — diplomatic channel intact",
     "IRGC naval commander: Hormuz 'will never return to previous state' for US/Israel"),
], "Gate 5 Framing Revision Trigger: Volume <10 ships/day through 10 April AND Iran formally links Hormuz to Lebanon — reframe Hormuz as permanent strategic asset.", styles))
story.append(hr())

# ── CASE D ────────────────────────────────────────────────────────────────
story.append(tag_table('D',
    'IRGC Gulf Attacks — Post-Ceasefire Compliance',
    'ESCALATING', 'HIGH', None, styles))
story.append(Paragraph(
    'Heuristics: H1 (Incentive Mismatch) · H5 (Structural Contradiction) · H6 (Suppressed Intersection)',
    styles['heuristic_line']))

story.append(Paragraph('PART 1 — FACTUAL ELEMENTS', styles['section_head']))
story.append(fact_table([
    ("Post-ceasefire: Iran launched 94 drones and 30 missiles toward Gulf states. Kuwait: 28 drones, significant damage to Mina Al Ahmadi refinery, desalination plants. UAE: 17 ballistic missiles + 35 drones. Bahrain: 6 missiles + 31 drones. Qatar: 7 missiles/drones. Saudi Arabia: 5 ballistic missiles + 9 drones.",
     "Asharq Al-Awsat — Tier 2 · Gulf MoD official statements — Tier 1 · CNBC — Tier 2 · 0.1✓ 0.4 Incentive: LOW for MoD casualty/intercept figures."),
    ("IRGC catalogued Kuwait strikes as its '95th wave' of Operation True Promise 4 — without any reference to the ceasefire. IRGC statement: 'heeding orders of Supreme Commander' but 'fingers on trigger.'",
     "House of Saud / IRGC statement — Tier 3 · 0.4 Incentive: HIGH — IRGC framing serves autonomous operational narrative."),
    ("Lavan Island oil refinery struck ~06:30 GMT 8 April (10am local). NIORDC confirmed: 'cowardly attack by enemies.' No casualties. Fires contained. Sirri Island crude export facilities also struck. No party claimed responsibility. Israel denied. CENTCOM declined to comment.",
     "NIORDC statement — Tier 1 · AP — Tier 1 · Argus Media — Tier 2 · 0.2✓ Competing claims: UAE Mirage 2000-9 suspected (Türkiye Today — Tier 3, unverified). 0.4 Incentive: HIGH for Iran — frames as ceasefire violation to justify retaliation."),
    ("Araghchi admitted in March 2026 that IRGC units 'are now, in fact, independent and somewhat isolated, and they are acting based on general instructions given to them in advance.'",
     "Iran International citing Araghchi — Tier 2 · 0.1: March statement — carry forward. 0.3✓"),
    ("Habshan gas complex fire in Abu Dhabi after interception debris. Kuwait Petroleum Corporation facilities hit by sustained strikes for several hours. Three desalination plants damaged.",
     "CNBC — Tier 2 · Kuwait Defence Ministry — Tier 1 · 0.4 Incentive: LOW for infrastructure damage reports."),
], styles))

story.append(Paragraph('PART 2 — OBSERVED INCONGRUITY', styles['section_head']))
story.append(Paragraph(
    "<b>H5 (Structural Contradiction):</b> Iran's political leadership announced a ceasefire. "
    "Iran's IRGC simultaneously launched its 95th operational wave without referencing the ceasefire. "
    "Both cannot represent unified Iranian state behaviour. Either the ceasefire announcement was "
    "not communicated to IRGC operational commands, or IRGC units are operating on pre-issued "
    "autonomous orders that the ceasefire announcement did not cancel.",
    styles['body']))
story.append(Paragraph(
    "<b>H6 (Suppressed Intersection):</b> Araghchi's own March 2026 admission — that IRGC units "
    "are acting on 'general instructions given to them in advance' — is the structural explanation "
    "for post-ceasefire attacks. This is not deception by Tehran's political leadership. It is "
    "a command architecture problem. The ceasefire may be genuine at the political level and "
    "unenforceable at the operational level simultaneously.",
    styles['body']))
story.append(Paragraph(
    "<b>AFC:</b> Fact most weakening the ESCALATING tag — Jordan's military stated it intercepted "
    "two Iranian missiles but did not confirm these were post-ceasefire launches. Some attacks "
    "may have been in-flight before the ceasefire announcement, not ordered after it.",
    styles['afc_note']))
story.append(Paragraph(
    "INFERENCE: The IRGC's autonomous command structure is the single greatest threat to ceasefire "
    "viability. Tehran's political leadership may be unable — not merely unwilling — to halt "
    "operational units acting on pre-issued orders. This is structurally more dangerous than "
    "deliberate Iranian deception, because it cannot be resolved through negotiation alone.",
    styles['infer']))
story.append(Paragraph(
    "Domain quality: Evidence supports conclusion structurally. Araghchi's own admission, "
    "ACLED documentation, and post-ceasefire attack pattern all corroborate autonomous IRGC command.",
    styles['small']))

story.append(Paragraph('PART 3 — HYPOTHESIS SET', styles['section_head']))
story.append(hyp_table([
    {'heading': 'HYPOTHESIS A — Autonomous Command Lag',
     'probability_range': '55–65%',
     'body': 'IRGC post-ceasefire attacks reflect pre-issued autonomous orders that Tehran\'s '
             'political leadership could not recall in time. Attacks taper within 24–48h as '
             'ceasefire orders propagate through decentralised IRGC command structure. '
             'Gulf attack volume drops below 10 incidents/day by 10 April.'},
    {'heading': 'HYPOTHESIS B — Deliberate Dual-Track Strategy',
     'probability_range': '35–45%',
     'body': 'Tehran uses IRGC attacks as deliberate leverage — maintaining military pressure '
             'while political leadership negotiates. IRGC attacks are not autonomous errors '
             'but calibrated signals. Attack volume remains elevated through Islamabad. '
             'Gulf states are the pressure instrument against US to accelerate sanctions relief.'},
], styles))

story.append(Paragraph('PART 4 — TRUTH QUALITY CHECK', styles['section_head']))
story.append(Paragraph(
    '<b>Assumptions:</b> (1) Araghchi\'s March 2026 statement about IRGC autonomous operations '
    'accurately describes the current command architecture — and has not been corrected since. '
    '(2) IRGC wave-numbering is sequential and uninterrupted — not performative.',
    styles['body']))
story.append(Paragraph(
    '<b>Fragile fact:</b> "95th wave" IRGC sequencing without ceasefire reference — '
    'Source: House of Saud / IRGC Telegram — Tier 3 — '
    'Risk: IRGC communications are adversarial information; wave numbering may be inflated or performative.',
    styles['body']))
story.append(Paragraph(
    '<b>High-impact uncertainty:</b> Whether Lavan/Sirri strikes were conducted by US, Israel, '
    'UAE, or another actor — and whether Iran can distinguish this. '
    'Impact if unresolved: Iran\'s retaliatory calculus depends entirely on attribution. '
    'Wrong attribution = disproportionate Gulf response = ceasefire collapse.',
    styles['body']))

story.append(Paragraph('PART 5 — DISCONFIRMATION', styles['section_head']))
story.append(disconf_table([
    ("Araghchi admitted autonomous IRGC command structure in March — structural explanation available",
     "IRGC catalogued attacks as Wave 95 — operational continuity, not wind-down"),
    ("IRGC stated it was 'heeding orders of Supreme Commander' — acknowledges political authority",
     "IRGC also stated 'fingers on trigger' and 'respond to any aggression with higher force'"),
    ("Gulf attack volume may include pre-ceasefire in-flight missiles",
     "Kuwait strikes targeted civilian infrastructure (desalination, refinery) hours after ceasefire — not in-flight lag"),
], "Gate 5 Framing Revision Trigger: IRGC issues formal statement acknowledging ceasefire and standing down operations — reframe from ESCALATING.", styles))
story.append(hr())

# ── CASE E ────────────────────────────────────────────────────────────────
story.append(tag_table('E',
    'India Oil Waiver — Expiry 19 April / PRED-008-D',
    'DEVELOPING', 'MEDIUM', None, styles))
story.append(Paragraph(
    'Heuristics: H2 (Timing Convergence) · H3 (Beneficiary Asymmetry) · H6 (Suppressed Intersection)',
    styles['heuristic_line']))

story.append(Paragraph('PART 1 — FACTUAL ELEMENTS', styles['section_head']))
story.append(fact_table([
    ("US Treasury General License U: authorises import of Iranian crude loaded by 20 March 2026, discharged by 19 April 2026. Russian oil waiver expires 11 April 2026.",
     "Atlantic Council / OFAC — Tier 2 · 0.1✓ 0.3✓ 0.4 Incentive: LOW — regulatory document."),
    ("India's Ministry of Petroleum (X statement): 'Indian refiners have secured crude oil requirements, including from Iran; there is no payment hurdle.' First public acknowledgment of Iranian imports since 2019.",
     "India Ministry of Petroleum X — Tier 1 · Bloomberg — Tier 2 · 0.4 Incentive: MEDIUM — India managing domestic energy narrative while balancing US relationship."),
    ("Reliance Industries purchased 5 million barrels of Iranian crude at $7 premium to Brent (Kpler/Iran International). State refiners IOC, BPCL largely stayed on sidelines — compliance risk concerns.",
     "Iran International / Kpler — Tier 2 · 0.4 Incentive: LOW for pricing data."),
    ("Atlantic Council: statutory sanctions on Iranian oil remain. Removal requires congressional action. If waiver lapses or challenged in court, buyers face renewed enforcement risk.",
     "Atlantic Council — Tier 2 · 0.4 Incentive: LOW-MEDIUM — policy advocacy but factually grounded."),
    ("Ceasefire context: if Islamabad talks produce sanctions relief framework, waiver extension becomes politically easier. If talks collapse, Treasury faces pressure to let waiver lapse to restore leverage.",
     "CARRY-FORWARD INFERENCE — analytical synthesis, not single source."),
], styles))

story.append(Paragraph('PART 2 — OBSERVED INCONGRUITY', styles['section_head']))
story.append(Paragraph(
    "<b>H6 (Suppressed Intersection):</b> The India waiver and the Islamabad talks are structurally "
    "linked but not publicly connected. If the US extends the waiver past 19 April, it signals "
    "willingness to use sanctions relief as a negotiating tool — validating Iran's demand. "
    "If it lets the waiver lapse, it signals maximum pressure is resuming even during talks. "
    "This decision will be made around 15–17 April, during the Islamabad negotiation window.",
    styles['body']))
story.append(Paragraph(
    "<b>AFC:</b> Fact most weakening continued DEVELOPING status — state refiners IOC and BPCL "
    "have largely avoided Iranian crude despite the waiver, citing compliance risk. If the two "
    "largest Indian buyers are not participating, the waiver's practical effect is limited "
    "and its extension may not be politically necessary from India's perspective.",
    styles['afc_note']))
story.append(Paragraph(
    "INFERENCE: The 19 April expiry date is a policy decision point that falls inside the "
    "Islamabad two-week window. Extension signals diplomatic flexibility; lapse signals "
    "maximum pressure resumption. Watch for Treasury statement 15–17 April.",
    styles['infer']))
story.append(Paragraph(
    "Domain quality: Evidence supports conclusion at structural level. Waiver terms confirmed "
    "by OFAC/Atlantic Council. Indian buying behaviour mixed — state vs private divergence documented.",
    styles['small']))

story.append(Paragraph('PART 3 — HYPOTHESIS SET', styles['section_head']))
story.append(hyp_table([
    {'heading': 'HYPOTHESIS A — Waiver Extended',
     'probability_range': '50–60%',
     'body': 'Islamabad talks proceeding → Treasury extends General License U past 19 April '
             'as diplomatic signal. India continues purchasing. China loses near-monopsony '
             'on sanctioned Iranian crude. Waiver extension becomes part of sanctions relief '
             'framework discussion.'},
    {'heading': 'HYPOTHESIS B — Waiver Lapses',
     'probability_range': '40–50%',
     'body': 'Islamabad talks stall or collapse before 17 April. Treasury allows waiver to lapse '
             'to restore maximum pressure leverage. Indian state refiners vindicated in their '
             'caution. Iran loses $139M/day windfall estimate. Renewed enforcement risk.'},
], styles))

story.append(Paragraph('PART 4 — TRUTH QUALITY CHECK', styles['section_head']))
story.append(Paragraph(
    '<b>Assumptions:</b> (1) Treasury waiver decision is linked to Islamabad progress — '
    'no confirmed evidence this is the case; may be independent energy market decision. '
    '(2) Indian state refiners will respond to extension by increasing purchases.',
    styles['body']))
story.append(Paragraph(
    '<b>Fragile fact:</b> Iran earning "$139 million per day" from waiver window — '
    'Source: Bloomberg estimate — Tier 2 — '
    'Risk: Estimate assumes full utilisation; actual Indian buying is partial and '
    'concentrated in private sector.',
    styles['body']))
story.append(Paragraph(
    '<b>High-impact uncertainty:</b> Whether US-Iran sanctions relief framework discussed '
    'at Islamabad will address statutory sanctions — which require congressional action — '
    'or only executive-level waivers. Impact: determines whether any deal can survive '
    'a future administration or court challenge.',
    styles['body']))

story.append(Paragraph('PART 5 — DISCONFIRMATION', styles['section_head']))
story.append(disconf_table([
    ("India publicly confirmed Iranian oil purchases — political signal of engagement",
     "State refiners IOC/BPCL largely avoided Iranian crude — compliance risk concerns"),
    ("Ceasefire creates political environment for waiver extension",
     "Russian waiver expires 11 April — if not extended, signals tightening not easing"),
    ("Reliance purchased 5M barrels at premium — private sector moving",
     "Atlantic Council: statutory sanctions require congressional action — executive waiver is fragile"),
], "Gate 5 Framing Revision Trigger: Treasury announces waiver extension OR lapse before 17 April — reclassify accordingly.", styles))
story.append(hr())

# ── CASE F ────────────────────────────────────────────────────────────────
story.append(tag_table('F',
    'Lavan / Sirri Island Strikes — Attribution Dispute',
    'ESCALATING', 'LOW-MEDIUM', None, styles))
story.append(Paragraph(
    'Heuristics: H1 (Incentive Mismatch) · H3 (Beneficiary Asymmetry) · H4 (Narrative vs Outcome Gap)',
    styles['heuristic_line']))

story.append(Paragraph('PART 1 — FACTUAL ELEMENTS', styles['section_head']))
story.append(fact_table([
    ("Lavan Island oil refinery struck ~06:30 GMT 8 April (10am local), ~8 hours post-ceasefire. NIORDC confirmed: 'cowardly attack by enemies.' No casualties. 55,000 bpd facility. Fires contained. Sirri Island crude export facilities also struck. No casualty reports.",
     "NIORDC statement — Tier 1 · AP — Tier 1 · Argus Media — Tier 2 · 0.1✓ 0.4 Incentive: HIGH — NIORDC framing serves Iranian ceasefire violation narrative."),
    ("No party claimed responsibility. Israel denied involvement. CENTCOM declined to comment. UAE has not confirmed or denied.",
     "AP / Argus Media / House of Saud — Tier 1/2 · 0.2✓ All three potential actors checked: no claim, denial, silence."),
    ("UAE Mirage 2000-9 jets suspected by Iranian sources and open-source analysts. Photographs circulating — not independently verified. UAE has documented history of deniable strike operations with this aircraft (Libya 2019 UN investigation).",
     "Türkiye Today — Tier 3 · TQL WARNING [v1.1.2]: Fragile fact — Tier 3, unverified imagery. Tag decision held."),
    ("Iran's IRIB: subsequent missile and drone operations launched 'in direct response' to Lavan/Sirri strikes. Iranian state attributed to 'US-Israeli forces' (Press TV — Tier 3/state).",
     "IRIB — Tier 2 (state broadcaster) · Press TV — Tier 3 · 0.4 Incentive: HIGH — attribution serves Iranian retaliation justification."),
    ("Combined Lavan and Sirri represent ~25% of Iran's total crude export volume relative to Kharg terminal (US Naval Institute Proceedings — April 2026). Kharg itself spared in US strikes on 7 April.",
     "House of Saud / USNI Proceedings — Tier 3/2 · 0.4 Incentive: LOW for export volume figure."),
], styles))

story.append(Paragraph('PART 2 — OBSERVED INCONGRUITY', styles['section_head']))
story.append(Paragraph(
    "<b>H1 (Incentive Mismatch):</b> Three potential actors — US, Israel, UAE — all have "
    "incentive to deny. US denial would admit ceasefire violation within hours of announcement. "
    "Israel denial separates it from post-ceasefire responsibility. UAE denial preserves "
    "deniable strike doctrine established in Libya (2019). Iran has maximum incentive to "
    "attribute to US-Israel to justify Gulf retaliation.",
    styles['body']))
story.append(Paragraph(
    "<b>H3 (Beneficiary Asymmetry):</b> Striking Lavan and Sirri after Kharg was spared on "
    "7 April has a specific strategic logic — disabling backup export infrastructure Iran would "
    "use precisely because Kharg was under pressure. This benefits whoever wants to maximise "
    "Iran's economic damage during ceasefire talks. UAE motive: retaliation for sustained "
    "Gulf attacks. US motive: leverage. Israel motive: prevent Iranian economic recovery.",
    styles['body']))
story.append(Paragraph(
    "<b>AFC:</b> Fact most weakening the ESCALATING classification — the strikes may have been "
    "ordered before the ceasefire was finalised and executed after it, making them "
    "pre-ceasefire decisions with post-ceasefire timing. If so, attribution dispute is still "
    "real but the 'ceasefire violation' framing Iran is using is technically incorrect.",
    styles['afc_note']))
story.append(Paragraph(
    "INFERENCE: Attribution for Lavan/Sirri will not be resolved before Islamabad. "
    "Iran will arrive at talks asserting ceasefire violation; the US will deny it; Israel "
    "and UAE will stay silent. This attribution vacuum is the most dangerous immediate "
    "variable — it gives Iran justification to exit the ceasefire that cannot be disproved.",
    styles['infer']))
story.append(Paragraph(
    "Domain quality: Evidence supports conclusion at surface level only. Attribution "
    "is genuinely unresolved. Tier 3 UAE Mirage claim is unverified. "
    "No structural evidence for any specific actor at this time.",
    styles['small']))

story.append(Paragraph('PART 3 — HYPOTHESIS SET', styles['section_head']))
story.append(hyp_table([
    {'heading': 'HYPOTHESIS A — UAE Strike (Deniable)',
     'probability_range': '35–50%',
     'body': 'UAE Mirage 2000-9 conducted retaliatory strike on Lavan as response to sustained '
             'Gulf infrastructure attacks. Consistent with UAE deniable strike doctrine (Libya 2019). '
             'Neither US nor Israel had operational motive to strike post-ceasefire announcement. '
             'UAE had direct retaliation motive — Habshan, desalination, refinery damage.'},
    {'heading': 'HYPOTHESIS B — Pre-Ceasefire US/Israel Order, Post-Ceasefire Execution',
     'probability_range': '30–45%',
     'body': 'Strike ordered before ceasefire finalised; execution window crossed ceasefire announcement. '
             'Explains CENTCOM silence — not denial, not confirmation. '
             'Sparing Kharg on 7 April and hitting Lavan/Sirri on 8 April fits deliberate '
             'infrastructure sequencing logic.'},
], styles))

story.append(Paragraph('PART 4 — TRUTH QUALITY CHECK', styles['section_head']))
story.append(Paragraph(
    '<b>Assumptions:</b> (1) The strikes occurred after the ceasefire was communicated to '
    'relevant military commands — if not, the ceasefire violation framing collapses. '
    '(2) NIORDC fuel conservation appeal (contradicting its own "stable supply" claim) '
    'accurately indicates significant infrastructure damage.',
    styles['body']))
story.append(Paragraph(
    '<b>Fragile fact:</b> UAE Mirage 2000-9 involvement — Source: Türkiye Today / social media — Tier 3 — '
    'Risk: Unverified imagery, Iranian-sourced framing. Single Tier 3 outlet. '
    'TQL WARNING [v1.1.2]: Tier 3 fragile fact. Tag decision held pending corroboration.',
    styles['body']))
story.append(Paragraph(
    '<b>High-impact uncertainty:</b> Whether CENTCOM will ever confirm or deny. '
    'Impact if unresolved: Iran uses perpetual attribution ambiguity as ongoing justification '
    'for Gulf attacks and potential ceasefire exit throughout Islamabad window.',
    styles['body']))

story.append(Paragraph('PART 5 — DISCONFIRMATION', styles['section_head']))
story.append(disconf_table([
    ("UAE has documented deniable strike history — Libya 2019 Mirage 2000 precedent",
     "No independent verification of UAE Mirage imagery — Tier 3 source only"),
    ("Kharg spared 7 April; Lavan/Sirri hit 8 April — sequential logic fits deliberate targeting",
     "No claim of responsibility from any party — attribution remains structurally unresolved"),
    ("NIORDC fuel conservation appeal contradicts its own 'stable supply' statement — damage significant",
     "Strikes may predate ceasefire in ordering — timing alone does not confirm violation"),
], "Gate 5 Framing Revision Trigger: Named state claims responsibility OR intelligence confirmation of actor — reframe attribution entirely.", styles))
story.append(hr())

# ── WHAT THIS BRIEF DOES NOT PROVE ────────────────────────────────────────
story.append(PageBreak())
story.append(Paragraph('WHAT THIS BRIEF DOES NOT PROVE', styles['section_head']))
story.append(hr())
for item in [
    "Whether the ceasefire text has been formally agreed in writing — only verbal and social media characterisations exist at sweep time",
    "Whether the Islamabad talks on 10 April will produce a binding framework or collapse on first session",
    "Whether the Lavan/Sirri strikes were conducted by UAE, US, Israel, or a pre-ceasefire order with post-ceasefire execution",
    "Whether Hezbollah will issue a formal ceasefire statement before PRED-012-B window closes at 17:00 GMT 09 April",
    "Whether IRGC post-ceasefire Gulf attacks reflect autonomous command lag or deliberate dual-track strategy",
    "Whether the India/Iran oil waiver will be extended past 19 April — Treasury decision point ~15–17 April",
    "Whether Trump's absolute 'no enrichment' position and Iran's enrichment demand can be reconciled through procedural language",
]:
    story.append(Paragraph(f'✕  {item}', styles['not_proven']))

story.append(hr())

# ── SOURCES ───────────────────────────────────────────────────────────────
story.append(Paragraph('SOURCES', styles['section_head']))
story.append(Paragraph(f'All Domains · {SWEEP_STR} · Edition {EDITION}', styles['small_bold']))
story.append(Spacer(1, 2*mm))

sources = [
    {'name': 'TRUMP TRUTH SOCIAL / WHITE HOUSE',
     'tier': '1', 'category': 'Primary Source',
     'incentive': 'HIGH — domestic victory framing consistent across statements',
     'body': 'Ceasefire announcement. Enrichment red line. Sanctions relief acknowledgment. Lebanon exclusion (Vance/Leavitt). Tariff warning on arms suppliers.',
     'url': 'https://truthsocial.com + https://www.whitehouse.gov'},
    {'name': 'AL JAZEERA — CEASEFIRE COVERAGE',
     'tier': '2', 'category': 'High-Authority Secondary',
     'incentive': 'LOW-MEDIUM',
     'body': 'Iran-US ceasefire terms. Netanyahu Lebanon exclusion. Pakistan mediation. Iran/US concession analysis. Hezbollah strategic trap analysis.',
     'url': 'https://www.aljazeera.com/news/2026/4/8/iran-says-talks-with-us-will-begin-in-pakistans-islamabad-on-friday'},
    {'name': 'NPR — CEASEFIRE & GULF ATTACKS',
     'tier': '2', 'category': 'High-Authority Secondary',
     'incentive': 'LOW',
     'body': 'US-Iran ceasefire announcement. Gulf air defenses. Israel Lebanon strikes. Ceasefire fragility reporting.',
     'url': 'https://www.npr.org/2026/04/08/nx-s1-5777291/iran-war-updates'},
    {'name': 'CBS NEWS LIVE UPDATES',
     'tier': '2', 'category': 'High-Authority Secondary',
     'incentive': 'LOW',
     'body': 'IRGC Hermes 900 drone destroyed Fars province. IRGC ceasefire statement. Tasnim SNSC characterisation. Iran accusing Israel of ceasefire violation. Hormuz tanker suspension.',
     'url': 'https://www.cbsnews.com/live-updates/iran-trump-ceasefire-strait-hormuz-israel-war-hezbollah-continues/'},
    {'name': 'NBC NEWS LIVE BLOG',
     'tier': '1/2', 'category': 'Named Officials',
     'incentive': 'LOW',
     'body': 'Vance Lebanon exclusion statement. IRGC regret-inducing response warning. Iran UN Ambassador Bahreini. Netanyahu TV remarks.',
     'url': 'https://www.nbcnews.com/world/iran/live-blog/live-updates-iran-war-ceasefire-trump-hormuz-israel-lebanon-rcna267205'},
    {'name': 'BLOOMBERG — HORMUZ SHIPPING',
     'tier': '2', 'category': 'High-Authority Secondary',
     'incentive': 'LOW',
     'body': '3 ships observed leaving Hormuz 8 April. 800+ freighters stuck inside Gulf. Normal volume ~135/day. India Iranian oil acknowledgment.',
     'url': 'https://www.bloomberg.com/news/articles/2026-04-08/hormuz-stays-blocked-for-now-as-hundreds-of-ships-seek-escape'},
    {'name': 'TIMES OF ISRAEL / ISRAEL HAYOM',
     'tier': '2', 'category': 'High-Authority Secondary',
     'incentive': 'MEDIUM — Israeli perspective on ceasefire terms',
     'body': 'Vance leading US delegation (White House confirmed). Hezbollah strategic trap analysis. Bennett criticism of Netanyahu. Netanyahu uranium removal statement.',
     'url': 'https://www.timesofisrael.com/liveblog-april-08-2026/'},
    {'name': 'ASHARQ AL-AWSAT — GULF ATTACKS',
     'tier': '2', 'category': 'High-Authority Secondary',
     'incentive': 'LOW',
     'body': 'Official Gulf MoD figures: Kuwait 28 drones, UAE 17 missiles + 35 drones, Bahrain 6 missiles + 31 drones, Qatar 7, Saudi Arabia 5 missiles + 9 drones. Post-ceasefire timeline confirmed.',
     'url': 'https://english.aawsat.com/gulf/5260255-iran-attacks-gulf-states-continue-despite-ceasefire-announcement'},
    {'name': 'ARGUS MEDIA — LAVAN REFINERY',
     'tier': '2', 'category': 'High-Authority Secondary',
     'incentive': 'LOW',
     'body': 'NIORDC confirmed Lavan 55,000 bpd refinery attacked. No casualty. White House red line: "end of enrichment in Iran." No formal US/Israel comment on Lavan.',
     'url': 'https://www.argusmedia.com/en/news-and-insights/latest-market-news/2811249-iran-says-lavan-refinery-attacked-despite-ceasefire'},
    {'name': 'EURONEWS — SHIPPING / HORMUZ',
     'tier': '2', 'category': 'High-Authority Secondary',
     'incentive': 'LOW',
     'body': 'Maersk statement on ceasefire transit uncertainty. Hapag-Lloyd CEO 6-week recovery estimate. ~1,000 ships stuck. Iran/Oman transit fee reports.',
     'url': 'https://www.euronews.com/business/2026/04/08/shipping-companies-see-opportunities-but-seek-clarity-on-strait-of-hormuz-reopening'},
    {'name': 'ATLANTIC COUNCIL — SANCTIONS WAIVERS',
     'tier': '2', 'category': 'Policy Analysis',
     'incentive': 'LOW-MEDIUM — policy advocacy',
     'body': 'Russian waiver expires 11 April, Iranian waiver expires 19 April. Statutory sanctions require congressional action. Iran estimated $139M/day from waiver.',
     'url': 'https://www.atlanticcouncil.org/dispatches/sanctions-waivers-on-russian-and-iranian-oil-are-set-to-expire/'},
    {'name': 'IRAN INTERNATIONAL / KPLER',
     'tier': '2', 'category': 'High-Authority Secondary',
     'incentive': 'LOW for Kpler data',
     'body': 'US waiver redirecting Iranian crude from China to India. Reliance purchased 5M barrels at $7 premium to Brent. India disrupting China near-monopsony on sanctioned crude.',
     'url': 'https://www.iranintl.com/en/202603279252'},
    {'name': 'WANA NEWS AGENCY',
     'tier': '3', 'category': 'Watch / Corroboration Required',
     'incentive': 'MEDIUM — Iranian state-adjacent',
     'body': 'NIORDC Lavan refinery attack statement. Lavan fuel conservation appeal (contradicts stability claim in same release).',
     'url': 'https://wanaen.com/strikes-hit-lavan-refinery-iran-launches-retaliatory-attacks/'},
    {'name': 'HOUSE OF SAUD / CONFLICT PULSE',
     'tier': '3', 'category': 'Specialist Analysis',
     'incentive': 'LOW-MEDIUM — analytical framing',
     'body': 'IRGC autonomous command architecture analysis. Kuwait post-ceasefire strike as "95th wave." Lavan attribution analysis. NIORDC self-contradiction flagged.',
     'url': 'https://houseofsaud.com/kuwait-ceasefire-irgc-strikes/'},
    {'name': 'ACLED — CONFLICT MONITOR',
     'tier': '4', 'category': 'Editorial Assembly',
     'incentive': 'LOW',
     'body': 'Total strike count: US/Israel 3,000+ strikes on Iran. Iran 1,511 strikes on Israel and Gulf. Hezbollah capability assessment (25,000 missiles, 1,000 drones). GCC all-six-country strike pattern.',
     'url': 'https://acleddata.com/update/middle-east-special-issue-march-2026'},
    {'name': 'WIKIPEDIA — IRAN WAR TIMELINE / CEASEFIRE',
     'tier': '4', 'category': 'Editorial Assembly',
     'incentive': 'LOW',
     'body': 'Chronological timeline of ceasefire events. Islamabad Accord background. Ceasefire terms summary. Hezbollah breakdown of November 2024 ceasefire context.',
     'url': 'https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire'},
    {'name': 'ANI / THE TRIBUNE — ISLAMABAD TALKS',
     'tier': '2', 'category': 'High-Authority Secondary',
     'incentive': 'LOW',
     'body': 'Iran delegation led by Ghalibaf confirmed. US delegation Vance + Witkoff + Kushner. First in-person US-Iran negotiations since war began. Iran entering with "complete distrust."',
     'url': 'https://aninews.in/news/world/asia/iran-and-us-delegations-to-hold-talks-in-islamabad-on-april-10-in-diplomatic-push20260408134330/'},
    {'name': 'NEWSWEEK — TRUMP ENRICHMENT STATEMENT',
     'tier': '2', 'category': 'High-Authority Secondary',
     'incentive': 'LOW',
     'body': 'Trump: "no enrichment of uranium" and will "dig up and remove all deeply buried Nuclear Dust." IAEA: Iran holds ~972 lbs uranium enriched to 60%. White House single red line: "end of enrichment."',
     'url': 'https://www.newsweek.com/donald-trump-iran-bombers-nuclear-dust-uranium-11798842'},
]

story.extend(source_block(sources, styles))

# Footer note
story.append(Spacer(1, 4*mm))
story.append(Paragraph(
    f'Atollsphere Brief · Edition {EDITION} · {SWEEP_STR} · {DATE_STR} · '
    f'Template build_1.1.0.py v1.1.2 · GMT primary timestamps · '
    f'18 sources · 6 cases · 3 forward flags · LS AI Systems',
    styles['footer']))

doc.build(story, onFirstPage=on_cover, onLaterPages=on_page)
print(f"Built: {path}")
```

if **name** == ‘**main**’:
build()
