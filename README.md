# WA Creative Solution graphics portfolio

Portfolio of Muhammad Waseem Akram: brand identity, packaging, print, social media and UI/UX.
Plain HTML, CSS and JavaScript. No build step is needed to host it.

## Editing

1. All projects live in `content/projects.json` (title, summary, palette, gallery images).
2. After editing it, run `python3 tools/build.py` to regenerate `index.html` and `work/*.html`.
3. Images are in `assets/work/<project>/`.
4. Contact details and social links are at the top of `tools/build.py` (`SITE`).
5. Colours and fonts are at the top of `css/style.css`. Animations are in `css/motion.css` and `js/motion.js`.

## Hosting on GitHub Pages

Repository Settings > Pages > Deploy from a branch > `main` / root.
