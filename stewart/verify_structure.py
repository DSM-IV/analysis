#!/usr/bin/env python3
"""stewart/ structure verifier (stdlib only). Usage: python3 stewart/verify_structure.py [files...]"""
import re, sys, glob, os
from html.parser import HTMLParser

class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.err = None
    def error(self, msg): self.err = msg

BANNED_KO = ['잠재함수', '유출', '원통좌표', '타원형 포물면', '컬 ', '다이버전스', '그래디언트', '그라디언트', '순환밀도', '발산밀도']
BANNED_TEX = [r'd\sigma', r'M\mathbf{i}+N\mathbf{j}', r'M\,\mathbf{i}+N\,\mathbf{j}', r'\iiint_D', r'd\rho\,d\phi\,d\theta', r'd\rho\, d\phi\, d\theta']
BANNED_EN = ["Stoke's", 'Green theorem', 'Fubini theorem']

def check(path):
    s = open(path, encoding='utf-8').read()
    name = os.path.basename(path)
    r = {}
    r['div_open'] = len(re.findall(r'<div\b', s)); r['div_close'] = s.count('</div>')
    nav = re.search(r'<nav class="site-nav".*?</nav>', s, re.S)
    r['nav_active'] = nav.group(0).count('class="active"') if nav else -1
    r['concept_cards'] = len(re.findall(r'<div class="card (?:def|thm|rem|note)-card" id="c\d+-\d+-\d+"', s))
    r['def'] = len(re.findall(r'<div class="card def-card"', s))
    r['thm'] = len(re.findall(r'<div class="card thm-card"', s))
    r['rem'] = len(re.findall(r'<div class="card rem-card"', s))
    r['note'] = len(re.findall(r'<div class="card note-card"', s))
    r['exam_cards'] = len(re.findall(r'<div class="card exam-card" id="ex\d+-\d+-\d+"', s))
    r['toc_li'] = len(re.findall(r'<li><a href="#', s))
    r['PROOF_KO'] = s.count('<!-- PROOF-KO -->'); r['PROOF_EN'] = s.count('<!-- PROOF-EN -->')
    r['placeholder'] = s.count('[번역 예정]') + s.count('[해석 예정]')
    r['ko_toggles'] = s.count('data-show="증명 보기"') + s.count('data-show="풀이 보기"')
    r['en_toggles'] = s.count('data-show="Proof"') + s.count('data-show="Solution"')
    r['qed'] = s.count('<div class="qed">')
    r['src_ref'] = s.count('class="src-ref"')
    r['svg'] = len(re.findall(r'<svg\b', s))
    ids = re.findall(r' id="([^"]+)"', re.sub(r'<!--.*?-->', '', s, flags=re.S))
    r['dup_ids'] = sorted({i for i in ids if ids.count(i) > 1})
    bad = []
    for m in re.finditer(r'\$\$(.+?)\$\$|\$(.+?)\$', s, re.S):
        seg = m.group(1) or m.group(2)
        if re.search(r'<[A-Za-z]', seg): bad.append(seg[:60])
    r['lt_letter_in_math'] = bad[:5]
    ko_in_en = 0
    for m in re.finditer(r'<div class="en-panel".*?</div>\s*</div>\s*</div>', s, re.S):
        seg = re.sub(r'<!--.*?-->', '', m.group(0), flags=re.S)
        seg = re.sub(r'<svg\b.*?</svg>', '', seg, flags=re.S)
        if re.search(r'[가-힣]', seg): ko_in_en += 1
    r['korean_in_en_panels'] = ko_in_en
    body = re.sub(r'<!--.*?-->', '', s, flags=re.S)
    banned = {}
    for b in BANNED_KO + BANNED_TEX + BANNED_EN:
        c = body.count(b)
        if c: banned[b] = c
    r['banned'] = banned
    p = P()
    try: p.feed(s); p.close()
    except Exception as e: p.err = str(e)
    r['html_parse'] = p.err or 'ok'
    return name, r

if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(here, 's*.html')) + glob.glob(os.path.join(here, 'index.html')))
    for f in files:
        name, r = check(f)
        flags = []
        if r['div_open'] != r['div_close']: flags.append('DIV-IMBALANCE')
        if r['nav_active'] != 1: flags.append('NAV-ACTIVE')
        if r['PROOF_KO'] != r['PROOF_EN']: flags.append('MARKER-ASYM')
        if r['ko_toggles'] != r['en_toggles']: flags.append('TOGGLE-ASYM')
        if r['dup_ids']: flags.append('DUP-IDS')
        if r['lt_letter_in_math']: flags.append('LT-LETTER')
        if r['banned']: flags.append('BANNED')
        if r['html_parse'] != 'ok': flags.append('PARSE')
        if r['korean_in_en_panels']: flags.append('KO-IN-EN')
        print(f"{name}: {'OK' if not flags else ' '.join(flags)}")
        for k, v in r.items(): print(f"   {k}: {v}")
