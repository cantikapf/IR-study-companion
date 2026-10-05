import os
import re
import json
import math
from collections import Counter

CHAPTERS_DIR = "_chapters"
GLOSSARY_FILE = "_data/ir_glossary.json"

def count_syllables(word):
    word = word.lower().strip(".:;?!,()\"'")
    if not word:
        return 0
    if len(word) <= 3:
        return 1
    # Simple syllable heuristic
    word = re.sub(r'(?:[^laeiouy]|ed|es|e)$', '', word)
    word = re.sub(r'^y', '', word)
    syllables = len(re.findall(r'[aeiouy]{1,2}', word))
    return max(1, syllables)

def analyze_text(text):
    # Remove markdown formatting, code blocks, html tags
    clean_text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    clean_text = re.sub(r'<.*?>', '', clean_text)
    clean_text = re.sub(r'\{%.*?%\}', '', clean_text)
    clean_text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', clean_text)
    clean_text = re.sub(r'[#*_~`]', '', clean_text)

    # Sentences
    sentences = [s.strip() for s in re.split(r'[.!?]+', clean_text) if len(s.strip()) > 5]
    words = re.findall(r'\b[a-zA-Z]{2,}\b', clean_text)

    num_sentences = max(1, len(sentences))
    num_words = max(1, len(words))

    num_syllables = sum(count_syllables(w) for w in words)
    poly_words = [w for w in words if count_syllables(w) >= 3]

    # Flesch Reading Ease: 206.835 - 1.015*(words/sentences) - 84.6*(syllables/words)
    fre = 206.835 - (1.015 * (num_words / num_sentences)) - (84.6 * (num_syllables / num_words))
    # Flesch-Kincaid Grade Level: 0.39*(words/sentences) + 11.8*(syllables/words) - 15.59
    fkgl = (0.39 * (num_words / num_sentences)) + (11.8 * (num_syllables / num_words)) - 15.59

    avg_sentence_len = num_words / num_sentences
    poly_pct = (len(poly_words) / num_words) * 100

    return {
        "word_count": num_words,
        "sentence_count": num_sentences,
        "avg_sentence_len": round(avg_sentence_len, 1),
        "poly_pct": round(poly_pct, 1),
        "flesch_reading_ease": round(fre, 1),
        "fkgl_grade": round(fkgl, 1),
    }

def main():
    # Load glossary terms
    glossary_terms = []
    if os.path.exists(GLOSSARY_FILE):
        with open(GLOSSARY_FILE, "r", encoding="utf-8") as f:
            gdata = json.load(f)
            glossary_terms = [item["term"] for item in gdata]

    print(f"Loaded {len(glossary_terms)} glossary terms from {GLOSSARY_FILE}")

    chapter_stats = []
    all_matched_terms = Counter()
    total_words_all = 0
    total_sentences_all = 0
    total_syllables_all = 0

    for root, dirs, files in os.walk(CHAPTERS_DIR):
        for f in sorted(files):
            if f.endswith(".md") and not f.startswith("000-") and "999-back" not in root:
                filepath = os.path.join(root, f)
                with open(filepath, "r", encoding="utf-8") as fh:
                    content = fh.read()

                # Separate frontmatter from body
                body = content
                fm_match = re.match(r"^---\s*\n(.*?)\n---(.*)", content, re.DOTALL)
                if fm_match:
                    body = fm_match.group(2)

                stats = analyze_text(body)
                stats["file"] = os.path.relpath(filepath, CHAPTERS_DIR)

                # Check glossary term occurrences in body
                terms_in_chapter = []
                for term in glossary_terms:
                    # Clean term for regex
                    pattern = r'\b' + re.escape(term.split('(')[0].strip()) + r'\b'
                    if re.search(pattern, body, re.IGNORECASE):
                        terms_in_chapter.append(term)
                        all_matched_terms[term] += 1

                stats["terms_count"] = len(terms_in_chapter)
                stats["terms_sample"] = terms_in_chapter[:5]
                chapter_stats.append(stats)

    # Global averages
    avg_fre = sum(s["flesch_reading_ease"] for s in chapter_stats) / len(chapter_stats)
    avg_fkgl = sum(s["fkgl_grade"] for s in chapter_stats) / len(chapter_stats)
    avg_sent_len = sum(s["avg_sentence_len"] for s in chapter_stats) / len(chapter_stats)
    avg_poly = sum(s["poly_pct"] for s in chapter_stats) / len(chapter_stats)
    avg_terms = sum(s["terms_count"] for s in chapter_stats) / len(chapter_stats)

    print("\n" + "="*60)
    print("=== EMPIRICAL READABILITY & JARGON AUDIT REPORT ===")
    print("="*60)
    print(f"Total Chapters Analyzed: {len(chapter_stats)}")
    print(f"Average Flesch Reading Ease: {avg_fre:.1f} / 100")
    print(f"  -> Interpretation: {'Very Difficult (College Graduate)' if avg_fre < 30 else 'Difficult (College)' if avg_fre < 50 else 'Fairly Difficult (High School)' if avg_fre < 60 else 'Standard'}")
    print(f"Average Flesch-Kincaid Grade Level: Grade {avg_fkgl:.1f}")
    print(f"  -> Target for general audience: Grade 8-10. Current is Grade {avg_fkgl:.1f} (University level)")
    print(f"Average Sentence Length: {avg_sent_len:.1f} words/sentence (Target: 15-20 words)")
    print(f"Average Polysyllabic (>3 syllables) Words: {avg_poly:.1f}%")
    print(f"Average Specialized IR Terms per Chapter: {avg_terms:.1f} terms")

    # Hardest chapters
    print("\n--- Top 5 Hardest Chapters (Lowest Flesch Reading Ease) ---")
    hardest = sorted(chapter_stats, key=lambda s: s["flesch_reading_ease"])[:5]
    for h in hardest:
        print(f"  • {h['file']}: FRE {h['flesch_reading_ease']}, FKGL Grade {h['fkgl_grade']}, Sent Len {h['avg_sentence_len']}, Jargon Terms: {h['terms_count']}")

    print("\n--- Most Jargon-Dense Chapters ---")
    jargon_dense = sorted(chapter_stats, key=lambda s: s["terms_count"], reverse=True)[:5]
    for jd in jargon_dense:
        print(f"  • {jd['file']}: {jd['terms_count']} terms (e.g. {', '.join(jd['terms_sample'])})")

    print("\n--- Most Frequent Specialized Terms across Repo ---")
    for t, c in all_matched_terms.most_common(15):
        print(f"  • {t}: appears in {c} chapters")

if __name__ == "__main__":
    main()
