/* Shared motion: page curtain, scroll reveals, split headlines, progress bar,
   custom cursor, magnetic buttons, tilt cards, parallax and the hero hexagon field. */
(function () {
  "use strict";
  var root = document.documentElement;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var fine = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* safety net: if anything below fails, show everything */
  var showAll = function () { $$(".reveal, .reveal-img, .split").forEach(function (el) { el.classList.add("in"); }); };
  window.addEventListener("error", showAll);
  setTimeout(showAll, 6000);

  /* ---- split headlines into words ---- */
  $$(".split").forEach(function (h) {
    var i = 0;
    var wrap = function (node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3) {
          var frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(function (part) {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(" ")); return; }
            var w = document.createElement("span"); w.className = "w";
            var inner = document.createElement("span"); inner.textContent = part; inner.style.setProperty("--i", i++);
            w.appendChild(inner); frag.appendChild(w);
          });
          node.replaceChild(frag, n);
        } else if (n.nodeType === 1) {
          // keep gradient text working: wrap the element's words but leave the element in place
          if (n.tagName === "EM") { n.style.setProperty("--i", i++); var w = document.createElement("span"); w.className = "w"; n.parentNode.insertBefore(w, n); var s = document.createElement("span"); s.style.setProperty("--i", i); w.appendChild(s); s.appendChild(n); }
          else wrap(n);
        }
      });
    };
    h.setAttribute("aria-label", h.textContent.trim());
    wrap(h);
  });

  /* ---- page curtain ---- */
  var markSvg = document.querySelector(".logo svg");
  if (!reduce) {
    var curtain = document.createElement("div");
    curtain.className = "curtain";
    if (markSvg) { var c = markSvg.cloneNode(true); c.querySelectorAll("path").forEach(function (p) { p.setAttribute("fill", "#080808"); }); curtain.appendChild(c); }
    document.body.appendChild(curtain);
    requestAnimationFrame(function () { requestAnimationFrame(function () { curtain.classList.add("out"); }); });
    setTimeout(function () { curtain.classList.remove("out"); curtain.classList.add("in"); curtain.innerHTML = ""; }, 900);
    document.addEventListener("click", function (e) {
      var a = e.target.closest && e.target.closest("a[href]");
      if (!a || a.target === "_blank" || e.metaKey || e.ctrlKey || e.shiftKey) return;
      var url = new URL(a.href, location.href);
      if (url.origin !== location.origin || url.pathname === location.pathname) return;
      if (!/\.html$|\/$/.test(url.pathname)) return;
      e.preventDefault();
      curtain.classList.add("go");
      setTimeout(function () { location.href = a.href; }, 430);
    });
    window.addEventListener("pageshow", function (e) { if (e.persisted) curtain.classList.remove("go"); });
  }

  /* ---- reveals ---- */
  var targets = $$(".reveal, .reveal-img, .split");
  // stagger siblings that enter together
  $$(".work-grid, .web-grid, .services, .steps, .gallery, .hero-reel, .ui-shots, .case-story").forEach(function (g) {
    $$(".reveal, .reveal-img", g).forEach(function (el, i) { el.style.setProperty("--d", (i % 3) * 110 + "ms"); });
  });
  if (reduce || !("IntersectionObserver" in window)) showAll();
  else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    targets.forEach(function (t) { io.observe(t); });
  }

  /* ---- scroll progress + parallax ---- */
  var bar = document.querySelector(".progress");
  var par = $$(".parallax");
  var ticking = false;
  function onScroll() {
    if (ticking) return; ticking = true;
    requestAnimationFrame(function () {
      var max = document.documentElement.scrollHeight - window.innerHeight;
      if (bar) bar.style.setProperty("--p", max > 0 ? (window.scrollY / max).toFixed(4) : 0);
      if (!reduce) par.forEach(function (p) {
        var r = p.getBoundingClientRect();
        var t = (r.top + r.height / 2 - window.innerHeight / 2) / window.innerHeight;
        p.querySelector("img").style.setProperty("--py", (t * -40).toFixed(1) + "px");
      });
      ticking = false;
    });
  }
  window.addEventListener("scroll", onScroll, { passive: true }); onScroll();

  if (fine && !reduce) {
    /* ---- custom cursor ---- */
    var cur = document.querySelector(".cursor");
    if (cur) {
      var label = cur.querySelector("span");
      window.addEventListener("pointermove", function (e) {
        cur.style.setProperty("--x", e.clientX + "px"); cur.style.setProperty("--y", e.clientY + "px");
        var t = e.target.closest && e.target.closest("[data-cursor]");
        if (t) { label.textContent = t.getAttribute("data-cursor"); cur.style.setProperty("--s", 1); }
        else cur.style.setProperty("--s", 0);
      }, { passive: true });
      document.addEventListener("pointerleave", function () { cur.style.setProperty("--s", 0); });
    }
    /* ---- magnetic buttons ---- */
    $$(".magnetic").forEach(function (b) {
      b.addEventListener("pointermove", function (e) {
        var r = b.getBoundingClientRect();
        b.style.transform = "translate(" + ((e.clientX - r.left - r.width / 2) * 0.28).toFixed(1) + "px," + ((e.clientY - r.top - r.height / 2) * 0.4).toFixed(1) + "px)";
      });
      b.addEventListener("pointerleave", function () { b.style.transform = ""; });
    });
    /* ---- tilt cards ---- */
    $$(".tilt").forEach(function (c) {
      var m = c.querySelector(".work-media");
      c.addEventListener("pointermove", function (e) {
        var r = m.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
        m.style.setProperty("--ry", ((x - 0.5) * 7).toFixed(2) + "deg");
        m.style.setProperty("--rx", ((0.5 - y) * 6).toFixed(2) + "deg");
        m.style.setProperty("--mx", (x * 100).toFixed(1) + "%"); m.style.setProperty("--my", (y * 100).toFixed(1) + "%");
        m.style.setProperty("--glow", 1);
      });
      c.addEventListener("pointerleave", function () { m.style.setProperty("--rx", "0deg"); m.style.setProperty("--ry", "0deg"); m.style.setProperty("--glow", 0); });
    });
  }

  /* ---- hero hexagon field ---- */
  var cv = document.getElementById("hexfield");
  if (cv && cv.getContext) {
    var ctx = cv.getContext("2d"), W, H, dpr, cells = [], R = 34, mouse = { x: -999, y: -999 }, running = true, t0 = performance.now();
    var build = function () {
      var r = cv.getBoundingClientRect();
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      W = r.width; H = r.height; cv.width = W * dpr; cv.height = H * dpr;
      R = W < 700 ? 26 : 34; cells = [];
      var w = Math.sqrt(3) * R, h = 1.5 * R;
      for (var row = -1; row * h < H + R; row++)
        for (var col = -1; col * w < W + w; col++)
          cells.push({ x: col * w + (row % 2 ? w / 2 : 0), y: row * h, e: 0, ph: Math.random() * 6.283 });
    };
    var hex = function (x, y, r) {
      ctx.beginPath();
      for (var i = 0; i < 6; i++) { var a = Math.PI / 3 * i + Math.PI / 6; ctx[i ? "lineTo" : "moveTo"](x + r * Math.cos(a), y + r * Math.sin(a)); }
      ctx.closePath();
    };
    var frame = function (now) {
      if (!running) return;
      var t = (now - t0) / 1000;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.clearRect(0, 0, W, H);
      // a slow diagonal wave of light plus the pointer
      var wave = (t * 140) % (W + H + 600) - 300;
      for (var i = 0; i < cells.length; i++) {
        var c = cells[i];
        var d = Math.hypot(c.x - mouse.x, c.y - mouse.y);
        var target = Math.max(0, 1 - d / 190);
        var wd = Math.abs(c.x + c.y - wave);
        target = Math.max(target, Math.max(0, 1 - wd / 150) * 0.5, (Math.sin(t * 0.8 + c.ph) > 0.985) ? 0.7 : 0);
        c.e += (target - c.e) * (target > c.e ? 0.2 : 0.035);
        var fade = 1 - Math.min(1, Math.max(0, (c.y - H * 0.45) / (H * 0.5)));  // fade toward the bottom
        hex(c.x, c.y, R - 1.5);
        ctx.strokeStyle = "rgba(217,178,95," + ((0.045 + c.e * 0.6) * fade).toFixed(3) + ")";
        ctx.lineWidth = 1; ctx.stroke();
        if (c.e > 0.04) { ctx.fillStyle = "rgba(217,178,95," + (c.e * 0.13 * fade).toFixed(3) + ")"; ctx.fill(); }
      }
      if (!reduce) requestAnimationFrame(frame);
    };
    build(); requestAnimationFrame(frame);
    window.addEventListener("resize", function () { build(); if (reduce) requestAnimationFrame(frame); });
    var hero = cv.parentNode;
    hero.addEventListener("pointermove", function (e) { var r = cv.getBoundingClientRect(); mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top; }, { passive: true });
    hero.addEventListener("pointerleave", function () { mouse.x = mouse.y = -999; });
    if ("IntersectionObserver" in window) new IntersectionObserver(function (en) {
      var vis = en[0].isIntersecting;
      if (vis && !running) { running = true; requestAnimationFrame(frame); } else if (!vis) running = false;
    }).observe(cv);
  }
})();
