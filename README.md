# H&M Junk Removal & Landscaping — Website (v2)

A polished, mobile-first single-page website for **H&M Junk Removal & Landscaping**, a Northern Virginia local service business.

This is an **improvement pass** over the original site — not a rebuild. Original site structure and the GSAP/ScrollTrigger animation system are preserved.

## What changed in v2

### Real assets
- **Real H&M Tacoma photo** in the hero and the Recent Work feature card (`assets/hm-truck.jpg`) — used twice, not over-repeated. The About section uses the round badge logo instead.
- **Real H&M brand logo** in the header and footer (`assets/logo-primary.png`)
- **Real brand favicon** (`assets/favicon.png`)
- **Real brand service icons** used in the services grid (Junk Removal, Landscaping & Mulch, Yard Cleanup, Power Washing)

### Brand palette + typography (per `hm_brand_assets_package`)
- Forest Green `#1F4D33`, Charcoal `#1F1F1F`, Warm Cream `#F5F1E6`, Sage `#A7B89A`, Construction Orange `#F47A20`
- **Manrope** for headlines, **Inter** for body, **Bebas Neue** for numbers/badges

### Sections replaced/added
- **Hero** — real truck photo replaces the SVG illustration. New headline: *"Junk Removal & Yard Cleanup Made Easy."* Trust row underneath: Local NoVA crew · Upfront pricing · Student-run.
- **Services** — redesigned as a 6-card grid (Junk Removal, Landscaping & Mulch, Yard Cleanup, Power Washing, Cleanouts, Small Hauling). Each card uses the brand icon and a "Text a __ quote" CTA.
- **NEW: "Text it. Quote it. Cleared." section** — the unique conversion section the prompt called for. It's a phone-mockup chat showing how the photo-quote flow actually works (customer texts photos → H&M replies with a real number → booked). On the right, a 4-step process and the badges "No hourly surprises / Fast photo quotes / Clear price up front." Underneath, a clean explanation that we quote by the job, not the hour.
- **Why H&M** — refreshed with 6 cards instead of 4 (added "One crew, one truck", "Cleanup included", "Flexible scheduling").
- **Service Areas** — expanded pill list to include Herndon, Reston, Vienna, Oakton, Oak Hill, Fairfax, Chantilly, Great Falls, McLean, Sterling, Centreville, Ashburn, Burke, Fairfax County, Loudoun County.
- **About** — kept the real Miles narrative; the old placeholder illustration is now a clean forest-green panel with the round badge logo and the "Hauling. Cleanups. Curb Appeal." tagline (keeps the truck photo from being over-repeated).
- **Recent Work** — replaced the old fake before/after gallery with a finished "Recent Work" block: the real truck photo as the feature card, a "What we haul" info panel, and a full-width "Have a pile like this?" CTA panel. **No "Photo coming soon" boxes** — the section reads as complete, not under construction. When you get real job photos, drop them in as new `work-card` figures (see "Add real job photos" below).
- **Reviews** — strengthened into an honest two-panel layout: a "Recently used H&M?" invitation card (stars are clearly labeled *"Review invitation, not a rating yet"* so nothing reads as a fake rating) next to a forest-green **trust-signals** panel (local owner-operated, real NoVA phone and truck, job-based quotes, cleanup included). Headline: *"Building reviews one neighbor at a time."*
- **FAQ** — tightened wording.
- **Final CTA** — "Need junk gone or a yard cleaned up?" with the primary "Text Photos for a Free Quote" and "Call 202-999-7885".
- **Footer** — real logo on a cream chip, plus the brand tagline "YOUNG CREW · STRONG WORK ETHIC · TOP-NOTCH RESULTS" from the brand guide footer strip.

