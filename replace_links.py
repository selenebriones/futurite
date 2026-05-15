import os
import glob

files = glob.glob('/Users/selene/Documents/Futurite/*.html')
for f in files:
    with open(f, 'r') as file:
        content = file.read()
        
    new_content = content.replace('"index.html#ecommerce"', '"comercio-electronico.html"').replace('"#ecommerce"', '"comercio-electronico.html"')
    
    if new_content != content:
        with open(f, 'w') as file:
            file.write(new_content)
        print(f"Updated {f}")

