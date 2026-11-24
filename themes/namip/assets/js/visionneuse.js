/* Visionneuse d'images : parcourt les images de l'article (galeries et images isolées).
   Commandes : boutons ‹ › ×, flèches ← →, Début/Fin, Échap, clic hors de l'image, glissement tactile. */
(function () {
  "use strict";
  var content = document.querySelector(".article .content");
  if (!content) return;

  var IMG_RE = /\.(jpe?g|png|gif|webp|bmp|svg)(\?.*)?$/i;
  var items = [];

  content.querySelectorAll("img").forEach(function (img) {
    var link = img.closest("a");
    // Une image qui pointe vers une autre page (logo, bannière) garde son lien.
    if (link && !IMG_RE.test(link.getAttribute("href") || "")) return;
    var fig = img.closest("figure");
    var cap = fig && fig.querySelector("figcaption");
    var item = {
      src: link ? link.href : img.currentSrc || img.src,
      caption: (cap ? cap.textContent : img.alt || img.title || "").trim(),
      trigger: link || img
    };
    items.push(item);
    var index = items.length - 1;
    var trigger = item.trigger;
    if (!link) {
      trigger.setAttribute("tabindex", "0");
      trigger.setAttribute("role", "button");
    }
    trigger.classList.add("zoomable");
    trigger.setAttribute("aria-label", "Agrandir l'image" + (item.caption ? " : " + item.caption : ""));
    trigger.addEventListener("click", function (e) {
      if (e.ctrlKey || e.metaKey || e.shiftKey || e.button === 1) return; // ouvrir dans un onglet reste possible
      e.preventDefault();
      open(index);
    });
    if (!link) {
      trigger.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); open(index); }
      });
    }
  });
  if (!items.length) return;

  var box = document.createElement("div");
  box.className = "lightbox";
  box.hidden = true;
  box.setAttribute("role", "dialog");
  box.setAttribute("aria-modal", "true");
  box.setAttribute("aria-label", "Visionneuse d'images");
  box.innerHTML =
    '<div class="lb-bar"><span class="lb-count" aria-live="polite"></span>' +
    '<button type="button" class="lb-close" aria-label="Fermer et revenir à l\'article" title="Fermer (Échap)">×</button></div>' +
    '<button type="button" class="lb-prev" aria-label="Image précédente" title="Précédente (←)">‹</button>' +
    '<figure class="lb-stage"><img alt=""><figcaption class="lb-caption"></figcaption></figure>' +
    '<button type="button" class="lb-next" aria-label="Image suivante" title="Suivante (→)">›</button>';
  document.body.appendChild(box);

  var imgEl = box.querySelector(".lb-stage img");
  var capEl = box.querySelector(".lb-caption");
  var countEl = box.querySelector(".lb-count");
  var prevBtn = box.querySelector(".lb-prev");
  var nextBtn = box.querySelector(".lb-next");
  var closeBtn = box.querySelector(".lb-close");
  var current = 0;
  var lastFocus = null;

  function show(i) {
    current = (i + items.length) % items.length;
    var it = items[current];
    box.classList.add("loading");
    imgEl.onload = imgEl.onerror = function () { box.classList.remove("loading"); };
    imgEl.src = it.src;
    imgEl.alt = it.caption;
    capEl.textContent = it.caption;
    capEl.hidden = !it.caption;
    countEl.textContent = (current + 1) + " / " + items.length;
    var single = items.length < 2;
    prevBtn.hidden = nextBtn.hidden = single;
    // Précharge les voisines pour un défilement fluide.
    if (!single) {
      [current + 1, current - 1].forEach(function (j) {
        new Image().src = items[(j + items.length) % items.length].src;
      });
    }
  }

  function open(i) {
    lastFocus = document.activeElement;
    show(i);
    box.hidden = false;
    document.documentElement.classList.add("lb-open");
    closeBtn.focus();
  }

  function close() {
    box.hidden = true;
    imgEl.removeAttribute("src");
    document.documentElement.classList.remove("lb-open");
    var t = items[current].trigger;
    (t || lastFocus).focus({ preventScroll: true });
    t.scrollIntoView({ block: "nearest" });
  }

  prevBtn.addEventListener("click", function () { show(current - 1); });
  nextBtn.addEventListener("click", function () { show(current + 1); });
  closeBtn.addEventListener("click", close);
  box.addEventListener("click", function (e) {
    if (e.target === box || e.target.classList.contains("lb-stage")) close();
  });

  document.addEventListener("keydown", function (e) {
    if (box.hidden) return;
    switch (e.key) {
      case "ArrowLeft": show(current - 1); break;
      case "ArrowRight": show(current + 1); break;
      case "Home": show(0); break;
      case "End": show(items.length - 1); break;
      case "Escape": close(); break;
      case "Tab": // garde le focus dans la visionneuse
        var f = [closeBtn, prevBtn, nextBtn].filter(function (b) { return !b.hidden; });
        var k = f.indexOf(document.activeElement);
        k = e.shiftKey ? (k <= 0 ? f.length - 1 : k - 1) : (k + 1) % f.length;
        f[k].focus();
        break;
      default: return;
    }
    e.preventDefault();
  });

  // Glissement horizontal sur écran tactile.
  var x0 = null, y0 = null;
  box.addEventListener("touchstart", function (e) {
    if (e.touches.length === 1) { x0 = e.touches[0].clientX; y0 = e.touches[0].clientY; }
  }, { passive: true });
  box.addEventListener("touchend", function (e) {
    if (x0 === null) return;
    var dx = e.changedTouches[0].clientX - x0, dy = e.changedTouches[0].clientY - y0;
    x0 = null;
    if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy)) show(current + (dx < 0 ? 1 : -1));
  });
})();
