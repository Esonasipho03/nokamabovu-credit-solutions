// A small testimonial slideshow: one quote visible at a time, with
// prev/next arrows, clickable dots, and gentle auto-advance that pauses
// once the person interacts with it.
document.addEventListener('DOMContentLoaded', function () {
  var slider = document.getElementById('testimonial-slider');
  if (!slider) return;

  var track = slider.querySelector('.nkmb-testimonial-track');
  var slides = slider.querySelectorAll('.nkmb-testimonial-slide');
  var dotsWrap = document.getElementById('testimonial-dots');
  var arrows = slider.querySelectorAll('.nkmb-slide-arrow');
  if (!track || slides.length < 2) return; // nothing to slide between

  var index = 0;
  var autoplayId = null;

  slides.forEach(function (_, i) {
    var dot = document.createElement('button');
    dot.setAttribute('aria-label', 'Go to testimonial ' + (i + 1));
    if (i === 0) dot.classList.add('is-active');
    dot.addEventListener('click', function () {
      goTo(i);
      stopAutoplay();
    });
    dotsWrap.appendChild(dot);
  });

  var dots = dotsWrap.querySelectorAll('button');

  function goTo(i) {
    index = (i + slides.length) % slides.length;
    track.style.transform = 'translateX(-' + index * 100 + '%)';
    dots.forEach(function (d, di) {
      d.classList.toggle('is-active', di === index);
    });
  }

  arrows.forEach(function (arrow) {
    arrow.addEventListener('click', function () {
      goTo(index + parseInt(arrow.dataset.dir, 10));
      stopAutoplay();
    });
  });

  function startAutoplay() {
    autoplayId = setInterval(function () {
      goTo(index + 1);
    }, 6000);
  }
  function stopAutoplay() {
    if (autoplayId) clearInterval(autoplayId);
  }

  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    startAutoplay();
  }
});
