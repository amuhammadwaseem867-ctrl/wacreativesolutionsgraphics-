(function () {
  "use strict";
  var SITE = window.SITE, PROJECTS = window.PROJECTS, CATS = window.CATEGORIES;
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- fill in contact details from projects.js ---- */
  document.querySelectorAll("[data-site]").forEach(function (el) {
    var v = SITE[el.getAttribute("data-site")];
    if (v) el.textContent = v;
  });
  var wa = document.getElementById("wa-link");
  if (wa) wa.href = "https://wa.me/" + SITE.whatsapp.replace(/[^\d]/g, "");
  var socials = document.getElementById("socials");
  SITE.socials.forEach(function (s) {
    var li = document.createElement("li");
    var a = document.createElement("a");
    a.href = s.url; a.textContent = s.label; a.target = "_blank"; a.rel = "noopener";
    li.appendChild(a); socials.appendChild(li);
  });
  var yr = document.getElementById("year");
  if (yr) yr.textContent = new Date().getFullYear();

  /* ---- header border on scroll ---- */
  var header = document.querySelector(".site-header");
  function onScroll() { header.classList.toggle("scrolled", window.scrollY > 8); }
  window.addEventListener("scroll", onScroll, { passive: true }); onScroll();

  /* ---- business card: flip on press, tilt with the pointer ---- */
  var card = document.getElementById("bizcard");
  card.addEventListener("click", function () {
    var flipped = card.getAttribute("aria-pressed") === "true";
    card.setAttribute("aria-pressed", String(!flipped));
  });
  card.addEventListener("animationend", function () { card.style.animation = "none"; });
  if (!reduceMotion && window.matchMedia("(hover: hover)").matches) {
    var area = document.querySelector(".hero-card-area");
    area.addEventListener("pointermove", function (e) {
      var r = card.getBoundingClientRect();
      var x = (e.clientX - r.left) / r.width - 0.5;
      var y = (e.clientY - r.top) / r.height - 0.5;
      card.style.setProperty("--ry", (x * 14).toFixed(2) + "deg");
      card.style.setProperty("--rx", (-y * 14).toFixed(2) + "deg");
    });
    area.addEventListener("pointerleave", function () {
      card.style.setProperty("--ry", "0deg");
      card.style.setProperty("--rx", "0deg");
    });
  }

  /* ---- work grid ---- */
  var grid = document.getElementById("work-grid");
  var current = "all";
  var visible = [];
  var PATTERN = ["wide", "narrow", "narrow", "wide"];

  function render() {
    visible = PROJECTS.filter(function (p) { return current === "all" || p.category === current; });
    grid.innerHTML = "";
    visible.forEach(function (p, i) {
      var li = document.createElement("li");
      var size = PATTERN[i % PATTERN.length];
      // a lone item in the last row spans the full width
      if (visible.length % 2 === 1 && i === visible.length - 1) size = "full";
      li.className = "work-item " + size;
      li.innerHTML =
        '<button type="button" class="work-link" aria-haspopup="dialog">' +
          '<span class="work-media"><img loading="lazy" alt=""><span class="work-view" aria-hidden="true">View project</span></span>' +
          '<span class="work-caption"><span><span class="work-title"></span><br><span class="work-client"></span></span><span class="work-cat"></span></span>' +
        "</button>";
      var img = li.querySelector("img");
      img.src = p.image; img.alt = p.alt;
      li.querySelector(".work-title").textContent = p.title;
      li.querySelector(".work-client").textContent = p.client + ", " + p.year;
      li.querySelector(".work-cat").textContent = CATS[p.category];
      li.querySelector(".work-link").addEventListener("click", function () { openProject(i); });
      grid.appendChild(li);
    });
  }

  function setFilter(f) {
    current = f;
    document.querySelectorAll(".chip").forEach(function (c) {
      c.setAttribute("aria-pressed", String(c.dataset.filter === f));
    });
    render();
  }
  document.querySelectorAll(".chip").forEach(function (c) {
    c.addEventListener("click", function () { setFilter(c.dataset.filter); });
  });
  document.querySelectorAll("[data-jump]").forEach(function (a) {
    a.addEventListener("click", function () { setFilter(a.dataset.jump); });
  });
  render();

  /* ---- project dialog ---- */
  var dlg = document.getElementById("project-dialog");
  var idx = 0;
  function fill(i) {
    idx = (i + visible.length) % visible.length;
    var p = visible[idx];
    document.getElementById("pd-img").src = p.image;
    document.getElementById("pd-img").alt = p.alt;
    document.getElementById("pd-meta").textContent = CATS[p.category] + " for a " + p.client.toLowerCase() + ", " + p.year;
    document.getElementById("pd-title").textContent = p.title;
    document.getElementById("pd-brief").textContent = p.brief;
    var ul = document.getElementById("pd-list");
    ul.innerHTML = "";
    p.deliverables.forEach(function (d) { var li = document.createElement("li"); li.textContent = d; ul.appendChild(li); });
    var single = visible.length < 2;
    document.getElementById("pd-prev").hidden = single;
    document.getElementById("pd-next").hidden = single;
  }
  function openProject(i) {
    fill(i);
    if (typeof dlg.showModal === "function") dlg.showModal(); else dlg.setAttribute("open", "");
  }
  document.getElementById("pd-close").addEventListener("click", function () { dlg.close(); });
  document.getElementById("pd-prev").addEventListener("click", function () { fill(idx - 1); });
  document.getElementById("pd-next").addEventListener("click", function () { fill(idx + 1); });
  dlg.addEventListener("click", function (e) { if (e.target === dlg) dlg.close(); });
  dlg.addEventListener("keydown", function (e) {
    if (e.key === "ArrowRight") fill(idx + 1);
    if (e.key === "ArrowLeft") fill(idx - 1);
  });

  /* ---- copy email ---- */
  document.querySelectorAll("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var value = SITE[btn.dataset.copy];
      var done = function () { btn.textContent = "Copied"; setTimeout(function () { btn.textContent = "Copy"; }, 1800); };
      var fallback = function () {
        var target = btn.parentNode.querySelector(".contact-value");
        var range = document.createRange(); range.selectNodeContents(target);
        var sel = window.getSelection(); sel.removeAllRanges(); sel.addRange(range);
        btn.textContent = "Press Ctrl+C";
      };
      try {
        navigator.clipboard.writeText(value).then(done, fallback);
      } catch (err) { fallback(); }
    });
  });

  /* ---- contact form: opens the visitor's email app with the message filled in ---- */
  var form = document.getElementById("contact-form");
  var status = document.getElementById("form-status");
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var ok = true;
    ["f-name", "f-email", "f-msg"].forEach(function (id) {
      var el = document.getElementById(id);
      var bad = !el.value.trim() || (el.type === "email" && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(el.value));
      el.closest(".field").classList.toggle("invalid", bad);
      el.setAttribute("aria-invalid", String(bad));
      if (bad) ok = false;
    });
    if (!ok) {
      status.textContent = "Add your name, a valid email and a few words about the project.";
      return;
    }
    var d = new FormData(form);
    var subject = d.get("type") + " enquiry from " + d.get("name");
    var body = d.get("message") + "\n\nTimeline: " + d.get("when") + "\nReply to: " + d.get("email");
    window.location.href = "mailto:" + SITE.email + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    status.textContent = "Your email app should open with the message ready to send. If it doesn't, email " + SITE.email + " directly.";
  });
})();
