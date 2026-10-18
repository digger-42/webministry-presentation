#!/usr/bin/env python3
"""Build the PCC Web Ministry Impress template and starter deck.

Writes a flat ODF presentation (.fodp) with the brand master slides, then
LibreOffice converts it to:
  templates/PCC-WebMinistry.otp   the reusable template (title slide only)
  deck/WebMinistry-Training.odp   the starter deck (title + sample slides)

Brand rules come from PCC Graphic Standards 2020. Run from the repo root:
  python3 tools/build_template.py
"""
import base64
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRAND = ROOT / "assets" / "brand"

# Slide size: 16:9
W, H = 28.0, 15.75

# Brand colors (Graphic Standards 2020, p. 11)
GREEN = "#95BA32"      # PMS 2301 C
BLACK = "#231F20"      # rich black, as printed in the guide
GREY = "#BCBCBC"       # Cool Grey 4 C
TEXT_GREY = "#5A5758"  # darker grey for small text, readable on white
PARTS = {               # secondary palette, one per part of the day
    "Gold": "#C69214",
    "Teal": "#1D8296",
    "Burgundy": "#7E2D40",
    "Dark Green": "#5E7E29",
}

# Avant Garde is the brand typeface; TeX Gyre Adventor is its free clone.
FONT = "TeX Gyre Adventor"

TAGLINE = "FIRMLY ROOTED AND NOW BEING BUILT UP"
FOOTER = "PCC Web Ministry Training"


def img(name):
    return base64.b64encode((BRAND / name).read_bytes()).decode()


def image_frame(name, x, y, w, h, href):
    return (
        f'<draw:frame draw:name="{name}" draw:style-name="grImage" draw:layer="backgroundobjects" '
        f'svg:x="{x}cm" svg:y="{y}cm" svg:width="{w}cm" svg:height="{h}cm">'
        f'<draw:image><office:binary-data>{href}</office:binary-data></draw:image></draw:frame>'
    )


def rect(name, x, y, w, h, style):
    return (
        f'<draw:rect draw:name="{name}" draw:style-name="{style}" draw:layer="backgroundobjects" '
        f'svg:x="{x}cm" svg:y="{y}cm" svg:width="{w}cm" svg:height="{h}cm"/>'
    )


def text_frame(name, x, y, w, h, style, pstyle, body):
    return (
        f'<draw:frame draw:name="{name}" draw:style-name="{style}" draw:layer="backgroundobjects" '
        f'svg:x="{x}cm" svg:y="{y}cm" svg:width="{w}cm" svg:height="{h}cm">'
        f'<draw:text-box><text:p text:style-name="{pstyle}">{body}</text:p></draw:text-box></draw:frame>'
    )


def placeholder(cls, master, x, y, w, h):
    return (
        f'<draw:frame presentation:style-name="{master}-{"outline1" if cls == "outline" else cls}" '
        'draw:layer="layout" '
        f'svg:x="{x}cm" svg:y="{y}cm" svg:width="{w}cm" svg:height="{h}cm" '
        f'presentation:class="{cls}" presentation:placeholder="true"><draw:text-box/></draw:frame>'
    )


def bullet_levels():
    """Green round bullets, en dashes on the second level."""
    return "".join(
        f'<text:list-level-style-bullet text:level="{lvl}" text:bullet-char="{"●" if lvl % 2 else "–"}">'
        f'<style:list-level-properties text:space-before="{(lvl - 1) * 1.2:.1f}cm" text:min-label-width="0.8cm"/>'
        f'<style:text-properties fo:font-family="OpenSymbol" style:use-window-font-color="false" '
        f'fo:color="{GREEN}" fo:font-size="{60 if lvl == 1 else 80}%"/></text:list-level-style-bullet>'
        for lvl in range(1, 10)
    )


