"""Local guide pages (/guides/...). Imported by build_pages.py, which passes itself in as `bp`
so these pages reuse the same head, header, hero, footer and CTA as every other sub-page."""
from guides_data import GUIDES, CHECKED

GUIDE_CSS = """
  <style>
    .pg-guide { max-width: 820px; }
    .pg-guide h2 { margin: 44px 0 14px; font-size: clamp(24px, 3vw, 32px); }
    .pg-guide ul { margin: 0; padding: 0; list-style: none; display: grid; gap: 10px; }
    .pg-guide li { position: relative; padding: 14px 18px 14px 46px; background: #fff; border: 1px solid rgba(31,77,51,.12);
      border-radius: 16px; color: var(--slate-700); font-weight: 500; line-height: 1.6; box-shadow: 0 6px 18px rgba(31,77,51,.06); }
    .pg-guide li::before { content: ""; position: absolute; left: 18px; top: 22px; width: 12px; height: 12px; border-radius: 50%;
      background: var(--orange); box-shadow: 0 0 0 4px rgba(242,122,26,.18); }
    .pg-quick { margin: 0 0 8px; padding: 22px 24px; border-radius: 20px; color: #fff; font-weight: 600; line-height: 1.6; font-size: 18px;
      background: linear-gradient(135deg, #1F4D33, #2c6a47); box-shadow: 0 18px 40px rgba(31,77,51,.25); }
    .pg-quick strong { display: block; color: #FFB25E; font-size: 13px; letter-spacing: .12em; text-transform: uppercase; margin-bottom: 6px; }
    .pg-us { margin-top: 44px; padding: 26px; border-radius: 22px; background: #FFF4E8; border: 1px solid rgba(242,122,26,.35); }
    .pg-us h2 { margin: 0 0 8px; }
    .pg-us p { margin: 0 0 16px; color: var(--slate-700); font-weight: 500; line-height: 1.65; }
    .pg-sources { margin-top: 40px; font-size: 14px; color: #5b6770; }
    .pg-sources ol { margin: 8px 0 0; padding-left: 20px; display: grid; gap: 6px; }
    .pg-sources a { color: #1F4D33; text-decoration: underline; }
    .pg-guide-grid { display: grid; gap: 18px; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }
    .pg-guide-card { display: block; padding: 24px; border-radius: 22px; background: #fff; border: 1px solid rgba(31,77,51,.12);
      box-shadow: 0 10px 26px rgba(31,77,51,.08); text-decoration: none; color: inherit; transition: transform .2s, box-shadow .2s, border-color .2s; }
    .pg-guide-card:hover { transform: translateY(-4px); border-color: var(--orange); box-shadow: 0 18px 40px rgba(31,77,51,.16); }
    .pg-guide-card strong { display: block; font-size: 19px; line-height: 1.3; margin-bottom: 8px; color: #16382a; }
    .pg-guide-card span { display: block; color: var(--slate-700); line-height: 1.55; }
    .pg-guide-card .link-arrow { margin-top: 14px; color: var(--orange); font-weight: 700; }
  </style>"""


def guide_page(bp, g: dict) -> str:
    e = bp.e
    path = f"/guides/{g['slug']}/"
    crumbs = [("Home", "/"), ("Local Guides", "/guides/"), (g["h1"], path)]
    schema = [
        {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": g["title"],
            "description": g["desc"],
            "datePublished": "2026-11-18",
            "dateModified": bp.TODAY,
            "mainEntityOfPage": bp.SITE + path,
            "author": {"@type": "LocalBusiness", "@id": bp.BUSINESS_ID, "name": "H&M Junk Removal & Landscaping", "url": bp.SITE},
            "publisher": {"@type": "LocalBusiness", "@id": bp.BUSINESS_ID, "name": "H&M Junk Removal & Landscaping", "url": bp.SITE},
        },
        bp.breadcrumb_schema(crumbs),
    ]
    body = ""
    for h2, bullets in g["sections"]:
        lis = "\n".join(f"          <li>{e(b)}</li>" for b in bullets)
        body += f"""
        <h2>{e(h2)}</h2>
        <ul>
{lis}
        </ul>"""
    srcs = "\n".join(f'          <li><a href="{u}" rel="noopener" target="_blank">{e(t)}</a></li>' for t, u in g["sources"])
    main = GUIDE_CSS + bp.hero(crumbs=crumbs, eyebrow="Local Guide · Northern Virginia", h1=g["h1"], lede=g["lede"])
    main += f"""

  <section class="section">
    <div class="container pg-guide" data-reveal>
      <p class="pg-quick"><strong>The short answer</strong>{e(g['quick'])}</p>{body}
      <div class="pg-us">
        <h2>Where we come in</h2>
        <p>{e(g['us'])}</p>
        {bp.cta_buttons(light=False)}
      </div>
      <div class="pg-sources">
        <p>Checked against these official pages on {CHECKED}. Rules, hours and fees change, so confirm with the source before you load the car.</p>
        <ol>
{srcs}
        </ol>
      </div>
    </div>
  </section>
"""
    main += bp.related_section("02", g["related"])
    main += bp.final_cta("Rather not deal with it?", "Text us a few photos and your town. We will send one flat price.")
    return bp.page(head_html=bp.head(title=f"{g['title']} | H&M", desc=g["desc"], path=path, schema=schema), main=main)


def guides_index(bp) -> str:
    e = bp.e
    path = "/guides/"
    crumbs = [("Home", "/"), ("Local Guides", path)]
    cards = "\n".join(
        f"""        <a class="pg-guide-card" href="/guides/{g['slug']}/" data-reveal>
          <strong>{e(g['h1'])}</strong>
          <span>{e(g['card'])}</span>
          <span class="link-arrow">Read the guide {bp.ICON['arrow']}</span>
        </a>""" for g in GUIDES)
    main = GUIDE_CSS + bp.hero(crumbs=crumbs, eyebrow="Local Guides", h1="Northern Virginia junk and yard waste guides",
                               lede="Straight answers on bulk pickup, drop-off sites, donations and leaf season in Fairfax and Loudoun counties, checked against the official county and town pages.")
    main += f"""

  <section class="section">
    <div class="container">
      <header class="section-head" data-reveal>
        <div class="kicker"><span class="kicker-num">01</span><span class="kicker-label">Guides</span></div>
        <h2>Know your options <em>before you pay anyone.</em></h2>
        <p class="section-lede">Sometimes the county will take it for free. Sometimes it is a donation. Sometimes you need a truck. These tell you which.</p>
      </header>
      <div class="pg-guide-grid">
{cards}
      </div>
    </div>
  </section>
"""
    main += bp.final_cta("Still stuck with it?", "Text us a few photos and your town. We will send one flat price.")
    return bp.page(head_html=bp.head(
        title="Local Junk Removal and Yard Waste Guides for Northern Virginia | H&M",
        desc="Free local guides for Herndon, Reston, Fairfax, Sterling and Ashburn: county bulk pickup, drop-off sites, furniture donation, mattress and TV disposal, and leaf collection.",
        path=path, schema=[bp.breadcrumb_schema(crumbs)]), main=main)
