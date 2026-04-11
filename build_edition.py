"""build_edition.py — AttolSphere per-edition build template.

Copy this file to build_edition_NNN.py, fill in every placeholder marked
with [SQUARE BRACKETS], then run:

    python build_edition_NNN.py

Dependencies:
    styles.py     — colour constants and make_styles()
    build_core.py — layout helpers and make_page_callbacks()
"""

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

# ── EDITION CONSTANTS  (update for every edition) ────────────────────────────

EDITION   = "XXX"               # e.g. "014"
DATE_STR  = "DD MONTH YYYY"     # e.g. "10 APRIL 2026"
SWEEP_STR = "MORNING SWEEP"     # "MORNING SWEEP" or "EVENING SWEEP"

GMT_NOW = datetime.datetime(YYYY, M, D, HH, MM, 0)   # fill in values
BST_NOW = GMT_NOW + datetime.timedelta(hours=1)
GMT_STR = GMT_NOW.strftime("%d %B %Y \u00b7 %H:%M GMT")
BST_STR = BST_NOW.strftime("%H:%M BST")

# ── BUILD ────────────────────────────────────────────────────────────────────

def build():
    path = (
        f"/mnt/user-data/outputs/"
        f"atollsphere_brief_{EDITION}_{SWEEP_STR.lower().replace(' ', '_')}.pdf"
    )
    doc = SimpleDocTemplate(
        path, pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=18*mm, bottomMargin=14*mm,
    )
    styles = make_styles()
    story  = []
    on_cover, on_page = make_page_callbacks(EDITION, SWEEP_STR, DATE_STR)

    # ── COVER ─────────────────────────────────────────────────────────────────
    story.append(Spacer(1, 28*mm))

    stats = Table([[
        Paragraph('<b>EDITION</b>', styles['cover_label']),
        Paragraph('<b>DATE</b>',    styles['cover_label']),
        Paragraph('<b>SWEEP</b>',   styles['cover_label']),
        Paragraph('<b>DAY</b>',     styles['cover_label']),
        Paragraph('<b>STATUS</b>',  styles['cover_label']),
    ], [
        Paragraph(f'<b>{EDITION}</b>',                 styles['cover_value']),
        Paragraph(f'<b>{DATE_STR}</b>',                styles['cover_value']),
        Paragraph(f'<b>{SWEEP_STR}</b>',               styles['cover_value']),
        Paragraph('<b>[DAY N OF CONFLICT]</b>',        styles['cover_value']),
        Paragraph('<b>[DOMINANT STATUS TAG]</b>',      styles['cover_value']),
    ]], colWidths=[35*mm]*5)
    stats.setStyle(TableStyle([
        ('ALIGN',         (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING',    (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LINEABOVE',     (0, 0), (-1,  0), 0.5, TEAL),
        ('LINEBELOW',     (0,-1), (-1, -1), 0.5, TEAL),
    ]))
    story.append(stats)
    story.append(Spacer(1, 10*mm))

    story.append(Paragraph('[EDITION HEADLINE]', styles['cover_title']))
    story.append(Spacer(1, 8*mm))

    counts = Table([[
        Paragraph('<b>N</b><br/><font size=7>CASES</font>',
            ParagraphStyle('cnt',  fontName='Helvetica-Bold', fontSize=20,
                           textColor=NAVY,    alignment=TA_CENTER)),
        Paragraph('<b>N</b><br/><font size=7>ESCALATING</font>',
            ParagraphStyle('cnt2', fontName='Helvetica-Bold', fontSize=20,
                           textColor=RED_TAG, alignment=TA_CENTER)),
        Paragraph('<b>N</b><br/><font size=7>DEVELOPING</font>',
            ParagraphStyle('cnt3', fontName='Helvetica-Bold', fontSize=20,
                           textColor=AMBER,   alignment=TA_CENTER)),
        Paragraph('<b>N</b><br/><font size=7>FORWARD FLAGS</font>',
            ParagraphStyle('cnt4', fontName='Helvetica-Bold', fontSize=20,
                           textColor=TEAL,    alignment=TA_CENTER)),
    ]], colWidths=[43.5*mm]*4)
    counts.setStyle(TableStyle([
        ('ALIGN',     (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN',    (0, 0), (-1, -1), 'MIDDLE'),
        ('LINEAFTER', (0, 0), ( 2,  0), 0.5, colors.HexColor('#D0D8E0')),
    ]))
    story.append(counts)
    story.append(PageBreak())

    # ── SITUATION OVERVIEW ────────────────────────────────────────────────────
    story.append(Paragraph('SITUATION OVERVIEW', styles['section_head']))
    story.append(hr())
    story.append(Paragraph(
        f'<b>{DATE_STR} \u00b7 {SWEEP_STR} \u00b7 {GMT_STR} ({BST_STR})</b>',
        styles['small_bold']))
    story.append(Spacer(1, 2*mm))
    story.append(Paragraph('[Situation overview text.]', styles['body']))
    # Optional: append pred_note paragraphs for any open prediction log updates.
    story.append(hr())

    # ── CASE A ────────────────────────────────────────────────────────────────
    story.append(tag_table('A', '[Case A Title]', 'DEVELOPING', 'MEDIUM', None, styles))
    story.append(Paragraph(
        'Heuristics: [H1 (Label)] \u00b7 [H2 (Label)]',
        styles['heuristic_line']))

    story.append(Paragraph('PART 1 \u2014 FACTUAL ELEMENTS', styles['section_head']))
    story.append(fact_table([
        ('[Fact text.]',
         '[Source name \u2014 Tier N \u00b7 Gate check notes.]'),
        # add more (fact, source) tuples as needed
    ], styles))

    story.append(Paragraph('PART 2 \u2014 OBSERVED INCONGRUITY', styles['section_head']))
    story.append(Paragraph(
        '<b>[Heuristic label]:</b> [Incongruity analysis text.]',
        styles['body']))
    story.append(Paragraph(
        '<b>AFC:</b> [Fact most weakening current tag.]',
        styles['afc_note']))
    story.append(Paragraph(
        'INFERENCE: [Analytical inference.]',
        styles['infer']))
    story.append(Paragraph(
        'Domain quality: [Evidence quality statement.]',
        styles['small']))

    story.append(Paragraph('PART 3 \u2014 HYPOTHESIS SET', styles['section_head']))
    story.append(hyp_table([
        {'heading':           'HYPOTHESIS A \u2014 [Label]',
         'probability_range': 'XX\u2013XX%',
         'body':              '[Hypothesis A text.]'},
        {'heading':           'HYPOTHESIS B \u2014 [Label]',
         'probability_range': 'XX\u2013XX%',
         'body':              '[Hypothesis B text.]'},
    ], styles))

    story.append(Paragraph('PART 4 \u2014 TRUTH QUALITY CHECK', styles['section_head']))
    story.append(Paragraph(
        '<b>Assumptions:</b> [List key assumptions.]',
        styles['body']))
    story.append(Paragraph(
        '<b>Fragile fact:</b> [Fact \u00b7 Source \u00b7 Tier N \u00b7 Risk if false.]',
        styles['body']))
    story.append(Paragraph(
        '<b>High-impact uncertainty:</b> [Uncertainty and impact if unresolved.]',
        styles['body']))

    story.append(Paragraph('PART 5 \u2014 DISCONFIRMATION', styles['section_head']))
    story.append(disconf_table([
        ('[Confirms current framing.]', '[Contradicts current framing.]'),
        # add more pairs as needed
    ], '[Gate 5 revision trigger statement.]', styles))
    story.append(Paragraph(
        '<i>Gate 5 Framing Revision Trigger: [condition] \u2014 reframe from scratch.</i>',
        styles['pred_note']))

    story.extend(flag_block(
        'PRED-XXX-A', 1,
        '[Forward prediction text. C1\u2713 C2\u2713 C3\u2713 C4\u2713 C5\u2713]',
        '[Falsification condition.]',
        styles))
    story.append(hr())

    # ── ADDITIONAL CASES: copy the Case A block above, change letter/tag/content
    # story.append(tag_table('B', '[Case B Title]', 'ESCALATING', 'HIGH', None, styles))
    # ...

    # ── WHAT THIS BRIEF DOES NOT PROVE ────────────────────────────────────────
    story.append(PageBreak())
    story.append(Paragraph('WHAT THIS BRIEF DOES NOT PROVE', styles['section_head']))
    story.append(hr())
    for item in [
        '[Unproven item 1]',
        '[Unproven item 2]',
    ]:
        story.append(Paragraph(f'\u2715  {item}', styles['not_proven']))
    story.append(hr())

    # ── SOURCES ───────────────────────────────────────────────────────────────
    story.append(Paragraph('SOURCES', styles['section_head']))
    story.append(Paragraph(
        f'All Domains \u00b7 {SWEEP_STR} \u00b7 Edition {EDITION}',
        styles['small_bold']))
    story.append(Spacer(1, 2*mm))
    story.extend(source_block([
        {
            'name':      '[SOURCE NAME]',
            'tier':      'N',
            'category':  '[Primary Source / High-Authority Secondary / etc.]',
            'incentive': '[LOW / MEDIUM / HIGH \u2014 reason]',
            'body':      '[What was sourced from this outlet.]',
            'url':       'https://[url]',
        },
        # add more source dicts as needed
    ], styles))

    story.append(Spacer(1, 4*mm))
    story.append(Paragraph(
        f'Atollsphere Brief \u00b7 Edition {EDITION} \u00b7 {SWEEP_STR} \u00b7 {DATE_STR} \u00b7'
        f' Template build_core.py / styles.py \u00b7 GMT primary timestamps \u00b7'
        f' N sources \u00b7 N cases \u00b7 N forward flags \u00b7 LS AI Systems',
        styles['footer']))

    doc.build(story, onFirstPage=on_cover, onLaterPages=on_page)
    print(f'Built: {path}')


if __name__ == '__main__':
    build()
