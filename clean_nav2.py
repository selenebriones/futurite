import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(r'\s*<li><a href="index\.html#google-ads">Google Ads</a></li>', '', content)
    new_content = re.sub(r'\s*<li><a href="#google-ads">Google Ads</a></li>', '', new_content)
    
    if new_content != content:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed old google ads link in {html_file}")
