#!/usr/bin/env python3
"""Build stewart/exams/ pages from data/<id>.html (problems) and solutions/<id>.html.

data/<id>.html     <exam ...> <problem n= pts= sec= title-ko= title-en=> <en>..</en> <ko>..</ko> [<fig>svg</fig>] </problem> </exam>
solutions/<id>.html <sol n="1" lang="ko">..</sol> <sol n="1" lang="en">..</sol>

Run: python3 stewart/exams/build_exams.py   (writes <id>.html for every data file + index.html)
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://univmathsurvive.com/stewart/exams/"

# 표시 순서: 중간 → 기말, 최신 연도부터
EXAMS = [
    ("2025-midterm", "2025 중간고사", "Midterm · Fall 2025", "25 중간"),
    ("2024-midterm", "2024 중간고사", "Midterm · Fall 2024", "24 중간"),
    ("2022-midterm-b1", "2022 중간고사 · 블럭 1", "Midterm · Fall 2022 · Block 1", "22 중간①"),
    ("2022-midterm-b2", "2022 중간고사 · 블럭 2", "Midterm · Fall 2022 · Block 2", "22 중간②"),
    ("2025-final", "2025 기말고사", "Final · Fall 2025", "25 기말"),
    ("2024-final", "2024 기말고사", "Final · Fall 2024", "24 기말"),
    ("2022-final-b1", "2022 기말고사 · 블럭 1", "Final · Fall 2022 · Block 1", "22 기말①"),
    ("2022-final-b2", "2022 기말고사 · 블럭 2", "Final · Fall 2022 · Block 2", "22 기말②"),
]

# 2026-2 강의계획서 기준 시험 범위
MIDTERM_SCOPE = {"12.6"} | {f"14.{i}" for i in range(1, 9)} | {f"15.{i}" for i in range(1, 9)}
FINAL_SCOPE = {"15.9", "matrix"} | {f"16.{i}" for i in range(1, 11)}
CONCEPT_PAGES = {"12.6"} | {f"14.{i}" for i in range(1, 9)} | {f"15.{i}" for i in range(1, 10)} | {f"16.{i}" for i in range(1, 11)}

ATTR = re.compile(r'([\w-]+)="(.*?)"', re.S)


def attrs(s):
    return {k: v for k, v in ATTR.findall(s)}


def parse_exam(eid):
    src = (ROOT / "data" / f"{eid}.html").read_text(encoding="utf-8")
    m = re.search(r"<exam\b(.*?)>", src, re.S)
    meta = attrs(m.group(1))
    probs = []
    for pm in re.finditer(r"<problem\b(.*?)>(.*?)</problem>", src, re.S):
        a = attrs(pm.group(1))
        body = pm.group(2)
        en = re.search(r"<en>(.*?)</en>", body, re.S).group(1).strip()
        ko = re.search(r"<ko>(.*?)</ko>", body, re.S).group(1).strip()
        fig = re.search(r"<fig>(.*?)</fig>", body, re.S)
        probs.append({
            "n": a["n"], "pts": a["pts"], "secs": a["sec"].split(),
            "title_ko": a["title-ko"], "title_en": a["title-en"],
            "en": en, "ko": ko, "fig": fig.group(1).strip() if fig else "",
            "orig": a.get("orig", "en"),
        })
    sols = {}
    sp = ROOT / "solutions" / f"{eid}.html"
    if sp.exists():
        for sm in re.finditer(r'<sol n="(\d+)" lang="(ko|en)">(.*?)</sol>', sp.read_text(encoding="utf-8"), re.S):
            sols[(sm.group(1), sm.group(2))] = sm.group(3).strip()
    return meta, probs, sols


def sec_name(s):
    return "행렬" if s == "matrix" else f"§{s}"


def sec_key(s):
    return (99, 0) if s == "matrix" else tuple(map(int, s.split(".")))


def sec_label(secs):
    return ", ".join(sec_name(s) for s in secs)


def scope_badge(kind, secs):
    scope = MIDTERM_SCOPE if kind == "midterm" else FINAL_SCOPE
    if all(s in scope for s in secs):
        return ""
    other = "중간" if kind == "final" else "기말"
    return f'<span class="scope-badge" title="2026-2 강의계획서 기준">올해는 {other} 범위</span>'


HEAD = """<!DOCTYPE html>
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
<title>{title} | Stewart 미적분학 교재 노트</title>
<meta name="description" content="{desc}">
<meta name="author" content="DDALKKAK">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="ko_KR">
<meta property="og:site_name" content="대학수학생존">
<meta name="google-adsense-account" content="ca-pub-1269032424784987">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1269032424784987" crossorigin="anonymous"></script>
{mathjax}<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link rel="stylesheet" href="../style.css">
<link rel="stylesheet" href="../exercises/exercise.css">
<link rel="stylesheet" href="exams.css">
</head>
<body>

