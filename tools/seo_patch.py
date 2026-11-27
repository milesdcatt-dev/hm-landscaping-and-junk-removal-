"""SEO patch, Nov 27, 2026. Safe to rerun.

Adds FAQPage JSON-LD to every page that shows a visible FAQ (built from the
visible questions and answers, word for word), and writes /llms.txt for AI
search tools.

Why a patch script: build_pages.py is OLDER than the live pages (later fixes
were applied straight to the HTML and by update_reviews.py), so rerunning it
would undo those fixes. Patch the HTML instead.
"""
import html
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://hmjunkland.org"
PAGES = ["junk-removal", "cleanouts", "furniture-removal", "yard-cleanup", "mulching",
         "power-washing", "student-run-junk-removal", "hot-tub-removal", "shed-removal",
         "deck-removal", "construction-debris-removal", "snow-removal"]
MARK_START = "  <!-- faq-schema -->"
MARK_END = "  <!-- /faq-schema -->"
ITEM = re.compile(r'<details class="pg-faq-item"[^>]*>\s*<summary>(.*?)</summary>\s*<p>(.*?)</p>', re.S)


def text(s: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def faq_block(doc: str) -> str | None:
    qa = [(text(q), text(a)) for q, a in ITEM.findall(doc)]
    if not qa:
        return None
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in qa
        ],
    }
    return (f"{MARK_START}\n  <script type=\"application/ld+json\">\n"
            f"{json.dumps(data, indent=2, ensure_ascii=False)}\n  </script>\n{MARK_END}\n")


def patch_faqs() -> None:
    for slug in PAGES:
        path = ROOT / slug / "index.html"
        doc = path.read_text(encoding="utf-8")
        doc = re.sub(re.escape(MARK_START) + r".*?" + re.escape(MARK_END) + r"\n", "", doc, flags=re.S)
        block = faq_block(doc)
        if not block:
            print("no faq:", slug)
            continue
        doc = doc.replace("</head>", block + "</head>", 1)
        path.write_text(doc, encoding="utf-8", newline="\n")
        print("faq schema:", slug, doc.count('"@type": "Question"'), "questions")


def page_info(rel: str) -> tuple[str, str]:
    doc = (ROOT / rel).read_text(encoding="utf-8")
    t = re.search(r"<title>(.*?)</title>", doc, re.S)
    d = re.search(r'<meta name="description" content="([^"]*)"', doc)
    title = re.split(r" \| ", html.unescape(t.group(1)))[0].strip() if t else rel
    return title, html.unescape(d.group(1)) if d else ""


def write_llms() -> None:
    services = ["junk-removal", "furniture-removal", "cleanouts", "yard-cleanup", "mulching", "power-washing",
                "hot-tub-removal", "shed-removal", "deck-removal", "construction-debris-removal", "snow-removal"]
    guides = sorted(p.parent.name for p in (ROOT / "guides").glob("*/index.html"))
    lines = [
        "# H&M Junk Removal & Landscaping",
        "",
        "> Student-run junk removal and yard work crew based in Herndon, Virginia, serving Fairfax and "
        "Loudoun counties (Herndon, Reston, Vienna, Oakton, Oak Hill, Fairfax, Chantilly, Centreville, "
        "Great Falls, McLean, Sterling, Ashburn). Customers text photos to 202-999-7885 and get one flat "
        "price for the job back by text.",
        "",
        "- Phone and text: 202-999-7885",
        "- Hours: 8 AM to 8 PM, every day",
        "- Owner: Miles Dickey",
        "- Quotes: free, by the job, from photos",
        "- Google reviews: https://maps.google.com/?cid=7233374597949165858",
        "",
        "## Services",
        "",
    ]
    for s in services:
        t, d = page_info(f"{s}/index.html")
        lines.append(f"- [{t}]({SITE}/{s}/): {d}")
    lines += ["", "## About", ""]
    for rel, url in [("student-run-junk-removal/index.html", "/student-run-junk-removal/"),
                     ("service-areas/index.html", "/service-areas/"), ("quote/index.html", "/quote/")]:
        t, d = page_info(rel)
        lines.append(f"- [{t}]({SITE}{url}): {d}")
    lines += ["", "## Local guides", ""]
    for g in guides:
        t, d = page_info(f"guides/{g}/index.html")
        lines.append(f"- [{t}]({SITE}/guides/{g}/): {d}")
    out = "\n".join(lines) + "\n"
    if re.search(r"[–—]", out):
        raise SystemExit("dash in llms.txt")
    (ROOT / "llms.txt").write_text(out, encoding="utf-8", newline="\n")
    print("wrote llms.txt", len(out), "bytes")


if __name__ == "__main__":
    patch_faqs()
    write_llms()
