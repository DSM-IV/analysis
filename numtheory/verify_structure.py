#!/usr/bin/env python3
"""numtheory structure verifier (stdlib only). Usage: python3 numtheory/verify_structure.py [files...]"""
import re, sys, glob, os
from html.parser import HTMLParser

class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.err = None
    def error(self, msg): self.err = msg

def check(path):
    s = open(path, encoding='utf-8').read()
    name = os.path.basename(path)
    r = {}
    r['div_open'] = len(re.findall(r'<div\b', s)); r['div_close'] = s.count('</div>')
    nav = re.search(r'<nav class="site-nav".*?</nav>', s, re.S)
    r['nav_active'] = nav.group(0).count('class="active"') if nav else -1
    r['cards'] = len(re.findall(r'<div class="card (?:def|thm|rem|exam|ex)-card" id="(?:c\d+-\d+[dt]?|rem\d+)"', s))
    r['ex_cards'] = len(re.findall(r'<div class="card ex-card" id="c\d+-\d+"', s))
    r['algo_cards'] = len(re.findall(r'<div class="card algo-card" id="algo\d+-\d+"', s))
    r['part2_markers'] = s.count('<!-- PROOF-KO-PART2 -->') + s.count('<!-- PROOF-EN-PART2 -->')
    r['notes'] = len(re.findall(r'<div class="card note-card"', s))
    r['toc_li'] = len(re.findall(r'<li><a href="#', s))
    r['PROOF_KO'] = s.count('<!-- PROOF-KO -->'); r['PROOF_EN'] = s.count('<!-- PROOF-EN -->')
    r['placeholder'] = s.count('[번역 예정]')
    r['ko_toggles'] = s.count('data-show="증명 보기"') + s.count('data-show="풀이 보기"')
    r['en_toggles'] = s.count('data-show="Proof"') + s.count('data-show="Solution"')
    r['qed'] = s.count('<div class="qed">')
    # ids unique
    ids = re.findall(r' id="([^"]+)"', re.sub(r'<!--.*?-->', '', s, flags=re.S))
    dup = sorted({i for i in ids if ids.count(i) > 1})
    r['dup_ids'] = dup
    # '<' followed by letter inside math
    bad = []
    for m in re.finditer(r'\$\$(.+?)\$\$|\$(.+?)\$', s, re.S):
        seg = m.group(1) or m.group(2)
        if re.search(r'<[A-Za-z]', seg): bad.append(seg[:60])
    r['lt_letter_in_math'] = bad[:5]
    # Korean in en-panel (outside comments)
    ko_in_en = []
    for m in re.finditer(r'<div class="en-panel".*?</div>\s*</div>\s*</div>', s, re.S):
        seg = re.sub(r'<!--.*?-->', '', m.group(0), flags=re.S)
        if re.search(r'[가-힣]', seg): ko_in_en.append(re.search(r'[가-힣]+', seg).group(0))
    r['korean_in_en_panels'] = len(ko_in_en)
    # banned terms
    banned = ['유클리드 알고리즘', '모듈로', '컨버전트', '수렴자', '오일러 파이', '토션트', '원시원소', '유니타리', '역수', '나눗셈 정리', '정수 해']
    r['banned'] = {b: s.count(b) for b in banned if s.count(b)}
    p = P()
    try: p.feed(s); p.close()
    except Exception as e: p.err = str(e)
    r['html_parse'] = p.err or 'ok'
    return name, r

if __name__ == '__main__':
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(os.path.dirname(__file__), 'ch*.html')) + glob.glob(os.path.join(os.path.dirname(__file__), 'index.html')))
    for f in files:
        name, r = check(f)
        flags = []
        if r['div_open'] != r['div_close']: flags.append('DIV-IMBALANCE')
        if r['nav_active'] != 1: flags.append('NAV-ACTIVE')
        if r['PROOF_KO'] != r['PROOF_EN']: flags.append('MARKER-ASYM')
        if r['dup_ids']: flags.append('DUP-IDS')
        if r['lt_letter_in_math']: flags.append('LT-LETTER')
        if r['banned']: flags.append('BANNED')
        if r['html_parse'] != 'ok': flags.append('PARSE')
        if r['korean_in_en_panels']: flags.append('KO-IN-EN')
        print(f"{name}: {'OK' if not flags else ' '.join(flags)}")
        for k, v in r.items(): print(f"   {k}: {v}")
