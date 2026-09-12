"""Validate full requested coverage, generated links, IDs and SVG assets."""
import json, re
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'exercise-content/manifest.json').read_text())['sections']
def check_text(value):
    if isinstance(value, str):
        assert not re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]",value), value
        for opening,closing in [("(",")"),("[","]")]:
            pattern=r"(?<!\\)\\"
            assert len(re.findall(pattern+re.escape(opening),value))==len(re.findall(pattern+re.escape(closing),value)),value
    elif isinstance(value, list):
        for item in value: check_text(item)
    elif isinstance(value, dict):
        for item in value.values(): check_text(item)
for path in (ROOT/'exercise-content').glob('s*.json'):
    check_text(json.loads(path.read_text()))
count=0
for row in manifest:
    if row['total'] is None: continue
    assert row['completedNumbers']==row['expectedNumbers'], row['section']
    count+=len(row['completedNumbers'])
assert count==591, count
class Page(HTMLParser):
    def __init__(self): super().__init__(); self.ids=[]; self.links=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        for key in ('href','src'):
            if key in a:self.links.append(a[key])
parsers={}
for p in (ROOT/'exercises').glob('*.html'):
    parser=Page();parser.feed(p.read_text());parsers[p.resolve()]=parser
    assert len(parser.ids)==len(set(parser.ids)),f'duplicate IDs: {p}'
for p,parser in parsers.items():
    for href in parser.links:
        u=urlsplit(href)
        if u.scheme or u.netloc:continue
        dest=(p.parent/unquote(u.path)).resolve() if u.path else p
        assert dest.exists(),f'broken link {p}: {href}'
        if u.fragment and dest in parsers:
            assert u.fragment in parsers[dest].ids,f'bad anchor: {href}'
for p in (ROOT/'exercise-content/assets').glob('*.svg'): ET.parse(p)
for row in manifest:
    s=row['section'].replace('.','-')
    assert f'exercises/s{s}.html' in (ROOT/f's{s}.html').read_text(),s
print(f'PASS: {count} requested exercises, {len(parsers)} generated pages, local links, anchors, SVG XML and entry links')
