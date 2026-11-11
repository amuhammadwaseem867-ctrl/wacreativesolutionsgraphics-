"""Generates the placeholder work samples in assets/work/.

These are stand-ins for real portfolio images. Replace each SVG with a real
JPG/PNG/WebP export and update the matching entry in js/projects.js.
Run: python3 tools/make_placeholders.py
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets" / "work"
OUT.mkdir(parents=True, exist_ok=True)

SANS = "Helvetica Neue, Helvetica, Arial, sans-serif"
SERIF = "Georgia, 'Times New Roman', serif"


# ---------- marks: each returns SVG markup centred on (cx, cy) with size s ----------
def mark(kind, cx, cy, s, c, c2=None):
    c2 = c2 or c
    h = s / 2
    if kind == "sun":  # saffron: half sun over a line
        rays = "".join(
            f'<rect x="{cx - s*0.03}" y="{cy - h}" width="{s*0.06}" height="{s*0.2}" rx="{s*0.03}" fill="{c}" transform="rotate({a} {cx} {cy + s*0.1})"/>'
            for a in range(-75, 90, 25)
        )
        return (f'<g>{rays}<path d="M{cx - h*0.62},{cy + s*0.1} A{h*0.62},{h*0.62} 0 0 1 {cx + h*0.62},{cy + s*0.1} Z" fill="{c}"/>'
                f'<rect x="{cx - h}" y="{cy + s*0.16}" width="{s}" height="{s*0.07}" rx="{s*0.035}" fill="{c2}"/></g>')
    if kind == "bean":  # coffee: bean made of two arcs
        return (f'<g transform="rotate(-28 {cx} {cy})"><ellipse cx="{cx}" cy="{cy}" rx="{h*0.62}" ry="{h*0.92}" fill="{c}"/>'
                f'<path d="M{cx},{cy - h*0.9} C{cx - h*0.35},{cy - h*0.3} {cx + h*0.35},{cy + h*0.3} {cx},{cy + h*0.9}" stroke="{c2}" stroke-width="{s*0.06}" fill="none" stroke-linecap="round"/></g>')
    if kind == "arch":  # architects: nested arches
        out = []
        for i, f in enumerate([1, 0.66, 0.32]):
            w = s * f
            col = c if i % 2 == 0 else c2
            out.append(f'<path d="M{cx - w/2},{cy + h} V{cy + h - w*0.5} A{w/2},{w/2} 0 0 1 {cx + w/2},{cy + h - w*0.5} V{cy + h} Z" fill="{col}"/>')
        return "<g>" + "".join(out) + "</g>"
    if kind == "flower":  # festival: 6 petals
        petals = "".join(
            f'<ellipse cx="{cx}" cy="{cy - h*0.5}" rx="{h*0.26}" ry="{h*0.5}" fill="{c}" transform="rotate({a} {cx} {cy})"/>'
            for a in range(0, 360, 60)
        )
        return f'<g>{petals}<circle cx="{cx}" cy="{cy}" r="{h*0.22}" fill="{c2}"/></g>'
    if kind == "atlas":  # logistics: circle + forward arrow cut
        return (f'<g><circle cx="{cx}" cy="{cy}" r="{h}" fill="{c}"/>'
                f'<path d="M{cx - h*0.5},{cy - h*0.45} L{cx + h*0.35},{cy} L{cx - h*0.5},{cy + h*0.45}" stroke="{c2}" stroke-width="{s*0.12}" fill="none" stroke-linejoin="round" stroke-linecap="round"/></g>')
    if kind == "drop":  # skincare: drop with crescent
        return (f'<g><path d="M{cx},{cy - h} C{cx + h*0.9},{cy - h*0.05} {cx + h*0.75},{cy + h} {cx},{cy + h} C{cx - h*0.75},{cy + h} {cx - h*0.9},{cy - h*0.05} {cx},{cy - h} Z" fill="{c}"/>'
                f'<path d="M{cx - h*0.35},{cy + h*0.2} A{h*0.4},{h*0.4} 0 0 0 {cx + h*0.3},{cy + h*0.65}" stroke="{c2}" stroke-width="{s*0.06}" fill="none" stroke-linecap="round"/></g>')
    if kind == "peak":  # fitness: two peaks
        return (f'<g><path d="M{cx - h},{cy + h*0.7} L{cx - h*0.25},{cy - h*0.7} L{cx + h*0.5},{cy + h*0.7} Z" fill="{c}"/>'
                f'<path d="M{cx - h*0.05},{cy + h*0.7} L{cx + h*0.45},{cy - h*0.2} L{cx + h},{cy + h*0.7} Z" fill="{c2}"/></g>')
    if kind == "smile":  # dental: rounded square + smile
        return (f'<g><rect x="{cx - h}" y="{cy - h}" width="{s}" height="{s}" rx="{s*0.28}" fill="{c}"/>'
                f'<path d="M{cx - h*0.5},{cy + h*0.05} Q{cx},{cy + h*0.6} {cx + h*0.5},{cy + h*0.05}" stroke="{c2}" stroke-width="{s*0.1}" fill="none" stroke-linecap="round"/>'
                f'<circle cx="{cx - h*0.35}" cy="{cy - h*0.3}" r="{s*0.06}" fill="{c2}"/><circle cx="{cx + h*0.35}" cy="{cy - h*0.3}" r="{s*0.06}" fill="{c2}"/></g>')
    raise ValueError(kind)


def svg(w, h, body, bg):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
            f'<defs><filter id="sh" x="-20%" y="-20%" width="140%" height="150%">'
            f'<feDropShadow dx="0" dy="18" stdDeviation="22" flood-color="#000" flood-opacity="0.28"/></filter></defs>'
            f'<rect width="{w}" height="{h}" fill="{bg}"/>{body}</svg>')


def text(x, y, t, size, fill, weight=700, family=SANS, anchor="start", ls=0, opacity=1):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}" opacity="{opacity}">{t}</text>')


# ---------- templates ----------
def identity(name, tagline, k, colors, ink, paper):
    """Brand board: primary panel, palette, card, type specimen."""
    c1, c2, c3 = colors
    b = []
    b.append(f'<rect x="60" y="60" width="900" height="1080" rx="8" fill="{c1}"/>')
    b.append(mark(k, 510, 480, 300, c2, c3))
    b.append(text(510, 760, name, 74, paper, 800, anchor="middle", ls=-1))
    b.append(text(510, 815, tagline, 28, paper, 400, anchor="middle", ls=2, opacity=.8))
    # palette
    for i, (col, label) in enumerate(zip(colors + [ink], ["Primary", "Accent", "Support", "Ink"])):
        y = 60 + i * 140
        b.append(f'<rect x="1000" y="{y}" width="540" height="120" rx="8" fill="{col}"/>')
        tc = paper if col in (c1, ink) else ink
        b.append(text(1030, y + 52, label, 26, tc, 700))
        b.append(text(1030, y + 90, col.upper(), 22, tc, 400, opacity=.8))
    # mini card + specimen
    b.append(f'<rect x="1000" y="640" width="540" height="240" rx="8" fill="{paper}"/>')
    b.append(mark(k, 1090, 760, 90, c1, c2))
    b.append(text(1170, 750, name, 30, ink, 800))
    b.append(text(1170, 790, "hello@" + name.lower().replace(" ", "").replace("&amp;", "and") + ".com", 20, ink, 400, opacity=.7))
    b.append(f'<rect x="1000" y="910" width="540" height="230" rx="8" fill="{c2}"/>')
    b.append(text(1030, 1060, "Aa", 150, ink, 800, ls=-4))
    b.append(text(1300, 1000, "Display", 24, ink, 700))
    b.append(text(1300, 1035, "Bold 800", 22, ink, 400, opacity=.7))
    b.append(text(1300, 1090, "Body", 24, ink, 700))
    b.append(text(1300, 1125, "Regular 400", 22, ink, 400, opacity=.7))
    return svg(1600, 1200, "".join(b), paper)


def logo(name, sub, k, bg, fg, accent):
    b = []
    for r in (150, 260, 370):  # construction circles
        b.append(f'<circle cx="800" cy="500" r="{r}" fill="none" stroke="{fg}" stroke-opacity=".12" stroke-width="2"/>')
    b.append(f'<line x1="800" y1="80" x2="800" y2="920" stroke="{fg}" stroke-opacity=".12" stroke-width="2"/>')
    b.append(f'<line x1="380" y1="500" x2="1220" y2="500" stroke="{fg}" stroke-opacity=".12" stroke-width="2"/>')
    b.append(mark(k, 800, 500, 300, fg, accent))
    b.append(text(800, 1010, name, 84, fg, 800, anchor="middle", ls=6))
    b.append(text(800, 1065, sub, 26, fg, 400, anchor="middle", ls=8, opacity=.7))
    return svg(1600, 1200, "".join(b), bg)


def cards(name, person, role, k, table, front, back, ink, accent):
    W, H = 680, 400  # 85 x 55 mm ratio is ~1.545; 680x440
    H = 440
    b = []
    # back card (rotated)
    b.append(f'<g transform="translate(250 230) rotate(-8)" filter="url(#sh)">'
             f'<rect width="{W}" height="{H}" rx="14" fill="{back}"/>'
             + mark(k, W/2, H/2 - 30, 150, front, accent)
             + text(W/2, H/2 + 120, name, 40, front, 800, anchor="middle", ls=4) + '</g>')
    # front card
    b.append(f'<g transform="translate(700 520) rotate(6)" filter="url(#sh)">'
             f'<rect width="{W}" height="{H}" rx="14" fill="{front}"/>'
             + mark(k, 90, 90, 80, back, accent)
             + text(50, 260, person, 40, ink, 800)
             + text(50, 300, role, 24, ink, 400, opacity=.7)
             + f'<rect x="50" y="330" width="80" height="4" fill="{accent}"/>'
             + text(50, 380, "+92 300 000 0000", 22, ink, 400)
             + text(W - 50, 380, "hello@" + name.lower().replace(" ", "") + ".com", 22, ink, 400, anchor="end")
             + '</g>')
    return svg(1600, 1200, "".join(b), table)


def flyer(title_lines, sub, date, k, table, paper, c1, c2, ink, cta="Free entry"):
    b = []
    PW, PH = 760, 1075  # A-series ratio
    g = [f'<rect width="{PW}" height="{PH}" fill="{paper}"/>']
    g.append(f'<rect x="0" y="0" width="{PW}" height="560" fill="{c1}"/>')
    g.append(f'<circle cx="{PW - 120}" cy="420" r="240" fill="{c2}" opacity=".9"/>')
    g.append(mark(k, 200, 280, 220, paper, c2))
    y = 650
    for line in title_lines:
        g.append(text(50, y, line, 92, ink, 900, ls=-3))
        y += 92
    g.append(text(52, y + 20, sub, 28, ink, 400, opacity=.75))
    g.append(f'<rect x="50" y="{PH - 130}" width="{PW - 100}" height="2" fill="{ink}" opacity=".3"/>')
    g.append(text(50, PH - 70, date, 30, ink, 800))
    g.append(f'<rect x="{PW - 250}" y="{PH - 108}" width="200" height="60" rx="30" fill="{c1}"/>')
    g.append(text(PW - 150, PH - 68, cta, 24, paper, 700, anchor="middle"))
    b.append(f'<clipPath id="pg"><rect width="{PW}" height="{PH}"/></clipPath>')
    b.append(f'<g transform="translate(220 62) rotate(-3)" filter="url(#sh)"><g clip-path="url(#pg)">' + "".join(g) + "</g></g>")
    return svg(1200, 1200, "".join(b), table)


PROJECTS = {
    "saffron-and-salt.svg": identity("Saffron &amp; Salt", "KITCHEN · LAHORE".replace(" · ", "  /  "), "sun",
                                     ["#1F4A3A", "#F2B134", "#E9DCC3"], "#14201B", "#F7F5EF"),
    "kora-coffee.svg": logo("KORA", "COFFEE ROASTERS", "bean", "#2A1A14", "#F1E6D6", "#2A1A14"),
    "northline-cards.svg": cards("NORTHLINE", "Sara Malik", "Principal Architect", "arch",
                                 "#C9CCC6", "#F4F3EF", "#22303C", "#22303C", "#B8875A"),
    "bloom-festival.svg": flyer(["Bloom", "Spring", "Festival"], "Music, food and flowers in the park", "Sat 14 March, 4 pm",
                                "flower", "#E7E3EA", "#FFF9F2", "#E0446A", "#FFC145", "#2A1630"),
    "atlas-logistics.svg": identity("Atlas Freight", "LOGISTICS  /  KARACHI", "atlas",
                                    ["#0E3B8C", "#36C2B4", "#DCE6F5"], "#0A1630", "#F5F7FB"),
    "noor-skincare.svg": logo("NOOR", "SKIN  CARE", "drop", "#EBDCD3", "#5A2E39", "#EBDCD3"),
    "peak-fitness.svg": flyer(["Train", "Like You", "Mean It"], "First month at Peak Fitness for half price", "Offer ends 30 June",
                              "peak", "#1E2328", "#F4F6F2", "#16181D", "#C6F432", "#16181D", cta="Join today"),
    "lumen-dental-cards.svg": cards("LUMEN", "Dr. Ali Raza", "Dental Surgeon", "smile",
                                    "#2F6F78", "#FFFFFF", "#7FD3DB", "#123A40", "#123A40"),
}

for fname, content in PROJECTS.items():
    (OUT / fname).write_text(content, encoding="utf-8")
    print("wrote", fname)
