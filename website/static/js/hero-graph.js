// Draws the hero line graph whenever it scrolls into view: the line
// traces its path, then the end-dot and labels settle in. Replays each
// time you scroll back to it — not just once per page load. No
// framework — just this file.
document.addEventListener('DOMContentLoaded', function () {
  var svg = document.querySelector('.nkmb-hero-graph');
  if (!svg) return;

  var line = svg.querySelector('.draw-line');
  if (!line) return;

  var length = Math.ceil(line.getTotalLength());
  line.style.setProperty('--len', length);

  function play() {
    svg.classList.remove('is-drawn');
    // Force a reflow so the removed class registers before we re-add it —
    // otherwise the browser can coalesce both changes and skip the animation.
    void svg.getBoundingClientRect();
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        svg.classList.add('is-drawn');
      });
    });
  }

  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) play();
        });
      },
      { threshold: 0.4 }
    );
    observer.observe(svg);
  } else {
    play();
  }
});
