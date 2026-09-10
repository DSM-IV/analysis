#!/usr/bin/env python3
"""Regenerate stewart/index.html from SECTIONS table. Edit status/counts here, then run."""
import os, json
HERE = os.path.dirname(os.path.abspath(__file__))
# file, sec, ko, en, week, examples, status(ready|building|planned), concept_count(or None)
SECTIONS = [
 ("s12-6","12.6","주면과 이차곡면","Cylinders and Quadric Surfaces",1,8,"ready",8),
 ("s14-1","14.1","다변수함수","Functions of Several Variables",1,16,"ready",11),
 ("s14-2","14.2","극한과 연속","Limits and Continuity",1,11,"ready",13),
 ("s14-3","14.3","편도함수","Partial Derivatives",1,10,"ready",14),
 ("s14-4","14.4","접평면과 선형근사","Tangent Planes and Linear Approximations",2,6,"ready",10),
 ("s14-5","14.5","연쇄법칙","The Chain Rule",2,9,"ready",10),
 ("s14-6","14.6","방향도함수와 기울기 벡터","Directional Derivatives and the Gradient Vector",2,9,"ready",17),
 ("s14-7","14.7","최댓값과 최솟값","Maximum and Minimum Values",3,7,"ready",13),
 ("s14-8","14.8","라그랑주 승수법","Lagrange Multipliers",3,5,"ready",9),
 ("s15-1","15.1","직사각형 위의 이중적분","Double Integrals over Rectangles",4,9,"ready",12),
 ("s15-2","15.2","일반 영역 위의 이중적분","Double Integrals over General Regions",4,6,"ready",13),
 ("s15-3","15.3","극좌표에서의 이중적분","Double Integrals in Polar Coordinates",5,5,"ready",8),
 ("s15-4","15.4","이중적분의 응용","Applications of Double Integrals",5,8,"ready",15),
 ("s15-5","15.5","곡면 넓이","Surface Area",6,2,"ready",6),
 ("s15-6","15.6","삼중적분","Triple Integrals",6,6,"ready",16),
 ("s15-7","15.7","원기둥좌표에서의 삼중적분","Triple Integrals in Cylindrical Coordinates",7,5,"ready",6),
 ("s15-8","15.8","구면좌표에서의 삼중적분","Triple Integrals in Spherical Coordinates",7,4,"ready",8),
 ("s15-9","15.9","중적분의 변수변환","Change of Variables in Multiple Integrals",8,4,"ready",12),
 ("s16-1","16.1","벡터장","Vector Fields",8,6,"ready",10),
 ("s16-2","16.2","선적분","Line Integrals",9,8,"ready",17),
 ("s16-3","16.3","선적분의 기본정리","The Fundamental Theorem for Line Integrals",10,5,"ready",15),
 ("s16-4","16.4","그린 정리","Green's Theorem",10,5,"ready",12),
 ("s16-5","16.5","회전과 발산","Curl and Divergence",11,5,"ready",13),
 ("s16-6","16.6","매개곡면과 그 넓이","Parametric Surfaces and Their Areas",11,11,"ready",14),
 ("s16-7","16.7","면적분","Surface Integrals",12,6,"ready",21),
 ("s16-8","16.8","스토크스 정리","Stokes' Theorem",13,2,"ready",10),
 ("s16-9","16.9","발산정리","The Divergence Theorem",13,3,"ready",9),
 ("s16-10","16.10","요약","Summary",14,0,"ready",1),
]
CHAPTERS = [("12","12장 · 벡터와 공간기하 (12.6만)","Vectors and the Geometry of Space"),
            ("14","14장 · 편도함수","Partial Derivatives"),
            ("15","15장 · 중적분","Multiple Integrals"),
            ("16","16장 · 벡터해석","Vector Calculus")]
STATUS_LABEL = {"ready":"본문 해석 &amp; 예제 답안","building":"작성 중","planned":"준비 중"}

def esc(s): return s.replace("&","&amp;")

nav_links = "\n".join(f'      <a href="{f}.html">{sec}</a>' for f,sec,*_ in SECTIONS)
cards = []
for ch, ch_ko, ch_en in CHAPTERS:
    items = [s for s in SECTIONS if s[1].split(".")[0]==ch]
    cards.append(f'\n  <div class="section-title" id="ch-{ch}">\n    <h2>{ch_ko}<span style="font-weight:400;color:var(--ink-faint);font-size:.8em;margin-left:.6em">{ch_en}</span></h2>\n  </div>\n\n  <div class="chapter-grid">\n')
    for f,sec,ko,en,week,nex,status,ncon in items:
        cnt = (f"개념 {ncon} · " if ncon else "") + (f"예제 {nex}" if nex else "정리 요약표")
        if status=="ready":
            action = f'<a href="{f}.html">{STATUS_LABEL[status]}</a>'
        elif status=="building":
            action = f'<a href="{f}.html">{STATUS_LABEL[status]}</a>'
        else:
            action = f'<span style="color:var(--ink-faint)">{STATUS_LABEL[status]}</span>'
        cards.append(f'''    <!-- §{sec} -->
    <article class="chapter-card" id="card-{f}">
      <div class="card-top">
        <span class="ch-num">§{sec} · {week}주차</span>
        <h3>{esc(ko)}</h3>
        <p class="ch-en-title">{esc(en)}</p>
        <p class="ch-count" style="font-size:.72rem; color:var(--ink-faint); margin-top:.7rem;">{cnt}</p>
      </div>
      <div class="card-actions">
        {action}
      </div>
    </article>
''')
    cards.append('  </div>\n')
