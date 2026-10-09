"""Generate the H&M sub-pages (service pages, service areas, quote, thanks, 404).

The homepage (index.html) is hand-edited. Every other page is generated from
the data below so the header, footer, schema and styling stay identical across
pages. Output is plain static HTML committed to the repo; Netlify does not run
this script.

    python tools/build_pages.py

Copy rules (from the H&M brand notes):
- Honest only. No made-up reviews, prices, stats or customer names.
- Stock / reference photos are captioned "Project example".
- No em or en dashes in visible copy.
- Never use: Premier, Elite, Industry-leading, World-class, transform.
"""

from __future__ import annotations

import html
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://hmjunkland.org"
PHONE_TEL = "2029997885"
PHONE_DISPLAY = "202-999-7885"
SMS = "sms:+12029997885?&body=Hi%20H%26M%2C%20I%27d%20like%20a%20free%20quote.%20I%27ll%20send%20photos."
CSS_VERSION = "20261009-reviews2"
JS_VERSION = "20261009-reviews2"
TODAY = date.today().isoformat()
BUSINESS_ID = f"{SITE}/#business"

FAIRFAX = ["Herndon", "Reston", "Vienna", "Oakton", "Oak Hill", "Fairfax",
           "Chantilly", "Centreville", "Great Falls", "McLean", "Burke"]
LOUDOUN = ["Sterling", "Ashburn"]
TOWNS = FAIRFAX + LOUDOUN

e = html.escape


# ---------------------------------------------------------------- icons
ICON = {
    "phone": '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.58 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.4 11.4 0 0 0 .58 3.6 1 1 0 0 1-.25 1z"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M4 4h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H8l-4 4V6a2 2 0 0 1 2-2z"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true"><path fill="currentColor" d="M5 12h12m0 0-5-5m5 5-5 5"/></svg>',
    "check": '<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path fill="currentColor" d="M9.5 17.5 4 12l1.5-1.5 4 4 9-9L20 6z"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path fill="currentColor" d="M12 2C8 2 5 5 5 9c0 5 7 13 7 13s7-8 7-13c0-4-3-7-7-7zm0 9.5A2.5 2.5 0 1 1 12 6a2.5 2.5 0 0 1 0 5.5z"/></svg>',
    "up": '<svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true"><path fill="currentColor" d="M12 20V6m0 0-6 6m6-6 6 6"/></svg>',
}


