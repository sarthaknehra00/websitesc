import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

config = re.search(r'<script id="tailwind-config">([\s\S]*?)</script>', html)
if config:
    with open('tw.txt', 'w', encoding='utf-8') as f:
        f.write(config.group(1))

# Also extract the Google Fonts URL
fonts = re.findall(r'<link[^>]*fonts\.googleapis\.com[^>]*>', html)
with open('tw.txt', 'a', encoding='utf-8') as f:
    f.write('\n\nFONTS:\n')
    for font in fonts:
        f.write(font + '\n')
