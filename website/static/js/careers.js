(function () {
  var chips = document.querySelectorAll('.car-chip');
  var roles = document.querySelectorAll('.car-role');
  var count = document.getElementById('car-count');
  var empty = document.getElementById('car-empty');

  function applyFilter(cat) {
    var shown = 0;
    roles.forEach(function (r) {
      var on = cat === 'All' || r.dataset.dept === cat;
      r.hidden = !on;
      if (on) shown++;
    });
    chips.forEach(function (c) {
      var active = c.dataset.cat === cat;
      c.classList.toggle('is-on', active);
      c.setAttribute('aria-pressed', active ? 'true' : 'false');
    });
    if (count) count.textContent = shown + (shown === 1 ? ' open role' : ' open roles');
    if (empty) empty.hidden = shown !== 0;
  }
  chips.forEach(function (c) {
    c.addEventListener('click', function () { applyFilter(c.dataset.cat); });
  });

  document.querySelectorAll('.car-toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var role = btn.closest('.car-role');
      var open = role.classList.toggle('is-open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.querySelector('.lbl').textContent = open ? 'Hide details' : 'View details';
    });
  });
})();
