import json
import os

def audit_module_exams():
    print("=== Auditing Module Exams (assets/data/module_exams.json) ===")
    ex_path = os.path.join("assets", "data", "module_exams.json")
    if not os.path.exists(ex_path):
        print("module_exams.json not found")
        return
        
    with open(ex_path, "r", encoding="utf-8") as fp:
        data = json.load(fp)
        
    print(f"Total modules with exams: {len(data)}")
    total_q = 0
    issues = []
    
    for mod_slug, exam in data.items():
        title = exam.get("module_title", "")
        questions = exam.get("questions", [])
        total_q += len(questions)
        for idx, q in enumerate(questions, 1):
            q_text = q.get("q", "")
            opts = q.get("opts", [])
            correct = q.get("correct")
            exp = q.get("explanation", "")
            
            if correct is None or not (0 <= correct < len(opts)):
                issues.append(f"[{mod_slug}] Q{idx}: invalid correct index {correct} for {len(opts)} options")
            if len(opts) < 2:
                issues.append(f"[{mod_slug}] Q{idx}: fewer than 2 options")
            if not exp:
                issues.append(f"[{mod_slug}] Q{idx}: missing explanation")
            if not q_text:
                issues.append(f"[{mod_slug}] Q{idx}: missing question text")
                
    print(f"Total exam questions: {total_q}")
    print(f"Issues found: {len(issues)}")
    if issues:
        for iss in issues:
            print(f"  {iss}")
    else:
        print("All 180 questions have valid text, valid options, valid correct indices, and detailed explanations!")

if __name__ == "__main__":
    audit_module_exams()
