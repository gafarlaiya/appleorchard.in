#!/usr/bin/env python3
"""bananafarming.in static build: python3 build.py -> dist/. Content lives in content.py (English) and content_local.py (Hindi, Gujarati)."""
import html, json, os, shutil, datetime

SITE = "https://bananafarming.in"
ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
WA = "919978791167"
PHONE = "+91 99787 91167"
GTM = "GTM-5R35GWSQ"
TODAY = "2026-11-25"
AUTHOR = {"@type": "Person", "name": "Gafar Laiya", "jobTitle": "Founder, Gujarat Bio Organics",
          "url": "https://www.gujaratbio.com/about"}
ORG = {"@type": "Organization", "@id": SITE + "/#org", "name": "Banana Farming India (by Gujarat Bio Organics)",
       "url": SITE + "/", "logo": SITE + "/icon.svg",
       "parentOrganization": {"@type": "Organization", "name": "Gujarat Bio Organics Pvt. Ltd.", "url": "https://www.gujaratbio.com/"},
       "sameAs": ["https://www.gujaratbio.com/", "https://b2b.gujaratbio.com/", "https://mangofarming.in/"],
       "telephone": PHONE}

esc = html.escape
PAGES = []   # (path, lastmod, lang)


def wa(text):
    from urllib.parse import quote
    return f"https://wa.me/{WA}?text={quote(text)}"


LEAF = ('<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 30c0-9 1-16 9-24-9 2-14 8-15 15" fill="none" stroke="#E5B41C" stroke-width="2.6" stroke-linecap="round"/>'
        '<path d="M10 21c-4-3-6-8-5-15 5 3 8 8 9 14" fill="#8FCB9B"/></svg>')

NAV_EN = [("/varieties/", "Varieties"), ("/tissue-culture-and-spacing/", "Planting & spacing"),
          ("/fertilizer-schedule-and-calculator/", "Fertilizer calculator"), ("/deficiencies-and-leaf-yellowing/", "Yellow leaves"),
          ("/diseases-and-pests/", "Diseases & pests"), ("/crop-operations-and-profit/", "Bunch care & profit")]
NAV_HI = [("/hi/kele-ki-kheti/", "केले की खेती"), ("/fertilizer-schedule-and-calculator/", "खाद कैलकुलेटर (English)")]
NAV_GU = [("/gu/kela-ni-kheti/", "કેળાની ખેતી"), ("/fertilizer-schedule-and-calculator/", "ખાતર કેલ્ક્યુલેટર (English)")]


def shell(path, title, desc, body, lang="en", schemas=None, crumbs=None, alternates=None, extra_head="", ogtype="article"):
    nav = {"en": NAV_EN, "hi": NAV_HI, "gu": NAV_GU}[lang]
    navh = "".join(f'<a href="{h}"{" aria-current=page" if h == path else ""}>{esc(t)}</a>' for h, t in nav)
    langs = '<nav class="langs" aria-label="Language"><a href="/" lang="en">English</a><a href="/hi/kele-ki-kheti/" lang="hi">हिन्दी</a><a href="/gu/kela-ni-kheti/" lang="gu">ગુજરાતી</a></nav>'
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
    wa_text = {"en": "Hello, I grow banana. I have a question:", "hi": "नमस्ते, मैं केले की खेती करता हूँ। मेरा सवाल है:", "gu": "નમસ્તે, હું કેળાની ખેતી કરું છું. મારો સવાલ છે:"}[lang]
    wa_lbl = {"en": "WhatsApp us", "hi": "WhatsApp करें", "gu": "WhatsApp કરો"}[lang]
    foot = FOOT[lang]
    return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}"><link rel="canonical" href="{SITE}{path}">{alt}
<meta property="og:type" content="{ogtype}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{SITE}{path}"><meta property="og:site_name" content="Banana Farming India"><meta property="og:locale" content="{ {'en':'en_IN','hi':'hi_IN','gu':'gu_IN'}[lang] }">
<meta name="theme-color" content="#1D4A2B"><link rel="icon" href="/icon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800{'&family=Noto+Sans+Devanagari:wght@400;700' if lang=='hi' else ''}{'&family=Noto+Sans+Gujarati:wght@400;700' if lang=='gu' else ''}&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css?v={TODAY}">{extra_head}{ld}
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s);j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{GTM}');</script>
</head><body>
<header class="top"><div class="wrap"><a class="brand" href="{'/' if lang=='en' else nav[0][0]}">{LEAF}Banana Farming India</a><nav class="nav" aria-label="Main">{navh}</nav>{langs}</div></header>
<main class="wrap">{crumbh}{body}</main>
<a class="wa-float" href="{wa(wa_text)}" rel="nofollow">{wa_lbl}</a>
{foot}
</body></html>"""


FOOT = {
    "en": f"""<footer class="foot"><div class="wrap"><div class="grid">
