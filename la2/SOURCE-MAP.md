# 선형대수학 2 SOURCE-MAP

소스: `la2/src/` (원본은 `~/Desktop/26-2/선형대수학2/`)
- `MATH222 Syllabus (2026 Fall).pdf` — 강의계획서 (Euisung Park, Korea Univ.; 교재 Friedberg–Insel–Spence 4e; 진도: Review → 5.1 → 5.2 → 5.4 → 6.1 → 6.2 → 6.3 → 6.4 → 6.5 → 6.6)
- `Lecture 1 - Preliminaries (9월 1일 화요일).pdf` — 24장 슬라이드 (영문)
- `Lecture 2 - Section 5.1  (9월 3일 목요일).pdf` — 14장 슬라이드 (영문)
- `5.1 Linear Algebra Solution.pdf` — §5.1 추천 연습문제(Friedberg) 풀이 9쪽 (문항: 1(a)–(k), 3(b)(d), 4(e)(g)(j), 11, 14, 15(a), 16(a), 17)
- `5.2 Linear Algebra Solution.pdf` — §5.2 추천 연습문제 풀이 6쪽 (문항: 1(a)–(h), 2(a)(d)(e), 3(a)(d)(e)(f), 7, 8, 9(a), 10, 11, 12, 18, 19)

**소스가 영문 슬라이드** → en-formal = verbatim 전사, ko-formal = 번역. 컨벤션은 `analysis2/`와 동일(analysis2/ch01.html 규약 주석) + 아래 la2 고유 규칙.
**슬라이드 PDF는 텍스트 추출이 불가**(한글 워드프로세서 수식이 글리프 없는 문자로 나옴) → 반드시 Read 도구로 페이지를 **시각적으로** 읽어 전사한다.
**학기 중 갱신되는 자료** — 강의마다 슬라이드 1개가 추가된다. 단원 = 교재 절(section). 새 강의가 오면 해당 단원 파일 끝(연습문제 섹션 앞)에 카드를 이어 붙이고 아래 인벤토리를 갱신한다.

## la2 고유 규칙 (analysis2 규약에 추가)

1. **카드 번호는 자체 순번** `c{단원}-{순번}`(슬라이드 등장 순). 배지는 `TYPE {단원}.{순번}` (예: `THM 1.5`). 슬라이드가 붙인 원문 번호(Theorem 1.3, Definition 3., Example 1., Theorem 5.1 …)는 제목 span 끝에 `<span class="src-ref">Theorem 1.3</span>`으로 표시한다. 번호 없는 라벨(Definition :, Remark :)은 src-ref를 두지 않는다.
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

## 전체 구조 (2026-09-03 현재)

| 단원 | 제목 | 소스 | 카드 | note | 연습문제 카드 |
|---|---|---|---|---|---|
| ch01 | 예비 사항: 선형대수학 I 복습 | Lecture 1 (24장) | 29 (EX 1) | 4 | — |
| ch02 | 5.1 고유값과 고유벡터 | Lecture 2 (14장) + §5.1 풀이 | 20 | 4 | 8 |
| ch03 | 5.2 대각화가능성 | §5.2 풀이 (강의 예정) | 0 | 1 | 11 |
| 계 | | | **49** | **9** | **19** (+ ch01 EX 1 = 풀이 대상 **20**) |

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

## 챕터별 인벤토리 (카드 id = 배지 번호; 슬라이드 페이지 = PDF 페이지)

### ch01.html — 예비 사항: 선형대수학 I 복습 / Preliminaries: Review of Linear Algebra I
Lecture 1, 24장. 카드 29 (DEF 12, THM 8, COR 1, EXAM 4, REM 3, EX 1) + note 4.

