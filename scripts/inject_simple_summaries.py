import os
import re

chapters_dir = r'd:\PERSONAL PROJECT\IR-study-companion\_chapters'

# Dictionary mapping keywords to their respective summaries
SUMMARY_MAPPINGS = {
    ('law', 'treaty', 'wto', 'settlement', 'dispute'): 
        "Think of this chapter like the rules of a playground. Without rules, kids might fight or take each other's toys. In the world, countries need rules (called International Law) so they know how to trade, travel, and solve arguments without going to war!",
    ('economy', 'economic', 'trade', 'development', 'wealth', 'growth', 'poverty'): 
        "Imagine the world as a giant marketplace where everyone is buying and trading snacks. This chapter explains how countries make money, trade their 'snacks' (goods and services), and why some countries end up with more snacks than others.",
    ('security', 'war', 'military', 'force', 'cyber', 'conflict'): 
        "Why do countries sometimes fight? Imagine two kids who don't trust each other and start building pillow forts to protect themselves. This chapter explores why countries build armies, how they feel threatened, and what they do to stay safe from bullies.",
    ('organization', 'un ', 'asean', 'institution', 'regionalism', 'united nations'): 
        "Have you ever been in a school club where everyone has to vote on what to do? International Organizations are exactly like that, but for countries! They join big clubs like the UN or ASEAN so they can sit at a round table and work together to fix big problems.",
    ('diplomacy', 'foreign policy', 'negotiation', 'statecraft'): 
        "Diplomacy is basically the art of talking things out instead of fighting. Think of diplomats as the 'peacemakers' or 'messengers' who travel to other schools (countries) to make friends, trade things, and say 'please' and 'thank you'.",
    ('theory', 'realism', 'liberalism', 'marxism', 'method', 'science', 'research', 'perspective'): 
        "This chapter gives you a pair of 'magic glasses' to look at the world. Different glasses (theories) make you see things differently. Some glasses make you see the world as a scary place where everyone is fighting, while others make you see it as a place where people love to cooperate!",
    ('globalization', 'issues', 'media', 'environment', 'disaster', 'politics', 'populism'): 
        "The world is shrinking! Because of the internet, airplanes, and trade, a problem in one side of the world (like a sick person or a polluted river) can quickly become everyone's problem. This chapter shows how everything is connected like a giant spider web.",
    ('history', 'evolution', 'origins', 'renaissance', 'cold war', 'past'): 
        "To understand why the world is the way it is today, we have to hop in a time machine. This chapter tells the story of how old kings, past wars, and ancient empires shaped the borders and the rules we use right now."
}

DEFAULT_SUMMARY = "Think of this chapter as an important puzzle piece. It explains a special part of how countries interact, make decisions, and affect your daily life, even if you don't realize it yet!"

def get_simple_summary(title):
    t = title.lower()
    for keywords, summary in SUMMARY_MAPPINGS.items():
        if any(keyword in t for keyword in keywords):
            return summary
    return DEFAULT_SUMMARY

def process_frontmatter(content, summary):
    """Safely injects simple_summary into the YAML frontmatter block."""
    if 'simple_summary:' in content:
        return content # Skip if already present

    # Regex to match the YAML block between the first two '---' markers safely
    match = re.match(r'^(---.*?---)', content, re.DOTALL)
    if not match:
        return content # Could not find valid frontmatter block
    
    frontmatter_block = match.group(1)
    new_property = f'\nsimple_summary: "{summary}"\n'

    # Inject right after abstract if abstract exists, else inject before the closing '---'
    if 'abstract:' in frontmatter_block:
        # Match 'abstract: ...' up to the next key or end of frontmatter
        new_frontmatter = re.sub(
            r'(\nabstract:.*?)(?=\n[a-z_]+:|\n---$)', 
            rf'\g<1>{new_property}', 
            frontmatter_block, 
            flags=re.DOTALL
        )
    else:
        # Append before the last '---' ensuring proper line breaks
        new_frontmatter = re.sub(r'\n*---$', rf'{new_property}---', frontmatter_block)

    return content.replace(frontmatter_block, new_frontmatter, 1)

if __name__ == "__main__":
    count = 0
    for r, dirs, files in os.walk(chapters_dir):
        for f in files:
            if f.endswith('.md') and not f.startswith('000-'):
                filepath = os.path.join(r, f)
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
                if match:
                    title = match.group(1).strip()
                    summary = get_simple_summary(title)
                    new_content = process_frontmatter(content, summary)
                    
                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as file:
                            file.write(new_content)
                        count += 1

    print(f"Successfully injected In Simple Words summaries into {count} chapters.")
