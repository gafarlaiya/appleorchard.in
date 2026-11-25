"""English pages for appleorchard.in, part 1. Every number comes from the research reference (research-reference.md, 25 Nov 2026), which cites
Dr. YSP UHF Nauni, SKUAST-K, SKUAST-J, ICAR-CITH, NHB (incl. Clean Plant Programme), MoA&FW, USDA FAS, NIF, NITI Aayog, DPPQ&S/CIB&RC.
Pesticides: molecule names only, doses 'as per label / university spray schedule' (owner rule)."""

S = {
    "moa": "Ministry of Agriculture & Farmers Welfare: 2023–24 final and 2024–25 second advance estimates (agriwelfare.gov.in)",
    "nhb": "National Horticulture Board: state apple output, harvest and storage standards; Clean Plant Programme 2025 (nhb.gov.in)",
    "usda": "USDA FAS: India apple GAIN report 2024 (apps.fas.usda.gov)",
    "ysp": "Dr. Y.S. Parmar University of Horticulture & Forestry, Nauni: Himachal package of practices, HDP fertigation and thinning trials (yspuniversity.ac.in)",
    "skuastk": "SKUAST-Kashmir and HortiKashmir: spray schedule 2026, replant disease bio-consortia (skuastkashmir.ac.in)",
    "cith": "ICAR–Central Institute of Temperate Horticulture, Srinagar: M.9 high-density models, root rot, scab-resistant cultivars (cith.res.in)",
    "skuastj": "SKUAST-Jammu and ICAR e-course: pollinizer ratios and wound pastes (skuast.org)",
    "ppqs": "DPPQ&S / CIB&RC: apple IPM and pesticides banned in India (ppqs.gov.in)",
    "nif": "National Innovation Foundation: HRMN-99 low-chill apple (nif.org.in)",
    "niti": "NITI Aayog 2026: Himachal apple post-harvest assessment (niti.gov.in)",
    "shc": "ICAR–IISS / Soil Health Card: soil fertility rating brackets (soilhealth.dac.gov.in)",
    "agm": "Agmarknet and eNAM daily mandi prices (agmarknet.gov.in, enam.gov.in)",
    "hp": "Himachal Pradesh Department of Horticulture: package of practices for apple",
    "units": "Land units: Himachal bigha, J&K kanal and Uttarakhand nali conversions",
}
HOME = [("/", "Home")]
VH = HOME + [("/varieties-and-rootstocks/", "Varieties & rootstocks")]


def season():
    ph = [("Dec–Feb", "Dormancy and pruning", "Chilling below 7°C; prune, paste every cut over 2.5 cm, give FYM, phosphorus and potash.", 3, "ph-v"),
          ("Mar–Apr", "Bud break and bloom", "Dormant oil spray, pre-bloom nitrogen, boron at pink bud, beehives in. No sprays at full bloom.", 2, "ph-s"),
          ("May–Jun", "Fruit set and thinning", "Thin to one fruit per cluster at pea size, start calcium sprays, irrigate dry spells.", 2, "ph-b"),
          ("Jul–Oct", "Sizing and harvest", "Next year's buds form now: protect leaves. Harvest by starch-iodine test.", 4, "ph-b"),
          ("Oct–Nov", "Leaf fall reload", "Urea + zinc + boron on green leaves to feed next spring's buds.", 1, "ph-v")]
    months = ["Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"]
    cls = ["ph-v"] * 3 + ["ph-s"] * 2 + ["ph-b"] * 6 + ["ph-v"]
    bar = "".join(f'<span class="{c}">{m}</span>' for m, c in zip(months, cls))
    leg = "".join(f'<div><b>{a}: {b}</b>{c}</div>' for a, b, c, _, _ in ph)
    return (f'<figure class="clock" aria-label="Apple orchard year, December to November"><div class="clock-bar">{bar}</div>'
            f'<div class="clock-legend" style="grid-template-columns:repeat(auto-fit,minmax(170px,1fr))">{leg}</div></figure>')


