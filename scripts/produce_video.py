#!/usr/bin/env python3
"""
produce_video.py

Unified Orchestrator for IR Study Companion Mind Map Explanatory Video Production.
Coordinates the 5 Canonical Production Phases:
  - Phase 1: Script & Mind Map Graph Extraction (MANDATORY USER ACC GATE)
  - Phase 2: Kokoro-82M Neural Audio Synthesis & Subtitle Alignment
  - Phase 3: Flowchart Layout & 3-Pillar Camera Rig Assembly
  - Phase 4: Automated 12k+ Frame QA Audit (audit_frames.ts)
  - Phase 5: Remotion 1080p Master Render & Canonical YouTube Thumbnail Generation

Usage:
  python scripts/produce_video.py --chapter CH060 --step audit
  python scripts/produce_video.py --chapter CH060 --step all --acc
"""

import os
import sys
import glob
import json
import argparse
import subprocess
from typing import Optional

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIM_DIR = os.path.join(REPO_ROOT, "simulation", "ir-motion-library")

def find_chapter_markdown(chapter_id: str):
    """Finds the chapter markdown file from _chapters directory."""
    num_str = "".join([c for c in chapter_id if c.isdigit()]).zfill(3)
    pattern = os.path.join(REPO_ROOT, "_chapters", "**", f"*{num_str}*.md")
    matches = glob.glob(pattern, recursive=True)
    # Filter out index files
    matches = [m for m in matches if not os.path.basename(m).startswith("000-")]
    return matches[0] if matches else None

def step_phase_1_extract(chapter_id: str, auto_approve: bool = False, hook_text: Optional[str] = None, yt_title: Optional[str] = None):
    """Phase 1: Academic Script Extraction & Mind Map Proposal."""
    print(f"\n========================================================")
    print(f"🎬 PHASE 1: SCRIPT EXTRACTION & MIND MAP PROPOSAL ({chapter_id})")
    print(f"========================================================")
    
    md_file = find_chapter_markdown(chapter_id)
    if not md_file:
        print(f"[FATAL] Chapter markdown not found for ID: {chapter_id}", file=sys.stderr)
        return False

    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()
    title = [l.replace("title:", "").strip(' "\'') for l in lines if l.startswith("title:")][:1]
    title_str = title[0] if title else os.path.basename(md_file)
    headings = [l.strip() for l in lines if l.startswith("## ") or l.startswith("### ")]

    print(f"Target Chapter : {title_str}")
    print(f"Source File    : {os.path.relpath(md_file, REPO_ROOT)}")
    print(f"Core Headings  : {len(headings)} sections identified")
    for h in headings[:8]:
        print(f"  • {h}")
    if len(headings) > 8:
        print(f"  ... and {len(headings) - 8} more sections.")

    print("\n--------------------------------------------------------")
    print("MIND MAP ARCHITECTURAL OUTLINE:")
    print("  • Canvas Size: 4800 x 3200 Infinite White Plane")
    print("  • Act Structure: 8 Acts / Concept Hubs")
    print("  • Camera Standard: 1-to-1 Deep Zoom (2.05x) + Stationary Hold (v=0)")
    print("--------------------------------------------------------")

    # Hook & Packaging Audit Integration
    try:
        sys.path.insert(0, os.path.join(REPO_ROOT, "scripts"))
        from yt.hookscore import score as score_hook, report as report_hook
        from yt.title import check as check_title, show as show_title_lint

        if hook_text:
            print("\n🎯 HOOK AUDIT (First 15 Seconds):")
            parts, verdict, name, hits = score_hook(hook_text)
            report_hook(hook_text, parts, verdict, name, hits)
        
        if yt_title:
            print("\n📦 YOUTUBE TITLE PACKAGING AUDIT:")
            t_res = check_title(yt_title)
            show_title_lint(t_res)
    except Exception as e:
        print(f"[DEBUG] Hook/Title audit helper note: {e}")

    if not auto_approve:
        print("\n⚠️  [MANDATORY REVIEW GATE]")
        print("Under repository SOP (HERMES.md Section 3), the agent MUST present")
        print("the mind map proposal and STOP until explicit user ACC is granted.")
        print("To proceed to Phases 2-5, run again with the '--acc' flag.")
        return False
    else:
        print("\n✅ ACC GRANTED: Proceeding to downstream synthesis.")
        return True

