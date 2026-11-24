// Client-side filters for the archive page: rubrique, auteur, année, titre.
(function () {
  var form = document.getElementById('filtres');
  if (!form) return;
  var cards = Array.prototype.slice.call(document.querySelectorAll('#archive .card'));
  var nb = document.getElementById('nb');
  var aucun = document.getElementById('aucun');

  function norm(s) {
    return (s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
  }

  function apply() {
    var theme = form.theme.value, auteur = form.auteur.value, annee = form.annee.value;
    var q = norm(form.q.value.trim());
    var shown = 0;
    cards.forEach(function (c) {
      var ok = (!theme || (' ' + c.dataset.themes).indexOf(' ' + theme + ' ') >= 0) &&
               (!auteur || (' ' + c.dataset.auteurs).indexOf(' ' + auteur + ' ') >= 0) &&
               (!annee || c.dataset.annee === annee) &&
               (!q || norm(c.dataset.titre).indexOf(q) >= 0);
      c.hidden = !ok;
      if (ok) shown++;
    });
    // Hide empty issue / year blocks.
    document.querySelectorAll('#archive .issue, #archive .year').forEach(function (s) {
      s.hidden = !s.querySelector('.card:not([hidden])');
    });
    nb.textContent = shown;
    aucun.hidden = shown > 0;
    var params = new URLSearchParams();
    ['theme', 'auteur', 'annee', 'q'].forEach(function (k) { if (form[k].value) params.set(k, form[k].value); });
    history.replaceState(null, '', params.toString() ? '?' + params : location.pathname);
  }

  // Restore filters from the URL so filtered views can be shared.
  var init = new URLSearchParams(location.search);
  ['theme', 'auteur', 'annee', 'q'].forEach(function (k) { if (init.get(k)) form[k].value = init.get(k); });
  form.addEventListener('input', apply);
  form.addEventListener('change', apply);
  apply();
})();
