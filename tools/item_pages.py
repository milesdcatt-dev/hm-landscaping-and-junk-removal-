"""Item pages, Nov 27, 2026. Safe to rerun.

Builds hot tub, shed, deck, construction debris and snow removal pages from the
live furniture-removal page (same header, footer, styles). Miles lists hot tub,
shed, deck and construction debris on the Google profile; snow removal he
confirmed in chat Nov 27. No prices, no insured/licensed claims, no equipment
claims we can't back up.

After this, run update_reviews.py (review cards) and seo_patch.py (FAQ schema,
llms.txt). Do NOT rerun build_pages.py (it is older than the live pages).
"""
import html
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "furniture-removal" / "index.html"
OLD_NAME = "Furniture, Mattress &amp; Appliance Removal"
OLD_NAME_RAW = "Furniture, Mattress & Appliance Removal"
CHECK = '<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path fill="currentColor" d="M9.5 17.5 4 12l1.5-1.5 4 4 9-9L20 6z"/></svg>'

PAGES = [
    {
        "slug": "hot-tub-removal",
        "name": "Hot Tub Removal",
        "service_type": "Hot tub removal",
        "title": "Hot Tub Removal in Herndon, Reston &amp; Fairfax | H&amp;M",
        "desc": "Old hot tub or spa removal in Herndon, Reston, Fairfax and Loudoun County. Taken out of the yard or deck and hauled off. Text a photo for a free quote.",
        "eyebrow": "Spas and hot tubs",
        "lede": "That old hot tub nobody has used in years. We get it out of the yard or off the deck, load it and haul it away, so you get the space back.",
        "img": ("/assets/hm-truck.webp", "The H&amp;M truck in Northern Virginia", 1500, 938, "The H&amp;M truck"),
        "includes_h2": "Hot tub removal, <em>start to finish.</em>",
        "includes_lede": "Not sure if yours is a fit? Text a photo of the tub and the path out to the street. We will tell you straight.",
        "cards": [
            ("Backyard hot tubs", "Sitting on a patio, pavers or the grass."),
            ("Tubs on a deck", "Carried off the deck and out to the truck."),
            ("The cover and steps", "The cover, steps and anything around it go too."),
            ("Swim spas", "Bigger tubs too. Send a photo so we can plan it."),
            ("Out through the gate", "We look at your gate and path before we quote."),
            ("Hauled off", "Taken away for disposal. Nothing left behind."),
        ],
        "points": ["The size of the tub", "Where it sits: patio, grass or deck", "The path out: gates, stairs, slopes", "Disposal for what we haul"],
        "faq": [
            ("Do I need to drain the hot tub first?", "Yes, please drain it and turn off its power at the breaker before we come. If you are not sure how, say so in your text."),
            ("Can you get it out of a fenced backyard?", "Usually, yes. Send a photo of the gate and the path to the street with your tub photos so the quote covers it."),
            ("Can you take the deck or pad under it too?", "Yes. Tell us if you want the deck or patio pieces gone as well, and we will price it all as one job."),
            ("How much does hot tub removal cost?", "It is priced by the job: the size of the tub, where it sits and how hard the path out is. Send a photo and you get one clear number back."),
        ],
        "reviews": ["carlos", "veljko", "donna"],
    },
    {
        "slug": "shed-removal",
        "name": "Shed Removal &amp; Demolition",
        "service_type": "Shed removal",
        "title": "Shed Removal &amp; Demolition in Northern Virginia | H&amp;M",
        "desc": "Old shed tear-down and removal in Herndon, Reston, Fairfax and Loudoun County. We take it apart, load it and haul it off. Text a photo for a free quote.",
        "eyebrow": "Tear-down and haul-off",
        "lede": "A rotting shed, a leaning shed or one you just don't need. We take it down, load every piece and haul it off. The stuff inside can go too.",
        "img": ("/assets/hm-truck.webp", "The H&amp;M truck in Northern Virginia", 1500, 938, "The H&amp;M truck"),
        "includes_h2": "Shed removal, <em>down to the ground.</em>",
        "includes_lede": "Text a photo of the shed, inside and out. We will tell you straight what it takes.",
        "cards": [
            ("Wood sheds", "Walls, roof, doors and the floor, taken apart and hauled."),
            ("Metal sheds", "Panels and frame taken down and loaded."),
            ("Plastic and resin sheds", "Broken down and gone in one trip."),
            ("Everything inside", "Old tools, bikes and years of clutter."),
            ("Playhouses and lean-tos", "Small backyard structures, same idea."),
            ("Clean ground left", "Debris picked up so the spot is ready for what is next."),
        ],
        "points": ["The size of the shed and what it is made of", "Whether it has a wood floor or sits on a slab", "What is still inside it", "Disposal for what we haul"],
        "faq": [
            ("Can you empty the shed before you take it down?", "Yes. We can clear out what is inside first, then take the shed down. Tell us what is in there so the quote covers it."),
            ("Do you remove a concrete slab?", "Tell us if the shed sits on a concrete slab and send a photo. We will tell you straight what we can do with it."),
            ("What photos should I send?", "The front of the shed, the inside and the path from the shed to the street. 3 to 5 photos is usually enough."),
            ("How much does shed removal cost?", "It is priced by the job: how big the shed is, what it is made of and what is inside. Send a photo and you get one clear number back."),
        ],
        "reviews": ["carlos", "veljko", "donna"],
    },
    {
        "slug": "deck-removal",
        "name": "Deck Removal",
        "service_type": "Deck removal",
        "title": "Deck Removal &amp; Tear-Out in Northern Virginia | H&amp;M",
        "desc": "Old deck tear-out and removal in Herndon, Reston, Fairfax and Loudoun County. Boards, railings and stairs taken apart and hauled off. Text a photo for a free quote.",
        "eyebrow": "Tear-out and haul-off",
        "lede": "Soft boards, wobbly railings or a deck you are replacing. We tear it out, load the wood and haul it all away.",
        "img": ("/assets/hm-truck.webp", "The H&amp;M truck in Northern Virginia", 1500, 938, "The H&amp;M truck"),
        "includes_h2": "Deck removal, <em>board by board.</em>",
        "includes_lede": "Text a few photos of the deck from the yard and from on top. We will tell you straight what it takes.",
        "cards": [
            ("Deck boards", "Pulled up and stacked into the truck."),
            ("Railings and stairs", "Taken apart and hauled with the rest."),
            ("Small decks and landings", "Back steps and small platforms too."),
            ("Before a new deck", "Clear the spot so your builder can start fresh."),
            ("Old lumber piles", "Leftover wood from a project you already did."),
            ("Hauled off", "Taken away for disposal. Nothing left in the yard."),
        ],
        "points": ["How big the deck is", "How high off the ground it sits", "Railings, stairs and what is under it", "Disposal for what we haul"],
        "faq": [
            ("Do you take out the posts and footings?", "Tell us if you want the posts and footings out too, and send a photo of them. We will tell you straight what is included."),
            ("Can you remove part of a deck?", "Yes. Just the stairs, the railings or one section is fine. Say which parts in your text."),
            ("Can you haul away lumber from a deck I already took down?", "Yes. A pile of old deck wood is a normal haul-away job for us."),
            ("How much does deck removal cost?", "It is priced by the job: the size of the deck, how high it sits and what comes out with it. Send a photo and you get one clear number back."),
        ],
        "reviews": ["carlos", "veljko", "donna"],
    },
    {
        "slug": "construction-debris-removal",
        "name": "Construction Debris Removal",
        "service_type": "Construction debris removal",
        "title": "Construction Debris Removal in Northern Virginia | H&amp;M",
        "desc": "Construction and renovation debris removal in Herndon, Reston, Fairfax and Loudoun County. Lumber, drywall, flooring and leftover project piles. Text a photo for a free quote.",
        "eyebrow": "Renovation leftovers",
        "lede": "The pile left after a remodel, a DIY project or a contractor who didn't haul it. Lumber, drywall, flooring and bags of scrap, loaded and gone.",
        "img": ("/assets/debris-pile-lumber.webp", "A real pile of lumber and bagged debris on an H&amp;M job in Northern Virginia", 1200, 900, "Real H&amp;M job"),
        "includes_h2": "Construction debris removal, <em>without a dumpster.</em>",
        "includes_lede": "Not sure if something is on the list? Text a photo of the pile. We will tell you straight.",
        "cards": [
            ("Lumber and scrap wood", "Boards, framing, pallets and offcuts."),
            ("Drywall and plaster", "Broken pieces, bagged or loose."),
            ("Flooring and carpet", "Old carpet, pad, laminate and tile pieces."),
            ("Cabinets and fixtures", "Old kitchen and bathroom pieces from a remodel."),
            ("Doors and windows", "The old ones that came out."),
            ("Bags and boxes of scrap", "The cleanup pile at the end of the job."),
        ],
        "points": ["How big the pile is", "How heavy the material is", "How far we carry it to the truck", "Disposal for what we haul"],
        "faq": [
            ("Do I need a dumpster?", "Often not. If the pile fits in a truckload or two, we load it and haul it off in one visit, so nothing sits in your driveway."),
            ("Do you work with contractors?", "Yes. Homeowners and contractors both text us photos of the pile and get one price for the haul."),
            ("Is there anything you can't take?", "Ask first about paint, chemicals or anything that could be hazardous. Send a photo and we will tell you straight."),
            ("How much does construction debris removal cost?", "It is priced by the job: how much there is, how heavy it is and how far we carry it. Send a photo and you get one clear number back."),
        ],
        "reviews": ["carlos", "veljko", "donna"],
    },
    {
        "slug": "snow-removal",
        "name": "Snow Removal",
        "service_type": "Snow removal",
        "title": "Snow Removal in Herndon, Reston &amp; Fairfax | H&amp;M",
        "desc": "Driveway, walkway and front step snow removal in Herndon, Reston, Fairfax and Loudoun County. Text us before or after the storm for a free quote.",
        "eyebrow": "Winter help",
        "lede": "Driveways, walkways and front steps cleared after the snow, so you can get out and nobody slips on the way in.",
        "img": ("/assets/crew.webp", "The H&amp;M crew in front of their truck in Northern Virginia", 1448, 1086, "The H&amp;M crew"),
        "includes_h2": "Snow removal, <em>so you can get out.</em>",
        "includes_lede": "Text a photo of your driveway and walkways. We will tell you straight when we can get there.",
        "cards": [
            ("Driveways", "Cleared so you can get the car out."),
            ("Walkways and paths", "From the driveway to the front door."),
            ("Front steps and porches", "The part everyone walks on first."),
            ("Sidewalks", "The stretch in front of your house."),
            ("Rentals and small businesses", "Entrances and walks, not just homes."),
            ("Before company comes", "Walks and steps cleared before family visits."),
        ],
        "points": ["How long and wide the driveway is", "Walkways, steps and sidewalks to clear", "How much snow fell", "How far you are from Herndon"],
        "faq": [
            ("When should I text you?", "Before the storm if you can, so we can plan your job. After the snow is fine too. Send a photo of the driveway either way."),
            ("Do you do just walkways and steps?", "Yes. A small job like the front walk and steps is fine. Say what you want cleared in your text."),
            ("Can you come back after every storm?", "Ask us about it in your text. We will tell you straight what we can do for your street this winter."),
            ("How much does snow removal cost?", "It is priced by the job: the size of the driveway, what else needs clearing and how much snow fell. Send a photo and you get one clear number back."),
        ],
        "reviews": ["michael", "skerdi", "donna"],
    },
]


