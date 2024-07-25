import os
from bs4 import BeautifulSoup

output_file = "index.html"
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != output_file]

with open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Index of HTML Files</title>\n</head>\n<body>\n")
    outfile.write("<h1>Index of HTML Files</h1>\n<ul>\n")
    for fname in html_files:
        with open(fname, 'r', encoding='utf-8') as infile:
            soup = BeautifulSoup(infile, 'html.parser')
            title_tag = soup.find('title')
            title = title_tag.string if title_tag else fname
            outfile.write(f'<li><a href="{fname}">{title}</a></li>\n')
    outfile.write("</ul>\n</body>\n</html>")

print(f"Created {output_file} with links to {len(html_files)} HTML files.")