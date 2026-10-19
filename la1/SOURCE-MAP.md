# 선형대수학 1 SOURCE-MAP

소스: `la1/src/` (원본은 `~/Desktop/26-2/선형대수학1/`)
- `Syllabus 221 F26.pdf` — MATH221 Linear Algebra I, Fall 2026, Changho Han (Korea Univ., 비전공 분반). 교재 Friedberg–Insel–Spence 5e(연습문제용).
  성적: 출석 10 / 퀴즈 20 (5·13주차 목요일) / 중간 35 (8주차 화) / 기말 35 (16주차 화). **답안은 영어로만(다른 언어 0점).**
  진도: 1–4주 §1 Vector Spaces → 5–7주 §2(1) 선형변환 → 8주 중간 → 9–10주 §2(2) 행렬표현 → 11–13주 §3 기본행연산·연립방정식 → 14–15주 §4 행렬식.
- `Course Intro.pdf` (5쪽) = Lecture 1 pp.1–5 와 동일 내용.
- `Lecture N on 221 F26.pdf` (N=1..9, 12, 13) — **손글씨 태블릿 노트**(텍스트 추출 불가 → Read 도구로 시각 전사). 1–5는 9/17, 6–8은 10/1에 Desktop에 추가됨. 9는 10/7, 12는 10/15에 추가(반영 10/19). **13은 10/19 Desktop `26-2/선형대수학2/` 폴더에 잘못 올라와 있었음**(파일명의 221 = MATH221; 내용도 §2.1 연속) → `la1/src/`로 복사, 10/19 반영. **Lecture 10–11 파일은 없음** — L12 Last Time이 L9 복습이고 번호가 Ex 1.61 → Def 1.62로 이어지므로 빠진 내용 없음.
  분량: L1 6 · L2 8(p8 빈 쪽) · L3 8 · L4 6 · L5 7 · L6 8 · L7 6 · L8 6 · L9 6 · L12 7쪽(p7은 위쪽만) · L13 8쪽(p8은 위쪽만).
- `Midterm MAT221 F24.pdf`(8쪽, 4문항 42점, 2024-10-24 목) · `Midterm MATH221 F25.pdf`(10쪽, 5문항 54점, 2025-10-20 월) — LaTeX 시험지(텍스트 추출 가능, 행렬은 깨짐). `Midterm Solutions … F24/F25.pdf` — 같은 시험지 위 손글씨 공식 해설(F24 pp.2–5, F25 pp.2–6; 나머지는 빈 추가 답안지). 10/19 Desktop `선형대수학1/`에 추가 → `la1/midterm.html`.
- `Unit 1.x / 2.1 of Linear Algebra I (non-math major) Notes at KU*.pdf` — 강의자가 정리한 단원 노트(1.1 8쪽, 1.2 6쪽, 1.3 2쪽, 2.1 4쪽(p4 빈 쪽); 강의노트와 같은 손글씨).
  강의 슬라이드와 내용·번호 동일 → **전사 원본은 Lecture PDF**, Unit 노트는 판독 보조. Unit 1.3은 Def 1.30까지만 있음. Unit 2.1은 L12 pp.4–7과 같고 Ex 2.3(1)의 "Pf:" 뒤가 비어 있음(L12는 "Pf: Next Class!").

**번호 체계:** 강의노트가 전역 번호(Def 1.1 … Ex 1.61)를 쓴다 → 카드 배지 = 노트의 라벨·번호 그대로 (`DEF 1.9`, `THM 1.20`, `PROP 1.28`, `LEM 1.15`, `COR 1.16`, `REM 1.10`, `NOTE 1.5`, `NOTATION 1.7`, `EXAM 1.8`(Ex = Example), `EX 1.27`(Exercise)). 번호 없는 항목은 유형 배지만(DEF/REM/NOTE/Q/RECALL/CLAIM/EXAM/EX). 카드 id는 자체 순번 `c{단원}-{순번}`, 서술 단락은 note-card `note{단원2자리}-{순번}`(목차 제외).
**규칙 요약:** 각 강의 첫머리 "Last Time" 복습은 카드로 만들지 않음(새 내용이 있을 때만 RECALL 카드). 손그림은 `p.fig-note` 한 줄 설명. 증명 중간 끝 표시 ▨ = `span.part-end`. 노트에 증명이 없는 진술("Pf: Exercise", "See FIS", "Unit notes", "Math-Major Only", "Pf Idea")은 자체 증명(마커 → 증명 토글; 노트 증명이 이미 있으면 "보충 증명" 토글). en = verbatim(오타 포함), ko = 바른 뜻.
**퀴즈 복습·기출:** `la1/quiz1.html` — Lecture 1–9 개념 복습·연습 13세트와 Fall 2025 Quiz 1·2 기출 4문항(소문항별 5블록). 영어 답안·한국어 해설, 원본 PDF 링크. MathJax 4.1.3.
**중간고사 기출:** `la1/midterm.html` — Fall 2025·2024 중간고사 9문항(소문항별 11블록), quiz1과 같은 qs-block 형식. 영어 모범답안·한국어 해설·원본 해설 정정. 아래 "중간고사 기출 반영" 절 참조.
**진행 상태 (2026-10-19, 오후):** Lecture 13까지 반영 — ch05에 Ex 2.3(1) 원문 증명(L13 pp.1–2)과 Ex 2.3(2)–Thm 2.12(L13 pp.2–8) 추가: ch05 환경 19, note 5, 한·영 토글 각 17. Thm 2.12(계수-퇴화차수 정리) 증명은 노트에서 WTS 직전까지 → 보충 증명으로 완성. 중간고사 기출 페이지 신설.
**이전 상태 (2026-10-19, 오전):** Lecture 12까지 반영. pp.1–4 → ch04 끝 c4-28–31(Def 1.62–Ex 1.65, 라그랑주 보간; ch04 환경 31, 한·영 토글 각 23), pp.4–7 → 새 ch05(Unit 2 도입·§2.1 시작; 환경 4, 토글 각 3). 2026-10-15 1차 작업(pickerel 워크트리, 미커밋)이 워크트리와 함께 소실되어 10/19 원본에서 다시 작업함.
**이전 상태 (2026-10-07):** Lecture 9까지 반영. ch04에 Def 1.56–Ex 1.61, Ex 1.51 재방문 및 질문 추가(환경 27, 한·영 증명 토글 각각 17). 구조·수식·토글 검증 완료. 기존 10/1 기록: 4단원 빌드·번역·자체 증명(마커 0)·Opus 검증 4/4 완료. 인벤토리의 "markers? yes" 표기는 빌드 시점 기록 — 현재는 모두 증명 토글/보충 증명으로 채워짐. la1 전 페이지 MathJax 4.1.3.
**갱신 절차:** 새 Lecture PDF → `la1/src/` 복사 → 해당 단원 파일 끝(마지막 note 앞)에 카드 append(ch04는 `note04-99`의 강의 범위 안내를 갱신) → 번역 → 자체 증명 → 검증 → 이 인벤토리·la1/index 카드 수·홈 칩 갱신. 새 단원 파일은 원본에서 새 절이 시작되는지 확인한 뒤 생성한다. Lecture 9는 전부 §1.4의 후속 내용이다. Lecture 12는 p.4 중간에서 Unit 2로 넘어가므로 ch04(§1.4 응용)와 ch05(Unit 2 도입·§2.1)로 나눴다. 다음 강의는 ch05 끝(`note05-99` 앞)에 이어 붙인다. Ex 2.3(1)의 원문 증명은 L13에서 와서 전사로 교체했다(옛 자체 증명의 그림 설명은 보충 증명으로 유지). **Thm 2.12 증명의 WTS 원문이 다음 강의에서 오면** c5-19 Proof 토글의 "Pf of WTS in next class!" 뒤에 원문 전사를 이어 붙이고 qed를 달며, 보충 증명은 (i)·(iv)와 원문에서 빠진 단계만 남긴다.

## 전체 구조 (2026-10-19)
| 단원 | 제목 | 소스 |
|---|---|---|
| ch01 | 1.1 벡터공간으로서의 ℝⁿ | Lecture 1 (강의 소개 포함) · Lecture 2 · Lecture 3 p.2 |
| ch02 | 1.2 벡터공간과 부분공간 | Lecture 3 pp.2–8 · Lecture 4 · Lecture 5 pp.1–6 |
| ch03 | 1.3 일차결합, 생성, 일차독립 | Lecture 5 pp.6–7 · Lecture 6 · Lecture 7 pp.1–4 |
| ch04 | 1.4 기저와 차원 | Lecture 7 pp.4–6 · Lecture 8 · Lecture 9 · Lecture 12 pp.1–4 |
| ch05 | 2.1 선형사상: 핵, 상, 동형사상 | Lecture 12 pp.4–7 (Unit 2 도입 포함) · Lecture 13 |
| quiz1 | 퀴즈 복습과 기출 연습 | Lecture 1–9 · Fall 2025 Quiz 1·2 |
| midterm | 중간고사 기출 | Fall 2025·2024 Midterm + 공식 해설 |

