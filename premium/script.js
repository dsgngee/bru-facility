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

  // Gallery lightbox: blättert durch alle Galerie-Bilder
  var lightbox = document.getElementById('lightbox');
  var lightboxImg = document.getElementById('lightboxImg');
  var lightboxCaption = document.getElementById('lightboxCaption');
  var lightboxCounter = document.getElementById('lightboxCounter');
  var lightboxClose = document.getElementById('lightboxClose');
  var lightboxPrev = document.getElementById('lightboxPrev');
  var lightboxNext = document.getElementById('lightboxNext');
  var galleryItems = [].slice.call(document.querySelectorAll('.gallery-item'));
  var lightboxIndex = 0;

  function showLightboxItem(i) {
    lightboxIndex = (i + galleryItems.length) % galleryItems.length;
    var item = galleryItems[lightboxIndex];
    var caption = item.getAttribute('data-caption') || '';
    lightboxImg.src = item.getAttribute('data-full');
    lightboxImg.alt = caption;
    lightboxCaption.textContent = caption;
    if (lightboxCounter) lightboxCounter.textContent = galleryItems.length > 1 ? (lightboxIndex + 1) + ' / ' + galleryItems.length : '';
  }

  function openLightbox(i) {
    if (lightboxPrev) lightboxPrev.hidden = galleryItems.length < 2;
    if (lightboxNext) lightboxNext.hidden = galleryItems.length < 2;
    showLightboxItem(i);
    lightbox.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    lightbox.classList.remove('open');
    document.body.style.overflow = '';
  }

  galleryItems.forEach(function (item, i) {
    item.addEventListener('click', function () { openLightbox(i); });
  });

  if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
  if (lightboxPrev) lightboxPrev.addEventListener('click', function () { showLightboxItem(lightboxIndex - 1); });
  if (lightboxNext) lightboxNext.addEventListener('click', function () { showLightboxItem(lightboxIndex + 1); });
  if (lightbox) {
    lightbox.addEventListener('click', function (e) {
      if (e.target === lightbox) closeLightbox();
    });
    var lbTouchStartX = null;
    lightbox.addEventListener('touchstart', function (e) { lbTouchStartX = e.touches[0].clientX; }, { passive: true });
    lightbox.addEventListener('touchend', function (e) {
      if (lbTouchStartX === null) return;
      var delta = e.changedTouches[0].clientX - lbTouchStartX;
      if (Math.abs(delta) > 40 && galleryItems.length > 1) showLightboxItem(lightboxIndex + (delta < 0 ? 1 : -1));
      lbTouchStartX = null;
    });
  }
  document.addEventListener('keydown', function (e) {
    if (!lightbox || !lightbox.classList.contains('open')) return;
    if (e.key === 'Escape') closeLightbox();
    if (galleryItems.length < 2) return;
    if (e.key === 'ArrowLeft') showLightboxItem(lightboxIndex - 1);
    if (e.key === 'ArrowRight') showLightboxItem(lightboxIndex + 1);
  });

  // Galerie-Slider: Pfeile gleiten um ein Panel weiter (eigene Ease-Animation statt nativem Smooth-Scroll)
  document.querySelectorAll('[data-gal-scroll]').forEach(function (track) {
    var frame = track.parentNode;
    var prev = frame.querySelector('[data-gal-scroll-prev]');
    var next = frame.querySelector('[data-gal-scroll-next]');
    var panels = track.children;
    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var DURATION = 750;
    var anim = null;
    var targetIndex = 0;

    function maxScroll() { return track.scrollWidth - track.clientWidth; }
    function panelLeft(i) { return Math.min(panels[i].offsetLeft - panels[0].offsetLeft, maxScroll()); }
    function lastIndex() {
      for (var i = 0; i < panels.length; i++) if (panelLeft(i) >= maxScroll() - 1) return i;
      return panels.length - 1;
    }
    function nearestIndex() {
      var best = 0;
      for (var i = 1; i < panels.length; i++) {
        if (Math.abs(panelLeft(i) - track.scrollLeft) < Math.abs(panelLeft(best) - track.scrollLeft)) best = i;
      }
      return best;
    }
    function easeInOutCubic(t) { return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; }

    function stopAnim() {
      if (!anim) return;
      cancelAnimationFrame(anim);
      anim = null;
      track.classList.remove('is-animating');
    }

    function goTo(i) {
      targetIndex = Math.max(0, Math.min(i, lastIndex()));
      var to = panelLeft(targetIndex);
      stopAnim();
      if (reduceMotion) { track.scrollLeft = to; return; }
      var from = track.scrollLeft;
      var start = null;
      track.classList.add('is-animating');
      (function frameStep(now) {
        if (start === null) start = now;
        var t = Math.min((now - start) / DURATION, 1);
        track.scrollLeft = from + (to - from) * easeInOutCubic(t);
        if (t < 1) { anim = requestAnimationFrame(frameStep); }
        else { anim = null; track.classList.remove('is-animating'); updateArrows(); }
      })(performance.now());
    }

    function updateArrows() {
      var idx = anim ? targetIndex : nearestIndex();
      if (prev) prev.disabled = idx <= 0;
      if (next) next.disabled = idx >= lastIndex();
    }

    // Mehrfachklicks addieren sich: Basis ist das laufende Ziel, nicht die aktuelle Position
    if (prev) prev.addEventListener('click', function () { goTo((anim ? targetIndex : nearestIndex()) - 1); updateArrows(); });
    if (next) next.addEventListener('click', function () { goTo((anim ? targetIndex : nearestIndex()) + 1); updateArrows(); });
    // Eigenes Wischen/Scrollen bricht die Animation ab und überlässt das Einrasten dem Browser
    ['touchstart', 'wheel', 'pointerdown'].forEach(function (ev) {
      track.addEventListener(ev, stopAnim, { passive: true });
    });
    track.addEventListener('scroll', function () { if (!anim) updateArrows(); }, { passive: true });
    window.addEventListener('resize', updateArrows);
    updateArrows();
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
