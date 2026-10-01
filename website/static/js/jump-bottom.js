// Floating bubble that smooth-scrolls to the bottom of the page. Hides
// itself once the visitor is already near the bottom, so it doesn't just
// sit there uselessly next to the footer.
document.addEventListener('DOMContentLoaded', function () {
  var btn = document.getElementById('nkmb-jump-bottom');
  if (!btn) return;

  btn.addEventListener('click', function () {
    window.scrollTo({
      top: document.documentElement.scrollHeight,
      behavior: 'smooth',
    });
  });

  function updateVisibility() {
    var scrollBottom = window.scrollY + window.innerHeight;
    var pageHeight = document.documentElement.scrollHeight;
    var nearBottom = pageHeight - scrollBottom < 120;
    btn.classList.toggle('is-hidden', nearBottom);
  }

  updateVisibility();
  window.addEventListener('scroll', updateVisibility, { passive: true });
  window.addEventListener('resize', updateVisibility);
});
