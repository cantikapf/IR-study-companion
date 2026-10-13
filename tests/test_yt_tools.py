import os
import sys
import tempfile
import pytest

# Ensure scripts is on pythonpath
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from yt.hookscore import score as score_hook, classify as classify_hook
from yt.title import check as check_title
from yt.retention import load_csv
from yt.swipe import classify as classify_title_swipe


def test_hookscore_evaluation():
    hook = "In the next 6 minutes you will have a working title and script for your video."
    parts, verdict, name, hits = score_hook(hook)
    
    assert "SPECIFICITY" in parts
    assert "BREVITY" in parts
    assert isinstance(verdict, int)
    assert 0 <= verdict <= 100
    assert name == "The Clock"
    assert hits >= 1


def test_title_lint_duplicate_and_truncation():
    # Title repeats thumb text and is too long for mobile
    res = check_title("The Secret Cuban Missile Crisis Strategy Revealed Today", thumb="SECRET CRISIS")
    
    assert res["chars"] > 40
    issue_keys = [k for k, _ in res["issues"]]
    assert "duplicate" in issue_keys
    assert "mobile" in issue_keys


def test_title_lint_healthy():
    res = check_title("Why 97% of Nuclear Treaties Fail in 2026?", thumb="TREATY ZERO")
    good_msgs = " ".join(res["good"])
    assert "carries a concrete figure" in good_msgs
    assert "open question" in good_msgs


def test_retention_csv_loader():
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".csv") as f:
        f.write("Time (seconds),Audience retention (%)\n")
        f.write("0,100\n10,85\n20,75\n30,70\n40,65\n50,60\n60,55\n70,50\n")
        f_path = f.name
        
    try:
        rows = load_csv(f_path)
        assert len(rows) == 8
        assert rows[0] == (0.0, 100.0)
        assert rows[-1] == (70.0, 50.0)
    finally:
        if os.path.exists(f_path):
            os.remove(f_path)


def test_swipe_classify_formula():
    title = "7 Things I Wish I Knew Before Studying Modern War"
    formula = classify_title_swipe(title)
    assert formula == "The List"