# ---------------------------------------------------------------- services
SERVICES = [
    {
        "slug": "junk-removal",
        "nav": "Junk Removal",
        "name": "Junk Removal & Hauling",
        "service_type": "Junk removal",
        "h1": "Junk Removal in Northern Virginia",
        "title": "Junk Removal in Herndon & Northern Virginia | H&M",
        "desc": "Junk removal in Herndon, Reston, Fairfax and across Northern Virginia. Furniture, appliances, garage piles and full loads. Text photos for a free quote.",
        "eyebrow": "Junk Removal & Hauling",
        "lede": "Furniture, mattresses, appliances, garage piles. One item or a full truckload. Text a few photos and get one clear price back, usually within the hour.",
        "img": "assets/hm-truck.webp", "img_w": 1500, "img_h": 938,
        "img_alt": "The H&M truck loaded with a junk haul in a Northern Virginia driveway",
        "img_tag": "Our truck", "img_example": False,
        "card": "Furniture, mattresses, appliances and garage piles. Single items to full loads.",
        "includes_title": "What we haul",
        "includes": [
            ("Furniture", "Couches, sectionals, recliners, dressers, tables, desks and bed frames."),
            ("Mattresses", "Mattresses and box springs, any size, carried out and loaded."),
            ("Appliances", "Washers, dryers and other household appliances."),
            ("Garage & basement piles", "Boxes, old tools, bikes, shelving and years of clutter."),
            ("Yard debris", "Branches, brush and bagged leaves that need to go."),
            ("Curbside piles", "Stuff already at the curb that the trash pickup left behind."),
        ],
        "price_points": [
            "How much there is, measured by how much of the truck it fills",
            "How heavy it is",
            "How far we carry it, and whether there are stairs",
            "Disposal for what we haul",
        ],
        "faqs": [
            ("How much does junk removal cost?",
             "We price by the job, not by the hour. Text 3 to 5 photos of what needs to go and we send back one clear price. Loading, hauling and disposal are in that number, so there is no clock running while we work."),
            ("How fast can you come out?",
             "Quotes usually come back within the hour. Same-day and next-day slots are often available, so text us early if you are on a deadline."),
            ("Do I have to carry anything out?",
             "No. We do the lifting, the carrying and the loading. Just show us what goes."),
            ("What happens to my stuff?",
             "It gets hauled to the dump or to donation. If something is still usable and you want it donated, tell us and we will set it aside for a donation run."),
            ("Is there anything you won't take?",
             "If you are not sure about an item, text a photo and ask. We will tell you straight before we show up."),
        ],
        "related": ["cleanouts", "furniture-removal", "yard-cleanup"],
    },
    {
        "slug": "cleanouts",
        "nav": "Cleanouts",
        "name": "Garage, Basement & Attic Cleanouts",
        "service_type": "Cleanout service",
        "h1": "Garage, Basement & Attic Cleanouts",
        "title": "Garage & Basement Cleanouts in Northern Virginia | H&M",
        "desc": "Garage, basement, attic, shed and move-out cleanouts across Northern Virginia. We bring the labor and the truck. Text photos for a free, by-the-job quote.",
        "eyebrow": "Cleanouts",
        "lede": "Garages, basements, attics, sheds and move-outs. You point at what stays. Everything else goes on the truck, and we sweep out the space when we are done.",
        "img": "assets/svc-cleanout.webp", "img_w": 760, "img_h": 428,
        "img_alt": "A cleared-out garage after a cleanout",
        "img_tag": "Project example", "img_example": True,
        "card": "Garages, basements, attics, sheds and move-outs. Labor, truck, and a plan.",
        "includes_title": "Spaces we clear out",
        "includes": [
            ("Garages", "Get the cars back in. Shelving, boxes, old equipment and everything in between."),
            ("Basements", "Furniture, storage bins and the stuff nobody has looked at in years, carried up and out."),
            ("Attics", "We carry it down so you don't have to balance on the ladder."),
            ("Sheds", "Old mowers, broken tools, rotted lumber and pots."),
            ("Move-outs & rentals", "Leftovers after a move, for homeowners, renters and landlords."),
            ("Downsizing", "Clearing out a family home one room at a time, at your pace."),
        ],
        "price_points": [
            "How much is in the space",
            "How heavy it is, and how far we carry it",
            "Stairs, attic access and tight spaces",
            "Disposal for what we haul",
        ],
        "faqs": [
            ("How much does a cleanout cost?",
             "Cleanouts are priced by the job. Send photos of each area, including the corners and shelves, and we send one clear price. The more angles you send, the tighter the quote."),
            ("How long does a cleanout take?",
             "It depends on the size of the space and how full it is. We tell you up front how long we expect it to take, so you can plan around it."),
            ("Can you work around a move-out date?",
             "Yes. Text us the date. Same-day and next-day slots are often available, and earlier is always easier."),
            ("Do you sort what stays and what goes?",
             "You make the calls, we do the work. Mark or tell us what stays and everything else gets loaded. Usable items can go to donation if you want."),
        ],
        "related": ["junk-removal", "furniture-removal", "power-washing"],
    },
    {
        "slug": "furniture-removal",
        "nav": "Furniture & Appliances",
        "name": "Furniture, Mattress & Appliance Removal",
        "service_type": "Furniture removal",
        "h1": "Furniture, Mattress & Appliance Removal",
        "title": "Furniture & Mattress Removal in Northern Virginia | H&M",
        "desc": "Couch, mattress, furniture and appliance removal in Herndon, Reston, Fairfax and nearby. Single items welcome. Text a photo for a free quote.",
        "eyebrow": "Single items to full rooms",
        "lede": "One couch or a whole room set. Mattresses, box springs, dressers, washers and dryers. We carry it out, load it and haul it off.",
        "img": "assets/crew.webp", "img_w": 1448, "img_h": 1086,
        "img_alt": "The H&M crew in front of their truck in Northern Virginia",
        "img_tag": "The H&M crew", "img_example": False,
        "card": "Couches, mattresses, dressers and appliances. One item is fine.",
        "includes_title": "What we pick up",
        "includes": [
            ("Couches & sectionals", "Including the heavy sleeper sofa nobody wants to move."),
            ("Mattresses & box springs", "Any size, from a guest room or a whole house."),
            ("Bedroom & dining sets", "Dressers, bed frames, tables, chairs and hutches."),
            ("Recliners & office chairs", "Bulky, awkward and finally out of the way."),
            ("Washers & dryers", "And other household appliances, carried out and loaded."),
            ("One single item", "No minimum pile. One item is a real job to us."),
        ],
        "price_points": [
            "How many pieces, and how big",
            "How heavy they are",
            "Stairs, tight hallways and how far we carry",
            "Disposal for what we haul",
        ],
        "faqs": [
            ("Can you take just one item?",
             "Yes. One couch, one mattress or one appliance is a normal job for us. Text a photo and we send a price."),
            ("Can you get it out of an upstairs room or a basement?",
             "Yes. Mention stairs or a tight turn in your text so the quote covers it."),
            ("Can my furniture be donated?",
             "If it is in usable shape and you want it donated, tell us. We can take it to donation instead of the dump."),
            ("How much does furniture removal cost?",
             "It is priced by the job: what the pieces are, how heavy, and how far we carry them. Send a photo and you get one clear number back."),
        ],
        "related": ["junk-removal", "cleanouts", "yard-cleanup"],
    },
    {
        "slug": "yard-cleanup",
        "nav": "Yard Cleanup",
        "name": "Yard Cleanup & Brush Removal",
        "service_type": "Yard cleanup",
        "h1": "Yard Cleanup & Brush Removal",
        "title": "Yard Cleanup & Brush Removal in Northern Virginia | H&M",
        "desc": "Leaf cleanup, brush and branch removal, overgrowth and storm cleanup across Northern Virginia. We clean it up and haul it away. Text photos for a free quote.",
        "eyebrow": "Yard Cleanup",
        "lede": "Leaves, branches, overgrowth and storm mess. We clean it up and haul the debris away in the same trip, so nothing sits in a pile at the curb.",
        "img": "assets/svc-yard.jpg", "img_w": 760, "img_h": 428,
        "img_alt": "A tidy front yard after a cleanup",
        "img_tag": "Project example", "img_example": True,
        "card": "Leaves, branches, overgrowth and storm cleanup, hauled in one trip.",
        "includes_title": "What a cleanup covers",
        "includes": [
            ("Leaf cleanup", "Fall and spring leaf cleanups, raked, bagged or loaded and hauled."),
            ("Brush & branches", "Fallen limbs, cut brush and branch piles cleared out."),
            ("Overgrowth", "Weed whacking and cutting back the parts of the yard that got away from you."),
            ("Storm cleanup", "Downed limbs and scattered debris after a storm."),
            ("Beds & edges", "Weeds pulled out of beds and clean edges along walks and driveways."),
            ("Haul-away", "All the yard waste goes on our truck. Nothing left at the curb."),
        ],
        "price_points": [
            "How big the yard or area is",
            "How much debris there is to haul",
            "Slopes, fences and how far we carry it to the truck",
            "Disposal for yard waste",
        ],
        "faqs": [
            ("Do you haul the debris away?",
             "Yes. Leaves, brush and branches go on our truck the same trip. You are not left with a pile at the curb."),
            ("Do you cut down trees?",
             "We handle fallen limbs, brush and cutback. Big standing trees usually need a tree service with climbing gear. Text a photo and we will tell you straight if it is a job for us."),
            ("When should I book a fall leaf cleanup?",
             "Most people book once the majority of leaves are down. Text us early in the season to get on the schedule."),
            ("How much does a yard cleanup cost?",
             "It is priced by the job. Send photos of the whole area from a few angles and we send one clear price."),
        ],
        "related": ["mulching", "power-washing", "junk-removal"],
    },
    {
        "slug": "mulching",
        "nav": "Mulching & Landscaping",
        "name": "Mulching & Landscaping",
        "service_type": "Landscaping",
        "h1": "Mulching & Landscaping",
        "title": "Mulching & Landscaping in Northern Virginia | H&M",
        "desc": "Mulch installation, bed cleanup, edging, hedge trimming and mowing across Northern Virginia. Text photos of your beds for a free quote.",
        "eyebrow": "Mulch & Beds",
        "lede": "Fresh mulch, clean beds and sharp edges. The kind of curb appeal you notice every time you pull into the driveway.",
        "img": "assets/svc-mulch.webp", "img_w": 760, "img_h": 410,
        "img_alt": "Fresh mulch and a clean planting bed",
        "img_tag": "Project example", "img_example": True,
        "card": "Fresh mulch, clean beds, edging, and curb appeal that lasts.",
        "includes_title": "What we do",
        "includes": [
            ("Mulch installation", "Fresh mulch spread evenly through your beds and around trees."),
            ("Bed cleanup", "Weeds and old debris pulled out before the new mulch goes down."),
            ("Edging", "Clean, defined edges between the lawn and the beds."),
            ("Hedge & shrub trimming", "Shrubs and hedges cut back neat and even."),
            ("Mowing", "Lawn mowing to go with a bed refresh or cleanup."),
            ("Seasonal refresh", "Spring and fall refreshes to keep the front of the house sharp."),
        ],
        "price_points": [
            "How many beds, and how big",
            "How much mulch it takes",
            "How much weeding and cleanup comes first",
            "Edging and trimming on top",
        ],
        "faqs": [
            ("Do you bring the mulch?",
             "Tell us in your text whether you already have mulch. Either way, the quote spells out exactly what is included."),
            ("How much mulch do I need?",
             "Send photos of each bed and a rough idea of the size. We work out how much it takes and put it in the quote."),
            ("When is the best time to mulch?",
             "Spring is the most popular time, and fall works well too. Text us when you want it done and we will find a slot."),
            ("How much does mulching cost?",
             "It is priced by the job: the number and size of the beds, the mulch, and any cleanup first. Photos get you one clear number."),
        ],
        "related": ["yard-cleanup", "power-washing", "junk-removal"],
    },
    {
        "slug": "power-washing",
        "nav": "Power Washing",
        "name": "Power Washing",
        "service_type": "Pressure washing",
        "h1": "Power Washing in Northern Virginia",
        "title": "Power Washing in Northern Virginia | H&M",
        "desc": "Power washing for driveways, sidewalks, patios, decks, fences and siding across Northern Virginia. Text photos for a free, by-the-job quote.",
        "eyebrow": "Power Washing",
        "lede": "Driveways, sidewalks, patios, decks, fences and siding. Years of dirt, grime and green buildup, washed off and back to looking new.",
        "img": "assets/svc-power.jpg", "img_w": 760, "img_h": 570,
        "img_alt": "A driveway after pressure washing",
        "img_tag": "Project example", "img_example": True,
        "card": "Driveways, sidewalks, decks, fences, and siding, back to like new.",
        "includes_title": "What we wash",
        "includes": [
            ("Driveways", "Concrete driveways with years of tire marks and grime."),
            ("Sidewalks & walkways", "Front walks and paths that went green or gray."),
            ("Patios", "Patio slabs and pavers ready for cookout season."),
            ("Decks", "Wood and composite decks, washed with the right pressure for the surface."),
            ("Fences", "Wood and vinyl fences, both sides if you want."),
            ("Siding", "House siding that picked up dirt and green buildup."),
        ],
        "price_points": [
            "How many surfaces, and how big",
            "What they are made of",
            "How heavy the buildup is",
            "Access around the house",
        ],
        "faqs": [
            ("Will power washing damage my deck or siding?",
             "Different surfaces need different pressure. Tell us what the surface is made of when you text photos and we wash it accordingly."),
            ("How much does power washing cost?",
             "It is priced by the job. Send photos of each surface and a rough size and we send back one clear number."),
            ("Can you do a driveway and a deck in the same visit?",
             "Yes. Put everything in one text and you get one price for the whole list."),
            ("When is a good time to power wash?",
             "Spring and early summer are the most popular, before cookout season. Any dry day with decent weather works."),
        ],
        "related": ["mulching", "yard-cleanup", "cleanouts"],
    },
]
BY_SLUG = {s["slug"]: s for s in SERVICES}


