import os
import re

TEMPLATE_DIR = './searchonclimb/templates'
STATIC_PREFIX = 'core/'

# Match inline CSS background-image URLs (within style="background-image: url(...)")
inline_css_pattern = re.compile(
    r'(<[^>]*?style=["\'][^"\']*?background-image:\s*url\(["\']?)([^"\')]+)(["\']?\)[^>]*?>)',
    re.IGNORECASE
)

def wrap_static_inline_css(match):
    before = match.group(1)
    path = match.group(2)
    after = match.group(3)

    # Only update local paths (not URLs starting with http://, https://, etc.)
    if not path.startswith(('http', 'https', 'mailto', 'tel')):
        # Wrap path in the {% static %} tag
        django_path = f"{{% static '{STATIC_PREFIX}{path}' %}}"
        return f"{before}{django_path}{after}"
    return match.group(0)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Update inline CSS background-image urls
    updated_content = re.sub(inline_css_pattern, wrap_static_inline_css, content)

    if updated_content != content:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(updated_content)
        print(f"✅ Updated: {filepath}")
    else:
        print(f"⏭️ No change: {filepath}")

def process_all():
    for root, _, files in os.walk(TEMPLATE_DIR):
        for file in files:
            if file.endswith('.html'):
                process_file(os.path.join(root, file))

if __name__ == '__main__':
    print("🔧 Running static asset updater for inline CSS background images...")
    process_all()
    print("✅ All done.")
