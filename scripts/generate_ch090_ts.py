#!/usr/bin/env python3
"""
generate_ch090_ts.py

Generates simulation/ir-motion-library/src/flowchart/data/ch090_flowchartData.ts
Compliant with:
- 29 nodes from public/data/ch090/graph.json
- Conservative typography & Content-derived node heights (audit_card_fit.ts)
- 3-Pillar Camera Laws (Deep Zoom 2.05x, Hold v=0, Panorama <= 0.33x)
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

# Load graph, subtitles & timestamps
with open(os.path.join(REPO_ROOT, "public", "data", "ch090", "graph.json"), "r", encoding="utf-8") as f:
    graph = json.load(f)

with open(os.path.join(REPO_ROOT, "public", "data", "ch090", "subtitles.json"), "r", encoding="utf-8") as f:
    subtitles = json.load(f)

with open(os.path.join(REPO_ROOT, "public", "data", "ch090", "timestamps.json"), "r", encoding="utf-8") as f:
    timestamps = json.load(f)

TOTAL_FRAMES = timestamps["totalFrames"]

# Coordinates layout on 4800 x 3200 with ZERO OVERLAPS and generous inter-card spacing
# Color palette:
# FEFCBF = hub/root
# BEE3F8 = state / traditional
# FED7D7 = realism / violence / threats / warning
# C6F6D5 = institutions / treaties
# E9D8FD = social constructivism / norms / critical
# FFFFFF = detail / mechanism
LAYOUT = {
    # Root (center x=2150..2600, y=1250..1550)
    "root_global_security": {"x": 2180, "y": 1280, "w": 440, "fill": "#FEFCBF", "fs": 24, "seed": 900, "reveal": 0},
    
    # Act 2: Far Upper Left (y=100..750)
    "hub_act2_traditional_security": {"x": 1450, "y": 180, "w": 400, "fill": "#FEFCBF", "fs": 22, "seed": 905, "reveal": 1595},
    "traditional_national_security": {"x": 880, "y": 120, "w": 420, "fill": "#FED7D7", "fs": 20, "seed": 910, "reveal": 1767},
    "balance_of_power_deterrence": {"x": 280, "y": 120, "w": 420, "fill": "#FED7D7", "fs": 20, "seed": 915, "reveal": 2406},

    # Act 1: Mid Upper Left (y=780..1180)
    "hub_act1_changing_security": {"x": 1450, "y": 820, "w": 400, "fill": "#FEFCBF", "fs": 22, "seed": 920, "reveal": 284},
    "multidimensional_security": {"x": 880, "y": 760, "w": 420, "fill": "#BEE3F8", "fs": 20, "seed": 925, "reveal": 1117},
    "transnational_threats": {"x": 280, "y": 760, "w": 420, "fill": "#FED7D7", "fs": 20, "seed": 930, "reveal": 398},

    # Act 5: Mid Lower Left (y=1500..2000)
    "hub_act5_critical_security": {"x": 1450, "y": 1560, "w": 400, "fill": "#FEFCBF", "fs": 22, "seed": 935, "reveal": 5980},
    "critical_security_studies": {"x": 880, "y": 1500, "w": 420, "fill": "#E9D8FD", "fs": 20, "seed": 940, "reveal": 5980},
    "state_as_insecurity_source": {"x": 280, "y": 1500, "w": 420, "fill": "#FED7D7", "fs": 20, "seed": 945, "reveal": 6463},

    # Act 6: Far Lower Left (y=2180..2900)
    "hub_act6_feminist_security": {"x": 1450, "y": 2240, "w": 400, "fill": "#FEFCBF", "fs": 22, "seed": 950, "reveal": 7486},
    "feminist_security_theory": {"x": 880, "y": 2180, "w": 420, "fill": "#E9D8FD", "fs": 20, "seed": 955, "reveal": 7486},
    "everyday_gendered_violence": {"x": 280, "y": 2180, "w": 420, "fill": "#FED7D7", "fs": 20, "seed": 960, "reveal": 7765},
    "globalization_flow_perspective": {"x": 880, "y": 2540, "w": 420, "fill": "#C6F6D5", "fs": 20, "seed": 965, "reveal": 8585},
    "geopolitics_territorial_control": {"x": 280, "y": 2540, "w": 420, "fill": "#FED7D7", "fs": 20, "seed": 970, "reveal": 8585},

    # Act 4: Far Upper Right (y=100..750)
    "hub_act4_constructivist_security": {"x": 2850, "y": 180, "w": 400, "fill": "#FEFCBF", "fs": 22, "seed": 975, "reveal": 4536},
    "constructivist_social_structure": {"x": 3450, "y": 120, "w": 420, "fill": "#E9D8FD", "fs": 20, "seed": 980, "reveal": 4536},
    "security_community": {"x": 4050, "y": 120, "w": 420, "fill": "#C6F6D5", "fs": 20, "seed": 985, "reveal": 5351},

    # Act 3: Mid Upper Right (y=780..1180)
    "hub_act3_liberal_security": {"x": 2850, "y": 820, "w": 400, "fill": "#FEFCBF", "fs": 22, "seed": 990, "reveal": 3031},
    "liberal_institutional_security": {"x": 3450, "y": 760, "w": 420, "fill": "#C6F6D5", "fs": 20, "seed": 995, "reveal": 3031},
    "iterated_reciprocity": {"x": 4050, "y": 760, "w": 420, "fill": "#FFFFFF", "fs": 20, "seed": 1000, "reveal": 3662},

    # Act 7: Mid Lower Right (y=1500..2000)
    "hub_act7_drc_humanitarian": {"x": 2850, "y": 1560, "w": 400, "fill": "#FEFCBF", "fs": 22, "seed": 1005, "reveal": 9122},
    "drc_conflict_humanitarian_crisis": {"x": 3450, "y": 1500, "w": 420, "fill": "#FED7D7", "fs": 20, "seed": 1010, "reveal": 9122},
    "limits_of_military_power": {"x": 4050, "y": 1500, "w": 420, "fill": "#BEE3F8", "fs": 20, "seed": 1015, "reveal": 10080},

    # Act 8: Far Lower Right (y=2180..2900)
    "hub_act8_nuclear_proliferation": {"x": 2850, "y": 2240, "w": 400, "fill": "#FEFCBF", "fs": 22, "seed": 1020, "reveal": 10690},
    "npt_1968": {"x": 3450, "y": 2180, "w": 420, "fill": "#C6F6D5", "fs": 20, "seed": 1025, "reveal": 10690},
    "dual_use_technology": {"x": 4050, "y": 2180, "w": 420, "fill": "#FFFFFF", "fs": 20, "seed": 1030, "reveal": 11333},
    "dprk_nuclear_proliferation": {"x": 3450, "y": 2540, "w": 420, "fill": "#FED7D7", "fs": 20, "seed": 1035, "reveal": 11634},
    "iran_nuclear_inspections": {"x": 4050, "y": 2540, "w": 420, "fill": "#FED7D7", "fs": 20, "seed": 1040, "reveal": 11985},
}

# Compile Nodes
node_objects = []
node_dict = {}
for n in graph["nodes"]:
    nid = n["id"]
    cfg = LAYOUT[nid]
    is_hub = n["kind"] == "hub"
    bullets = None if is_hub else n.get("bullets")
    
    # Compute safe height (+28px safety margin)
    req_h = compute_required_height({"title": n["title"], "subtitle": n.get("subtitle"), "bullets": bullets}, cfg["w"], cfg["fs"])
    h = math.ceil(req_h + 28)
    
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
arrow_seeds = 1400
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

# Camera Segments (48 sentence holds + Root + Panorama)
CAMERA_MAPPING = [
    # Slide 1 (7 sentences)
    (0, 275, "root_global_security", "Global Security Dynamics Root Hub", 1.65),
    (284, 389, "hub_act1_changing_security", "Act I: Changing Security Arena", 2.05),
    (398, 643, "transnational_threats", "Complex Transnational Dangers", 2.05),
    (651, 878, "transnational_threats", "Borderless Vulnerabilities", 2.05),
    (887, 1109, "transnational_threats", "Limits of Heavy Armor", 2.05),
    (1117, 1398, "multidimensional_security", "Multidimensional Security Dimensions", 2.05),
    (1406, 1576, "multidimensional_security", "Rethinking the Foundations of Defense", 2.05),

    # Slide 2 (6 sentences)
    (1595, 1758, "hub_act2_traditional_security", "Act II: Realist Orthodoxy", 2.05),
    (1767, 2002, "traditional_national_security", "Hobbesian Anarchic System", 2.05),
    (2010, 2245, "traditional_national_security", "Self-Help and Power Capabilities", 2.05),
    (2253, 2397, "traditional_national_security", "Military Compulsion to Deter Rivals", 2.05),
    (2406, 2714, "balance_of_power_deterrence", "Balance of Power and Alliances", 2.05),
    (2723, 3011, "balance_of_power_deterrence", "Institutional Limits under Anarchy", 2.05),

    # Slide 3 (6 sentences)
    (3031, 3192, "hub_act3_liberal_security", "Act III: Liberal Institutionalism", 2.05),
    (3201, 3449, "liberal_institutional_security", "Mitigating the Zero-Sum Trap", 2.05),
    (3458, 3653, "liberal_institutional_security", "UN, WTO, and NATO Multilateral Bodies", 2.05),
    (3662, 3968, "iterated_reciprocity", "Information, Transaction Costs, and Reciprocity", 2.05),
    (3977, 4272, "iterated_reciprocity", "Internalizing Cooperative Norms", 2.05),
    (4281, 4516, "liberal_institutional_security", "Positive-Sum Security Interdependence", 2.05),

    # Slide 4 (6 sentences)
    (4536, 4799, "hub_act4_constructivist_security", "Act IV: Constructivist Social Structures", 2.05),
    (4808, 5133, "constructivist_social_structure", "Wendtian Thesis: Anarchy is Socially Constructed", 2.05),
    (5142, 5342, "constructivist_social_structure", "Perception and the Security Dilemma", 2.05),
    (5351, 5589, "security_community", "Evolution of Shared Values and Trust", 2.05),
    (5598, 5842, "security_community", "Transnational Security Communities", 2.05),
    (5851, 5961, "security_community", "NATO Pluralistic Security Norms", 2.05),

    # Slide 5 (5 sentences)
    (5980, 6223, "hub_act5_critical_security", "Act V: Critical Security Studies", 2.05),
    (6232, 6454, "critical_security_studies", "Interrogating the State-Centric Blind Spot", 2.05),
    (6463, 6788, "state_as_insecurity_source", "The State as a Primary Source of Insecurity", 2.05),
    (6797, 7068, "state_as_insecurity_source", "Institutional Oppression under Defense Rhetoric", 2.05),
    (7077, 7466, "critical_security_studies", "Emancipating Human Beings and Communities", 2.05),

    # Slide 6 (5 sentences)
    (7486, 7756, "hub_act6_feminist_security", "Act VI: Feminist Security Theory", 2.05),
    (7765, 8151, "everyday_gendered_violence", "Everyday Bodily Violence and Structural Threat", 2.05),
    (8160, 8438, "feminist_security_theory", "Women as Active Agents of Transformation", 2.05),
    (8447, 8684, "globalization_flow_perspective", "Globalization Versus Resurgent Geopolitics", 2.05),
    (8693, 9102, "geopolitics_territorial_control", "Strategic Competition for Territorial Space", 2.05),

    # Slide 7 (5 sentences)
    (9122, 9381, "hub_act7_drc_humanitarian", "Act VII: Humanitarian Catastrophe in the DRC", 2.05),
    (9390, 9694, "drc_conflict_humanitarian_crisis", "Rwandan Genocide Spillover and Regional Proxy War", 2.05),
    (9703, 10071, "drc_conflict_humanitarian_crisis", "Six Million Civilian Deaths and War Costs", 2.05),
    (10080, 10376, "limits_of_military_power", "Failure to Halt Child Soldiers and Mass Rape", 2.05),
    (10385, 10671, "limits_of_military_power", "Human Security Beyond Military Balance of Power", 2.05),

    # Slide 8 (8 sentences)
    (10690, 10899, "hub_act8_nuclear_proliferation", "Act VIII: Nuclear Governance and Proliferation", 2.05),
    (10908, 11324, "npt_1968", "1968 Nuclear Non-Proliferation Treaty Architecture", 2.05),
    (11333, 11467, "dual_use_technology", "Dual-Use Fuel Cycle Dilemmas", 2.05),
    (11476, 11625, "dual_use_technology", "Enrichment and Weapons-Grade Fissile Material", 2.05),
    (11634, 11776, "dprk_nuclear_proliferation", "Sovereign Defection and Agreed Framework Exit", 2.05),
    (11785, 11976, "dprk_nuclear_proliferation", "DPRK Nuclear Tests and Diplomacy Breakdown", 2.05),
    (11985, 12224, "iran_nuclear_inspections", "Iran Enrichment Controversies under IAEA Safeguards", 2.05),
    (12233, 12380, "root_global_security", "Cognitive Advance Organizer Review", 1.65),
    (12389, 12499, None, "Final Panorama Pull-Back", 0.28),
]

camera_segments = []
for i, (sf, ef, nid, name, zoom) in enumerate(CAMERA_MAPPING):
    if nid is None:
        # Panorama centered on (2350, 1500) at zoom 0.28 (safe from subtitles: sy2 < 905px, sy1 >= 90px)
        camera_segments.append({
            "id": f"seg_{i:02d}_panorama",
            "name": name,
            "x": 2350,
            "y": 1500,
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

output_path = os.path.join(SIM_DIR, "src", "flowchart", "data", "ch090_flowchartData.ts")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(ts_code)

print(f"✓ Generated {output_path}")
print(f"  Nodes: {len(node_objects)}")
print(f"  Arrows: {len(arrow_objects)}")
print(f"  Camera Segments: {len(camera_segments)}")
print(f"  Total Frames: {TOTAL_FRAMES}")
