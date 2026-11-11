# Muhammad Waseem Akram — portfolio website

A fast, static website (plain HTML, CSS and JavaScript, no build step). Open `index.html` in a browser to view it.

## Make it yours

1. **Contact details and social links**: edit the top of `js/projects.js` (`email`, `whatsapp`, `location`, `socials`). They appear everywhere automatically.
2. **Your work**: put images in `assets/work/` (JPG, PNG or WebP, about 1600 px wide) and edit the `PROJECTS` list in `js/projects.js`: title, client type, category (`identity`, `logo`, `cards` or `print`), year, image path, a short description and what you delivered. The eight current projects are fictional samples; delete them once yours are in.
3. **Your photo**: in `index.html`, replace the `portrait-placeholder` block in the About section with `<img src="assets/portrait.jpg" alt="Muhammad Waseem Akram">`.
4. **Bio**: edit the About section text in `index.html`.

## Contact form

The form opens the visitor's email app with their message filled in. To receive messages directly without that step, sign up for a free form service such as Formspree or Netlify Forms and point the form at it.

## Hosting (all free)

- **Netlify**: drag this folder onto https://app.netlify.com/drop
- **Vercel**: import the folder or a GitHub repo containing it
- **GitHub Pages**: push to a repo and enable Pages in its settings

## Files

- `index.html` page structure and text
- `css/style.css` design (colours and fonts are at the top)
- `js/projects.js` your content
- `js/main.js` filtering, project pop-up, business card flip, contact form
- `tools/make_placeholders.py` regenerates the sample artwork (not needed once you use real images)
