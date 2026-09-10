# 선형대수학 2 SOURCE-MAP

소스: `la2/src/` (원본은 `~/Desktop/26-2/선형대수학2/`)
- `MATH222 Syllabus (2026 Fall).pdf` — 강의계획서 (Euisung Park, Korea Univ.; 교재 Friedberg–Insel–Spence 4e; 진도: Review → 5.1 → 5.2 → 5.4 → 6.1 → 6.2 → 6.3 → 6.4 → 6.5 → 6.6)
- `Lecture 1 - Preliminaries (9월 1일 화요일).pdf` — 24장 슬라이드 (영문)
- `Lecture 2 - Section 5.1  (9월 3일 목요일).pdf` — 14장 슬라이드 (영문)
- `Lecture 3 - Section 5.1 (9월 8일 화요일).pdf` — 17장 슬라이드 (영문, 9/8)
- `Lecture 4 - Section 5.2 (9월 10일 목요일).pdf` — 16장 슬라이드 (영문, 9/10)
- `Lecture 5 - Section 5.2 (9월 15일 화요일).pdf` — 16장 슬라이드 (영문, 9/15 강의분 — 9/10에 선게시; 원본 파일명 끝의 " (1)" 제거하고 복사)
- `5.1 Linear Algebra Solution.pdf` — §5.1 추천 연습문제(Friedberg) 풀이 9쪽 (문항: 1(a)–(k), 3(b)(d), 4(e)(g)(j), 11, 14, 15(a), 16(a), 17)
- `5.2 Linear Algebra Solution.pdf` — §5.2 추천 연습문제 풀이 6쪽 (문항: 1(a)–(h), 2(a)(d)(e), 3(a)(d)(e)(f), 7, 8, 9(a), 10, 11, 12, 18, 19)

**소스가 영문 슬라이드** → en-formal = verbatim 전사, ko-formal = 번역. 컨벤션은 `analysis2/`와 동일(analysis2/ch01.html 규약 주석) + 아래 la2 고유 규칙.
**슬라이드 PDF는 텍스트 추출이 불가**(한글 워드프로세서 수식이 글리프 없는 문자로 나옴) → 반드시 Read 도구로 페이지를 **시각적으로** 읽어 전사한다.
**학기 중 갱신되는 자료** — 강의마다 슬라이드 1개가 추가된다. 단원 = 교재 절(section). 새 강의가 오면 해당 단원 파일 끝(연습문제 섹션 앞)에 카드를 이어 붙이고 아래 인벤토리를 갱신한다.

## la2 고유 규칙 (analysis2 규약에 추가)