VAR = {
    "red-delicious": dict(name="Red Delicious and Royal Delicious", short="Red / Royal Delicious", kw="red delicious apple",
        title="Red Delicious & Royal Delicious Apple: Growing in India", h1="Red Delicious and Royal Delicious apple: growing guide for India",
        habit="Standard, vigorous; striped or blushed red", chill="1,000–1,500 hours below 7°C (about 5,500–7,500 ft)", role="Main variety; needs a pollinizer",
        good="The classic Indian apple with the familiar aroma; still the base of most old orchards in Himachal and Kashmir.",
        weak="Severe alternate bearing (heavy one year, little the next) and weak colour at lower altitudes.",
        intro="Royal Delicious and Red Delicious are the standard, vigorous Delicious apples that most traditional Indian orchards are built on. They need 1,000–1,500 chilling hours (about 5,500–7,500 ft) and a compatible pollinizer, and they are prone to severe alternate bearing.",
        extra="<p>Most of the alternate-bearing and small-fruit complaints in old Delicious orchards come from too many fruits in an 'on' year. Thinning to one king fruit per cluster within 10–25 days after petal fall, plus the October urea, zinc and boron spray, are the two steps that break the cycle. See <a href=\"/alternate-bearing-and-fruit-quality/\">alternate bearing and fruit size</a>.</p><p>At lower belts (4,500–6,000 ft) the newer spur and high-colour strains colour better than old Royal Delicious. See <a href=\"/varieties/spur-and-high-colour-strains/\">spur and high-colour strains</a>.</p>"),
    "spur-and-high-colour-strains": dict(name="Spur and high-colour strains (Scarlet Spur-II, Red Chief, Super Chief, Oregon Spur, Jeromine, Red Velox)", short="Spur & high-colour strains", kw="red chief apple",
        title="Red Chief, Super Chief, Scarlet Spur & Jeromine Apple", h1="Spur and high-colour apple strains: Scarlet Spur-II, Red Chief, Super Chief, Oregon Spur, Jeromine",
        habit="Compact spur (Scarlet Spur-II, Red Chief, Super Chief); semi-spur (Oregon Spur, King Roat); standard vigour high-colour (Jeromine, Red Velox, Red Cap Valtod)",
        chill="Spur types 1,000–1,200 hours (4,500–7,500 ft); Oregon Spur 900–1,200; Jeromine and Red Velox 900–1,200 hours (4,500–8,000 ft)", role="Main varieties; all need 25–33% pollinizers",
        good="Dark red colour earlier, even at 4,500–6,000 ft; high pack-out of coloured fruit at lower belts (Jeromine, Red Velox).",
        weak="Spur types give small fruit on M.9 in poor soil; Jeromine and Red Velox turn too dark above about 7,500 ft.",
        intro="Modern Indian high-density blocks plant high-colour Delicious strains: compact spur types (Scarlet Spur-II, Red Chief, Super Chief), semi-spur Oregon Spur and King Roat, and standard-vigour high-colour strains such as Jeromine, Red Velox and Red Cap Valtod. They colour earlier than old Royal Delicious, especially at 4,500–6,000 ft.",
        extra="<p>Choose by altitude and soil. Spur strains suit medium-density blocks on MM.106 or MM.111; on M.9 they need deep, fertile, irrigated soil or the fruit stays small. Jeromine and Red Velox give a high share of coloured fruit in lower belts but can colour too dark above 7,500 ft (Himachal package of practices).</p>"),
    "gala": dict(name="Gala (Gale Gala, Redlum Gala, Gala Venus)", short="Gala", kw="gala apple",
        title="Gala Apple in India: Gale Gala, Redlum Gala, Growing Guide", h1="Gala apple: growing Gale Gala, Redlum Gala and Gala Venus in India",
        habit="Standard; bright early red", chill="700–1,000 hours below 7°C", role="Both a main variety and a pollinizer",
        good="Early harvest in July–August with export-grade fruit; doubles as a pollinizer for Delicious.",
        weak="Fruit is smaller at the highest elevations.",
        intro="Gala strains such as Gale Gala, Redlum Gala and Gala Venus are bright red, early apples harvested in July–August. They need 700–1,000 chilling hours and work both as a main variety and as a pollinizer for Delicious (Himachal package of practices).",
        extra="<p>Because Gala ripens 110–120 days after full bloom, against 130–145 for Delicious, it reaches the market before the main Delicious glut. Redlum Gala is one of the recommended diploid pollinizers, so a Gala row inside a Delicious block does two jobs.</p>"),
    "golden-delicious": dict(name="Golden Delicious", short="Golden Delicious", kw="golden delicious apple",
        title="Golden Delicious Apple: Best Pollinizer for Indian Orchards", h1="Golden Delicious apple: growing guide and pollinizer role",
        habit="Standard or semi-spur; yellow fruit", chill="800–1,100 hours below 7°C", role="Classic pollinizer",
        good="The most reliable pollen donor for Delicious orchards.",
        weak="Alternate bearing if not thinned; russeting (rough skin) in wet weather.",
        intro="Golden Delicious (Reinders) is a yellow apple needing 800–1,100 chilling hours, and the classic pollinizer for Delicious orchards in India. Like Delicious it bears alternately unless the crop is thinned, and wet weather causes skin russeting.",
        extra="<p>Plant 25–33% pollinizers (30–50% in cold, rainy valleys) spread through the block, flowering at the same time as the main variety. Avoid triploid varieties such as Mutsu or Jonagold as pollinizers: their pollen is sterile. See <a href=\"/alternate-bearing-and-fruit-quality/\">fixing poor fruit set</a>.</p>"),
    "granny-smith": dict(name="Granny Smith", short="Granny Smith", kw="granny smith apple",
        title="Granny Smith Apple: Can It Grow in India? Growing Guide", h1="Granny Smith apple: growing it in Indian orchards",
        habit="Vigorous; green fruit", chill="700–1,000 hours below 7°C; long season", role="Pollinizer and commercial variety",
        good="Green, tart apple with a separate market; useful pollinizer for Delicious.",
        weak="Needs a long frost-free autumn (October–November) to mature properly.",
        intro="Granny Smith is a vigorous green apple needing 700–1,000 chilling hours and a long frost-free autumn into October–November to mature. In Indian orchards it is planted both for its own market and as a pollinizer for Delicious (Himachal package of practices).",
        extra="<p>Plant Granny Smith only where autumn frost comes late. At higher, colder sites it may not ripen before frost. Its vigour suits wider spacing on MM.111 or MM.106 rather than poor soil on M.9.</p>"),
    "fuji": dict(name="Fuji (Sun Fuji)", short="Fuji", kw="fuji apple",
        title="Fuji Apple in India: Sun Fuji Growing & Storage Guide", h1="Fuji apple: growing Sun Fuji in India",
        habit="Vigorous; pink-red fruit", chill="700–1,000 hours below 7°C; long season", role="Pollinizer and commercial variety",
        good="Long storage life and a sweet, crisp apple that sells against imported Fuji.",
        weak="Long season: needs a frost-free autumn to ripen.",
        intro="Fuji, grown in India mainly as Sun Fuji, is a vigorous pink-red apple that needs 700–1,000 chilling hours and a long season. It stores for a long time and also serves as a pollinizer for Delicious (Himachal package of practices).",
        extra="<p>India imports 544,000–600,000 tonnes of apples a year, including large volumes of uniform Fuji-type fruit (USDA FAS 2024). Clean, well-coloured domestic Fuji above 70 mm, stored well, competes directly with that fruit.</p>"),
    "ambri": dict(name="Ambri, Shireen and Firdous", short="Ambri", kw="ambri apple",
        title="Ambri Apple of Kashmir, Shireen & Firdous: Variety Guide", h1="Ambri apple of Kashmir, and SKUAST-K's Shireen and Firdous",
        habit="Heritage Kashmiri apple (Ambri); scab-resistant releases (Shireen, Firdous)", chill="Temperate Kashmir", role="Main varieties",
        good="Ambri keeps very long in storage; Shireen and Firdous were bred for resistance to apple scab.",
        weak="Ambri is slow to come into bearing.",
        intro="Ambri is Kashmir's heritage apple, known for its very long storage life but slow to start bearing. SKUAST-Kashmir and ICAR-CITH released Shireen and Firdous as scab-resistant varieties for the Valley.",
        extra="<p>Apple scab is one of the main reasons Kashmir growers spray so often. A November 2026 survey found Kashmir growers spending Rs 97,360–1,09,870 per hectare on pesticides, with only about a quarter following the SKUAST-K schedule. Scab-resistant varieties such as Shireen and Firdous cut that pressure. See <a href=\"/diseases-and-pests/apple-scab/\">apple scab</a>.</p>"),
    "low-chill-hrmn-99-anna": dict(name="Low-chill apples: HRMN-99, Anna and Dorsett Golden", short="HRMN-99, Anna (low chill)", kw="hrmn 99 apple",
        title="HRMN-99 & Anna Apple: Low-Chill Apples for Warm Areas", h1="Low-chill apples: HRMN-99, Anna and Dorsett Golden",
        habit="Low-chill", chill="250–500 hours below 7°C (HRMN-99 300–500); 400–1,400 m and warm valleys", role="HRMN-99 is self-fertile; Anna and Dorsett Golden need cross-pollination",
        good="Fruit where standard apples get too little winter cold; early June ripening for fresh local markets.",
        weak="Short shelf life of 10–12 days; not a storage apple.",
        intro="HRMN-99 (promoted by the National Innovation Foundation), Anna and Dorsett Golden are low-chill apples needing only 250–500 hours below 7°C, so they fruit in warm valleys at 400–1,400 m where Delicious cannot. They ripen early, in June, but keep only 10–12 days.",
        extra="<p>HRMN-99 is self-fertile; Anna and Dorsett Golden must be planted together to pollinate each other. Because the fruit keeps only 10–12 days, plan to sell fresh in nearby markets. Before planting in a new area, check how many hours your winter actually spends below 7°C, and ask your state horticulture department or KVK about local trial results.</p>"),
}


