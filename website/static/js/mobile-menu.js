// Toggles the mobile nav menu open/closed, and closes it automatically
// when a link inside it is clicked (so navigating doesn't leave the menu
// stuck open on the next page).
document.addEventListener('DOMContentLoaded', function () {
  var burger = document.getElementById('nkmb-burger');
  var menu = document.getElementById('nkmb-mobile-menu');
  if (!burger || !menu) return;

  function closeMenu() {
    menu.classList.remove('is-open');
    burger.classList.remove('is-open');
    burger.setAttribute('aria-expanded', 'false');
  }

  function toggleMenu() {
    var isOpen = menu.classList.toggle('is-open');
    burger.classList.toggle('is-open', isOpen);
    burger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  }

  burger.addEventListener('click', toggleMenu);

  menu.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', closeMenu);
  });
});
