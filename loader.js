/* =====================================================================
   H&M BRANDED LOADER — animation controller
   ---------------------------------------------------------------------
   Drives the loading screen with the Web Animations API so motion stays
   smooth and is independent of any global prefers-reduced-motion CSS.
   Markup lives inline in index.html (see the <div id="hm-loader"> block);
   this file only sequences it.
   ===================================================================== */
(function () {
  "use strict";

  /* ===================================================================
     ASSET PATHS + TUNING  —  EDIT HERE
     Change the folder once, or swap any single file. Frame order is the
     mower pull-start animation (1 -> 2 -> 3) then the thumbs-up payoff.
     =================================================================== */
  var BASE = "assets/loader/";
  var CONFIG = {
    frames: [
      BASE + "03_mower_pull_frame_1.png", // 0  stance / first pull
      BASE + "04_mower_pull_frame_2.png", // 1  mid pull
      BASE + "05_mower_pull_frame_3.png", // 2  hard pull
      BASE + "06_mower_thumbs_up.png"     // 3  started! thumbs up
    ],
    audio: BASE + "15_mower_start_rev_sound.wav", // optional, gesture-gated only
    // every image the loader paints — preloaded up front to avoid pop-in
    preload: [
      BASE + "01_hm_logo_pill.png",
      BASE + "02_grass_strip.png",
      BASE + "17_dirt_strip.png",
      BASE + "07_spark_pop.png",
      BASE + "08_smoke_puff_1.png",
      BASE + "09_smoke_puff_2.png",
      BASE + "10_smoke_puff_3.png",
      BASE + "11_tree_pine_grove_line_art.png",
      BASE + "12_tree_bonsai_line_art.png",
      BASE + "13_tree_watercolor.png",
      BASE + "14_leafy_branch_line_art.png",
      BASE + "16_subtle_paper_texture.png"
    ],
    sessionKey: "hm_loader_shown",
    playAudio: true            // still only plays after a real user gesture
  };

  var EASE_OUT = "cubic-bezier(0.16, 1, 0.3, 1)";
  var EASE_IO  = "cubic-bezier(0.65, 0, 0.35, 1)";

  var loader = document.getElementById("hm-loader");
  if (!loader) return;

  // query params: ?loader=full forces the full show (testing); ?loader=off skips
  var qs = new URLSearchParams(location.search);
  var forceFull = qs.get("loader") === "full";
  var forceOff  = qs.get("loader") === "off";
  var freeze    = qs.get("loader") === "freeze"; // debug: run show, hold final state

  var els = {
    stage:  loader.querySelector(".hm-stage"),
    logo:   loader.querySelector(".hm-logo"),
    grass:  loader.querySelector(".hm-grass"),
    dirt:   loader.querySelector(".hm-dirt"),
    group:  loader.querySelector(".hm-mower-group"),
    mower:  loader.querySelector(".hm-mower-img"),
    spark:  loader.querySelector(".hm-spark"),
    smokes: Array.prototype.slice.call(loader.querySelectorAll(".hm-smoke")),
    bar:    loader.querySelector(".hm-bar"),
    fill:   loader.querySelector(".hm-progress-fill"),
    pct:    loader.querySelector(".hm-pct")
  };

  var GBASE = "translate(-50%, -50%)";   // mower-group transform origin pin
  var timers = [];
  var finished = false;
  var progressTimer = null;

  function at(ms, fn) { timers.push(setTimeout(fn, ms)); }
  function setFrame(i) { if (els.mower) els.mower.src = CONFIG.frames[i]; }

  /* drive the heat-up bar: width + % climb, --heat warms green -> fire.
     pct uses ease-out so it sprints early then settles into 100. */
  function renderProgress(p) {            // p in [0,1]
    var pct = Math.round(p * 100);
    if (els.fill) els.fill.style.width = (p * 100) + "%";
    if (els.pct)  els.pct.textContent = pct + "%";
    // heat lags the fill a touch, then surges past ~60% so the "fire" reads late
    var heat = Math.min(1, Math.pow(p, 1.7));
    if (els.bar) els.bar.style.setProperty("--heat", heat.toFixed(3));
  }
  function runProgress(duration) {
    // setInterval (not rAF) so it ticks reliably even when the tab is throttled
    var start = Date.now();
    renderProgress(0);
    progressTimer = setInterval(function () {
      if (finished) { clearInterval(progressTimer); return; }
      var t = Math.min(1, (Date.now() - start) / duration);
      var eased = 1 - Math.pow(1 - t, 2.2);   // ease-out
      renderProgress(eased);
      if (t >= 1) { clearInterval(progressTimer); progressTimer = null; }
    }, 30);
  }

  function preload() {
    CONFIG.preload.concat(CONFIG.frames).forEach(function (src) {
      var im = new Image(); im.src = src;
    });
  }

  function cleanup() {
    if (finished) return;
    finished = true;
    if (progressTimer) clearInterval(progressTimer);
    timers.forEach(clearTimeout);
    loader.setAttribute("hidden", "");
    loader.style.pointerEvents = "none";
    try { sessionStorage.setItem(CONFIG.sessionKey, "1"); } catch (e) {}
    if (loader.parentNode) loader.parentNode.removeChild(loader);
  }

  function fadeOut(duration, lift) {
    var a = loader.animate(
      [{ opacity: 1 }, { opacity: 0 }],
      { duration: duration, easing: EASE_IO, fill: "forwards" }
    );
    if (lift && els.stage) {
      els.stage.animate(
        [{ transform: "translateY(0)" }, { transform: "translateY(-8px)" }],
        { duration: duration, easing: EASE_IO, fill: "forwards" }
      );
    }
    a.onfinish = cleanup;
    // safety net if onfinish never fires
    at(duration + 120, cleanup);
  }

  /* ---------- optional audio: only after a genuine user gesture ---------- */
  function wireAudio() {
    if (!CONFIG.playAudio) return;
    var played = false;
    var audio = new Audio(CONFIG.audio);
    audio.volume = 0.5;
    function go() {
      if (played || finished) return;
      played = true;
      audio.play().catch(function () {});
      window.removeEventListener("pointerdown", go);
      window.removeEventListener("keydown", go);
    }
    window.addEventListener("pointerdown", go, { once: true });
    window.addEventListener("keydown", go, { once: true });
  }

  /* ===================== reduced-motion / fast paths ==================== */
  function quickReveal(duration) {
    // logo only, then a clean fade — no characters, no motion
    if (els.logo) els.logo.style.opacity = "1";
    renderProgress(1);                  // show a filled, fully-hot bar at 100%
    at(duration, function () { fadeOut(280, false); });
  }

  /* ============================ full show ============================== */
  function fullShow() {
    preload();
    wireAudio();
    setFrame(0);
    runProgress(2350);                  // bar fills + heats over the full timeline, hits 100% as the site reveals

    // -- Step 1: stage reveal (0 - 0.25s) --
    els.logo.animate(
      [{ opacity: 0, transform: GBASE + " scale(0.96)" },
       { opacity: 1, transform: GBASE + " scale(1)" }],
      { duration: 440, easing: EASE_OUT, fill: "forwards" }
    );
    if (els.dirt) els.dirt.animate(
      [{ opacity: 0, transform: "translateX(-50%) translateY(10px)" },
       { opacity: 1, transform: "translateX(-50%) translateY(0)" }],
      { duration: 460, easing: EASE_OUT, fill: "forwards" }
    );
    els.grass.animate(
      [{ opacity: 0, transform: "translateX(-50%) translateY(18px)" },
       { opacity: 1, transform: "translateX(-50%) translateY(0)" }],
      { duration: 500, easing: EASE_OUT, fill: "forwards" }
    );

    // -- Step 2: character enters from the left (0.25 - 0.65s) --
    at(250, function () {
      els.group.animate(
        [{ opacity: 0, transform: GBASE + " translate(-22px,0)" },
         { opacity: 1, transform: GBASE + " translate(0,0)" }],
        { duration: 380, easing: EASE_OUT, fill: "forwards" }
      );
    });

    // -- Step 3: pull-start motion 03 -> 04 -> 05 + spark (0.65 - 1.20s) --
    at(650, function () {
      setFrame(1);
      // lean back into the pull
      els.group.animate(
        [{ transform: GBASE + " translate(0,0) rotate(0deg)" },
         { transform: GBASE + " translate(-3px,1px) rotate(-1.4deg)" }],
        { duration: 150, easing: "ease-out", fill: "forwards" }
      );
    });
    at(840, function () {
      setFrame(2);
      // hard pull jerk
      els.group.animate(
        [{ transform: GBASE + " translate(-3px,1px) rotate(-1.4deg)" },
         { transform: GBASE + " translate(5px,-2px) rotate(1.6deg)" },
         { transform: GBASE + " translate(0,0) rotate(0deg)" }],
        { duration: 240, easing: EASE_OUT, fill: "forwards" }
      );
    });
    at(900, function () {
      // spark pop near the engine, brief
      els.spark.animate(
        [{ opacity: 0, transform: "translate(-50%,-50%) scale(0.4)" },
         { opacity: 1, transform: "translate(-50%,-50%) scale(1.15)", offset: 0.45 },
         { opacity: 0, transform: "translate(-50%,-50%) scale(0.95)" }],
        { duration: 170, easing: "ease-out" }
      );
    });

    // -- Step 4: startup vibration + smoke (1.20 - 1.90s) --
    at(1200, function () {
      setFrame(0);                       // upright, engine running
      // engine vibration
      els.group.animate(
        [{ transform: GBASE + " translate(0,0) rotate(0deg)" },
         { transform: GBASE + " translate(1.4px,-1px) rotate(0.5deg)" },
         { transform: GBASE + " translate(-1.4px,1px) rotate(-0.5deg)" },
         { transform: GBASE + " translate(0,0) rotate(0deg)" }],
        { duration: 110, iterations: 6, easing: "linear" }
      );
    });
    var puffDelays = [1200, 1380, 1560];
    var puffSpec = [
      { x: 10, y: -42, s: 1.10, dur: 1400 },
      { x: 18, y: -52, s: 1.18, dur: 1550 },
      { x: 24, y: -34, s: 1.05, dur: 1300 }
    ];
    els.smokes.forEach(function (puff, i) {
      var sp = puffSpec[i] || puffSpec[0];
      at(puffDelays[i] || 1200, function () {
        puff.animate(
          [{ opacity: 0,    transform: "translate(-50%,-50%) translate(0,0) scale(0.5)" },
           { opacity: 0.85, transform: "translate(-50%,-50%) translate(" + (sp.x*0.4) + "px," + (sp.y*0.35) + "px) scale(0.85)", offset: 0.35 },
           { opacity: 0,    transform: "translate(-50%,-50%) translate(" + sp.x + "px," + sp.y + "px) scale(" + sp.s + ")" }],
          { duration: sp.dur, easing: EASE_OUT }
        );
      });
    });

    // -- Step 5: thumbs up payoff (1.90 - 2.35s) --
    at(1900, function () {
      setFrame(3);
      els.group.animate(
        [{ transform: GBASE + " scale(1)" },
         { transform: GBASE + " scale(1.06)", offset: 0.5 },
         { transform: GBASE + " scale(1)" }],
        { duration: 260, easing: EASE_OUT, fill: "forwards" }
      );
    });

    // -- Step 6: reveal the site (2.35 - 3.00s) --
    if (!freeze) at(2350, function () { fadeOut(620, true); });
  }

  /* ============================ bootstrap ============================= */
  function boot() {
    if (forceOff) { cleanup(); return; }

    var reduced = window.matchMedia &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    if (forceFull || freeze) { fullShow(); return; }

    // Reduced motion -> simple logo reveal, no animation (accessibility)
    if (reduced) { quickReveal(650); return; }

    // Otherwise play the full show on every reload
    fullShow();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot, { once: true });
  } else {
    boot();
  }
})();
