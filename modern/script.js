// Ease-Out-Scroll (Lenis): sanftes Nachlaufen nach dem Scrollen
if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches && window.Lenis) {
  var lenis = new Lenis({ duration: 1.1, easing: function (t) { return 1 - Math.pow(1 - t, 3); } });
  (function raf(time) {
    lenis.raf(time);
    requestAnimationFrame(raf);
  })();
}

// Mobiles Menü
const navToggle = document.getElementById('navToggle');
const mainNav = document.getElementById('mainNav');

if (navToggle && mainNav) {
  navToggle.addEventListener('click', () => {
    const isOpen = mainNav.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  });

  mainNav.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      mainNav.classList.remove('open');
      navToggle.setAttribute('aria-expanded', 'false');
      mainNav.querySelectorAll('.nav-has-dropdown.open').forEach((item) => {
        item.classList.remove('open');
      });
    });
  });
}

// Leistungen-Dropdown im Hauptmenü (Klick öffnet/schließt, wichtig für Touch-Geräte)
document.querySelectorAll('.nav-drop-toggle').forEach((toggle) => {
  toggle.addEventListener('click', () => {
    const item = toggle.closest('.nav-has-dropdown');
    if (!item) return;
    const isOpen = item.classList.toggle('open');
    toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  });
});

document.addEventListener('click', (event) => {
  document.querySelectorAll('.nav-has-dropdown.open').forEach((item) => {
    if (!item.contains(event.target)) {
      item.classList.remove('open');
      const toggle = item.querySelector('.nav-drop-toggle');
      if (toggle) toggle.setAttribute('aria-expanded', 'false');
    }
  });
});

// Schnellanfrage-Formular im Hero: kleines Feedback nach "Absenden"
const quickForm = document.getElementById('quickForm');
if (quickForm) {
  quickForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const button = quickForm.querySelector('button[type="submit"]');
    if (button) {
      button.textContent = 'Danke! Wir melden uns in Kürze ✓';
      button.disabled = true;
    }
  });
}

// Kontaktformular (kontakt.html): gleiches einfache Feedback
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const button = contactForm.querySelector('button[type="submit"]');
    if (button) {
      button.textContent = 'Danke! Wir melden uns in Kürze ✓';
      button.disabled = true;
    }
  });
}

// Vorauswahl des Leistungsbereichs, wenn von einer Kategorieseite verlinkt
// (z. B. kontakt.html?leistung=Winterdienst)
const params = new URLSearchParams(location.search);
const preselect = params.get('leistung');
if (preselect) {
  const select = document.querySelector('select[name="bereich"]');
  if (select) {
    const match = [...select.options].find(o => o.value === preselect || o.textContent.trim() === preselect);
    if (match) select.value = match.value;
  }
}
