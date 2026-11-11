"""Static site generator. Reads content/projects.json and writes index.html and work/<slug>.html.
Run: python3 tools/build.py
"""
import json, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = json.loads((ROOT / "content/projects.json").read_text())
P, WEB, UI = D["projects"], D["web"], D["uiConcepts"]
e = html.escape

SITE = {
    "name": "WA Creative Solution",
    "person": "Muhammad Waseem Akram",
    "email": "amuhammadwaseem867@gmail.com",
    "phones": [("+92 311 5962551", "+923115962551"), ("+92 346 5187384", "+923465187384"), ("+27 61 069 7051", "+27610697051")],
    "socials": [("Instagram", "https://www.instagram.com/wacreativesstudio/"),
                ("Facebook", "https://www.facebook.com/people/WA-Creative-Solutions/61593247537659/"),
                ("LinkedIn", "https://www.linkedin.com/in/muhammad-waseem-akram-996015425/"),
                ("Agency site", "https://wacreativesolution.com/")],
}
CATS = {"identity": "Brand identity", "packaging": "Packaging", "social": "Social media"}

HEX = "M0.00 23.00 L39.84 0.00 L79.67 23.00 L79.67 69.00 L39.84 92.00 L0.00 69.00 Z M71.17 27.91 L39.84 9.81 L8.50 27.91 L8.50 64.09 L39.84 82.19 L71.17 64.09 Z"
WA = "M29.44 64.00 L20.46 64.00 L11.71 29.03 L11.46 28.00 L20.22 28.00 L25.85 50.52 L34.84 28.95 L44.03 51.02 L50.43 28.00 L59.25 28.00 L68.93 62.86 L69.25 64.00 L60.43 64.00 L57.80 54.56 L51.87 54.56 L49.25 64.00 L40.23 64.00 L34.84 51.05 Z M54.84 43.88 L53.57 48.44 L56.10 48.44 Z"


def mark(cls=""):
    return (f'<svg class="{cls}" viewBox="0 0 79.67 92" aria-hidden="true">'
            f'<path fill="var(--gold)" fill-rule="evenodd" d="{HEX}"/><path fill="var(--paper)" fill-rule="evenodd" d="{WA}"/></svg>')


def mark_outline():
    return (f'<svg class="hero-mark" viewBox="-2 -2 83.67 96" aria-hidden="true">'
            f'<path class="draw d1" pathLength="1" d="{HEX}"/><path class="draw d2" pathLength="1" d="{WA}"/></svg>')


def head(title, desc, pre, og=None):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
{f'<meta property="og:image" content="{og}">' if og else ''}
<meta name="theme-color" content="#080808">
<link rel="icon" href="{pre}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800&family=Poppins:wght@300;400;500;600&display=swap">
<link rel="stylesheet" href="{pre}css/style.css">
<link rel="stylesheet" href="{pre}css/motion.css">
<script>document.documentElement.classList.add("js")</script>
</head>
<body>
'''


def header(pre, home):
    h = "" if home else pre + "index.html"
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="progress" aria-hidden="true"></div>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="logo" href="{pre}index.html" aria-label="{SITE['name']}, home">
      {mark()}
      <span class="logo-text"><b>WA CREATIVE</b><span>SOLUTION</span></span>
    </a>
    <nav class="nav" aria-label="Main">
      <a href="{h}#work">Work</a>
      <a href="{h}#uiux">UI/UX</a>
      <a href="{h}#services">Services</a>
      <a href="{h}#process">Process</a>
      <a href="{h}#about">About</a>
    </nav>
    <a class="btn btn-sm magnetic" href="{h}#contact">Start a project</a>
  </div>
</header>
'''


def footer(pre, scripts):
    s = "".join(f'<script src="{pre}js/{x}"></script>\n' for x in scripts)
    return f'''<footer class="site-footer">
  <div class="wrap footer-inner">
    <p>© 2026 {SITE['name']}. Design by {SITE['person']}.</p>
    <a href="#top">Back to top</a>
  </div>
</footer>
<div class="cursor" aria-hidden="true"><span>View</span></div>
{s}</body>
</html>
'''


