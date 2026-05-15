import os

files = [f for f in os.listdir('.') if f.endswith('.html')]
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'href="index.html#seo"' in content:
        content = content.replace('href="index.html#seo"', 'href="agencia-seo.html"')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated links in {file}")