# ---------------------------------------------------------------- shared chrome
def head(*, title: str, desc: str, path: str, schema: list[dict], og_image: str | None = None,
         noindex: bool = False, og_alt: str | None = None) -> str:
    url = SITE + path
    og_image = og_image or f"{SITE}/assets/hm-truck.jpg"
    og_alt = og_alt or "The H&M truck loaded with a junk haul in a Northern Virginia driveway"
    robots = '\n  <meta name="robots" content="noindex, follow" />' if noindex else ""
    canonical = "" if noindex else f'\n  <link rel="canonical" href="{url}" />'
    ld = "\n".join(
        f'  <script type="application/ld+json">\n{json.dumps(s, indent=2, ensure_ascii=False)}\n  </script>'
        for s in schema
    )
    fonts = "https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&family=Inter:wght@400;500;600;700&family=Bebas+Neue&display=swap"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
  <meta name="theme-color" content="#1F4D33" />
  <title>{e(title)}</title>
  <meta name="description" content="{e(desc)}" />{robots}{canonical}
  <link rel="icon" type="image/png" href="/assets/favicon.png" />

  <meta property="og:type" content="website" />
  <meta property="og:title" content="{e(title)}" />
  <meta property="og:description" content="{e(desc)}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:site_name" content="H&amp;M Junk Removal &amp; Landscaping" />
  <meta property="og:image" content="{og_image}" />
  <meta property="og:image:alt" content="{e(og_alt)}" />
  <meta name="twitter:card" content="summary_large_image" />

{ld}

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="{fonts}" media="print" onload="this.media='all'" />
  <noscript><link rel="stylesheet" href="{fonts}" /></noscript>

  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js" defer></script>
  <link rel="stylesheet" href="/styles.css?v={CSS_VERSION}" />
  <noscript><style>[data-reveal] {{ opacity: 1 !important; transform: none !important; }}</style></noscript>