| id | 유형·배지 | 슬라이드 | 내용 | src-ref |
|---|---|---|---|---|
| note01-1 | NOTE | p2 | Review of Linear Algebra I — 이번 학기 Ch.5·6, 복습 항목 6개 목록 | |
| c1-1 | REM 1.1 (Q) | p3 | Question/Answer: 선형대수학의 연구 대상 = 벡터공간과 선형변환 | |
| c1-2 | DEF 1.2 | p4 | Definition of Field (1)–(6) + "Why do we need…" + "This semester… ℝ, ℂ" | |
| note01-2 | NOTE | p5 | Definition of Vector Space 도입: 벡터공간의 예 4개(ℝⁿ, Pₙ(F), M_{m×n}(F), C[0,1]) + "same algebraic rules" | |
| c1-3 | DEF 1.3 | p6 | Vector space (VS 1)–(VS 8) | |
| c1-4 | DEF 1.4 | p7 상 | Definition of Subspace | |
| c1-5 | THM 1.5 | p7 하 | Theorem 1.3: 부분공간 판정 (i)(ii)(iii) | Theorem 1.3 |
| c1-6 | EXAM 1.6 | p8 | P(F), Pₙ(F) 정의, Pₙ(F)는 P(F)의 부분공간 | |
| c1-7 | EXAM 1.7 | p9–11 | 행렬 용어(대각성분·행·열·정사각행렬), (1) 대각행렬 Dₙ, (2) 대칭행렬 정의·부분공간, (3) 대각합 tr, {tr=0} 부분공간 | |
| c1-8 | THM 1.8 | p12 | Theorem 1.4: 부분공간의 교집합 | Theorem 1.4 |
| c1-9 | DEF 1.9 | p13 | Linear Combination (1) 유한 S, (2) 비공 S; span(S) | |
| c1-10 | THM 1.10 | p14 | Theorem 1.5: span(S) 부분공간·최소성 | Theorem 1.5 |
| c1-11 | DEF 1.11 | p15 상 | Linearly dependent 정의 | |
| c1-12 | THM 1.12 | p15 하 | Theorem 1.7: S∪{v} 일차종속 ⇔ v∈span(S) | Theorem 1.7 |
| c1-13 | DEF 1.13 | p16 상 | Basis 정의 | |
| c1-14 | EXAM 1.14 | p16 중 | Fⁿ의 표준기저 | |
| c1-15 | EXAM 1.15 | p16 하 | P(F)의 기저 {1,x,x²,…} | |
| c1-16 | THM 1.16 | p17 상 | Theorem: 유한기저 ⇒ 모든 기저 n개 | |
| c1-17 | DEF 1.17 | p17 중 | finite dimensional, dim(V), infinite-dimensional | |
| c1-18 | **EX 1.18** | p17 하 | Question (1) ℝⁿ/ℝ dim n (2) ℂⁿ/ℂ dim n (3) ℂⁿ/ℝ dim 2n — **마커** | |
| c1-19 | DEF 1.19 | p18 | Linear transformation (1), N(T)·R(T) (2) | |
| c1-20 | DEF 1.20 | p19 상 | nullity(T), rank(T) | |
| c1-21 | THM 1.21 | p19 하 | Theorem 2.3 (Dimension Theorem) (i)(ii) | Theorem 2.3 |
| c1-22 | DEF 1.22 | p20 | Definition and Remark: 행렬표현 [T]_B^γ (1)(2)(3) | |
| c1-23 | THM 1.23 | p21 상 | Theorem: [T(v)]_γ = [T]_B^γ [v]_B | |
| c1-24 | REM 1.24 | p21 하 | Remark: 선형대수학 II의 출발점, Ch.5의 근본 질문 | |
| note01-3 | NOTE | p22 상 | Determinants 도입: det(A)≠0 ⇔ A invertible (박스) | |
| c1-25 | DEF 1.25 | p22 중 | Definition 1: 2×2 행렬식 | Definition 1 |
| c1-26 | DEF 1.26 | p22 하–p23 상 | Definition 2: 3×3 행렬식(여인수 전개 2줄) + 박스 6항 전개식 + "This formula says:" 4줄 | Definition 2 |
| note01-4 | NOTE | p23 중 | "In Chapter 4, we learned several fundamental properties… following formula." | |
| c1-27 | THM 1.27 | p23 하 | Leibniz Formula det(A)=Σ sgn(σ)Π a_{i,σ(i)} | |
| c1-28 | COR 1.28 | p24 상 | Corollary: det(A−tI) = (−1)ⁿtⁿ + lower terms, 차수 n | |
| c1-29 | REM 1.29 | p24 하 | Final Remark: 행렬식에서 고유값으로 | |

