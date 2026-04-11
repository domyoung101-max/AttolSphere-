"""build_core.py — AttolSphere reusable layout functions.

Provides all table/flowable builders and the page-callback factory.
Import in per-edition scripts:
    from build_core import (
        hr, thin_rule, tag_table, fact_table, hyp_table,
        disconf_table, flag_block, source_block, make_page_callbacks,
        get_source_info,
    )
"""

import json
from pathlib import Path

from reportlab.platypus import Paragraph, Table, TableStyle, HRFlowable
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_CENTER

from styles import (
    NAVY, TEAL, CHARCOAL, MID_GREY, LIGHT_BG, ROW_ALT,
    WHITE, RED_TAG, AMBER, GREEN_TAG, PURPLE, DK_GREEN,
    MARGIN, PAGE_W, PAGE_H,
)

# ── SOURCE REGISTRY LOOKUP ───────────────────────────────────────────────────

_REGISTRY_PATH = Path(__file__).parent / 'SOURCE_REGISTRY.json'
_registry_cache: list | None = None


def _load_registry() -> list:
    """Load and cache the sources list from SOURCE_REGISTRY.json."""
    global _registry_cache
    if _registry_cache is None:
        with _REGISTRY_PATH.open(encoding='utf-8') as fh:
            data = json.load(fh)
        # The registry stores all sources in a single 'sources' array.
        # (Equivalent to both core_sweep_feeds and supplementary_feeds.)
        _registry_cache = data.get('sources', [])
    return _registry_cache


def get_source_info(domain: str) -> dict:
    """Look up tier, category, and incentive_baseline for a domain.

    Searches all entries in SOURCE_REGISTRY.json['sources'], matching
    the supplied domain against each entry's 'domains' list.  A plain
    domain (e.g. 'reuters.com') also matches registry entries that
    include sub-paths for the same host (e.g. 'x.com/IDF').

    Parameters
    ----------
    domain : str
        Bare domain name, e.g. 'reuters.com' or 'bbc.co.uk'.

    Returns
    -------
    dict with keys:
        tier              : int   — 1–4 per registry
        category          : str   — e.g. 'High-Authority Secondary'
        incentive_baseline: str   — 'LOW' / 'LOW-MEDIUM' / 'MEDIUM' / 'HIGH'

    Safe defaults (tier 2, Unknown, MEDIUM) are returned when the
    domain is not found in the registry.
    """
    domain = domain.strip().lower()
    for entry in _load_registry():
        for reg_domain in entry.get('domains', []):
            reg_norm = reg_domain.strip().lower()
            # Exact match, or the registry entry is a sub-path of the domain
            # (e.g. 'x.com/IDF' vs query 'x.com').
            if reg_norm == domain or reg_norm.startswith(domain + '/'):
                return {
                    'tier':               entry['tier'],
                    'category':           entry['category'],
                    'incentive_baseline': entry['incentive_baseline'],
                }
    return {
        'tier':               2,
        'category':           'Unknown',
        'incentive_baseline': 'MEDIUM',
    }


# ── HELPERS ──────────────────────────────────────────────────────────────────

def hr(width='100%'):
    return HRFlowable(width=width, thickness=0.5, color=TEAL,
                      spaceAfter=5, spaceBefore=5)


def thin_rule():
    return HRFlowable(width='100%', thickness=0.3,
                      color=colors.HexColor('#D0D8E0'),
                      spaceAfter=2, spaceBefore=2)


def tag_table(case_letter, title, tag, confidence, st, styles):
    """Coloured header row for a case block."""
    tag_colors = {
        'ESCALATING':             (RED_TAG,   WHITE),
        'ESCALATING-PROVISIONAL': (AMBER,     WHITE),
        'DEVELOPING':             (AMBER,     WHITE),
        'NEW':                    (TEAL,      WHITE),
        'ELEVATED':               (NAVY,      WHITE),
        'STABLE':                 (GREEN_TAG, WHITE),
        'RESOLVED':               (MID_GREY,  WHITE),
        'DE-ESCALATING':          (DK_GREEN,  WHITE),
        'WATCH':                  (PURPLE,    WHITE),
    }
    conf_map = {
        'HIGH':       (GREEN_TAG, '70\u201390%'),
        'MEDIUM':     (AMBER,     '55\u201370%'),
        'LOW-MEDIUM': (AMBER,     '40\u201355%'),
        'LOW':        (RED_TAG,   '25\u201340%'),
    }
    tag_bg, tag_fg = tag_colors.get(tag, (MID_GREY, WHITE))
    conf_bg, conf_range = conf_map.get(confidence, (MID_GREY, ''))

    case_cell = Paragraph(f'<b>CASE {case_letter}</b>',
        ParagraphStyle('cc', fontName='Helvetica-Bold', fontSize=8,
                       textColor=WHITE))
    title_cell = Paragraph(f'<b>{title}</b>',
        ParagraphStyle('tc', fontName='Helvetica-Bold', fontSize=8,
                       textColor=NAVY))
    tag_cell = Paragraph(f'<b>{tag}</b>',
        ParagraphStyle('tgc', fontName='Helvetica-Bold', fontSize=7.5,
                       textColor=tag_fg, alignment=TA_CENTER))
    conf_cell = Paragraph(
        f'<b>{confidence}</b><br/><font size=6>{conf_range}</font>',
        ParagraphStyle('cfc', fontName='Helvetica-Bold', fontSize=7.5,
                       textColor=WHITE, alignment=TA_CENTER))

    tbl = Table([[case_cell, title_cell, tag_cell, conf_cell]],
                colWidths=[22*mm, 95*mm, 35*mm, 22*mm])
    tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (0, 0), NAVY),
        ('BACKGROUND',    (1, 0), (1, 0), LIGHT_BG),
        ('BACKGROUND',    (2, 0), (2, 0), tag_bg),
        ('BACKGROUND',    (3, 0), (3, 0), conf_bg),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING',   (0, 0), (-1, -1), 5),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 5),
        ('TOPPADDING',    (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LINEBELOW',     (0, 0), (-1, -1), 1, TEAL),
    ]))
    return tbl


