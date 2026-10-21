// Nudge each land-bound route vertex to the nearest water point, then rewrite the route arrays in bake_geo.js.
const fs = require("fs");
global.window = {};
require("./data/countries.js");
const geo = global.window.WORLD_GEOJSON;

const rad = Math.PI / 180;
const FOCUS = ["Malaysia", "Indonesia", "Singapore", "Thailand"];
const rings = [];
for (const f of geo.features) {
  if (!FOCUS.includes(f.properties.name)) continue;
  const g = f.geometry;
  const polys = g.type === "Polygon" ? [g.coordinates] : g.type === "MultiPolygon" ? g.coordinates : [];
  for (const poly of polys) for (const ring of poly) rings.push(ring);
}
function inside(lon, lat, ring) {
  let hit = false;
  for (let i = 0, j = ring.length - 1; i < ring.length; j = i++) {
    const [xi, yi] = ring[i], [xj, yj] = ring[j];
    if (((yi > lat) !== (yj > lat)) && (lon < ((xj - xi) * (lat - yi)) / (yj - yi) + xi)) hit = !hit;
  }
  return hit;
}
function isLand(lon, lat) { return rings.some(r => inside(lon, lat, r)); }

function nearestWater(lon, lat, maxR = 2.4) {
  if (!isLand(lon, lat)) return [lon, lat, 0];
  let best = null;
  for (let r = 0.05; r <= maxR; r += 0.05) {
    for (let a = 0; a < 360; a += 10) {
      const lo = lon + r * Math.cos(a * rad), la = lat + r * Math.sin(a * rad);
      if (!isLand(lo, la)) {
        const d = Math.hypot(lo - lon, la - lat);
        if (!best || d < best[2]) best = [lo, la, d];
      }
    }
    if (best) break;
  }
  return best || [lon, lat, -1];
}

const LANE = [[93.5, 6.0], [96.5, 5.2], [99.0, 4.0], [101.2, 3.0], [102.8, 2.0],
              [103.85, 1.24], [104.9, 1.55], [106.0, 2.2], [107.6, 3.4], [109.6, 5.0], [112.0, 6.6]];
const SUNDA = [[103.85, 1.24], [102.0, -0.6], [100.6, -3.0], [101.4, -5.4], [103.4, -5.9],
               [105.4, -5.9], [105.9, -6.0], [106.6, -4.0], [107.6, -1.6], [108.6, 0.8], [110.0, 3.2]];
const LOMBOK = [[103.85, 1.24], [101.4, -1.6], [99.6, -4.8], [101.8, -8.2], [106.0, -9.0],
                [111.0, -8.9], [115.9, -8.7], [117.4, -6.4], [118.0, -3.6], [118.5, -1.0],
                [119.6, 1.6], [121.4, 4.2]];

const fix = (name, arr) => arr.map(([lo, la]) => {
  const [nlo, nla, d] = nearestWater(lo, la);
  if (d > 0) console.log(`${name}: [${lo}, ${la}] land -> [${nlo.toFixed(2)}, ${nla.toFixed(2)}] (moved ${d.toFixed(2)}°)`);
  return [Number(nlo.toFixed(2)), Number(nla.toFixed(2))];
});

const L2 = fix("lane", LANE), S2 = fix("sunda", SUNDA), K2 = fix("lombok", LOMBOK);

const fmt = a => "[" + a.map(([x, y]) => `[${x}, ${y}]`).join(", ") + "]";
let src = fs.readFileSync("./bake_geo.js", "utf8");
src = src.replace(/const LANE = \[[\s\S]*?\];/, `const LANE = ${fmt(L2)};`);
src = src.replace(/const SUNDA = \[[\s\S]*?\];/, `const SUNDA = ${fmt(S2)};`);
src = src.replace(/const LOMBOK = \[[\s\S]*?\];/, `const LOMBOK = ${fmt(K2)};`);
fs.writeFileSync("./bake_geo.js", src);
console.log("bake_geo.js rewritten");