## ERRATA (원문 오타·결함 — en verbatim 유지, ko는 바른 뜻 / 필요 시 증명에서 역주)
1. L2 p2 Def 1.2: "ℝ³ := {(a,b,c) : a,b,c ∈ ℝ³}" → ∈ ℝ.
2. L2 p4 Def 1.4(2): "∀(x_1,…,x_n) ∈ ℝ" → ∈ ℝⁿ. (Unit 1.1 노트 p8 열벡터판 Def 1.4도 "∈ ℝ" — 강의 L3 p2는 정상)
3. 번호 충돌: L2 "Rmk 1.7"과 L3 "Notation 1.7" — 둘 다 원문대로 배지 유지.
4. L5 p3 Ex 1.25 Hint: "deg(fg) = deg(f) deg(g)" → deg(f) + deg(g).
5. Unit 1.2 노트 p6: "a + c = b + c ⇒ a = c" → a = b (강의 L3 p8은 정상). Unit 1.2 노트 p5 Ex 1.14: +′ 대신 +.
6. L4 p4 Thm 1.20 Pf Idea: "(⇒) is just the def (& Prop 1.17(3))" — 0_V ∈ W에는 Prop 1.17(1)·소거법칙이 필요(확신 낮음).
7. L5 p5 Rmk 1.29(2): 𝒞 ⊆ 𝒫(V)가 부분공간들의 모임이라는 가정 누락.
8. L5 p1 Ex 1.24: "FIS calls it P(x)" — FIS 표기는 P(F).
9. Unit 1.3 노트 p1 Motivation: W = {(a, −a, b)} → {(a, a, b)} (강의 L5 p6은 정상).
10. L6 p6 Def 1.35 뒤 Note / Def 1.35(2): "S = {v_1,…,v_n} l.d. iff v_1,…,v_n l.d."는 v_i가 서로 다를 때만 성립.
11. L7 p2 Lem 1.41 증명: S∖{v} = ∅인 경우(v = 0) 누락. L7 p3 Prop 1.43 (⇐)는 Lem 1.41 앞에 Prop 1.42(⇒)가 암묵적으로 필요; (⇒)는 "Unit 1.3 Notes" 참조인데 보유 PDF에 없음 → 자체 증명.
12. L7 p4 Lem 1.44: "Henceforth" → Hence; 증명은 유한 S만 다룸 → 일반 경우 자체 증명.
13. L7 p4 Motivation: "nize" → nice. L8 p6 Exercise 1.54: "then" 중복. L8 p1 복습: "(b) β ⊆ S of V" → β ⊆ V.
14. L8 p6 Cor 1.55 증명: Replacement Thm 적용 전 #β̃ < ∞(Exercise 1.54)가 필요 — 보충 증명으로 처리.
15. L2 p4 Rmk 1.7 이후 "Pf Idea of Prop 1.6"은 증명 아이디어만("this needs full-justification") → 보충 증명.
16. L2 p6 Pf Idea of Prop 1.6 (Unit 1.1 노트 p7도 동일): "satisties" → satisfies (철자; en verbatim).
17. L4 p2 Prop 1.17(2) 괄호: "(so a = −1 ⇒(VS5) −v = (−1)·v)" — 바로 대입되는 것은 a = 1(즉 −a = −1). ko는 "−a = −1, 즉 a = 1"로 (확신 중간).
18. L4 p2 Prop 1.17(3) 증명: 공통항 a·0_V가 왼쪽에 있는데 소거법칙(Lem 1.15)은 오른쪽 공통항을 지움 → (VS 1) 선행 필요. ch02 보충 증명에서 보완.
19. L12 p3 Cor 1.64 유일성 증명: "basis by Prop 1.62" → Prop 1.63 (1.62는 정의). ch04 보충 증명에 명시.
20. L12 p2 Prop 1.63 진술: t_0,…,t_n이 "distinct"라는 가정 생략(Def 1.62에서 상속). 증명의 Cor 1.59(2) 적용에는 f_i들이 서로 다르다는 점(★에서 따라 나옴)도 필요 → ch04 보충 증명.
21. L13 p5 Ex 2.7: "Recall from Ex 2.3(3)" → Ex 2.3(2) (ax+by+cz 사상은 2.3(2), 2.3(3)은 미분). ko는 2.3(2)로, c5-13 보충 증명에 명시.
22. L13 p7 Observation: "w/ V f.d., is how are …"의 군더더기 "is", 괄호 "(Ex 2.10: guess is …"가 닫히지 않음 — en verbatim, ko는 바른 문장.
23. L13 p7 Thm 2.12: 진술에 V 유한차원 가정이 없는데 증명은 "when V f.d."만 다룸(p8). 무한차원이면 ker(T)·im(T) 중 하나가 무한차원 → c5-19 보충 증명 (iv).
24. L13 p2 Ex 2.3(3): D : ℝ[x]≤n → ℝ[x]≤n−1은 n = 0이면 공역이 ℝ[x]≤−1 = {0}(deg 0 = −∞ 약속) — 오류는 아니고 c5-6 보충 증명에 명시.

## 챕터별 인벤토리 (빌드 시점 기록)

### Inventory — la1/ch01.html (Unit 01 · §1.1 ℝⁿ as a Vector Space)

Sources: Lecture 1 pp.1–6, Lecture 2 pp.1–7 (p.1 Last Time/Today skipped), Lecture 3 p.2 (Today agenda skipped; stops before §1.2 heading).
Cross-checked against "Unit 1.1 … Notes at KU-2.pdf" (8 pp., same handwriting, identical content).

Section titles: "Course Introduction · 강의 소개" (before note01-1), "§1.1 ℝⁿ as a Vector Space · 1.1 벡터공간으로서의 ℝⁿ" (before note01-8).

| id | 배지 | Lecture·page | content (one line) | markers? |
|---|---|---|---|---|
| note01-1 | NOTE | L1 p.1 | Welcome to MATH221; instructor/email/office hour; grade distribution 10/20/35/35; classroom expectations | – |
| note01-2 | NOTE | L1 p.2 | "So what is Linear Algebra?" — study of vector spaces & higher-dim analog of linear fcns/equations; fig y=ax; a vector = point of a v.s. (Science/AI-CS/Stats examples) | – |
| note01-3 | NOTE | L1 p.2–3 | "Why Linear Algebra?" — building block of modern math; linear ~ complicated fcns (tangent-line fig) | – |
| note01-4 | NOTE | L1 p.3–4 | Traditional Applications: Lagrange interpolation, image manipulation (90° rotation fig), solving linear systems, (signed) volume via determinants | – |
| note01-5 | NOTE | L1 p.4 | "This hybrid theory/computation course is about": fundamentals, proof-based, course structure (8+8 weeks) | – |
| note01-6 | NOTE | L1 p.5 | Unit Notes: textbook only for practice problems; Unit Notes in LMS | – |
| note01-7 | NOTE | L1 p.5 | Unit 1: Vector Spaces — Goal | – |
| note01-8 | NOTE | L1 p.5 | Before jumping into ℝⁿ start with ℝ²; ℝ = set of all real numbers (number-line fig) | – |
| c1-1 | DEF 1.1 | L1 p.5 | ℝ² := {(a,b) : a,b ∈ ℝ}, with side remarks (pair; := meaning) | – |
| c1-2 | NOTE | L1 p.5 | ℝ² is a set of pairs (2-tuples) of real numbers | – |
| note01-9 | NOTE | L1 p.6 | Cartesian plane is a way to visualize ℝ² (fig) | – |
| c1-3 | DEF | L2 p.1–2 | Two operations on ℝ²: (1) coordinate-wise addition, e.g. (2,1)+(1,−2)=(3,−1); (2) scalar multiplication, e.g. 2·(1,1)=(2,2) (figs) | – |
| c1-4 | NOTE | L2 p.2 | Subtraction on ℝ²: (a,b)−(c,d) := (a,b)+(−1)·(c,d) = (a−c,b−d) | – |
| c1-5 | REM | L2 p.2 | Physics: displacement on a plane modelled as a point of ℝ² (fig) | – |
| note01-10 | NOTE | L2 p.2 | "Similarly, ℝ³ has many properties similar to ℝ²:" | – |
| c1-6 | DEF 1.2 | L2 p.2 | ℝ³ := {(a,b,c) : a,b,c ∈ ℝ³} (erratum kept), 3-tuples (fig) | – |
| c1-7 | DEF | L2 p.2–3 | + and · on ℝ³ coordinate-wise, plus subtraction | – |
| c1-8 | REM | L2 p.3 | Mathematician's Guiding Principle: "vector" = things that can be added & scalar multiplied; ℝ², ℝ³ are v.s. (defined in §1.2) | – |
| note01-11 | NOTE | L2 p.3 | ℝ² = 2-dim plane, ℝ³ = 3-dim space; need to generalize to ℝⁿ | – |
| c1-9 | DEF 1.3 | L2 p.4 | ℝⁿ := {(x_1,…,x_n) : x_i ∈ ℝ ∀i}, n ∈ ℤ_{>0}; k-th coordinate | – |
| c1-10 | REM | L2 p.4 | Some books def ℝ⁰ := {0} | – |
| c1-11 | DEF 1.4 | L2 p.4 | Addition and scalar multiplication on ℝⁿ (erratum "∈ ℝ" in (2) kept) | – |
| note01-12 | NOTE | L2 p.4 | Need to re-interpret + & · via sets and functions (maps) | – |
| c1-12 | DEF | L2 p.5 | Cartesian product X × Y := {(x,y) : x ∈ X, y ∈ Y}; side box on f : X → Y, x ↦ f(x) | – |
| c1-13 | EXAM | L2 p.5 | ℝ² = ℝ×ℝ; ℝ³ ↔ ℝ²×ℝ (1-1 onto / 1-1 cor), (a,b,c) ↦ ((a,b),c) | – |
| c1-14 | NOTE 1.5 | L2 p.5 | Def 1.4 & Prev Def ⇒ + : ℝⁿ×ℝⁿ→ℝⁿ and · : ℝ×ℝⁿ→ℝⁿ are functions | – |
| c1-15 | PROP 1.6 | L2 p.5–6 (Pf Idea p.6–7) | ℝⁿ with + and · satisfies (VS 1)–(VS 8); toggle holds "Pf Idea of Prop 1.6 … (this needs full-justification) □" | **YES** (toggle + PROOF-KO/EN) |
| c1-16 | REM 1.7 | L2 p.6 | (a) axioms = proper behaviour; (b) 0_{ℝⁿ} unique, zero vector (abuse of notation 0); (c) w = (−1)v =: −v, unique | – |
| c1-17 | NOTATION 1.7 | L3 p.2 | ℝⁿ as column vectors; [x_1;…;x_n] := (x_1,…,x_n); Def 1.4 in column form | – |

Totals: 17 TOC cards — def-card 8 (DEF 1.1, 1.2, 1.3, 1.4 + 3 unnumbered DEF + NOTATION 1.7), rem-card 7 (REM ×3 unnumbered, REM 1.7, NOTE ×2 unnumbered, NOTE 1.5), thm-card 1 (PROP 1.6), exam-card 1 (EXAM); plus 12 note-cards; 1 marker pair (PROOF-KO/EN) + 1 proof toggle.

