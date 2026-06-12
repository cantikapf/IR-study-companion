import os
import glob
from html.parser import HTMLParser

class LinkChecker(HTMLParser):
    def __init__(self, filepath):
        super().__init__()
        self.links = []
        self.filepath = filepath
        
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, val in attrs:
                if attr == 'href' and not val.startswith(('http', 'mailto:', 'tel:', '#')):
                    self.links.append(val)

def check_site(site_dir):
    html_files = glob.glob(os.path.join(site_dir, '**/*.html'), recursive=True)
    valid_paths = [os.path.relpath(p, site_dir).replace('\\', '/') for p in html_files]
    # Also add '/' and '/index.html'
    valid_paths.extend(['/', '/index.html', ''])
    
    broken_links = []
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        parser = LinkChecker(filepath)
        parser.feed(content)
        
        for link in parser.links:
            # Strip query params or hash
            clean_link = link.split('?')[0].split('#')[0]
            # Strip leading slash
            if clean_link.startswith('/'):
                clean_link = clean_link[1:]
                
            if clean_link == '':
                continue
                
            if clean_link not in valid_paths and clean_link + '/index.html' not in valid_paths and clean_link + '.html' not in valid_paths:
                # One last check if it's pointing to assets
                asset_path = os.path.join(site_dir, clean_link)
                if not os.path.exists(asset_path):
                    broken_links.append((filepath, link))
                    
    if broken_links:
        print(f"Found {len(broken_links)} broken internal links:")
        for fp, link in broken_links:
            print(f"File: {fp} -> Broken Link: {link}")
        return 1
    else:
        print("All internal links are valid!")
        return 0

if __name__ == '__main__':
    import sys
    sys.exit(check_site('_site'))