1. **카드 id는 자체 순번** `c{단원}-{순번}`(슬라이드 등장 순, 앵커·인벤토리용). **배지는 강의 슬라이드의 번호를 그대로 따른다(2026-09-10 사용자 지시 "강의 자료에 있는 번호에 맞춰서")**: 슬라이드가 번호를 붙인 항목은 `TYPE {원문 번호}` (Example 1 → `EXAM 1`, Theorem 5.1 → `THM 5.1`, Definition 3 → `DEF 3`, Remark 1 → `REM 1`), 번호 없는 항목(Definition :, Remark :, Recall, Question, 번호 없는 Example)은 **유형 배지만** (`DEF`, `REM`, `RECALL`, `Q`, `EXAM`, `COR`, `LEM`). 따라서 `src-ref` pill은 연습문제(Friedberg §5.1 #3 …)에만 남는다. 본문에서 번호 없는 카드를 인용할 때는 자체 번호 대신 `<a href="#c2-10">주의 「제목」</a>`처럼 제목 링크로 쓴다. 순서는 슬라이드 등장 순 그대로(예: ch02는 Example 5가 Example 4보다 앞). 아래 인벤토리 표의 배지 열은 새 규칙으로 갱신됨.
2. rem-card 배지 변형: `REM`(Remark), `RECALL`(Recall), `Q`(Question/Answer, 대각화 문제 Q1·Q2). 모두 `.rem-num` 클래스.
3. thm-card 배지 변형: `THM`, `COR`(Corollary). 라이프니츠 공식은 `THM`.
4. **연습문제(Friedberg 추천문제)**는 각 단원 끝 `<div class="section-title"><h2>연습문제 · Exercises (Friedberg §5.1)</h2></div>` 아래 ex-card로. id는 `e{단원}-{교재 문항번호}` (예: `e2-3`), 배지 `EX 5.1-3`, src-ref `Friedberg §5.1 #3 (b), (d)`. 하위 문항은 교재 글자(a),(b)… 그대로 `<strong>(b)</strong>` 라벨로.
   - **문제 진술은 교재 문장을 그대로 베끼지 않고 우리 말로 다시 서술**한다(수학적 데이터 — 행렬·사상·공간 — 는 정확히 동일). 풀이도 우리가 새로 쓴다(공개된 풀이 PDF는 기준값·검산용).
   - ex-card는 빌드 단계에서 풀이 없이 `PROOF-KO`/`PROOF-EN` 주석 마커만 둔다(la/ch01.html pr-card 형태).
5. 슬라이드의 "Question"이 실제 풀 문제(ch01 차원 질문)면 ex-card(`EX 1.n`)로 두고 마커를 둔다.
6. 원문 증명이 있는 정리(Theorem 5.2)는 en verbatim 증명 토글(■ → `<div class="qed">□</div>`) + ko `[번역 예정]` 토글.
7. note-card id `note{단원 2자리}-{순번}` (예: `note02-3`). 목차 제외.
8. 슬라이드 1(제목 슬라이드)은 카드로 만들지 않는다. "Studying Contents"는 SOURCE-MAP에만 남긴다.
9. 색·밑줄 강조는 옮기지 않는다. 슬라이드 내 박스(det(A)≠0 ⇔ invertible, 3×3 전개식)는 `div.math-display`로.
10. 문자 표기: 슬라이드의 칼리그래피 $\mathcal{B}$는 `\mathcal{B}`, 풀이 PDF의 $\beta$는 `\beta`. Lecture 2가 체를 $\mathbb{F}$(blackboard)로 쓴 슬라이드(8–14)는 `\mathbb{F}`, $F$(이탤릭)로 쓴 슬라이드(2–7)는 `F` — 원문 그대로.

## 전체 구조 (2026-09-10 현재)

| 단원 | 제목 | 소스 | 카드 | note | 연습문제 카드 |
|---|---|---|---|---|---|
| ch01 | 예비 사항: 선형대수학 I 복습 | Lecture 1 (24장) | 29 (EX 1) | 4 | — |
| ch02 | 5.1 고유값과 고유벡터 | Lecture 2 (14장) + Lecture 3 (17장) + §5.1 풀이 | 33 | 3 | 8 |
| ch03 | 5.2 대각화가능성 | Lecture 4 (16장) + Lecture 5 (16장) + §5.2 풀이 | 26 | 1 | 11 |
| 계 | | | **88** | **8** | **19** (+ ch01 EX 1 = 풀이 대상 **22**, THM 2.25·THM 3.21 자체 증명 포함) |

## ERRATA / 역주 후보 (en verbatim 유지, ko는 바른 뜻·풀이에서 역주)

1. L1 p8 Example: $P_n(F)$의 집합 표기에 `n ≥ 0` 조건이 $P(F)$ 정의에서 복사됨(차수 $\le n$ 고정이므로 불필요·부적절) — verbatim.
2. L1 p11 Example(3): "we define the trace of $A$, denoted by $tr(M)$, is defined to be" — $M$↔$A$ 불일치 + 문장 중복 — verbatim, ko는 $\operatorname{tr}(A)$.
3. L1 p19 Theorem 2.3: "the followings are true" — verbatim.
4. L1 p21 Remark: 문제 없음. L1 p24 Corollary: "det(A−tI) = (−1)ⁿtⁿ + lower terms" — 정리 진술로 전사.
5. L2 p9 Definition 1: "there exist an ordered basis" (exists) — verbatim.
6. L2 p7 Example: "reflection along the line y = 2x" (p8에서는 "about the line") — 원문 표기 각각 유지.
7. L2 p14 Theorem 5.2 증명: "nonzer vector" — verbatim.
8. §5.1 풀이 PDF #1(b): 풀이가 "Theorem 5.4"를 인용(교재 4e에서 해당 내용은 Thm 5.2 및 그 따름정리) — 우리 풀이는 정리 번호 대신 내용을 명시.
9. §5.2 풀이 PDF #1(f)·(g): "See Theorem 5.11" — 4e 기준 (f)의 판정 정리는 Thm 5.9(분해 + 중복도 = dim $E_\lambda$). 우리 풀이는 내용을 명시하고 필요 시 4e 번호를 괄호로.
10. §5.2 풀이 PDF #2(e): 특성다항식 $(x-1)(-x^2-1)$ — 부호 관례상 $-(t-1)(t^2+1)$; 기준값 GROUND-TRUTH 참조.
11. §5.1 풀이 PDF #4(e): $[T]_\gamma$의 기저 $\gamma=\{x^2,x,1\}$ 순서 — 우리 풀이는 표준순서기저 $\{1,x,x^2\}$를 써도 됨(답의 기저는 유일하지 않음, 고유값 0,2,4 동일).
13. L2 p5 Remark (4) 전개식: `a_1Au_1 + \cdots a_nAu_n = a_1\lambda_1u_1 + \cdots a_n\lambda_nu_n` — 마지막 항 앞 `+` 누락(두 군데) — verbatim, ko는 `+` 넣어 번역.
14. L2 p7 Example (5): `[T]_\beta = [[u]_\beta \; [-v]_\beta]` — 엄밀히는 `[[T(u)]_\beta \; [T(v)]_\beta]`(값은 같음) — verbatim.
15. L2 p5: 산문은 $\mathcal{B}$, 첨자는 $\beta$로 혼용 인쇄 — 원문 그대로 전사. L2 p8 Example: 기저를 $\{v_1,v_2\}$로 두고 행렬은 $[T]_{\mathcal{B}}$로 씀($\mathcal{B}$ 미도입) — verbatim.
16. L2 p14 Theorem 5.2 증명의 영벡터는 이중선 $\mathbb{O}$로 인쇄 — `\mathbb{O}`로 전사.
12. **§5.2 풀이 PDF #3(d) 오류(기준값으로 확정)**: $[T]_\beta=\begin{pmatrix}1&0&0\\1&1&1\\1&1&1\end{pmatrix}$의 $E_1$ 기저를 $(1,0,-1)$로 적었으나 $A(1,0,-1)^t=(1,0,0)^t\neq(1,0,-1)^t$ — 고유벡터가 아님. 올바른 $E_1$ 기저는 $(-1,1,1)$ (다항식 $-1+x+x^2$). 따라서 게시된 $Q$의 2열도 틀림. 우리 풀이는 GROUND-TRUTH 값을 쓴다. 나머지 기준값(§5.1 #3·#4·#17, §5.2 #2·#3(a)(e)(f)·#7)은 게시 풀이와 일치.
17. **L3 p7 Example 4 (1)–(3) 부호 오류(220 dpi 확인)**: 인쇄된 것은 $A-tI_2=\begin{pmatrix}1-t&-3\\-4&2-t\end{pmatrix}$, $A+2I_2=\begin{pmatrix}3&-3\\-4&4\end{pmatrix}$(→ $x-y=0$, $(1,1)$), $A-5I_2=\begin{pmatrix}-4&-3\\-4&-3\end{pmatrix}$(→ $4x+3y=0$, $(3,-4)$). 올바른 값은 $A-tI_2=\begin{pmatrix}1-t&3\\4&2-t\end{pmatrix}$, $A+2I_2=\begin{pmatrix}3&3\\4&4\end{pmatrix}$(→ $x+y=0$, $v_1=(1,-1)$), $A-5I_2=\begin{pmatrix}-4&3\\4&-3\end{pmatrix}$(→ $4x-3y=0$, $v_2=(3,4)$). 고유값 $-2,5$와 p8의 (4)(5)는 옳다. en은 verbatim 전사 + 말미 Note 로 정정, ko는 번역 단계에서 바른 값으로.
18. L3 p11 Remark Step 3: "$v$ is an eigenvalue corresponding to $\lambda$ … $\phi_{\mathcal{B}}(v)$ is an eigenvalue corresponding to $\lambda$" — 두 곳 모두 eigenvector 여야 한다 — en verbatim, ko는 고유벡터로 번역.
19. L3 p6 Theorem 5.3: 슬라이드에 "Proof : (1)" 만 있고 본문이 공란(수업 중 구두 증명) → 원문 증명 전사 불가. c2-25 에 `PROOF-KO`/`PROOF-EN` 마커만 두고 우리 증명을 나중에 작성한다(풀이 대상 21건에 포함).
20. L3 p4 Remark: 마지막 행렬식 줄에서 가운데 두 개의 "det"만 이탤릭으로 인쇄됨(`det Q × det(...) × det Q⁻¹`) — 전사에서는 모두 `\det`으로 통일.
21. **L4 p5 Example(번호 없음) 전개식 부호 오류(기준값 확정)**: 인쇄 $-(t^3-5t^2+34t-80)$ → 옳은 전개는 $-(t^3-5t^2-34t+80)$. 인수분해 $-(t-8)(t-2)(t+5)$와 고유값 $-5,2,8$은 옳다. en verbatim + Note, ko는 바른 식.
22. **L4 p14 Example 4 (3)**: 결론 줄 "$E_{\lambda_1} = \{c(0,1,0)+d(-1,0,1)\}$"의 첨자는 $E_{\lambda_2}$ 여야 함($\lambda_2=3$, 차원 2). en verbatim + Note, ko는 $E_{\lambda_2}$. (L5 p3 재수록에도 동일)
23. **L4 p15 Remark**: Example 4 항목의 결론 "In this case, T fails to be diagonalizable."는 "T is diagonalizable" 이어야 함(Example 4는 대각화가능 — 각 고유공간 차원 = 중복도). en verbatim + Note, ko는 바른 뜻. (L5 p4 재수록에도 동일; L5 p4 마지막 줄만 "This is indeed true, as we now show.")
24. L5 p8 Theorem 5.9: "a linear operator on an n-dimensional vector space V whose characteristic polynomial of T splits" — 어법 verbatim, ko는 "특성다항식이 분해되는 선형연산자".
25. L5 p12 Example 5: $M_{3\times 3}(R)$의 $R$이 일반 이탤릭으로 인쇄(L4 p14·L5 p14의 집합기호 안 $\in R^3$도 동일) — 수식편집기 글꼴 문제로 판단해 모두 `\mathbb{R}`로 정규화(검증 단계 결정).
26. L5 p10 "◎ Test for diagonalization": 슬라이드에 증명 없음 → c3-21에 자체 증명(정리 5.9 + $\dim E_\lambda = n - \operatorname{rank}(T-\lambda I)$). ◎ 기호는 옮기지 않음.
27. L5 p5 Lemma 진술 끝이 "then $v_1 = v_2 = \cdots = O_V$"로 $= v_k$가 빠짐 — p6 상단의 온전한 재수록판("$\cdots = v_k = O_V$")을 c3-18에 전사. L4 p7 (2) "Thus the property that a polynomial $f(t)\in P(F)$ depends heavily on the field $F$."는 "splits" 누락 비문 — en verbatim, ko는 바른 뜻. L4 p11 Theorem 5.7 증명은 상계만 다룸(하계 $1 \le \dim E_\lambda$는 고유벡터 존재로 자명) — verbatim.
28. L5 p11 Step 4 마지막 도식 "$Bu_i = \lambda u_i = [\lambda v_i]_\alpha$ … $T(v_i) = \lambda v_i$": $\lambda$에 첨자가 없음 — $u_i$마다 고유값이 다를 수 있으므로 $\lambda_i$가 정확. en·ko 모두 원문대로.
29. L4 p14 Example 4: (2)는 $E_{\lambda_1} = N(T-\lambda_1 I)$(연산자), (3)은 $E_{\lambda_2} = N([T]_\beta - \lambda_2 I)$(행렬)로 표기 혼용 — 값에 영향 없음, verbatim.

## 챕터별 인벤토리 (카드 id = 배지 번호; 슬라이드 페이지 = PDF 페이지)

### ch01.html — 예비 사항: 선형대수학 I 복습 / Preliminaries: Review of Linear Algebra I
Lecture 1, 24장. 카드 29 (DEF 12, THM 8, COR 1, EXAM 4, REM 3, EX 1) + note 4.

| id | 유형·배지 | 슬라이드 | 내용 | src-ref |
|---|---|---|---|---|
| note01-1 | NOTE | p2 | Review of Linear Algebra I — 이번 학기 Ch.5·6, 복습 항목 6개 목록 | |
| c1-1 | Q | p3 | Question/Answer: 선형대수학의 연구 대상 = 벡터공간과 선형변환 | |
| c1-2 | DEF | p4 | Definition of Field (1)–(6) + "Why do we need…" + "This semester… ℝ, ℂ" | |
| note01-2 | NOTE | p5 | Definition of Vector Space 도입: 벡터공간의 예 4개(ℝⁿ, Pₙ(F), M_{m×n}(F), C[0,1]) + "same algebraic rules" | |
| c1-3 | DEF | p6 | Vector space (VS 1)–(VS 8) | |
| c1-4 | DEF | p7 상 | Definition of Subspace | |
| c1-5 | THM 1.3 | p7 하 | Theorem 1.3: 부분공간 판정 (i)(ii)(iii) | Theorem 1.3 |
| c1-6 | EXAM | p8 | P(F), Pₙ(F) 정의, Pₙ(F)는 P(F)의 부분공간 | |
| c1-7 | EXAM | p9–11 | 행렬 용어(대각성분·행·열·정사각행렬), (1) 대각행렬 Dₙ, (2) 대칭행렬 정의·부분공간, (3) 대각합 tr, {tr=0} 부분공간 | |
| c1-8 | THM 1.4 | p12 | Theorem 1.4: 부분공간의 교집합 | Theorem 1.4 |
| c1-9 | DEF | p13 | Linear Combination (1) 유한 S, (2) 비공 S; span(S) | |
| c1-10 | THM 1.5 | p14 | Theorem 1.5: span(S) 부분공간·최소성 | Theorem 1.5 |
| c1-11 | DEF | p15 상 | Linearly dependent 정의 | |
| c1-12 | THM 1.7 | p15 하 | Theorem 1.7: S∪{v} 일차종속 ⇔ v∈span(S) | Theorem 1.7 |
| c1-13 | DEF | p16 상 | Basis 정의 | |
| c1-14 | EXAM | p16 중 | Fⁿ의 표준기저 | |
| c1-15 | EXAM | p16 하 | P(F)의 기저 {1,x,x²,…} | |
| c1-16 | THM | p17 상 | Theorem: 유한기저 ⇒ 모든 기저 n개 | |
| c1-17 | DEF | p17 중 | finite dimensional, dim(V), infinite-dimensional | |
| c1-18 | EX | p17 하 | Question (1) ℝⁿ/ℝ dim n (2) ℂⁿ/ℂ dim n (3) ℂⁿ/ℝ dim 2n — **마커** | |
| c1-19 | DEF | p18 | Linear transformation (1), N(T)·R(T) (2) | |
| c1-20 | DEF | p19 상 | nullity(T), rank(T) | |
| c1-21 | THM 2.3 | p19 하 | Theorem 2.3 (Dimension Theorem) (i)(ii) | Theorem 2.3 |
| c1-22 | DEF | p20 | Definition and Remark: 행렬표현 [T]_B^γ (1)(2)(3) | |
| c1-23 | THM | p21 상 | Theorem: [T(v)]_γ = [T]_B^γ [v]_B | |
| c1-24 | REM | p21 하 | Remark: 선형대수학 II의 출발점, Ch.5의 근본 질문 | |
| note01-3 | NOTE | p22 상 | Determinants 도입: det(A)≠0 ⇔ A invertible (박스) | |
| c1-25 | DEF 1 | p22 중 | Definition 1: 2×2 행렬식 | Definition 1 |
| c1-26 | DEF 2 | p22 하–p23 상 | Definition 2: 3×3 행렬식(여인수 전개 2줄) + 박스 6항 전개식 + "This formula says:" 4줄 | Definition 2 |
| note01-4 | NOTE | p23 중 | "In Chapter 4, we learned several fundamental properties… following formula." | |
| c1-27 | THM | p23 하 | Leibniz Formula det(A)=Σ sgn(σ)Π a_{i,σ(i)} | |
| c1-28 | COR | p24 상 | Corollary: det(A−tI) = (−1)ⁿtⁿ + lower terms, 차수 n | |
| c1-29 | REM | p24 하 | Final Remark: 행렬식에서 고유값으로 | |

### ch02.html — 5.1 고유값과 고유벡터 / §5.1 Eigenvalues and Eigenvectors
Lecture 2, 14장 + Lecture 3, 17장. 카드 33 (DEF 6, THM 4, EXAM 10, REM 13) + note 3 + 연습문제 8.
섹션 구분: `제5장 대각화 · Chapter 5. Diagonalization`(L2 p2–7) → `§5.1 고유값과 고유벡터`(L2 p8–14 + L3 p2–17) → `연습문제 · Exercises (Friedberg §5.1)`.

| id | 유형·배지 | 슬라이드 | 내용 | src-ref |
|---|---|---|---|---|
| c2-1 | RECALL | p2 | Recall: 선형연산자, (1) 좌표벡터 [T(v_i)]_B, 행렬표현 [T]_B | |
| note02-1 | NOTE | p3 상 | "This chapter is devoted to the so-called diagonalization problem…" | |
| c2-2 | REM | p3–5 | Remark (1)–(4): L_A, R(L_A)=span{Au_i}, L_A(e_i)=v_i, 대각행렬일 때, 일반화 [L_A]_B 대각 | |
| c2-3 | Q | p6 상 | 대각화 문제 도입 + Q1, Q2 | |
| c2-4 | REM | p6 하 | Remark: [T]_B 대각이면 T(v)=Σ b_i a_ii v_i, 실용적 문제 | |
| c2-5 | EXAM | p7 | Example: reflection along y=2x (1)–(5), [T]_β = diag(1,−1) | |
| c2-6 | RECALL | p8 상 | Section 5.1 Recall: 목표 — T(v_i)=c_i v_i | |
| c2-7 | EXAM | p8 하 | Example: reflection about y=2x, v₁=(1,2), v₂=(−2,1) | |
| c2-8 | DEF 1 | p9 상 | Definition 1: T diagonalizable | Definition 1 |
| c2-9 | DEF 2 | p9 중 | Definition 2: A diagonalizable | Definition 2 |
| c2-10 | REM | p9 하 | Remark: A[v₁…vₙ]=[v₁…vₙ]D, Q 가역, A=QDQ⁻¹ | |
| c2-11 | REM | p10 | when T diagonalizable / how to obtain B; (1)(2) | |
| note02-2 | NOTE | p11 상 | "In the preceding slide… motivate the following definitions." | |
| c2-12 | DEF 3 | p11 중 | Definition 3: eigenvector/eigenvalue of T | Definition 3 |
| c2-13 | DEF 4 | p11 하 | Definition 4: eigenvector/eigenvalue of A + ※ Terminologies | Definition 4 |
| c2-14 | THM 5.1 | p12 상 | Theorem 5.1: diagonalizable ⇔ eigenvector basis; D_jj | Theorem 5.1 |
| c2-15 | REM | p12 하 | Remark: Theorem 5.1 shows … | |
| c2-16 | EXAM 1 | p13 상 | Example 1: A=(1 3;4 2), v₁=(1,−1) λ=−2, v₂=(3,4) λ=5, [L_A]_B=diag(−2,5) | Example 1 |
| c2-17 | EXAM 2 | p13 하 | Example 2: rotation π/2, 고유벡터 없음 | Example 2 |
| note02-3 | NOTE | p14 상 | Next Problem: how to find eigenvectors/eigenvalues? | |
| c2-18 | THM 5.2 | p14 중 | Theorem 5.2 + **Proof** (verbatim 토글) | Theorem 5.2 |
| c2-19 | DEF | p14 하 | Definition: characteristic polynomial f(t)=det(A−tIₙ) | |
| c2-20 | REM | p14 하 | Remark: eigenvalues = zeros of det(A−tIₙ) | |
| c2-21 | RECALL | L3 p2 | Recall (1) 고유벡터·고유값 (2) 고유벡터 기저 ⇒ [T]_B 대각, diagonalizable (3) A diagonalizable ⇔ L_A diagonalizable | |
| c2-22 | DEF | L3 p4 상 | Definition: 선형변환 T의 특성다항식 f(t) := det(A−tIₙ), A = [T]_B | |
| c2-23 | REM | L3 p4 하 | Remark: [T]_γ = Q[T]_B Q⁻¹, det로 기저 무관 확인, det(T−tI) 표기 | |
| c2-24 | EXAM 5 | L3 p5 | Example 5: T(f)=f+(x+1)f′ on P₂(ℝ), [T]_B, 특성다항식, λ=1,2,3 | Example 5 |
| c2-25 | THM 5.3 | L3 p6 상 | Theorem 5.3 (1) deg n·최고차계수 (−1)ⁿ (2) 서로 다른 고유값 최대 n개 — **마커**(슬라이드 증명 공란) | Theorem 5.3 |
| c2-26 | THM 5.4 | L3 p6 하 | Theorem 5.4: v가 λ의 고유벡터 ⇔ v ∈ N(T−λI) | Theorem 5.4 |
| c2-27 | EXAM 4 | L3 p7–8 | Example 4: A=(1 3;4 2) (1)–(5) 고유값 −2,5, v₁,v₂, A=QDQ⁻¹ — p7 부호 오류(ERRATA 17) + en 말미 Note | Example 4 |
| c2-28 | EXAM 6 | L3 p9–10 | Example 6: A=(1 1;4 1) 모든 고유벡터, λ=3,−1, A=QDQ⁻¹ | Example 6 |
| c2-29 | REM | L3 p11 | Remark: 고유벡터 찾는 절차 Step 1–3, φ_B 가환도식(ko·en 동일 배치) — ERRATA 18 | |
| c2-30 | EXAM 7 | L3 p12–15 | Example 7: [T]_B의 λ₁=1, λ₂=2, λ₃=3 고유벡터와 φ_B⁻¹, 기저 γ={1, x+1, x²+2x+1}, [T]_γ 대각 | Example 7 |
| c2-31 | REM | L3 p16 | Remark: W = span{v} 위의 T, CASE 1–5 (λ>1, =1, 0<λ<1, =0, <0) + 인라인 SVG 그림(ko·en 동일) | |
| c2-32 | EXAM A | L3 p17 상 | Example A: x축에 대한 반사, e₁·e₂가 고유벡터 | Example A |
| c2-33 | EXAM B | L3 p17 하 | Example B: 각 θ(0<θ<π) 회전, [T]_{e₁,e₂}, t²−(2cos θ)t+1 실근 없음 | Example B |

L3 p1 제목·Studying Contents, L3 p3(L2 p14 재수록)은 카드 없음.

연습문제 (Friedberg §5.1 추천문제; 진술은 재서술, 풀이는 자체 작성):

| id | 배지 | 문항 | 유형 | 기준값(공개 풀이) |
|---|---|---|---|---|
| e2-1 | EX 5.1-1 | #1 (a)–(k) 참·거짓 | 풀이 | F T T F F F F T T F F |
| e2-3 | EX 5.1-3 | #3 (b),(d): 고유값·고유벡터·기저·Q,D | 풀이 | (b) λ=1,2,3; (d) λ=0,1,1 — GROUND-TRUTH |
| e2-4 | EX 5.1-4 | #4 (e),(g),(j): 연산자의 고유값·대각화 기저 | 풀이 | (e) 0,2,4; (g) −1,1,2,3; (j) −1,1,1,5 |
| e2-11 | EX 5.1-11 | #11 (a)(b)(c) 스칼라행렬 | 증명 | |
| e2-14 | EX 5.1-14 | #14 A, Aᵗ 특성다항식 동일 | 증명 | |
| e2-15 | EX 5.1-15 | #15 (a) Tᵐ의 고유벡터 | 증명 | |
| e2-16 | EX 5.1-16 | #16 (a) 닮은 행렬의 대각합 (힌트: tr(AB)=tr(BA)) | 증명 | |
| e2-17 | EX 5.1-17 | #17 (a)–(d) 전치 연산자 T(A)=Aᵗ | 풀이 | ±1; 대칭/반대칭; n=2 기저 4개; 일반 n: E_ii, E_ij+E_ji, E_ij−E_ji |

### ch03.html — 5.2 대각화가능성 / §5.2 Diagonalizability
Lecture 4, 16장 + Lecture 5, 16장. 카드 26 (RECALL 1, THM 7(LEM 1·COR 1 포함), DEF 2, REM 7, EXAM 9) + note 1 + 연습문제 11.
섹션 구분: `§5.2 Diagonalizability · 대각화가능성`(L4 p2–16 + L5 p5–16) → `연습문제 · Exercises (Friedberg §5.2)`. L4 p1·L5 p1 제목, L5 p2–4(L4 p13–15 재수록: Example 4 + Remark; 마지막 줄만 "as we now show"), L4 p4·L5 p6 하단 Theorem 5.5 박스, L5 p5 상·p7 상 Theorem 5.8 재진술, L5 p9 상 Theorem 5.9 재진술은 카드 없음. note03-1(강의 예정 안내)은 삭제.

| id | 유형·배지 | 슬라이드 | 내용 | src-ref |
|---|---|---|---|---|
| c3-1 | RECALL | L4 p2 | 대각화가능 행렬의 정의 복습 + "Want to find :" (i) 판정법 (ii) 고유벡터 기저를 찾는 방법 | — |
| c3-2 | THM 5.5 | L4 p3 | 서로 다른 고유값에 대응하는 고유벡터들은 일차독립 + Proof(k에 대한 귀납법) 토글 | Theorem 5.5 |
| c3-3 | COR | L4 p4 | 서로 다른 고유값이 n개면 T는 대각화가능 + Proof 토글 | — |
| c3-4 | EXAM 1 | L4 p5 상 | $A=\begin{pmatrix}1&1\\1&1\end{pmatrix}$, $\det(A-tI_2)=t(t-2)$, 고유값 $0,2$ → 대각화가능 | Example 1 |
| c3-5 | EXAM | L4 p5 하 | $A=\begin{pmatrix}1&2&3\\2&3&1\\12&1&1\end{pmatrix}$, $-(t-8)(t-2)(t+5)$, 고유값 $-5,2,8$ → 대각화가능 | — |
| c3-6 | REM | L4 p6 | 대각화가능 ⇒ 서로 다른 고유값 n개? Answer : No. 반례 $A=I_n$, $\det(A-tI_n)=(1-t)^n$ | — |
| c3-7 | DEF | L4 p7 상 | $f(t)\in P(F)$가 $F$ 위에서 분해된다(splits over $F$)의 정의 | — |
| c3-8 | REM | L4 p7 하 | (1) $t^2-1$은 ℝ 위에서 분해 (2) $t^3-2t^2+t-2$는 ℝ에서 분해 안 됨·ℂ에서 분해 (3) $f(t):=\det(T-t\,\mathrm{Id}_V)$가 $F$ 위에서 분해될 때 "splits"라 함 | — |
| c3-9 | THM 5.6 | L4 p8 | T가 대각화가능이면 특성다항식이 분해된다 + Proof 토글(대각행렬 $D=[T]_\beta$) | Theorem 5.6 |
| c3-10 | REM | L4 p9 | 사상 $\mathcal{L}(V)\to P_n(F)$, (1)–(4)와 세 조건(n개의 서로 다른 영점 / 대각화가능 / 분해)의 YES⇓ ⇑NO 도식 | — |
| c3-11 | DEF | L4 p10 상 | (1) (대수적) 중복도 (2) 고유공간 $E_\lambda:=\{x\in V\mid T(x)=\lambda x\}$ + 행렬의 고유공간은 $L_A$의 것으로 정의 | — |
| c3-12 | REM | L4 p10 하 | (1) $E_\lambda=N(T-\lambda I_V)$는 부분공간 (2) $O_V$와 모든 고유벡터로 구성 (3) $\dim E_\lambda$ = 일차독립인 고유벡터의 최대 개수 | — |
| c3-13 | THM 5.7 | L4 p11 | $1\le\dim E_\lambda\le m$ + Proof 토글(블록행렬 $\begin{pmatrix}\lambda I_p&B\\O&C\end{pmatrix}$, $f(t)=(\lambda-t)^p g(t)$) | Theorem 5.7 |
| c3-14 | EXAM 2 | L4 p12 상 | $A=\begin{pmatrix}3&1&0\\0&3&4\\0&0&4\end{pmatrix}$, $f(t)=-(t-3)^2(t-4)$, 중복도 2와 1 | Example 2 |
| c3-15 | EXAM 3 | L4 p12 하 | $T:P_2(\mathbb{R})\to P_2(\mathbb{R})$, $f(t)\mapsto f'(t)$, $[T]_\beta$, $-t^3$, $E_0$ = 상수다항식 공간 → 대각화 불가 | Example 3 |
| c3-16 | EXAM 4 | L4 p13–15 상 | Example 4 (1)–(4): $[T]_\beta=\begin{pmatrix}4&0&1\\2&3&2\\1&0&4\end{pmatrix}$, $-(t-5)(t-3)^2$, $E_{\lambda_1}$ 기저 $(1,2,1)$, $E_{\lambda_2}$ 기저 $(0,1,0),(-1,0,1)$, 고유벡터 기저 → 대각화가능 | Example 4 |
| c3-17 | REM | L4 p15 하 | Example 3·Example 4에서의 (i)(ii) 비교와 Theorem 5.8 예고 | — |
| note03-2 | NOTE | L5 p5 중 | "To prove Theorem 5.8, we need the following lemma." 한 문장 (목차 제외) | — |
| c3-18 | LEM | L5 p5 하 – p6 | Lemma: $v_i \in E_{\lambda_i}$이고 $v_1+\cdots+v_k = O_V$이면 모두 $O_V$ + 증명(p6, Theorem 5.5 이용한 귀류법) | — |
| c3-19 | THM 5.8 | L5 p7 (진술 재수록: L4 p16 · L5 p5 상 · L5 p7 상) | Theorem 5.8: 서로 다른 고유공간의 유한 일차독립 부분집합들의 합집합은 일차독립 + 증명(이중합) | Theorem 5.8 |
| c3-20 | THM 5.9 | L5 p8 – p9 | Theorem 5.9 (1)(2) + 증명 ((⇒) p8, (⇐)·(2) p9) | Theorem 5.9 |
| c3-21 | THM | L5 p10 상 | Test for diagonalization: (i) 특성다항식이 분해된다, (ii) 중복도 $= n - \operatorname{rank}(T-\lambda I)$ — 슬라이드에 증명 없음, 마커만 | — |
| c3-22 | REM 1 | L5 p10 중 | Remark 1: 고유공간 순서기저들의 합집합 $\beta$, $[T]_\beta$는 대각행렬 | Remark 1 |
| c3-23 | REM | L5 p10 하 – p11 | Step 1. – Step 4. 대각화 절차(Step 4의 좌표사상 $[\ ]_\alpha : V \to F^n$과 ⇒ 두 줄 포함) | — |
| c3-24 | EXAM 5 | L5 p12 | Example 5: $A = \begin{pmatrix}3&1&0\\0&3&0\\0&0&4\end{pmatrix}$ (1)–(3), 대각화가능하지 않음 | Example 5 |
| c3-25 | EXAM 6 | L5 p13 – p15 | Example 6 (1)–(6): $T(f(x)) = f(1)+f'(0)x+(f'(0)+f''(0))x^2$, $B=[T]_\alpha$, $E_{\lambda_1}$·$E_{\lambda_2}$·$\gamma$·$\beta$·$[T]_\beta$ | Example 6 |
| c3-26 | EXAM 7 | L5 p16 | Example 7: $A = \begin{pmatrix}0&-2\\1&3\end{pmatrix}$ (1)–(4), $A^n$ 닫힌 식 | Example 7 |