### ch02.html — 5.1 고유값과 고유벡터 / §5.1 Eigenvalues and Eigenvectors
Lecture 2, 14장 (9/8 강의분 추가 예정). 카드 20 (DEF 5, THM 2, EXAM 4, REM 9) + note 4 + 연습문제 8.
섹션 구분: `제5장 대각화 · Chapter 5. Diagonalization`(p2–7) → `§5.1 고유값과 고유벡터`(p8–14) → `연습문제 · Exercises (Friedberg §5.1)`.

| id | 유형·배지 | 슬라이드 | 내용 | src-ref |
|---|---|---|---|---|
| c2-1 | RECALL 2.1 | p2 | Recall: 선형연산자, (1) 좌표벡터 [T(v_i)]_B, 행렬표현 [T]_B | |
| note02-1 | NOTE | p3 상 | "This chapter is devoted to the so-called diagonalization problem…" | |
| c2-2 | REM 2.2 | p3–5 | Remark (1)–(4): L_A, R(L_A)=span{Au_i}, L_A(e_i)=v_i, 대각행렬일 때, 일반화 [L_A]_B 대각 | |
| c2-3 | Q 2.3 | p6 상 | 대각화 문제 도입 + Q1, Q2 | |
| c2-4 | REM 2.4 | p6 하 | Remark: [T]_B 대각이면 T(v)=Σ b_i a_ii v_i, 실용적 문제 | |
| c2-5 | EXAM 2.5 | p7 | Example: reflection along y=2x (1)–(5), [T]_β = diag(1,−1) | |
| c2-6 | RECALL 2.6 | p8 상 | Section 5.1 Recall: 목표 — T(v_i)=c_i v_i | |
| c2-7 | EXAM 2.7 | p8 하 | Example: reflection about y=2x, v₁=(1,2), v₂=(−2,1) | |
| c2-8 | DEF 2.8 | p9 상 | Definition 1: T diagonalizable | Definition 1 |
| c2-9 | DEF 2.9 | p9 중 | Definition 2: A diagonalizable | Definition 2 |
| c2-10 | REM 2.10 | p9 하 | Remark: A[v₁…vₙ]=[v₁…vₙ]D, Q 가역, A=QDQ⁻¹ | |
| c2-11 | REM 2.11 | p10 | when T diagonalizable / how to obtain B; (1)(2) | |
| note02-2 | NOTE | p11 상 | "In the preceding slide… motivate the following definitions." | |
| c2-12 | DEF 2.12 | p11 중 | Definition 3: eigenvector/eigenvalue of T | Definition 3 |
| c2-13 | DEF 2.13 | p11 하 | Definition 4: eigenvector/eigenvalue of A + ※ Terminologies | Definition 4 |
| c2-14 | THM 2.14 | p12 상 | Theorem 5.1: diagonalizable ⇔ eigenvector basis; D_jj | Theorem 5.1 |
| c2-15 | REM 2.15 | p12 하 | Remark: Theorem 5.1 shows … | |
| c2-16 | EXAM 2.16 | p13 상 | Example 1: A=(1 3;4 2), v₁=(1,−1) λ=−2, v₂=(3,4) λ=5, [L_A]_B=diag(−2,5) | Example 1 |
| c2-17 | EXAM 2.17 | p13 하 | Example 2: rotation π/2, 고유벡터 없음 | Example 2 |
| note02-3 | NOTE | p14 상 | Next Problem: how to find eigenvectors/eigenvalues? | |
| c2-18 | THM 2.18 | p14 중 | Theorem 5.2 + **Proof** (verbatim 토글) | Theorem 5.2 |
| c2-19 | DEF 2.19 | p14 하 | Definition: characteristic polynomial f(t)=det(A−tIₙ) | |
| c2-20 | REM 2.20 | p14 하 | Remark: eigenvalues = zeros of det(A−tIₙ) | |
| note02-4 | NOTE | (편집) | 갱신 안내: 9/8 강의분(§5.1 후반) 추가 예정 — 2언어 | |

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
강의(9/10·9/15) 미진행. note 1 + 연습문제 11. 강의 슬라이드가 오면 note03-1 앞에 카드 c3-1… 추가.

| id | 배지 | 문항 | 유형 | 기준값(공개 풀이) |
|---|---|---|---|---|
| note03-1 | NOTE | 갱신 안내(강의 예정, 연습문제 선공개) | | |
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
