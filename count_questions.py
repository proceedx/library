#!/usr/bin/env python3
import os, re

output_dir = "."
results = []

for d in os.listdir(output_dir):
    if not os.path.isdir(d) or d == '.git':
        continue
    html_path = os.path.join(d, 'index.html')
    if not os.path.exists(html_path):
        continue
    try:
        content = open(html_path, encoding='utf-8').read()
        # "q": " または "term": " の数を数える
        count = len(re.findall(r'"q":\s*"', content)) + len(re.findall(r'"term":\s*"', content))
        results.append((d, count))
    except:
        results.append((d, 0))

results.sort()
for name, count in results:
    print(f"{name},{count}")