def raw(s: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def build(p: dict, tpl: str) -> str:
    s = tpl
    name, name_raw = p["name"], raw(p["name"])
    url = f"https://hmjunkland.org/{p['slug']}/"
    old_title = re.search(r"<title>(.*?)</title>", s).group(1)
    old_desc = re.search(r'<meta name="description" content="([^"]*)"', s).group(1)
    s = s.replace(old_title, p["title"]).replace(old_desc, p["desc"])
    s = s.replace("https://hmjunkland.org/furniture-removal/", url)
    s = s.replace('"description": "' + raw(old_desc) + '"', '"description": "' + raw(p["desc"]) + '"')
    s = s.replace('"serviceType": "Furniture removal"', f'"serviceType": "{p["service_type"]}"')
    s = s.replace(f'"name": "{OLD_NAME_RAW}"', f'"name": "{name_raw}"')
    # faq schema gets rebuilt by seo_patch.py
    s = re.sub(r"  <!-- faq-schema -->.*?<!-- /faq-schema -->\n", "", s, flags=re.S)
    # hero
    s = re.sub(r'(<div class="hero-eyebrow"><span class="pulse-dot"></span>).*?(</div>)', rf'\g<1>{p["eyebrow"]}\2', s)
    s = re.sub(r'(<p class="pg-lede">).*?(</p>)', lambda m: m.group(1) + p["lede"] + m.group(2), s)
    src, alt, w, h, cap = p["img"]
    s = re.sub(r'(<figure class="pg-hero-figure" data-reveal>\s*<img [^>]*?)src="[^"]*" alt="[^"]*" width="\d+" height="\d+"',
               lambda m: f'{m.group(1)}src="{src}" alt="{alt}" width="{w}" height="{h}"', s)
    s = re.sub(r'(<figcaption class="pg-tag">).*?(</figcaption>)', lambda m: m.group(1) + cap + m.group(2), s, count=1)
    # includes
    s = s.replace(f"<h2>{OLD_NAME}, <em>done right.</em></h2>", f"<h2>{p['includes_h2']}</h2>")
    s = s.replace("Not sure if it is on the list? Text a photo and ask. We will tell you straight.", p["includes_lede"])
    cards = "\n".join(
        f'        <div class="pg-check-card" data-reveal>\n          <span class="pg-check-ico">{CHECK}</span>\n'
        f"          <h3>{t}</h3>\n          <p>{d}</p>\n        </div>" for t, d in p["cards"])
    s = re.sub(r'(<div class="pg-check-grid">\n).*?(\n      </div>\n    </div>\n  </section>)',
               lambda m: m.group(1) + cards + m.group(2), s, count=1, flags=re.S)
    # pricing
    s = s.replace(f"We quote {OLD_NAME.lower()} by the job", f"We quote {name.lower()} by the job")
    pts = "\n".join(f"            <li>{CHECK}<span>{x}</span></li>" for x in p["points"])
    s = re.sub(r'(<h3>What goes into the price</h3>\n          <ul>\n).*?(\n          </ul>)',
               lambda m: m.group(1) + pts + m.group(2), s, count=1, flags=re.S)
    # faq
    faq = "\n".join(f'        <details class="pg-faq-item">\n          <summary>{q}</summary>\n          <p>{a}</p>\n        </details>'
                    for q, a in p["faq"])
    s = re.sub(r'(<div class="pg-faq" data-reveal>\n).*?(\n      </div>)', lambda m: m.group(1) + faq + m.group(2), s, count=1, flags=re.S)
    # remaining name mentions (breadcrumb, h1, faq head, final CTA, areas head)
    s = s.replace(f"get a price on {OLD_NAME.lower()}", f"get a price on {name.lower()}")
    main_part, foot = s.split('<footer class="site-footer">', 1)
    s = main_part.replace(OLD_NAME, name) + '<footer class="site-footer">' + foot
    body = s.split("<main", 1)[1].split('pg-related-section')[0]
    body = re.sub(r'<div class="rv-grid">.*?<div class="rv-actions"', "", body, flags=re.S)  # cards come from update_reviews.py
    head = s.split("</head>", 1)[0]
    assert "urniture" not in body and "urniture" not in head, p["slug"]
    if re.search(r"[–—]", s):
        raise SystemExit("dash in " + p["slug"])
    return s


FOOTER_ANCHOR = '          <li><a href="/power-washing/">Power Washing</a></li>\n'
FOOTER_LINKS = ('          <li><a href="/hot-tub-removal/">Hot Tubs</a> · <a href="/shed-removal/">Sheds</a>'
                ' · <a href="/deck-removal/">Decks</a></li>\n'
                '          <li><a href="/construction-debris-removal/">Construction Debris</a>'
                ' · <a href="/snow-removal/">Snow Removal</a></li>\n')
DONE = 'href="/snow-removal/">Snow Removal</a></li>'
SKIP = {"_deploy", "_preview", "_backups", "preview-redesign", "chats", "public", "_source_assets", "tools"}


def with_footer(doc: str) -> str:
    if FOOTER_ANCHOR not in doc or DONE in doc:
        return doc
    return doc.replace(FOOTER_ANCHOR, FOOTER_ANCHOR + FOOTER_LINKS, 1)


def add_footer_links() -> None:
    n = 0
    for path in sorted(ROOT.rglob("*.html")):
        if SKIP & set(path.relative_to(ROOT).parts):
            continue
        doc = path.read_text(encoding="utf-8")
        new = with_footer(doc)
        if new != doc:
            path.write_text(new, encoding="utf-8", newline="\n")
            n += 1
    print("footer links added to", n, "pages")


def main() -> None:
    tpl = TEMPLATE.read_text(encoding="utf-8")
    for p in PAGES:
        out = ROOT / p["slug"] / "index.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(with_footer(build(p, tpl)), encoding="utf-8", newline="\n")
        print("wrote", out.relative_to(ROOT))
    add_footer_links()


if __name__ == "__main__":
    main()
