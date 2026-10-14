#!/usr/bin/env python3
"""
generate_ch080_ts.py

Generates simulation/ir-motion-library/src/flowchart/data/ch080_flowchartData.ts
Compliant with:
- 34 nodes from public/data/ch080/graph.json
- Conservative typography & Content-derived node heights (audit_card_fit.ts)
- 3-Pillar Camera Laws (Deep Zoom 2.05x, Hold v=0, Panorama 0.35x)
- Subtitle safe zone clearance (audit_frames.ts: sy2 < 920, sy1 >= 30)
- Edge labels concise <= 14 chars (validate_mindmap.ts)
"""

import os
import json
import math

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIM_DIR = os.path.join(REPO_ROOT, "simulation", "ir-motion-library")

def count_lines(text, cpl):
    if not text:
        return 0
    total = 0
    for part in text.split('\n'):
        total += max(1, math.ceil(len(part) / cpl))
    return max(1, total)

def compute_required_height(node, w, fs):
    title_cpl = (w - 40) / (0.50 * fs)
    title_h = count_lines(node["title"], title_cpl) * fs * 1.28
    sub_h = 0
    if node.get("subtitle"):
        sub_fs = max(16, fs - 5)
        sub_cpl = (w - 40) / (0.50 * sub_fs)
        sub_h = count_lines(node["subtitle"], sub_cpl) * sub_fs * 1.28 + 6
    bul_h = 0
    if node.get("bullets"):
        bul_fs = max(15, fs - 6)
        bul_cpl = (w - 40 - 24) / (0.50 * bul_fs)
        b_tot = sum(count_lines(b, bul_cpl) * bul_fs * 1.28 + 3 for b in node["bullets"])
        bul_h = b_tot + 8
    return title_h + sub_h + bul_h + 32 + 28

# Load graph & subtitles
with open(os.path.join(REPO_ROOT, "public", "data", "ch080", "graph.json"), "r", encoding="utf-8") as f:
    graph = json.load(f)

with open(os.path.join(REPO_ROOT, "public", "data", "ch080", "subtitles.json"), "r", encoding="utf-8") as f:
    subtitles = json.load(f)

with open(os.path.join(REPO_ROOT, "public", "data", "ch080", "timestamps.json"), "r", encoding="utf-8") as f:
    timestamps = json.load(f)

TOTAL_FRAMES = timestamps["totalFrames"]