def contact():
    phones = "".join(f'<div class="contact-line"><span class="lbl">{"Phone" if i == 0 else ("South Africa" if n.startswith("+27") else "Phone")}</span><a class="val" href="tel:{t}">{n}</a></div>'
                     for i, (n, t) in enumerate(SITE["phones"]))
    socials = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{l}</a></li>' for l, u in SITE["socials"])
    return f'''<section class="contact" id="contact" aria-labelledby="contact-title">
  <div class="wrap contact-grid">
    <div class="contact-intro">
      <h2 id="contact-title" class="reveal">Let's build your brand.</h2>
      <p>Tell me about your business and what you need. You'll get a reply with ideas, a timeline and a written quote.</p>
      <div class="contact-lines">
        <div class="contact-line"><span class="lbl">Email</span><span class="val" id="email-val">{SITE['email']}</span><button type="button" class="copy" id="copy-email">Copy</button></div>
        {phones}
        <div class="contact-line"><span class="lbl">Studios</span><span>Rawalpindi, Pakistan and Cape Town, South Africa</span></div>
      </div>
      <ul class="socials">{socials}</ul>
    </div>
    <form class="form" id="contact-form" novalidate>
      <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
      <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
      <div class="field-row">
        <div class="field"><label for="f-type">What do you need?</label>
          <select id="f-type" name="type"><option>Brand identity</option><option>Logo design</option><option>Packaging</option><option>Business cards and stationery</option><option>Flyers and social media</option><option>UI/UX design</option><option>Something else</option></select></div>
        <div class="field"><label for="f-when">When do you need it?</label>
          <select id="f-when" name="when"><option>This month</option><option>In 1 to 3 months</option><option>No fixed date</option></select></div>
      </div>
      <div class="field"><label for="f-msg">Tell me about your project</label><textarea id="f-msg" name="message" rows="5" required></textarea></div>
      <button class="btn magnetic" type="submit">Send message</button>
      <p class="form-status" id="form-status" role="status" aria-live="polite"></p>
    </form>
  </div>
</section>
'''


def tag(p):
    return '<span class="tag">Concept</span>' if p.get("concept") else ""


