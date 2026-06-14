/* =========================================================
   H&M Junk Removal & Landscaping — script v2
   GSAP + ScrollTrigger powered scroll animations
   ========================================================= */

(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // -----------------------------
  // Footer year
  // -----------------------------
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // -----------------------------
  // Mobile menu
  // -----------------------------
  var toggle = document.getElementById('menuToggle');
  var drawer = document.getElementById('mobileDrawer');
  if (toggle && drawer) {
    toggle.addEventListener('click', function () {
      var open = !drawer.hasAttribute('hidden');
      if (open) {
        drawer.setAttribute('hidden', '');
        toggle.setAttribute('aria-expanded', 'false');
      } else {
        drawer.removeAttribute('hidden');
        toggle.setAttribute('aria-expanded', 'true');
      }
    });
    drawer.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        drawer.setAttribute('hidden', '');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // -----------------------------
  // Scroll progress + header shrink
  // -----------------------------
  var progressEl = document.getElementById('scrollProgress');
  var header = document.querySelector('.site-header');

  function onScrollLite() {
    var max = document.documentElement.scrollHeight - window.innerHeight;
    var pct = max > 0 ? (window.scrollY / max) * 100 : 0;
    if (progressEl) progressEl.style.width = pct + '%';
    if (header) header.classList.toggle('is-scrolled', window.scrollY > 8);
  }
  window.addEventListener('scroll', onScrollLite, { passive: true });
  onScrollLite();

  // -----------------------------
  // Curtain page-load reveal
  // -----------------------------
  var curtain = document.getElementById('curtain');

  function fallbackReveal() {
    // CSS fallback if GSAP doesn't load
    if (curtain) curtain.style.display = 'none';
    document.querySelectorAll('[data-reveal]').forEach(function (el) {
      el.classList.add('is-in');
    });
  }

  // Wait for GSAP to load (it's deferred). Use a short polling window then start.
  var gsapTries = 0;
  function whenGSAP(cb) {
    if (window.gsap && window.ScrollTrigger) { cb(); return; }
    if (gsapTries++ > 60) { fallbackReveal(); return; }
    setTimeout(function () { whenGSAP(cb); }, 50);
  }

  if (reduced) {
    fallbackReveal();
  } else {
    whenGSAP(initAnimations);
  }

  // -----------------------------
  // Split words in hero title for staggered reveal
  // -----------------------------
  function splitHeroWords() {
    var title = document.querySelector('.hero-title[data-split]');
    if (!title) return [];
    var words = title.querySelectorAll('.word');
    words.forEach(function (w) {
      // Wrap each word in a span we can transform without breaking line wrapping
      if (w.dataset.split === '1') return;
      var inner = document.createElement('span');
      inner.className = 'word-inner';
      inner.style.display = 'inline-block';
      inner.style.willChange = 'transform';
      inner.textContent = w.textContent;
      w.textContent = '';
      w.appendChild(inner);
      w.style.display = 'inline-block';
      w.style.overflow = 'hidden';
      w.style.verticalAlign = 'top';
      w.dataset.split = '1';
    });
    return title.querySelectorAll('.word-inner');
  }

  // -----------------------------
  // Init GSAP animations
  // -----------------------------
  function initAnimations() {
    var gsap = window.gsap;
    var ST = window.ScrollTrigger;
    gsap.registerPlugin(ST);

    // === Curtain intro ===
    var tlIntro = gsap.timeline({
      defaults: { ease: 'expo.out' },
      onComplete: function () {
        if (curtain) curtain.classList.add('is-done');
      }
    });

    if (curtain) {
      var mark = curtain.querySelector('.curtain-mark');
      tlIntro
        .to(mark, { opacity: 1, y: 0, duration: 0.5, ease: 'power2.out' }, 0)
        .to(mark, { opacity: 0, y: -16, duration: 0.4, ease: 'power2.in' }, 0.8)
        .to(curtain, { yPercent: -100, duration: 0.9, ease: 'expo.inOut' }, 1.0);
    }

    // === Hero reveal ===
    var heroWords = splitHeroWords();
    var heroEyebrow = document.querySelector('[data-anim="eyebrow"]');
    var heroSub = document.querySelector('.hero-sub');
    var heroCTA = document.querySelector('.hero-cta');
    var heroMeta = document.querySelector('.hero-meta');
    var heroIllo = document.querySelector('.hero-illo');
    var floatCards = document.querySelectorAll('.float-card');
    var scrollCue = document.querySelector('.scroll-cue');

    var tlHero = gsap.timeline({ delay: curtain ? 1.4 : 0.1, defaults: { ease: 'expo.out', duration: 1 } });

    if (heroEyebrow) tlHero.from(heroEyebrow, { opacity: 0, y: 14, duration: 0.6 }, 0);
    if (heroWords.length) {
      tlHero.from(heroWords, { yPercent: 110, duration: 0.9, stagger: 0.06, ease: 'expo.out' }, 0.1);
    }
    if (heroSub) tlHero.from(heroSub, { opacity: 0, y: 18, duration: 0.7 }, 0.6);
    if (heroCTA) tlHero.from(heroCTA.children, { opacity: 0, y: 14, stagger: 0.08, duration: 0.6 }, 0.7);
    if (heroMeta) tlHero.from(heroMeta.children, { opacity: 0, y: 12, stagger: 0.08, duration: 0.6 }, 0.85);
    if (heroIllo) tlHero.from(heroIllo, { opacity: 0, scale: 0.92, duration: 1.1, ease: 'expo.out' }, 0.2);
    if (floatCards.length) tlHero.from(floatCards, { opacity: 0, y: 16, stagger: 0.12, duration: 0.6 }, 0.9);
    if (scrollCue) tlHero.from(scrollCue, { opacity: 0, y: -10, duration: 0.5 }, 1.4);

    // === Parallax on hero illustration ===
    document.querySelectorAll('[data-parallax]').forEach(function (el) {
      var depth = parseFloat(el.getAttribute('data-parallax')) || 0.1;
      gsap.to(el, {
        yPercent: -depth * 100,
        ease: 'none',
        scrollTrigger: {
          trigger: el,
          start: 'top bottom',
          end: 'bottom top',
          scrub: true
        }
      });
    });

    // === Generic [data-reveal] reveals ===
    var reveals = document.querySelectorAll('[data-reveal]');
    reveals.forEach(function (el) {
      gsap.fromTo(el,
        { opacity: 0, y: 36 },
        {
          opacity: 1, y: 0,
          duration: 0.9,
          ease: 'expo.out',
          scrollTrigger: {
            trigger: el,
            start: 'top 88%',
            toggleActions: 'play none none none',
            once: true
          },
          onStart: function () { el.classList.add('is-in'); }
        }
      );
    });

    // === Service rows: stagger chips & icon ===
    document.querySelectorAll('.service-row').forEach(function (row) {
      var icon = row.querySelector('.service-icon-wrap');
      var heading = row.querySelector('h3');
      var lede = row.querySelector('p');
      var chips = row.querySelectorAll('.chip-list li');
      var link = row.querySelector('.link-arrow');
      var visual = row.querySelector('.visual-shell');

      var tl = gsap.timeline({
        scrollTrigger: { trigger: row, start: 'top 78%', once: true }
      });
      if (visual) tl.from(visual, { opacity: 0, x: row.classList.contains('service-row-rev') ? 40 : -40, duration: 1, ease: 'expo.out' }, 0);
      if (icon) tl.from(icon, { opacity: 0, scale: 0.6, rotate: -20, duration: 0.6, ease: 'back.out(2)' }, 0.15);
      if (heading) tl.from(heading, { opacity: 0, y: 18, duration: 0.6, ease: 'expo.out' }, 0.25);
      if (lede) tl.from(lede, { opacity: 0, y: 16, duration: 0.6, ease: 'expo.out' }, 0.35);
      if (chips.length) tl.from(chips, { opacity: 0, y: 12, stagger: 0.03, duration: 0.4, ease: 'power3.out' }, 0.45);
      if (link) tl.from(link, { opacity: 0, x: -10, duration: 0.5, ease: 'expo.out' }, 0.7);
    });

    // === Process steps: stagger ===
    var steps = document.querySelectorAll('.process-step');
    if (steps.length) {
      gsap.from(steps, {
        opacity: 0, y: 30, stagger: 0.12, duration: 0.8, ease: 'expo.out',
        scrollTrigger: { trigger: '.process-list', start: 'top 80%', once: true }
      });
    }

    // === Why cards: batch reveal ===
    var whyCards = gsap.utils.toArray('.why-card');
    if (whyCards.length) {
      gsap.from(whyCards, {
        opacity: 0, y: 26, stagger: 0.08, duration: 0.7, ease: 'expo.out',
        scrollTrigger: { trigger: '.why-grid', start: 'top 82%', once: true }
      });
    }

    // === Service cards: stagger in ===
    var svcCards = gsap.utils.toArray('.service-cards .svc-card');
    if (svcCards.length) {
      gsap.from(svcCards, {
        opacity: 0, y: 24, stagger: 0.09, duration: 0.6, ease: 'power3.out',
        scrollTrigger: { trigger: '.service-cards', start: 'top 84%', once: true }
      });
    }

    // === Phone mockup: gentle slide + scale in ===
    var flowPhone = document.querySelector('.flow-phone');
    if (flowPhone) {
      gsap.from(flowPhone, {
        opacity: 0, y: 30, scale: 0.96, duration: 0.8, ease: 'expo.out',
        scrollTrigger: { trigger: flowPhone, start: 'top 82%', once: true }
      });
    }

    // === Recent Work cards: stagger in ===
    var workItems = gsap.utils.toArray('.work-grid-v3 > *');
    if (workItems.length) {
      gsap.from(workItems, {
        opacity: 0, y: 26, stagger: 0.1, duration: 0.65, ease: 'power3.out',
        scrollTrigger: { trigger: '.work-grid-v3', start: 'top 84%', once: true }
      });
    }

    // === Trust signals: stagger in ===
    var trustItems = gsap.utils.toArray('.trust-signals li');
    if (trustItems.length) {
      gsap.from(trustItems, {
        opacity: 0, x: -14, stagger: 0.07, duration: 0.5, ease: 'power3.out',
        scrollTrigger: { trigger: '.trust-signals', start: 'top 86%', once: true }
      });
    }

    // === Area pills: cascade in ===
    var pills = gsap.utils.toArray('.areas-pill-grid li');
    if (pills.length) {
      gsap.from(pills, {
        opacity: 0, y: 20, scale: 0.9, stagger: 0.04, duration: 0.6, ease: 'back.out(1.6)',
        scrollTrigger: { trigger: '.areas-pill-grid', start: 'top 85%', once: true }
      });
    }

    // === Stats counters ===
    var counters = document.querySelectorAll('.counter');
    counters.forEach(function (el) {
      var target = parseInt(el.getAttribute('data-target'), 10) || 0;
      var obj = { val: 0 };
      gsap.to(obj, {
        val: target,
        duration: target > 500 ? 2.0 : 1.6,
        ease: 'power2.out',
        scrollTrigger: { trigger: el, start: 'top 88%', once: true },
        onUpdate: function () {
          el.textContent = Math.floor(obj.val).toLocaleString();
        }
      });
    });

    // === Marquee speed-up on scroll ===
    var track = document.querySelector('.marquee-track');
    if (track) {
      var st = ScrollTrigger.create({
        trigger: '.marquee',
        start: 'top bottom',
        end: 'bottom top',
        onUpdate: function (self) {
          var v = self.getVelocity();
          // Slightly tilt marquee based on scroll velocity
          gsap.to(track, { skewX: gsap.utils.clamp(-8, 8, v / -200), duration: 0.4, overwrite: true });
        }
      });
      void st;
    }

    // === Hero illustration tilt on mouse ===
    var illo = document.querySelector('.hero-illo');
    if (illo && window.matchMedia('(hover: hover)').matches) {
      illo.addEventListener('mousemove', function (e) {
        var rect = illo.getBoundingClientRect();
        var x = (e.clientX - rect.left) / rect.width - 0.5;
        var y = (e.clientY - rect.top) / rect.height - 0.5;
        gsap.to(illo, { rotateY: x * 6, rotateX: -y * 6, transformPerspective: 800, duration: 0.4, ease: 'power2.out' });
      });
      illo.addEventListener('mouseleave', function () {
        gsap.to(illo, { rotateY: 0, rotateX: 0, duration: 0.6, ease: 'expo.out' });
      });
    }

    // === Subtle scale on gallery cards on scroll ===
    gsap.utils.toArray('.gallery-card').forEach(function (card) {
      gsap.fromTo(card,
        { y: 30, opacity: 0 },
        {
          y: 0, opacity: 1, duration: 0.9, ease: 'expo.out',
          scrollTrigger: { trigger: card, start: 'top 85%', once: true }
        }
      );
    });

    // === Refresh on font load to recompute positions ===
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(function () { ScrollTrigger.refresh(); });
    }
  }
})();

