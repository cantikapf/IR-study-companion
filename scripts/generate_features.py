import os
import glob
import json
import re
import time
import sys

try:
    from openai import OpenAI
except ImportError:
    print("Error: Library 'openai' is missing.")
    print("Please install it first by running: pip install openai")
    sys.exit(1)

# Ambil API Key dari Environment Variable
API_KEY = os.environ.get("GROQ_API_KEY")
if not API_KEY:
    print("=========================================================")
    print("ERROR: GROQ_API_KEY belum diatur!")
    print("Silakan jalankan perintah ini di PowerShell Anda terlebih dahulu:")
    print("  $env:GROQ_API_KEY=\"masukkan_api_key_groq_anda_disini\"")
    print("Lalu jalankan ulang skrip ini.")
    print("=========================================================")
    sys.exit(1)

# Konfigurasi client OpenAI untuk menggunakan endpoint Groq
client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

# Cari model yang tersedia secara dinamis dari server Groq
print("Mendeteksi model Groq yang tersedia...")
try:
    models_data = client.models.list().data
    available_models = [m.id for m in models_data]
except Exception as e:
    print(f"Gagal menghubungi Groq API. Pastikan API Key valid. Error: {e}")
    sys.exit(1)

if not available_models:
    print("Error: Tidak ada model yang tersedia di API Key Groq Anda.")
    sys.exit(1)

# Prioritaskan model llama terbaru, jika tidak ada pakai model pertama
chosen_model = available_models[0]
for m in available_models:
    if "llama" in m.lower() and "vision" not in m.lower():
        chosen_model = m
        break

print(f"Menggunakan model Groq: {chosen_model}")

PROMPT = """
You are an expert educational content creator. I will provide you with the text of a chapter from an International Relations course.
Your task is to analyze the material and generate:
1. 4 key concepts with short, concise definitions (maximum 15 words each) for interactive flashcards.
2. 1 multiple-choice question testing the core concept of the chapter, with 4 options and the index (1-4) of the correct answer.

Output ONLY valid JSON in exactly this structure, do not include markdown formatting or backticks:
{
  "flashcards": [
    {"term": "Term 1", "def": "Definition 1"},
    {"term": "Term 2", "def": "Definition 2"},
    {"term": "Term 3", "def": "Definition 3"},
    {"term": "Term 4", "def": "Definition 4"}
  ],
  "quiz": {
    "question": "The question text?",
    "opt1": "Option 1 text",
    "opt2": "Option 2 text",
    "opt3": "Option 3 text",
    "opt4": "Option 4 text",
    "correct": "2"
  }
}
"""

def process_file(filepath):
    print(f"Memproses: {filepath} ...")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Mengecek apakah file ini masih menggunakan kuis dan flashcard generik
        if "Which of the following best summarizes the core concept discussed in this chapter?" not in content:
            print("  -> Dilewati: Fitur sudah kontekstual atau tidak ada kuis generik.")
            return

        # Hapus blok interaktif lama
        text_to_analyze = re.sub(r"### Interactive Learning.*", "", content, flags=re.DOTALL)
        
        # Panggil Groq API
        max_retries = 3
        response_text = ""
        for attempt in range(max_retries):
            try:
                response = client.chat.completions.create(
                    model=chosen_model,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that always responds in valid JSON format only."},
                        {"role": "user", "content": PROMPT + "\n\nText:\n" + text_to_analyze}
                    ],
                    temperature=0.2
                )
                response_text = response.choices[0].message.content
                break
            except Exception as e:
                if "429" in str(e) or "limit" in str(e).lower() or "rate" in str(e).lower():
                    print(f"  -> Limit API tercapai (Mencoba ulang {attempt+1}/{max_retries}). Menunggu 15 detik...")
                    time.sleep(15)
                    if attempt == max_retries - 1:
                        raise Exception("Gagal setelah beberapa kali percobaan akibat Limit API.")
                else:
                    raise e
        
        # Parsing JSON
        json_str = re.search(r'\{.*\}', response_text, re.DOTALL)
        if json_str:
            data = json.loads(json_str.group(0))
        else:
            print("  -> Gagal: Response bukan JSON valid.")
            return
            
        fc = data['flashcards']
        qz = data['quiz']
        
        def sanitize(val):
            return str(val).replace('"', "'")
            
        for item in fc:
            item['term'] = sanitize(item.get('term', ''))
            item['def'] = sanitize(item.get('def', ''))
            
        qz['question'] = sanitize(qz.get('question', ''))
        qz['opt1'] = sanitize(qz.get('opt1', ''))
        qz['opt2'] = sanitize(qz.get('opt2', ''))
        qz['opt3'] = sanitize(qz.get('opt3', ''))
        qz['opt4'] = sanitize(qz.get('opt4', ''))
        qz['correct'] = sanitize(qz.get('correct', ''))
        
        quiz_id = "quiz_" + os.path.basename(filepath).replace(".md", "").replace("-", "_")
        
        # Buat blok markdown baru yang kontekstual
        new_block = f"""### Interactive Learning 
{{% include flashcards.html term1="{fc[0]['term']}" def1="{fc[0]['def']}" term2="{fc[1]['term']}" def2="{fc[1]['def']}" term3="{fc[2]['term']}" def3="{fc[2]['def']}" term4="{fc[3]['term']}" def4="{fc[3]['def']}" %}}

### Knowledge Check
{{% include quiz.html id="{quiz_id}" question="{qz['question']}" opt1="{qz['opt1']}" opt2="{qz['opt2']}" opt3="{qz['opt3']}" opt4="{qz['opt4']}" correct="{qz['correct']}" %}}
"""
        
        # Timpa blok lama dengan blok baru
        new_content = re.sub(r"### Interactive Learning.*", new_block, content, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print("  -> Sukses! Kuis & Flashcards berhasil diperbarui.")
        
    except Exception as e:
        print(f"  -> Terjadi Error: {e}")

if __name__ == "__main__":
    # Mencari semua file markdown di direktori _chapters
    md_files = glob.glob("_chapters/**/*.md", recursive=True)
    count = 0
    
    for filepath in md_files:
        # Lewati folder front/back dan file index
        if "000-front" in filepath or "999-back" in filepath or "000-index.md" in filepath:
            continue
            
        process_file(filepath)
        time.sleep(1) # Jeda ringan karena Groq biasanya punya throughput tinggi
        count += 1
        
    print(f"\n=========================================================")
    print(f"Selesai! Telah mengeksekusi {count} file.")
