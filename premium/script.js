// Ease-Out-Scroll (Lenis): sanftes Nachlaufen nach dem Scrollen
if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches && window.Lenis) {
  var lenis = new Lenis({ duration: 1.1, easing: function (t) { return 1 - Math.pow(1 - t, 3); } });
  (function raf(time) {
    lenis.raf(time);
    requestAnimationFrame(raf);
  })();
}

document.addEventListener('DOMContentLoaded', function () {

  // Mobile navigation toggle
  var navToggle = document.getElementById('navToggle');
  var mainNav = document.getElementById('mainNav');
  if (navToggle && mainNav) {
    navToggle.addEventListener('click', function () {
      mainNav.classList.toggle('open');
      navToggle.classList.toggle('active');
    });
    mainNav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        mainNav.classList.remove('open');
        navToggle.classList.remove('active');
      });
    });
  }

  // Nav dropdown ("Leistungen"): click-to-toggle, works on desktop and inside the mobile overlay menu
  var dropdownItems = document.querySelectorAll('.nav-has-dropdown');
  dropdownItems.forEach(function (item) {
    var caret = item.querySelector('.nav-caret');
    if (!caret) return;
    caret.addEventListener('click', function (e) {
      e.preventDefault();
      var isOpen = item.classList.toggle('open');
      caret.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function (e) {
    dropdownItems.forEach(function (item) {
      if (item.classList.contains('open') && !item.contains(e.target)) {
        item.classList.remove('open');
        var caret = item.querySelector('.nav-caret');
        if (caret) caret.setAttribute('aria-expanded', 'false');
      }
    });
  });

  // Gallery lightbox
  var lightbox = document.getElementById('lightbox');
  var lightboxImg = document.getElementById('lightboxImg');
  var lightboxCaption = document.getElementById('lightboxCaption');
  var lightboxClose = document.getElementById('lightboxClose');
  var galleryItems = document.querySelectorAll('.gallery-item');

  function openLightbox(src, caption) {
    lightboxImg.src = src;
    lightboxImg.alt = caption || '';
    lightboxCaption.textContent = caption || '';
    lightbox.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    lightbox.classList.remove('open');
    document.body.style.overflow = '';
  }

  galleryItems.forEach(function (item) {
    item.addEventListener('click', function () {
      openLightbox(item.getAttribute('data-full'), item.getAttribute('data-caption'));
    });
  });

  if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
  if (lightbox) {
    lightbox.addEventListener('click', function (e) {
      if (e.target === lightbox) closeLightbox();
    });
  }
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeLightbox();
  });

  // Kontaktformular: Leistung per Query-Parameter vorbelegen (z. B. kontakt.html?leistung=Winterdienst)
  var params = new URLSearchParams(location.search);
  var preselect = params.get('leistung');
  if (preselect) {
    var select = document.querySelector('select[name="bereich"]');
    if (select) {
      var match = [].slice.call(select.options).find(function (o) {
        return o.value === preselect || o.textContent.trim() === preselect;
      });
      if (match) select.value = match.value;
    }
  }

  // Rezensionen: Feature-Karussell (Slides, Punkte, Swipe)
  var rezFeatureTrack = document.getElementById('rezFeatureTrack');
  if (rezFeatureTrack) {
    var rezSlides = rezFeatureTrack.querySelectorAll('.rez-feature-slide');
    var rezDots = document.getElementById('rezFeatureDots');
    var rezIndex = 0;

    rezSlides.forEach(function (_, i) {
      var dot = document.createElement('button');
      dot.type = 'button';
      dot.className = 'rez-feature-dot';
      dot.setAttribute('aria-label', 'Rezension ' + (i + 1) + ' von ' + rezSlides.length + ' anzeigen');
      dot.addEventListener('click', function () { goToRezSlide(i); });
      rezDots.appendChild(dot);
    });
    var rezDotEls = rezDots.querySelectorAll('.rez-feature-dot');

    function goToRezSlide(i) {
      rezIndex = (i + rezSlides.length) % rezSlides.length;
      rezFeatureTrack.style.transform = 'translateX(-' + (rezIndex * 100) + '%)';
      rezDotEls.forEach(function (d, di) { d.classList.toggle('active', di === rezIndex); });
    }
    goToRezSlide(0);

    var rezFeaturePrev = document.querySelector('[data-rez-feature-prev]');
    var rezFeatureNext = document.querySelector('[data-rez-feature-next]');
    if (rezFeaturePrev) rezFeaturePrev.addEventListener('click', function () { goToRezSlide(rezIndex - 1); });
    if (rezFeatureNext) rezFeatureNext.addEventListener('click', function () { goToRezSlide(rezIndex + 1); });

    var rezTouchStartX = null;
    rezFeatureTrack.addEventListener('touchstart', function (e) { rezTouchStartX = e.touches[0].clientX; }, { passive: true });
    rezFeatureTrack.addEventListener('touchend', function (e) {
      if (rezTouchStartX === null) return;
      var delta = e.changedTouches[0].clientX - rezTouchStartX;
      if (Math.abs(delta) > 40) goToRezSlide(rezIndex + (delta < 0 ? 1 : -1));
      rezTouchStartX = null;
    });
  }

  // Contact form: no backend yet, show inline confirmation
  var form = document.getElementById('contactForm');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = form.querySelector('button[type="submit"]');
      if (btn) {
        btn.textContent = 'Danke! Wir melden uns.';
        btn.disabled = true;
      }
    });
  }

});