연습문제 (Friedberg §5.2 추천문제; 진술은 재서술, 풀이는 자체 작성):

| id | 배지 | 문항 | 유형 | 기준값(공개 풀이) |
|---|---|---|---|---|
| e3-1 | EX 5.2-1 | #1 (a)–(h) 참·거짓 | 풀이 | F F F T T F T T |
| e3-2 | EX 5.2-2 | #2 (a),(d),(e) 행렬의 대각화가능성 판정, Q·D | 풀이 | (a) 불가; (d) λ=3,3,−1 가능; (e) 분해 안 됨(ℝ) 불가 |
| e3-3 | EX 5.2-3 | #3 (a),(d),(e),(f) 연산자의 대각화가능성 | 풀이 | (a) 불가(λ=0만, dim E₀=1); (d) 0,1,2 가능; (e) 1∓i 가능(ℂ); (f) 1,1,1,−1 가능 |
| e3-7 | EX 5.2-7 | #7 A=(1 4;2 3), Aⁿ | 풀이 | λ=5,−1 — GROUND-TRUTH |
| e3-8 | EX 5.2-8 | #8 두 고유값, dim E_λ₁=n−1 ⇒ 대각화가능 | 증명 | |
| e3-9 | EX 5.2-9 | #9 (a) [T]_β 상삼각 ⇒ 특성다항식 분해 | 증명 | |
| e3-10 | EX 5.2-10 | #10 상삼각 [T]_β의 대각성분 = λ_i (m_i회) | 증명 | |
| e3-11 | EX 5.2-11 | #11 (a) tr(A)=Σm_iλ_i (b) det(A)=Πλ_i^{m_i} | 증명 | |
| e3-12 | EX 5.2-12 | #12 (a) E_λ(T)=E_{λ⁻¹}(T⁻¹) (b) T 대각화가능 ⇒ T⁻¹ 대각화가능 | 증명 | |
| e3-18 | EX 5.2-18 | #18 (a) 동시 대각화가능 연산자는 교환 (b) 행렬 | 증명 | 정의(#17)를 진술에 포함 |
| e3-19 | EX 5.2-19 | #19 T 대각화가능 ⇒ T, Tᵐ 동시 대각화가능 | 증명 | |