/* =========================================================
   Services section — lawn-mowing scene
   Man walks left -> right and the grass he passes gets mowed.
   Loops: grass grows back when he wraps to the left.
   ========================================================= */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var lawn = document.querySelector('.svc-lawn');
  var guy  = document.querySelector('.svc-mower-guy');
  if (!lawn || !guy) return;

  // scatter grass patches across the lane
  var N = 14, tufts = [];
  for (var i = 0; i < N; i++) {
    var img = document.createElement('img');
    img.src = 'assets/landscape/grass_patch.png';
    img.alt = '';
    img.className = 'svc-tuft';
    var xpct = 3 + i * (94 / (N - 1));
    img.style.left = xpct + '%';
    img.style.setProperty('--sc', (0.7 + ((i * 7) % 11) / 18).toFixed(2));
    lawn.appendChild(img);
    tufts.push({ el: img, xpct: xpct });
  }

  function laneW() { return lawn.getBoundingClientRect().width || window.innerWidth; }
  function guyW()  { return guy.getBoundingClientRect().width || 150; }

  function place(p) {
    var w = laneW(), gw = guyW();
    var x = -gw + p * (w + gw);
    guy.style.transform = 'translateX(' + x + 'px)';
    var front = x + gw * 0.88;            // the mower deck is the cutting edge
    for (var k = 0; k < tufts.length; k++) {
      if (front >= tufts[k].xpct / 100 * w) tufts[k].el.classList.add('cut');
    }
  }
  function regrow() {
    for (var k = 0; k < tufts.length; k++) tufts[k].el.classList.remove('cut');
  }

  // verification hook (this preview forces prefers-reduced-motion)
  window.__mowTick = function (p) {
    if (p < 0.02) regrow();
    place(p);
    return {
      cut: tufts.filter(function (t) { return t.el.classList.contains('cut'); }).length,
      total: tufts.length
    };
  };

  if (reduce) { place(0.42); return; }   // parked mid-lawn, grass mowed behind him

  var DUR = 13000, t0 = null, prev = 0;
  function frame(ts) {
    if (t0 === null) t0 = ts;
    var p = ((ts - t0) % DUR) / DUR;
    if (p < prev) regrow();              // wrapped to the left -> lawn grows back
    prev = p;
    place(p);
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
})();