# ---------------- home ----------------
def home():
    feats = [p for p in P if p.get("featured")][:3]
    reel = "".join(f'<a href="work/{p["slug"]}.html" class="reveal-img" data-cursor="View"><img src="{p["cover"]}" alt="{e(p["title"])} project cover"><span>{e(p.get("short", p["title"]))}</span></a>' for p in feats)
    marquee_items = ["Brand identity", "Logo design", "Brand guidelines", "Packaging", "Business cards", "Stationery", "Flyers and print", "Social media", "UI/UX design"]
    mq = "".join(f"<span>{e(x)}</span>" for x in marquee_items)
    cards = []
    for i, p in enumerate(P):
        feature = " feature" if i == 0 else ""
        cards.append(f'''<li class="work-item{feature}" data-cats="{' '.join(p['categories'])}">
  <a class="work-card tilt" href="work/{p['slug']}.html" data-cursor="View case">
    <div class="work-media reveal-img"><img loading="lazy" src="{p['cover']}" alt="{e(p['title'])}: {e(p['summary'])}"></div>
    <div class="work-meta">
      <h3 class="work-title">{e(p['title'])}{tag(p)}</h3>
      <span class="work-disc">{e(p['discipline'])}</span>
      <p class="work-sum">{e(p['summary'])}</p>
    </div>
  </a>
</li>''')
    ui = []
    for u in UI:
        imgs = "".join(f'<img loading="lazy" class="reveal-img" src="{s}" alt="{e(u["title"])} screen {i+1}">' for i, s in enumerate(u["images"]))
        more = f'<a class="more" href="{u["link"]}">See the full project</a>' if u.get("link") else ""
        ui.append(f'''<article class="ui-case">
  <div class="reveal"><h3>{e(u['title'])}</h3><p class="disc">{e(u['discipline'])}</p><p class="sum">{e(u['summary'])}</p>{more}</div>
  <div class="ui-shots{' one' if len(u['images']) == 1 else ''}">{imgs}</div>
</article>''')
    web = []
    for w in WEB:
        link = f'<a href="{w["url"]}" target="_blank" rel="noopener">Visit live site</a>' if w.get("url") else ""
        web.append(f'''<li class="web-card reveal">
  <div class="shot"><img loading="lazy" src="assets/work/web/{w['slug']}/desktop-0.webp" alt="{e(w['title'])} website, desktop"><div class="phone"><img loading="lazy" src="assets/work/web/{w['slug']}/mobile-0.webp" alt="{e(w['title'])} website, mobile"></div></div>
  <h3>{e(w['title'])}</h3><p class="disc">{e(w['discipline'])}</p><p>{e(w['summary'])}</p>{link}
</li>''')
    services = [
        ("Brand identity", "A complete look for your business, from strategy to a system anyone on your team can use.", ["Logo suite", "Colour and typography", "Brand guidelines", "Tone of voice"]),
        ("Logo design", "A mark that works on a sign, a phone screen and a stamp, with every file you need.", ["Concept directions", "Construction and clear space", "Colour and one-colour versions", "AI, SVG, PDF and PNG files"]),
        ("Packaging", "Cartons, labels, bags and cups designed for the shelf and prepared for the printer.", ["Dielines", "Labels and sleeves", "Carton and polybag artwork", "3D mockups"]),
        ("Business cards and stationery", "Cards people keep, with letterheads, envelopes and email signatures that match.", ["Business cards", "Letterhead and envelope", "Compliments slip", "Print-ready CMYK files"]),
        ("Flyers, print and social", "Campaigns with one clear message, sized for print and for every feed.", ["Flyers and posters", "Menus and brochures", "Social post templates", "Stories and ads"]),
        ("UI/UX design", "Websites and apps that carry your brand properly, from first wireframe to final screens.", ["Website design", "Mobile app screens", "Design systems", "Prototypes"]),
    ]
    sv = "".join(f'<article class="service reveal"><h3>{e(t)}</h3><p>{e(d)}</p><ul>{"".join(f"<li>{e(x)}</li>" for x in li)}</ul></article>' for t, d, li in services)
    steps = [("Discover", "We talk about your business, audience and goals, and agree a written scope."),
             ("Strategize", "Research, positioning and a clear creative direction before any drawing starts."),
             ("Design", "Concepts shown on real items like packaging, signs and screens, then refined with you."),
             ("Build", "The full system: logo files, guidelines, print artwork and digital assets."),
             ("Launch", "Final files handed over, organised and ready for printers and developers. You own the result.")]
    st = "".join(f'<li class="step reveal"><b aria-hidden="true">{i+1}</b><h3>{e(t)}</h3><p>{e(d)}</p></li>' for i, (t, d) in enumerate(steps))
    chips = '<button type="button" class="chip" data-filter="all" aria-pressed="true">All</button>' + "".join(
        f'<button type="button" class="chip" data-filter="{k}" aria-pressed="false">{v}</button>' for k, v in CATS.items())

    body = f'''{header("", True)}
<main id="main">
<span id="top"></span>
<section class="hero">
  <canvas class="hexfield" id="hexfield" aria-hidden="true"></canvas>
  {mark_outline()}
  <div class="wrap hero-inner">
    <p class="hero-kicker"><i></i>{SITE['person']}, graphic designer. Available for selected projects.</p>
    <h1 class="split">Brand identities <em>people remember.</em></h1>
    <div class="hero-row">
      <p class="hero-lede">I design logos, identity systems, packaging, business cards, flyers and interfaces at WA Creative Solution, for businesses that want to look as good as the work they do.</p>
      <div class="hero-actions"><a class="btn magnetic" href="#work">View the work</a><a class="btn btn-line magnetic" href="#contact">Start a project</a></div>
    </div>
    <div class="hero-reel">{reel}</div>
  </div>
  <div class="marquee" aria-hidden="true"><div class="marquee-track">{mq}{mq}</div></div>
  <ul class="sr-only">{"".join(f"<li>{e(x)}</li>" for x in marquee_items)}</ul>
</section>

<section class="section" id="work" aria-labelledby="work-title">
  <div class="wrap">
    <div class="section-head"><h2 id="work-title" class="reveal">Selected work</h2><div class="filters" role="toolbar" aria-label="Filter projects">{chips}</div></div>
    <ul class="work-grid" id="work-grid">{"".join(cards)}</ul>
  </div>
</section>

<section class="section" id="uiux" aria-labelledby="ui-title">
  <div class="wrap">
    <div class="section-head"><h2 id="ui-title" class="reveal">UI/UX design</h2><p class="section-note">Interfaces designed as part of a brand, so the app and the website feel like the same company as the business card.</p></div>
    <div class="ui-list">{"".join(ui)}</div>
    <h3 class="sub-head reveal">Websites, designed and live</h3>
    <p class="section-note">Designed and built at WA Creative Solution. Each one is online now.</p>
    <ul class="web-grid">{"".join(web)}</ul>
  </div>
</section>

<section class="section" id="services" aria-labelledby="services-title">
  <div class="wrap">
    <div class="section-head"><h2 id="services-title" class="reveal">What I can make for you</h2><p class="section-note">Written scope, defined revisions and clear pricing before any work starts.</p></div>
    <div class="services">{sv}</div>
  </div>
</section>

<section class="section" id="process" aria-labelledby="process-title">
  <div class="wrap">
    <div class="section-head"><h2 id="process-title" class="reveal">How a project runs</h2><p class="section-note">Five steps, with your sign-off at each one.</p></div>
    <ol class="steps">{st}</ol>
  </div>
</section>

<section class="section" id="about" aria-labelledby="about-title">
  <div class="wrap about">
    <div class="about-mark reveal-img">{mark("spin")}</div>
    <div class="about-copy">
      <h2 id="about-title" class="reveal">Hi, I'm Waseem.</h2>
      <p>I'm {SITE['person']}, a graphic designer and the founder of WA Creative Solution, a creative studio working from Rawalpindi and Cape Town with clients around the world.</p>
      <p>I believe a brand should do a job. A logo has to be remembered, a package has to be picked up and a guideline has to be easy enough that people actually follow it. Every project here was designed with that job in mind, down to the dielines and the Pantone references.</p>
      <dl class="facts">
        <div><dt>Studio</dt><dd>WA Creative Solution</dd></div>
        <div><dt>Based in</dt><dd>Rawalpindi, Pakistan and Cape Town, South Africa</dd></div>
        <div><dt>Focus</dt><dd>Brand identity, packaging, print, social media, UI/UX</dd></div>
        <div><dt>Tools</dt><dd>Illustrator, Photoshop, InDesign, Figma</dd></div>
      </dl>
    </div>
  </div>
</section>

{contact()}
</main>
{footer("", ["motion.js", "main.js"])}'''
    (ROOT / "index.html").write_text(
        head(f"{SITE['person']} | Brand identity and graphic design portfolio",
             "Portfolio of Muhammad Waseem Akram, graphic designer at WA Creative Solution: brand identities, logos, packaging, business cards, flyers and UI/UX design.", "", P[0]["cover"]) + body)


