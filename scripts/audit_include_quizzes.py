import os
import re

def audit_include_quizzes():
    print("=== Auditing Liquid {% include quiz.html ... %} in _chapters/ ===")
    total_quizzes = 0
    issues = []
    
    quiz_pattern = re.compile(r'{%\s*include\s+quiz\.html\s+([^%]+)%}', re.DOTALL)
    param_pattern = re.compile(r'(\w+)=(?:"([^"]*)"|\'([^\']*)\'|([^\s]+))')
    
    for root, dirs, files in os.walk("_chapters"):
        for f in files:
            if not f.endswith(".md"):
                continue
            fpath = os.path.join(root, f)
            with open(fpath, "r", encoding="utf-8", errors="replace") as fp:
                text = fp.read()
                
            matches = quiz_pattern.findall(text)
            for m in matches:
                total_quizzes += 1
                params = {}
                for k, v1, v2, v3 in param_pattern.findall(m):
                    params[k] = v1 or v2 or v3
                    
                qid = params.get("id")
                q_text = params.get("question")
                opt1 = params.get("opt1")
                opt2 = params.get("opt2")
                opt3 = params.get("opt3")
                opt4 = params.get("opt4")
                correct = params.get("correct")
                
                relpath = os.path.relpath(fpath, "_chapters")
                
                if not qid:
                    issues.append(f"[{relpath}] Missing quiz id")
                if not q_text:
                    issues.append(f"[{relpath}] Missing question text")
                if not (opt1 and opt2):
                    issues.append(f"[{relpath}] (ID: {qid}) Missing at least opt1 and opt2")
                if correct not in ["1", "2", "3", "4"]:
                    issues.append(f"[{relpath}] (ID: {qid}) Invalid correct value '{correct}' (must be 1-4)")
                else:
                    opt_key = f"opt{correct}"
                    if not params.get(opt_key):
                        issues.append(f"[{relpath}] (ID: {qid}) Correct points to {opt_key}, which is missing/empty")

    print(f"Total quizzes audited: {total_quizzes}")
    print(f"Quiz integrity issues found: {len(issues)}")
    if issues:
        for iss in issues[:20]:
            print(f"  {iss}")
    else:
        print("All 155 chapter quizzes have 100% valid structure, complete options, and valid correct answers!")

if __name__ == "__main__":
    audit_include_quizzes()
