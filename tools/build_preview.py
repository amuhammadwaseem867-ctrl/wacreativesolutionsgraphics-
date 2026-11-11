"""Builds a single-page preview (inlined CSS/JS) for the hosted Claude preview."""
from pathlib import Path
import re, sys
root = Path(__file__).resolve().parent.parent
out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
html = (root/"index.html").read_text()
page = html.split("<!--PAGE-START-->")[1].split("<!--PAGE-END-->")[0]
font = re.search(r'<link rel="stylesheet" href="(https://fonts[^"]+)">', html).group(1)
css = (root/"css/style.css").read_text()
js = (root/"js/projects.js").read_text() + "\n" + (root/"js/main.js").read_text()
doc = f'''<title>Waseem Akram Portfolio</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="{font}">
<style>{css}</style>
{page}
<script>{js}</script>
'''
(out/"index.html").write_text(doc)
