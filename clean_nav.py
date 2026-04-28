import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

target_string = '<li><a href="#google-ads">Google Ads</a></li>\n'

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target_string in content:
        content = content.replace(target_string, '')
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Removed old google ads link in {html_file}")