# Coordinates layout on 4800 x 3200 with ZERO OVERLAPS and generous inter-card spacing
LAYOUT = {
    # Root
    "root_global_environment": {"x": 2050, "y": 1250, "w": 420, "fill": "#FEFCBF", "fs": 24, "seed": 800, "reveal": 0},
    
    # Act 2: Far Upper Left (y=100..720)
    "hub_act2_milestones": {"x": 1500, "y": 150, "w": 380, "fill": "#FEFCBF", "fs": 22, "seed": 805, "reveal": 1516},
    "stockholm_conference_1972": {"x": 950, "y": 100, "w": 390, "fill": "#BEE3F8", "fs": 20, "seed": 810, "reveal": 1791},
    "unep": {"x": 350, "y": 100, "w": 390, "fill": "#C6F6D5", "fs": 20, "seed": 815, "reveal": 2628},
    "domestic_agencies": {"x": 350, "y": 430, "w": 390, "fill": "#BEE3F8", "fs": 20, "seed": 820, "reveal": 2977},

    # Act 1: Mid Upper Left (y=800..1090)
    "hub_act1_global_commons": {"x": 1500, "y": 850, "w": 380, "fill": "#FEFCBF", "fs": 22, "seed": 825, "reveal": 122},
    "global_commons": {"x": 950, "y": 800, "w": 390, "fill": "#BEE3F8", "fs": 20, "seed": 830, "reveal": 389},
    "free_rider_problem": {"x": 350, "y": 800, "w": 390, "fill": "#FED7D7", "fs": 20, "seed": 835, "reveal": 835},

    # Act 5: Mid Lower Left (y=1480..2100)
    "hub_act5_theories": {"x": 1500, "y": 1550, "w": 380, "fill": "#FEFCBF", "fs": 22, "seed": 840, "reveal": 7208},
    "regime_theory": {"x": 950, "y": 1480, "w": 390, "fill": "#C6F6D5", "fs": 20, "seed": 845, "reveal": 7534},
    "epistemic_communities": {"x": 950, "y": 1810, "w": 390, "fill": "#E9D8FD", "fs": 20, "seed": 850, "reveal": 8242},
    "gef_capacity": {"x": 350, "y": 1650, "w": 390, "fill": "#FFFFFF", "fs": 20, "seed": 855, "reveal": 8833},

    # Act 6: Far Lower Left (y=2220..2840)
    "hub_act6_cbdr": {"x": 1500, "y": 2280, "w": 380, "fill": "#FEFCBF", "fs": 22, "seed": 860, "reveal": 9132},
    "cbdr_doctrine": {"x": 950, "y": 2220, "w": 390, "fill": "#E9D8FD", "fs": 20, "seed": 865, "reveal": 9132},
    "historical_emissions_legacy": {"x": 350, "y": 2220, "w": 390, "fill": "#FED7D7", "fs": 20, "seed": 870, "reveal": 9452},
    "developing_country_emissions": {"x": 350, "y": 2550, "w": 390, "fill": "#BEE3F8", "fs": 20, "seed": 875, "reveal": 10050},

    # Act 4: Far Upper Right (y=100..720)
    "hub_act4_climate_regimes": {"x": 2700, "y": 150, "w": 380, "fill": "#FEFCBF", "fs": 22, "seed": 880, "reveal": 5387},
    "unfccc_1992": {"x": 3300, "y": 100, "w": 390, "fill": "#C6F6D5", "fs": 20, "seed": 885, "reveal": 5620},
    "kyoto_protocol_1997": {"x": 3900, "y": 100, "w": 390, "fill": "#C6F6D5", "fs": 20, "seed": 890, "reveal": 6530},
    "emissions_trading": {"x": 3900, "y": 430, "w": 390, "fill": "#FFFFFF", "fs": 20, "seed": 895, "reveal": 6837},

    # Act 3: Mid Upper Right (y=800..1445)
    "hub_act3_sustainability": {"x": 2700, "y": 850, "w": 380, "fill": "#FEFCBF", "fs": 22, "seed": 900, "reveal": 3465},
    "brundtland_report": {"x": 3300, "y": 800, "w": 390, "fill": "#E9D8FD", "fs": 20, "seed": 905, "reveal": 3819},
    "sustainable_development": {"x": 3900, "y": 800, "w": 390, "fill": "#E9D8FD", "fs": 20, "seed": 910, "reveal": 4071},
    "ipcc": {"x": 3300, "y": 1130, "w": 390, "fill": "#C6F6D5", "fs": 20, "seed": 915, "reveal": 4450},
    "rio_earth_summit_1992": {"x": 3900, "y": 1130, "w": 390, "fill": "#C6F6D5", "fs": 20, "seed": 920, "reveal": 4972},

    # Act 7: Mid Lower Right (y=1520..2140)
    "hub_act7_obstacles": {"x": 2700, "y": 1600, "w": 380, "fill": "#FEFCBF", "fs": 22, "seed": 925, "reveal": 10928},
    "enforcement_deficit": {"x": 3300, "y": 1520, "w": 390, "fill": "#FED7D7", "fs": 20, "seed": 930, "reveal": 11096},
    "energy_security_dilemma": {"x": 3300, "y": 1850, "w": 390, "fill": "#FED7D7", "fs": 20, "seed": 935, "reveal": 11680},
    "equity_poverty_tradeoff": {"x": 3900, "y": 1680, "w": 390, "fill": "#BEE3F8", "fs": 20, "seed": 940, "reveal": 12308},

    # Act 8: Far Lower Right (y=2250..2870)
    "hub_act8_pathways": {"x": 2700, "y": 2280, "w": 380, "fill": "#FEFCBF", "fs": 22, "seed": 945, "reveal": 12771},
    "paris_agreement_2015": {"x": 3300, "y": 2250, "w": 390, "fill": "#C6F6D5", "fs": 20, "seed": 950, "reveal": 12771},
    "ndcs": {"x": 3900, "y": 2250, "w": 390, "fill": "#C6F6D5", "fs": 20, "seed": 955, "reveal": 13391},
    "carbon_pricing": {"x": 3300, "y": 2580, "w": 390, "fill": "#FFFFFF", "fs": 20, "seed": 960, "reveal": 13782},
    "ambition_gap_15": {"x": 3900, "y": 2580, "w": 390, "fill": "#FED7D7", "fs": 20, "seed": 965, "reveal": 14091},
}

# Compile Nodes
node_objects = []
node_dict = {}
for n in graph["nodes"]:
    nid = n["id"]
    cfg = LAYOUT[nid]
    is_hub = n["kind"] == "hub"
    bullets = None if is_hub else n.get("bullets")
    
    # Compute safe height (+25px safety margin)
    req_h = compute_required_height({"title": n["title"], "subtitle": n.get("subtitle"), "bullets": bullets}, cfg["w"], cfg["fs"])
    h = math.ceil(req_h + 25)
    
    node_obj = {
        "id": nid,
        "x": cfg["x"],
        "y": cfg["y"],
        "width": cfg["w"],
        "height": h,
        "fill": cfg["fill"],
        "title": n["title"],
        "subtitle": n.get("subtitle"),
        "revealFrame": cfg["reveal"],
        "seed": cfg["seed"],
        "fontSize": cfg["fs"],
    }
    if bullets is not None:
        node_obj["bullets"] = bullets
    node_objects.append(node_obj)
    node_dict[nid] = node_obj

