// Reveals section headings with a smooth rise-and-fade as they scroll into
// view. Runs once per heading (no replay on repeated scrolling). Hero
// headings and hero photos animate separately, purely in CSS, since they're
// already visible the moment the page opens.
document.addEventListener('DOMContentLoaded', function () {
  var headings = document.querySelectorAll('.nkmb-section-head h2');
  if (!headings.length) return;

  if (!('IntersectionObserver' in window)) {
    headings.forEach(function (h) {
      h.classList.add('is-visible');
    });
    return;
  }

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15, rootMargin: '0px 0px -40px 0px' }
  );

  headings.forEach(function (h) {
    observer.observe(h);
  });
});
