# Claude / Codex implementation prompt — HM How It Works section

Build the HM Junk Removal & Landscaping “How It Works” section from the supplied PNG assets. Use the PNGs as visual layers only. All readable website text must be real HTML text, not baked into images, so it stays sharp, editable, and correct.

## Asset folder
Place these files in:
`/public/assets/hm-how-it-works/`

Files included:
- `00_full_section_reference.png` — final visual reference only. Do not display on the live page.
- `01_bg_dark_green_gradient.png` — base section background.
- `02_headline_glass_backplate.png` — subtle foundation behind headline/subheadline.
- `03_step_card_backplate.png` — reusable glass card behind each step row.
- `04_trust_pill_base.png` — reusable pill background.
- `05_cta_orange_button_base.png` — CTA button background.
- `06_icon_circle_base.png` — empty glowing icon circle.
- `07_icon_photo_upload.png` — step 1 icon.
- `08_icon_quote_doc.png` — step 2 icon.
- `09_icon_calendar.png` — step 3 icon.
- `10_icon_truck.png` — step 4 icon.
- `11_phone_float_2_5d.png` — floating 2.5D phone mockup.
- `12_phone_shadow_glow.png` — phone shadow/glow layer.
- `13_left_leaf_grass_cluster.png` — foreground foliage cutout.
- `14_upper_right_leaf_glow.png` — upper-right foliage/light texture.
- `15_right_paver_path_texture.png` — subtle right-side path texture.
- `16_warm_sunlight_corner_glow.png` — warm orange/cream glow overlay.
- `17_left_foliage_soft_overlay.png` — lower-opacity foliage overlay.

## Section layout
Create a full-width section with id/class:
`hm-how-it-works`

Desktop reference canvas: 1827 × 861.
Use responsive scaling, but these are the desktop design positions:

- Section height: `min-height: 860px` on desktop.
- Max content width: `1280px` to `1360px`.
- Background base: absolutely fill the section with `01_bg_dark_green_gradient.png`, `object-fit: cover`.

Layer placement:
1. `01_bg_dark_green_gradient.png`
   - position: absolute inset 0
   - width/height: 100%
   - z-index: 0

2. `15_right_paver_path_texture.png`
   - position: absolute
   - right: 0
   - bottom: 95px
   - width: 42vw, max-width: 720px
   - opacity: 0.42
   - z-index: 1

3. `16_warm_sunlight_corner_glow.png`
   - position: absolute
   - right: 0
   - top: 0
   - width: 34vw, max-width: 520px
   - opacity: 0.55
   - mix-blend-mode: screen
   - z-index: 1

4. `14_upper_right_leaf_glow.png`
   - position: absolute
   - right: 0
   - top: 0
   - width: 25vw, max-width: 380px
   - opacity: 0.36
   - z-index: 2

5. `13_left_leaf_grass_cluster.png`
   - position: absolute
   - left: 0
   - bottom: 0
   - width: 27vw, max-width: 390px
   - opacity: 0.95
   - z-index: 3

6. `17_left_foliage_soft_overlay.png`
   - position: absolute
   - left: 0
   - bottom: 0
   - width: 32vw, max-width: 470px
   - opacity: 0.35
   - z-index: 2

7. `02_headline_glass_backplate.png`
   - position: absolute
   - top: 28px
   - left: 50%
   - transform: translateX(-50%)
   - width: min(1280px, 78vw)
   - height: auto
   - opacity: 0.92
   - z-index: 4

## Top text
Place actual HTML text above the headline backplate, z-index 5.

Small label:
- Text: `02  HOW IT WORKS`
- top: around 26px
- centered
- Use a pill: orange left cap with `02`, dark green/right cap for `HOW IT WORKS`.

Headline exact text:
`Text Photos. Get a Clear Quote. Cleared.`

Style:
- Centered
- Font: use the site’s main sans-serif. Prefer `Inter`, `Satoshi`, `Manrope`, or existing site font.
- Size desktop: clamp(46px, 5vw, 68px)
- Weight: 800
- Color: #F4F0E6
- The word `Cleared.` should be orange `#ff7a1a`, italic, weight 800.

Subheadline exact text:
`No in-person estimate. No hourly surprises. Send a few photos and see the by-the-job price before we lift a thing.`

Style:
- Centered
- max-width: 1120px
- color: rgba(244,240,230,.88)
- font-size: 18px–22px desktop
- line-height: 1.45

## Main two-column layout
Wrapper:
- display: grid
- columns: `0.92fr 1.08fr`
- gap: 70px
- align-items: start
- margin-top: 185px desktop
- z-index: 5