<a href="#main-content" class="skip-link">본문으로 건너뛰기</a>
"""

MATHJAX = """<script>
MathJax = {
  tex: {inlineMath: [['\\\\(', '\\\\)']], displayMath: [['\\\\[', '\\\\]']], packages: {'[+]': ['ams']}},
  options: {skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre']}
};
</script>
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-chtml.min.js"></script>
"""

FOOTER = """
<footer class="site-footer">
  <div>
    <a href="../../index.html">홈</a>
    <a href="../index.html">Stewart 홈</a>
    <a href="../exercises/index.html">연습문제</a>
    <a href="index.html">기출문제</a>
    <a href="../../about.html">소개</a>
    <a href="../../privacy.html">개인정보처리방침</a>
  </div>
  <p class="footer-copy">고려대학교 미적분학및연습II(MATH162) 지난 시험지의 문제와 자체 작성 풀이입니다. 공식 해설이 아니며, 오류를 발견하면 알려 주세요.</p>
</footer>

<script src="../common.js"></script>
<button class="scroll-top" id="scrollTop" type="button" onclick="window.scrollTo({top:0,behavior:'smooth'})" aria-label="맨 위로">&#8593;</button>
</body>
</html>
"""


def nav(active_id, available):
    links = [
        '<a href="../index.html">Stewart</a>',
        '<a href="../exercises/index.html">연습문제</a>',
        '<a href="index.html" class="active">기출</a>' if active_id == "index" else '<a href="index.html">기출</a>',
        '<span class="nav-sep">·</span>',
    ]
    for eid, _, _, short in EXAMS:
        if eid in available:
            cls = ' class="active"' if eid == active_id else ""
            links.append(f'<a href="{eid}.html"{cls}>{short}</a>')
    return f"""<nav class="site-nav" aria-label="사이트 탐색">
  <div class="nav-inner">
    <a class="logo" href="../../index.html" aria-label="대학수학생존 홈"><span class="logo-mark" aria-hidden="true">√</span>대학수학생존</a>
    <div class="nav-links">
      {chr(10).join('      ' + l for l in links).lstrip()}
    </div>
  </div>
</nav>
"""


LANG_BAR = """
<div class="lang-toggle-bar">
  <label><input type="checkbox" id="toggle-ko" checked onchange="toggleLang()">한국어 표시</label>
  <span class="sep">|</span>
  <label><input type="checkbox" id="toggle-en" checked onchange="toggleLang()">English 표시</label>
  <span class="sep">|</span>
  <span style="color:var(--ink-faint); font-size:.7rem;">왼쪽: 한국어 · 오른쪽: English</span>
</div>
"""


def toggle(lang, body):
    if lang == "ko":
        return ('<button class="proof-toggle" type="button" onclick="toggleProof(this)" data-show="풀이 보기" data-hide="풀이 접기">'
                '<span class="arrow">&#9654;</span> 풀이 보기</button>\n'
                f'      <div class="proof-content">\n{body}\n      </div>')
    return ('<button class="proof-toggle" type="button" onclick="toggleProof(this)" data-show="Solution" data-hide="Hide Solution">'
            '<span class="arrow">&#9654;</span> Solution</button>\n'
            f'      <div class="en-proof-content">\n{body}\n      </div>')


def card(meta, label_short, p, sols):
    cid = f'{meta["prefix"]}-{p["n"]}'
    sec_links = "".join(
        f'<a class="ref-link" href="../s{s.replace(".", "-")}.html" title="Stewart §{s} 개념·예제">§{s}</a>'
        for s in p["secs"] if s in CONCEPT_PAGES)
    fig = f'\n      <figure class="fig">{p["fig"]}</figure>' if p["fig"] else ""
    ko_sol = sols.get((p["n"], "ko"))
    en_sol = sols.get((p["n"], "en"))
    ko_tail = toggle("ko", ko_sol) if ko_sol else '<p class="sol-pending">풀이 준비 중</p>'
    en_tail = toggle("en", en_sol) if en_sol else '<p class="sol-pending">Solution in preparation</p>'
    ko_label, en_label = ("한국어 · 원문", "English · 번역") if p["orig"] == "ko" else ("한국어 · 번역", "English · 원문")
    return f"""<article class="card ex-card exam-problem" id="{cid}">
  <div class="card-head">
    <span class="exam-num">{label_short} {p["n"]}번</span>
    <span class="ex-title">{p["title_ko"]}<em>{p["title_en"]}</em><span class="src-ref">{p["pts"]} pts</span>{scope_badge(meta["kind"], p["secs"])}</span>
    <span class="ref-links">{sec_links}</span>
  </div>
  <div class="card-body">
    <div class="ko-panel">
      <span class="panel-label ko-label">{ko_label}</span>
      <div class="formal">
{p["ko"]}
      </div>{fig}
      {ko_tail}
    </div>
    <div class="en-panel" lang="en">
      <span class="panel-label en-label">{en_label}</span>
      <div class="en-formal">
{p["en"]}
      </div>{fig}
      {en_tail}
    </div>
  </div>
</article>
"""


def exam_page(eid, title_ko, title_en, short, available):
    meta, probs, sols = parse_exam(eid)
    kind_ko = "중간고사" if meta["kind"] == "midterm" else "기말고사"
    total = sum(int(p["pts"]) for p in probs)
    secs = sorted({s for p in probs for s in p["secs"]}, key=sec_key)
    n_sol = sum(1 for p in probs if (p["n"], "ko") in sols and (p["n"], "en") in sols)
    page_title = f"{title_ko} 기출 해설"
    desc = (f"미적분학및연습II(MATH162) {title_ko} {len(probs)}문항 — 시험지 원문(영어)과 한국어 번역, "
            f"한국어·영어 단계별 풀이. 출제 범위 {sec_label(secs)}.")
    scope_txt = ("올해(2026-2) 중간고사 범위는 §12.6, §14.1–14.8, §15.1–15.8입니다(10/24)."
                 if meta["kind"] == "midterm" else
                 "올해(2026-2) 기말고사 범위는 §15.9, §16.1–16.10과 행렬입니다(12/19).")
    instr = f'<li>시험지 지시문: “{meta["instructions"]}”</li>' if meta.get("instructions") else ""
    toc = "\n".join(
        f'    <li><a href="#{meta["prefix"]}-{p["n"]}"><span class="toc-num">{p["n"]}번 · {p["pts"]}점</span>{p["title_ko"]} <em>{sec_label(p["secs"])}</em></a></li>'
        for p in probs)
    cards = "\n".join(card(meta, short, p, sols) for p in probs)
    out = HEAD.format(title=page_title, desc=html.escape(desc, quote=True), url=SITE + f"{eid}.html", mathjax=MATHJAX)
    out += "\n" + nav(eid, available)
    out += f"""
<header>
  <p class="subtitle">{html.escape(meta["header-en"])}</p>
  <h1>{title_ko} 기출 해설<span>{title_en} — Problems &amp; Solutions</span></h1>
  <p class="header-desc">시험지 원문(영어)을 그대로 옮기고 한국어 번역을 나란히 두었습니다. 풀이는 접혀 있으니 먼저 직접 풀어 본 뒤 펼쳐 확인하세요.</p>
  <div class="lang-badge"><span class="ko">한국어</span><span class="en">English</span></div>
</header>
{LANG_BAR}
<main id="main-content" role="main">
  <div class="exam-info">
    <ul>
      <li><strong>{len(probs)}문항 · {total}점</strong> · 출제 절 {sec_label(secs)}</li>
      {instr}
      <li>{scope_txt} 범위 밖 문항에는 표시를 달았습니다.</li>
      <li><a href="src/{eid}.pdf">문제지 PDF</a> · 풀이는 공식 해설이 아닌 자체 작성본입니다 (풀이 {n_sol}/{len(probs)}).</li>
    </ul>
  </div>

  <nav class="toc" aria-label="문항 목차">
    <h3>문항 · Problems</h3>
    <ol>
{toc}
    </ol>
  </nav>

{cards}
</main>
"""
    out += FOOTER
    (ROOT / f"{eid}.html").write_text(out, encoding="utf-8")
    return {"eid": eid, "n": len(probs), "total": total, "secs": secs, "n_sol": n_sol, "kind": meta["kind"]}


def index_page(stats, available):
    def tile(eid, title_ko, title_en, _short):
        s = stats.get(eid)
        if not s:
            return f"""    <article class="chapter-card exam-tile pending">
      <div class="card-top">
        <span class="ch-num">{title_en}</span>
        <h3>{title_ko}</h3>
        <p class="ch-desc">해설 준비 중</p>
      </div>
      <div class="card-actions"><a href="src/{eid}.pdf">문제지 PDF</a></div>
    </article>"""
        chips = " ".join(f'<span class="sec-chip">{sec_name(x)}</span>' for x in s["secs"])
        return f"""    <article class="chapter-card exam-tile">
      <div class="card-top">
        <span class="ch-num">{title_en}</span>
        <h3>{title_ko}</h3>
        <p class="ch-count">{s["n"]}문항 · {s["total"]}점 · 풀이 {s["n_sol"]}/{s["n"]}</p>
        <p class="sec-chips">{chips}</p>
      </div>
      <div class="card-actions">
        <a href="{eid}.html">문제·해설</a>
        <a href="src/{eid}.pdf">문제지 PDF</a>
      </div>
    </article>"""

    mids = "\n".join(tile(*e) for e in EXAMS if "midterm" in e[0])
    fins = "\n".join(tile(*e) for e in EXAMS if "final" in e[0])
    title = "미적분학2 기출문제와 해설"
    desc = "미적분학및연습II(MATH162) 2022·2024·2025년 2학기 중간·기말고사 기출문제 — 시험지 원문과 한국어 번역, 한국어·영어 단계별 풀이."
    out = HEAD.format(title=title, desc=desc, url=SITE + "index.html", mathjax="")
    out += "\n" + nav("index", available)
    out += f"""
<header>
  <p class="subtitle">Calculus II (MATH 162) · Past Exams</p>
  <h1>미적분학2 기출문제와 해설<span>Midterm &amp; Final Exams — Fall 2022, 2024, 2025</span></h1>
  <p class="header-desc">지난 2학기 미적분학및연습II 시험지를 중간·기말로 나누어 연도별로 정리했습니다. 문제마다 관련 Stewart 절로 가는 링크를 달았습니다.</p>
</header>

<main id="main-content">
  <div class="exam-info">
    <ul>
      <li><strong>올해 시험(2026-2 강의계획서)</strong> · 중간 10/24(토) — §12.6, §14.1–14.8, §15.1–15.8 · 기말 12/19(토) — §15.9, §16.1–16.10, 행렬. 정확한 범위는 LMS 공지를 따르세요.</li>
      <li>2022년은 블럭 1·2 시험지가 따로 있습니다. 2023년 2학기 시험지는 받은 자료에 없습니다.</li>
      <li>풀이는 공식 해설이 아닌 자체 작성본이며, 계산 결과는 별도로 검산했습니다.</li>
    </ul>
  </div>

  <div class="section-title" id="midterm"><h2>중간고사<span class="sec-en">Midterm Exams</span></h2></div>
  <div class="chapter-grid">
{mids}
  </div>

  <div class="section-title" id="final"><h2>기말고사<span class="sec-en">Final Exams</span></h2></div>
  <div class="chapter-grid">
{fins}
  </div>
</main>
"""
    out += FOOTER
    (ROOT / "index.html").write_text(out, encoding="utf-8")


def main():
    available = [e[0] for e in EXAMS if (ROOT / "data" / f"{e[0]}.html").exists()]
    stats = {}
    for eid, tko, ten, short in EXAMS:
        if eid in available:
            stats[eid] = exam_page(eid, tko, ten, short, available)
            s = stats[eid]
            print(f'{eid}: {s["n"]} problems, {s["total"]} pts, solutions {s["n_sol"]}/{s["n"]}')
    index_page(stats, available)
    print("index.html written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