<div><b>Banana Farming India</b><br>A free banana growing guide for Indian farmers, built from ICAR-NRCB, TNAU, state university and government sources. Run by <a href="https://www.gujaratbio.com/">Gujarat Bio Organics Pvt. Ltd.</a>, Bhavnagar, Gujarat, working with farmers since 2006.</div>
<div><b>Guides</b><br><a href="/">Banana farming guide</a><br><a href="/varieties/">Banana varieties</a><br><a href="/fertilizer-schedule-and-calculator/">Fertilizer schedule & calculator</a><br><a href="/diseases-and-pests/">Diseases & pests</a><br><a href="/crop-operations-and-profit/">Yield, cost & profit</a></div>
<div><b>Contact</b><br>WhatsApp / call {PHONE}<br><a href="/about/">About this site</a><br><a href="https://mangofarming.in/">mangofarming.in</a> · <a href="https://www.gujaratbio.com/crops/banana">GBO banana page</a></div>
</div><p>Information is general guidance from published university and ICAR recommendations. Always follow the product label and your local KVK or state agriculture department for pesticide use. Results vary with soil, weather and care.</p></div></footer>""",
    "hi": f"""<footer class="foot"><div class="wrap"><p><b>Banana Farming India</b> — गुजरात बायो ऑर्गेनिक्स प्रा. लि., भावनगर द्वारा (2006 से किसानों के साथ)। WhatsApp / कॉल {PHONE}. जानकारी ICAR-NRCB, TNAU और राज्य कृषि विश्वविद्यालयों की सिफारिशों पर आधारित है। दवा का उपयोग लेबल और अपने KVK की सलाह के अनुसार करें।</p></div></footer>""",
    "gu": f"""<footer class="foot"><div class="wrap"><p><b>Banana Farming India</b> — ગુજરાત બાયો ઓર્ગેનિક્સ પ્રા. લિ., ભાવનગર (2006 થી ખેડૂતો સાથે). WhatsApp / કૉલ {PHONE}. માહિતી ICAR-NRCB, TNAU અને રાજ્ય કૃષિ યુનિવર્સિટીઓની ભલામણો પરથી છે. દવાનો ઉપયોગ લેબલ અને તમારા KVKની સલાહ મુજબ કરો.</p></div></footer>""",
}


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


def cta(lang="en", topic="banana"):
    if lang == "hi":
        return f'<section class="cta"><h2>अपने केले के खेत के लिए सलाह चाहिए?</h2><p>पत्तों, तने या घौद की फ़ोटो WhatsApp पर भेजें। हमारी टीम जवाब देगी कि क्या जाँचना है और क्या करना है।</p><div class="btns"><a class="btn btn-wa" href="{wa("नमस्ते, केले के खेत के लिए सलाह चाहिए।")}">WhatsApp पर फ़ोटो भेजें</a><a class="btn btn-line" href="tel:+919978791167">कॉल करें</a></div></section>'
    if lang == "gu":
        return f'<section class="cta"><h2>તમારા કેળના ખેતર માટે સલાહ જોઈએ છે?</h2><p>પાન, થડ કે લૂમનો ફોટો WhatsApp પર મોકલો. અમારી ટીમ જણાવશે કે શું તપાસવું અને શું કરવું.</p><div class="btns"><a class="btn btn-wa" href="{wa("નમસ્તે, કેળના ખેતર માટે સલાહ જોઈએ છે.")}">WhatsApp પર ફોટો મોકલો</a><a class="btn btn-line" href="tel:+919978791167">કૉલ કરો</a></div></section>'
    return (f'<section class="cta"><h2>Stuck with a problem in your banana field?</h2><p>Send a photo of the leaves, stem or bunch on WhatsApp with your variety, age and location. '
            f'Our team replies with what to check and what to do next.</p><div class="btns"><a class="btn btn-wa" href="{wa("Hello, I need advice for my banana field. Topic: " + topic)}">Send a photo on WhatsApp</a>'
            f'<a class="btn btn-line" href="tel:+919978791167">Call {PHONE}</a></div></section>')


def gbo_box():
    return ('<div class="note"><b>From Gujarat Bio Organics:</b> <a href="https://www.gujaratbio.com/products/immunity-banana-special">Immunity Banana Special</a> is our organic liquid input made for banana, '
            'developed with growers in Central Gujarat who faced plant losses from wilt and leaf spot. It is used alongside the fertilizer schedule, not instead of it; '
            f'follow the pack label. <a href="{wa("I want to know about Immunity Banana Special for my banana crop.")}">Ask on WhatsApp</a> for a schedule for your field.</div>')


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
    open(os.path.join(DIST, "icon.svg"), "w").write(LEAF.replace('aria-hidden="true"', 'xmlns="http://www.w3.org/2000/svg"').replace("<svg ", '<svg width="64" height="64" ', 1).replace("<path", '<rect width="32" height="32" rx="7" fill="#1D4A2B"/><path', 1))
    import content, content_local
    content.build(globals())
    content_local.build(globals())
    # 404
    write("/404.html", shell("/404.html", "Page not found | Banana Farming India", "This page does not exist.",
                             '<h1>This page does not exist</h1><p>Try the <a href="/">banana farming guide</a> or the <a href="/fertilizer-schedule-and-calculator/">fertilizer calculator</a>.</p>'), sitemap=False)
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(
        f"<url><loc>{SITE}{p}</loc><lastmod>{d}</lastmod></url>" for p, d, _ in PAGES) + "</urlset>\n"
    open(os.path.join(DIST, "sitemap.xml"), "w").write(sm)
    open(os.path.join(DIST, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    open(os.path.join(DIST, "_headers"), "w").write("/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n/styles.css\n  Cache-Control: public, max-age=86400\n/calc.js\n  Cache-Control: public, max-age=86400\n")
    content.llms(globals())
    print("built", len(PAGES), "pages")