def build(g):
    article, table, answer, facts, gbo_box = g["article"], g["table"], g["answer"], g["facts"], g["gbo_box"]

    # ---------------------------------------------------------------- pillar
    body = f"""<p class="lede">A practical orchard guide for Himachal Pradesh, Jammu & Kashmir, Uttarakhand and new low-chill areas: varieties and rootstocks, pollination, pruning, a fertilizer calculator for bigha, kanal and nali, fixing fruit drop and small fruit, saving dying trees, sprays, harvest and profit.</p>
{season()}
{answer("<b>Apple farming in India in short:</b> plant virus-indexed trees on a rootstock that suits your soil (never MM.106 in heavy clay), with 25–33% compatible pollinizers and 4–6 beehives per hectare at bloom. Standard Delicious needs 800–1,500 chilling hours below 7°C (about 1,500–2,700 m). Feed by tree age (Dr. YSP UHF: 70:35:70 g N:P₂O₅:K₂O per year of age, full 700:350:700 g from year 10), thin fruit at pea size, seal pruning cuts and keep water away from the trunk. Seedling orchards average 6–11 t/ha; clonal high-density orchards reach 30–45 t/ha and more.")}
{facts([("2.69 million t", "India's apple output, 2024–25 (MoA&FW)"), ("about 70%", "grown in Jammu & Kashmir"), ("6–11 t/ha", "average of traditional orchards"), ("30–45+ t/ha", "clonal high-density orchards (ICAR-CITH)"), ("25–33%", "pollinizer trees needed in a block")])}
<div class="grid">
<a class="card" href="/fertilizer-schedule-and-calculator/"><span class="tag">Free tool</span><h3>Fertilizer calculator</h3><p>Dose by tree age for bigha, kanal, nali or acre, standard or M.9 high density.</p></a>
<a class="card" href="/root-rot-and-tree-mortality/"><h3>Trees drying and dying?</h3><p>White root rot, collar rot and replant disease: how to tell them apart and save trees.</p></a>
<a class="card" href="/alternate-bearing-and-fruit-quality/"><h3>Fruit drop and small apples</h3><p>Pollination, thinning, calcium and the October spray that breaks alternate bearing.</p></a>
<a class="card" href="/diseases-and-pests/spray-schedule/"><h3>Apple spray schedule</h3><p>Stage-wise sprays from dormancy to leaf fall, and why calendar spraying backfires.</p></a>
</div>

<h2>Apple in India at a glance</h2>
<p>India is the world's fifth-largest apple producer: about 297 thousand hectares and 2.69 million tonnes in 2024–25 (MoA&FW second advance estimates; USDA FAS forecasts 2.55 million tonnes). Jammu & Kashmir grows about 70%, Himachal Pradesh about 20–26%, Uttarakhand about 3%, with smaller areas in Arunachal Pradesh and the North-East.</p>
{table(["State (2021–22, NHB)", "Production ('000 t)", "Share"], [["Jammu & Kashmir", "1,719", "70.5%"], ["Himachal Pradesh", "644", "26.4%"], ["Uttarakhand", "65", "2.7%"], ["Arunachal Pradesh", "7.3", "0.3%"], ["Nagaland", "1.8", "0.1%"]])}
<p>Traditional seedling orchards average only 6–11 t/ha, against 30–45 t/ha and more in clonal high-density orchards (ICAR-CITH). Nearly 30% of Himachal's harvest is lost or downgraded after picking (NITI Aayog 2026), and 544,000–600,000 tonnes of imported apples a year press prices for small, poorly coloured Delicious (USDA FAS 2024). The money is in clean, well-coloured fruit above 70 mm.</p>

<h2>Climate, chilling hours and site</h2>
<p>Standard Delicious apples need 800–1,500 hours below 7°C (chilling hours), roughly 1,500–2,700 m altitude, 1,000–1,250 mm of rain and frost-free weather at bloom: below −2°C the flowers' pistils die (NHB, Himachal package of practices). In lower belts (4,000–6,500 ft) choose north or north-east slopes, which avoid winter sunscald, and high-colour strains; in high belts (6,500–8,000 ft and above) use south-east slopes. Warm valleys at 400–1,400 m can grow <a href="/varieties/low-chill-hrmn-99-anna/">low-chill HRMN-99, Anna or Dorsett Golden</a>. Anti-hail nets prevent hail damage and soften summer sunscald.</p>

<h2>Soil</h2>
<p>Apple needs deep, well-drained loam with pH 5.5–6.8 and organic carbon above 1.0%. Waterlogging in the June–September monsoon is the main trigger of white root rot, and wet clay kills MM.106 trees through collar rot. Below pH 5.5, use CAN or lime/dolomite rather than ammonium sulphate. <a href="/root-rot-and-tree-mortality/">Root rot and dying trees →</a></p>

<h2>Varieties, rootstocks and pollination</h2>
<p>Old orchards are mostly Royal or Red Delicious on seedling rootstock. New blocks use high-colour strains (Scarlet Spur-II, Red Chief, Super Chief, Oregon Spur, Jeromine, Red Velox) and Gala on clonal rootstocks (M.9, MM.106, MM.111, M.7), which bear in 2–3 years instead of 6–8. Every block needs 25–33% diploid pollinizers (Golden Delicious, Granny Smith, Redlum Gala, Fuji or Manchurian crabapple) flowering at the same time. <a href="/varieties-and-rootstocks/">Varieties and rootstocks →</a></p>

<h2>Spacing and trees per acre</h2>
{table(["System", "Rootstock and training", "Spacing (m)", "Trees/ha", "Trees/acre"], [["Traditional", "Seedling, open or modified leader", "7.5 × 7.5 to 8 × 8", "156–178", "63–72"], ["Standard square", "Seedling or MM.111, modified leader", "5 × 5 to 6 × 6", "278–400", "112–162"], ["Medium density", "MM.106, MM.111, M.7, spindle bush", "3 × 3 to 4 × 4", "625–1,111", "253–450"], ["High density, vertical axis", "M.9 on trellis with drip", "3.0 × 1.5", "2,222", "899"], ["High density, tall spindle", "M.9 / T337 on trellis with drip", "3.0 × 1.0 (3.5 × 1.0)", "3,333 (2,857)", "1,349 (1,156)"]])}
<p><b>Hill land units:</b> 1 acre = 5 Himachal bighas (809.37 m² each) = 8 J&K kanals (505.86 m² each) = 20.16 Uttarakhand nalis (200.67 m² each). A 6 × 6 m orchard holds about 22 trees per Himachal bigha.</p>

<h2>Pruning</h2>
<p>Heavy heading cuts, shaded lower branches, narrow forks and unsealed stubs cause upright non-fruiting shoots, canker dieback, weak buds and alternate bearing. Use thinning cuts, remove limbs thicker than half the trunk with angled renewal cuts, bend branches to 45–60°, and paste every cut over 2.5 cm at once with copper oxychloride or Bordeaux paste. <a href="/pruning-and-canopy-management/">Pruning guide →</a></p>

<h2>Irrigation</h2>
<p>Even with 1,000–1,250 mm of rain, dry spells in May–June (cell division) and August–September (fruit sizing) shrink fruit and trigger bitter pit. On M.9 drip, give about 2–4 L per tree per day in early spring, 6–10 L in May–June and 10–15 L or more in July–August; drip saves 40–50% water (ICAR-CITH, SKUAST-K). A 10–15 cm organic mulch ring, kept 30 cm away from the trunk, cuts evaporation by over 30% and reduces collar rot from soil splash. Dry-then-flooded irrigation cracks fruit.</p>

<h2>Fertilizer in one paragraph</h2>
<p>Standard trees get 70 g N, 35 g P₂O₅, 70 g K₂O and 10 kg FYM per year of age until year 10; bearing trees take 700 : 350 : 700 g plus 70–100 kg FYM (Dr. YSP UHF, SKUAST-K). M.9 high-density trees get half that per year of age up to year 7, through weekly drip. FYM, all phosphorus and half the potash go in November–December; 60% of nitrogen 2–3 weeks before bud break; the rest after petal fall, and less of it in an off year. <a href="/fertilizer-schedule-and-calculator/">Calculate your orchard's dose →</a></p>
{gbo_box()}

<h2>The orchard year</h2>
{table(["Month", "Main work"], [["Dec–Feb", "Dormant pruning (thin out limbs over half trunk size), paste cuts over 2.5 cm, clear drainage ditches, FYM + phosphorus + potash"], ["Mar", "Dormant horticultural mineral oil (2%) above 4°C and 14–21 days apart from sulphur; pre-bloom nitrogen (50–67%)"], ["Apr", "Boron at pink bud (0.1–0.15%); 4–6 beehives per hectare; no sprays at full bloom"], ["May", "Thin fruit 10–25 days after petal fall; start 4–6 calcium chloride sprays; reduce nitrogen in an off year"], ["Jun–Aug", "Irrigate dry spells; summer pruning of water sprouts; watch root rot, Marssonina and mites in the monsoon"], ["Aug–Oct", "Stop sprays 3–4 weeks before picking; NAA against pre-harvest drop if needed; harvest by starch-iodine test"], ["Oct–Nov", "3–5% urea + 0.5% zinc sulphate + 0.1–0.2% boron on green leaves; copper clean-up"]])}

<h2>Main problems by state</h2>
<ul><li><b>Jammu & Kashmir:</b> overspending on pesticides, Marssonina and Alternaria leaf fall, white root rot, and the codling moth quarantine in Ladakh (SKUAST-K).</li>
<li><b>Himachal Pradesh:</b> falling chill below 1,200 m, May–June drought, replant disease in old blocks, hail and about 30% post-harvest loss (Dr. YSP UHF, NITI Aayog 2026).</li>
<li><b>Uttarakhand:</b> small hill holdings, canker and dieback from unsealed pruning cuts, root rot and cold-chain gaps.</li>
<li><b>Arunachal Pradesh and low-chill areas:</b> high monsoon humidity, very acidic soils (pH below 5.2) needing lime and boron, and access to clean nursery plants.</li></ul>"""
    qas = [("How much chilling does an apple tree need?", "Standard Delicious apples need 800–1,500 hours below 7°C; Gala, Granny Smith and Fuji 700–1,000; low-chill HRMN-99, Anna and Dorsett Golden only 250–500."),
           ("How many apple trees are planted per acre?", "63–72 in traditional seedling orchards, 112–162 at 5–6 m, 253–450 in medium density on MM.106 or MM.111, and 899–1,349 in M.9 high density."),
           ("How long does an apple tree take to bear fruit?", "Seedling rootstocks take 6–8 years; clonal rootstocks such as M.9 and MM.106 bear in 2–3 years."),
           ("What is the yield of apple per hectare in India?", "Traditional orchards average 6–11 t/ha; clonal high-density orchards reach 30–45 t/ha and more by year 5 (ICAR-CITH)."),
           ("Why are my apple trees drying?", "Most often white root rot in wet monsoon soil, collar rot on MM.106 in clay, canker from unsealed pruning cuts, or replant disease. <a href=\"/root-rot-and-tree-mortality/\">See how to tell them apart</a>."),
           ("Why do apple flowers drop without fruit?", "Too few compatible pollinizers, too few bees, cold or rain at bloom, boron shortage or spraying during bloom. Plant 25–33% pollinizers and keep 4–6 beehives per hectare."),
           ("Which states grow apple in India?", "Jammu & Kashmir (about 70%), Himachal Pradesh (about 20–26%) and Uttarakhand (about 3%), with smaller areas in Arunachal Pradesh and the North-East."),
           ("How many kanals or bighas are in an acre?", "1 acre = 5 Himachal bighas = 8 J&K kanals = 20.16 Uttarakhand nalis.")]
    article("/", "Apple Farming in India: Orchard Guide & Annual Calendar", "Apple farming in India: varieties, rootstocks, pollinizers, spacing, pruning, fertilizer calculator for bigha and kanal, root rot, sprays and profit.",
            "Apple farming in India: the orchard guide", body, crumbs=[], qas=qas, srcs=[S[k] for k in ("moa", "nhb", "usda", "ysp", "skuastk", "cith", "skuastj", "niti", "units")],
            alternates={"en": "/", "hi": "/hi/seb-ki-kheti/", "x-default": "/"})

    # ---------------------------------------------------------------- apple tree
    body = f"""{answer("An apple tree (<i>Malus × domestica</i>) is a deciduous temperate fruit tree. Commercial trees are grafted: the variety (such as Royal Delicious or Gala) is joined onto a rootstock that decides the tree's size and how soon it bears. Seedling rootstock trees bear after 6–8 years; dwarfing clonal rootstocks such as M.9 or MM.106 bear in 2–3 years (SKUAST-J, ICAR-CITH).")}
<h2>How an apple tree grows through the year</h2>
{season()}
<p>The tree needs winter cold (chilling hours below 7°C) to break dormancy evenly. Flower buds for next year form in June–August, while this year's fruit is sizing. That is why healthy summer leaves and the October urea-zinc-boron spray decide next year's crop.</p>
{table(["Stage", "When", "What to do"], [["Dormancy", "Dec–Feb", "Chilling below 7°C; winter pruning"], ["Silver tip", "Feb–Mar", "Horticultural mineral oil 2% against scale and mite eggs"], ["Green tip", "Mar", "Start watching for scab"], ["Tight cluster / pink bud", "Mar–Apr", "Boron spray"], ["Full bloom", "Apr", "No sprays at all; bees at work"], ["Petal fall", "Apr–May", "Post-bloom nitrogen if fruit set is heavy"], ["Pea (8–12 mm) and walnut size", "May–Jun", "Fruit thinning; start calcium sprays"], ["Summer sizing and bud formation", "Jun–Aug", "Protect the leaves; irrigate dry spells"], ["Harvest", "Jul–Oct", "Pick by starch-iodine test and firmness"], ["Leaf fall", "Oct–Nov", "Urea + zinc + boron reload spray"]])}
<h2>How to plant an apple tree</h2>
<ol><li><b>Buy clean, virus-indexed plants.</b> Mosaic and stem pitting viruses silently stunt young orchards; NHB's Clean Plant Programme is indexing 535 apple samples across J&K, Himachal and Uttarakhand.</li>
<li><b>Match the rootstock to the soil</b>: M.9 only in deep, fertile, irrigated soil with a trellis; MM.106 only in well-drained, non-clay soil; MM.111 for drier, shallower hill soil. <a href="/varieties/rootstocks/">Rootstock guide</a>.</li>
<li><b>Never replant straight into an old apple pit.</b> Shift pits to the old alleyways or treat for replant disease first (solarise or fallow, virgin topsoil, FYM, VAM, Trichoderma and Pseudomonas).</li>
<li><b>Keep the graft union 15–20 cm above the soil</b> to avoid collar rot, and plant on a slight mound where soil stays wet.</li>
<li><b>Plant 25–33% pollinizers</b> spread through the block.</li>
<li><b>Mulch</b> a 10–15 cm ring, kept 30 cm away from the trunk.</li></ol>
<h2>Apple tree care through the year</h2>
<p>Prune in winter and paste every cut over 2.5 cm; feed by age in two or three splits; thin fruit at pea size; give 4–6 calcium sprays; irrigate in May–June and August–September dry spells; keep monsoon water off the trunk; and spray only by a university schedule. <a href="/">Full orchard guide</a> · <a href="/fertilizer-schedule-and-calculator/">fertilizer calculator</a>.</p>
<h2>Why apple leaves turn yellow</h2>
<ul><li><b>Mottled, early-dropping leaves in July–August:</b> often Marssonina blotch (<a href="/diseases-and-pests/">diseases</a>).</li><li><b>Bronze, silvery leaves in summer:</b> European red mite; check with a 10× lens for red eggs.</li><li><b>Yellowing between the veins of older leaves, early drop:</b> magnesium; 1–2% magnesium sulphate at walnut stage.</li><li><b>Small, crowded leaves in rosettes:</b> zinc (little leaf); 0.5% zinc sulphate + 0.25% lime.</li><li><b>Sparse, small yellow leaves on the whole tree:</b> check the roots for <a href="/root-rot-and-tree-mortality/">root rot</a>.</li></ul>"""
    qas = [("How long does an apple tree take to grow fruit?", "6–8 years on seedling rootstock; 2–3 years on clonal rootstocks such as M.9 or MM.106."),
           ("Can I grow an apple tree from seed?", "A seedling grows into a tree, but its fruit will not match the parent. Commercial trees are grafted onto rootstocks."),
           ("When is the best time to plant apple trees?", "During winter dormancy, before bud break, so roots settle before spring growth (Himachal and Kashmir orchards plant in the dormant season)."),
           ("Why is my apple tree not fruiting?", "Too few pollinizers or bees, too little winter chill for the variety, heavy pruning that removes fruiting spurs, an off year after a heavy crop, or too much nitrogen pushing shoots.")]
    article("/apple-tree/", "Apple Tree: Growth Stages, Planting & Care in India", "The apple tree explained for Indian growers: growth stages through the year, how to plant, rootstocks, pollinizers, care and why leaves turn yellow.",
            "The apple tree: growth stages, planting and care", body, crumbs=HOME, qas=qas, srcs=[S["skuastj"], S["cith"], S["nhb"], S["skuastk"], S["hp"]])

    # ---------------------------------------------------------------- varieties and rootstocks hub
    cards = "".join(f'<a class="card" href="/varieties/{k}/"><h3>{v["short"]}</h3><p>{v["chill"].split(";")[0]}</p></a>' for k, v in VAR.items())
    rows = [[f'<a href="/varieties/{k}/">{v["short"]}</a>', v["habit"].split(";")[0], v["chill"].split(";")[0].split(" (")[0], v["role"]] for k, v in VAR.items()]
    body = f"""{answer("Old Indian orchards rely on Royal and Red Delicious. New high-density blocks plant high-colour strains (Scarlet Spur-II, Red Chief, Super Chief, Oregon Spur, Jeromine, Red Velox) and Gala, always with 25–33% compatible diploid pollinizers such as Golden Delicious, Granny Smith, Redlum Gala, Fuji or Manchurian crabapple. Warm valleys use low-chill HRMN-99, Anna or Dorsett Golden (Himachal package of practices, SKUAST-J, NIF).")}
<div class="grid">{cards}<a class="card" href="/varieties/rootstocks/"><span class="tag">Rootstocks</span><h3>M.9, MM.106, MM.111, M.7</h3><p>Which rootstock for which soil</p></a></div>
<h2>Apple varieties in India compared</h2>
{table(["Variety", "Habit", "Chilling below 7°C", "Role"], rows)}
<p class="src">Sources: Himachal Pradesh package of practices, SKUAST-K, ICAR-CITH, NIF.</p>
<h2>Pollinizers: the most common cause of poor fruit set</h2>
<p>Delicious apples cannot set fruit with their own pollen. Plant 25–33% diploid pollinizers (30–50% in cold or rainy valleys) that flower at the same time: Golden Delicious, Granny Smith, Redlum Gala, Fuji, or flowering crabapples such as Manchurian or Snowdrift. Avoid triploids such as Mutsu and Jonagold, whose pollen is sterile. Place 4–6 beehives per hectare (2–3 per acre) at 10–15% bloom, clear flowering mustard weeds that pull bees away, and never spray at full bloom (SKUAST-J, HortiKashmir).</p>
<h2>Rootstocks in one table</h2>
{table(["Rootstock", "Vigour", "Best soil", "Watch out", "Spacing"], [["Seedling (<i>M. baccata</i>)", "100%", "Steep, unirrigated slopes", "Bears in 6–8 years; uneven; woolly aphid", "7.5 × 7.5–8 × 8 m"], ["MM.111", "70–80%", "Drought-prone, lighter, shallow hill soil", "Woolly aphid resistant", "4 × 4–4.5 × 4.5 m"], ["M.7", "55–65%", "Sloping land, moderate moisture", "Suckers; woolly aphid prone", "3.5 × 3.5–4 × 4 m"], ["MM.106", "60–75%", "Well-drained loam, never clay", "Highly susceptible to collar rot in wet or clay soil", "3 × 3 m"], ["M.9 / T337", "30–40%", "Deep, fertile, irrigated flat or terraced land", "Shallow brittle roots; needs trellis and drip", "3.0 × 1.0–1.5 m"]])}
<p><a href="/varieties/rootstocks/">Full rootstock guide, including Geneva rootstocks for replant land →</a></p>"""
    qas = [("Which apple variety is best in India?", "It depends on altitude: Royal Delicious and spur strains at 5,500–7,500 ft, high-colour strains such as Jeromine and Red Velox at lower belts, Gala for early markets, and low-chill HRMN-99 or Anna in warm valleys."),
           ("Which variety is the best pollinizer for Royal Delicious?", "Golden Delicious is the classic choice; Granny Smith, Redlum Gala, Fuji and Manchurian crabapple also work. Plant 25–33% of trees as pollinizers."),
           ("Which apple can grow in warm areas?", "Low-chill HRMN-99, Anna and Dorsett Golden need only 250–500 chilling hours. HRMN-99 is self-fertile; Anna and Dorsett Golden need each other."),
           ("Which rootstock is best for apple?", "M.9 for deep, fertile, irrigated land with trellis; MM.106 for well-drained non-clay soil; MM.111 for drier, shallow hill soil; seedling for steep, unirrigated slopes.")]
    article("/varieties-and-rootstocks/", "Apple Varieties & Rootstocks in India (+ Pollinizer Guide)", "Apple varieties in India compared: Royal Delicious, spur strains, Gala, Golden Delicious, Granny Smith, Fuji, Ambri, HRMN-99, pollinizers and rootstocks.",
            "Apple varieties and rootstocks in India", body, crumbs=HOME, qas=qas, srcs=[S["hp"], S["skuastj"], S["skuastk"], S["cith"], S["nif"]],
            extra_schema=[{"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": g["SITE"] + f"/varieties/{k}/", "name": VAR[k]["short"]} for i, k in enumerate(VAR)]}])

    for k, v in VAR.items():
        body = f"""{answer(v["intro"])}
{table(["", v["short"]], [["Tree habit and fruit", v["habit"]], ["Chilling need", v["chill"]], ["Role in the orchard", v["role"]], ["Strengths", v["good"]], ["Weaknesses", v["weak"]]])}
{v["extra"]}
<h2>Rootstock, spacing and feeding</h2>
<p>Choose the rootstock by soil, not by variety alone: M.9 only on deep, fertile, irrigated land with a trellis; MM.106 only on well-drained soil; MM.111 on drier slopes (<a href="/varieties/rootstocks/">rootstock guide</a>). Feed by tree age with our <a href="/fertilizer-schedule-and-calculator/">apple fertilizer calculator</a>.</p>
<h2>Pollination</h2>
<p>Keep 25–33% compatible pollinizers flowering at the same time, 4–6 beehives per hectare at bloom, a boron spray at pink bud, and no sprays during full bloom.</p>
<p>Compare: <a href="/varieties-and-rootstocks/">all apple varieties and rootstocks</a>.</p>"""
        qas = [(f"How much chilling does {v['short']} need?", v["chill"] + "."), (f"Does {v['short']} need a pollinizer?", v["role"] + "."), (f"What are the problems with {v['short']}?", v["weak"])]
        article(f"/varieties/{k}/", v["title"], (v["intro"][:150].rsplit(" ", 1)[0] + "…") if len(v["intro"]) > 155 else v["intro"],
                v["h1"], body, crumbs=VH, qas=qas, srcs=[S["hp"], S["skuastk"], S["skuastj"], S["cith"]] + ([S["nif"]] if "low" in k else []) + ([S["usda"]] if k == "fuji" else []))

    # ---------------------------------------------------------------- rootstocks
    body = f"""{answer("Pick the rootstock for your soil and water first. M.9 (30–40% vigour) bears in 2–3 years and resists collar rot, but needs deep, fertile, irrigated soil, a 3–4 wire trellis and drip. MM.106 resists woolly aphid and bears early, but is highly susceptible to collar rot in wet or clay soil. MM.111 suits drier, shallower hill soil. Seedling rootstock anchors well on steep unirrigated slopes but takes 6–8 years to bear (Himachal package of practices, ICAR-CITH).")}
{table(["Rootstock", "Vigour", "Soil and drainage", "Strengths and weaknesses", "Support and spacing"], [
 ["Seedling (<i>Malus baccata</i>)", "100% (standard)", "Deep anchorage; steep, unirrigated slopes", "Slow to bear (6–8 years); uneven vigour; woolly aphid susceptible", "No trellis; 7.5 × 7.5–8 × 8 m (156–178 per ha)"],
 ["MM.111 / EMLA-111", "about 70–80%", "Best for drought-prone, lighter, shallow hill soil", "Woolly aphid resistant; tolerates drier slopes than MM.106", "Light or no staking; 4 × 4–4.5 × 4.5 m (494–625 per ha)"],
 ["M.7 / EMLA-7", "about 55–65%", "Sloping land, moderate moisture", "Moderate collar rot tolerance; suckers; woolly aphid prone", "Stake for 4–5 years; 3.5 × 3.5–4 × 4 m"],
 ["MM.106 / EMLA-106", "about 60–75%", "Sloping, well-drained loam; never clay", "Woolly aphid resistant, bears in year 3; highly susceptible to <i>Phytophthora</i> collar rot in wet or clay soil", "Stake early; 3 × 3 m (1,111 per ha) to 3.5 × 2.5 m"],
 ["M.9 / T337", "about 30–40%", "Deep, fertile, irrigated flat or terraced soil; avoid windy hilltops", "Bears in years 2–3, collar rot resistant; shallow, brittle roots; woolly aphid and fire blight prone", "3–4 wire trellis and drip essential; 3.0 × 1.0 m (3,333 per ha) or 3.0 × 1.5 m (2,222 per ha)"],
 ["G.11, G.41, G.214, Bud.9", "Dwarf", "Certified high-density blocks", "Geneva rootstocks bred for replant tolerance and collar rot and fire blight resistance; Bud.9 is winter hardy", "Trellis and drip"]])}
<h2>Common rootstock mistakes</h2>
<ul><li><b>MM.106 in heavy clay or wet soil:</b> the main cause of collar rot deaths in young medium-density orchards.</li>
<li><b>M.9 on poor, dry or windy land without trellis or drip:</b> small fruit, leaning trees and early decline, especially with spur strains.</li>
<li><b>Burying the graft union:</b> keep it 15–20 cm above the soil, or the variety roots itself and loses the rootstock's benefits, and collar rot risk rises.</li>
<li><b>Replanting into old apple pits:</b> replant disease stunts new trees on any rootstock except, partly, the Geneva series. <a href="/root-rot-and-tree-mortality/">How to treat replant soil</a>.</li></ul>"""
    qas = [("What is the best rootstock for apple in Himachal?", "On deep, irrigated, terraced land with trellis: M.9. On well-drained slopes: MM.106 (not in clay). On drier, shallow hill soil: MM.111. On steep, unirrigated slopes: seedling."),
           ("Why are MM.106 trees dying?", "MM.106 is highly susceptible to <i>Phytophthora</i> collar rot in wet or clay soil. Improve drainage, keep the graft high and treat as for collar rot."),
           ("Does M.9 need support?", "Yes. M.9 has shallow, brittle roots and needs a 3–4 wire trellis and drip irrigation.")]
    article("/varieties/rootstocks/", "Apple Rootstocks: M9, MM106, MM111, M7 Compared", "Apple rootstocks for Indian orchards: M.9, MM.106, MM.111, M.7, seedling and Geneva compared by vigour, soil, collar rot risk, trellis and spacing.",
            "Apple rootstocks: M.9, MM.106, MM.111 and M.7", body, crumbs=VH, qas=qas, srcs=[S["hp"], S["cith"], S["skuastj"], S["skuastk"]])

    # ---------------------------------------------------------------- pruning
    body = f"""{answer("Bad pruning is behind much of the dieback, weak buds and alternate bearing in Indian orchards. Use thinning cuts instead of heading cuts, remove limbs thicker than half the trunk with angled renewal cuts, bend branches to 45–60°, cut 15 cm below any canker with sterilised tools, and immediately paste every cut over 2.5 cm with copper oxychloride or Bordeaux paste (ICAR, SKUAST-K).")}
<h2>What goes wrong with heavy pruning</h2>
<ul><li><b>Heading cuts</b> (cutting branch tips back) produce bunches of upright, non-fruiting shoots.</li>
<li><b>Vigorous upper tiers shade the lower branches</b>, so lower spurs do not form flower buds: weak flowering and on-year/off-year bearing.</li>
<li><b>Narrow forks under 30°</b> split under crop load.</li>
<li><b>Unsealed stubs and large cuts</b> let <i>Botryosphaeria</i> and <i>Diplodia</i> canker in; limbs then die back, and growers call them "dead-like plants".</li></ul>
<h2>Winter (dormant) pruning, step by step</h2>
<ol><li>Remove dead, diseased and broken wood first. Cut cankers 15 cm into healthy green wood.</li>
<li>Sterilise tools between trees with 70% ethanol.</li>
<li>Thin out, do not head back: remove whole limbs that are more than half the trunk's thickness with an angled renewal cut that leaves a short stub to regrow.</li>
<li>Keep the top narrower than the bottom so light reaches lower spurs (tall spindle or modified leader shape).</li>
<li>Bend young branches to 45–60° (beyond horizontal in tall spindle systems) instead of cutting them.</li>
<li>Paste every cut over 2.5 cm the same day with copper oxychloride or Bordeaux paste. Old Chaubattia paste contains red lead; prefer lead-free copper paste.</li>
<li>Whitewash trunks in November against sunscald and canker.</li></ol>
<h2>Summer pruning</h2>
<p>In July–August remove upright water sprouts that shade fruit. This lets light colour the fruit naturally and reduces the need for colour sprays.</p>
<h2>Training systems</h2>
{table(["System", "Rootstock", "Shape"], [["Open centre / modified leader", "Seedling, MM.111", "Wide tree, few scaffold limbs"], ["Spindle bush", "MM.106, MM.111, M.7", "Central leader with short, renewed fruiting branches"], ["Vertical axis / tall spindle", "M.9 on trellis", "Narrow, tall leader; many small branches bent below horizontal and renewed regularly"]])}"""
    qas = [("When should apple trees be pruned?", "Main pruning in winter dormancy (December–February), plus light summer pruning of water sprouts in July–August."),
           ("What should I apply on apple pruning cuts?", "Copper oxychloride or Bordeaux paste on every cut over 2.5 cm, the same day. Prefer lead-free paste to old Chaubattia paste."),
           ("Why do apple branches dry after pruning?", "Usually canker (<i>Botryosphaeria</i>, <i>Diplodia</i>) entering through unsealed cuts or stubs. Cut 15 cm into healthy wood, sterilise tools and paste the cut."),
           ("Does pruning cause alternate bearing?", "Heavy heading cuts and shaded lower branches reduce flower buds and feed the on-year/off-year cycle. Thinning cuts and an open canopy help.")]
    article("/pruning-and-canopy-management/", "Apple Pruning Guide: Stop Dieback, Shading & Weak Buds", "Apple tree pruning for Indian orchards: thinning vs heading cuts, canker and dieback, copper paste, branch bending, summer pruning and training systems.",
            "Apple pruning: stop dieback, shading and weak buds", body, crumbs=HOME, qas=qas, srcs=[S["skuastk"], S["hp"], S["skuastj"]])

    import content2
    content2.build(g, S, HOME, season)