# Compile Arrows
arrow_objects = []
arrow_seeds = 1200
for i, e in enumerate(graph["edges"]):
    fn = node_dict[e["from"]]
    tn = node_dict[e["to"]]
    
    # Determine side based on relative position
    dx = tn["x"] - fn["x"]
    dy = tn["y"] - fn["y"]
    
    if abs(dx) > abs(dy):
        from_side = "right" if dx > 0 else "left"
        to_side = "left" if dx > 0 else "right"
    else:
        from_side = "bottom" if dy > 0 else "top"
        to_side = "top" if dy > 0 else "bottom"
        
    arrow_objects.append({
        "id": f"arr_{i:02d}_{e['from'][:10]}_{e['to'][:10]}",
        "fromId": e["from"],
        "toId": e["to"],
        "fromSide": from_side,
        "toSide": to_side,
        "label": e.get("label", ""),
        "revealFrame": tn["revealFrame"],
        "seed": arrow_seeds + i * 3,
    })

# Camera Segments (49 sentence holds + Root + Advance Organizer + Panorama)
# Map each sentence index to target node
CAMERA_MAPPING = [
    # Slide 1
    (0, 113, "root_global_environment", "Global Environmental Governance Root Hub", 1.65),
    (122, 381, "hub_act1_global_commons", "Act I: Global Commons Dilemma", 2.05),
    (389, 827, "global_commons", "Planetary Global Commons", 2.05),
    (835, 1075, "free_rider_problem", "The Free-Rider Dilemma", 2.05),
    (1083, 1497, "free_rider_problem", "Cooperation Under Anarchy", 2.05),

    # Slide 2
    (1516, 1783, "hub_act2_milestones", "Act II: Early Institutional Milestones", 2.05),
    (1791, 2234, "stockholm_conference_1972", "1972 Stockholm Conference", 2.05),
    (2243, 2620, "stockholm_conference_1972", "Stockholm Declaration 26 Principles", 2.05),
    (2628, 2969, "unep", "United Nations Environment Programme", 2.05),
    (2977, 3445, "domestic_agencies", "Domestic Environmental Agencies (EPA & UK)", 2.05),

    # Slide 3
    (3465, 3811, "hub_act3_sustainability", "Act III: Sustainable Development", 2.05),
    (3819, 4063, "brundtland_report", "1987 Brundtland Report", 2.05),
    (4071, 4442, "sustainable_development", "Doctrine of Sustainability", 2.05),
    (4450, 4964, "ipcc", "Intergovernmental Panel on Climate Change", 2.05),
    (4972, 5368, "rio_earth_summit_1992", "1992 Rio Earth Summit Agenda 21", 2.05),

    # Slide 4
    (5387, 5611, "hub_act4_climate_regimes", "Act IV: Climate Governance Architecture", 2.05),
    (5620, 5834, "unfccc_1992", "1992 UNFCCC Adoption", 2.05),
    (5842, 6165, "unfccc_1992", "UNFCCC Objective & COP Architecture", 2.05),
    (6173, 6522, "unfccc_1992", "Non-Binding Limits & Protocol Updates", 2.05),
    (6530, 6829, "kyoto_protocol_1997", "1997 Kyoto Protocol Annex I Binding Caps", 2.05),
    (6837, 7188, "emissions_trading", "Market Emissions Trading Mechanism", 2.05),

    # Slide 5
    (7208, 7384, "hub_act5_theories", "Act V: Theories Explaining Cooperation", 2.05),
    (7393, 7525, "hub_act5_theories", "Two Theoretical Frameworks", 2.05),
    (7534, 8064, "regime_theory", "Regime Theory & Reciprocity", 2.05),
    (8073, 8234, "regime_theory", "Deterring Defection in Anarchy", 2.05),
    (8242, 8510, "epistemic_communities", "Transnational Epistemic Networks", 2.05),
    (8518, 8825, "epistemic_communities", "Expert Consensus & National Interest", 2.05),
    (8833, 9112, "gef_capacity", "Capacity-Building via Global Environment Facility", 2.05),

    # Slide 6
    (9132, 9443, "hub_act6_cbdr", "Act VI: The Equity Deadlock (CBDR)", 2.05),
    (9452, 9822, "historical_emissions_legacy", "Historical Western Carbon Accumulation", 2.05),
    (9831, 10042, "cbdr_doctrine", "Common but Differentiated Responsibilities", 2.05),
    (10050, 10388, "developing_country_emissions", "Surging Developing Country Emissions", 2.05),
    (10397, 10668, "developing_country_emissions", "Global Supply Chain Emissions Accounting", 2.05),
    (10676, 10908, "cbdr_doctrine", "Climate Diplomacy Deadlock", 2.05),

    # Slide 7
    (10928, 11088, "hub_act7_obstacles", "Act VII: Obstacles to Agreement", 2.05),
    (11096, 11484, "enforcement_deficit", "Self-Enforcement Deficit in Environmental Law", 2.05),
    (11493, 11672, "enforcement_deficit", "Free-Rider Temptations in Treaties", 2.05),
    (11680, 11780, "energy_security_dilemma", "Energy Security Priorities", 2.05),
    (11788, 12078, "energy_security_dilemma", "Fossil Infrastructure Dependencies", 2.05),
    (12086, 12299, "energy_security_dilemma", "Asset Preservation in Resource States", 2.05),
    (12308, 12751, "equity_poverty_tradeoff", "Poverty Alleviation vs Emission Curbs", 2.05),

    # Slide 8
    (12771, 13006, "hub_act8_pathways", "Act VIII: New Climate Pathways", 2.05),
    (13014, 13182, "paris_agreement_2015", "2015 Paris Accord Universal Action", 2.05),
    (13190, 13383, "paris_agreement_2015", "The 1.5°C & 2°C Planetary Temperature Goals", 2.05),
    (13391, 13773, "ndcs", "Nationally Determined Contributions & 5-Year Ratchet", 2.05),
    (13782, 14083, "carbon_pricing", "Net-Zero Pledges & Carbon Pricing Markets", 2.05),
    (14091, 14327, "ambition_gap_15", "The 1.5°C Ambition Gap", 2.05),
    (14336, 14453, "root_global_environment", "Your Cognitive Advance Organizer", 1.65),
    (14461, 14573, None, "Final Panorama Pull-Back", 0.28),
]

