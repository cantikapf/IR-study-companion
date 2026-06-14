import os
import re
import yake

# YAKE configuration
language = "en"
max_ngram_size = 2
deduplication_threshold = 0.9
numOfKeywords = 5
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)

chapters_dir = r"d:\PERSONAL PROJECT\IR-study-companion\_chapters"

def extract_body(text):
    # Remove YAML frontmatter
    text = re.sub(r'^---.*?---\n', '', text, flags=re.DOTALL)
    # Remove code blocks
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    # Remove headers
    text = re.sub(r'^#+ .*?$', '', text, flags=re.MULTILINE)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove markdown links
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    return text

def highlight_keywords_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split frontmatter and body to avoid touching frontmatter
    match = re.match(r'^---.*?---\n', content, flags=re.DOTALL)
    if not match:
        return # Skip files without frontmatter just in case
    
    frontmatter = match.group(0)
    body = content[len(frontmatter):]

    # Extract clean text for YAKE
    clean_text = extract_body(body)
    keywords = custom_kw_extractor.extract_keywords(clean_text)

    modified = False
    for kw, score in keywords:
        # Sort keywords by length descending to replace longer phrases first if needed, though here we just process top 5
        keyword_str = kw

        # Check if keyword is already bolded (case insensitive check)
        if re.search(rf'\*\*{re.escape(keyword_str)}\*\*', body, re.IGNORECASE):
            continue
            
        # We want to replace the first occurrence of the keyword that is NOT inside html, links, or already bold.
        # This is tricky with regex. A simpler approach:
        # Find the keyword with word boundaries, case-insensitive.
        # We will use a function to replace only the FIRST occurrence
        
        pattern = re.compile(rf'\b({re.escape(keyword_str)})\b', re.IGNORECASE)
        
        # We can try to replace it only if it's not preceded/followed by **
        def replacer(m):
            return f"**{m.group(1)}**"
        
        # Let's do a simple replace, but limit to 1 occurrence
        # To avoid replacing inside links or HTML, we could use a complex regex, 
        # but since IR text is mostly paragraphs, we'll do a simple heuristic:
        # Split by paragraph, find the first normal paragraph, replace there.
        
        paragraphs = body.split('\n\n')
        for i, p in enumerate(paragraphs):
            # Skip if it's a heading, list, or html
            if p.strip().startswith('#') or p.strip().startswith('<') or p.strip().startswith('{%') or p.strip().startswith('-'):
                continue
                
            new_p, count = pattern.subn(replacer, p, count=1)
            if count > 0:
                # To prevent nested ** like ****keyword****
                new_p = new_p.replace('****', '**')
                paragraphs[i] = new_p
                modified = True
                break # Move to next keyword
                
        body = '\n\n'.join(paragraphs)

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(frontmatter + body)
        print(f"Highlighted {filepath}")

for root, dirs, files in os.walk(chapters_dir):
    for file in files:
        if file.endswith('.md'):
            highlight_keywords_in_file(os.path.join(root, file))

print("Auto-highlighting complete!")
