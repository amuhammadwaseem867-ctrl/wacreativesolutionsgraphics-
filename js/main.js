/* Home page: work filter, copy email, contact form. */
(function () {
  "use strict";
  var EMAIL = "amuhammadwaseem867@gmail.com";

  var chips = document.querySelectorAll(".chip");
  var items = document.querySelectorAll(".work-item");
  chips.forEach(function (c) {
    c.addEventListener("click", function () {
      var f = c.dataset.filter;
      chips.forEach(function (x) { x.setAttribute("aria-pressed", String(x === c)); });
      items.forEach(function (it) {
        var show = f === "all" || it.dataset.cats.split(" ").indexOf(f) > -1;
        it.hidden = !show;
        if (show) it.querySelectorAll(".reveal-img").forEach(function (el) { el.classList.add("in"); });
      });
    });
  });

  var copy = document.getElementById("copy-email");
  if (copy) copy.addEventListener("click", function () {
    var done = function () { copy.textContent = "Copied"; setTimeout(function () { copy.textContent = "Copy"; }, 1800); };
    var fallback = function () {
      var range = document.createRange(); range.selectNodeContents(document.getElementById("email-val"));
      var sel = window.getSelection(); sel.removeAllRanges(); sel.addRange(range); copy.textContent = "Press Ctrl+C";
    };
    try { navigator.clipboard.writeText(EMAIL).then(done, fallback); } catch (e) { fallback(); }
  });

  var form = document.getElementById("contact-form");
  var status = document.getElementById("form-status");
  if (form) form.addEventListener("submit", function (e) {
    e.preventDefault();
    var ok = true;
    ["f-name", "f-email", "f-msg"].forEach(function (id) {
      var el = document.getElementById(id);
      var bad = !el.value.trim() || (el.type === "email" && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(el.value));
      el.closest(".field").classList.toggle("invalid", bad); el.setAttribute("aria-invalid", String(bad));
      if (bad) ok = false;
    });
    if (!ok) { status.textContent = "Add your name, a valid email and a few words about the project."; return; }
    var d = new FormData(form);
    var subject = d.get("type") + " enquiry from " + d.get("name");
    var body = d.get("message") + "\n\nTimeline: " + d.get("when") + "\nReply to: " + d.get("email");
    window.location.href = "mailto:" + EMAIL + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    status.textContent = "Your email app should open with the message ready to send. If it doesn't, email " + EMAIL + " directly.";
  });
})();
