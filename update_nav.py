import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

target_string = '<li><a href="agencia-de-redes-sociales.html">Redes Sociales</a></li>'
replacement_string = '<li><a href="agencia-de-redes-sociales.html">Redes Sociales</a></li>\n                        <li><a href="agencia-de-google-ads.html">Google Ads</a></li>'

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target_string in content and 'agencia-de-google-ads.html' not in content:
        content = content.replace(target_string, replacement_string)
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated nav menu in {html_file}")
    else:
        print(f"No changes needed for {html_file}")
