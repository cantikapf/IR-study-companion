import os
import re

def audit_all_quizzes():
    print("=== Auditing All Chapter Quizzes in _chapters/ ===")
    total_chapters = 0
    chapters_with_quiz = 0
    malformed_quizzes = []
    
    # Regex to find quiz questions
    # Format in chapters:
    # question: "..."
    # options: [...]
    # correct: 0/1/2/3
    # or Liquid include quiz.html
    for root, dirs, files in os.walk("_chapters"):
        for f in files:
            if not f.endswith(".md"):
                continue
            total_chapters += 1
            fpath = os.path.join(root, f)
            with open(fpath, "r", encoding="utf-8", errors="replace") as fp:
                text = fp.read()
                
            # Check frontmatter quiz block
            # Often either in frontmatter or in body
            quiz_blocks = re.findall(r'question:\s*["\x27](.*?)["\x27]', text)
            if quiz_blocks:
                chapters_with_quiz += 1
                
            # Check for correct parameter
            correct_matches = re.findall(r'correct:\s*(\d+)', text)
            options_matches = re.findall(r'options:\s*(\[.*?\])', text, re.DOTALL)
            
            for c_idx, o_str in zip(correct_matches, options_matches):
                c_val = int(c_idx)
                # count elements in options list
                opts = re.findall(r'["\x27](.*?)["\x27]', o_str)
                if c_val >= len(opts) or c_val < 0:
                    malformed_quizzes.append({
                        "file": fpath,
                        "error": f"Correct index {c_val} out of bounds for {len(opts)} options"
                    })
                    
    print(f"Total markdown chapters examined: {total_chapters}")
    print(f"Chapters with structured quiz: {chapters_with_quiz}")
    print(f"Malformed quiz questions found: {len(malformed_quizzes)}")
    for mq in malformed_quizzes:
        print(f"  {mq['file']}: {mq['error']}")

if __name__ == "__main__":
    audit_all_quizzes()
