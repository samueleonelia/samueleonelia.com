#!/usr/bin/env python3
"""Turn index.html into a self-contained page for publishing as a Claude Artifact.

The Artifact host wraps the file in <!doctype html><head></head><body>, so this
script strips our own wrapper tags and inlines assets/portrait.jpg as a data URI
(the Artifact CSP blocks external hosts other than Google Fonts).
"""
import base64
import mimetypes
import pathlib
import re

root = pathlib.Path(__file__).resolve().parent.parent
src = (root / "index.html").read_text(encoding="utf-8")

# inline every local asset referenced with src="..."
def inline(match):
    path = match.group(1)
    if path.startswith(("http", "data:", "//")):
        return match.group(0)
    f = root / path
    if not f.exists():
        raise SystemExit(f"missing asset: {path}")
    mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
    b64 = base64.b64encode(f.read_bytes()).decode("ascii")
    return f'src="data:{mime};base64,{b64}"'

out = re.sub(r'src="([^"]+)"', inline, src)

# drop the document wrapper the Artifact host supplies itself
head = re.search(r"<head>(.*?)</head>", out, re.S).group(1)
body = re.search(r"<body>(.*?)</body>", out, re.S).group(1)

# keep only the head bits that still work inside <body>
keep = re.findall(
    r"(<title>.*?</title>|<link rel=\"stylesheet\"[^>]*>|<style>.*?</style>)", head, re.S
)

dest = root / "build" / "mockup.html"
dest.parent.mkdir(exist_ok=True)
dest.write_text("\n".join(keep) + "\n" + body.strip() + "\n", encoding="utf-8")
print(f"wrote {dest} ({dest.stat().st_size:,} bytes)")