Placement notes:
- The "Pf Idea of Prop 1.6" appears in the notes AFTER Rmk 1.7 (L2 p.6 bottom → p.7 "this needs full-justification □"). It was moved into the Prop 1.6 card's proof toggle (an HTML comment above c1-15 records this). Rmk 1.7 stays after Prop 1.6.
- c1-3 and c1-7 (operations on ℝ² / ℝ³) are unlabeled in the notes ("There are two operations on ℝ²:", "ℝ³ has both + & ·:") but are definitions with := — built as def-card with plain `DEF` badge so they appear in the TOC. Change to note-cards if strict label-only badging is preferred.
- The "For example," computations inside c1-3 are inline in the notes (no "Example:" label), so they stay in the DEF card rather than separate EXAM cards.
- The Cartesian-plane sentence (L1 p.6) and the lead-in sentences ("Similarly, ℝ³ …", "ℝ² represents …", "To extract properties …") are unlabeled prose → note-cards.
- "⇓" between Note 1.5 and Prop 1.6 is kept as the first line of the Prop 1.6 card.
- Glosses dropped: "Definition", "Proposition", "Remark" above labels; LHS/RHS; ∀ above "for every"; ℝ #s above "real numbers"; coord; mult; fcns; w/; ∃ above "There exists"; s.t. above "such that"; (ab)v / a(bv) above (VS 6); b/c above "Because"; §1.2 above "Section 1.2"; col/vec above "column vector".
- Side remarks kept in parentheses: "a pair", "means a & b are elements of ℝ", ":= Left-hand side is defined by Right-hand side", "2-tuples", "3-tuple of real numbers", "set of positive integers", "n-tuple of real numbers", "k ∈ {1,…,n}", "vector addition", "scalar-multi; ℝ: set of scalars", "abuse of notation", "1-1 onto"/"1-1 cor" arrow labels, f : X → Y side box, "(mathematician's viewpoint)", "n rows, single column, each x_i ∈ ℝ ∀i; column vector of size n (over ℝ)", "n-tuple of ℝ #s", "(Def 1.4)" brace label, "(this needs full-justification)".
- Verifier flag KO-IN-EN = 1 is expected: note01-1 keeps the instructor's name as printed, "Changho Han (한창호)".

#### Errata candidates

1. **Lecture 2 p.2 Def 1.2** (also Unit 1.1 Notes p.3): "ℝ³ := {(a,b,c) : a,b,c ∈ ℝ³}" → should be "a,b,c ∈ ℝ". Kept verbatim in c1-6.
2. **Lecture 2 p.4 Def 1.4(2)** (also Unit 1.1 Notes p.5): "∀(x_1,…,x_n) ∈ ℝ & ∀c ∈ ℝ" → should be "∀(x_1,…,x_n) ∈ ℝⁿ". Kept verbatim in c1-11.
3. **Unit 1.1 Notes p.8** (not built from; lecture is correct): column-vector restatement of Def 1.4 writes "∀[a_i], [b_i] ∈ ℝ" and "∀[a_i] ∈ ℝ & ∀c ∈ ℝ" → should be ∈ ℝⁿ. Lecture 3 p.2 writes ∈ ℝⁿ correctly; c1-17 follows the lecture.
4. **Numbering clash**: Lecture 2 p.6 "Rmk 1.7" and Lecture 3 p.2 "Notation 1.7" share the number 1.7 (Unit 1.1 Notes p.6–7 has the same clash). Both badges kept as printed: REM 1.7 (c1-16), NOTATION 1.7 (c1-17).
5. Minor (not an error, just inconsistent spacing): the notes write "(VS 1)–(VS 3)" with a space and "(VS4)–(VS8)" without; normalized to "(VS n)" throughout.
6. Minor wording kept verbatim: Rmk 1.7(c) "We often write −v as (−1)v" (i.e. −v := (−1)v, as the L3 p.1 recap writes); "So that w is unique." Def 1.4 heading "Addition and scalar-multiplication on ℝⁿ is:" (singular "is").

#### Marker cards (proofs to write later)

| id | 배지 | what remains to be proved |
|---|---|---|
| c1-15 | PROP 1.6 | Full proof that ℝⁿ with coordinate-wise + and · satisfies (VS 1)–(VS 8): the notes give only the idea "ℝ = ℝ¹ satisfies (VS 1)–(VS 8) and the operations are coordinate-wise, so the n = 1 case 'implies' the n > 1 case — this needs full-justification". Write the coordinate-by-coordinate verification of each axiom (VS 3 with 0_{ℝⁿ} = (0,…,0), VS 4 with w = (−x_1,…,−x_n)). |

Possible additional marker candidates (NOT marked, flagged for the supervisor): Rmk 1.7(b) asserts uniqueness of 0_{ℝⁿ} without proof; Rmk 1.7(c) asserts the w of (VS 4) is (−1)v and unique, with only a one-line reason.

### Inventory — la1/ch02.html (Unit 02 · §1.2 Vector Spaces and Subspaces)

Sources: Lecture 3 pp.2(bottom)–8, Lecture 4 pp.1–6 (recap skipped), Lecture 5 pp.1–6 top (recap skipped; stops before §1.3).
Cross-check: Unit 1.2 Notes (6 pp., typed-up Lecture 3 pp.3–8).

| id | 배지 | Lecture·page | content (one line) | markers? |
|---|---|---|---|---|
| note02-1 | NOTE | L3 p.3 | Motivation: properties of + and · on ℝⁿ (Prop 1.6); want to define vector / vector space | – |
| c2-1 | Q | L3 p.3 | Q: What else behaves like ℝⁿ? A: functions ℝ→ℝ can be added & scalar-mult | – |
| c2-2 | EXAM 1.8 | L3 p.3 | 𝓕(X,ℝ) := set of all fcns X→ℝ, with pointwise + and · (h(x)=\|x\| example) | – |
| c2-3 | CLAIM | L3 p.3–4 | 𝓕(X,ℝ) satisfies (VS1)–(VS8); zero fcn (if X≠∅) and (−1)·v; toggle: Pf Idea + Actual Pf of (VS1) ▨ | yes |
| note02-2 | NOTE | L3 p.4 | Conclusion: (VS1)–(VS8) are the rules for + & · to "behave like" ℝⁿ | – |
| c2-4 | DEF 1.9 | L3 p.4–5 | Vector space (over ℝ): set with + and · satisfying (VS 1)–(VS 8); elements = vectors | – |
| c2-5 | REM 1.10 | L3 p.5–6 | (a) bijection ℝⁿ ⇄ 𝓕({1,…,n},ℝ) "Pf: Exercise □"; (b) ℝⁿ v.s. of col vecs; (c) 𝓕(X,ℝ) generalizes ℝⁿ | yes |
| c2-6 | NOTE | L3 p.6 | NO NEED TO MEMORIZE statement #s; CONTENT is important | – |
| c2-7 | EXAM 1.11 | L3 p.6 | ℝ^∞ := 𝓕(ℤ_{>0},ℝ); sequences "are" vectors | – |
| c2-8 | EXAM 1.12 | L3 p.6–7 | m×n matrices, (i,j)-entry, B∈M_{2×3}(ℝ) with B_{2,2}=3; M_{m×n}(ℝ) is a v.s. "Pf: Exercise (Similar to Pf of Ex 1.8.) □" | yes |
| c2-9 | REM 1.13 | L3 p.7 | (a) ℝⁿ = M_{n×1}(ℝ); (b) row vecs M_{1×n}(ℝ), [1 3 5] ≠ column (1,3,5); (c) M_n(ℝ) | – |
| c2-10 | EXAM 1.14 | L3 p.7 | ℝ² with +′ (a,b),(c,d) ↦ (a+c,0): (VS3) fails for v=(1,1) | – |
| (section) | Properties of V.S. | L3 p.7 | section-title | – |
| note02-3 | NOTE | L3 p.7–8 | Motivation: zero & inverses unique, a+c=b+c ⇒ a=b in ℝⁿ and 𝓕(X,ℝ) | – |
| c2-11 | Q | L3 p.8 | Q: True for general v.s.? ⇓ Yes! | – |
| c2-12 | LEM 1.15 | L3 p.8 | Cancellation Law: x+z=y+z ⇒ x=y; proof (VS2, VS4, VS3) in toggle | – |
| c2-13 | COR 1.16 | L4 p.1–2 | (1) unique zero vec; (2) unique additive inverse −v; toggle: (1) "See Unit 1.2 Notes ▨", (2) proved | yes |
| c2-14 | PROP 1.17 | L4 p.2 | (1) 0·v=0_V, (2) (−a)v=−(av)=a(−v), (3) a·0_V=0_V; toggle: (1)&(2) "See Pf of Thm 1.2 in FIS textbook ▨", (3) proved | yes |
| c2-15 | REM | L4 p.2 | (1) intuitions from ℝⁿ hold in any v.s.; (2) 0 ∈ V means 0_V | – |
| (section) | Subspaces | L4 p.2 | section-title | – |
| note02-4 | NOTE | L4 p.2–3 | Motivation: subsets of v.s. that are v.s.? + 2 figure notes (lines in ℝ², plane in ℝ³) | – |
| c2-16 | DEF 1.18 | L4 p.3 | Subspace: W ⊆ V with induced (restricted) +_W, ·_W is a v.s. | – |
| c2-17 | EXAM 1.19 | L4 p.3–4 | (1) V and {0} (trivial subsp); (2) xy-plane in ℝ³ via bijection with ℝ² | – |
| note02-5 | NOTE | L4 p.4 | "Before giving more Exs of subsps, need simpler way …" | – |
| c2-18 | THM 1.20 | L4 p.4 | Subsp Criterion (1) 0_V∈W (2) closed under + (3) closed under ·; "Pf: FIS Thm 1.3."; toggle: Idea … □ | yes |
| note02-6 | NOTE | L4 p.5 | "Actually more important to learn how to use statements than the Pfs!" | – |
| c2-19 | REM 1.21 | L4 p.5 | (1) 0_W = 0_V; (2) additive inverse in W is −x=(−1)x, same as in V | – |
| c2-20 | EXAM 1.22 | L4 p.5–6 | W = {Σa_i = 0} ⊆ ℝⁿ is a subsp; proof (1)▨ (2)▨ (3)□ in toggle | – |
| c2-21 | EXAM 1.23 | L4 p.6 | union of axes in ℝ² is not a subsp ((1,0)+(0,1)=(1,1)∉W); figure note | – |
| c2-22 | EXAM 1.24 | L5 p.1–2 | ℝ[x] ⊆ 𝓕(ℝ,ℝ) (FIS calls it P(x)) is a subsp; proof (1)▨ (2)▨ (3)□ in toggle | – |
| c2-23 | EXAM 1.25 | L5 p.2–3 | degree, deg(0):=−∞, ℝ[x]_{≤n} ⊊ ℝ[x] is a subsp; "Pf: Exercise by using Subsp Crit." + Hint | yes |
| c2-24 | EXAM 1.26 | L5 p.3 | C(ℝ,ℝ) (MATH 161) subsp of 𝓕(ℝ,ℝ) by Subsp Crit; ℝ[x] ⊊ C(ℝ,ℝ) ∋ eˣ, sin(x) | – |
| c2-25 | EX 1.27 | L5 p.3–4 | prove subsps: (a) even fcns (b) {f∈ℝ[x]_{≤n}: f(a)=0} (c) symmetric matrices (sym/not-sym examples) | yes |
| c2-26 | RECALL | L5 p.4 | Ex 1.23: W_1 ∪ W_2 need not be a subsp | – |
| c2-27 | Q | L5 p.4 | Q: W_1 ∩ W_2 subsp? + figure (xz-plane ∩ xy-plane = x-axis) | – |
| c2-28 | PROP 1.28 | L5 p.4 (Pf p.5–6) | W_1 ∩ W_2 is a subsp; "Pf of Prop 1.28" (written after Rmk 1.29) attached to toggle, HTML comment notes original order | – |
| c2-29 | REM 1.29 | L5 p.4–5 | (1) finite intersections "(Pf: Exercise via Induction or (2))"; (2) ⋂_{W∈𝒞} W "(Pf: FIS Thm 1.4)" | yes |

