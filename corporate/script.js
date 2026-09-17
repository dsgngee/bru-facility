// Ease-Out-Scroll (Lenis): sanftes Nachlaufen nach dem Scrollen
if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches && window.Lenis) {
  var lenis = new Lenis({ duration: 1.1, easing: function (t) { return 1 - Math.pow(1 - t, 3); } });
  (function raf(time) {
    lenis.raf(time);
    requestAnimationFrame(raf);
  })();
}

const navToggle = document.getElementById('navToggle');
const mainNav = document.getElementById('mainNav');
navToggle.addEventListener('click', () => {
  const isOpen = mainNav.classList.toggle('open');
  if (isOpen) {
    const header = document.querySelector('.site-header');
    mainNav.style.top = header.getBoundingClientRect().bottom + 'px';
  }
});

// Leistungen-Dropdown im Hauptmenü (Klick, funktioniert auf Desktop und Mobile)
document.querySelectorAll('.nav-dropdown-toggle').forEach((btn) => {
  btn.addEventListener('click', (e) => {
    e.stopPropagation();
    const item = btn.closest('.nav-item');
    const isOpen = item.classList.contains('open');
    document.querySelectorAll('.nav-item.open').forEach((el) => {
      if (el !== item) {
        el.classList.remove('open');
        const toggle = el.querySelector('.nav-dropdown-toggle');
        if (toggle) toggle.setAttribute('aria-expanded', 'false');
      }
    });
    item.classList.toggle('open', !isOpen);
    btn.setAttribute('aria-expanded', String(!isOpen));
  });
});
document.addEventListener('click', (e) => {
  document.querySelectorAll('.nav-item.open').forEach((item) => {
    if (!item.contains(e.target)) {
      item.classList.remove('open');
      const toggle = item.querySelector('.nav-dropdown-toggle');
      if (toggle) toggle.setAttribute('aria-expanded', 'false');
    }
  });
});

// Kontaktformular: rein clientseitig, kein Backend vorhanden
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    contactForm.reset();
    const successMsg = document.getElementById('formSuccess');
    if (successMsg) {
      successMsg.hidden = false;
      successMsg.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  });
}

// Vorauswahl des Leistungsbereichs über den Query-Parameter (?leistung=...)
const params = new URLSearchParams(location.search);
const preselect = params.get('leistung');
if (preselect) {
  const select = document.querySelector('select[name="bereich"]');
  if (select) {
    const match = [...select.options].find(o => o.value === preselect || o.textContent.trim() === preselect);
    if (match) select.value = match.value;
  }
}
