"""Swap the real Google review cards + count into every page (Nov 27, 2026).
Text is copied word for word from the H&M Google Business Profile."""
import html, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
COUNT = 18
REVIEW_LINK = "https://g.page/r/CSIRGG7fG2JkEBE/review"
R = {
 "laura": ("Laura Thompson", "I hired H & M for leaf cleanup, weeding and mulching, and power washing my stone patio. They did a great job. I have a lot of native plants which look like weeds to most landscapers. Miles walked through my yard to ensure they removed the right plants. I plan to use these hard-working college students in the future and you should too!"),
 "veljko": ("Veljko Gojkovic", "We had new furniture arriving the next day, so we needed to get our old couches removed. I had never hired a junk removal company before, so I contacted a few places and ended up speaking with Miles at H&M Junk Removal.\n\nI explained what we needed, including that we are on the third floor with no elevator. We quickly agreed on a price and scheduled the removal for the next morning.\n\nMiles and his team showed up on time, carried the couches downstairs, and hauled them away. I paid exactly what we agreed on."),
 "susan": ("susan rojas", "I had a great experience with H&M Junkland service! They arrived right on time, were incredibly fast and efficient, and had no problem carrying my sofa down from the second floor to their truck. They were both very nice, polite, and professional throughout the entire process. Everything went smoothly, and I truly appreciate their hard work. I highly recommend their service!"),
 "carlos": ("Carlos Mendez", "I highly recommend Miles for completing hauling and moving tasks. Miles and team were very courteous, efficient and safe while removing and hauling items from my home. Miles is reasonably priced and definitely worth it.\nAs such, I highly recommend Miles for anyone needing help with their hauling needs."),
 "jenny": ("Jenny Marsh", "Great work power washing my house! Professional and super efficient- highly recommend H&M"),
 "liza": ("Liza Paqueo", "These gentlemen are polite, hardworking and excellent. My backyard patio was transformed. It had looked like a junkyard, but now it is immaculate."),
 "patricia": ("Patricia Kirkendall", "I enjoyed having the young men do a job for us. They arrived on time and promptly moved a recliner to the upstairs bedroom.\nPrice was reasonable too!"),
 "michael": ("Michael R", "I couldn't be happier the work. Miles and his team are very professional, meticulous, and hardworking. I will definitely use them again."),
 "skerdi": ("Skerdi Kostreci", "Hard working and very polite young boys. Very impressed! Will definitely hire them again."),
 "donna": ("Donna McKenna", "Great, responsible, and responsive. Reasonable pricing and very professional"),
 "donald": ("Donald Payne", "Great service, nobody better."),
 "goopert": ("Goopert", "Very professional and efficient!"),
 "evan": ("Evan K", "Solid work!"),
}
PAGES = {
 "index.html": ["laura","veljko","susan","carlos","jenny","liza","patricia","michael","skerdi","donna","donald","goopert","evan"],
 "junk-removal/index.html": ["veljko","susan","carlos"],
 "furniture-removal/index.html": ["veljko","susan","patricia"],
 "cleanouts/index.html": ["carlos","veljko","donna"],
 "yard-cleanup/index.html": ["laura","liza","michael"],
 "mulching/index.html": ["laura","liza","michael"],
 "power-washing/index.html": ["jenny","laura","liza"],
 "student-run-junk-removal/index.html": ["laura","skerdi","patricia"],
 "hot-tub-removal/index.html": ["carlos","veljko","donna"],
 "shed-removal/index.html": ["carlos","veljko","donna"],
 "deck-removal/index.html": ["carlos","veljko","donna"],
 "construction-debris-removal/index.html": ["carlos","veljko","donna"],
 "snow-removal/index.html": ["michael","skerdi","donna"],
}
G_ICON = None
def card(name, text):
    body = "<br>".join(html.escape(l, quote=False) for l in text.split("\n"))
    return f"""        <figure class="rv-card" data-reveal>
          <div class="rv-stars" aria-label="5 out of 5 stars">★★★★★</div>
          <blockquote class="rv-quote">{body}</blockquote>
          <figcaption class="rv-who"><span class="rv-av" aria-hidden="true">{html.escape(name[0].upper())}</span><strong>{html.escape(name)}</strong><span>{G_ICON} Google review</span></figcaption>
        </figure>"""
for rel, keys in PAGES.items():
    p = ROOT / rel; s = p.read_text(encoding="utf-8")
    if G_ICON is None:
        G_ICON = re.search(r'<svg viewBox="0 0 24 24" width="14".*?</svg>', s[s.find('rv-card'):], re.S).group(0)
    a = s.find('<div class="rv-grid'); b = s.find('<div class="rv-actions"', a)
    grid_open = '<div class="rv-grid rv-grid--wall">' if rel == "index.html" else '<div class="rv-grid">'
    new_grid = grid_open + "\n" + "\n".join(card(*R[k]) for k in keys) + "\n      </div>\n      "
    s = s[:a] + new_grid + s[b:]
    s, n1 = re.subn(r"5\.0 on Google from \d+ reviews", f"5.0 on Google from {COUNT} reviews", s)
    s, n2 = re.subn(r'(<a class="btn btn-outline" href=")[^"]*(" target="_blank" rel="noopener">Leave us a review</a>)', rf"\g<1>{REVIEW_LINK}\2", s)
    p.write_text(s, encoding="utf-8", newline="\n")
    print(rel, len(keys), n1, n2)
