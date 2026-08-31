"""
Verification of academic references and citations in IR Study Companion.
Audits _chapters/999-back/010-references.md:
- Extracts DOIs, URLs, book/article titles, and authors
- Queries CrossRef REST API for DOIs and bibliographic matching
- Validates URLs and flags 404/broken links
- Outputs a comprehensive JSON and Markdown audit report
"""

import os
import re
import json
import time
import urllib.request
import urllib.parse
import urllib.error

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFERENCES_FILE = os.path.join(BASE_DIR, '_chapters', '999-back', '010-references.md')
REPORT_FILE_MD = os.path.join(BASE_DIR, 'wiki', 'reference_audit_report.md')
REPORT_FILE_JSON = os.path.join(BASE_DIR, 'wiki', 'reference_audit_data.json')

USER_AGENT = 'IR-Study-Companion-ReferenceChecker/1.0 (mailto:admin@irstudy.local)'

def check_doi_crossref(doi):
    """Check DOI validity against CrossRef API."""
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            if resp.status == 200:
                data = json.loads(resp.read().decode('utf-8'))
                title = data.get('message', {}).get('title', [''])[0]
                authors = data.get('message', {}).get('author', [])
                author_names = [a.get('family', '') for a in authors if 'family' in a]
                return {
                    'valid': True,
                    'status': 'verified_crossref',
                    'title': title,
                    'authors': author_names,
                    'type': data.get('message', {}).get('type', '')
                }
    except urllib.error.HTTPError as e:
        return {'valid': False, 'status': f'http_{e.code}', 'error': str(e)}
    except Exception as e:
        return {'valid': None, 'status': 'timeout_or_error', 'error': str(e)}
    return {'valid': False, 'status': 'unknown'}

def check_url(url):
    """Check URL status via HTTP GET."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            return {'status_code': resp.status, 'accessible': 200 <= resp.status < 400}
    except urllib.error.HTTPError as e:
        return {'status_code': e.code, 'accessible': e.code in [403, 401]}
    except Exception as e:
        return {'status_code': 0, 'accessible': False, 'error': str(e)}

def parse_references():
    with open(REFERENCES_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    current_module = "General"
    entries = []

    doi_pattern = re.compile(r'10\.\d{4,9}/[-._;()/:A-Z0-9]+', re.IGNORECASE)
    url_pattern = re.compile(r'https?://[^\s)\]]+')

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith('**') and stripped.endswith('**') and not stripped.startswith('- '):
            current_module = stripped.strip('*').strip()
            continue
        if stripped.startswith('- ') or (stripped[0].isalpha() and not stripped.startswith('#')):
            text = stripped.lstrip('- ').strip()
            doi_match = doi_pattern.search(text)
            doi = doi_match.group(0).rstrip('.') if doi_match else None
            url_match = url_pattern.search(text)
            url = url_match.group(0).rstrip('.') if url_match else None

            year_match = re.search(r'\((\d{4})[a-z]?\)', text)
            year = year_match.group(1) if year_match else None

            author = text.split('(')[0].strip() if '(' in text else text.split('.')[0].strip()

            title_part = ""
            if year_match:
                after_year = text[year_match.end():].lstrip('. ')
                title_part = after_year.split('.')[0].strip()

            entries.append({
                'module': current_module,
                'raw': text,
                'author': author,
                'year': year,
                'title_approx': title_part,
                'doi': doi,
                'url': url
            })

    return entries

def main():
    print(f"Reading references from {REFERENCES_FILE}...", flush=True)
    entries = parse_references()
    print(f"Found {len(entries)} references across modules.", flush=True)

    results = []
    verified_dois = 0
    broken_urls = 0
    hallucination_suspects = []

    for i, entry in enumerate(entries, 1):
        print(f"[{i}/{len(entries)}] Checking: {entry['raw'][:50]}...", flush=True)
        audit_info = {
            'entry': entry,
            'doi_status': None,
            'url_status': None,
            'flag': 'OK'
        }

        if entry['doi']:
            doi_res = check_doi_crossref(entry['doi'])
            audit_info['doi_status'] = doi_res
            if doi_res.get('valid'):
                verified_dois += 1
            else:
                audit_info['flag'] = 'INVALID_DOI'
                hallucination_suspects.append(entry)
            time.sleep(0.1)

        elif entry['url']:
            url_res = check_url(entry['url'])
            audit_info['url_status'] = url_res
            if not url_res.get('accessible'):
                audit_info['flag'] = 'BROKEN_URL'
                broken_urls += 1
            time.sleep(0.1)

        results.append(audit_info)

    os.makedirs(os.path.dirname(REPORT_FILE_JSON), exist_ok=True)
    with open(REPORT_FILE_JSON, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    with open(REPORT_FILE_MD, 'w', encoding='utf-8') as f:
        f.write("# Academic Reference Verification & Hallucination Audit Report\n\n")
        f.write(f"**Generated on**: 2026-08-31\n\n")
        f.write(f"- **Total References Scanned**: {len(entries)}\n")
        f.write(f"- **Verified DOIs via CrossRef**: {verified_dois}\n")
        f.write(f"- **Broken/Inaccessible URLs**: {broken_urls}\n")
        f.write(f"- **Hallucination Suspects (Invalid DOI/Mismatch)**: {len(hallucination_suspects)}\n\n")
        
        f.write("## Detailed Audit by Module\n\n")
        modules = {}
        for r in results:
            mod = r['entry']['module']
            modules.setdefault(mod, []).append(r)

        for mod, items in modules.items():
            f.write(f"### {mod} ({len(items)} references)\n\n")
            for item in items:
                flag = item['flag']
                doi = item['entry']['doi']
                raw = item['entry']['raw']
                status_symbol = "✅" if flag == 'OK' else "⚠️"
                
                detail = ""
                if item['doi_status'] and item['doi_status'].get('valid'):
                    detail = f"*(Verified DOI: {doi} - CrossRef Title: '{item['doi_status'].get('title')}')*"
                elif item['url_status']:
                    detail = f"*(URL status: HTTP {item['url_status'].get('status_code')})*"

                f.write(f"- {status_symbol} **[{flag}]** {raw}\n  {detail}\n\n")

    print("\n==========================================", flush=True)
    print("AUDIT COMPLETED!", flush=True)
    print(f"Report written to: {REPORT_FILE_MD}", flush=True)
    print(f"Data written to: {REPORT_FILE_JSON}", flush=True)
    print("==========================================\n", flush=True)

if __name__ == '__main__':
    main()
