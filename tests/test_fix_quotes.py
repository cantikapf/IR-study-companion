import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import re
from fix_quotes import fix_quotes_in_tag

class MockMatch:
    def __init__(self, string):
        self.string = string
    def group(self, index):
        return self.string

def test_fix_quiz_quotes():
    original = '''{% include quiz.html id="test" question="Who said "hello"?" opt1="A" opt2="B" opt3="C" opt4="D" correct="1" %}'''
    expected = '''{% include quiz.html id="test" question="Who said 'hello'?" opt1="A" opt2="B" opt3="C" opt4="D" correct="1" %}'''
    match = MockMatch(original)
    assert fix_quotes_in_tag(match) == expected

def test_fix_flashcards_quotes():
    original = '''{% include flashcards.html term1="A" def1="A "B"" term2="C" def2="D" term3="E" def3="F" term4="G" def4="H" %}'''
    expected = '''{% include flashcards.html term1="A" def1="A 'B'" term2="C" def2="D" term3="E" def3="F" term4="G" def4="H" %}'''
    match = MockMatch(original)
    assert fix_quotes_in_tag(match) == expected

def test_ignore_other_tags():
    original = '''{% include something_else.html prop="A "B"" %}'''
    match = MockMatch(original)
    assert fix_quotes_in_tag(match) == original
