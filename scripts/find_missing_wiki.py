import os
import re
import json
import urllib.request
from urllib.error import HTTPError
import concurrent.futures

chapters_dir = r"d:\PERSONAL PROJECT\IR-study-companion\_chapters"
keywords = set()

for root, dirs, files in os.walk(chapters_dir):
    for file in files:
        if file.endswith('.md'):
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                content = f.read()
                # Find all **keyword** occurrences
                matches = re.findall(r'\*\*([^*]+)\*\*', content)
                for m in matches:
                    kw = m.strip()
                    if len(kw) > 1 and len(kw) < 40:
                        keywords.add(kw)

print(f"Found {len(keywords)} unique keywords.")

missing_keywords = []

def check_wiki(kw):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(kw)}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                return None
    except HTTPError as e:
        if e.code == 404:
            return kw
    except Exception as e:
        return kw
    return kw

print("Checking Wikipedia API...")
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(check_wiki, keywords))

for res in results:
    if res is not None:
        missing_keywords.append(res)

print(f"Found {len(missing_keywords)} missing keywords.")

with open('missing_keywords.json', 'w', encoding='utf-8') as f:
    json.dump(missing_keywords, f, indent=2)

print("Saved to missing_keywords.json")
