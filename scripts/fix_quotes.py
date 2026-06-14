import os
import glob
import re

def fix_quotes_in_tag(match):
    tag = match.group(0)
    
    if 'quiz.html' in tag:
        m = re.search(r'id="(.*?)"\s+question="(.*?)"\s+opt1="(.*?)"\s+opt2="(.*?)"\s+opt3="(.*?)"\s+opt4="(.*?)"\s+correct="(.*?)"\s*%\}', tag, re.DOTALL)
        if m:
            id_val, q_val, o1_val, o2_val, o3_val, o4_val, c_val = m.groups()
            q_val = q_val.replace('"', "'")
            o1_val = o1_val.replace('"', "'")
            o2_val = o2_val.replace('"', "'")
            o3_val = o3_val.replace('"', "'")
            o4_val = o4_val.replace('"', "'")
            return f'{{% include quiz.html id="{id_val}" question="{q_val}" opt1="{o1_val}" opt2="{o2_val}" opt3="{o3_val}" opt4="{o4_val}" correct="{c_val}" %}}'
            
    elif 'flashcards.html' in tag:
        m = re.search(r'term1="(.*?)"\s+def1="(.*?)"\s+term2="(.*?)"\s+def2="(.*?)"\s+term3="(.*?)"\s+def3="(.*?)"\s+term4="(.*?)"\s+def4="(.*?)"\s*%\}', tag, re.DOTALL)
        if m:
            t1, d1, t2, d2, t3, d3, t4, d4 = [g.replace('"', "'") for g in m.groups()]
            return f'{{% include flashcards.html term1="{t1}" def1="{d1}" term2="{t2}" def2="{d2}" term3="{t3}" def3="{d3}" term4="{t4}" def4="{d4}" %}}'
            
    return tag

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    content = re.sub(r'\{%\s*include\s+quiz\.html\s+.*?%\}', fix_quotes_in_tag, content, flags=re.DOTALL)
    content = re.sub(r'\{%\s*include\s+flashcards\.html\s+.*?%\}', fix_quotes_in_tag, content, flags=re.DOTALL)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed quotes in: {filepath}")

if __name__ == '__main__':
    for filepath in glob.glob("_chapters/**/*.md", recursive=True):
        fix_file(filepath)
