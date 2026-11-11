/* Case study pages: image lightbox with keyboard navigation. */
(function () {
  "use strict";
  var dlg = document.getElementById("lightbox");
  if (!dlg) return;
  var btns = Array.prototype.slice.call(document.querySelectorAll(".gallery button"));
  var img = document.getElementById("lb-img"), cap = document.getElementById("lb-cap"), i = 0;
  function show(n) {
    i = (n + btns.length) % btns.length;
    img.src = btns[i].dataset.full; img.alt = btns[i].dataset.cap; cap.textContent = btns[i].dataset.cap + "  (" + (i + 1) + " of " + btns.length + ")";
  }
  btns.forEach(function (b, n) {
    b.addEventListener("click", function () { show(n); if (dlg.showModal) dlg.showModal(); else dlg.setAttribute("open", ""); });
  });
  document.getElementById("lb-prev").addEventListener("click", function () { show(i - 1); });
  document.getElementById("lb-next").addEventListener("click", function () { show(i + 1); });
  document.getElementById("lb-close").addEventListener("click", function () { dlg.close(); });
  dlg.addEventListener("click", function (e) { if (e.target === dlg || e.target === img) dlg.close(); });
  dlg.addEventListener("keydown", function (e) { if (e.key === "ArrowRight") show(i + 1); if (e.key === "ArrowLeft") show(i - 1); });
})();