</head>
<body class="subpage">
"""


def header() -> str:
    links = [("/#services", "Services"), ("/#hm-how-it-works", "How It Works"),
             ("/service-areas/", "Areas"), ("/#about", "About"), ("/quote/", "Free Quote")]
    nav = "\n        ".join(f'<a href="{h}">{t}</a>' for h, t in links)
    drawer = "\n      ".join(f'<a href="{h}">{t}</a>' for h, t in links)
    return f"""
  <div class="scroll-progress" id="scrollProgress" aria-hidden="true"></div>
  <a class="skip-link" href="#main">Skip to main content</a>

  <header class="site-header" id="top">
    <div class="container nav-wrap">
      <a href="/" class="brand brand-logo-img" aria-label="H&amp;M Junk Removal and Landscaping home">
        <img decoding="async" loading="eager" src="/assets/logo-primary.webp" alt="H&amp;M Junk Removal &amp; Landscaping" width="700" height="156" />
      </a>

      <nav class="primary-nav" aria-label="Primary">
        {nav}
      </nav>

      <div class="header-cta">
        <a class="phone-pill" href="tel:{PHONE_TEL}" aria-label="Call us at {PHONE_DISPLAY}">
          {ICON['phone'].replace('width="18" height="18"', 'width="14" height="14"')}
          {PHONE_DISPLAY}
        </a>
        <a class="btn btn-primary" href="{SMS}">Text Photos for a Quote
          {ICON['arrow']}
        </a>
      </div>

      <button class="menu-toggle" id="menuToggle" aria-label="Open menu" aria-expanded="false">
        <span></span><span></span>
      </button>
    </div>

    <div class="mobile-drawer" id="mobileDrawer" hidden>
      {drawer}
      <div class="drawer-cta">
        <a class="btn btn-primary block" href="{SMS}">Text Photos for a Quote</a>
        <a class="btn btn-outline block" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
      </div>
    </div>
  </header>
"""


def footer_html(prefix: str = "/") -> str:
    """Footer shared by every page. prefix='/' on sub-pages; the homepage uses the same markup."""
    svc = "\n          ".join(
        f'<li><a href="/{s["slug"]}/">{e(s["name"])}</a></li>' for s in SERVICES)
    return f"""
  <footer class="site-footer">
    <div class="footer-strip">
      <div class="container footer-strip-inner">
        <span class="footer-strip-item">Based in Northern Virginia</span>
        <span class="footer-strip-dot" aria-hidden="true"></span>
        <span class="footer-strip-item">Serving homes, rentals, HOAs &amp; businesses</span>
        <span class="footer-strip-dot" aria-hidden="true"></span>
        <span class="footer-strip-item">Young crew. Strong work ethic. Clean results.</span>
      </div>
    </div>
    <div class="container footer-grid">
      <div>
        <a href="{prefix}" class="brand-footer-logo">
          <img decoding="async" loading="lazy" src="/assets/logo-primary.webp" alt="H&amp;M Junk Removal &amp; Landscaping" width="700" height="156" />
        </a>
        <p class="muted small">Local, owner-operated junk removal and landscaping in Northern Virginia. Run by Miles Dickey and a small student crew.</p>
      </div>

      <div>
        <h4>Contact</h4>
        <ul class="footer-list">
          <li><a href="tel:{PHONE_TEL}">Call: {PHONE_DISPLAY}</a></li>
          <li><a href="{SMS}">Text: {PHONE_DISPLAY}</a></li>
          <li><a href="/quote/">Free quote form</a></li>
        </ul>
      </div>

      <div>
        <h4>Services</h4>
        <ul class="footer-list">
          {svc}
        </ul>
      </div>

      <div>
        <h4>Service Areas</h4>
        <ul class="footer-list">
          <li>Herndon · Reston · Vienna · Oakton</li>
          <li>Oak Hill · Fairfax · Chantilly</li>
          <li>Great Falls · McLean · Sterling</li>
          <li>Centreville · Ashburn · Burke</li>
          <li><a href="/service-areas/">All service areas</a></li>
        </ul>
      </div>
    </div>

    <div class="container footer-bottom">
      <span>© <span id="year"></span> H&amp;M Junk Removal &amp; Landscaping</span>
      <a href="#top" class="back-top">Back to top
        {ICON['up']}
      </a>
    </div>
  </footer>
"""


def tail() -> str:
    return f"""
  <div class="mobile-bar">
    <a href="tel:{PHONE_TEL}" class="mobile-bar-btn">
      {ICON['phone'].replace('width="18" height="18"', 'width="16" height="16"')}
      Call
    </a>
    <a href="{SMS}" class="mobile-bar-btn mobile-bar-btn-primary">
      {ICON['chat'].replace('width="18" height="18"', 'width="16" height="16"')}
      Text Photos
    </a>
  </div>

  <script src="/script.js?v={JS_VERSION}" defer></script>
