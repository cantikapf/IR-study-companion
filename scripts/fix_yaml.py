import os

d = r'd:\PERSONAL PROJECT\IR-study-companion\_chapters'
c = 0
for r, dirs, files in os.walk(d):
    for f in files:
        if f.endswith('.md'):
            filepath = os.path.join(r, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # replace \' with '
            if r"\'" in content:
                new_content = content.replace(r"\'", "'")
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                c += 1

print(f'Fixed YAML apostrophes in {c} files.')