def presentation_styles(master, title, outline, subtitle):
    """Presentation-family styles a master needs. Each arg is (size_pt, color, bold)."""
    def tp(size, color, bold):
        weight = "bold" if bold else "normal"
        return (
            f'<style:text-properties fo:font-family="\'{FONT}\'" style:font-family-generic="swiss" '
            f'fo:font-size="{size}pt" fo:color="{color}" fo:font-weight="{weight}"/>'
        )

    out = [
        f'<style:style style:name="{master}-title" style:family="presentation">'
        '<style:graphic-properties draw:stroke="none" draw:fill="none" draw:textarea-vertical-align="bottom" '
        'draw:auto-grow-height="false" fo:padding="0cm"/>'
        '<style:paragraph-properties fo:text-align="start" fo:line-height="100%"/>'
        f'{tp(*title)}</style:style>',
        f'<style:style style:name="{master}-subtitle" style:family="presentation">'
        '<style:graphic-properties draw:stroke="none" draw:fill="none" draw:textarea-vertical-align="top" '
        'draw:auto-grow-height="false" fo:padding="0cm"/>'
        '<style:paragraph-properties fo:text-align="start"/>'
        f'{tp(*subtitle)}</style:style>',
        f'<style:style style:name="{master}-background" style:family="presentation">'
        '<style:graphic-properties draw:stroke="none" draw:fill="none"/></style:style>',
        f'<style:style style:name="{master}-backgroundobjects" style:family="presentation">'
        '<style:graphic-properties draw:shadow="hidden"/></style:style>',
        f'<style:style style:name="{master}-notes" style:family="presentation">'
        f'<style:text-properties fo:font-family="\'{FONT}\'" fo:font-size="14pt"/></style:style>',
    ]
    size, color, _ = outline
    bullets = bullet_levels()
    out.append(
        f'<style:style style:name="{master}-outline1" style:family="presentation">'
        '<style:graphic-properties draw:stroke="none" draw:fill="none" draw:textarea-vertical-align="top" '
        'draw:auto-grow-height="false" fo:padding="0cm">'
        f'<text:list-style style:name="{master}-outline1">{bullets}</text:list-style></style:graphic-properties>'
        '<style:paragraph-properties fo:margin-top="0.35cm" fo:margin-bottom="0cm" fo:line-height="110%"/>'
        f'{tp(size, color, False)}</style:style>'
    )
    for lvl in range(2, 10):
        sub = max(size - 3 * (lvl - 1), 14)
        out.append(
            f'<style:style style:name="{master}-outline{lvl}" style:family="presentation" '
            f'style:parent-style-name="{master}-outline{lvl - 1}">'
            '<style:paragraph-properties fo:margin-top="0.15cm"/>'
            f'<style:text-properties fo:font-size="{sub}pt"/></style:style>'
        )
    return "".join(out)