def fact_table(rows, styles):
    """Two-column fact/source table.

    rows = [(fact_text, source_attribution), ...]
    """
    header = [
        Paragraph('<b>FACT</b>',
            ParagraphStyle('fh', fontName='Helvetica-Bold',
                           fontSize=7, textColor=WHITE)),
        Paragraph('<b>SOURCE \u2014 TIER \u00b7 GATE 0</b>',
            ParagraphStyle('sh', fontName='Helvetica-Bold',
                           fontSize=7, textColor=WHITE)),
    ]
    table_rows = [header]
    for fact, source in rows:
        table_rows.append([
            Paragraph(fact,
                ParagraphStyle('fb', fontName='Helvetica',
                               fontSize=7.5, leading=10, textColor=CHARCOAL)),
            Paragraph(source,
                ParagraphStyle('sb', fontName='Helvetica-Oblique',
                               fontSize=7, leading=9.5, textColor=MID_GREY)),
        ])
    tbl = Table(table_rows, colWidths=[117*mm, 57*mm])
    style = [
        ('BACKGROUND',    (0, 0), (-1, 0), NAVY),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING',   (0, 0), (-1, -1), 5),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 5),
        ('TOPPADDING',    (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LINEBELOW',     (0, 1), (-1, -1), 0.3, colors.HexColor('#D0D8E0')),
    ]
    for i in range(1, len(table_rows)):
        if i % 2 == 0:
            style.append(('BACKGROUND', (0, i), (-1, i), ROW_ALT))
    tbl.setStyle(TableStyle(style))
    return tbl


def hyp_table(hypotheses, styles):
    """N-column hypothesis comparison table.

    hypotheses = [{'heading': str, 'body': str, 'probability_range': str}, ...]
    """
    n = len(hypotheses)
    col_w = 174 * mm / n
    headers, bodies = [], []
    for h in hypotheses:
        teal_hex = TEAL.hexval()[2:]  # strip '0x' prefix
        headers.append(
            Paragraph(
                f'<b>{h["heading"]}</b><br/>'
                f'<font size=6 color="#{teal_hex}">{h["probability_range"]}</font>',
                ParagraphStyle('hh', fontName='Helvetica-Bold', fontSize=7.5,
                               textColor=NAVY, leading=11)))
        bodies.append(
            Paragraph(h['body'],
                ParagraphStyle('hb', fontName='Helvetica', fontSize=7.5,
                               leading=10, textColor=CHARCOAL)))
    tbl = Table([headers, bodies], colWidths=[col_w] * n)
    line_cmds = [
        ('LINEAFTER', (i - 1, 0), (i - 1, -1), 0.5, TEAL)
        for i in range(1, n)
    ]
    tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), LIGHT_BG),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING',   (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 6),
        ('TOPPADDING',    (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('BOX',           (0, 0), (-1, -1), 0.5, TEAL),
    ] + line_cmds))
    return tbl


def disconf_table(rows, revision_trigger, styles):
    """Two-column confirms/contradicts disconfirmation table.

    rows = [(confirms_text, contradicts_text), ...]
    revision_trigger — string shown as a Gate 5 note (not rendered in the
    table itself; caller should append it as a pred_note paragraph).
    """
    header = [
        Paragraph('<b>CONFIRMS</b>',
            ParagraphStyle('ch', fontName='Helvetica-Bold',
                           fontSize=7.5, textColor=GREEN_TAG)),
        Paragraph('<b>CONTRADICTS</b>',
            ParagraphStyle('cth', fontName='Helvetica-Bold',
                           fontSize=7.5, textColor=RED_TAG)),
    ]
    table_rows = [header]
    for conf, contra in rows:
        table_rows.append([
            Paragraph(f'\u25a0 {conf}',
                ParagraphStyle('cr', fontName='Helvetica',
                               fontSize=7.5, leading=10, textColor=CHARCOAL)),
            Paragraph(f'\u25a0 {contra}',
                ParagraphStyle('ctr', fontName='Helvetica',
                               fontSize=7.5, leading=10, textColor=CHARCOAL)),
        ])
    tbl = Table(table_rows, colWidths=[87*mm, 87*mm])
    tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), NAVY),
        ('TEXTCOLOR',     (0, 0), (-1, 0), WHITE),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING',   (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 6),
        ('TOPPADDING',    (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LINEAFTER',     (0, 0), (0, -1),  0.5, TEAL),
        ('LINEBELOW',     (0, 1), (-1, -1), 0.3, colors.HexColor('#D0D8E0')),
    ]))
    return tbl


