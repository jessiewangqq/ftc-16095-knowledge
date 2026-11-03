#!/usr/bin/env python3
"""Check local Markdown links; no network, dependencies, or file writes."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
checked = 0
links = 0
for page in sorted(ROOT.rglob('*.md')):
    if '.git' in page.parts:
        continue
    checked += 1
    raw = page.read_text(encoding='utf-8')
    text = re.sub(r'^(```|~~~).*?^\1\s*$', '', raw, flags=re.M | re.S)
    if re.search(r'(?:/Users/[^/\s]+/|/home/[^/\s]+/)', raw):
        errors.append((page, '包含本机用户目录的绝对路径'))
    if re.search(r'\[\[[^\]]+\]\]', text):
        errors.append((page, '使用了 GitHub 不支持的 Obsidian 双括号链接'))
    pattern = r'!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+"[^"]*")?\s*\)'
    for match in re.finditer(pattern, text):
        target = match.group(1).strip('<>')
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        links += 1
        dest = (page.parent / unquote(parsed.path)).resolve()
        try:
            dest.relative_to(ROOT)
        except ValueError:
            errors.append((page, '链接跳出了本仓库：' + target))
            continue
        if not dest.exists():
            errors.append((page, '库内链接不存在：' + target))
if errors:
    for page, message in errors:
        print(str(page.relative_to(ROOT)) + ': ' + message)
    print(f'未通过：检查 {checked} 个 Markdown 文件、{links} 个库内链接，发现 {len(errors)} 项问题。')
    sys.exit(1)
print(f'通过：检查 {checked} 个 Markdown 文件、{links} 个库内文件链接。外部网址、页内锚点和内容准确性需另行核对。')
