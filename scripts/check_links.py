import os
import re

def check_links():
    base_dir = r'd:\PERSONAL PROJECT\IR-study-companion'
    chapters_dir = os.path.join(base_dir, '_chapters')
    pages_dir = os.path.join(base_dir, '_pages')
    site_dir = os.path.join(base_dir, '_site')
    
    # regex for markdown links [text](link) and images ![alt](link)
    link_regex = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    img_regex = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
    
    # HTML links <a href="...">
    html_link_regex = re.compile(r'href=[\'"]?([^\'" >]+)')
    html_img_regex = re.compile(r'src=[\'"]?([^\'" >]+)')
    
    broken_links = []
    
    def check_file(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        links = []
        links.extend([m[1] for m in link_regex.findall(content)])
        links.extend([m[1] for m in img_regex.findall(content)])
        links.extend(html_link_regex.findall(content))
        links.extend(html_img_regex.findall(content))
        
        for link in links:
            if link.startswith('http') or link.startswith('mailto') or link.startswith('#') or link.startswith('{{'):
                continue # Skip external, mailto, anchor links, and liquid tags
            
            # remove hash fragments and query params
            clean_link = link.split('#')[0].split('?')[0]
            if not clean_link:
                continue
                
            # resolve path
            if clean_link.startswith('/'):
                # absolute to base
                # in jekyll base is usually site_dir or just assume it maps to root
                target = os.path.join(base_dir, clean_link.lstrip('/'))
            else:
                # relative
                target = os.path.normpath(os.path.join(os.path.dirname(filepath), clean_link))
                
            # Check if file exists in source
            if not os.path.exists(target):
                # Also check if it's a generated HTML file slug (e.g. /study-of-international-relations.html)
                # We can just check if it exists in _site
                site_target = os.path.join(site_dir, clean_link.lstrip('/'))
                if not os.path.exists(site_target):
                    broken_links.append((filepath, link))
                    
    for root, _, files in os.walk(chapters_dir):
        for f in files:
            if f.endswith('.md') or f.endswith('.html'):
                check_file(os.path.join(root, f))
                
    for root, _, files in os.walk(pages_dir):
        for f in files:
            if f.endswith('.md') or f.endswith('.html'):
                check_file(os.path.join(root, f))
                
    if broken_links:
        print(f"Found {len(broken_links)} potentially broken internal links:")
        for file, link in broken_links[:50]:
            print(f"- {file}: {link}")
    else:
        print("All internal links look good!")

if __name__ == '__main__':
    check_links()
