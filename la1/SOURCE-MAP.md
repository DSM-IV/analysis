# 선형대수학 1 SOURCE-MAP

소스: `la1/src/` (원본은 `~/Desktop/26-2/선형대수학1/`)
- `Syllabus 221 F26.pdf` — MATH221 Linear Algebra I, Fall 2026, Changho Han (Korea Univ., 비전공 분반). 교재 Friedberg–Insel–Spence 5e(연습문제용).
  성적: 출석 10 / 퀴즈 20 (5·13주차 목요일) / 중간 35 (8주차 화) / 기말 35 (16주차 화). **답안은 영어로만(다른 언어 0점).**
  진도: 1–4주 §1 Vector Spaces → 5–7주 §2(1) 선형변환 → 8주 중간 → 9–10주 §2(2) 행렬표현 → 11–13주 §3 기본행연산·연립방정식 → 14–15주 §4 행렬식.
- `Course Intro.pdf` (5쪽) = Lecture 1 pp.1–5 와 동일 내용.
- `Lecture N on 221 F26.pdf` (N=1..8) — **손글씨 태블릿 노트**(텍스트 추출 불가 → Read 도구로 시각 전사). 1–5는 9/17, 6–8은 10/1에 Desktop에 추가됨.
  분량: L1 6 · L2 8(p8 빈 쪽) · L3 8 · L4 6 · L5 7 · L6 8 · L7 6 · L8 6쪽.
- `Unit 1.x of Linear Algebra I (non-math major) Notes at KU*.pdf` — 강의자가 정리한 단원 노트(1.1 8쪽, 1.2 6쪽, 1.3 2쪽; 강의노트와 같은 손글씨).
  강의 슬라이드와 내용·번호 동일 → **전사 원본은 Lecture PDF**, Unit 노트는 판독 보조. Unit 1.3은 Def 1.30까지만 있음.

**번호 체계:** 강의노트가 전역 번호(Def 1.1 … Cor 1.55)를 쓴다 → 카드 배지 = 노트의 라벨·번호 그대로 (`DEF 1.9`, `THM 1.20`, `PROP 1.28`, `LEM 1.15`, `COR 1.16`, `REM 1.10`, `NOTE 1.5`, `NOTATION 1.7`, `EXAM 1.8`(Ex = Example), `EX 1.27`(Exercise)). 번호 없는 항목은 유형 배지만(DEF/REM/NOTE/Q/RECALL/CLAIM/EXAM/EX). 카드 id는 자체 순번 `c{단원}-{순번}`, 서술 단락은 note-card `note{단원2자리}-{순번}`(목차 제외).
**규칙 요약:** 각 강의 첫머리 "Last Time" 복습은 카드로 만들지 않음(새 내용이 있을 때만 RECALL 카드). 손그림은 `p.fig-note` 한 줄 설명. 증명 중간 끝 표시 ▨ = `span.part-end`. 노트에 증명이 없는 진술("Pf: Exercise", "See FIS", "Unit notes", "Math-Major Only", "Pf Idea")은 자체 증명(마커 → 증명 토글; 노트 증명이 이미 있으면 "보충 증명" 토글). en = verbatim(오타 포함), ko = 바른 뜻.
**퀴즈 요약:** `la1/quiz1.html` — Quiz 1(5주차 목, 2026-10-01) 대비 요약. 이 페이지만 MathJax 4.1.3(인라인 자동 줄바꿈).
**진행 상태 (2026-10-01):** 4단원 빌드·번역·자체 증명(마커 0)·Opus 검증 4/4 완료. 인벤토리의 "markers? yes" 표기는 빌드 시점 기록 — 현재는 모두 증명 토글/보충 증명으로 채워짐. la1 전 페이지 MathJax 4.1.3.
**갱신 절차:** 새 Lecture PDF → `la1/src/` 복사 → 해당 단원 파일 끝(마지막 note 앞)에 카드 append(ch04는 `note04-99` "Lecture 8 ends here" 노트를 갱신) → 번역 → 자체 증명 → 검증 → 이 인벤토리·la1/index 카드 수·홈 칩 갱신. 다음 단원은 §1.5(차원 계속) 또는 §2 선형변환 — 새 파일 ch05.

## 전체 구조 (2026-10-01)
| 단원 | 제목 | 소스 |
|---|---|---|
| ch01 | 1.1 벡터공간으로서의 ℝⁿ | Lecture 1 (강의 소개 포함) · Lecture 2 · Lecture 3 p.2 |
| ch02 | 1.2 벡터공간과 부분공간 | Lecture 3 pp.2–8 · Lecture 4 · Lecture 5 pp.1–6 |
| ch03 | 1.3 일차결합, 생성, 일차독립 | Lecture 5 pp.6–7 · Lecture 6 · Lecture 7 pp.1–4 |
| ch04 | 1.4 기저와 차원 | Lecture 7 pp.4–6 · Lecture 8 (진행 중) |

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
| note04-99 | NOTE | — | "Lecture 8 ends here; §1.4 continues in the next lecture." (placeholder for unit in progress) | – |

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