</body>
</html>
"""


def page(*, head_html: str, main: str) -> str:
    return head_html + header() + f'\n  <main id="main">\n{main}\n  </main>\n' + footer_html() + tail()


# ---------------------------------------------------------------- sections
def breadcrumbs(items: list[tuple[str, str]]) -> str:
    parts = []
    for i, (label, href) in enumerate(items):
        if i == len(items) - 1:
            parts.append(f'<li aria-current="page">{e(label)}</li>')
        else:
            parts.append(f'<li><a href="{href}">{e(label)}</a></li>')
    return '<nav class="pg-crumbs" aria-label="Breadcrumb"><ol>' + "".join(parts) + "</ol></nav>"


def breadcrumb_schema(items: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": label, "item": SITE + href}
            for i, (label, href) in enumerate(items)
        ],
    }


def cta_buttons(light: bool = True) -> str:
    second = "btn-light-outline" if light else "btn-outline"
    return f"""<div class="pg-cta-row">
          <a class="btn btn-primary btn-lg btn-glow" href="{SMS}">{ICON['chat']} Text Photos for a Free Quote</a>
          <a class="btn {second} btn-lg" href="tel:{PHONE_TEL}">{ICON['phone']} Call {PHONE_DISPLAY}</a>
        </div>"""


def hero(*, crumbs: list[tuple[str, str]], eyebrow: str, h1: str, lede: str, img: str | None = None,
         img_w: int = 0, img_h: int = 0, img_alt: str = "", img_tag: str = "", img_example: bool = False,
         extra: str = "") -> str:
    figure = ""
    if img:
        tag_cls = "pg-tag pg-tag-example" if img_example else "pg-tag"
        figure = f"""
      <figure class="pg-hero-figure" data-reveal>
        <img decoding="async" loading="eager" fetchpriority="high" src="/{img}" alt="{e(img_alt)}" width="{img_w}" height="{img_h}" />
        <figcaption class="{tag_cls}">{e(img_tag)}</figcaption>
      </figure>"""
    grid_cls = "pg-hero-grid" if img else "pg-hero-grid pg-hero-solo"
    return f"""
  <section class="pg-hero">
    <div class="pg-hero-glow" aria-hidden="true"></div>
    <div class="container {grid_cls}">
      <div class="pg-hero-copy">
        {breadcrumbs(crumbs)}
        <div class="hero-eyebrow"><span class="pulse-dot"></span>{e(eyebrow)}</div>
        <h1>{e(h1)}</h1>
        <p class="pg-lede">{e(lede)}</p>
        {cta_buttons()}
        <ul class="pg-trust">
          <li>{ICON['check']} Free photo quotes</li>
          <li>{ICON['check']} Priced by the job</li>
          <li>{ICON['check']} Local, student-run crew</li>
        </ul>{extra}
      </div>{figure}
    </div>
  </section>"""


def steps_section(num: str) -> str:
    steps = [
        ("Text a few photos", "3 to 5 photos of the pile or project area. More angles mean a tighter quote."),
        ("Get one clear price", "A by-the-job number, usually within the hour. No hourly clock."),
        ("Pick a time", "Same-day and next-day slots are often available."),
        ("We handle the rest", "Loaded, hauled and cleaned up. You only notice what is gone."),
    ]
    items = "\n".join(
        f"""          <li class="pg-step" data-reveal>
            <span class="pg-step-num">0{i + 1}</span>
            <h3>{e(t)}</h3>
            <p>{e(d)}</p>
          </li>""" for i, (t, d) in enumerate(steps))
    return f"""
  <section class="section pg-steps-section">
    <div class="container">
      <header class="section-head" data-reveal>
        <div class="kicker"><span class="kicker-num">{num}</span><span class="kicker-label">How It Works</span></div>
        <h2>Text it. Quote it. <em>Done.</em></h2>
      </header>
      <ol class="pg-steps">
{items}
      </ol>
    </div>
  </section>"""


def faq_section(num: str, faqs: list[tuple[str, str]], title: str) -> str:
    items = "\n".join(
        f"""        <details class="pg-faq-item"{' open' if i == 0 else ''}>
          <summary>{e(q)}</summary>
          <p>{e(a)}</p>
        </details>""" for i, (q, a) in enumerate(faqs))
    return f"""
  <section class="section pg-faq-section">
    <div class="container pg-narrow">
      <header class="section-head" data-reveal>
        <div class="kicker"><span class="kicker-num">{num}</span><span class="kicker-label">Questions</span></div>
        <h2>{e(title)}</h2>
      </header>
      <div class="pg-faq" data-reveal>
{items}
      </div>
    </div>
  </section>"""


def areas_strip(num: str, service_name: str) -> str:
    pills = "".join(f"<li>{e(t)}</li>" for t in TOWNS)
    return f"""
  <section class="section section-areas pg-areas">
    <div class="container">
      <header class="section-head section-head-light" data-reveal>
        <div class="kicker"><span class="kicker-num">{num}</span><span class="kicker-label">Service Areas</span></div>
        <h2>{e(service_name)} across <em>Northern Virginia.</em></h2>
        <p>Based in Herndon and working across Fairfax and Loudoun counties, generally within about 40 minutes of home base.</p>
      </header>
      <div class="areas-row" data-reveal>
        <ul class="areas-pill-grid">{pills}</ul>
      </div>
      <div class="areas-cta" data-reveal>
        <a class="btn btn-primary btn-lg" href="/service-areas/">See all service areas</a>
        <a class="btn btn-light-outline btn-lg" href="{SMS}">Check my area by text</a>
      </div>
    </div>
  </section>"""


def related_section(num: str, slugs: list[str]) -> str:
    cards = "\n".join(
        f"""        <a class="pg-related-card" href="/{s['slug']}/" data-reveal>
          <span class="pg-related-img"><img decoding="async" loading="lazy" src="/{s['img']}" alt="" width="{s['img_w']}" height="{s['img_h']}" />{'<span class="pg-tag pg-tag-example pg-tag-sm">Project example</span>' if s['img_example'] else ''}</span>
          <span class="pg-related-body">
            <strong>{e(s['name'])}</strong>
            <span>{e(s['card'])}</span>
            <span class="link-arrow">Learn more {ICON['arrow']}</span>
          </span>
        </a>""" for s in (BY_SLUG[x] for x in slugs))
    return f"""
  <section class="section pg-related-section">
    <div class="container">
      <header class="section-head" data-reveal>
        <div class="kicker"><span class="kicker-num">{num}</span><span class="kicker-label">More Services</span></div>
        <h2>One crew for the <em>whole job.</em></h2>
      </header>
      <div class="pg-related">
{cards}
      </div>
    </div>
  </section>"""



# ---------------------------------------------------------------- reviews
# Copied word for word from the Google Business Profile (Oct 2026). Never edit
# the text. Ian Lee left 5 stars with no written review, so he is counted in
# the rating but has no card. Customer words are exempt from the copy rules.
GOOGLE_URL = "https://maps.google.com/?cid=7233374597949165858"
GOOGLE_RATING = "5.0"
GOOGLE_COUNT = 6
REVIEWS = [
    ("Liza Paqueo", "These gentlemen are polite, hardworking and excellent. My backyard patio was transformed. It had looked like a junkyard, but now it is immaculate."),
    ("Skerdi Kostreci", "Hard working and very polite young boys. Very impressed! Will definitely hire them again."),
    ("Bloxy Clips", "Great work and amazing attention to detail it was my pleasure to hire them"),
    ("Goopert", "Very professional and efficient!"),
    ("TtvCOMA HYPER", "definitely calling them back for another job!"),
]
G_ICON = '<svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true"><path fill="#4285F4" d="M23.5 12.3c0-.8-.1-1.6-.2-2.3H12v4.4h6.5a5.6 5.6 0 0 1-2.4 3.6v3h3.9c2.2-2.1 3.5-5.1 3.5-8.7z"/><path fill="#34A853" d="M12 24c3.2 0 6-1.1 8-2.9l-3.9-3c-1.1.7-2.5 1.2-4.1 1.2-3.1 0-5.8-2.1-6.7-5H1.3v3.1A12 12 0 0 0 12 24z"/><path fill="#FBBC05" d="M5.3 14.3a7.2 7.2 0 0 1 0-4.6V6.6H1.3a12 12 0 0 0 0 10.8z"/><path fill="#EA4335" d="M12 4.8c1.8 0 3.3.6 4.6 1.8l3.4-3.4A12 12 0 0 0 1.3 6.6l4 3.1c.9-2.9 3.6-4.9 6.7-4.9z"/></svg>'


def review_cards(items) -> str:
    return "\n".join(
        f"""        <figure class="rv-card" data-reveal>
          <div class="rv-stars" aria-label="5 out of 5 stars">★★★★★</div>
          <blockquote class="rv-quote">{e(text)}</blockquote>
          <figcaption class="rv-who"><strong>{e(name)}</strong><span>{G_ICON} Google review</span></figcaption>
        </figure>""" for name, text in items)


def reviews_section(num: str, items=None, title: str = "What neighbors are saying.") -> str:
    items = items or REVIEWS
    return f"""
  <section class="section rv-section">
    <div class="container">
      <header class="section-head" data-reveal>
        <div class="kicker"><span class="kicker-num">{num}</span><span class="kicker-label">Reviews</span></div>
        <h2>{e(title)}</h2>
        <p class="section-lede"><a class="rv-rating" href="{GOOGLE_URL}" target="_blank" rel="noopener"><span aria-hidden="true">★★★★★</span> {GOOGLE_RATING} on Google from {GOOGLE_COUNT} reviews</a>. Every review here is copied word for word from Google.</p>
      </header>
      <div class="rv-grid">
{review_cards(items)}
      </div>
      <div class="rv-actions" data-reveal>
        <a class="btn btn-primary" href="{GOOGLE_URL}" target="_blank" rel="noopener">Read all reviews on Google</a>
        <a class="btn btn-outline" href="{GOOGLE_URL}" target="_blank" rel="noopener">Leave us a review</a>
      </div>
    </div>
  </section>"""


def final_cta(title: str, text: str) -> str:
    return f"""
  <section class="final-cta">
    <div class="final-cta-bg" aria-hidden="true"><div class="blob blob-final"></div></div>
    <div class="container final-cta-inner" data-reveal>
      <h2>{e(title)}</h2>
      <p>{e(text)}</p>
      <div class="final-cta-buttons">
        <a class="btn btn-primary btn-lg btn-glow" href="{SMS}">Text Photos for a Free Quote</a>
        <a class="btn btn-light-outline btn-lg" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
      </div>
      <p class="fine">No job too small · Fast quotes · Fair pricing · Hard work</p>
    </div>
  </section>"""


# ---------------------------------------------------------------- pages
def service_page(s: dict) -> str:
    path = f"/{s['slug']}/"
    crumbs = [("Home", "/"), (s["name"], path)]
    schema = [
        {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": s["name"],
            "serviceType": s["service_type"],
            "url": SITE + path,
            "description": s["desc"],
            "provider": {"@type": "LocalBusiness", "@id": BUSINESS_ID, "name": "H&M Junk Removal & Landscaping",
                         "telephone": "+1-202-999-7885", "url": SITE},
            "areaServed": [{"@type": "City", "name": f"{t}, VA"} for t in TOWNS]
            + [{"@type": "AdministrativeArea", "name": "Fairfax County, VA"},
               {"@type": "AdministrativeArea", "name": "Loudoun County, VA"}],
        },
        breadcrumb_schema(crumbs),
    ]
    includes = "\n".join(
        f"""        <div class="pg-check-card" data-reveal>
          <span class="pg-check-ico">{ICON['check']}</span>
          <h3>{e(t)}</h3>
          <p>{e(d)}</p>
        </div>""" for t, d in s["includes"])
    points = "\n".join(f"            <li>{ICON['check']}<span>{e(p)}</span></li>" for p in s["price_points"])
    example_note = (
        '<p class="pg-photo-note">Photos marked "Project example" show the kind of job we take on, not a specific H&amp;M job. Real job photos are on the way.</p>'
        if s["img_example"] else "")
    main = hero(crumbs=crumbs, eyebrow=s["eyebrow"], h1=s["h1"], lede=s["lede"], img=s["img"],
                img_w=s["img_w"], img_h=s["img_h"], img_alt=s["img_alt"], img_tag=s["img_tag"],
                img_example=s["img_example"])
    main += f"""

  <section class="section pg-includes">
    <div class="container">
      <header class="section-head" data-reveal>
        <div class="kicker"><span class="kicker-num">01</span><span class="kicker-label">{e(s['includes_title'])}</span></div>
        <h2>{e(s['name'])}, <em>done right.</em></h2>
        <p class="section-lede">Not sure if it is on the list? Text a photo and ask. We will tell you straight.</p>
      </header>
      <div class="pg-check-grid">
{includes}
      </div>
    </div>
  </section>

  <section class="section pg-pricing">
    <div class="container pg-split">
      <div class="pg-split-copy" data-reveal>
        <div class="kicker"><span class="kicker-num">02</span><span class="kicker-label">Pricing</span></div>
        <h2>One price for the job. <em>No hourly clock.</em></h2>
        <p>We quote {e(s['name'].lower())} by the job, from your photos. You get one number before we lift a thing, and that number is the price.</p>
        <div class="pg-points">
          <h3>What goes into the price</h3>
          <ul>
{points}
          </ul>
        </div>
        <a class="btn btn-primary btn-lg" href="{SMS}">{ICON['chat']} Text photos for my price</a>
      </div>
      <div class="pg-split-panel" data-reveal>
        <div class="pg-panel-card">
          <span class="pg-panel-big">3-5</span>
          <p>photos is usually all it takes for an accurate quote. Wide shots plus a close-up or two.</p>
        </div>
        <div class="pg-panel-card pg-panel-dark">
          <span class="pg-panel-big">1</span>
          <p>clear, by-the-job price back by text. Usually within the hour.</p>
        </div>
        {example_note}
      </div>
    </div>
  </section>