### v4 brand-board pass (latest)
- **Service icons** rebuilt as circular warm-cream badges with a soft green ring (brand-board style), holding clean icon-only art. The brand-pack icon tiles had text labels baked in, so cropped label-free versions were created (`icon-junk-c.png`, `icon-landscaping-c.png`, `icon-yard-c.png`, `icon-power-c.png`).
- **Recent Work renamed to "Jobs we handle around NoVA."** This is the honest fix. Only the real H&M truck photo is tagged **"Our truck"** (orange pill). The four reference photos are tagged **"Project example"** (dark pill) and the section lede says plainly: *"The truck is ours. The rest show the kinds of projects we take on."* Nothing claims H&M did those exact jobs. Watermarked photos, other companies' trucks/people, and baked-in BEFORE/AFTER images were all excluded.
- **Footer brand messaging strip** added above the footer (orange band): *BASED IN NORTHERN VIRGINIA · SERVING HOMES, RENTALS, HOAS & BUSINESSES · YOUNG CREW. STRONG WORK ETHIC. CLEAN RESULTS.* Footer tagline updated to "Clean Results."
- **Responsive gallery**: `.work-grid-v3` now collapses 3 → 2 → 1 columns so the project cards never crowd on tablet/mobile.
- New optimized photos: `svc-mulch.jpg` (142 KB), `svc-power.jpg` (97 KB), `svc-yard.jpg` (113 KB), `svc-cleanout.jpg` (44 KB).

### v3 refinement pass
- **Removed every "Photo coming soon" card** in Recent Work and rebuilt it as a finished, honest section (feature photo + info panel + CTA panel).
- **Rebuilt Reviews** with an invitation card + trust-signals panel; stars are explicitly labeled as an invitation, not a rating.
- **Removed all em/en dashes from customer-facing copy** (replaced with commas, colons, or periods) per brand voice. Meta titles now use `·` separators.
- **Phone mockup copy** reworked to be more believable and to spell out that price depends on load size, weight, stairs, and dump fees (no fixed price shown).
- **Scroll animations**: service cards, Recent Work cards, and trust signals now stagger in; the phone mockup gently slides and scales into place. All respect `prefers-reduced-motion` (motion disabled, final states shown, marquee frozen).
- **Service cards** now use flex so each card's "Text a __ quote" CTA pins to the bottom for an even grid rhythm.

