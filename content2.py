"""English pages for appleorchard.in, part 2: fertilizer + calculator, fruit quality, root rot, diseases and pests, spray schedule, harvest and profit, about."""

LBL = "Use only pesticides registered for apple by CIB&RC, at the dose and waiting period on the label, and follow your state's current spray schedule (SKUAST-K, Dr. YSP UHF or the state horticulture department)."


def calc_form():
    opt = lambda lst, sel=None: "".join(f'<option value="{v}"{" selected" if v == sel else ""}>{t}</option>' for v, t in lst)
    lvl = '<option value="low">Low</option><option value="med" selected>Medium / not tested</option><option value="high">High</option>'
    units = [("bigha", "Bigha, Himachal (809 m²)"), ("kanal", "Kanal, J&K (506 m²)"), ("nali", "Nali, Uttarakhand (201 m²)"), ("acre", "Acre"), ("ha", "Hectare")]
    sp = [("s75", "7.5 × 7.5 m, seedling (72 / acre)"), ("s6", "6 × 6 m (112 / acre)"), ("s5", "5 × 5 m (162 / acre)"), ("s4", "4 × 4 m (253 / acre)"), ("s35", "3.5 × 3.5 m (330 / acre)"),
          ("s3", "3 × 3 m, MM.106 (450 / acre)"), ("h315", "3.0 × 1.5 m, M.9 (899 / acre)"), ("h31", "3.0 × 1.0 m, M.9 tall spindle (1,349 / acre)"), ("h351", "3.5 × 1.0 m, M.9 (1,156 / acre)"), ("custom", "Other spacing")]
    return f"""<div class="calc"><form id="calc" onsubmit="return false">
<fieldset><legend>Your orchard</legend>
<div class="row2"><label>Orchard type<select id="system"><option value="std">Standard (seedling, MM.111, MM.106, M.7)</option><option value="hdp">M.9 high density</option></select></label>
<label>Tree age (years)<input id="age" type="number" min="1" max="40" value="8"></label></div>
<div class="row2"><label>Area<input id="area" type="number" min="0.1" step="0.1" value="5" inputmode="decimal"></label><label>Unit<select id="unit">{opt(units)}</select></label></div>
<label>Spacing<select id="spacing">{opt(sp, "s6")}</select></label>
<div class="row2" id="customsp" hidden><label>Row to row (m)<input id="rowm" type="number" step="0.1" value="5"></label><label>Tree to tree (m)<input id="plantm" type="number" step="0.1" value="5"></label></div>
<label>Or exact number of trees <span class="hint">(optional)</span><input id="trees" type="number" min="0" placeholder="e.g. 110"></label>
<div class="row2"><label>Irrigation<select id="irr"><option value="basin">Rainfed / basin</option><option value="drip">Drip fertigation</option></select></label>
<label>This year's crop<select id="load"><option value="normal">Normal or heavy bloom</option><option value="light">Light crop / off year</option><option value="none">Almost no crop</option><option value="shoots">Shoots growing over 50 cm</option></select></label></div>
</fieldset>
<fieldset><legend>Soil test <span class="hint">(Soil Health Card, optional)</span></legend>
<div class="row3"><label>Nitrogen<select id="soiln">{lvl}</select></label><label>Phosphorus<select id="soilp">{lvl}</select></label><label>Potash<select id="soilk">{lvl}</select></label></div>
<span class="hint">Low adds 25%, high cuts 25% (N &lt;280 / &gt;560 kg/ha, P &lt;10 / &gt;25, K &lt;118 / &gt;280). Standard trees are capped at 700 : 350 : 700 g.</span>
<label>Soil pH<input id="ph" type="number" step="0.1" placeholder="e.g. 5.8"></label>
</fieldset>
<a id="wa" class="btn btn-wa" href="#" rel="nofollow">Send this plan to our team on WhatsApp</a>
</form><section id="result" aria-live="polite"></section></div>"""