### Left phone area
Create a relative phone stage.

`12_phone_shadow_glow.png`
- position absolute
- left: 8%
- top: 560px in reference terms / align under phone bottom
- width: 440px
- opacity: 0.85
- z-index: 4

`11_phone_float_2_5d.png`
- position relative
- width: clamp(330px, 29vw, 445px)
- margin-left: 5%
- margin-top: 0
- z-index: 6
- filter: drop-shadow(0 34px 45px rgba(0,0,0,.45))
- transform: translateY(-4px) rotate(-1deg)
- Add hover only on desktop: translateY(-10px) rotate(-0.5deg).

Do not recreate the phone in CSS unless needed. Use the PNG.

### Right process area
Create 4 real HTML step rows. Behind each row, place `03_step_card_backplate.png` as an absolute img, or use it as CSS background image.

Process column desktop position:
- max-width: 760px
- margin-top: 18px

Each step card:
- position: relative
- min-height: 112px
- display: grid
- grid-template-columns: 88px 94px 1fr
- align-items: center
- padding: 0 34px
- margin-bottom: 10px
- background-image: url(`/assets/hm-how-it-works/03_step_card_backplate.png`)
- background-size: 100% 100%

Step number style:
- color: #ff7a1a
- font-size: 44px
- line-height: 1
- font-weight: 800
- letter-spacing: -0.04em

Icon images:
- Step 1 use `07_icon_photo_upload.png`
- Step 2 use `08_icon_quote_doc.png`
- Step 3 use `09_icon_calendar.png`
- Step 4 use `10_icon_truck.png`
- width: 76px
- height: 76px

Step heading style:
- color: #F4F0E6
- font-size: 21px–23px
- font-weight: 800
- margin-bottom: 6px

Step body style:
- color: rgba(244,240,230,.82)
- font-size: 16px
- line-height: 1.42

Exact step text:
1. Heading: `Send a few photos`
   Body: `Text the pile, the yard, the driveway, or whatever needs to go. More angles mean a tighter quote.`

2. Heading: `Get a clear quote back`
   Body: `One number, by the job. Written, not a phone guess. Disposal and clean-up baked in.`

3. Heading: `Pick a time`
   Body: `Same-day and next-day spots are often available. We work around your schedule.`

4. Heading: `We haul, clean, leave it better`
   Body: `Loaded, hauled, swept up. You should only notice what’s gone.`

## Trust chips
Place below step cards, centered under the process column.
Use actual HTML text with the `04_trust_pill_base.png` as background image.

Container:
- display: flex
- gap: 16px
- margin-top: 14px
- flex-wrap: wrap

Each chip:
- min-width: 210px
- height: 52px
- background-image: url(`/assets/hm-how-it-works/04_trust_pill_base.png`)
- background-size: 100% 100%
- display flex center
- icon can be inline lucide/svg or simple text icon.

Exact chip text:
- `No hourly surprises`
- `Fast photo quotes`
- `Clear price up front`

## CTA
Place CTA under the chips.
Use `05_cta_orange_button_base.png` as the background image, but keep label as actual text.

Button text exact:
`Text Photos for a Free Quote →`

Style:
- width: 430px
- height: 62px
- margin-top: 18px
- background-image: url(`/assets/hm-how-it-works/05_cta_orange_button_base.png`)
- color: white
- font-size: 20px
- font-weight: 800
- border: 0
- border-radius: 999px
- box-shadow: 0 20px 42px rgba(255,122,26,.22)

Helper text exact:
`Most quotes only need 3–5 photos.`

Style:
- margin-top: 10px
- color: rgba(244,240,230,.76)
- font-size: 15px
- text-align: center

## Mobile behavior
At max-width 900px:
- Section min-height auto; padding: 72px 18px.
- Headline backplate should still sit behind the headline but width 94vw.
- Grid becomes one column.
- Phone appears below headline and above steps.
- Phone width: min(88vw, 380px), centered.
- Step cards use 2-column layout: number/icon on top or left, text to right.
- CTA full width max 430px.
- Hide or reduce `15_right_paver_path_texture.png` opacity to 0.18.
- Foliage assets should not cover text; keep z-index below content.

## Important
- All visible words must be typed in HTML/CSS, not only embedded inside PNGs.
- Use the full reference image only to match spacing and mood.
- Keep the section premium, warm, local, and trustworthy — not corporate SaaS.
- Keep colors consistent: deep forest green, warm cream, restrained orange.
- Avoid clutter. The cards should give the text a foundation and make everything easier to read.