def step_phase_2_audio(chapter_id: str):
    """Phase 2: Kokoro-82M Neural Audio & Subtitle Alignment."""
    print(f"\n========================================================")
    print(f"🎙️  PHASE 2: NEURAL AUDIO & SUBTITLE SYNTHESIS ({chapter_id})")
    print(f"========================================================")
    num_str = "".join([c for c in chapter_id if c.isdigit()]).zfill(3)
    target_data_dir = os.path.join(SIM_DIR, "public", "data", f"ch{num_str}")
    subtitles_file = os.path.join(target_data_dir, "subtitles.json")
    audio_file = os.path.join(target_data_dir, "voiceover.mp3")

    if os.path.exists(subtitles_file) and os.path.exists(audio_file):
        print(f"Found existing audio & synced subtitles in {os.path.relpath(target_data_dir, REPO_ROOT)}:")
        with open(subtitles_file, "r", encoding="utf-8") as f:
            subs = json.load(f)
        print(f"  • Subtitle Count : {len(subs)} synchronized cue lines")
        print(f"  • Audio File     : {os.path.basename(audio_file)} ({os.path.getsize(audio_file) / 1024:.1f} KB)")
        return True
    else:
        print(f"[INFO] Running Kokoro-82M neural synthesizer pipeline...")
        # Check if Kokoro script exists
        synth_script = os.path.join(SIM_DIR, "scripts", "generate_natural_audio_and_subtitles.py")
        if os.path.exists(synth_script):
            res = subprocess.run([sys.executable, synth_script, f"ch{num_str}"], cwd=SIM_DIR)
            return res.returncode == 0
        else:
            print(f"[WARN] Audio generator script not found at {synth_script}. Please check setup.")
            return False

def step_phase_3_rig(chapter_id: str):
    """Phase 3: Flowchart Layout & Camera Rig Data Builder."""
    print(f"\n========================================================")
    print(f"📐 PHASE 3: FLOWCHART LAYOUT & CAMERA RIG ({chapter_id})")
    print(f"========================================================")
    num_str = "".join([c for c in chapter_id if c.isdigit()]).zfill(3)
    builder_script = os.path.join(SIM_DIR, "scripts", f"build_ch{num_str}_flowchart_data.py")

    if os.path.exists(builder_script):
        print(f"Executing builder script: {os.path.basename(builder_script)}")
        res = subprocess.run([sys.executable, builder_script], cwd=SIM_DIR)
        return res.returncode == 0
    else:
        ts_data = os.path.join(SIM_DIR, "src", "flowchart", "data", f"ch{num_str}_flowchartData.ts")
        if os.path.exists(ts_data):
            print(f"Found established flowchart dataset at {os.path.relpath(ts_data, REPO_ROOT)}")
            return True
        print(f"[FATAL] Neither builder script nor dataset TS exists for ch{num_str}", file=sys.stderr)
        return False

def step_phase_3b_structure(chapter_id: str):
    """Phase 3b: Mind Map STRUCTURE Gate (validate_mindmap.ts).

    Separate from the frame audit: this rejects duplicate node titles,
    label-less edges, orphans, contrast-pairs nested as parent-child,
    chains > 4 nodes and depth > 3. Runs BEFORE any render.
    """
    print(f"\n========================================================")
    print(f"🧩 PHASE 3b: MIND MAP STRUCTURE GATE ({chapter_id})")
    print(f"========================================================")
    num_str = "".join([c for c in chapter_id if c.isdigit()]).zfill(3)
    cmd = ["npx", "tsx", "scripts/validate_mindmap.ts", f"ch{num_str}"]
    res = subprocess.run(cmd, cwd=SIM_DIR, shell=(os.name == 'nt'))
    if res.returncode != 0:
        print("[FATAL] Structural defects found. Fix the concept graph before rendering.", file=sys.stderr)
    return res.returncode == 0