# ---------------- case pages ----------------
def text_on(hexv):
    h = hexv.lstrip("#"); r, g, b = (int(h[i:i+2], 16) for i in (0, 2, 4))
    return "#080808" if (0.299*r + 0.587*g + 0.114*b) > 150 else "#F5F2EA"


def case(p, nxt):
    pre = "../"
    facts = f'<div><dt>Discipline</dt><dd>{e(p["discipline"])}</dd></div><div><dt>Scope</dt><dd>{e(", ".join(p["services"]))}</dd></div>'
    facts += f'<div><dt>Type</dt><dd>{"Self-initiated concept project" if p.get("concept") else "Client brand project"}</dd></div>'
    system = ""
    if p.get("palette") or p.get("fonts"):
        sw = ""
        if p.get("palette"):
            sw = '<div><h2>Colour palette</h2><ul class="swatches">' + "".join(
                f'<li style="background:{c["hex"]};color:{text_on(c["hex"])}"><b>{e(c["name"])}</b><span>{c["hex"].upper()}</span></li>' for c in p["palette"]) + "</ul></div>"
        ft = ""
        if p.get("fonts") or p.get("values"):
            ft = "<div>"
            if p.get("fonts"):
                ft += '<h2>Typography</h2><ul class="fonts">' + "".join(f'<li><b>{e(f["name"])}</b><span>{e(f["role"])}</span></li>' for f in p["fonts"]) + "</ul>"
            if p.get("values"):
                ft += ('<h2 style="margin-top:28px">Brand personality</h2>' if p.get("fonts") else "<h2>Brand personality</h2>") + '<ul class="values">' + "".join(f"<li>{e(v)}</li>" for v in p["values"]) + "</ul>"
            ft += "</div>"
        system = f'<section class="wrap case-system reveal" aria-label="Brand system">{sw}{ft}</section>'
    gal = "".join(
        f'<figure class="{"half" if g.get("half") else "third" if g.get("third") else ""}"><button type="button" class="reveal-img" data-full="{pre}{g["src"]}" data-cap="{e(g["caption"])}" aria-label="Enlarge: {e(g["caption"])}"><img loading="lazy" src="{pre}{g["src"]}" alt="{e(p["title"])}: {e(g["caption"])}"></button><figcaption>{e(g["caption"])}</figcaption></figure>'
        for g in p["gallery"])
    body = f'''{header(pre, False)}
<main id="main">
<span id="top"></span>
<section class="case-hero">
  <div class="wrap">
    <a class="crumb" href="{pre}index.html#work">All work</a>
    <h1 class="split">{e(p['title'])}</h1>
    <div class="case-top">
      <p class="case-sum reveal">{e(p['summary'])}</p>
      <dl class="case-facts reveal">{facts}</dl>
    </div>
    <div class="case-cover reveal-img parallax"><img src="{pre}{p['cover']}" alt="{e(p['title'])} cover image"></div>
  </div>
</section>
<section class="wrap case-story" aria-label="Project story">
  <div class="reveal"><h2>Overview</h2><p>{e(p['overview'])}</p></div>
  <div class="reveal"><h2>Challenge</h2><p>{e(p['challenge'])}</p></div>
  <div class="reveal"><h2>Solution</h2><p>{e(p['solution'])}</p></div>
</section>
{system}
<section class="wrap gallery" aria-label="Project gallery">{gal}</section>
<div class="wrap">
  <a class="next" href="{nxt['slug']}.html" data-cursor="Next"><small>Next project</small><strong>{e(nxt['title'])}</strong></a>
  <div class="case-cta"><p>Want something like this for your brand?</p><a class="btn magnetic" href="{pre}index.html#contact">Start a project</a></div>
</div>
</main>
<dialog class="lightbox" id="lightbox" aria-label="Image viewer">
  <img id="lb-img" alt="">
  <p id="lb-cap"></p>
  <button type="button" class="lb-btn lb-prev" id="lb-prev" aria-label="Previous image">&#8249;</button>
  <button type="button" class="lb-btn lb-next" id="lb-next" aria-label="Next image">&#8250;</button>
  <button type="button" class="lb-btn lb-close" id="lb-close" aria-label="Close">&#10005;</button>
</dialog>
{footer(pre, ["motion.js", "case.js"])}'''
    (ROOT / "work").mkdir(exist_ok=True)
    (ROOT / "work" / f"{p['slug']}.html").write_text(
        head(f"{p['title']} | {SITE['name']}", p["summary"], pre) + body)


home()
for i, p in enumerate(P):
    case(p, P[(i + 1) % len(P)])
(ROOT / "assets/favicon.svg").write_text(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-6 0 91.67 92"><path fill="#D9B25F" fill-rule="evenodd" d="{HEX}"/><path fill="#111" d="M71.17 27.91 L39.84 9.81 L8.50 27.91 L8.50 64.09 L39.84 82.19 L71.17 64.09 Z"/><path fill="#F5F2EA" fill-rule="evenodd" d="{WA}"/></svg>')
print("built", 1 + len(P), "pages")