"""
    main += steps_section("03")
    main += reviews_section("04", REVIEWS[:3])
    main += faq_section("05", s["faqs"], f"{s['name']} questions")
    main += areas_strip("06", s["name"])
    main += related_section("07", s["related"])
    main += final_cta(f"Ready to get a price on {s['name'].lower()}?",
                      "Text us a few photos and we will send a fast, free quote. Local, honest work across Northern Virginia.")
    return page(head_html=head(title=s["title"], desc=s["desc"], path=path, schema=schema,
                               og_image=f"{SITE}/{s['img'].replace('.webp', '.jpg')}",  # scrapers prefer JPG
                               og_alt=s["img_alt"]), main=main)


def areas_page() -> str:
    path = "/service-areas/"
    crumbs = [("Home", "/"), ("Service Areas", path)]
    schema = [
        {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "@id": BUSINESS_ID,
            "name": "H&M Junk Removal & Landscaping",
            "url": SITE,
            "telephone": "+1-202-999-7885",
            "areaServed": [{"@type": "City", "name": f"{t}, VA"} for t in TOWNS],
        },
        breadcrumb_schema(crumbs),
    ]

    def county(name: str, towns: list[str], note: str) -> str:
        cards = "".join(
            f"""
          <li class="pg-town{' pg-town-home' if t == 'Herndon' else ''}">
            {ICON['pin']}<strong>{e(t)}</strong>{'<span>Home base</span>' if t == 'Herndon' else ''}
          </li>""" for t in towns)
        return f"""
      <div class="pg-county" data-reveal>
        <h3>{e(name)}</h3>
        <p>{e(note)}</p>
        <ul class="pg-town-grid">{cards}
        </ul>
      </div>"""

    svc_links = "".join(
        f'<li><a href="/{s["slug"]}/">{e(s["name"])} {ICON["arrow"]}</a></li>' for s in SERVICES)
    main = hero(crumbs=crumbs, eyebrow="Service Areas", h1="Service Areas in Northern Virginia",
                lede="Based in Herndon. We work across Fairfax and Loudoun counties, generally within about 40 minutes of home base. Don't see your town? Text us, odds are we can still help.")
    main += f"""

  <section class="section pg-areas-list">
    <div class="container">
      <header class="section-head" data-reveal>
        <div class="kicker"><span class="kicker-num">01</span><span class="kicker-label">Where We Work</span></div>
        <h2>Where you'll find <em>our truck.</em></h2>
        <p class="section-lede">Every service is available in every town on this list.</p>
      </header>
      <div class="pg-counties">{county('Fairfax County', FAIRFAX, 'Home base is Herndon, so most of Fairfax County is a short drive away.')}{county('Loudoun County', LOUDOUN, 'Eastern Loudoun is a short drive from Herndon.')}
      </div>
    </div>
  </section>

  <section class="section pg-areas-services">
    <div class="container pg-split">
      <div class="pg-split-copy" data-reveal>
        <div class="kicker"><span class="kicker-num">02</span><span class="kicker-label">Services</span></div>
        <h2>Everything we do, <em>in every town.</em></h2>
        <p>Junk removal, cleanouts, yard work, mulch and power washing. Same crew, same by-the-job pricing, wherever you are on the list.</p>
        <ul class="pg-svc-links">{svc_links}</ul>
      </div>
      <div class="pg-split-panel" data-reveal>
        <div class="pg-panel-card pg-panel-dark">
          <span class="pg-panel-big">~40</span>
          <p>minutes from our Herndon base is the usual range. Farther out? Text us anyway.</p>
        </div>
        <div class="pg-panel-card">
          <span class="pg-panel-big">2</span>
          <p>counties: Fairfax and Loudoun.</p>
        </div>
      </div>
    </div>
  </section>