def build_fodp(slides):
    logo = img("pcc-logo-horizontal-color.png")
    logo_rev = img("pcc-logo-horizontal-reversed-a.png")
    tree = img("pcc-tree-watermark.png")

    styles, auto, masters = [], [], []

    # Automatic styles shared by masters
    auto.append(
        '<style:page-layout style:name="PM1"><style:page-layout-properties fo:margin-top="0cm" '
        f'fo:margin-bottom="0cm" fo:margin-left="0cm" fo:margin-right="0cm" fo:page-width="{W}cm" '
        f'fo:page-height="{H}cm" style:print-orientation="landscape"/></style:page-layout>'
        '<style:style style:name="dpWhite" style:family="drawing-page"><style:drawing-page-properties '
        'draw:background-size="full" draw:fill="solid" draw:fill-color="#FFFFFF"/></style:style>'
        '<style:style style:name="dpDark" style:family="drawing-page"><style:drawing-page-properties '
        f'draw:background-size="full" draw:fill="solid" draw:fill-color="{BLACK}"/></style:style>'
        '<style:style style:name="grImage" style:family="graphic"><style:graphic-properties '
        'draw:stroke="none" draw:fill="none" style:protect="position size"/></style:style>'
        '<style:style style:name="grText" style:family="graphic"><style:graphic-properties '
        'draw:stroke="none" draw:fill="none" draw:auto-grow-height="false" fo:padding="0cm" '
        'draw:textarea-vertical-align="middle"/></style:style>'
        '<style:style style:name="grRule" style:family="graphic"><style:graphic-properties '
        f'draw:stroke="none" draw:fill="solid" draw:fill-color="{GREY}"/></style:style>'
        f'<style:style style:name="pFooter" style:family="paragraph"><style:text-properties '
        f'fo:font-family="\'{FONT}\'" fo:font-size="10pt" fo:color="{TEXT_GREY}"/></style:style>'
        '<style:style style:name="pTagline" style:family="paragraph"><style:paragraph-properties '
        f'fo:text-align="start"/><style:text-properties fo:font-family="\'{FONT}\'" fo:font-size="12pt" '
        f'fo:letter-spacing="0.12cm" fo:color="{GREEN}"/></style:style>'
    )
    auto.append(f'<text:list-style style:name="LBullets">{bullet_levels()}</text:list-style>')
    accents = {"Green": GREEN, **PARTS}
    for name, color in accents.items():
        key = name.replace(" ", "")
        auto.append(
            f'<style:style style:name="grAccent{key}" style:family="graphic"><style:graphic-properties '
            f'draw:stroke="none" draw:fill="solid" draw:fill-color="{color}"/></style:style>'
            f'<style:style style:name="pNum{key}" style:family="paragraph"><style:paragraph-properties '
            f'fo:text-align="end"/><style:text-properties fo:font-family="\'{FONT}\'" fo:font-size="14pt" '
            f'fo:color="{color}"/></style:style>'
        )

    # Title master: tree watermark bleeding off the left, logo and title on the right
    m = "PCC-Title"
    styles.append(presentation_styles(m, (30, BLACK, True), (20, BLACK, False), (18, TEXT_GREY, False)))
    tree_h = 18.5
    tree_w = tree_h * 4292 / 4900
    masters.append(
        f'<style:master-page style:name="{m}" style:page-layout-name="PM1" draw:style-name="dpWhite">'
        + image_frame("Tree watermark", -3.2, -1.4, round(tree_w, 3), tree_h, tree)
        + image_frame("PCC logo", 13.2, 4.1, 13.5, round(13.5 * 430 / 3098, 3), logo)
        + placeholder("title", m, 13.2, 6.7, 13.5, 2.6)
        + placeholder("subtitle", m, 13.2, 9.6, 13.5, 1.4)
        + "</style:master-page>"
    )

    # Section divider: dark background, reversed logo (Option A), green tagline
    m = "PCC-Section"
    styles.append(presentation_styles(m, (40, "#FFFFFF", True), (20, "#FFFFFF", False), (20, GREEN, False)))
    masters.append(
        f'<style:master-page style:name="{m}" style:page-layout-name="PM1" draw:style-name="dpDark">'
        + rect("Accent bar", 2.0, 4.6, 0.4, 3.6, "grAccentGreen")
        + placeholder("title", m, 2.9, 4.4, 22.5, 2.6)
        + placeholder("subtitle", m, 2.9, 7.2, 22.5, 1.4)
        + image_frame("PCC logo reversed", 17.2, 12.6, 9.4, round(9.4 * 430 / 3097, 3), logo_rev)
        + "</style:master-page>"
    )

    # Content masters: one per accent color
    for name, color in accents.items():
        key = name.replace(" ", "")
        m = "PCC-Content" if name == "Green" else f"PCC-Content-{key}"
        styles.append(presentation_styles(m, (28, BLACK, True), (20, BLACK, False), (18, TEXT_GREY, False)))
        masters.append(
            f'<style:master-page style:name="{m}" style:page-layout-name="PM1" draw:style-name="dpWhite">'
            + rect("Accent bar", 1.2, 1.0, 0.3, 1.5, f"grAccent{key}")
            + placeholder("title", m, 1.9, 0.6, 24.9, 1.9)
            + rect("Rule", 1.2, 2.85, 25.6, 0.03, "grRule")
            + placeholder("outline", m, 1.9, 3.4, 24.9, 10.4)
            + text_frame("Footer", 1.2, 14.4, 15.0, 0.8, "grText", "pFooter", FOOTER)
            + text_frame("Slide number", 22.8, 14.3, 4.0, 1.0, "grText", f"pNum{key}",
                         "<text:page-number>1</text:page-number>")
            + "</style:master-page>"
        )

    pages = []
    for i, s in enumerate(slides, 1):
        m = s["master"]
        body = [f'<draw:page draw:name="Slide {i}" draw:style-name="dp{"Dark" if m == "PCC-Section" else "White"}" '
                f'draw:master-page-name="{m}" presentation:presentation-page-layout-name="'
                f'{"AL1" if s.get("bullets") else "AL2"}">']
        geo = {
            "PCC-Title": {"title": (13.2, 6.7, 13.5, 2.6), "subtitle": (13.2, 9.6, 13.5, 1.4)},
            "PCC-Section": {"title": (2.9, 4.4, 22.5, 2.6), "subtitle": (2.9, 7.2, 22.5, 1.4)},
        }.get(m, {"title": (1.9, 0.6, 24.9, 1.9), "outline": (1.9, 3.4, 24.9, 10.4)})
        x, y, w, h = geo["title"]
        body.append(
            f'<draw:frame presentation:style-name="{m}-title" draw:layer="layout" svg:x="{x}cm" svg:y="{y}cm" '
            f'svg:width="{w}cm" svg:height="{h}cm" presentation:class="title" presentation:user-transformed="true">'
            f'<draw:text-box><text:p>{s["title"]}</text:p></draw:text-box></draw:frame>'
        )
        if "subtitle" in s:
            x, y, w, h = geo["subtitle"]
            body.append(
                f'<draw:frame presentation:style-name="{m}-subtitle" draw:layer="layout" svg:x="{x}cm" '
                f'svg:y="{y}cm" svg:width="{w}cm" svg:height="{h}cm" presentation:class="subtitle" '
                f'presentation:user-transformed="true"><draw:text-box><text:p>{s["subtitle"]}</text:p>'
                '</draw:text-box></draw:frame>'
            )
        if "bullets" in s:
            x, y, w, h = geo["outline"]
            items = ""
            for b in s["bullets"]:
                if isinstance(b, tuple):  # (text, [sub-bullets])
                    subs = "".join(f"<text:list-item><text:p>{t}</text:p></text:list-item>" for t in b[1])
                    items += f"<text:list-item><text:p>{b[0]}</text:p><text:list>{subs}</text:list></text:list-item>"
                else:
                    items += f"<text:list-item><text:p>{b}</text:p></text:list-item>"
            body.append(
                f'<draw:frame presentation:style-name="{m}-outline1" draw:layer="layout" svg:x="{x}cm" '
                f'svg:y="{y}cm" svg:width="{w}cm" svg:height="{h}cm" presentation:class="outline" '
                f'presentation:user-transformed="true"><draw:text-box><text:list text:style-name="LBullets">{items}</text:list>'
                '</draw:text-box></draw:frame>'
            )
        body.append("</draw:page>")
        pages.append("".join(body))

    ns = (
        'xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" '
        'xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" '
        'xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" '
        'xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" '
        'xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" '
        'xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" '
        'xmlns:presentation="urn:oasis:names:tc:opendocument:xmlns:presentation:1.0" '
        'xmlns:dc="http://purl.org/dc/elements/1.1/" '
        'xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" '
        'xmlns:xlink="http://www.w3.org/1999/xlink"'
    )
    layouts = (
        '<style:presentation-page-layout style:name="AL1">'
        '<presentation:placeholder presentation:object="title" svg:x="1.9cm" svg:y="0.6cm" svg:width="24.9cm" svg:height="1.9cm"/>'
        '<presentation:placeholder presentation:object="outline" svg:x="1.9cm" svg:y="3.4cm" svg:width="24.9cm" svg:height="10.4cm"/>'
        '</style:presentation-page-layout>'
        '<style:presentation-page-layout style:name="AL2">'
        '<presentation:placeholder presentation:object="title" svg:x="13.2cm" svg:y="6.7cm" svg:width="13.5cm" svg:height="2.6cm"/>'
        '<presentation:placeholder presentation:object="subtitle" svg:x="13.2cm" svg:y="9.6cm" svg:width="13.5cm" svg:height="1.4cm"/>'
        '</style:presentation-page-layout>'
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<office:document {ns} office:version="1.3" office:mimetype="application/vnd.oasis.opendocument.presentation">'
        '<office:meta><dc:title>PCC WebMinistry Training</dc:title></office:meta>'
        f'<office:font-face-decls><style:font-face style:name="{FONT}" svg:font-family="\'{FONT}\'" '
        'style:font-family-generic="swiss" style:font-pitch="variable"/></office:font-face-decls>'
        f'<office:styles>{layouts}{"".join(styles)}</office:styles>'
        f'<office:automatic-styles>{"".join(auto)}</office:automatic-styles>'
        f'<office:master-styles>{"".join(masters)}</office:master-styles>'
        f'<office:body><office:presentation>{"".join(pages)}</office:presentation></office:body>'
        '</office:document>'
    )


