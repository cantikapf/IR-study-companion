// Bake GeoJSON -> screen SVG paths. No d3, no network, deterministic.
// Run: node bake_geo.js
const fs = require("fs");
const path = require("path");

global.window = {};
require("./data/countries.js");
const geo = global.window.WORLD_GEOJSON;

const W = 1080, H = 1920;
// frame: Malacca + Nusantara sea lanes + Sunda/Lombok to the east
const CENTER = [104.0, -1.0];
const ZOOM = 1180; // px per unit of mercator-y at equator

const rad = Math.PI / 180;
function merc(lon, lat) {
  const x = lon * rad;
  const y = Math.log(Math.tan(Math.PI / 4 + (lat * rad) / 2));
  return [x, y];
}
const c = merc(CENTER[0], CENTER[1]);
function proj(lon, lat) {
  const m = merc(lon, lat);
  return [W / 2 + (m[0] - c[0]) * ZOOM, H / 2 - (m[1] - c[1]) * ZOOM];
}

const FOCUS = ["Malaysia", "Indonesia", "Singapore", "Thailand"];
const LABEL = { Malaysia: "MALAYSIA", Indonesia: "INDONESIA", Singapore: "SINGAPORE", Thailand: "THAILAND" };

// keep only rings whose bbox intersects the visible frame (with margin) -> drops overseas territories
const MX = 900, MY = 1200;
function ringInView(ring) {
  let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
  for (const [lon, lat] of ring) {
    const [x, y] = proj(lon, lat);
    if (x < x0) x0 = x; if (x > x1) x1 = x;
    if (y < y0) y0 = y; if (y > y1) y1 = y;
  }
  return !(x1 < -MX || x0 > W + MX || y1 < -MY || y0 > H + MY);
}
function ringToPath(ring) {
  let d = "";
  for (let i = 0; i < ring.length; i++) {
    const [x, y] = proj(ring[i][0], ring[i][1]);
    d += (i ? "L" : "M") + x.toFixed(1) + " " + y.toFixed(1);
  }
  return d + "Z";
}
function polys(feature) {
  const g = feature.geometry;
  if (!g) return [];
  if (g.type === "Polygon") return [g.coordinates];
  if (g.type === "MultiPolygon") return g.coordinates;
  return [];
}

const out = { view: { W, H, center: CENTER, zoom: ZOOM }, focus: {}, dim: [], bbox: {} };

for (const f of geo.features) {
  const name = f.properties && f.properties.name;
  if (!name) continue;
  const isFocus = FOCUS.includes(name);
  for (const poly of polys(f)) {
    const d = poly.filter(ringInView).map(ringToPath).join("");
    if (!d) continue;
    if (isFocus) {
      if (!out.focus[name]) out.focus[name] = { label: LABEL[name] || name.toUpperCase(), d: "" };
      out.focus[name].d += d;
    } else {
      out.dim.push(d);
    }
  }
}

// bbox for each focus country so labels can be anchored to the polygon centroid of the largest ring
for (const name of Object.keys(out.focus)) {
  const d = out.focus[name].d;
  const nums = d.match(/-?\d+\.?\d*/g).map(Number);
  let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
  for (let i = 0; i < nums.length; i += 2) {
    if (nums[i] < x0) x0 = nums[i]; if (nums[i] > x1) x1 = nums[i];
    if (nums[i + 1] < y0) y0 = nums[i + 1]; if (nums[i + 1] > y1) y1 = nums[i + 1];
  }
  out.bbox[name] = [x0, y0, x1, y1];
}

out.points = {
  phillips: proj(103.85, 1.24),
  singapore: proj(103.82, 1.35),
  sunda: proj(105.9, -6.0),
  lombok: proj(115.9, -8.7),
  makassar: proj(118.5, -1.0),
};
// label anchors: keep them on the visible part of each country, not the bbox centre
// (Indonesia's bbox spans Papua, so its centre lands in open sea)
out.labels = {
  INDONESIA: proj(101.6, -2.2),
  MALAYSIA: proj(102.4, 4.4),
};

// routes defined in lon/lat so they follow water, then projected
const LANE = [[93.5, 6], [95.6, 5.9], [99, 4], [101.2, 3], [102.61, 1.93], [103.85, 1.24], [104.9, 1.55], [106, 2.2], [107.6, 3.4], [109.6, 5], [112, 6.6]];
const SUNDA = [[103.85, 1.24], [103.5, -0.6], [100.6, -3], [101.4, -5.4], [103.4, -5.9], [105.4, -5.9], [105.9, -6], [106.6, -4], [107.6, -1.6], [108.6, 0.8], [110, 3.2]];
const LOMBOK = [[103.85, 1.24], [100.71, -1.72], [99.6, -4.8], [101.8, -8.2], [106, -9], [111, -8.9], [115.9, -8.7], [117.4, -6.4], [118, -3.6], [118.5, -1], [119.6, 1.6], [121.4, 4.2]];
const px = a => a.map(([lo, la]) => proj(lo, la).map(v => Math.round(v)));
out.routes = { lane: px(LANE), sunda: px(SUNDA), lombok: px(LOMBOK) };

const dst = path.join(__dirname, "compositions", "geo.json");
fs.writeFileSync(dst, JSON.stringify(out));
fs.writeFileSync(path.join(__dirname, "compositions", "geo.js"), "window.GEO=" + JSON.stringify(out) + ";");
console.log("focus:", Object.keys(out.focus).join(", "));
console.log("dim shapes:", out.dim.length);
console.log("bytes:", fs.statSync(dst).size);
console.log("phillips px:", out.points.phillips.map(v => v.toFixed(0)).join(","));
for (const k of Object.keys(out.bbox)) console.log(k, "bbox", out.bbox[k].map(v => v.toFixed(0)).join(","));