"""
    main += steps_section("03")
    main += final_cta("In our area? Let's get you a price.",
                      "Text us a few photos and your town. We will send a fast, free quote.")
    return page(head_html=head(
        title="Service Areas in Fairfax & Loudoun County | H&M",
        desc="H&M serves Herndon, Reston, Vienna, Fairfax, McLean, Great Falls, Sterling, Ashburn and more across Fairfax and Loudoun counties. Text photos for a free quote.",
        path=path, schema=schema), main=main)


def quote_page() -> str:
    path = "/quote/"
    crumbs = [("Home", "/"), ("Free Quote", path)]
    town_opts = "".join(f'<option value="{e(t)}">{e(t)}</option>' for t in TOWNS)
    svc_opts = "".join(f'<option value="{e(s["name"])}">{e(s["name"])}</option>' for s in SERVICES)
    main = hero(crumbs=crumbs, eyebrow="Free Quote", h1="Get a Free Quote",
                lede="The fastest way is to text 3 to 5 photos to 202-999-7885. Rather fill out a form? Send it below and we will get back to you with a by-the-job price.")
    main += f"""

  <section class="section pg-quote">
    <div class="container pg-quote-grid">
      <form class="pg-form" name="quote" method="POST" action="/thanks/" data-netlify="true" netlify-honeypot="bot-field" enctype="multipart/form-data" data-reveal>
        <input type="hidden" name="form-name" value="quote" />
        <p class="pg-hp"><label>Leave this empty: <input name="bot-field" /></label></p>

        <h2>Tell us about the job</h2>
        <div class="pg-form-row">
          <label>Your name<span aria-hidden="true">*</span>
            <input type="text" name="name" autocomplete="name" required />
          </label>
          <label>Phone<span aria-hidden="true">*</span>
            <input type="tel" name="phone" autocomplete="tel" inputmode="tel" required />
          </label>
        </div>
        <div class="pg-form-row">
          <label>Email <small>(optional)</small>
            <input type="email" name="email" autocomplete="email" />
          </label>
          <label>Town<span aria-hidden="true">*</span>
            <select name="town" required>
              <option value="">Choose your town</option>{town_opts}<option value="Other">Somewhere else</option>
            </select>
          </label>
        </div>
        <label>What do you need?<span aria-hidden="true">*</span>
          <select name="service" required>
            <option value="">Choose a service</option>{svc_opts}<option value="Not sure / more than one">Not sure, or more than one</option>
          </select>
        </label>
        <label>Tell us about it
          <textarea name="details" rows="5" placeholder="What needs to go or get done, roughly how much, any stairs, and when you'd like it done."></textarea>
        </label>
        <label class="pg-file">Add a photo <small>(optional, one image up to 8 MB)</small>
          <input type="file" name="photo" accept="image/*" />
        </label>
        <fieldset class="pg-radio">
          <legend>Best way to reach you</legend>
          <label><input type="radio" name="contact_pref" value="Text" checked /> Text</label>
          <label><input type="radio" name="contact_pref" value="Call" /> Call</label>
          <label><input type="radio" name="contact_pref" value="Email" /> Email</label>
        </fieldset>
        <button class="btn btn-primary btn-lg btn-glow" type="submit">Send my quote request {ICON['arrow']}</button>
        <p class="pg-form-fine">We only use your info to reply about this job. No spam, no selling your number.</p>
      </form>

      <aside class="pg-quote-side" data-reveal>
        <div class="pg-panel-card pg-panel-dark">
          <h3>Faster: just text us</h3>
          <p>Photos tell us more than a form can. Text 3 to 5 pictures to <strong>{PHONE_DISPLAY}</strong> and get a price back, usually within the hour.</p>
          <a class="btn btn-primary btn-lg" href="{SMS}">{ICON['chat']} Text photos now</a>
        </div>
        <div class="pg-panel-card">
          <h3>Rather talk?</h3>
          <p>Call {PHONE_DISPLAY}. You will reach the person doing the job, not a call center.</p>
          <a class="btn btn-outline btn-lg" href="tel:{PHONE_TEL}">{ICON['phone']} Call {PHONE_DISPLAY}</a>
        </div>
        <div class="pg-panel-card">
          <h3>Good photos to send</h3>
          <ul class="pg-photo-tips">
            <li>{ICON['check']}<span>One wide shot of the whole pile or area</span></li>
            <li>{ICON['check']}<span>A couple of closer shots of big or heavy items</span></li>
            <li>{ICON['check']}<span>The path out: stairs, doors, the driveway</span></li>
          </ul>
        </div>
      </aside>
    </div>
  </section>
