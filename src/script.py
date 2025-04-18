import os
import re

TEMPLATE_DIR = "./searchonclimb/templates"

def fix_extra_quotes(content):
    # Pattern: href="{% url 'name' %}""  → should be href="{% url 'name' %}"
    return re.sub(r'({% url\s+\'[^\']+\'\s*%})["]', r'\1', content)

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    updated_content = fix_extra_quotes(content)
    if updated_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print(f"✅ Fixed quotes: {filepath}")
    else:
        print(f"⏭️ No extra quotes found: {filepath}")

def process_all():
    print("🔍 Scanning for extra quotes after {% url %}...")
    for root, dirs, files in os.walk(TEMPLATE_DIR):
        for file in files:
            if file.endswith(".html"):
                process_file(os.path.join(root, file))
    print("✅ Done fixing invalid quotes.")

if __name__ == "__main__":
    process_all()