body = "".join(cards)

html = f'''<!DOCTYPE html>
<html lang="ko">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-N702T3QW76"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', 'G-N702T3QW76');
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Stewart 미적분학 교재 노트 — 본문 해석과 예제 답안 | 대학수학생존</title>
<meta name="description" content="Stewart, Calculus: Early Transcendentals 9판 12.6·14–16장(다변수 미적분·중적분·벡터해석)의 정의·정리를 한국어로 해석하고 예제를 자체 풀이한 교재 노트. 강의 노트(미적분학 2)와 별도로 구성.">
<meta name="keywords" content="Stewart, Calculus Early Transcendentals, 9판, 미적분학 2, 다변수 미적분, 편도함수, 중적분, 벡터해석, 예제 풀이, 한국어 해석">
<meta name="author" content="DDALKKAK">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://univmathsurvive.com/stewart/index.html">
<meta property="og:type" content="website">
<meta property="og:title" content="Stewart 미적분학 교재 노트 — 본문 해석과 예제 답안">
<meta property="og:description" content="Stewart Calculus ET 9판 12.6·14–16장의 개념 해석과 예제 145개 자체 풀이.">
<meta property="og:url" content="https://univmathsurvive.com/stewart/index.html">
<meta property="og:locale" content="ko_KR">
<meta property="og:site_name" content="대학수학생존">
<meta name="google-adsense-account" content="ca-pub-1269032424784987">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1269032424784987" crossorigin="anonymous"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link rel="stylesheet" href="style.css">
</head>
<body>

<a href="#main-content" class="skip-link">본문으로 건너뛰기</a>

<nav class="site-nav" aria-label="사이트 탐색">
  <div class="nav-inner">
    <a class="logo" href="../index.html" aria-label="대학수학생존 홈"><span class="logo-mark" aria-hidden="true">√</span>대학수학생존</a>
    <div class="nav-links">
      <a href="index.html" class="active">Stewart</a>
      <a href="../calc2/index.html">미적분학 2 (강의)</a>
      <a href="../settheory/index.html">집합론</a>
      <a href="../analysis2/index.html">해석학2</a>
      <a href="../la2/index.html">선형대수학2</a>
      <a href="../numtheory/index.html">응용정수론</a>
    </div>
  </div>
</nav>

<header>
  <p class="subtitle">Stewart · Calculus: Early Transcendentals 9e</p>
  <h1>Stewart 미적분학 교재 노트<span>Textbook Notes — Chapters 12.6, 14, 15, 16</span></h1>
  <p class="header-desc">교재 본문의 정의·정리·공식을 한국어로 해석하고, 본문 예제를 다시 서술해 직접 풀이한 노트입니다. 강의 노트(<a href="../calc2/index.html">미적분학 2</a>)와는 별도로, 교재 절 순서를 그대로 따릅니다. 표기는 Stewart 원서 규약을 따릅니다.</p>
  <div class="lang-badge">
    <span class="ko">한국어</span>
    <span class="en">English</span>
  </div>
</header>

<main id="main-content">

  <p class="intro-text">절마다 <strong>개념 해석</strong>(정의·정리·주의)과 <strong>예제 답안</strong>(문제 재서술 + 자체 풀이)을 한국어·영어 대조로 정리합니다. 원문 산문은 옮기지 않고 요지만 해석합니다. 주차는 2026-2 강의계획서 기준입니다.</p>
{body}
</main>

<footer class="site-footer">
  <div>
    <a href="../index.html">홈</a>
    <a href="../calc2/index.html">미적분학 2 (강의)</a>
    <a href="../about.html">소개</a>
    <a href="../privacy.html">개인정보처리방침</a>
    <a href="../disclaimer.html">면책조항</a>
  </div>
  <p class="footer-copy">Stewart, <em>Calculus: Early Transcendentals</em>, 9th ed. (Cengage) 의 내용을 학습 목적으로 재서술·해석한 개인 노트입니다. 원문 텍스트·그림은 수록하지 않습니다. &copy; 2025–2026 DDALKKAK.</p>
</footer>

<script src="common.js"></script>
</body>
</html>
'''
open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(html)
print("index.html written:", len(SECTIONS), "sections")
