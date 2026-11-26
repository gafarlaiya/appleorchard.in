#!/usr/bin/env python3
"""applesorchard.in static build: python3 build.py -> dist/. Content: content.py, content2.py (English), content_local.py (Hindi)."""
import html, json, os, shutil, datetime

SITE = "https://applesorchard.in"
ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
WA = "919978791167"
PHONE = "+91 99787 91167"
GTM = "GTM-5R35GWSQ"
TODAY = "2026-11-25"
AUTHOR = {"@type": "Person", "name": "Gafar Laiya", "jobTitle": "Founder, Gujarat Bio Organics",
          "url": "https://www.gujaratbio.com/about"}
ORG = {"@type": "Organization", "@id": SITE + "/#org", "name": "Apple Orchard India (by Gujarat Bio Organics)",
       "url": SITE + "/", "logo": SITE + "/icon.svg",
       "parentOrganization": {"@type": "Organization", "name": "Gujarat Bio Organics Pvt. Ltd.", "url": "https://www.gujaratbio.com/"},
       "sameAs": ["https://www.gujaratbio.com/", "https://b2b.gujaratbio.com/", "https://mangofarming.in/", "https://bananafarming.in/"],
       "telephone": PHONE}

esc = html.escape
PAGES = []   # (path, lastmod, lang)


def wa(text):
    from urllib.parse import quote
    return f"https://wa.me/{WA}?text={quote(text)}"


LEAF = ('<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 10c-3-3-10-3-11 5-1 7 4 14 8 14 1 0 2-1 3-1s2 1 3 1c4 0 9-7 8-14-1-8-8-8-11-5z" fill="#C8323C"/>'
        '<path d="M16 10c0-3 1-5 3-6" stroke="#6B3E1F" stroke-width="2" fill="none" stroke-linecap="round"/><path d="M18 7c3-3 7-2 8 0-3 2-6 2-8 0z" fill="#8FCB9B"/></svg>')

NAV_EN = [("/varieties-and-rootstocks/", "Varieties & rootstocks"), ("/pruning-and-canopy-management/", "Pruning"),
          ("/fertilizer-schedule-and-calculator/", "Fertilizer calculator"), ("/alternate-bearing-and-fruit-quality/", "Fruit drop & size"),
          ("/root-rot-and-tree-mortality/", "Root rot"), ("/diseases-and-pests/", "Diseases & sprays"), ("/harvest-storage-and-profit/", "Harvest & profit")]
NAV_HI = [("/hi/seb-ki-kheti/", "सेब की खेती"), ("/fertilizer-schedule-and-calculator/", "खाद कैलकुलेटर (English)")]
NAV_GU = NAV_HI


def shell(path, title, desc, body, lang="en", schemas=None, crumbs=None, alternates=None, extra_head="", ogtype="article"):
    nav = {"en": NAV_EN, "hi": NAV_HI, "gu": NAV_GU}[lang]
    navh = "".join(f'<a href="{h}"{" aria-current=page" if h == path else ""}>{esc(t)}</a>' for h, t in nav)
    langs = '<nav class="langs" aria-label="Language"><a href="/" lang="en">English</a><a href="/hi/seb-ki-kheti/" lang="hi">हिन्दी</a></nav>'
    crumbh = ""
    sch = list(schemas or [])
    if crumbs:
        crumbh = '<p class="crumb">' + " / ".join(f'<a href="{h}">{esc(t)}</a>' for h, t in crumbs) + f" / {esc(title.split(':')[0].split('|')[0].strip())}</p>"
        items = [{"@type": "ListItem", "position": i + 1, "name": t, "item": SITE + h} for i, (h, t) in enumerate(crumbs)]
        items.append({"@type": "ListItem", "position": len(items) + 1, "name": title.split("|")[0].strip(), "item": SITE + path})
        sch.append({"@type": "BreadcrumbList", "itemListElement": items})
    sch.append(ORG)
    ld = "".join(f'<script type="application/ld+json">{json.dumps(dict({"@context": "https://schema.org"}, **s), ensure_ascii=False)}</script>' for s in sch)
    alt = ""
    for hl, href in (alternates or {}).items():
        alt += f'<link rel="alternate" hreflang="{hl}" href="{SITE}{href}">'
    wa_text = {"en": "Hello, I grow apple. I have a question:", "hi": "नमस्ते, मेरा सेब का बगीचा है। मेरा सवाल है:", "gu": "નમસ્તે, હું કેળાની ખેતી કરું છું. મારો સવાલ છે:"}[lang]
    wa_lbl = {"en": "WhatsApp us", "hi": "WhatsApp करें", "gu": "WhatsApp કરો"}[lang]
    foot = FOOT[lang]
    return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}"><link rel="canonical" href="{SITE}{path}">{alt}