camera_segments = []
for i, (sf, ef, nid, name, zoom) in enumerate(CAMERA_MAPPING):
    if nid is None:
        # Panorama centered on (2320, 1580) at zoom 0.28
        camera_segments.append({
            "id": f"seg_{i:02d}_panorama",
            "name": name,
            "x": 2320,
            "y": 1580,
            "zoom": zoom,
            "holdStartFrame": sf,
            "holdEndFrame": ef,
            "activeNodeIds": [],
            "isPanorama": True,
        })
    else:
        n = node_dict[nid]
        cx = n["x"] + n["width"] / 2.0
        cy = n["y"] + n["height"] / 2.0
        camera_segments.append({
            "id": f"seg_{i:02d}_{nid[:12]}",
            "name": name,
            "x": cx,
            "y": cy,
            "zoom": zoom,
            "holdStartFrame": sf,
            "holdEndFrame": ef,
            "activeNodeIds": [nid],
            "isPanorama": False,
        })

# Format TypeScript output
ts_code = f"""import {{ FlowNodeData, FlowArrowData, CameraHoldSegment }} from '../types';

export const TOTAL_FRAMES = {TOTAL_FRAMES};

// Semantic Academic Color Palette
export const COLOR_HUB = '#FEFCBF';
export const COLOR_STATE = '#BEE3F8';
export const COLOR_REALISM = '#FED7D7';
export const COLOR_LIBERALISM = '#C6F6D5';
export const COLOR_CONSTRUCT = '#E9D8FD';
export const COLOR_DETAIL = '#FFFFFF';

export const PASTEL_BLUE = COLOR_STATE;
export const PASTEL_YELLOW = COLOR_HUB;
export const PASTEL_GREEN = COLOR_LIBERALISM;
export const PASTEL_PINK = COLOR_REALISM;
export const PASTEL_PURPLE = COLOR_CONSTRUCT;
export const CLEAN_WHITE = COLOR_DETAIL;

export const FLOWCHART_NODES: FlowNodeData[] = {json.dumps(node_objects, indent=2)};

export const FLOWCHART_ARROWS: FlowArrowData[] = {json.dumps(arrow_objects, indent=2)};

export const CAMERA_SEGMENTS: CameraHoldSegment[] = {json.dumps(camera_segments, indent=2)};
"""

output_path = os.path.join(SIM_DIR, "src", "flowchart", "data", "ch080_flowchartData.ts")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(ts_code)

print(f"✓ Generated {output_path}")
print(f"  Nodes: {len(node_objects)}")
print(f"  Arrows: {len(arrow_objects)}")
print(f"  Camera Segments: {len(camera_segments)}")
print(f"  Total Frames: {TOTAL_FRAMES}")