Totals: 29 TOC cards (def 2 · thm 6 · rem 10 · exam 10 · ex 1) + 6 note-cards; 8 proof toggles (7 with qed; the Claim's toggle ends with ▨ as in the source); 9 PROOF-KO/PROOF-EN marker pairs.

#### Errata candidates

1. **L5 p.3, Ex 1.25 Hint (c2-23)** — "deg(fg) = deg(f) deg(g) if f,g ≠ 0" → correct rule is **deg(fg) = deg(f) + deg(g)**. Kept verbatim.
2. **Unit 1.2 Notes p.6 (cross-check only)** — "a + c = b + c ⇒ a = c" → **a = b**. Lecture 3 p.8 has the correct "⇒ a = b"; the page follows Lecture 3, so this typo does not appear in ch02.
3. **Unit 1.2 Notes p.5 (cross-check only)** — Ex 1.14 writes "(1,1) + (c,d)" without the prime; Lecture 3 p.7 has "(1,1) +′ (c,d)". Page follows the lecture.
4. **L4 p.4, Thm 1.20 Pf Idea (c2-18)** — "(⇒) direction is just the def (& Prop 1.17(3))". Getting 0_V ∈ W needs 0_W = 0_V, which follows from Prop 1.17**(1)** (0·w = 0_V, computed in W and in V) or from the Cancellation Law (0_W + 0_W = 0_W = 0_W + 0_V). Prop 1.17(3) (a·0_V = 0_V) alone does not give it, so "(1)" may have been meant. Low confidence.
5. **L5 p.5, Rmk 1.29(2) (c2-29)** — "If 𝒞 ⊆ 𝒫(V), then ⋂_{W∈𝒞} W … is a subsp of V" is missing a hypothesis: 𝒞 must be a collection of **subsps** of V. For example, 𝒞 = {W} with W not a subsp is a counterexample. (With the stated definition, 𝒞 = ∅ gives V, which is fine.)
6. **L5 p.1, Ex 1.24 side note (c2-22)** — "FIS calls it P(x)". FIS writes P(F), here P(ℝ). Minor.
7. **L5 p.3, Exercise 1.27 (c2-25)** — "each of the following subset" → "subsets". Grammar only.
8. **L4 p.2, Prop 1.17(3) proof (c2-14)** — this is a small rigor gap, not a typo. Lem 1.15 cancels a common term on the right (x+z = y+z ⇒ x = y), but here the common term a·0_V is on the left: a·0_V + 0_V = a·0_V + a·0_V. VS1 is needed first. The proof of Cor 1.16(2) does cite VS1 for exactly this step.
9. **L3 p.4, Claim (c2-3)** — the side remark "if X ≠ ∅" is not needed. For X = ∅, 𝓕(∅,ℝ) = {empty fcn} and x ↦ 0 is that fcn. Harmless.

#### Marker cards (proofs to write later)

| id | 배지 | what remains to be proved |
|---|---|---|
| c2-3 | CLAIM | (VS2)–(VS8) for 𝓕(X,ℝ) ("rest are Exercises"), and that the zero vector is x ↦ 0 and the additive inverse of v is (−1)·v: x ↦ (−1)v(x). Uniqueness can cite Cor 1.16. |
| c2-5 | REM 1.10 | (a) the maps ℝⁿ → 𝓕({1,…,n},ℝ), (a_1,…,a_n) ↦ (i ↦ a_i) and f ↦ (f(1),…,f(n)) are mutually inverse bijections ("Pf: Exercise"). |
| c2-8 | EXAM 1.12 | M_{m×n}(ℝ) with entrywise + and · satisfies (VS1)–(VS8) ("Similar to Pf of Ex 1.8"). |
| c2-13 | COR 1.16 | (1) uniqueness of the zero vector ("See Unit 1.2 Notes"). The Unit 1.2 Notes PDF in src/ stops at "Q: True for general v.s.? ⇓ Yes!" and does **not** contain this proof. (2) is proved in the toggle. |
| c2-14 | PROP 1.17 | (1) 0·v = 0_V and (2) (−a)·v = −(av) = a(−v) ("See Pf of Thm 1.2 in FIS textbook"). (3) is proved in the toggle. |
| c2-18 | THM 1.20 | Full proof of the Subspace Criterion ("Pf: FIS Thm 1.3"). Only the Idea is written, in the toggle. |
| c2-23 | EXAM 1.25 | ℝ[x]_{≤n} is a subsp of ℝ[x] via Subsp Crit ("Pf: Exercise by using Subsp Crit"; use the correct deg(fg) = deg f + deg g if the degree route is used). |
| c2-25 | EX 1.27 | (a) even fcns, (b) {f ∈ ℝ[x]_{≤n} : f(a) = 0}, and (c) symmetric matrices in M_n(ℝ) are each a subsp. |
| c2-29 | REM 1.29 | (1) finite intersection W_1 ∩ ⋯ ∩ W_m is a subsp ("Exercise via Induction or (2)"); (2) arbitrary intersection ⋂_{W∈𝒞} W of subsps is a subsp ("FIS Thm 1.4"). |

#### Reading / judgment notes

- **Rmk 1.13(b):** the red vertical "≠" marks are transcribed as "([1 3 5] ≠ column (1,3,5) = (1,3,5) ∈ ℝ³ = M_{3×1}(ℝ); M_{1×3}(ℝ) ≠ M_{3×1}(ℝ))".
- **Claim:** the red "unique" (arrows to both "=") is transcribed as "(both unique)". "if X ≠ ∅" is placed after the zero-fcn line.
- **Ex 1.26 side note:** a diagonal ⊋ pointing to ℝ[x] plus "∋ eˣ, sin(x)" is transcribed as "(ℝ[x] ⊊ C(ℝ,ℝ) ∋ eˣ, sin(x))".
- **Prop 1.17(2):** the gray "VS5" is placed over the ⇒ in "(so a = −1 ⇒ −v = (−1)·v)".
- **Glosses kept because they carry content:** "(1-1 & onto fcn)" (Rmk 1.10(a), Ex 1.19(2)), "($0_V$)" after "zero vec" (Cor 1.16(1)), "(Calc I)" after "(MATH 161)", "FIS" in "FIS textbook".
- **Glosses dropped:** elts, vecs, col, s.t., ∃, ∀, w/, WTS, Crit, iff, inv, cts, sym, polys, coeffs, deg, b/c, "(ab)v a(bv)" over VS6, "for example", "implies", "End of (Part of) Pf", and the Example/Remark/Lemma/Definition/Proof labels.
- **Lecture 4 p.1 recap** has a small addition: "(has commas)" for (a_1,…,a_n) vs "(no commas)" for the row vec [a_1 ⋯ a_n]. It mostly repeats Rmk 1.13(b), so no RECALL card was made. HTML comments mark both skipped recaps.
- **Cor 1.16 / Prop 1.17:** the reference line for the unproved part ("(1): See Unit 1.2 Notes ▨", "(1) & (2): See Pf of Thm 1.2 in FIS textbook ▨") is kept inside the toggle together with the written part, in source order. The markers sit after the formal divs.

### la1/ch03.html inventory: §1.3 Linear Combinations, Span, and Linear Independence

Sources: Lecture 5 pp.6–7 (from the §1.3 heading), Lecture 6 pp.1–8, Lecture 7 pp.1–4 (up to just before the §1.4 heading).
Cross-check: Unit 1.3 Notes (2 pp.). It covers only Motivation through Def 1.30.

Totals: 27 TOC cards (def 5, thm 7, rem 7, exam 6, ex 2), 5 note-cards, 7 marker pairs, 7 proof toggles.
Section titles: "§1.3 Linear Combinations, Span, and Linear Independence · 1.3 일차결합, 생성, 일차독립" (top) and "Linear (In)dependence · 일차종속과 일차독립" (Lecture 6 p.4).

| id | 배지 | Lecture·page | content (one line) | markers? |
|---|---|---|---|---|
| note03-1 | NOTE | L5 p.6 | Motivation: how to build a subsp W containing w_1..w_m. ℝ³ figure, w_1=(1,1,0), w_2=(0,0,1). Guess W=ℝ³ or W={(a,a,b)} | – |
| c3-1 | EX | L5 p.6 | Exercise (side box): Check W={(a,a,b)} is a subsp | **yes** |
| c3-2 | DEF 1.30 | L5 p.6–7 | (1) l.c. of w_1..w_k; (2) l.c. of nonempty S via a finite nonempty T⊆S; (3) l.c. of ∅ iff v=0 | – |
| c3-3 | DEF 1.31 | L5 p.7 | (1) span(w_1..w_k) = {Σa_iw_i}; (2) span(S) = {l.c.s of S} | – |
| c3-4 | RECALL | L6 p.1 | margin remark: w_1..w_k can be treated as a list (w_1..w_k) ∈ V^k | – |
| c3-5 | EXAM 1.32 | L6 p.2 | (a) span((1,1),(1,−1)) = ℝ², with figure; Pf by elimination (toggle) | – |
| c3-6 | EXAM 1.32 (cont.) | L6 p.2–3 | (b) span(e_1,e_2) = xy-plane ⊊ ℝ³; (c) 2+3x+x² = 0·1+(1+x)+(1+x)², YES (Sol kept in body) | – |
| c3-7 | Q | L6 p.3 | spans in 1.32(a)(b) are subsps; is span(S) always a subsp? ⇓ Yes | – |
| c3-8 | PROP 1.33 | L6 p.3–4 | span(S) is the smallest subsp containing S. "Pf: See FIS Thm 1.5 (uses Subsp Crit)." | **yes** |
| c3-9 | REM | L6 p.4 | (1) span(v_1..v_n) = span({v_i}) (remove repetitions); (2) span(S) = ⋂ of subsps W ⊇ S | – |
| c3-10 | DEF 1.34 | L6 p.4 | spanning set; S spans (generates) W | – |
| note03-2 | NOTE | L6 p.4–5 | Motivation: e_1, e_2, (1,1) in ℝ² (figure). Adding (1,1) does not grow the span ("redundant") | – |
| c3-11 | Q | L6 p.5 | How to tell when S ⊆ V is "redundant"? | – |
| note03-3 | NOTE | L6 p.5 | experiment: two representations of (1,1) give 0 = 1e_1+1e_2−1(1,1); impossible for e_1, e_2; ⇓ benchmark | – |
| c3-12 | DEF 1.35 | L6 p.6 | (1) list l.d. iff ∃ nonzero (a_i) with Σa_iv_i = 0 (side remarks kept); (2) subset l.d. via a finite nonempty T | – |
| c3-13 | NOTE | L6 p.6 | S={v_1..v_n} l.d. iff v_1..v_n l.d. (see errata 2) | – |
| c3-14 | EXAM 1.36 | L6 p.6–7 | (1) repeated vector ⇒ l.d.; (2) some v_i=0 ⇒ l.d.; (3) (1,1),(2,2) l.d. (figure) | – |
| c3-15 | EX | L6 p.7 | ⇓ generalization. Exercise: v_2 = cv_1 ⇒ v_1, v_2 l.d. | **yes** |
| c3-16 | EXAM 1.36 (cont.) | L6 p.7 | (4) e_1, e_2, (1,1) l.d. but e_1, e_2 not l.d. | – |
| c3-17 | DEF 1.37 | L6 p.7 | (1) list l.i. = not l.d.; (2) S l.i. = not l.d.; ∅ is l.i. | – |
| c3-18 | EXAM 1.38 | L6 p.7–8 | (1) e_i via Kronecker delta δ_ij, with examples; Claim: e_1..e_n l.i. Pf in toggle | – |
| c3-19 | EXAM 1.38 (cont.) | L6 p.8 | (2) 1, x, ..., xⁿ l.i. in ℝ[x]_{≤n} "Pf: Exercise."; (3) MATH161: sin x, cos x l.i. in 𝓕(ℝ,ℝ) | **yes** |
| c3-20 | RECALL | L7 p.1 | (1′) l.i. ⇔ (Σa_iv_i=0 ⇒ a_i=0 ∀i); (2′) S l.i. (∅ l.i.) means every fin subset l.i. | – |
| c3-21 | PROP 1.39 | L7 p.1 | S_1 ⊆ S_2, S_1 l.d. ⇒ S_2 l.d. Pf in toggle | – |
| c3-22 | COR 1.40 | L7 p.2 | ⇓ Contrapositive: S_1 ⊆ S_2, S_2 l.i. ⇒ S_1 l.i. (no Pf written) | **yes** |
| note03-4 | NOTE | L7 p.2 | compare "redundancy" with l.d.: span(e_1,e_2) [l.i.] = span(e_1,e_2,(1,1)) [l.d.] | – |
| c3-23 | LEM 1.41 | L7 p.2 | v ∈ S, v ∈ span(S∖{v}) ⇒ S l.d. Pf in toggle | – |
| c3-24 | PROP 1.42 | L7 p.2–3 | span(S∖{v}) = span(S) ⇔ v ∈ span(S∖{v}). Pf (⇒) ▨ (⇐) □ in toggle | – |
| c3-25 | PROP 1.43 | L7 p.3 | S l.d. iff ∃v∈S with span(S∖{v}) = span(S). Pf: (⇐) Lem 1.41 ▨; (⇒) "Unit 1.3 Notes" | **yes** |
| c3-26 | REM | L7 p.3 | such v is a "redundant" vec; removing it does not change the span | – |
| note03-5 | NOTE | L7 p.3 | "L.i. analog of Lem 1.41:" | – |
| c3-27 | LEM 1.44 | L7 p.3–4 | S l.i., v ∉ span(S) ⇒ S∪{v} l.i. "Pf when S = {w_1..w_n} fin" (by contradiction) in toggle | **yes** |

#### Errata candidates (kept verbatim on the page, not fixed)

1. **Unit 1.3 Notes p.1, Motivation** (cross-check source only): writes W = {(a, −a, b) : a, b ∈ ℝ}. This is wrong, and the lecture
   (Lecture 5 p.6) has the correct W = {(a, a, b) : a, b ∈ ℝ} = a(1,1,0) + b(0,0,1). The page follows the lecture, so the page itself is correct.
2. **Note after Def 1.35 (c3-13), Lecture 6 p.6**: "if S = {v_1,…,v_n} ⊆ V, then S l.d. iff v_1,…,v_n l.d." This holds only when the
   v_i are pairwise distinct. Counterexample: v_1 = v_2 ≠ 0 makes the list v_1, v_2 l.d. (Ex 1.36(1)), but S = {v_1} is l.i.
   The span analogue (Rmk (1), c3-9) does state "if v_i ≠ v_j ∀i≠j (otherwise, remove repetitions)". Def 1.35(2) has the same gap:
   T = {v_1,…,v_k} must be listed without repetition (k = #T). Otherwise every nonempty S would be l.d. by listing one element twice.
   Suggested fix: add "with v_i ≠ v_j for i ≠ j".
3. **Lem 1.41 Pf (c3-23), Lecture 7 p.2**: the Pf uses Def 1.30(2) to get a nonempty T = {w_1,…,w_k} ⊆ S∖{v}. It misses the case
   S∖{v} = ∅ (S = {v}). In that case v ∈ span(∅) = {0} forces v = 0, and S = {0} is l.d. by Ex 1.36(2). This is a gap, not a typo.
4. **Prop 1.43 Pf (⇐) (c3-25), Lecture 7 p.3**: the Pf cites only "Lem 1.41". It also needs Prop 1.42 (⇒) first:
   span(S∖{v}) = span(S) ⇒ v ∈ span(S∖{v}), and then Lem 1.41 gives S l.d.
   The (⇒) direction cites "Unit 1.3 Notes", but the provided Unit 1.3 Notes PDF (2 pp.) stops at Def 1.30 and does not contain it.
5. **Lem 1.44 Pf (c3-27), Lecture 7 p.4**: "Henceforth, S ∪ {v} = … l.i." should be "Hence" (wording only).
   The Pf covers only finite nonempty S. The general S, and S = ∅, are not written.
6. Checked and correct, no errata: Ex 1.32(a) a = (x+y)/2, b = (x−y)/2 (the red x/1 = 2x/2 aid is kept); Ex 1.32(c) a = 0, b = 1, c = 1;
   Ex 1.36(1) coefficients a_ℓ; Ex 1.36(3) 0 = 2(1,1) − 1(2,2); Lem 1.44 b = 0 case and v = Σ(−a_i/b)w_i;
   Ex 1.38(1) (e_i)_{j1} = δ_ij (δ is symmetric, so fine).

#### Marker cards (proofs to write later)

| id | 배지 | what remains to be proved |
|---|---|---|
| c3-1 | EX | W = {(a,a,b) : a,b ∈ ℝ} is a subsp of ℝ³ (Subsp Crit) |
| c3-8 | PROP 1.33 | span(S) is a subsp of V containing S, and span(S) ⊆ W for every subsp W ⊇ S (FIS Thm 1.5, via Subsp Crit; handle S = ∅) |
| c3-15 | EX | v_2 = cv_1 ⇒ v_1, v_2 l.d. (e.g. 0 = c·v_1 − 1·v_2) |
| c3-19 | EXAM 1.38 (cont.) | (2) 1, x, …, xⁿ l.i. in ℝ[x]_{≤n} ("Pf: Exercise."); (3) sin x, cos x l.i. in 𝓕(ℝ,ℝ) (no Pf given) |
| c3-22 | COR 1.40 | contrapositive of Prop 1.39 (no Pf written) |
| c3-25 | PROP 1.43 | (⇒): S l.d. ⇒ ∃v ∈ S with span(S∖{v}) = span(S) ("Unit 1.3 Notes", not in the provided PDF); written (⇐) is in the toggle |
| c3-27 | LEM 1.44 | general case (S infinite, and S = ∅); the finite case is written in the toggle |

#### Reading and placement decisions
- Ex 1.32 and Ex 1.38 were each split into two cards, "(cont.)", so the written proofs stay next to their statements,
  following the Ex 1.36 precedent: 1.32 = (a)+Pf / (b)(c); 1.38 = (1)+Claim+Pf / (2)(3). The Claim stays inside EXAM 1.38 and is not a separate CLAIM card.
- Ex 1.32(c) "Sol:" stays in the card body because it is the example's worked answer. It is not in a toggle.
- RECALL c3-4: "(Def 1.31 (1))" was added as context. The red recap gloss "set of all l.c.s of w_1,…,w_k" was not carried over.
- Arrows with labels were moved to the top of the next card: "⇓ generalization" (c3-15) and "⇓ Contrapositive" (c3-22). Bare layout arrows were dropped.
- Glosses dropped: l.c. / l.d. / l.i. above the defined terms, "empty set", "fin", "gens", "i.e.", "iff", "soln", and the orange ※ above "contradiction" in Lem 1.44.
- Ex 1.38 e_2 example read at 600 dpi as [0;1;0;⋮;0], and e_n as [0;⋮;0;1].

### Inventory — la1/ch04.html (Unit 04 · §1.4 Basis and Dimension)

Source: Lecture 7 pp.4–6 (from the "§1.4 Basis and Dimension" heading) + Lecture 8 pp.1–6.
Lecture 8 p.1 "Last Time" recap + "Today" agenda skipped (no new content; recorded as an HTML comment).

| id | 배지 | Lecture·page | content (one line) | markers? |
|---|---|---|---|---|
| note04-1 | NOTE | L7 p.4 | Motivation: W = span(W) = span(W∖{0}) (l.d. unless W={0}); want S ⊆ W l.i. with span(S)=W ⇒ minimal spanning subset (Prop 1.43) | – |
| c4-1 | Q | L7 p.4 | Q: How to find such S? | – |
| c4-2 | DEF 1.45 | L7 p.5 | Basis (a) as a list β ∈ Vⁿ, (b) as a subset β ⊆ V; "(two defs agree for … ordered & … unordered)" | – |
| c4-3 | EXAM 1.46 | L7 p.5 | (1) ∅ basis of {0}; (2) standard basis (e_1,…,e_n) of ℝⁿ — proof in toggle | – |
| c4-4 | EXAM 1.46 (3)(4) | L7 p.5–6 | (3) std basis (1,x,…,xⁿ) of ℝ[x]_{≤n}; (4) (1,x+1,(x+1)²) basis of ℝ[x]_{≤2}; both "Pf: Exercise" | yes |
| c4-5 | REM | L7 p.6 | Comment: basis not unique in gen'l; (1,x,x²) & (1,(x+1),(x+1)²) are bases (plural of basis) of ℝ[x]_{≤2} | – |
| c4-6 | REM | L8 p.1 | By def, l.i. v_1,…,v_n form a basis of span(v_1,…,v_n) | – |
| c4-7 | EXAM 1.47 | L8 p.1 | {xⁿ : n ∈ ℤ_{≥0}} (infinite-set {1,x,x²,…}) is a basis of ℝ[x]; "Pf: Unit 1.4 notes (only for Math-Major)" | yes |
| (section) | — | L8 p.2 | section-title "Properties of bases · 기저의 성질" | – |
| c4-8 | PROP 1.48 | L8 p.2 | v_1,…,v_n basis iff every w has a unique l.c.; proof (⇒) ▨ (⇐) □ in toggle | – |
| c4-9 | REM | L8 p.3 | Coordinates [w]_β ∈ ℝⁿ relative to β (Unit 2 preview) | – |
| c4-10 | Q | L8 p.3 | "In many cases … span(S) … S fin." Q: Does span(S) have a basis? ⇓ Yes! | – |
| c4-11 | PROP 1.49 | L8 p.3–4 | V = span(S), S fin ⇒ ∃ β ⊆ S basis; proof by contradiction (S_1 ⊋ S_2 ⊋ …) in toggle | – |
| c4-12 | REM 1.50 | L8 p.4 | Chain S = S_1 ⊋ … ⊋ S_ℓ, ℓ ≤ n+1, S_ℓ l.i. basis of V | – |
| c4-13 | EXAM 1.51 | L8 p.4–5 | S = {(1,0,0),(0,1,0),(3,2,1),(1,0,−1)}: drop (1,0,−1), T l.i. (Cor 1.40, Lem 1.44), β := T basis, span(S) = ℝ³ | – |
| c4-14 | REM | L8 p.5 | Every v.sp has a basis; hard case needs Optional §1.7* of FIS (Math Major Only!) | – |
| c4-15 | REM 1.52 | L8 p.6 | Both bases in Ex 1.51 have 3 elts; common pattern? ⇓ Yes by two Results! | – |
| c4-16 | THM 1.53 | L8 p.6 | Replacement Thm: m ≤ n and ∃ H ⊆ G, #H = n−m, B ∪ H spans V; "Pf: Math-Major Only (in §1.6 of FIS)" | yes |
| c4-17 | EX 1.54 | L8 p.6 | Use Replacement Thm: V = span(G), #G < ∞ ⇒ every l.i. B ⊆ V has #B < ∞ | yes |
| c4-18 | COR 1.55 | L8 p.6 | β fin basis ⇒ every basis β̃ fin and #β̃ = #β; proof in toggle | – |
| note04-99 | NOTE | — | Lecture 9까지 반영, 마지막 내용 Ex 1.61 안내 | – |

Totals: 18 TOC cards (def 1, thm 4 [PROP 1.48, PROP 1.49, THM 1.53, COR 1.55], rem 8 [incl. 2 Q], exam 4, ex 1) + 2 note-cards.
Proof toggles: 4 (c4-3, c4-8, c4-11, c4-18). Marker pairs: 4.

#### Arithmetic check (Ex 1.51)
- 4(1,0,0) + 2(0,1,0) − (3,2,1) = (4−3, 2−2, 0−1) = (1,0,−1) ✓
- (3,2,1) − 3(1,0,0) − 2(0,1,0) = (0,0,1) ✓

#### Errata candidates
1. Lecture 8 p.1 "Last Time" recap (skipped, not in page): "(b) β ⊆ S of V is a l.i. subset that also spans V" → should be "β ⊆ V". (known)
2. Lecture 7 p.4 Motivation (note04-1): "It would be nize if we can find …" → "nice". Kept verbatim. (Third letter is clearly drawn as z; compare the c in "can" on the same line.)

#### Other observations (not errata, kept verbatim)
- COR 1.55 proof (c4-18): applies the Replacement Thm to β̃ (which requires #β̃ < ∞) without first proving the "every basis β̃ is fin" part; that finiteness follows from Exercise 1.54. Gap in the written proof — no markers placed (proof is written), but a later proof-writer may want to add one line citing Ex 1.54.
- PROP 1.49 proof (c4-11): "T is l.d. (∗) (or T is a basis for V)" — the parenthetical means "otherwise T would be a basis for V". Kept as written.
- EX 1.54 (c4-17): "prove that if …, then ∀B ⊆ V l.i. (…), then #B < ∞" — double "then", kept.
- Comment (c4-5) writes "(1, (x+1), (x+1)²)" with parentheses around x+1, while Ex 1.46(4) writes "(1, x+1, (x+1)²)"; same list, kept as written.

#### Transcription choices
- Ex 1.51 green annotation (overbrace above e_1, e_2 with a rotated ∈ at its tip, labelled "span(β) = span(S) by (★)") rendered as \overbrace{e_1, e_2}^{∈ span(β) = span(S) by (★)}. The green star label (★) is rendered as \bigstar; the purple (∗) as (*).
- Motivation red annotation "l.d. unless W = {0}" under W∖{0} rendered as \underbrace.
- "S ← l.i. & spanning set of W (= V as special case)" with purple "both" under "l.i. &" rendered as "(S: both l.i. & spanning set of W (= V as special case))".
- Ex 1.47 red underbrace "infinite-set {1, x, x², x³, …}" rendered in parentheses after the set; orange "∞-set" gloss dropped.
- Dropped pure glosses: "min'l" (above minimal), "std" (above standard), "there exists unique" (above ∃!), "rel" (above relative), "#" (above number), "constr" (above construction). Kept "plural of basis" as "(plural of basis)" after "bases".
- Red circles on entries (Ex 1.51 third coordinates, e_3) and boxes around "Yes!" not reproduced.

#### Marker cards (proofs to write later)
| id | 배지 | what remains to be proved |
|---|---|---|
| c4-4 | EXAM 1.46 (3)(4) | (3) (1, x, …, xⁿ) is l.i. and spans ℝ[x]_{≤n}; (4) (1, x+1, (x+1)²) is l.i. and spans ℝ[x]_{≤2} |
| c4-7 | EXAM 1.47 | {xⁿ : n ∈ ℤ_{≥0}} is l.i. (every finite subset) and spans ℝ[x] |
| c4-16 | THM 1.53 | Replacement Theorem (m ≤ n and ∃ H ⊆ G with #H = n − m, B ∪ H spans V) — FIS §1.6 |
| c4-17 | EX 1.54 | If V = span(G), #G < ∞, then every l.i. B ⊆ V is finite (use Thm 1.53 on finite subsets of B) |


### Lecture 9 추가 반영 (2026-10-07) — la1/ch04.html

Source: `Lecture 9 on 221 F26.pdf`, 6 pages. p.1 Last Time / Today는 중복 복습이므로 제외. 새 내용은 모두 §1.4에 이어 붙였다. 기존 Lecture 1–8의 인벤토리와 중복 여부 확인. 퀴즈 페이지는 10/7 후속 요청으로 Lecture 9 추가 복습을 포함하도록 갱신했다. 실제 2026 Quiz 1 범위와 구분한다.

| id | 배지 | 쪽 | 내용 | 증명 |
|---|---|---|---|---|
| note04-3 | NOTE | 1 | Cor 1.55 leads to def of dimension | — |
| c4-19 | DEF 1.56 | 1 | 유한차원, 차원 정의와 기저 선택 독립성 | — |
| c4-20 | DEF 1.57 | 1 | 무한차원 | — |
| c4-21 | EXAM 1.58 (1)–(4) | 2 | 영공간, ℝⁿ, 차수 제한 다항식, ℝ[x]의 차원 | (4) 원문 증명 |
| c4-22 | EXAM 1.58 (5) | 2 | 행렬공간의 차원 mn, 표준 행렬 E_ij | Exercise를 자체 증명으로 보완 |
| c4-23 | COR 1.59 | 2–4 | 차원에 의한 기저 판정, 기저 확장정리 | 원문 + 보충 |
| c4-24 | EXAM 1.51 | 4 | 차원을 이용한 Ex 1.51 재방문 | 본문 논증 |
| c4-25 | Q | 4 | 부분공간의 기저와 차원에 관한 질문 | — |
| c4-26 | THM 1.60 | 4–5 | dim W ≤ dim V, 차원이 같으면 W=V | 원문 + 보충 |
| c4-27 | EXAM 1.61 | 5–6 | 좌표합 0인 공간, 기저 e_i−e_(i+1), 차원 n−1 | 원문 + 보충 |

검토·보완 사항:
- Cor 1.59(2) 원문 증명에서 생략한 역방향을 보충 증명에 추가했다.
- Cor 1.59(3)의 교체정리 적용 전에 γ의 유한성(Exercise 1.54)이 필요하므로 보충했다.
- Thm 1.60(1)의 “By Prop 1.49 & a Rmk”는 일반 기저 존재에 관한 앞선 주의를 참조한다. 유한 생성집합을 아직 모르는 W에 Prop 1.49만 직접 적용할 수 없으므로, 최대 dim V번의 벡터 추가로 유한 기저를 얻는 보충 증명을 제공했다.
- Ex 1.61의 나열식은 작은 n에서 항이 겹쳐 보일 수 있다. a₀=aₙ=0을 쓴 통일된 전개와 n=1의 빈 기저를 보충 증명으로 처리했다. W가 진부분공간인 이유(e₁∉W)도 명시했다.
- 원문의 색상은 생략하고 수학적 곁말은 괄호로 보존. Cor 1.59의 벤 다이어그램은 fig-note로 설명.


### Lecture 12 반영 (2026-10-19) — la1/ch04.html · la1/ch05.html

Source: `Lecture 12 on 221 F26.pdf`, 7 pages (p.7은 위쪽만). p.1 Last Time(차원 정의·BET·Thm 1.60 복습)과 Today 안내는 새 내용이 없어 제외. 판독 보조로 `Unit 2.1 … Notes at KU.pdf`(L12 pp.4–7과 동일)를 대조했다.

| id | 배지 | 쪽 | 내용 | 증명 |
|---|---|---|---|---|
| (section) | — | 1 | ch04 section-title "Application: Lagrange Interpolation Formula · 응용: 라그랑주 보간 공식" | — |
| note04-4 | NOTE | 1–2 | Motivation(서로 다른 t_i의 자료점을 지나는 다항식) + 그림 + Strategy(ℝ[x]≤n의 적당한 기저의 일차결합) | — |
| c4-28 | DEF 1.62 | 2 | 라그랑주 다항식 f_i = ∏_{j≠i}(x−t_j)/(t_i−t_j), n차, 관찰 f_i(t_j) =(★) δ_ij | 자체 증명(잘 정의됨·차수·★) |
| c4-29 | PROP 1.63 | 2 | 라그랑주 다항식은 ℝ[x]≤n의 기저 | 원문 + 보충(대입의 근거, 서로 다름·원소 수) |
| c4-30 | COR 1.64 | 3 | 라그랑주 보간 공식(LIF): ∃! p ∈ ℝ[x]≤n, p(t_i) = y_i | 원문(존재 ▨ / 유일 □) + 보충(Prop 1.62→1.63, 계산 전개, 차수) |
| c4-31 | EXAM 1.65 | 3–4 | (1,8),(2,5),(3,−4)를 지나는 다항식 = −3x²+6x+5 | 원문 Sol 본문 + 보충(검산, 차수 제한 없는 경우) |
| note04-99 | NOTE | — | Lecture 12 pp.1–4까지, 나머지는 ch05 안내 | — |
| (section) | — | 4 | ch05 section-title "Unit 2: Linear Transformations · 2단원: 선형변환" | — |
| note05-1 | NOTE | 4 | This unit is about "special" fcns btwn v.s. | — |
| note05-2 | NOTE | 4–5 | Motivation: 포토샵 연산(π/2 회전·층밀림 그림), 원점·직선·평행사변형 보존 → 덧셈·스칼라곱 보존 | — |
| c5-1 | DEF | 5 | Set Theory Warm-Up: 정의역·공역, im = range(FIS) = f(X), 역상 f⁻¹(Z), 전단사일 때 역함수에 의한 상과 일치 | 자체 증명(괄호 안 주장) |
| (section) | — | 5 | "§2.1 Linear Maps: ker, im, and isom · 2.1 선형사상: 핵, 상, 동형사상" | — |
| note05-3 | NOTE | 5 | As in Motivation, + & · 를 보존하는 함수 | — |
| c5-2 | DEF 2.1 | 6 | 선형변환(lin map/homomorphism), (1)(2), 𝓛(V,W), 𝓛(V) | — |
| c5-3 | REM 2.2 | 6 | T(0_V) = 0_W, T(−v) = −T(v) | 원문(▨/□) |
| c5-4 | EXAM 2.3 (1) | 6–7 | R:(x,y)↦(−y,x) 반시계 π/2 회전은 선형사상; "Pf: Next Class!" | 자체 증명(+그림의 뜻) |
| note05-99 | NOTE | — | Lecture 12까지 반영, Ex 2.3(1) 원문 증명은 다음 강의 | — |

Totals: ch04 31 TOC cards · note 4 · ko/en 토글 각 23. ch05 4 TOC cards · note 4 · 토글 각 3.

#### Arithmetic check (Ex 1.65)
- f_0 = (x−2)(x−3)/((1−2)(1−3)) = ½(x²−5x+6), f_1 = (x−1)(x−3)/((2−1)(2−3)) = −(x²−4x+3), f_2 = (x−1)(x−2)/((3−1)(3−2)) = ½(x²−3x+2) ✓
- 8f_0+5f_1−4f_2 = (4−5−2)x² + (−20+20+6)x + (24−15−4) = −3x²+6x+5 ✓; p(1)=8, p(2)=5, p(3)=−4 ✓

#### Transcription choices
- 보라색 (★)(오각별)는 `(\bigstar)`, 파란 "x = t_j"는 `\overset{x=t_j}{\Longrightarrow}`, 파란 "∈ ℝ[x]≤n"은 "deg n poly"의 underbrace 첨자로.
- Set Theory Warm-Up의 빨강 "domain"/보라 "codomain"은 X, Y 아래 underset, 갈색 "(FIS)"는 range 위 overset, 빨간 괄호 설명(전단사일 때)은 괄호 문단으로 보존.
- Def 2.1·Rmk 2.2의 주황 괄호식(T(v_1+v_2) = T(v_1)+T(v_2) 등)은 괄호로 제자리에, 파란 근거 표기(Prop 1.17(1), Def 2.1)는 등호 위 overset.
- 버린 순수 곁말: dimension, f.d., BET(p.1 Last Time), assoc, WTS, eqn, LIF, lin/transf/hom/fcn, im, preimg. 동그라미("lin map")·밑줄·색은 미반영.
- 그림 5개(자료점 곡선, 회전, 층밀림, 평행사변형 소품, Ex 2.3(1) 기울기 그림)는 fig-note 설명줄.
- Lecture 12 1차 작업(2026-10-15, pickerel 워크트리)은 커밋 전에 워크트리와 함께 사라졌다. 이 표는 10/19 원본에서 새로 작업한 결과다.

### 과거 퀴즈 반영 (2026-10-07)

`la1/src/`에 Fall 2025 Quiz 1·2 문제지와 Solutions PDF 4개 추가(각 4쪽). 원본 문제 pp.2–3와 해설 pp.2–3을 시각 대조했다.

| 페이지 앵커 | 출처 | 내용 |
|---|---|---|
| past-q1-1 | Quiz 1 p.2 / Solutions p.2 | x₁=5x₃ 부분공간, 12점; 판정법·생성공간 두 풀이 |
| past-q1-2 | Quiz 1 p.3 / Solutions p.3 | v=(9,4,−3)=−2u₁+3u₂, 12점 |
| past-q2-1a | Quiz 2 p.2 / Solutions p.2 | B 역행렬, 6점; 전체 행연산 |
| past-q2-1b | Quiz 2 p.2 / Solutions p.2 | [L_A]_γ=B⁻¹AB, 6점; 열별 추가 검산 |
| past-q2-2 | Quiz 2 p.3 / Solutions p.3 | ℝ⁴의 네 벡터 일차독립 판정, 12점; rank=3, 종속관계 추가 검산 |

문제는 영문 원문·수치·배점을 유지. 답안은 원본 해설 논증을 영어 문장으로 정리하고 한국어 해설을 추가했다. Quiz 2는 Lecture 9 이후 학습할 주제임을 표시했다. 과거 시험 일시를 올해 일정으로 표시하지 않는다.

오타: Quiz 2 Solutions p.2의 1(a) 마지막 첨가행렬 오른쪽 아래 −2는 −3의 오기. 최종 상자 답과 곱 검산에 맞추어 풀이를 수정했다. PDF 텍스트 추출의 β/γ 오인식은 문제지·손글씨 시각 확인으로 교정했다.

Lecture 9 보충: dimension-review 개념 블록, P11(차원으로 기저 판정), P12(ℝ⁴ 좌표합 0), P13(M₂×₃ 표준기저) 추가. P11–P13은 편집 연습문제이며 기출과 별도 표시한다.

### Lecture 13 반영 (2026-10-19) — la1/ch05.html

Source: `Lecture 13 on 221 F26.pdf`, 8 pages (p.8은 위쪽만). p.1 Last Time(Def 2.1·𝓛(V,W)·Rmk 2.2 복습)과 Today("Continue §2.1 Linear Maps: ker, im, isom (Exs)")는 새 내용이 없어 제외. Unit 노트(2.x)는 아직 없음. 이번에는 메인 루프가 직접 전사·번역·자체 증명.

| id | 배지 | 쪽 | 내용 | 증명 |
|---|---|---|---|---|
| c5-4 | EXAM 2.3 (1) | L12 6–7 · L13 1–2 | (갱신) en "Pf: Next Class!" 삭제, Proof 토글 = L13 원문(WTS·(1) ▨·(2) □), 옛 자체 증명의 그림 설명은 보충 증명 | 원문 + 보충(그림의 뜻) |
| c5-5 | EXAM 2.3 (2) | 2 | T(x,y,z) = ax+by+cz는 선형; "Pf: Exercise (Similar to Ex 2.3(1))" | 자체 증명(스칼라를 d로) |
| c5-6 | EXAM 2.3 (3) | 2 | 미분 D : ℝ[x]≤n → ℝ[x]≤n−1, "b/c (f+g)′ = f′+g′ …", "Take this granted (Calc I)" 계수 공식 | 보충(계수 공식으로 잘 정의됨·선형, n = 0) |
| c5-7 | EXAM 2.3 (4) | 2–3 | 항등사상 I_V = 𝟙_V, 선형연산자 | 원문 |
| c5-8 | EXAM 2.3 (5) | 3 | 영사상 T_0, 기호의 남용 0 ∈ 𝓛(V,W); "Pf: Exercise: Similar to Ex 2.3(4)" | 자체 증명 |
| c5-9 | EX | 3 | T(∑a_i v_i) = ∑a_i T(v_i), "Hint: use Induction on n" | 자체 증명(귀납법) |
| c5-10 | REM 2.4 | 3–4 | 𝓛(V,W)는 +, ·로 벡터공간; "Pf: Exercise (Similar to Ex 1.8 …) □ (also need … T+U & cT are lin maps)" | 자체 증명(1단계 닫힘, 2단계 VS 1–8) |
| (section) | — | 4 | "Kernel and Image · 핵과 상" | — |
| note05-4 | NOTE | 4 | Motivation: 근 f⁻¹(0)과 치역 f(ℝ) → 선형사상에서도 | — |
| c5-11 | DEF 2.5 | 4 | ker(T) (null space, FIS) = T⁻¹(0) ⊆ V, im(T) (range, FIS) = T(V) ⊆ W | — |
| c5-12 | PROP 2.6 | 4–5 | ker(T) ≤ V, im(T) ≤ W | 원문(▨/□) |
| c5-13 | EXAM 2.7 | 5 | ker(ax+by+cz)는 부분공간, "Later: plane (dim 2) iff (a,b,c) ≠ 0", 그림(a=0,b=1,c=1) | 보충(Later 주장: R-N 및 직접 기저) |
| c5-14 | PROP 2.8 | 6 | T 1-1(injective) ⟺ ker(T) = {0} | 원문(▨/□) |
| c5-15 | PROP 2.9 | 6 | V = span{v_1,…,v_n} ⇒ im(T) = span(T(v_1),…,T(v_n)) | 원문(▨/□) |
| c5-16 | EXAM 2.10 | 7 | T(x,y) = (x+y, x+y): im = span((1,1)), ker = span((1,−1)); "T ∈ 𝓛(ℝ²) (Exercise)" | 자체 증명(선형성) + 계산 세부 |
| c5-17 | Q | 7 | Observation: dim V, dim ker, dim im의 관계? ⇓ Yes! | — |
| c5-18 | DEF 2.11 | 7 | nullity(T) := dim ker(T), rank(T) (rk) := dim im(T) | — |
| c5-19 | THM 2.12 | 7–8 | Rank-Nullity Thm (Dim Thm in FIS): dim V = nullity + rank; "Pf of R-N when V f.d." … "Pf of WTS in next class!" | 원문(미완, qed 없음) + 보충((i) 근거 (ii) WTS (iii) 결론 (iv) 무한차원) |
| note05-99 | NOTE | — | Lecture 13까지 반영, WTS는 다음 강의, 동형사상 미착수 | — |

Totals: ch05 19 TOC cards · note 5 · ko/en 토글 각 17 · qed 32.

#### Transcription choices
- p.1–2의 Ex 2.3(1) 증명에서 파란 "WTS"는 굵은 라벨, 소단계 끝 빗금 상자는 ▨(part-end).
- p.2의 초록 "Take this granted"와 파란 Calc I 공식은 en "Take this granted (Calc I):" + display로, 주황 "u = m−1"은 등호 위 overset.
- 주황 곁말(fcn, lin, transf, hom, id, op, ker, im(g), sp, rk, inj, R-N Thm)은 순수 풀이라 버렸다. 단 "1-1" 위의 "injective"는 증명이 "inj"로 쓰므로 괄호로 남겼고, rank 위의 "rk"는 증명이 rk(T)를 쓰므로 "(rk)"로 남겼다.
- 갈색 "(FIS)"(null space, range 위)는 "(FIS)"로 제자리에. 파란 "(= T⁻¹(0) preimg of 0)", "(= T(V))"는 괄호식으로 유지.
- 등호 위 근거(Rmk 2.2, T lin, def, T lin + Exercise)는 overset/substack. 동그라미 친 등호·밑줄·색 박스(Thm 2.12의 빨간 상자)는 미반영.
- p.8 im(T) 계산에서 빨간 사선으로 지운 T(v_1),…,T(v_k)(위에 0)는 underbrace "= 0", 초록 중괄호 "n−k elts"는 underbrace 첨자.
- p.5 Ex 2.7의 점선 상자 그림(P = ker(T), a=0, b=1, c=1인 평면)은 fig-note.
- 𝟙_V는 `\mathbb{1}_V`(MathJax 4 기본 글꼴에 있음 — 브라우저 확인).
- c5-8: 노트의 "(Pf: Exercise: Similar to Ex 2.3(4))"는 화살표로 "is a lin map"에 걸려 있어 그 문장 뒤로 옮겼다(Abuse of notation 앞).
- 흐름 화살표 ⇓(Ex 2.10 → Observation, Def 2.11 → Thm 2.12)는 Observation 카드의 "⇓ Yes!"만 남겼다.

#### 검증 (2026-10-19)
- Opus 적대적 검증 1회(L13 원본 8쪽 대조): MUST-FIX 0. SHOULD-FIX 3 반영(c5-17 ko 괄호, c5-4 보충을 극좌표 논증으로 일반화, c5-6 n = 0 설명), NIT 6 반영(c5-16 선형성 첫 단계·핵 기저의 일차독립, c5-13 두 벡터가 ker에 속함, c5-10 괄호·문자 S→F, note05-4 "상", note05-99 링크 → note04-4, c5-8 Pf 위치).
- headless Chrome(lazy 해제, 증명 펼침): ch05 수식 838개 MathJax 오류 0, 500px·1400px 넘침 0, 𝟙(NCM-DS 글리프) 정상.
- midterm.html: Opus 검증 1회 — 문제 원문 11개 일치, 정답·증명·정정 3건 모두 확인, MUST-FIX 0; SHOULD-FIX 2·NIT 4 반영. 수식 525개 오류 0, 넘침 0.


### 중간고사 기출 반영 (2026-10-19) — la1/midterm.html

`la1/src/`에 Fall 2024·2025 중간고사 문제지와 Solutions PDF 4개 추가. 문제는 LaTeX 시험지에서 원문 그대로(행렬은 PDF 이미지로 확인), 풀이는 손글씨 공식 해설과 시각 대조. 형식은 `quiz1.html`의 qs-block(영어 원문 `qs-en` + 한국어 번역 `qs-ko` + `details.qs-proof` 영어 모범답안·한국어 해설). 빌드는 Opus 에이전트, 정답은 메인 루프가 독립 검산.

| 앵커 | 출처 | 내용 · 정답 |
|---|---|---|
| mt25-1a | F25 p.2 / Sol p.2 | [[2,1,3],[0,−2,1]](3(1,1,1)−(2,−1,4)) = (3, −9), 6점 |
| mt25-1b | F25 p.2 / Sol p.2 | (2B+C)(2,3) = [[3,1],[−1,3],[4,2]](2,3) = (9, 7, 14), 6점 |
| mt25-2 | F25 p.3 / Sol p.3 | v₃ = (0,6,t): 일차종속 ⟺ t = 5 (v₁+2v₂−v₃ = 0), 12점; 풀이 1(동차 연립)·풀이 2(v₃ ∈ span) |
| mt25-3 | F25 p.4 / Sol p.4 | ker T 기저 {(1,1,−1,0), (0,0,0,1)}, 12점 |
| mt25-4 | F25 p.5 / Sol p.5 | {u,v,w,s} l.i. ⇒ {u+s,v+s,w+s} l.i., 9점; 직접 증명(원본은 귀류법) |
| mt25-5 | F25 p.6 / Sol p.6 | T(x³…x⁶)=0 ⇒ im T ≠ M₂(ℝ), 9점; 풀이 1(nullity ≥ 4, R-N) · 풀이 2(im = span(T(1),T(x),T(x²))) |
| mt24-1 | F24 p.2 / Sol p.2 | 짝함수 전체는 𝓕(ℝ,ℝ)의 부분공간, 10점 |
| mt24-2 | F24 p.3 / Sol p.3 | (1,1,1),(1,2,3),(1,5,8)은 𝔽³의 기저(예), 10점; 풀이 1(LEM 1.44) · 풀이 2(정의, 원본 계산 정정) |
| mt24-3 | F24 p.4 / Sol p.4 | ker T 기저 {(1,0,−4,1), (0,1,2,0)}, 10점 |
| mt24-4a | F24 p.5 / Sol p.5 | [x²+x+1]_β = (7,5,1), 6점 |
| mt24-4b | F24 p.5 / Sol p.5 | [T]_β = [[2,−2,0],[0,1,−4],[0,0,0]], 6점 |

공식 해설 정정(페이지 `#pitfalls`에 표시):
- F24 Sol p.3 #2 Sol 2: c = −a−b = −(7/3)a, (3) → −(65/3)a = 0 은 오산. 바르게는 c = (1/3)a, (3) → −(1/3)a = 0. 결론(a=b=c=0, 기저)은 같음.
- F25 Sol p.4 #3: "x, w ∈ ℝ²" → x, w ∈ ℝ.
- F25 Sol p.1 표지 날짜 "Tuesday, June 17th"는 양식 잔재(문제지: Monday, October 20th).
- F25 Sol p.3 #2 Sol 2의 "From class (§1.5)" = 2026 노트 Lem 1.44 + Lem 1.41(또는 Prop 1.43), 노트 §1.3. "§1.5"는 FIS 교재 절 번호(Thm 1.7)로 보임.
- F25 Sol p.5 #4: (a,b,c) ∈ ℝ³∖{0} — 시험 관례상 𝔽 (무해).
- 두 벡터의 일차독립을 "둘 다 0이 아니고 스칼라배가 아님"으로 보이는 공식 해설 방식(F25 #2·#3, F24 #2·#3)은 벡터 2개일 때만 유효 — 해설에 주의로 표시.

범위 표시: 2024 #4(b) 행렬표현은 2026 강의계획서상 9–10주차(중간 이후)로 표시. 과거 시험 날짜를 올해 일정으로 쓰지 않음. 2026 중간고사는 강의계획서상 8주차 화요일(잠정).
