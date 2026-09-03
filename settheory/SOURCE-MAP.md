# 집합론 SOURCE-MAP

소스: `[2026-08-28] Lecture note(집합론).pdf` (리포 루트, 50쪽, 영문)
저자: Ildoo Kim (Korea University). 교재 기반: Pinter, *A Book of Set Theory* (Courier, 2014).
**소스가 영문** → en-formal = verbatim 전사, ko-formal = 번역 (LA와 같은 방향).
**학기 중 갱신되는 자료** — 파일명 날짜(2026-08-28) 기준 스냅숏. 이후 갱신 PDF가 오면 아래 인벤토리와 diff하여 증분 추가한다. 환경 번호(N.M)는 소스 번호를 그대로 카드 번호로 쓴다.

## 전체 구조

| 섹션 | 제목 | PDF 페이지 | 환경 수 | Exercise |
|---|---|---|---|---|
| §1 | Historical Introduction | 1–4 | 16 | 2 |
| §2 | Sentence and Logic | 5–11 | 22 | 5 |
| §3 | Classes and Sets | 11–33 | 89 | 14 |
| §4 | Functions | 33–50 | 77 | 20 |
| 계 | | 50쪽 | **204** | **41** |

§3·§4는 분량(각 89·77 환경)이 커서 사이트에서는 3분할씩, 총 **8페이지(ch01–ch08)**.
페이지 제목은 "3. Classes and Sets (i): …" 식으로 소스 섹션 번호를 보존한다.

## 환경 유형 → 카드 클래스 매핑

- `def-card`: Definition, Undefined notion, Notation, **Axiom** (배지: 정의/무정의 용어/표기/공리)
- `thm-card`: Theorem, Lemma, Corollary (배지: 정리/보조정리/따름정리)
- `rem-card`: Remark, Idea, Question, **Paradox** (배지: 주의/아이디어/질문/역설)
- `exam-card`: Example (배지: 예)
- `ex-card`: Exercise (배지: 연습문제) — 소스에 풀이 없음. 우리가 양언어 풀이 작성(PROOF 마커).

원문에 Proof가 있는 정리는 증명도 verbatim 전사(EN) + 번역(KO)하여 proof-toggle에 넣는다.
"The proof of (2) is left as an exercise" 같은 문장도 verbatim 유지.

## 그림 (SVG 재현 필요)

- p16 Figures 1–4: Venn diagrams (A∪B, A∩B, Aᶜ, A∩(B∪C)) — ch03 (Def 3.27 다음 서술 단락)
- p25 Figures 5–6: coordinate diagrams (A×B, (A×B)∩(C×D)) — ch04 (Remark 3.57)
- 해칭(빗금) 스타일은 SVG pattern으로 재현

## ERRATA / 역주 후보 (en verbatim 유지, 풀이·역주에서 처리)

