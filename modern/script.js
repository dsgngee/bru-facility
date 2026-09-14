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
    });
  });
}

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

// Kontaktformular unten: gleiches einfache Feedback
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