"""
    return page(head_html=head(
        title="Get a Free Quote | H&M Junk Removal & Landscaping",
        desc="Get a free, by-the-job quote for junk removal, cleanouts, yard cleanup, mulching or power washing in Northern Virginia. Text photos or send the form.",
        path=path, schema=[breadcrumb_schema(crumbs)]), main=main)


def thanks_page() -> str:
    main = hero(crumbs=[("Home", "/"), ("Thanks", "/thanks/")], eyebrow="Request received",
                h1="Thanks, we got it.",
                lede="We will get back to you with a price soon, usually within the hour during the day. Want to speed it up? Text a few photos of the job to 202-999-7885.")
    main += final_cta("Have photos? Send them over.",
                      "A few pictures let us lock in an exact price.")
    return page(head_html=head(title="Thanks | H&M Junk Removal & Landscaping",
                               desc="Your quote request was received.", path="/thanks/", schema=[],
                               noindex=True), main=main)


def not_found_page() -> str:
    links = "".join(f'<li><a href="/{s["slug"]}/">{e(s["name"])} {ICON["arrow"]}</a></li>' for s in SERVICES)
    main = hero(crumbs=[("Home", "/"), ("Page not found", "/404")], eyebrow="404",
                h1="That page got hauled away.",
                lede="The page you were looking for is not here. Try one of these, or just text us.",
                extra=f'\n        <ul class="pg-svc-links pg-svc-links-light">{links}<li><a href="/">Back to the homepage {ICON["arrow"]}</a></li></ul>')
    return page(head_html=head(title="Page not found | H&M Junk Removal & Landscaping",
                               desc="Page not found.", path="/404.html", schema=[], noindex=True), main=main)


# ---------------------------------------------------------------- sitemap
def sitemap() -> str:
    urls = ["/", "/service-areas/", "/quote/"] + [f"/{s['slug']}/" for s in SERVICES]
    rows = "\n".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{rows}
</urlset>
"""


# ---------------------------------------------------------------- write
BANNED = re.compile(r"[–—]|\b(premier|elite|industry-leading|world-class|transform\w*)\b", re.I)


def check_copy(name: str, doc: str) -> None:
    # customer quotes are shown exactly as written, so they skip the copy rules
    visible = re.sub(r"<script.*?</script>|<style.*?</style>|<blockquote.*?</blockquote>|<[^>]+>", " ", doc, flags=re.S)
    visible = html.unescape(visible)
    hits = [m.group(0) for m in BANNED.finditer(visible)]
    if hits:
        raise SystemExit(f"{name}: banned copy {hits}")


def write(rel: str, doc: str) -> None:
    check_copy(rel, doc)
    out = ROOT / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8", newline="\n")
    print("wrote", rel)


def main() -> None:
    for s in SERVICES:
        write(f"{s['slug']}/index.html", service_page(s))
    write("service-areas/index.html", areas_page())
    write("quote/index.html", quote_page())
    write("thanks/index.html", thanks_page())
    write("404.html", not_found_page())
    (ROOT / "sitemap.xml").write_text(sitemap(), encoding="utf-8", newline="\n")
    print("wrote sitemap.xml")


if __name__ == "__main__":
    main()