1. **Ex 4.60은 의도된 메타 문제**: Thm 4.59(2) 증명(p47)의 오류를 찾으라는 문제. 오류: "y = f(x) ∧ x ∈ Cᵢ for all i ⟺ ∃x ∈ Cᵢ ∋ y = f(x) for all i"의 역방향이 성립하지 않음(i마다 x가 다를 수 있음). 등호가 성립할 추가 조건은 f 단사. 정리 4.59(2)의 서술 자체(⊂)는 참이나 증명이 ⟺ 사슬로 등호를 도출하는 형태라는 점을 풀이에서 지적할 것.
2. ~~p15 Def 3.24 아래 "quaranteed" 오탈자 추정~~ — ch03 빌더가 텍스트 레이어로 확정: **"guaranteed"가 맞음** (오탈자 아님). 단, 해당 문장의 종결 마침표 누락은 실재하며 verbatim 유지됨.
3. Def 4.51/4.52 원문에 "we denote the graph(?)"의 "(?)"가 실제로 인쇄되어 있음 — verbatim 유지, 역주로 저자의 자기 표시임을 언급 가능.
4. Ex 3.89 "(1) dom G is a set (2) Ran G is a set" — "Ran" 대문자 표기 원문 그대로.
5. Axiom 1.10 "Zermelo's axiom of selection" = 표준 용어로는 분리공리(axiom of separation/Aussonderung). 선택공리(axiom of choice, 4.64)와 혼동 금지 — GLOSSARY 참조.
6. Def 4.14 항목 (1)–(4)가 "Definition 4.14. (1) …" 형태로 시작 — 인벤토리 name 필드의 "(1)"은 파싱 부산물이며 제목 아님.
7. Thm 2.19는 8개 법칙 중 (1)만 증명, 나머지는 "exercises"라고만 언급(번호 붙은 Exercise 없음) — 풀이 범위는 번호 붙은 Exercise 41개만.
8. **빌드 단계에서 확정된 원문 오탈자** (모두 verbatim 전사됨, 6배줌/텍스트레이어 확인):
   - Thm 4.58 증명 (2) 사슬 마지막 줄 첨자 $\bigcap_{i\in D_i}$ (→ $i\in I$이어야 함), Thm 4.59(2) 마지막 줄 $\bigcap_{i\in C_i}$ (동일) — Ex 4.60 풀이에서 역주로 언급 가치 있음.
   - Def 4.14(4) "ono-to-one correspondence" (one-to-one 오타).
   - Thm 4.57 증명 "In other owrds".
   - Cor 4.42 끝문장 마침표 위치 오류("…is a function. $x_1=x_2$, i.e. …"), Lemma 4.24(5) 증명 "Recall that (Case 3: …" 괄호 미닫힘.
   - Thm 3.28(4) "$B\cap B\subset B$" ($A\cap B$이어야 함 — 진술 자체는 여전히 참), Ex 3.74 "$\{A_n\}_{i\in\mathbb{N}}$" 첨자 불일치, Notation 4.70 셋째 불릿 여는 따옴표 미닫힘, Def 3.3/Q 1.13 따옴표 미닫힘 등 문장부호 다수.
   - Thm 3.56 진술은 $A,B,C$만 선언하나 (3)과 증명은 $D$ 사용(미선언 변수); Cor 3.65 증명이 "Theorem 3.64(iii)" 인용(3.64 항목은 (1)–(4)).
   - Thm 3.32(1) 증명이 $A \subset A\cup(A\cap B)$의 근거로 "Theorem 3.28(2)"를 인용하나 실제 근거는 3.28(1) (원문 오인용, verbatim 유지). Lemma 3.31 증명의 "Theorem 2.19(3)" 인용도 해당 단계와 정확히 맞지 않는 느슨한 인용 (verbatim 유지). Lemma 3.31은 (1)을 증명한다면서 실제로는 (2)를 증명 (verbatim 유지).
   - Thm 3.28(4)의 $B\cap B\subset B$ 오기는 진술뿐 아니라 원문 증명("(3) holds for all classes A=B")까지 일관된 오류 — EX 3.30 풀이 역주에 반영됨.
   - "Let $A$ and $B$ classes/sets" (be 누락) 계열 다수 — 전부 verbatim 유지.
9. dom/ran 표기: 원문이 수학 이탤릭이므로 전사는 이탤릭($dom\ G$, $\mathit{dom}$ 등 챕터별 혼재 — 시각적 동일). **우리 풀이에서도 이탤릭 계열로 맞출 것** (GLOSSARY의 \operatorname 표는 사용하지 않음).

## 챕터별 인벤토리 (번호 = 소스 환경 번호 = 카드 id)

