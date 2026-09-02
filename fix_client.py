import os

filepath = 'react-app/src/components/ui/bento-grid-01.tsx'
with open(filepath, 'r', encoding='utf-8') as f:
    code = f.read()

if '"use client"' not in code:
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('"use client";\n' + code)