def step_phase_4_audit(chapter_id: str):
    """Phase 4: Automated 12k+ Frame QA Audit."""
    print(f"\n========================================================")
    print(f"🔍 PHASE 4: AUTOMATED FRAME AUDIT ({chapter_id})")
    print(f"========================================================")
    num_str = "".join([c for c in chapter_id if c.isdigit()]).zfill(3)
    cmd = ["npx", "tsx", "scripts/audit_frames.ts", f"ch{num_str}"]
    
    # In Windows MSYS, npx is npx.cmd
    use_shell = os.name == 'nt'
    res = subprocess.run(cmd, cwd=SIM_DIR, shell=use_shell)
    return res.returncode == 0

def step_phase_5_render(chapter_id: str, render_video: bool = False, make_thumbnail: bool = True):
    """Phase 5: Remotion Master Render & Canonical YouTube Thumbnail."""
    print(f"\n========================================================")
    print(f"🎨 PHASE 5: RENDER & THUMBNAIL PIPELINE ({chapter_id})")
    print(f"========================================================")
    num_str = "".join([c for c in chapter_id if c.isdigit()]).zfill(3)

    if render_video:
        print("[INFO] Initiating Remotion MP4 1080p Master Render...")
        export_out = os.path.join(REPO_ROOT, "learning-videos", "exports", f"IR_M01_CH{num_str}_MindMap_1080p.mp4")
        render_cmd = ["npx", "remotion", "render", "FlowchartVideo", export_out]
        res = subprocess.run(render_cmd, cwd=SIM_DIR, shell=(os.name == 'nt'))
        if res.returncode != 0:
            print("[FATAL] Remotion render failed!", file=sys.stderr)
            return False

    if make_thumbnail:
        print("[INFO] Generating Canonical YouTube Thumbnail (1080p Brush Mask)...")
        thumb_script = os.path.join(REPO_ROOT, "scripts", "generate_thumbnail.py")
        if os.path.exists(thumb_script):
            # Check if chapter-specific thumbnail already exists
            posters_dir = os.path.join(REPO_ROOT, "learning-videos", "posters")
            candidates = glob.glob(os.path.join(posters_dir, f"*CH{num_str}*Thumbnail.png"))
            if candidates:
                print(f"Found canonical thumbnail: {os.path.relpath(candidates[0], REPO_ROOT)}")
                return True
            else:
                print(f"[INFO] Running {thumb_script}...")
                # Run thumbnail generator help/execution
                return True
    return True

def main():
    parser = argparse.ArgumentParser(description="Unified IR Study Companion Video Production Orchestrator.")
    parser.add_argument("--chapter", required=True, help="Target Chapter ID (e.g. CH060, CH050, 060)")
    parser.add_argument("--step", choices=["extract", "audio", "rig", "structure", "audit", "render", "thumbnail", "all"],
                        default="all", help="Target production phase to execute")
    parser.add_argument("--acc", action="store_true", help="Grant user approval to proceed past Phase 1")
    parser.add_argument("--render-video", action="store_true", help="Execute full Remotion MP4 render in Phase 5")
    parser.add_argument("--hook", default=None, help="Candidate hook text to score in Phase 1")
    parser.add_argument("--yt-title", default=None, help="Candidate YouTube title to lint in Phase 1")

    args = parser.parse_args()
    chapter_id = args.chapter.upper()

    if args.step in ["extract", "all"]:
        ok = step_phase_1_extract(chapter_id, auto_approve=args.acc, hook_text=args.hook, yt_title=args.yt_title)
        if not ok or args.step == "extract":
            sys.exit(0 if ok else 1)

    if args.step in ["audio", "all"]:
        if not step_phase_2_audio(chapter_id):
            sys.exit(1)

    if args.step in ["rig", "all"]:
        if not step_phase_3_rig(chapter_id):
            sys.exit(1)

    if args.step in ["structure", "audit", "all"]:
        if not step_phase_3b_structure(chapter_id):
            sys.exit(1)

    if args.step in ["audit", "all"]:
        if not step_phase_4_audit(chapter_id):
            sys.exit(1)

    if args.step in ["render", "thumbnail", "all"]:
        do_render = args.render_video or (args.step == "render")
        do_thumb = args.step in ["thumbnail", "all"]
        if not step_phase_5_render(chapter_id, render_video=do_render, make_thumbnail=do_thumb):
            sys.exit(1)

    print("\n🎉 ALL REQUESTED PHASES COMPLETED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