### ch01.html — 1. Historical Introduction / 역사적 서론
- PDF pages 1–4, 환경 1.1–1.16, **카드 16개**, Exercise 2개: 1.2, 1.5
  - `1.1` Paradox (Russell’s paradox (a logical paradox) — p1
  - `1.2` Exercise — p1
  - `1.3` Definition (Cantor’s definition of a set) — p1
  - `1.4` Paradox (Berry’s paradox (a semantic paradox) — p1
  - `1.5` Exercise — p2
  - `1.6` Definition (Definition and Axiom) — p2
  - `1.7` Definition (Euclidean geometry) — p2
  - `1.8` Remark — p2
  - `1.9` Idea (Zermelo’s idea) — p2
  - `1.10` Axiom (Zermelo’s axiom of selection) — p3
  - `1.11` Idea (Zermelo’s idea and Russell’s paradox) — p3
  - `1.12` Remark — p3
  - `1.13` Question — p3
  - `1.14` Idea (Von Neumann’s idea) — p4
  - `1.15` Axiom (the class axiom) — p4
  - `1.16` Remark — p4

### ch02.html — 2. Sentence and Logic / 명제와 논리
- PDF pages 5–11, 환경 2.1–2.22, **카드 22개**, Exercise 5개: 2.2, 2.9, 2.16, 2.20, 2.21
  - `2.1` Definition (Sentence) — p5
  - `2.2` Exercise — p5
  - `2.3` Definition (Negation) — p5
  - `2.4` Definition (Conjunction) — p5
  - `2.5` Definition (Disjunction) — p5
  - `2.6` Definition (Implication) — p6
  - `2.7` Notation — p6
  - `2.8` Example — p6
  - `2.9` Exercise — p6
  - `2.10` Definition (The converse, inverse, contrapositive) — p6
  - `2.11` Remark — p7
  - `2.12` Notation — p7
  - `2.13` Theorem — p7
  - `2.14` Theorem — p8
  - `2.15` Remark — p9
  - `2.16` Exercise — p9
  - `2.17` Theorem (Transitive law) — p9
  - `2.18` Notation — p10
  - `2.19` Theorem — p10
  - `2.20` Exercise — p11
  - `2.21` Exercise — p11
  - `2.22` Notation — p11

### ch03.html — 3. Classes and Sets (i): The Algebra of Classes / 모임과 집합 (i): 모임의 대수
- PDF pages 11–21, 환경 3.1–3.42, **카드 42개**, Exercise 10개: 3.7, 3.10, 3.14, 3.15, 3.18, 3.22, 3.30, 3.35, 3.37, 3.39
  - `3.1` Undefined notion (Class and ∈) — p11
  - `3.2` Remark — p11
  - `3.3` Definition — p11
  - `3.4` Remark — p12
  - `3.5` Notation — p12
  - `3.6` Definition — p12
  - `3.7` Exercise — p12
  - `3.8` Remark — p12
  - `3.9` Axiom (Axiom of extent) — p12
  - `3.10` Exercise — p12
  - `3.11` Definition — p12
  - `3.12` Remark — p13
  - `3.13` Theorem — p13
  - `3.14` Exercise — p14
  - `3.15` Exercise — p14
  - `3.16` Axiom (Axiom of class construction) — p14
  - `3.17` Remark — p14
  - `3.18` Exercise — p14
  - `3.19` Definition — p14
  - `3.20` Remark — p14
  - `3.21` Definition — p14
  - `3.22` Exercise — p14
  - `3.23` Definition — p14
  - `3.24` Definition — p15
  - `3.25` Theorem — p15
  - `3.26` Definition — p15
  - `3.27` Definition — p15
  - `3.28` Theorem — p16
  - `3.29` Theorem — p16
  - `3.30` Exercise — p17
  - `3.31` Lemma — p17
  - `3.32` Theorem (Absorption Laws) — p17
  - `3.33` Theorem — p18
  - `3.34` Theorem (DeMorgan’s Laws) — p18
  - `3.35` Exercise — p19
  - `3.36` Theorem — p19
  - `3.37` Exercise — p20
  - `3.38` Theorem — p20
  - `3.39` Exercise — p21
  - `3.40` Example — p21
  - `3.41` Definition — p21
  - `3.42` Example — p21

### ch04.html — 3. Classes and Sets (ii): Ordered Pairs, Products, and Graphs / 모임과 집합 (ii): 순서쌍·곱·그래프
- PDF pages 21–27, 환경 3.43–3.65, **카드 23개**, Exercise 1개: 3.58
  - `3.43` Definition (singleton and doubleton) — p21
  - `3.44` Remark — p22
  - `3.45` Axiom (Axiom of the empty set) — p22
  - `3.46` Theorem — p22
  - `3.47` Definition — p22
  - `3.48` Remark — p22
  - `3.49` Axiom (Axiom of doubleton) — p23
  - `3.50` Remark — p23
  - `3.51` Axiom (Axiom of subset) — p23
  - `3.52` Lemma — p23
  - `3.53` Theorem — p23
  - `3.54` Theorem — p23
  - `3.55` Definition (The Cartesian product) — p24
  - `3.56` Theorem — p24
  - `3.57` Remark — p24
  - `3.58` Exercise — p25
  - `3.59` Definition — p25
  - `3.60` Definition (The inverse of a graph) — p25
  - `3.61` Definition (The composition of graphs) — p25
  - `3.62` Theorem — p25
  - `3.63` Definition — p26
  - `3.64` Theorem — p26
  - `3.65` Corollary — p27

### ch05.html — 3. Classes and Sets (iii): Indexed Families and Power Sets / 모임과 집합 (iii): 첨수족과 멱집합
- PDF pages 27–33, 환경 3.66–3.89, **카드 24개**, Exercise 3개: 3.74, 3.76, 3.89
  - `3.66` Definition (Index class and indexed family of classes (Intuitive definition) — p27
  - `3.67` Definition (Index class and indexed family of classes (Formal definition) — p27
  - `3.68` Example — p27
  - `3.69` Remark — p28
  - `3.70` Definition — p28
  - `3.71` Theorem — p28
  - `3.72` Theorem (Generalized De Morgan’s Laws) — p28
  - `3.73` Remark — p29
  - `3.74` Exercise — p30
  - `3.75` Theorem (Generalized Distributive Laws) — p30
  - `3.76` Exercise — p30
  - `3.77` Theorem — p30
  - `3.78` Definition — p31
  - `3.79` Notation — p31
  - `3.80` Remark — p32
  - `3.81` Axiom (Axiom of union) — p32
  - `3.82` Example — p32
  - `3.83` Definition (The power set) — p32
  - `3.84` Remark — p32
  - `3.85` Axiom (Axiom of power set) — p32
  - `3.86` Theorem — p32
  - `3.87` Corollary — p32
  - `3.88` Corollary — p33
  - `3.89` Exercise — p33

### ch06.html — 4. Functions (i): Definitions and Basic Properties / 함수 (i): 정의와 기본 성질
- PDF pages 33–38, 환경 4.1–4.23, **카드 23개**, Exercise 4개: 4.11, 4.12, 4.16, 4.23
  - `4.1` Definition (function (intuitive definition) — p33
  - `4.2` Definition (function (formal definition) — p33
  - `4.3` Notation — p33
  - `4.4` Remark — p34
  - `4.5` Lemma — p34
  - `4.6` Notation — p34
  - `4.7` Definition — p34
  - `4.8` Theorem — p34
  - `4.9` Corollary — p35
  - `4.10` Notation — p35
  - `4.11` Exercise — p35
  - `4.12` Exercise — p35
  - `4.13` Theorem — p35
  - `4.14` Definition (1) — p36
  - `4.15` Remark — p36
  - `4.16` Exercise — p36
  - `4.17` Example (Identity function) — p36
  - `4.18` Example (Constant function) — p37
  - `4.19` Example (Inclusion Function) — p37
  - `4.20` Example (Characteristic function (Indicator function) — p37
  - `4.21` Example (Restriction of a function) — p37
  - `4.22` Example (Extension of a function) — p37
  - `4.23` Exercise — p37

### ch07.html — 4. Functions (ii): Composition and Inverses / 함수 (ii): 합성과 역함수
- PDF pages 38–43, 환경 4.24–4.50, **카드 27개**, Exercise 9개: 4.25, 4.28, 4.29, 4.32, 4.38, 4.40, 4.41, 4.44, 4.45
  - `4.24` Lemma — p38
  - `4.25` Exercise — p38
  - `4.26` Theorem — p38
  - `4.27` Theorem — p39
  - `4.28` Exercise — p39
  - `4.29` Exercise — p39
  - `4.30` Definition — p39
  - `4.31` Lemma — p39
  - `4.32` Exercise — p40
  - `4.33` Lemma — p40
  - `4.34` Theorem — p40
  - `4.35` Theorem — p40
  - `4.36` Corollary — p41
  - `4.37` Theorem — p41
  - `4.38` Exercise — p41
  - `4.39` Theorem — p41
  - `4.40` Exercise — p41
  - `4.41` Exercise — p42
  - `4.42` Corollary — p42
  - `4.43` Corollary — p42
  - `4.44` Exercise — p42
  - `4.45` Exercise — p42
  - `4.46` Definition — p42
  - `4.47` Theorem — p42
  - `4.48` Remark — p43
  - `4.49` Theorem — p43
  - `4.50` Corollary — p43

### ch08.html — 4. Functions (iii): Images, Choice, and Products / 함수 (iii): 상·선택공리·곱
- PDF pages 43–50, 환경 4.51–4.77, **카드 27개**, Exercise 7개: 4.56, 4.60, 4.61, 4.66, 4.69, 4.71, 4.74
  - `4.51` Definition (Direct image) — p43
  - `4.52` Definition (Inverse image) — p44
  - `4.53` Notation — p44
  - `4.54` Theorem — p44
  - `4.55` Remark — p44
  - `4.56` Exercise — p44
  - `4.57` Theorem — p44
  - `4.58` Theorem — p45
  - `4.59` Theorem — p46
  - `4.60` Exercise — p47
  - `4.61` Exercise — p47
  - `4.62` Definition (Choice function) — p47
  - `4.63` Remark — p47
  - `4.64` Axiom (Axiom of choice) — p47
  - `4.65` Theorem — p47
  - `4.66` Exercise — p48
  - `4.67` Definition (Product of a family of classes) — p48
  - `4.68` Example — p48
  - `4.69` Exercise — p49
  - `4.70` Notation — p49
  - `4.71` Exercise — p49
  - `4.72` Notation — p49
  - `4.73` Theorem — p49
  - `4.74` Exercise — p50
  - `4.75` Remark — p50
  - `4.76` Axiom (Axiom of replacement) — p50
  - `4.77` Theorem — p50
