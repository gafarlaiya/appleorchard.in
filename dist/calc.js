/* Apple orchard fertilizer calculator (appleorchard.in).
   Logic from the research reference, section 17: Dr. YSP UHF Nauni age-scaled doses (standard: 70:35:70 g x age up to 10 years,
   FYM 10 kg x age; M.9 high density: 35:17.5:35 g x age up to 7 years), Soil Health Card +/-25%, off-year brake on post-bloom N,
   CAN instead of urea in acidic soil, M.9 N cap 245 g/tree, SKUAST-K Karewa ceiling warning. Pure functions first, then page wiring. */
(function (root) {
  "use strict";
  var UNITS = {
    acre: { m2: 4046.86, label: "Acre" }, ha: { m2: 10000, label: "Hectare" },
    bigha: { m2: 809.37, label: "Bigha, Himachal (5 per acre)" }, kanal: { m2: 505.86, label: "Kanal, J&K (8 per acre)" },
    nali: { m2: 200.67, label: "Nali, Uttarakhand (20.16 per acre)" }
  };
  var G = {
    urea: { n: 0.46, bag: 45, name: "Urea (46% N)" }, can: { n: 0.25, bag: 50, name: "CAN (25% N)" },
    ssp: { p: 0.16, bag: 50, name: "SSP (16% P₂O₅)" }, mop: { k: 0.60, bag: 50, name: "MOP (60% K₂O)" },
    map: { n: 0.12, p: 0.61, bag: 25, name: "MAP 12:61:00" }, sop: { k: 0.50, bag: 25, name: "SOP 0:0:50" }
  };
  var LEVEL = { low: 1.25, med: 1, high: 0.75 };
  var LOAD = { normal: 1, light: 0.5, none: 0, shoots: 0.5 };   // multiplier on post-bloom N only
  function round(x, d) { var f = Math.pow(10, d || 0); return Math.round(x * f) / f; }

  function calculate(inp) {
    var hdp = inp.system === "hdp";
    var age = Math.max(1, Math.floor(inp.age || 1));
    var eff = Math.min(age, hdp ? 7 : 10);
    var base = hdp ? { n: 35 * eff, p: 17.5 * eff, k: 35 * eff } : { n: 70 * eff, p: 35 * eff, k: 70 * eff };
    var g = { n: base.n * LEVEL[inp.soilN || "med"], p: base.p * LEVEL[inp.soilP || "med"], k: base.k * LEVEL[inp.soilK || "med"] };
    var alerts = [];
    if (!hdp) { g.n = Math.min(g.n, 700); g.p = Math.min(g.p, 350); g.k = Math.min(g.k, 700); }
    if (hdp && g.n > 245) { g.n = 245; alerts.push({ t: "warn", k: "m9cap" }); }
    var areaM2 = inp.area * UNITS[inp.unit].m2;
    var trees = inp.trees > 0 ? Math.round(inp.trees) : Math.round(areaM2 / (inp.row * inp.plant));
    var fymKg = trees * (hdp ? Math.min(20, Math.max(5, 3 * eff)) : 10 * eff);   // HDP research range 5-20 kg/tree; standard 10 kg x age
    var tot = { n: g.n * trees / 1000, p: g.p * trees / 1000, k: g.k * trees / 1000 };
    var acid = inp.ph && inp.ph < 5.5;
    var nSrc = acid ? "can" : "urea";
    if (acid) alerts.push({ t: "warn", k: "acid" });
    var mult = LOAD[inp.load || "normal"];
    if (mult < 1) alerts.push({ t: "info", k: "offyear" });
    var stages = [], prod = {};
    if (hdp && inp.irrigation === "drip") {
      prod.map = tot.p / G.map.p;
      prod.sop = tot.k / G.sop.k;
      var nFromMap = prod.map * G.map.n;
      prod.urea = Math.max(0, tot.n - nFromMap) / G.urea.n;
      if (acid) { prod.can = prod.urea * G.urea.n / G.can.n; delete prod.urea; }
      var nk = acid ? "can" : "urea";
      stages.push({ when: "Nov–Dec (late autumn)", items: [["fym", fymKg]] });
      stages.push({ when: "15 weekly drip doses, mid-March to end of June", weekly: true,
                    items: [["map", prod.map / 15], [nk, prod[nk] / 15], ["sop", prod.sop / 15]] });
      if (mult < 1) stages.push({ when: "Off-year / excess shoots", note: "Cut the May–June drip nitrogen by " + Math.round((1 - mult) * 100) + "% and watch shoot length (30–45 cm is right)." });
      nSrc = nk;
    } else {
      prod.ssp = tot.p / G.ssp.p;
      prod.mop = tot.k / G.mop.k;
      var nKg = tot.n / G[nSrc].n;
      var pre = nKg * 0.6, post = nKg * 0.4 * mult;
      prod[nSrc] = pre + post;
      stages.push({ when: "Nov–Dec (late autumn), in a ring 30 cm inside the drip line", items: [["fym", fymKg], ["ssp", prod.ssp], ["mop", prod.mop * 0.5]] });
      stages.push({ when: "Feb–Mar (2–3 weeks before bud break)", items: [[nSrc, pre]] });
      stages.push({ when: "Apr–May (after petal fall)", items: [[nSrc, post], ["mop", prod.mop * 0.5]] });
    }
    var nPerHa = tot.n / (areaM2 / 10000);
    if (hdp && nPerHa > 120) alerts.push({ t: "info", k: "karewa", v: round(nPerHa) });
    alerts.push({ t: "info", k: "tank" });
    return { trees: trees, eff: eff, age: age, perTree: g, tot: tot, fymKg: fymKg, prod: prod, stages: stages, alerts: alerts, nSrc: nSrc, hdp: hdp };
  }

  var api = { UNITS: UNITS, G: G, calculate: calculate, round: round };
  if (typeof module !== "undefined" && module.exports) { module.exports = api; return; }
  root.AppleCalc = api;

  var $ = function (id) { return document.getElementById(id); };
  if (!$("calc")) return;
  var SP = { s75: [7.5, 7.5], s6: [6, 6], s5: [5, 5], s4: [4, 4], s35: [3.5, 3.5], s3: [3, 3], h315: [3, 1.5], h31: [3, 1], h351: [3.5, 1] };
  var NAMES = { fym: "FYM", urea: G.urea.name, can: G.can.name, ssp: G.ssp.name, mop: G.mop.name, map: G.map.name, sop: G.sop.name };
  var MSG = {
    acid: "Soil pH is below 5.5 (acidic), so nitrogen is given as CAN instead of urea. Get a lime or dolomite recommendation from your soil test.",
    offyear: "Light crop or strong shoot growth: the post-bloom nitrogen is reduced so trees do not throw wild shoots instead of fruit buds.",
    m9cap: "Nitrogen for M.9 trees is capped at 245 g per tree per year.",
    karewa: "This is above the 45–120 kg N per hectare that SKUAST-K found enough on fertile Karewa soils. If shoots grow longer than 50 cm, cut the June nitrogen.",
    tank: "Never mix calcium chloride or calcium nitrate with sulphates (SOP, magnesium, zinc sulphate) or phosphates (MAP, 19:19:19) in one tank. Do not spray calcium chloride above 28–30°C."
  };
  function fmt(x) { return x >= 100 ? Math.round(x).toLocaleString("en-IN") : round(x, 1).toLocaleString("en-IN"); }
  function read() {
    var sp = SP[$("spacing").value] || [+$("rowm").value || 3, +$("plantm").value || 3];
    return { system: $("system").value, age: +$("age").value || 1, area: +$("area").value || 1, unit: $("unit").value,
             row: sp[0], plant: sp[1], trees: +$("trees").value || 0, irrigation: $("irr").value, load: $("load").value,
             soilN: $("soiln").value, soilP: $("soilp").value, soilK: $("soilk").value, ph: $("ph").value ? +$("ph").value : null };
  }
  function render() {
    $("customsp").hidden = $("spacing").value !== "custom";
    var inp = read(), r = calculate(inp), h = "";
    h += '<div class="res-top"><div><b>' + r.trees.toLocaleString("en-IN") + '</b><span>trees</span></div><div><b>' + fmt(r.tot.n) + '</b><span>kg N</span></div>' +
         '<div><b>' + fmt(r.tot.p) + '</b><span>kg P₂O₅</span></div><div><b>' + fmt(r.tot.k) + '</b><span>kg K₂O</span></div></div>';
    h += '<p class="res-note">Per tree (age ' + r.age + (r.age > r.eff ? ', dosed as ' + r.eff + ' years' : '') + '): ' + round(r.perTree.n) + ' g N, ' + round(r.perTree.p) + ' g P₂O₅, ' + round(r.perTree.k) + ' g K₂O, ' +
         round(r.fymKg / r.trees) + ' kg FYM. ' + (r.hdp ? "M.9 high-density dose (Dr. YSP UHF: half the standard dose per year of age, up to 7 years)." : "Standard dose (Dr. YSP UHF / SKUAST-K: 70:35:70 g per year of age, full dose from year 10).") + '</p>';
    r.alerts.forEach(function (a) { h += '<p class="alert alert-' + a.t + '">' + MSG[a.k] + (a.k === "karewa" ? " (Your plan: " + a.v + " kg N/ha.)" : "") + '</p>'; });
    h += '<h3>Totals for the year</h3><table class="tbl"><tr><th>Product</th><th>Total</th></tr><tr><td>FYM</td><td>' + round(r.fymKg / 1000, 1) + ' tonnes</td></tr>';
    Object.keys(r.prod).forEach(function (k) { h += '<tr><td>' + NAMES[k] + '</td><td>' + fmt(r.prod[k]) + ' kg (' + round(r.prod[k] / G[k].bag, 1) + ' bags of ' + G[k].bag + ' kg)</td></tr>'; });
    h += '</table><h3>When to apply</h3><table class="tbl"><tr><th>When</th><th>What</th></tr>';
    r.stages.forEach(function (s) {
      var body = s.note || s.items.filter(function (i) { return i[1] > 0.05; }).map(function (i) { return NAMES[i[0]] + ": " + (i[0] === "fym" ? round(i[1] / 1000, 1) + " t" : fmt(i[1]) + " kg" + (s.weekly ? " per week" : "")); }).join("<br>");
      h += '<tr><td>' + s.when + '</td><td>' + (body || "None this year") + '</td></tr>';
    });
    h += '</table><p class="res-note">Sprays on top of this plan: boron 0.1–0.15% at pink bud; 4–6 calcium chloride sprays (0.3–0.5%) from 2–3 weeks after petal fall; 3–5% urea + 0.5% zinc sulphate + 0.1–0.2% boron on green leaves in October–November. No sprays at full bloom.</p>';
    $("result").innerHTML = h;
    var wa = "Apple fertilizer plan: " + inp.area + " " + UNITS[inp.unit].label + ", " + r.trees + " trees, age " + r.age + ", " + (r.hdp ? "M.9 HDP" : "standard") + ". N " + fmt(r.tot.n) + " kg, P " + fmt(r.tot.p) + " kg, K " + fmt(r.tot.k) + " kg. Please check my plan.";
    $("wa").href = "https://wa.me/919978791167?text=" + encodeURIComponent(wa);
  }
  $("system").addEventListener("change", function () {
    var h = $("system").value === "hdp"; $("spacing").value = h ? "h315" : "s6"; $("irr").value = h ? "drip" : "basin"; render();
  });
  $("calc").addEventListener("input", render); $("calc").addEventListener("change", render); render();
})(typeof window !== "undefined" ? window : this);
