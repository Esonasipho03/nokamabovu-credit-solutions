// A back-to-top bubble that only appears once the visitor has scrolled
// near the bottom of the page, and smooth-scrolls back to the top on click.
document.addEventListener('DOMContentLoaded', function () {
  var btn = document.getElementById('nkmb-back-top');
  if (!btn) return;

  btn.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  function updateVisibility() {
    var scrollBottom = window.scrollY + window.innerHeight;
    var pageHeight = document.documentElement.scrollHeight;
    var nearBottom = pageHeight - scrollBottom < 400;
    btn.classList.toggle('is-visible', nearBottom);
  }

  updateVisibility();
  window.addEventListener('scroll', updateVisibility, { passive: true });
  window.addEventListener('resize', updateVisibility);
  window.addEventListener('load', updateVisibility);
});