def build(g, S, HOME, season):
    article, table, answer, facts, gbo_box = g["article"], g["table"], g["answer"], g["facts"], g["gbo_box"]

    # ---------------------------------------------------------------- fertilizer
    body = f"""{answer("Bearing standard apple trees (10 years and older) need about 700 g N, 350 g P₂O₅ and 700 g K₂O plus 70–100 kg FYM per tree per year; younger trees get 70 : 35 : 70 g and 10 kg FYM per year of age (Dr. YSP UHF Nauni, SKUAST-K). Mature M.9 high-density trees need about 120–180 g N, 50–80 g P₂O₅ and 150–250 g K₂O per tree through weekly drip (ICAR-CITH, Dr. YSP UHF). Give FYM, phosphorus and half the potash in November–December, 60% of nitrogen before bud break and the rest after petal fall.")}
<h2>Apple fertilizer calculator</h2>
<p>Enter your orchard in bigha, kanal, nali or acre, the tree age and spacing. The calculator works out the tree count, the dose per tree, total SSP, MOP and urea (or CAN in acidic soil), bags to buy, and when to give each part. For M.9 on drip it gives weekly MAP, urea and SOP.</p>
{calc_form()}
<p class="src">Calculator rules (research reference, section 17): standard dose 70 : 35 : 70 g × age up to 10 years, FYM 10 kg × age; M.9 dose 35 : 17.5 : 35 g × age up to 7 years, capped at 245 g N per tree; soil test ±25% (ICAR-IISS brackets); off-year or excess shoots halve or remove the post-bloom nitrogen; pH below 5.5 switches urea to CAN; M.9 drip: all phosphorus as MAP, all potash as SOP, urea reduced by MAP's nitrogen, 15 weekly doses mid-March to June; warning above SKUAST-K's 120 kg N/ha Karewa ceiling.</p>

<h2>Recommended doses</h2>
{table(["Institute / system", "Tree age / rootstock", "N (g/tree/yr)", "P₂O₅", "K₂O", "FYM (kg/tree/yr)"], [
 ["Dr. YSP UHF Nauni (Himachal)", "Standard, 1–9 years", "70 × age", "35 × age", "70 × age", "10 × age"],
 ["Dr. YSP UHF / SKUAST-K", "Standard bearing, 10+ years", "700", "350", "700 (up to 1,000 for a heavy crop)", "70–100"],
 ["Uttarakhand (Chaubattia)", "Standard bearing, 10+ years", "500–700", "250–350", "500–700", "50–100"],
 ["Dr. YSP UHF (high density)", "M.9 on drip, 1–7+ years, 14–15 splits", "35 × age (year 5 = 175)", "17.5 × age", "35 × age", "5–20"],
 ["SKUAST-K / ICAR-CITH (high density)", "M.9 on fertile Karewa soil", "45–120 kg N/ha total (trim if shoots over 50 cm)", "40–60 kg/ha", "120–180 kg/ha", "15–20"]])}
<p>In acidic soil (pH below 5.5) use CAN or lime/dolomite rather than ammonium sulphate alone.</p>

<h2>When to apply</h2>
{table(["When", "What"], [["Late autumn (Nov–Dec)", "All FYM, all phosphorus (SSP) and 50–100% of potash (MOP), in a ring 30 cm inside the drip line, never touching the trunk"], ["Pre-bloom (Feb–Mar, 2–3 weeks before bud break)", "50–67% of nitrogen (urea or CAN)"], ["After petal fall (Apr–May)", "The remaining 33–50% of nitrogen and any remaining potash, only if fruit set is heavy. In an off year cut this nitrogen by 50–100% so trees do not throw wild shoots"], ["Fruit sizing (Jun–Aug)", "No heavy soil nitrogen; SOP (0:0:50) and calcium sprays"], ["Leaf fall (Oct–Nov)", "3–5% urea (30–50 g/L) + 0.5% zinc sulphate + 0.1–0.2% Solubor on green leaves before they drop: reloads next spring's buds and speeds rotting of scabbed leaves (SKUAST-K)"]])}

<h2>Worked example: 5 bighas (1 acre) in Himachal, standard trees, year 8</h2>
<p>6 × 6 m spacing gives 112 trees (about 22 per bigha). Soil: pH 5.3 (acidic), organic carbon 1.1%, N 260 (low, +25%), P 15 (medium), K 105 (low, +25%), heavy bloom. Year-8 dose: N 560 × 1.25 = 700 g, P₂O₅ 280 g, K₂O 700 g per tree: <b>78.4 kg N, 31.4 kg P₂O₅ and 78.4 kg K₂O</b> per acre, plus about 9 tonnes FYM.</p>
{table(["Product", "Quantity", "When"], [["SSP (16%)", "196 kg (about 4 bags)", "Nov–Dec"], ["MOP (60%)", "131 kg (about 2.6 bags)", "65 kg Nov–Dec, 65 kg Apr–May"], ["CAN (25% N), because pH is below 5.5", "314 kg (about 6.3 bags)", "188 kg Feb–Mar, 125 kg Apr–May"]])}
<p>Because pH is 5.3, check lime or dolomite with your soil lab, and add the pink-bud boron, 4–6 calcium chloride sprays and the October urea-zinc-boron spray.</p>
<h2>Worked example: 8 kanals (1 acre) in Kashmir, M.9 high density, year 5</h2>
<p>3.0 × 1.5 m gives 899 trees. Dose 175 : 87.5 : 175 g per tree = <b>157 kg N, 79 kg P₂O₅, 157 kg K₂O</b> and about 13.5 tonnes FYM. Through drip in 15 weekly doses (mid-March to end of June): MAP 129 kg, SOP 315 kg and urea 308 kg in total, that is <b>8.6 kg MAP + 21.0 kg SOP + 20.6 kg urea per acre per week</b>. Watch shoot length (30–45 cm is right) and trim June nitrogen if shoots go past 50 cm.</p>

<h2>Foliar sprays: boron, calcium, zinc, magnesium</h2>
{table(["Nutrient", "When", "Spray", "Why"], [["Boron", "Pink bud and October", "0.1–0.15% Solubor or boric acid (1–1.5 g/L); never above 0.2%", "Pollen tube growth; reduces flower drop"], ["Calcium", "4–6 sprays, 15 days apart, from 2–3 weeks after petal fall", "0.3–0.5% calcium chloride (3–5 g/L); skip above 28–30°C", "Prevents bitter pit and cork spot"], ["Zinc", "Delayed dormant and October", "0.5% zinc sulphate (5 g/L) + 0.25% lime", "Little leaf and rosettes"], ["Magnesium", "Walnut stage", "1–2% magnesium sulphate (10–20 g/L)", "Prevents early yellow leaf drop"], ["Potassium", "Fruit sizing", "1% SOP (10 g/L)", "Size and colour (ICAR-CITH)"]])}
<p class="note"><b>Tank mixing:</b> never mix calcium chloride or calcium nitrate with sulphates (SOP, magnesium, zinc sulphate) or phosphates (MAP, MKP, 19:19:19). Use separate tanks.</p>
<h2>Biofertilizers and biostimulants</h2>
<ul><li><b>VAM (AMF) + Trichoderma + Pseudomonas</b> strongly reduced replant disease deaths (SKUAST-K 2024).</li>
<li><b>Humic acids</b> improve fine roots in compacted soil when combined with drainage and mulch; they cannot cure root rot.</li>
<li><b>Seaweed (Ascophyllum) and amino acids</b> support fruit set and colour under cold spring swings, alongside boron and calcium (<i>Scientia Horticulturae</i>).</li></ul>
{gbo_box()}
<h2>Mistakes that waste money</h2>
<ul><li>Water-soluble fertilizer poured on waterlogged or very acidic soil is mostly wasted.</li>
<li>Excess growth regulators on stressed trees worsen fruit drop.</li>
<li>Full nitrogen in an off year produces long shoots, shade and more alternate bearing.</li></ul>
<script src="/calc.js?v={g['TODAY']}" defer></script>"""
    qas = [("How much fertilizer does an apple tree need?", "Standard trees: 70 g N, 35 g P₂O₅, 70 g K₂O and 10 kg FYM per year of age until year 10, then 700 : 350 : 700 g and 70–100 kg FYM. M.9 trees: half that per year of age up to year 7."),
           ("When should I give fertilizer to apple trees?", "FYM, phosphorus and half the potash in November–December; 60% of nitrogen 2–3 weeks before bud break; the rest after petal fall if fruit set is good."),
           ("What is the best fertilizer for apple trees?", "Well-rotted FYM plus balanced N, P and K by tree age, with boron, calcium and zinc sprays. Use CAN instead of urea in acidic soil."),
           ("Which spray is given to apple in October?", "3–5% urea + 0.5% zinc sulphate + 0.1–0.2% Solubor on green leaves before leaf fall (SKUAST-K)."),
           ("How do I calculate fertilizer for my apple orchard in bigha or kanal?", "Use the calculator above: 1 acre = 5 Himachal bighas = 8 J&K kanals = 20.16 Uttarakhand nalis.")]
    article("/fertilizer-schedule-and-calculator/", "Apple Fertilizer Schedule & Orchard Dose Calculator (India)", "Apple fertilizer schedule by tree age with a free calculator for bigha, kanal, nali or acre: standard and M.9 doses, timing, boron and calcium sprays.",
            "Apple fertilizer schedule and orchard dose calculator", body, crumbs=HOME, qas=qas, srcs=[S[k] for k in ("ysp", "skuastk", "cith", "shc", "units")],
            extra_schema=[{"@type": "WebApplication", "name": "Apple orchard fertilizer calculator", "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any", "url": g["SITE"] + "/fertilizer-schedule-and-calculator/", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"}}])

    # ---------------------------------------------------------------- alternate bearing and fruit quality
    body = f"""{answer("Apples drop in three waves: after bloom (poor pollination, boron or bees), the June drop (May–June drought and too many fruits competing) and before harvest (heat, ethylene, mites). Fix them with 25–33% pollinizers and a pink-bud boron spray, irrigation in May–June, thinning to one fruit per cluster at pea size (30–40 leaves per fruit), 4–6 calcium chloride sprays, summer pruning for colour, and NAA 10 ppm 10–20 days before expected pre-harvest drop (Dr. YSP UHF, SKUAST-K).")}
<h2>Breaking alternate bearing (on year, off year)</h2>
<p>A heavy crop makes seeds that suppress next year's flower buds, so a bumper year is followed by a poor one. Three steps break the cycle:</p>
<ol><li><b>Thin early:</b> within 10–25 days after petal fall (fruits 8–12 mm), hand-thin to one king fruit per cluster, 15–20 cm apart, about 30–40 leaves per fruit. Or use a registered thinner such as NAA (10–15 ppm) or 6-BA (75–100 ppm) as advised by your university. Avoid carbaryl: it is toxic to bees and restricted. Thinning also roughly doubles fruit size (SKUAST-K, Himachal package of practices).</li>
<li><b>Protect summer leaves</b> (June–August), when next year's buds form: control Marssonina, Alternaria and mites, and irrigate dry spells.</li>
<li><b>Reload buds after harvest:</b> 3–5% urea + 0.5% zinc sulphate + 0.1–0.2% Solubor on green leaves in October–November.</li></ol>
<p>In the off year cut the post-bloom nitrogen by 50–100%; full nitrogen only produces shoots and shade.</p>
<h2>Fruit drop</h2>
{table(["Wave", "When", "Main causes", "What helps"], [["Post-bloom drop", "After flowering", "Too few pollinizers or bees, cold or rain at bloom, boron shortage, spraying at bloom", "25–33% pollinizers, 4–6 beehives per hectare, boron at pink bud, no bloom sprays"], ["June drop", "May–June", "Drought during cell division, too many fruits", "Irrigation, pea-stage thinning"], ["Pre-harvest drop", "Before picking", "Heat, ethylene, mite stress", "NAA 10 ppm (1 mL Planofix in 4.5 L) 10–20 days before expected drop, mite control; avoid overusing ethephon"]])}
<h2>Small apples</h2>
<ul><li>Over-cropping without thinning: the most common cause.</li><li>Dry spells in May–June (cell division) and August–September (sizing).</li><li>Spur strains on M.9 in poor soil.</li><li>Weak roots from root rot, woolly aphid galls or replant disease.</li><li>Leaf loss from Marssonina, scab or mites before harvest.</li></ul>
<h2>Fruit quality: bitter pit, colour and cracking</h2>
<ul><li><b>Bitter pit and cork spot</b> (brown sunken spots in the flesh): calcium shortage in the fruit. 4–6 sprays of 0.3–0.5% calcium chloride every 15 days from 2–3 weeks after petal fall; skip above 28–30°C; avoid excess nitrogen and drought swings.</li>
<li><b>Poor red colour:</b> shaded fruit and low altitude. Summer pruning in July–August, high-colour strains in lower belts.</li>
<li><b>Fruit cracking:</b> irregular watering, dry then flooded. Keep moisture even and mulch.</li></ul>"""
    qas = [("How do I stop alternate bearing in apple?", "Thin to one fruit per cluster 10–25 days after petal fall, protect summer leaves, cut off-year nitrogen, and give the October urea + zinc + boron spray."),
           ("Why do apple fruits drop in June?", "Dry weather in May–June combined with too many fruits competing. Irrigate and thin at pea size."),
           ("How do I stop pre-harvest fruit drop in apple?", "NAA at 10 ppm (1 mL Planofix in 4.5 L water) 10–20 days before expected drop, plus mite control. Do not overuse ethephon."),
           ("What causes bitter pit in apple?", "Low calcium in the fruit. Give 4–6 calcium chloride sprays (0.3–0.5%) from 2–3 weeks after petal fall, avoid excess nitrogen and keep watering even."),
           ("Why are my apples small?", "Usually too many fruits (no thinning), dry spells in May–June or August–September, weak roots or early leaf loss.")]
    article("/alternate-bearing-and-fruit-quality/", "Stop Alternate Bearing, Fruit Drop & Small Apples (India)", "Why apple trees bear alternately, why fruit drops and stays small, and how thinning, pollination, boron, calcium sprays and NAA fix it.",
            "Stop alternate bearing, fruit drop and small apples", body, crumbs=HOME, qas=qas, srcs=[S["ysp"], S["skuastk"], S["skuastj"], S["hp"]])

    # ---------------------------------------------------------------- root rot and tree mortality
    body = f"""{answer("Most apple tree deaths in India come from three causes: white root rot (<i>Dematophora necatrix</i>) in waterlogged monsoon soil, collar rot (<i>Phytophthora cactorum</i>) on MM.106 in clay, and untreated apple replant disease. All three start with poor drainage or the wrong site. Early cases can be saved by draining water away, exposing and cleaning the root collar, copper paste and a drench recommended by your university (ICAR-CITH, SKUAST-K).")}
<h2>Which one is killing your trees?</h2>
{table(["Problem", "What you see", "When", "Main cause"], [["White root rot", "Sparse, small, yellow leaves, then the tree collapses; dig the roots: brown rotten roots covered in white cottony fungus", "Worst in June–September", "Waterlogged soil, hillside runoff"], ["Collar rot", "Slimy reddish-brown bark rot right at the soil line", "Wet seasons", "MM.106 in clay or wet soil; buried graft union"], ["Canker and dieback", "Cracked, sunken bark; branches dying back from pruning stubs", "Any time", "Unsealed pruning cuts and stubs (<i>Botryosphaeria</i>, <i>Diplodia</i>)"], ["Apple replant disease", "Young trees in old apple land stay stunted for years", "First 1–3 years", "Fungi, nematodes and soil fatigue in old apple soil"], ["Woolly aphid on roots", "White wool on twigs; galls on roots; stunted trees", "Spring to autumn", "Susceptible rootstock (seedling, M.9, M.7)"]])}
<h2>Saving trees with white root rot or collar rot</h2>
<ol><li><b>Drain the water:</b> dig cut-off ditches above the orchard on slopes so runoff does not reach the trees; plant on raised mounds where soil stays wet.</li>
<li><b>Keep the graft union 15–20 cm above the soil</b> and keep a 60 cm undisturbed basin around the trunk.</li>
<li><b>Expose the collar and main roots in November–December</b>, cut away dead roots and rotten bark, and paint with copper oxychloride or Bordeaux paste.</li>
<li><b>Drench the root zone</b> in April, June, July and September as per the ICAR / state university protocol: for white root rot, carbendazim + mancozeb or a <i>Trichoderma</i> + <i>Pseudomonas</i> bio-drench; for collar rot, metalaxyl-M + mancozeb or copper oxychloride with <i>Trichoderma</i>. Doses as per the registered label.</li>
<li>Remove dead trees with as many roots as possible and do not replant in the same pit without treating the soil.</li></ol>
<h2>Replanting old apple land</h2>
<ul><li>Shift new pits into the old alleyways, away from old root zones.</li><li>Fallow with mustard or marigold, or solarise the soil under clear plastic in summer.</li><li>Fill pits with virgin topsoil, well-rotted FYM and a bio-consortium of VAM (AMF), <i>Trichoderma</i> and <i>Pseudomonas</i>; SKUAST-K (2024) found this strongly cut replant deaths.</li><li>Use Geneva rootstocks (G.11, G.41, G.214) where available: bred for replant tolerance.</li></ul>
<h2>Prevent canker dieback</h2>
<p>Seal every pruning cut over 2.5 cm the same day with copper paste, cut cankers 15 cm into healthy wood, sterilise tools with 70% ethanol, whitewash trunks in November and give a post-harvest copper spray. <a href="/pruning-and-canopy-management/">Pruning guide</a>.</p>
{gbo_box()}
<p class="note"><b>Pesticide safety:</b> {LBL}</p>"""
    qas = [("Why are my apple trees dying?", "Most often white root rot in waterlogged monsoon soil, collar rot on MM.106 in clay, canker from unsealed pruning cuts, or replant disease in old apple land."),
           ("How do I identify white root rot in apple?", "Leaves become sparse, small and yellow; dig at the roots: rotten brown roots covered with white cottony fungus, mostly in June–September."),
           ("How do I treat collar rot in apple?", "Improve drainage, keep the graft 15–20 cm above soil, scrape rotten bark and paint with Bordeaux paste, and drench as per your university protocol."),
           ("Can I plant new apple trees where old ones died?", "Not directly. Move pits to the old alleyways or treat the soil (fallow or solarise, fresh topsoil, FYM, VAM + Trichoderma + Pseudomonas) and use replant-tolerant rootstocks if available.")]
    article("/root-rot-and-tree-mortality/", "Apple Root Rot, Collar Rot & Dying Trees: Rescue Guide", "Why apple trees die in Indian orchards: white root rot, collar rot on MM.106, canker dieback and replant disease, how to tell them apart and save trees.",
            "Apple root rot, collar rot and dying trees", body, crumbs=HOME, qas=qas, srcs=[S["cith"], S["skuastk"], S["hp"], S["ppqs"]])

    # ---------------------------------------------------------------- diseases and pests hub
    sub = HOME + [("/diseases-and-pests/", "Diseases & pests")]
    body = f"""{answer("Apple tree deaths come mainly from white root rot, collar rot and canker dieback; leaf diseases such as apple scab, Marssonina blotch and Alternaria strip leaves and spoil fruit. Leaf diseases are controlled by leaf sanitation (including the October 5% urea spray) and rotating fungicides from different groups; root diseases by drainage, collar surgery and copper paste. Calendar spraying wastes money and kills the predatory mites that keep red mite in check (SKUAST-K 2026, ICAR-CITH).")}
<div class="grid"><a class="card" href="/diseases-and-pests/spray-schedule/"><span class="tag">Schedule</span><h3>Apple spray schedule</h3><p>What to spray at each stage, and when not to spray at all.</p></a>
<a class="card" href="/diseases-and-pests/apple-scab/"><h3>Apple scab</h3><p>Olive velvety spots to dark corky scabs on leaves and fruit.</p></a>
<a class="card" href="/diseases-and-pests/powdery-mildew/"><h3>Powdery mildew</h3><p>White floury shoot tips; winter pruning and sulphur.</p></a>
<a class="card" href="/diseases-and-pests/woolly-apple-aphid/"><h3>Woolly apple aphid</h3><p>White wool on twigs and galls on roots.</p></a></div>
<h2>Apple diseases at a glance</h2>
{table(["Disease", "Symptoms", "Curable?", "Management"], [["White root rot", "Sparse small leaves, collapse; white cottony fungus on brown roots (Jun–Sep)", "Early only", "<a href=\"/root-rot-and-tree-mortality/\">Drainage, root exposure, copper paste, drench</a>"], ["Collar rot", "Slimy red-brown bark rot at the soil line (worst on MM.106 in clay)", "Early only", "Raised beds, graft 15–20 cm high, Bordeaux paste, drench"], ["Canker and dieback", "Cracked, sunken bark; branches dying from pruning stubs", "Prune and prevent", "Cut 15 cm into healthy wood, sterilise tools, copper paste, whitewash"], ["<a href=\"/diseases-and-pests/apple-scab/\">Apple scab</a>", "Velvety olive spots turning into dark corky scabs on leaves and fruit", "Preventive", "October 5% urea, rotated fungicides"], ["Marssonina blotch and Alternaria", "Purple-brown blotches turning bright yellow, leaf fall in July–August; frog-eye spots (Alternaria)", "Preventive", "Open canopy, leaf sanitation, rotated fungicides"], ["<a href=\"/diseases-and-pests/powdery-mildew/\">Powdery mildew</a>", "White floury shoot tips", "Manageable", "Winter pruning of white tips, wettable sulphur"], ["Viruses; fire blight", "Mosaic patches; black shepherd's-crook shoots (fire blight)", "No", "Virus-free planting material; report suspected fire blight to SKUAST or ICAR-CITH"]])}
<h2>Apple pests at a glance</h2>
{table(["Pest", "Signs", "When", "Non-chemical control", "Registered chemicals (as per label)"], [["San Jose scale", "Ash-grey crust on bark; red halos on fruit", "Dormant season and summer crawlers", "Prune encrusted twigs; parasitoid <i>Encarsia perniciosi</i>", "Horticultural mineral oil 2% at delayed dormant (14–21 days apart from sulphur); summer insecticide as per schedule"], ["European red mite", "Silvery-bronze leaves, summer leaf drop (check with a 10× lens for red eggs)", "May–August", "Stop calendar pyrethroid sprays that kill predatory mites; dormant oil", "Rotate acaricide groups: hexythiazox, fenazaquin, spiromesifen, propargite"], ["<a href=\"/diseases-and-pests/woolly-apple-aphid/\">Woolly apple aphid</a>", "White wool on twigs; galls on roots", "Spring–autumn", "Resistant MM.106 / MM.111; parasitoid <i>Aphelinus mali</i>", "Imidacloprid or thiamethoxam; root treatment as per schedule"], ["Stem and shot-hole borers", "Coarse sawdust (stem borer); pinhead holes on stressed trunks", "Summer", "Fix drought, canker and sunscald first; hooked wire in tunnels", "Insecticide plug in tunnels as per label. Dichlorvos, phorate and monocrotophos are banned or withdrawn."], ["Blossom thrips", "Browned, distorted petals", "Tight cluster to pink bud", "Sticky traps", "Pre-bloom only; never during bloom"], ["Codling moth", "Worm tunnel to the core", "Quarantine pest found only in Ladakh (Leh, Kargil)", "Strict crate quarantine, pheromone traps, <i>Trichogramma</i>", "Ladakh IPM schedule (SKUAST-K)"]])}
<p class="note"><b>Pesticide safety:</b> {LBL} Dichlorvos, monocrotophos, phorate, carbofuran, benomyl and carbaryl are banned, withdrawn or restricted in India.</p>"""
    qas = [("What are the main diseases of apple in India?", "White root rot, collar rot, canker and dieback, apple scab, Marssonina blotch, Alternaria leaf spot and powdery mildew."),
           ("Why are apple leaves falling in July–August?", "Most often Marssonina blotch or Alternaria, sometimes European red mite. Leaf sanitation, an open canopy and rotated fungicides help."),
           ("How do I control red mite in apple?", "Stop calendar pyrethroid sprays that kill predatory mites, use dormant oil, and rotate acaricide groups only when counts exceed 5–10 mites per leaf.")]
    article("/diseases-and-pests/", "Apple Diseases & Pests in India: Symptoms & IPM Control", "Apple diseases and pests in India: root rot, collar rot, canker, scab, Marssonina, mildew, San Jose scale, red mite, woolly aphid, borers and IPM control.",
            "Apple diseases and pests: identification and control", body, crumbs=HOME, qas=qas, srcs=[S["skuastk"], S["cith"], S["ysp"], S["ppqs"]])

    body = f"""{answer("Apple scab, caused by the fungus <i>Venturia inaequalis</i>, shows as velvety olive-green spots on leaves and fruit that turn into dark, corky, cracked scabs. It is prevented, not cured: a 5% urea spray on leaves in October speeds the rotting of fallen leaves where the fungus survives winter, and fungicides from different groups are rotated through spring (SKUAST-K 2026).")}
<h2>Symptoms</h2><ul><li>Velvety olive-green spots on young leaves from green tip onwards.</li><li>Spots darken; leaves curl and fall early.</li><li>Fruit get dark, corky, scabby patches that crack and lose market value.</li></ul>
<h2>Why it keeps coming back</h2><p>The fungus survives winter in fallen scabbed leaves and releases spores in spring rain from green tip onwards. Orchards that leave last year's leaves on the ground carry the disease forward.</p>
<h2>Control</h2><ol><li><b>October–November:</b> 5% urea spray on leaves before they fall, then rake or rot fallen leaves.</li>
<li><b>From green tip in wet weather:</b> protect with fungicides rotated between groups. The SKUAST-K 2026 schedule lists captan, mancozeb, dodine, difenoconazole and myclobutanil; use doses and intervals from the current schedule and label. Do not rely on carbendazim alone.</li>
<li>Keep the canopy open so leaves dry quickly.</li>
<li>In Kashmir, consider scab-resistant <a href="/varieties/ambri/">Shireen and Firdous</a>.</li></ol>
<p class="note"><b>Pesticide safety:</b> {LBL}</p>"""
    qas = [("What is apple scab?", "A fungal disease (<i>Venturia inaequalis</i>) that causes olive spots and corky scabs on apple leaves and fruit."),
           ("How do I stop apple scab?", "Spray 5% urea on leaves in October to rot fallen leaves, and rotate fungicides from different groups from green tip in wet weather as per the SKUAST-K schedule."),
           ("Which apple varieties resist scab?", "Shireen and Firdous, released for Kashmir, were bred for scab resistance.")]
    article("/diseases-and-pests/apple-scab/", "Apple Scab Disease: Symptoms, Spray Schedule & Control", "Apple scab (Venturia) in Indian orchards: symptoms, why it returns, the October urea spray, fungicide rotation per SKUAST-K and resistant varieties.",
            "Apple scab: symptoms and control", body, crumbs=sub, qas=qas, srcs=[S["skuastk"], S["cith"], S["ppqs"]])

    body = f"""{answer("Apple powdery mildew coats young shoot tips, leaves and flowers with white floury fungus, stunting shoots and russeting fruit. Cut out white shoot tips during winter pruning, and spray wettable sulphur or myclobutanil as per label, keeping sulphur 14–21 days apart from horticultural mineral oil (Dr. YSP UHF).")}
<h2>Symptoms</h2><ul><li>White, powdery growth on young leaves and shoot tips; leaves narrow and curl.</li><li>Infected buds open late and weak; fruit can show net-like russet.</li></ul>
<h2>Control</h2><ol><li>In winter pruning, cut off shoot tips that look white or silvery; the fungus overwinters there.</li><li>From pink bud through early summer, spray wettable sulphur or myclobutanil at label doses.</li><li><b>Never spray sulphur within 14–21 days of horticultural mineral oil</b>: the combination burns leaves.</li><li>No sprays at full bloom.</li></ol>
<p class="note"><b>Pesticide safety:</b> {LBL}</p>"""
    qas = [("What causes white powder on apple leaves?", "Apple powdery mildew, a fungus that overwinters in shoot tips."), ("How do I control powdery mildew in apple?", "Remove white tips in winter pruning and spray wettable sulphur or myclobutanil as per label, keeping sulphur 14–21 days away from oil sprays.")]
    article("/diseases-and-pests/powdery-mildew/", "Apple Powdery Mildew: Symptoms & Control in India", "Apple powdery mildew: white floury shoot tips, winter pruning, wettable sulphur and myclobutanil, and the 14–21 day gap from horticultural oil.",
            "Apple powdery mildew", body, crumbs=sub, qas=qas, srcs=[S["ysp"], S["skuastk"], S["ppqs"]])

    body = f"""{answer("Woolly apple aphid covers twigs, pruning wounds and roots with white cottony wax. Root colonies make galls that weaken and stunt trees. MM.106 and MM.111 rootstocks resist it; the parasitoid wasp <i>Aphelinus mali</i> controls it naturally; registered insecticides such as imidacloprid or thiamethoxam are used as per label when colonies are heavy (SKUAST-K).")}
<h2>Signs</h2><ul><li>White woolly tufts on twigs, cracks and pruning wounds.</li><li>Knotty galls on roots; trees stunted and weak.</li><li>Sticky honeydew and black sooty mould.</li></ul>
<h2>Control</h2><ol><li>Plant on resistant rootstocks: MM.106 or MM.111.</li><li>Protect natural enemies, especially <i>Aphelinus mali</i>: avoid unnecessary broad-spectrum sprays.</li><li>Where colonies are heavy, spray imidacloprid or thiamethoxam as per label; treat root colonies as per your state schedule.</li></ol>
<p class="note"><b>Pesticide safety:</b> {LBL}</p>"""
    qas = [("What is the white cotton on my apple tree?", "Woolly apple aphid, a pest that covers twigs and roots with white wax."), ("Which rootstocks resist woolly aphid?", "MM.106 and MM.111.")]
    article("/diseases-and-pests/woolly-apple-aphid/", "Woolly Apple Aphid: Signs, Resistant Rootstocks & Control", "Woolly apple aphid: white wool on twigs, root galls, resistant MM.106 and MM.111 rootstocks, the parasitoid Aphelinus mali and registered sprays.",
            "Woolly apple aphid", body, crumbs=sub, qas=qas, srcs=[S["skuastk"], S["ppqs"]])

    body = f"""{answer("Spray apple by stage and by need, not by calendar. The key points are: horticultural mineral oil (2%) at delayed dormant above 4°C; scab protection from green tip in wet weather; boron at pink bud; <b>no sprays at full bloom</b>; calcium chloride sprays from 2–3 weeks after petal fall; Marssonina, Alternaria and mite watch in the monsoon; no sprays 3–4 weeks before picking; and urea + zinc + boron at leaf fall. Use the doses in your state's current schedule (SKUAST-K 2026, Dr. YSP UHF).")}
<p>A November 2026 survey found only about 25% of Kashmir growers following the SKUAST-K schedule, while spending Rs 97,360–1,09,870 per hectare on pesticides. Calendar spraying kills predatory <i>Typhlodromus</i> mites and causes European red mite outbreaks, so growers then spray even more.</p>
<h2>Stage-wise spray guide</h2>
{table(["Stage", "Main target", "What the schedules use", "Notes"], [
 ["Dormant (Dec–Feb)", "Canker, scale eggs", "Copper paste on cuts; whitewash trunks (Nov)", "Prune and paste the same day"],
 ["Delayed dormant / silver tip (Feb–Mar)", "San Jose scale, mite eggs", "Horticultural mineral oil 2%", "Only above 4°C; keep 14–21 days apart from sulphur"],
 ["Green tip to tight cluster (Mar)", "Apple scab", "Protectant fungicide in wet weather (e.g. captan, mancozeb, dodine)", "Rotate fungicide groups"],
 ["Pink bud (Mar–Apr)", "Fruit set; thrips; scab", "Boron 0.1–0.15%; thrips control only pre-bloom", "Last chance before bloom"],
 ["Full bloom (Apr)", "Pollination", "<b>Nothing</b>", "Bees at work; 4–6 hives per hectare"],
 ["Petal fall to pea size (Apr–May)", "Scab, powdery mildew; thinning", "Fungicide rotation (e.g. difenoconazole, myclobutanil); thinners only as advised", "Thin within 10–25 days after petal fall"],
 ["Fruit development (May–Aug)", "Bitter pit; Marssonina, Alternaria; red mite", "Calcium chloride 0.3–0.5% (4–6 sprays, 15 days apart); rotated fungicides (e.g. zineb/propineb, ziram, metiram + pyraclostrobin, tebuconazole + trifloxystrobin); acaricides only above threshold", "No calcium chloride above 28–30°C; separate calcium from sulphates and phosphates"],
 ["Pre-harvest (Aug–Oct)", "Pre-harvest drop", "NAA 10 ppm 10–20 days before expected drop, if needed", "Stop other sprays 3–4 weeks before picking"],
 ["Leaf fall (Oct–Nov)", "Bud reload; scab carry-over", "3–5% urea + 0.5% zinc sulphate + 0.1–0.2% Solubor; copper clean-up", "Spray while leaves are still green"]])}
<p class="note"><b>Pesticide safety:</b> {LBL} This table shows stages and active ingredients named in the SKUAST-K and Dr. YSP UHF schedules; always take doses and intervals from the current official schedule and the product label.</p>
<h2>How to cut your spray bill</h2>
<ul><li>Spray for a reason: scout first (10× lens for mites, leaf spots after rain).</li><li>Do not spray pyrethroids by calendar; they kill predatory mites.</li><li>Keep the canopy open and rake or rot fallen leaves to cut scab and Marssonina.</li><li>Never mix calcium sprays with sulphates or phosphates; never spray sulphur within 14–21 days of oil.</li></ul>"""
    qas = [("What is the apple spray schedule for 2026?", "Follow your state's official schedule (SKUAST-K 2026 for Kashmir; Dr. YSP UHF / Himachal horticulture department). The stages are dormant oil, scab protection from green tip, pink-bud boron, no sprays at bloom, calcium and leaf-disease sprays in summer, and urea + zinc + boron at leaf fall."),
           ("Should I spray apple during flowering?", "No. Never spray at full bloom: it kills bees and harms pollination."),
           ("Why are red mites increasing in my orchard?", "Calendar spraying of pyrethroids kills the predatory mites that keep red mite under control. Spray only when needed and rotate acaricide groups."),
           ("Can I mix sulphur and oil sprays?", "No. Keep wettable sulphur and horticultural mineral oil 14–21 days apart.")]
    article("/diseases-and-pests/spray-schedule/", "Apple Spray Schedule 2026: Stage-Wise Guide (SKUAST-K)", "Apple spray schedule by stage: dormant oil, scab, pink-bud boron, no bloom sprays, calcium, Marssonina, mites, pre-harvest, leaf fall and cutting spray costs.",
            "Apple spray schedule by stage", body, crumbs=sub, qas=qas, srcs=[S["skuastk"], S["ysp"], S["ppqs"]])

    # ---------------------------------------------------------------- harvest, storage and profit
    body = f"""{answer("Delicious apples are harvested 130–145 days after full bloom (Gala 110–120 days), judged by a starch-iodine reading of 2.5–3.5 on a 1–6 scale for controlled-atmosphere storage (4–5 for fresh sale) and firmness of 16–18 lb per square inch (NHB). Traditional orchards yield 6–11 t/ha; M.9 high-density orchards 30–45 t/ha or more by year 5, with 75–85% grade-A fruit (ICAR-CITH).")}
<h2>Harvest and grading</h2>
{table(["Grade", "Fruit diameter"], [["Extra large", "Over 80 mm"], ["Large", "75–80 mm"], ["Medium", "70–75 mm"], ["Small", "65–70 mm"], ["Extra small", "Below 65 mm"]])}
<p>Only clean fruit above 70 mm wins strong prices against 544,000–600,000 tonnes of imported apples a year (USDA FAS 2024). Nearly 30% of Himachal's harvest is lost or downgraded after picking (NITI Aayog 2026), so careful picking, grading and cold chain pay directly.</p>
<h2>Storage</h2>
<p>Controlled-atmosphere (CA) storage at 0–1°C, 90–95% humidity, 1.5–2.0% oxygen and 1.5–2.0% carbon dioxide keeps apples for 6–9 months (NHB). Low-chill apples such as HRMN-99 keep only 10–12 days and should be sold fresh.</p>
<h2>Cost and returns</h2>
{table(["Orchard type", "Investment / cost", "Yield"], [["Traditional seedling", "About Rs 1.2–1.8 lakh per hectare per year to maintain (pesticides alone Rs 97,360–1,09,870/ha in poorly scheduled Kashmir orchards)", "6–11 t/ha (2.5–4.5 t/acre)"], ["M.9 high density (3,333 trees/ha)", "About Rs 35–48 lakh per hectare in year one (Rs 14–19.5 lakh per acre) for plants, trellis, drip and anti-hail net; 50% state / MIDH subsidy available for high-density planting", "30–45+ t/ha (12–18+ t/acre) by year 5, 75–85% grade A"]])}
<p class="src">Sources: ICAR-CITH, SKUAST-K survey (Nov 2026). Prices vary sharply by year, grade and market.</p>
<h2>Apple price and rate today</h2>
<p>Check today's apple rates on the government's <a href="https://agmarknet.gov.in/" rel="nofollow">Agmarknet</a> and <a href="https://enam.gov.in/" rel="nofollow">eNAM</a> portals. Key markets: Azadpur (Delhi), Sopore, Parwanoo and Solan.</p>"""
    qas = [("When is apple harvested in India?", "Gala in July–August (110–120 days after full bloom); Delicious 130–145 days after full bloom, mostly August–October depending on altitude."),
           ("What is apple yield per acre?", "Traditional orchards 2.5–4.5 t per acre; M.9 high-density orchards 12–18 t per acre and more by year 5."),
           ("What is the cost of a high-density apple orchard?", "About Rs 35–48 lakh per hectare (Rs 14–19.5 lakh per acre) in year one, with 50% state or MIDH subsidy available for high-density planting."),
           ("How long can apples be stored?", "6–9 months in CA storage at 0–1°C, 90–95% humidity and 1.5–2% oxygen and carbon dioxide.")]
    article("/harvest-storage-and-profit/", "Apple Harvest, Grading, Storage, Cost & Profit (India)", "Apple harvest timing, starch-iodine test, grades by size, CA storage, yield per acre, cost of traditional and M.9 high-density orchards and mandi prices.",
            "Apple harvest, storage, cost and profit", body, crumbs=HOME, qas=qas, srcs=[S[k] for k in ("nhb", "cith", "skuastk", "usda", "niti", "agm")])

    body = """<p>Apple Orchard India is a free guide for apple growers, published by <a href="https://www.gujaratbio.com/">Gujarat Bio Organics Pvt. Ltd.</a>, a manufacturer of organic fertilizers, biostimulants and biofertilizers in Bhavnagar, Gujarat, working with farmers since 2006, including apple growers in Himachal Pradesh and Jammu & Kashmir.</p>
<h2>Who writes it</h2><p>Pages are written and reviewed by Gafar Laiya, founder of Gujarat Bio Organics, with the company's field team.</p>
<h2>Where the information comes from</h2><p>Dr. Y.S. Parmar University of Horticulture & Forestry (Nauni), SKUAST-Kashmir, SKUAST-Jammu, ICAR-Central Institute of Temperate Horticulture, the National Horticulture Board, the Ministry of Agriculture, USDA FAS, the National Innovation Foundation, NITI Aayog and DPPQ&S/CIB&RC. Sources are listed on each page.</p>
<h2>Our rules</h2><ul><li>No yield promises; yields shown are research and good-orchard figures.</li><li>Pesticides are named by active ingredient only; doses come from the official spray schedule and label. Banned chemicals are flagged.</li><li>Our own products are clearly marked as ours.</li></ul>
<h2>Contact</h2><p>WhatsApp or call +91 99787 91167 · sales@gujaratbio.com</p>"""
    g["write"]("/about/", g["shell"]("/about/", "About Apple Orchard India | Gujarat Bio Organics", "Who publishes appleorchard.in, who writes it, where the information comes from and how to contact us.",
                                     "<h1>About Apple Orchard India</h1>" + body, crumbs=HOME, schemas=[{"@type": "AboutPage", "name": "About Apple Orchard India", "url": g["SITE"] + "/about/"}]))
