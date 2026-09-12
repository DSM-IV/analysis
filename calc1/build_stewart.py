"""Build the Calculus 1 landing page from the approved Stewart ledger."""
from pathlib import Path
import json,html,argparse
R=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
rows=[r for r in json.loads((R/'stewart/exercise-content/manifest.json').read_text())['sections'] if int(r['section'].split('.')[0])<=13 and r.get('kind','exercise')=='exercise']
count=sum(len(r['completedNumbers']) for r in rows)
cards=[]
for r in rows:
 if not r['completedNumbers']:continue
 s=r['section']; title=r.get('title',{'ko':'연습문제','en':'Exercises'})
 cards.append(f'''<article class="chapter-card"><div class="card-top"><span class="ch-num">§{html.escape(s)}</span><h3>{html.escape(title['ko'])}</h3><p class="ch-en-title">{html.escape(title['en'])}</p><p class="ch-count">{len(r['completedNumbers'])}문항 · 한국어·English</p></div><div class="card-actions"><a href="../stewart/exercises/s{s.replace('.','-').replace("*", "-alt")}.html">문제와 해설</a></div></article>''')
page='''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>미적분학 1 · Stewart Exercises와 해설</title><link rel="stylesheet" href="style.css"><link rel="canonical" href="https://univmathsurvive.com/calc1/stewart.html"></head><body>
<a href="#main-content" class="skip-link">본문으로 건너뛰기</a>
<nav class="site-nav"><div class="nav-inner"><a class="logo" href="../index.html">√ 대학수학생존</a><div class="nav-links"><a href="index.html">미적분학 1</a><a href="stewart.html" class="active">Stewart Exercises</a><a href="../stewart/exercises/index.html">전체 연습문제</a></div></div></nav>
<header><p class="subtitle">Stewart · Calculus · Ninth Edition</p><h1>미적분학 1 · 교재 연습문제<span>Exercises and Solutions</span></h1><p class="header-desc">1–13장의 일반 Exercises를 절별로 제공합니다. 문제 요약, 힌트, 단계별 풀이와 검산을 한국어·영어로 읽을 수 있습니다.</p><p class="header-desc">현재 공개: COUNT문항 · 나머지 절은 작성·검산을 마치는 대로 추가합니다.</p></header>
<main id="main-content"><div class="section-title"><h2>공개된 절</h2></div><div class="chapter-grid">CARDS</div></main>
<footer class="site-footer"><div><a href="index.html">미적분학 1</a><a href="../index.html">홈</a></div><p class="footer-copy">문제는 학습 목적으로 요약하고 해설과 그림은 직접 작성했습니다.</p></footer></body></html>
'''.replace('COUNT',f'{count:,}').replace('CARDS','\n'.join(cards))
p=R/'calc1/stewart.html'
if args.check:assert p.read_text()==page,'stale calc1/stewart.html'
else:p.write_text(page)
print(f'Calculus 1: {len(cards)} sections, {count} exercises')