TITLE_SLIDE = {"master": "PCC-Title", "title": "PCC WebMinistry Training", "subtitle": "11/21/2026"}

DECK = [
    TITLE_SLIDE,
    {"master": "PCC-Content", "title": "Today", "bullets": [
        "10:00  How we're organized: people and responsibilities",
        "10:15  The building: network, phones, video streaming",
        "10:35  Services: Google Workspace, Breeze, Planning Center",
        "11:00  The website: Flex, menus, content, page types",
        "11:45  Hands-on: edit a page",
        "Lunch, then your turn: questions and ideas for the website",
    ]},
    {"master": "PCC-Section", "title": "How we're organized", "subtitle": "People and responsibilities"},
    {"master": "PCC-Content-Gold", "title": "Sample: a content slide in a part's color", "bullets": [
        ("Each part of the day has its own content master", [
            "Gold: people",
            "Teal: the building",
            "Burgundy: services",
            "Dark Green: the website",
        ]),
        "Green (PCC-Content) is the default for everything else",
    ]},
]


def convert(fodp, fmt, out_dir):
    subprocess.run(
        ["soffice", "--headless", "--convert-to", fmt, "--outdir", str(out_dir), str(fodp)],
        check=True, capture_output=True,
    )


def main():
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for stem, slides, fmt, dest in [
            ("PCC-WebMinistry", [TITLE_SLIDE], "otp", ROOT / "templates"),
            ("WebMinistry-Training", DECK, "odp", ROOT / "deck"),
        ]:
            fodp = tmp / f"{stem}.fodp"
            fodp.write_text(build_fodp(slides), encoding="utf-8")
            convert(fodp, fmt, tmp)
            dest.mkdir(exist_ok=True)
            (tmp / f"{stem}.{fmt}").replace(dest / f"{stem}.{fmt}")
            print(f"wrote {dest / f'{stem}.{fmt}'}")
            if "--keep-fodp" in sys.argv:
                (dest / f"{stem}.fodp").write_text(fodp.read_text(encoding="utf-8"), encoding="utf-8")


if __name__ == "__main__":
    main()