### Removed (not real, not needed)
- Fake stats strip (`24 hr · 100% · 40 min · 20+` counters)
- "Replace with a real photo" placeholder block in About
- Three placeholder review quotes
- "Photo coming soon" placeholder cards (replaced with finished honest panels)
- Old before/after placeholders (`Before` / `After` half-card gradients)
- The standalone Pricing section (kept the same explanation but consolidated into the new flow section's note — keeps the page tighter, prompt asked for "do not make the site too wordy")
- "Same-day pickups available" claim from the hero eyebrow (replaced with a more honest "Northern Virginia · Local · Student-Run")

### Kept
- The existing GSAP + ScrollTrigger smooth-reveal system (`script.js`)
- Scroll-progress bar, curtain intro, mobile drawer
- Sticky bottom call/text bar on mobile
- LocalBusiness JSON-LD schema (now with Loudoun County + extra towns)
- Smooth anchor scrolling, scroll-velocity marquee, parallax on the truck photo

## Files

```
hmjunkland-site-v2/
├── index.html          # Improved single page
├── styles.css          # Original styles + v2 palette/section overrides
├── script.js           # GSAP scroll animations (unchanged)
├── README.md           # This file
└── assets/                # all images optimized — folder total ~780 KB
    ├── favicon.png         # H&M icon (brand pack), 128px
    ├── logo-primary.png    # H&M primary horizontal logo — header + footer
    ├── logo-badge.png      # Round badge logo — used in the About panel
    ├── hm-truck.jpg        # Real H&M Tacoma photo (hero + Recent Work feature), 305 KB
    ├── icon-junk.png       # Original labeled icon tile (kept, unused)
    ├── icon-landscaping.png# Original labeled icon tile (kept, unused)
    ├── icon-yard.png       # Original labeled icon tile (kept, unused)
    ├── icon-power.png      # Original labeled icon tile (kept, unused)
    ├── icon-junk-c.png     # Clean (label-free) icon — Junk Removal, in service card
    ├── icon-landscaping-c.png # Clean icon — Landscaping & Mulch, in service card
    ├── icon-yard-c.png     # Clean icon — Yard Cleanup, in service card
    ├── icon-power-c.png    # Clean icon — Power Washing, in service card
    ├── svc-mulch.jpg       # "Jobs We Handle" project example — mulch/beds
    ├── svc-power.jpg       # "Jobs We Handle" project example — surface washing
    ├── svc-yard.jpg        # "Jobs We Handle" project example — yard cleanup
    └── svc-cleanout.jpg    # "Jobs We Handle" project example — garage/shed cleanout
```

> Images were optimized for Netlify: the truck photo was converted from a 2.5 MB PNG to a 305 KB JPEG, and the logo/favicon/badge were downscaled. Total `assets/` weight is ~780 KB.

`_source_assets/` holds the unzipped brand and improvement packs for reference. It is **not** served at runtime — safe to delete before deploying.

## How to preview locally

```bash
cd hmjunkland-site-v2
python -m http.server 8000
# then visit http://localhost:8000
```

Or just double-click `index.html`.

## How to deploy to Netlify

### Drag & drop (easiest)
1. Go to https://app.netlify.com/drop
2. Drag the whole `hmjunkland-site-v2/` folder onto the page (you can leave out `_source_assets/` to save space)
3. Netlify gives you a live URL
4. **Domain settings → Add custom domain → hmjunkland.org** and point DNS as Netlify instructs

### Git-based deploy
1. Push the folder contents to a GitHub repo
2. Connect the repo to Netlify
3. Build command: *(none)*, Publish directory: `/`

## How to edit common things

### Phone number
Search and replace these strings if your number ever changes:
- `2029997885` (in `tel:` / `sms:` links)
- `202-999-7885` (display text)
- `+1-202-999-7885` (in LocalBusiness schema)

### Domain
Search `hmjunkland.org`.

### Add real job photos to the Recent Work gallery
1. Drop your photo into `assets/` (e.g. `assets/oakhill-garage.jpg`)
2. In `index.html`, find the `work-grid-v3` block under `#gallery`
3. Add a new figure next to the feature card:
   ```html
   <figure class="work-card">
     <img src="assets/oakhill-garage.jpg" alt="Garage cleanout in Oak Hill" />
     <figcaption><strong>Garage cleanout</strong><span>Oak Hill</span></figcaption>
   </figure>
   ```
4. As you add more real photos, you can drop the "What we haul" / CTA panels and let the grid fill with real jobs. The `.work-card` styles (rounded, clipped image, hover lift) are already in the stylesheet, so images stay contained with no overflow.

### Add real reviews
In `#reviews`, replace the `.reviews-invite` card with real `<blockquote>` quotes (real names only). Keep the `.trust-signals` panel next to it. The `.reviews-grid` / `.review` CSS from the original site is still in the stylesheet if you want that layout.

### Update service areas
In `index.html` find `<ul class="areas-pill-grid">` and edit the `<li>` items. Also update the `areaServed` array in the LocalBusiness JSON-LD at the top of the file.

### Add a real photo of Miles to About
The About section currently shows a branded badge panel (`about-badge-panel` in `index.html`). To use a real photo instead, replace that whole `<div class="about-badge-panel">…</div>` with:
```html
<div class="about-photo about-photo-v2" data-parallax="0.08" data-reveal>
  <img src="assets/miles-on-job.jpg" alt="Miles on a job site" />
  <div class="about-tag">Owner · Operator · Northern Virginia</div>
</div>
```
The `about-photo-v2` styles are already in the stylesheet.

## Comparing v1 vs v2

The original site is still untouched at `../hmjunkland-site/`. You can open both side-by-side in your browser to compare.

## What's intentionally NOT included
- No "licensed/insured" claims
- No fake reviews from named real people
- No fake before/after photos
- No fake stats / 0+ / 24hr / 100% counters
- No business email address (everything routes to text or call)
