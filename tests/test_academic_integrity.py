"""
Automated Academic Integrity and Quiz Consistency Test Suite
Validates that:
1. No malformed markdown bold tags exist (**word **word**).
2. No Unicode replacement artifacts exist (\ufffd).
3. All chapter quizzes have complete, valid structures (question, opt1-opt4, correct in 1..4).
4. All module exams in module_exams.json have 10 valid questions with answer in 1..4.
5. All glossary concepts in ir_glossary.json have term, definition, and category.
"""

import os
import re
import json
import pytest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS_DIR = os.path.join(BASE_DIR, "_chapters")
DATA_DIR = os.path.join(BASE_DIR, "assets", "data")

def get_markdown_files():
    md_files = []
    for root, dirs, files in os.walk(CHAPTERS_DIR):
        for f in files:
            if f.endswith(".md"):
                md_files.append(os.path.join(root, f))
    return md_files

@pytest.mark.parametrize("filepath", get_markdown_files())
def test_no_encoding_artifacts(filepath):
    """Ensure no replacement characters or corrupted encoding bytes exist."""
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    assert "\ufffd" not in content, f"File {filepath} contains corrupted Unicode replacement character (\ufffd)"

@pytest.mark.parametrize("filepath", get_markdown_files())
def test_no_malformed_bold_markdown(filepath):
    """Ensure no AI artifact corrupted bold patterns (**word **word**)."""
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    for idx, line in enumerate(lines, 1):
        assert not re.search(r"\*\*[A-Za-z0-9_\-]+\s+\*\*", line), (
            f"Malformed bold pattern in {filepath}:{idx}: {line.strip()}"
        )

def test_chapter_quizzes_integrity():
    """Ensure all chapter quizzes have proper fields and correct option indices."""
    quiz_pattern = re.compile(r"\{%\s*include\s+quiz\.html\s+([^%]+)%\}")
    md_files = get_markdown_files()
    total_quizzes = 0
    
    for path in md_files:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        for match in quiz_pattern.finditer(content):
            total_quizzes += 1
            args = match.group(1)
            # check question
            assert re.search(r'question="[^"]+"', args), f"Quiz missing question in {path}"
            # check options
            for i in range(1, 5):
                assert re.search(rf'opt{i}="[^"]+"', args), f"Quiz missing opt{i} in {path}"
            # check correct
            correct_m = re.search(r'correct="([1-4])"', args)
            assert correct_m, f"Quiz has missing or invalid correct option (must be 1-4) in {path}"
            
    assert total_quizzes >= 150, f"Expected at least 150 quizzes, found {total_quizzes}"

def test_module_exams_data_integrity():
    """Ensure all 18 modules have 10 valid questions in module_exams.json."""
    exams_path = os.path.join(DATA_DIR, "module_exams.json")
    assert os.path.exists(exams_path), "assets/data/module_exams.json missing"
    
    with open(exams_path, "r", encoding="utf-8") as f:
        modules = json.load(f)
        
    assert len(modules) == 18, f"Expected 18 modules, found {len(modules)}"
    
    for mod_id, mod_data in modules.items():
        assert "module_title" in mod_data, f"Module {mod_id} missing module_title"
        questions = mod_data.get("questions", [])
        assert len(questions) == 10, f"Module {mod_id} must have exactly 10 questions, found {len(questions)}"
        for q_idx, q in enumerate(questions, 1):
            assert "q" in q and len(q["q"]) > 10, f"Module {mod_id} Q{q_idx} invalid question"
            assert "opts" in q and len(q["opts"]) == 4, f"Module {mod_id} Q{q_idx} must have 4 options"
            assert "correct" in q and q["correct"] in [0, 1, 2, 3], f"Module {mod_id} Q{q_idx} correct must be 0-3"
            assert "explanation" in q and len(q["explanation"]) > 10, f"Module {mod_id} Q{q_idx} missing explanation"

def test_glossary_data_integrity():
    """Ensure ir_glossary.json has complete, well-formed terms."""
    glossary_path = os.path.join(DATA_DIR, "ir_glossary.json")
    assert os.path.exists(glossary_path), "assets/data/ir_glossary.json missing"
    
    with open(glossary_path, "r", encoding="utf-8") as f:
        terms = json.load(f)
        
    assert isinstance(terms, list), f"Expected list of terms, got {type(terms)}"
    assert len(terms) >= 120, f"Expected >= 120 terms, found {len(terms)}"
    
    for t in terms:
        assert "term" in t and len(t["term"]) > 1, f"Missing term name: {t}"
        assert "definition" in t and len(t["definition"]) > 15, f"Missing or brief definition for {t.get('term')}"
        assert "category" in t, f"Missing category for {t.get('term')}"
