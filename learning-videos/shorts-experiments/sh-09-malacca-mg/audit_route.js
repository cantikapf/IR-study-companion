// Point-in-polygon audit: which route vertices sit on land?
const fs = require("fs");
global.window = {};
require("./data/countries.js");
const geo = global.window.WORLD_GEOJSON;
const G = JSON.parse(fs.readFileSync("./compositions/geo.json", "utf8"));

const rad = Math.PI / 180;
function merc(lon, lat) {
  return [lon * rad, Math.log(Math.tan(Math.PI / 4 + (lat * rad) / 2))];
}
const c = merc(G.view.center[0], G.view.center[1]);
function unproj(x, y) {
  const mx = (x - 540) / G.view.zoom + c[0];
  const my = -(y - 960) / G.view.zoom + c[1];
  return [mx / rad, (2 * Math.atan(Math.exp(my)) - Math.PI / 2) / rad];
}

const FOCUS = ["Malaysia", "Indonesia", "Singapore", "Thailand"];
const rings = [];
for (const f of geo.features) {
  if (!FOCUS.includes(f.properties.name)) continue;
  const g = f.geometry;
  const polys = g.type === "Polygon" ? [g.coordinates] : g.type === "MultiPolygon" ? g.coordinates : [];
  for (const poly of polys) for (const ring of poly) rings.push({ name: f.properties.name, ring });
}

function inside(lon, lat, ring) {
  let hit = false;
  for (let i = 0, j = ring.length - 1; i < ring.length; j = i++) {
    const [xi, yi] = ring[i], [xj, yj] = ring[j];
    if (((yi > lat) !== (yj > lat)) && (lon < ((xj - xi) * (lat - yi)) / (yj - yi) + xi)) hit = !hit;
  }
  return hit;
}
function landAt(lon, lat) {
  for (const r of rings) if (inside(lon, lat, r.ring)) return r.name;
  return null;
}

for (const key of Object.keys(G.routes)) {
  console.log("\n== " + key);
  for (const [px, py] of G.routes[key]) {
    const [lon, lat] = unproj(px, py);
    const hit = landAt(lon, lat);
    console.log(`  [${lon.toFixed(2)}, ${lat.toFixed(2)}] px(${px},${py}) -> ${hit ? "ON LAND: " + hit : "water"}`);
  }
}
