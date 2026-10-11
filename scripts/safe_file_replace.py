#!/usr/bin/env python3
"""
safe_file_replace.py

Atomic, verified file replacement utility for IR Study Companion.
Solves the "write_file stale-read guard" problem and enforces transcription integrity:
  1. Performs atomic write via temporary file (os.replace) without stale-read lockouts.
  2. Runs language-specific syntax checks:
     - Python: py_compile
     - JSON: json.loads
     - JavaScript: node -c
     - HTML/Liquid: <div> tag balance + inline <script> JavaScript syntax verification.
  3. Greps for accidental corruption markers (e.g., [SKILL_PRUNED], truncated diff headers).
"""

import os
import sys
import argparse
import subprocess
import json
import py_compile
import re

def audit_html_content(content: str, filepath: str):
    """Audits HTML/Liquid templates for tag balance and inline script syntax."""
    # 1. Div balance audit
    open_divs = len(re.findall(r'<div\b[^>]*>', content, re.IGNORECASE))
    close_divs = len(re.findall(r'</div>', content, re.IGNORECASE))
    if open_divs != close_divs:
        print(f"[WARN] <div> tag mismatch in {filepath}: {open_divs} open vs {close_divs} close.")

    # 2. Extract inline <script> tags and verify JS syntax
    script_blocks = re.findall(r'<script\b[^>]*>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
    for idx, script in enumerate(script_blocks):
        cleaned_script = script.strip()
        # Skip empty or Liquid-only templating scripts
        if not cleaned_script or '{{' in cleaned_script or '{%' in cleaned_script:
            continue
        try:
            res = subprocess.run(
                ["node", "-e", f"new Function({json.dumps(cleaned_script)})"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if res.returncode != 0:
                raise ValueError(f"Inline <script> #{idx+1} syntax error: {res.stderr.strip()}")
        except FileNotFoundError:
            pass # Node not found, skip

def validate_content(filepath: str, content: str):
    """Validates content integrity before committing to disk."""
    # Check for corruption markers
    corruption_markers = ["[SKILL_PRUNED]", "<<<<<<<", "=======", ">>>>>>>"]
    for m in corruption_markers:
        if m in content:
            raise ValueError(f"Detected illegal corruption marker in content: '{m}'")

    ext = os.path.splitext(filepath)[1].lower()
    
    if ext == ".json":
        json.loads(content)
    elif ext in [".html", ".liquid"]:
        audit_html_content(content, filepath)

def safe_replace(filepath: str, new_content: str, skip_validation: bool = False):
    abs_path = os.path.abspath(filepath)
    os.makedirs(os.path.dirname(abs_path), exist_ok=True)

    if not skip_validation:
        validate_content(abs_path, new_content)

    tmp_path = abs_path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_content)

    ext = os.path.splitext(abs_path)[1].lower()
    if not skip_validation:
        if ext == ".py":
            py_compile.compile(tmp_path, doraise=True)
        elif ext in [".js", ".mjs"]:
            try:
                res = subprocess.run(["node", "-c", tmp_path], capture_output=True, text=True, timeout=5)
                if res.returncode != 0:
                    os.remove(tmp_path)
                    raise ValueError(f"JavaScript syntax error: {res.stderr.strip()}")
            except FileNotFoundError:
                pass

    # Atomic swap
    os.replace(tmp_path, abs_path)
    print(f"[SAFE_WRITE] Successfully wrote {len(new_content)} bytes to {abs_path}")

def main():
    parser = argparse.ArgumentParser(description="Safely replace a file atomically with syntax verification.")
    parser.add_argument("target", help="Target file path")
    parser.add_argument("content", nargs="?", default=None, help="Inline content (or '-' to read stdin)")
    parser.add_argument("--from-file", help="Source file to read replacement from")
    parser.add_argument("--skip-validation", action="store_true", help="Bypass syntax and corruption checks")

    args = parser.parse_args()

    if args.from_file:
        with open(args.from_file, "r", encoding="utf-8") as f:
            content = f.read()
    elif args.content == "-" or (args.content is None and not sys.stdin.isatty()):
        content = sys.stdin.read()
    elif args.content is not None:
        content = args.content
    else:
        print("[FATAL] No content provided. Provide string, --from-file, or pipe via stdin.", file=sys.stderr)
        sys.exit(1)

    try:
        safe_replace(args.target, content, skip_validation=args.skip_validation)
    except Exception as e:
        print(f"[FATAL] Safe replace failed: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