<meta property="og:type" content="{ogtype}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{SITE}{path}"><meta property="og:site_name" content="Apple Orchard India"><meta property="og:locale" content="{ {'en':'en_IN','hi':'hi_IN','gu':'gu_IN'}[lang] }">
<meta property="og:image" content="{SITE}/og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:image" content="{SITE}/og.png">
<meta name="theme-color" content="#F6F3EE"><link rel="icon" href="/icon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;700&family=Young+Serif{'&family=Noto+Sans+Devanagari:wght@400;700' if lang=='hi' else ''}{'&family=Noto+Sans+Gujarati:wght@400;700' if lang=='gu' else ''}&display=optional"><link href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;700&family=Young+Serif{'&family=Noto+Sans+Devanagari:wght@400;700' if lang=='hi' else ''}{'&family=Noto+Sans+Gujarati:wght@400;700' if lang=='gu' else ''}&display=optional" rel="stylesheet" media="print" onload="this.media='all'"><noscript><link href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;700&family=Young+Serif{'&family=Noto+Sans+Devanagari:wght@400;700' if lang=='hi' else ''}{'&family=Noto+Sans+Gujarati:wght@400;700' if lang=='gu' else ''}&display=optional" rel="stylesheet"></noscript>
<link rel="stylesheet" href="/styles.css?v={TODAY}">{extra_head}{ld}
<script>window.dataLayer=window.dataLayer||[];(function(){{var done=false;function load(){{if(done)return;done=true;window.dataLayer.push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var j=document.createElement('script');j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id={GTM}';document.head.appendChild(j);}}['scroll','pointerdown','keydown','touchstart'].forEach(function(e){{window.addEventListener(e,load,{{once:true,passive:true}});}});window.addEventListener('load',function(){{setTimeout(load,4000);}});}})();</script>
</head><body>
<header class="top"><div class="wrap"><a class="brand" href="{'/' if lang=='en' else nav[0][0]}">{LEAF}Apple Orchard India</a><nav class="nav" aria-label="Main">{navh}</nav>{langs}</div></header>
<main class="wrap">{crumbh}{body}</main>
<a class="wa-float" href="{wa(wa_text)}" rel="nofollow">{wa_lbl}</a>
{foot}
</body></html>"""


FOOT = {
    "en": f"""<footer class="foot"><div class="wrap"><div class="grid">
<div><b>Apple Orchard India</b><br>A free apple orchard guide for growers in Himachal Pradesh, Jammu & Kashmir, Uttarakhand and new low-chill areas, built from Dr. YSP UHF Nauni, SKUAST-Kashmir, ICAR-CITH, NHB and government sources. Run by <a href="https://www.gujaratbio.com/">Gujarat Bio Organics Pvt. Ltd.</a>, working with farmers since 2006.</div>
<div><b>Guides</b><br><a href="/">Apple farming guide</a><br><a href="/apple-tree/">The apple tree</a><br><a href="/varieties-and-rootstocks/">Varieties & rootstocks</a><br><a href="/fertilizer-schedule-and-calculator/">Fertilizer calculator</a><br><a href="/root-rot-and-tree-mortality/">Root rot & dying trees</a><br><a href="/diseases-and-pests/spray-schedule/">Spray schedule</a></div>
<div><b>Contact</b><br>WhatsApp / call {PHONE}<br><a href="/about/">About this site</a><br><a href="https://bananafarming.in/">bananafarming.in</a> · <a href="https://mangofarming.in/">mangofarming.in</a> · <a href="https://www.gujaratbio.com/crops/apple">GBO apple page</a></div>
</div><p>Information is general guidance from published university, ICAR and government recommendations. Always follow the product label and your state horticulture department or university spray schedule for pesticide use. Results vary with altitude, soil, weather and care.</p></div></footer>""",
    "hi": f"""<footer class="foot"><div class="wrap"><p><b>Apple Orchard India</b> — गुजरात बायो ऑर्गेनिक्स प्रा. लि. द्वारा (2006 से किसानों के साथ)। WhatsApp / कॉल {PHONE}. जानकारी डॉ. वाई.एस. परमार विश्वविद्यालय नौणी, SKUAST-कश्मीर और ICAR-CITH की सिफारिशों पर आधारित है। दवा का उपयोग लेबल और बागवानी विभाग की स्प्रे सारणी के अनुसार करें।</p></div></footer>""",
}
FOOT["gu"] = FOOT["hi"]


# ------------------------------------------------------------------ small content helpers
def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="tbl-wrap"><table class="tbl"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


def answer(text):
    return f'<div class="answer"><p>{text}</p></div>'


def facts(items):
    return '<div class="facts">' + "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in items) + "</div>"


def faq(qas, lang="en"):
    h = "".join(f"<details><summary>{esc(q)}</summary><p>{a}</p></details>" for q, a in qas)
    import re
    sch = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in qas]}
    title = {"en": "Questions farmers ask", "hi": "किसानों के सवाल", "gu": "ખેડૂતોના સવાલ"}[lang]
    return f"<h2>{title}</h2>{h}", sch


def sources(lst):
    return '<h2>Sources</h2><ol class="src">' + "".join(f"<li>{s}</li>" for s in lst) + "</ol>"


def byline(lang="en"):
    t = {"en": f'By <a href="/about/">Gafar Laiya</a>, Gujarat Bio Organics · Updated {TODAY}',
         "hi": f'लेखक: <a href="/about/">गफ़ार लैया</a>, गुजरात बायो ऑर्गेनिक्स · अपडेट {TODAY}',
         "gu": f'લેખક: <a href="/about/">ગફાર લૈયા</a>, ગુજરાત બાયો ઓર્ગેનિક્સ · અપડેટ {TODAY}'}[lang]
    return f'<p class="byline">{t}</p>'


def cta(lang="en", topic="apple"):
    if lang != "en":
        return f'<section class="cta"><h2>अपने सेब के बगीचे के लिए सलाह चाहिए?</h2><p>पत्तों, तने, जड़ या फल की फ़ोटो, किस्म, उम्र और ऊँचाई के साथ WhatsApp पर भेजें। हमारी टीम बताएगी कि क्या जाँचना है और क्या करना है।</p><div class="btns"><a class="btn btn-wa" href="{wa("नमस्ते, सेब के बगीचे के लिए सलाह चाहिए।")}">WhatsApp पर फ़ोटो भेजें</a><a class="btn btn-line" href="tel:+919978791167">कॉल करें</a></div></section>'
    return (f'<section class="cta"><h2>Trees dying, fruit dropping or staying small?</h2><p>Send photos of the leaves, trunk, roots or fruit on WhatsApp with your variety, rootstock, tree age and altitude. '
            f'Our team replies with what to check and what to do next.</p><div class="btns"><a class="btn btn-wa" href="{wa("Hello, I need advice for my apple orchard. Topic: " + topic)}">Send photos on WhatsApp</a>'
            f'<a class="btn btn-line" href="tel:+919978791167">Call {PHONE}</a></div></section>')


def gbo_box():
    return ('<div class="note"><b>From Gujarat Bio Organics:</b> <a href="https://www.gujaratbio.com/products/immunity-apple-special">Immunity Apple Special</a> is our organic liquid input made for apple orchards, '
            'developed for growers in Himachal Pradesh and Jammu and Kashmir facing tree losses, low production and small, poorly coloured fruit. It is used alongside the fertilizer and spray schedule, not instead of it; '
            f'follow the pack label. <a href="{wa("I want to know about Immunity Apple Special for my apple orchard.")}">Ask on WhatsApp</a> for a schedule for your orchard.</div>')


def article(path, title, desc, h1, body, crumbs=None, qas=None, srcs=None, lang="en", alternates=None, extra_schema=None, headline=None):
    parts = [f"<h1>{h1}</h1>", byline(lang), body]
    sch = [{"@type": "Article", "headline": headline or title.split("|")[0].strip(), "description": desc, "inLanguage": lang,
            "datePublished": TODAY, "dateModified": TODAY, "author": AUTHOR, "publisher": {"@id": SITE + "/#org"},
            "mainEntityOfPage": SITE + path}]
    if qas:
        fh, fs = faq(qas, lang); parts.append(fh); sch.append(fs)
    parts.append(cta(lang, h1))
    if srcs:
        parts.append(sources(srcs))
    sch += extra_schema or []
    write(path, shell(path, title, desc, "\n".join(parts), lang, sch, crumbs or ([("/", "Home")] if path != "/" else None), alternates), lang)


def write(path, html_text, lang="en", sitemap=True):
    out = os.path.join(DIST, path.strip("/"), "index.html") if path.endswith("/") else os.path.join(DIST, path.strip("/"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(html_text)
    if sitemap:
        PAGES.append((path, TODAY, lang))


if __name__ == "__main__":
    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    shutil.copy(os.path.join(ROOT, "src", "styles.css"), DIST)
    shutil.copy(os.path.join(ROOT, "src", "calc.js"), DIST)
    shutil.copy(os.path.join(ROOT, "src", "235bb937b1754b038af67d3b9269d1b8.txt"), DIST)  # IndexNow key
    if os.path.exists(os.path.join(ROOT, "src", "og.png")):
        shutil.copy(os.path.join(ROOT, "src", "og.png"), DIST)
    open(os.path.join(DIST, "icon.svg"), "w").write(LEAF.replace('aria-hidden="true"', 'xmlns="http://www.w3.org/2000/svg"').replace("<svg ", '<svg width="64" height="64" ', 1).replace("<path", '<rect width="32" height="32" rx="7" fill="#1D4A2B"/><path', 1))
    import content, content_local
    content.build(globals())
    content_local.build(globals())
    # 404
    write("/404.html", shell("/404.html", "Page not found | Apple Orchard India", "This page does not exist.",
                             '<h1>This page does not exist</h1><p>Try the <a href="/">apple farming guide</a> or the <a href="/fertilizer-schedule-and-calculator/">fertilizer calculator</a>.</p>'), sitemap=False)
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(
        f"<url><loc>{SITE}{p}</loc><lastmod>{d}</lastmod></url>" for p, d, _ in PAGES) + "</urlset>\n"
    open(os.path.join(DIST, "sitemap.xml"), "w").write(sm)
    open(os.path.join(DIST, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    open(os.path.join(DIST, "_headers"), "w").write("/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n/styles.css\n  Cache-Control: public, max-age=86400\n/calc.js\n  Cache-Control: public, max-age=86400\n")
    content.llms(globals())
    print("built", len(PAGES), "pages")