def llms(g):
    import os
    lines = ["# Apple Orchard India (appleorchard.in)", "",
             "> Free apple orchard guide for growers in Himachal Pradesh, Jammu & Kashmir, Uttarakhand and low-chill areas, by Gujarat Bio Organics. Built from Dr. YSP UHF Nauni, SKUAST-K, SKUAST-J, ICAR-CITH, NHB, MoA&FW and CIB&RC sources. English and Hindi.", "",
             "## Key pages"]
    names = {"/": "Apple farming in India: orchard guide", "/fertilizer-schedule-and-calculator/": "Apple fertilizer schedule and calculator (bigha, kanal, nali)",
             "/varieties-and-rootstocks/": "Apple varieties, rootstocks and pollinizers", "/root-rot-and-tree-mortality/": "Apple root rot, collar rot and tree deaths",
             "/alternate-bearing-and-fruit-quality/": "Alternate bearing, fruit drop and small fruit", "/diseases-and-pests/spray-schedule/": "Apple spray schedule by stage",
             "/hi/seb-ki-kheti/": "सेब की खेती (Hindi)"}
    for p, n in names.items():
        lines.append(f"- [{n}]({g['SITE']}{p})")
    lines += ["", "## All pages"] + [f"- {g['SITE']}{p}" for p, _, _ in g["PAGES"]]
    lines += ["", "## Contact", "WhatsApp / phone +91 99787 91167. Publisher: Gujarat Bio Organics Pvt. Ltd. (https://www.gujaratbio.com/)."]
    open(os.path.join(g["DIST"], "llms.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
