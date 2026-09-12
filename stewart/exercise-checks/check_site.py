"""Validate ordinary Exercises only: coverage, links, IDs and referenced SVGs."""
import json, re, argparse
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import xml.etree.ElementTree as ET
args=argparse.ArgumentParser()
args.add_argument('--allow-partial',action='store_true')
args=args.parse_args()
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'exercise-content/manifest.json').read_text())['sections']
BASELINE_COUNTS={'12.6': 55, '14.1': 81, '14.2': 59, '14.3': 101, '14.4': 54, '14.5': 60, '14.6': 77, '14.7': 62, '14.8': 63, '15.1': 58, '15.2': 82, '15.3': 51, '15.4': 35, '15.5': 26, '15.6': 59, '15.7': 33, '15.8': 51, '15.9': 31, '16.1': 40, '16.2': 54, '16.3': 42, '16.4': 35, '16.5': 41, '16.6': 64, '16.7': 49, '16.8': 24, '16.9': 34}
by_section={row['section']:row for row in manifest}
assert len(by_section)==len(manifest), 'duplicate manifest sections'
for section,total in BASELINE_COUNTS.items():
    assert section in by_section and by_section[section]['total']==total, f'missing or changed required section: {section}'
expected_total=sum(len(row['expectedNumbers']) for row in manifest)
assert all(row['total']==len(row['expectedNumbers']) for row in manifest), 'inconsistent expected inventory'
assert all(row.get('kind','exercise')=='exercise' for row in manifest), 'non-Exercise entry in manifest'
assets=set()
def check_text(value):
    if isinstance(value, str):
        assert not re.search(r"(?<!\\)\\(?:theta|phi|rho|alpha|beta|gamma)[a-z]+",value),value
        assert not re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]",value), value
        for opening,closing in [("(",")"),("[","]")]:
            pattern=r"(?<!\\)\\"
            assert len(re.findall(pattern+re.escape(opening),value))==len(re.findall(pattern+re.escape(closing),value)),value
    elif isinstance(value, list):
        for item in value: check_text(item)
    elif isinstance(value, dict):
        if "en" in value:
            english = value["en"] if isinstance(value["en"], list) else [value["en"]]
            assert all(not re.search("[가-힣]", text) for text in english), english
        for item in value.values(): check_text(item)
for row in manifest:
    path=ROOT/'exercise-content'/('s'+row['section'].replace('.','-').replace("*", "-alt")+'.json')
    if not path.exists() and args.allow_partial: continue
    document=json.loads(path.read_text())
    assert document.get('kind',document.get('scope',{}).get('kind','exercise'))=='exercise',path
    check_text(document)
    for exercise in document['exercises']:
        if 'figure' in exercise:
            assets.add((ROOT/'exercises'/exercise['figure']['src']).resolve())
count=0
for row in manifest:
    if row['total'] is None: continue
    if not args.allow_partial:
        assert row['completedNumbers']==row['expectedNumbers'], row['section']
    count+=len(row['completedNumbers'])
assert sum(row['total'] for row in manifest)==expected_total, 'unexpected inventory total'
if not args.allow_partial: assert count==expected_total,count
class Page(HTMLParser):
    def __init__(self): super().__init__(); self.ids=[]; self.links=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        for key in ('href','src'):
            if key in a:self.links.append(a[key])
parsers={}
pages=[ROOT/'exercises/index.html']+[ROOT/'exercises'/('s'+row['section'].replace('.','-').replace("*", "-alt")+'.html') for row in manifest if row['completedNumbers']]
pages += [ROOT.parent/"calc1/index.html", ROOT.parent/"calc1/stewart.html"]
for p in pages:
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
for p in assets:
    if p.suffix.lower()=='.svg': ET.parse(p)
for row in manifest:
    s=row['section'].replace('.','-').replace("*", "-alt")
    if (ROOT/f's{s}.html').exists():
        assert f'exercises/s{s}.html' in (ROOT/f's{s}.html').read_text(),s
    elif row['completedNumbers']:
        assert f's{s}.html' in (ROOT/'exercises/index.html').read_text(),s
print(f'PASS: {count} requested exercises, {len(parsers)} site pages, local links, anchors, SVG XML and entry links')