def flag_block(ref, number, body_text, gate_note, styles):
    """Forward-flag prediction block. Returns a list of flowables."""
    return [
        Paragraph(f'<b>FLAG {number} \u00b7 {ref}</b>', styles['flag_head']),
        Paragraph(body_text, styles['body']),
        Paragraph(f'<i>Gate note: {gate_note}</i>', styles['pred_note']),
    ]


def source_block(sources, styles):
    """Formatted source list. Returns a list of flowables.

    Each source dict: name, tier, category, body, and optionally
    incentive (str) and url (str).
    """
    flowables = []
    for i, s in enumerate(sources, 1):
        flowables.append(Paragraph(
            f'SOURCE {i} \u2014 {s["name"]}',
            ParagraphStyle('sn', fontName='Helvetica-Bold', fontSize=7.5,
                           textColor=NAVY, spaceBefore=4)))
        flowables.append(Paragraph(
            f'TIER {s["tier"]} \u2014 {s["category"]}',
            styles['source_tier']))
        flowables.append(Paragraph(s['body'], styles['small']))
        if s.get('incentive'):
            flowables.append(Paragraph(
                f'Incentive: {s["incentive"]}',
                ParagraphStyle('inc', fontName='Helvetica-Oblique',
                               fontSize=7, textColor=AMBER)))
        if s.get('url'):
            flowables.append(Paragraph(s['url'], styles['small']))
        flowables.append(thin_rule())
    return flowables


# ── PAGE-CALLBACK FACTORY ────────────────────────────────────────────────────

def make_page_callbacks(edition, sweep_str, date_str):
    """Return (on_cover, on_page) callables for SimpleDocTemplate.build().

    Parameters
    ----------
    edition   : str  e.g. '013'
    sweep_str : str  e.g. 'MORNING SWEEP'
    date_str  : str  e.g. '09 APRIL 2026'
    """

    def on_cover(canvas, doc):
        canvas.saveState()
        # Teal strip top
        canvas.setFillColor(TEAL)
        canvas.rect(0, PAGE_H - 4*mm, PAGE_W, 4*mm, fill=1, stroke=0)
        # Navy footer bar
        canvas.setFillColor(NAVY)
        canvas.rect(0, 0, PAGE_W, 14*mm, fill=1, stroke=0)
        canvas.setFont('Helvetica', 6.5)
        canvas.setFillColor(MID_GREY)
        canvas.drawCentredString(
            PAGE_W / 2, 5*mm,
            'CONFIDENTIAL \u2014 For Editorial Review Only \u00b7 AttolSphere \u00b7 LS AI Systems')
        canvas.restoreState()

    def on_page(canvas, doc):
        canvas.saveState()
        # Navy header bar
        canvas.setFillColor(NAVY)
        canvas.rect(0, PAGE_H - 13*mm, PAGE_W, 13*mm, fill=1, stroke=0)
        canvas.setFont('Helvetica-Bold', 7)
        canvas.setFillColor(TEAL)
        canvas.drawString(MARGIN, PAGE_H - 8*mm, 'LS')
        canvas.setFillColor(WHITE)
        canvas.setFont('Helvetica', 6.5)
        canvas.drawString(MARGIN + 8*mm, PAGE_H - 8*mm, 'AI SYSTEMS')
        canvas.setFont('Helvetica', 6.5)
        canvas.drawRightString(
            PAGE_W - MARGIN, PAGE_H - 8*mm,
            f'ATOLLSPHERE BRIEF \u00b7 EDITION {edition} \u00b7 {sweep_str} \u00b7 {date_str}')
        # Light footer
        canvas.setFillColor(LIGHT_BG)
        canvas.rect(0, 0, PAGE_W, 9*mm, fill=1, stroke=0)
        canvas.setFont('Helvetica', 6.5)
        canvas.setFillColor(MID_GREY)
        canvas.drawCentredString(
            PAGE_W / 2, 3*mm,
            f'CONFIDENTIAL \u2014 For Editorial Review Only \u00b7 AttolSphere \u00b7 LS AI Systems'
            f' \u00b7 smarter ai prediction systems \u00b7 Page {doc.page}')
        canvas.restoreState()

    return on_cover, on_page
