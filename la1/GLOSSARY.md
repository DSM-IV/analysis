# 선형대수학 1 용어집 (Linear Algebra I Glossary — MATH221, Fall 2026)

소스: MATH221 Linear Algebra I (2026 Fall, 고려대 Changho Han, 비전공 분반) 손글씨 강의노트(Lecture 1–9, 12, 13) — 영문. 중간고사 기출(Fall 2024·2025)은 $\mathbb{F}=\mathbb{R}$ 또는 $\mathbb{C}$ 표기.
교재는 Friedberg–Insel–Spence 5th ed.(연습문제용)이지만 **내용·번호·기호는 강의노트를 따른다**(ℝ 위 벡터공간, $\mathcal{F}(X,\mathbb{R})$, $\mathbb{R}[x]$, $\mathbb{R}[x]_{\leq n}$, $M_{m\times n}(\mathbb{R})$).
`la/GLOSSARY.md`(Friedberg 한국어판 관행)를 상속한다. 번역·풀이 작성 시 이 표의 용어만 쓴다.

## 핵심 금칙·주의
- linear combination / linearly independent / linearly dependent = **일차결합 / 일차독립 / 일차종속** ("선형결합·선형독립·선형종속" 금지).
- span = **생성(span)**, $\operatorname{span}(S)$는 "$S$의 생성공간" 또는 "$\operatorname{span}(S)$" 그대로. "$S$ spans $W$" = "$S$가 $W$를 생성한다". spanning set = **생성집합**.
- subspace = **부분공간**, trivial subspace = **자명한 부분공간**, Subspace Criterion = **부분공간 판정법**.
- vector space = **벡터공간**, zero vector = **영벡터**, additive inverse = **덧셈에 대한 역원**(줄여서 역원), scalar multiplication = **스칼라곱**.
- basis / bases / standard basis = **기저 / 기저들 / 표준기저**, dimension = **차원**, Replacement Theorem = **교체정리**(첫 등장에 "(Replacement Theorem)" 병기 가능).
- Cancellation Law = **소거법칙**. Proposition = **명제**, Lemma = **보조정리**, Corollary = **따름정리**, Remark = **주의**, Notation = **표기**, Claim = **주장**, Motivation = **동기**, Exercise = **연습**.
- 강의노트 약어(v.s., subsp, l.c., l.i., l.d., fcn, w/, b/c, s.t., WTS, Pf, iff, std, fin, coeffs, #s, elts, vecs, col)는 **en에만** 그대로 둔다. ko는 풀어 쓴다: v.s.→벡터공간, subsp→부분공간, l.c.→일차결합, l.i.→일차독립, l.d.→일차종속, fcn→함수, s.t.→~인/~를 만족하는, WTS→보이고자 하는 것, Pf→증명, iff→필요충분조건(⟺), std→표준, fin→유한, coeffs→계수.
- 수식 안의 기호(∀, ∃, ⇒, ⟺, :=, ※, ▨)는 그대로 둔다. ※는 "모순" 표시, ▨(`<span class="part-end">`)는 증명 중간 단계 끝 표시 — 손대지 말 것.

## 문체 규칙 (la2·analysis2와 동일)
- 진술·증명: "-이다"체. 연습·문제 서술: "-하라"체("증명하라", "확인하라", "구하라").
- 증명/풀이 토글: 라벨("증명."/"Proof.") 없이 본문 바로 시작. 원문 증명은 en verbatim + ko 번역 미러(문단·항목 구조 동일), qed `<div class="qed">□</div>` 유지.
- **display·inline 수식 안의 `\text{…}` 영문 산문도 ko 패널에서는 한국어로** 옮긴다 (예: `\text{for some } a_i` → `(\text{어떤 } a_i \text{에 대하여})`, `\text{ s.t. }` → `\text{ 인 }`/`\text{을 만족하는}`). 기호·변수명은 그대로.
- 강의노트 원문 오타는 en에 그대로 두고, ko는 **바른 뜻**으로 옮긴다(오타 목록은 SOURCE-MAP ERRATA).
- 색 강조·밑줄은 옮기지 않는다. `[Figure: …]` 설명줄은 ko에서 `[그림: …]`으로 번역.

## 용어표
| English | 한국어 |
|---|---|
| set of all real numbers ℝ | 실수 전체의 집합 ℝ |
| pair / 2-tuple / $n$-tuple | 순서쌍 / 2-튜플 / $n$-튜플 |
| $k$-th coordinate | $k$번째 좌표 |
| coordinate-wise addition | 좌표별 덧셈 |
| Cartesian plane | 좌표평면(데카르트 평면) |
| (Cartesian) product $X\times Y$ | (데카르트) 곱 |
| function (map) / domain / codomain | 함수(사상) / 정의역 / 공역 |
| 1-1 correspondence / bijection / 1-1 & onto | 일대일대응 / 전단사 / 단사이고 전사 |
| displacement / reference point | 변위 / 기준점 |
| Mathematician's Guiding Principle | 수학자의 지침 |
| column vector / row vector (of size $n$) | (크기 $n$의) 열벡터 / 행벡터 |
| axioms of vector space (VS 1)–(VS 8) | 벡터공간의 공리 (VS 1)–(VS 8) |
| abuse of notation | 기호의 남용 |
| set of all functions from $X$ to ℝ | $X$에서 ℝ로 가는 함수 전체의 집합 |
| sequence | 수열 |
| $m\times n$ matrix / $(i,j)$-entry / square matrix | $m\times n$ 행렬 / $(i,j)$-성분 / 정사각행렬 |
| symmetric matrix | 대칭행렬 |
| even function | 짝함수 (우함수) |
| polynomial / coefficient / degree / variable | 다항식 / 계수 / 차수 / 변수 |
| continuous function | 연속함수 |
| induced (restricted) operations | 유도된(제한된) 연산 |
| power set $\mathcal{P}(V)$ | 멱집합 |
| intersection / union | 교집합 / 합집합 |
| skeleton (of $W$) | ($W$의) 뼈대 |
| system of linear equations / method of elimination / substitution | 연립일차방정식 / 소거법 / 대입 |
| compare coefficients | 계수를 비교하다 |
| smallest subspace containing $S$ | $S$를 포함하는 가장 작은 부분공간 |
| generates | 생성한다 |
| redundant (vector) | 중복된 (불필요한) 벡터 |
| benchmark (this experiment) | (이 실험을) 기준으로 삼다 |
| list $(w_1,\dots,w_k)\in V^k$ / ordered / unordered | 리스트 / 순서 있는 / 순서 없는 |
| Kronecker delta $\delta_{ij}$ | 크로네커 델타 |
| contrapositive / contradiction / by construction | 대우 / 모순 / 구성에 의해 |
| minimal subset | 극소 부분집합 |
| unique / there exists unique ∃! | 유일한 / 유일하게 존재한다 |
| coordinates relative to $\beta$, $[w]_\beta$ | $\beta$에 대한 좌표 $[w]_\beta$ |
| Math-Major Only | 수학과 전용 |
| infinite set | 무한집합 |
| finite-dimensional (f.d.) / infinite-dimensional | 유한차원 / 무한차원 |
| Basis Extension Theorem (BET) | 기저 확장정리 |
| well-defined | 잘 정의된 |
| Lagrange interpolation | 라그랑주 보간 |
| parallelogram / parallelepiped / (signed) volume | 평행사변형 / 평행육면체 / (부호 있는) 부피 |
| tangent line / approximation | 접선 / 근사 |
| attendance / quiz / midterm / final exam | 출석 / 퀴즈 / 중간고사 / 기말고사 |
| Unit Notes | 단원 노트(Unit Notes) |
| data points | 자료점 |
| Lagrange polynomials (associated with $t_0,\dots,t_n$) | ($t_0,\dots,t_n$에 대응하는) 라그랑주 다항식 |
| Lagrange Interpolation Formula (LIF) | 라그랑주 보간 공식 |
| distinct | 서로 다른 |
| linear transformation / linear map / homomorphism | 선형변환 / 선형사상 / 준동형사상 |
| $\mathcal{L}(V,W)$ (set of linear maps) | $V$에서 $W$로 가는 선형사상 전체의 집합 $\mathcal{L}(V,W)$ |
| range / image $\operatorname{im}(f)$ | 치역 / 상 |
| preimage $f^{-1}(Z)$ | 역상 |
| kernel (ker) / isomorphism (isom) | 핵 / 동형사상 |
| rotation by $\frac{\pi}{2}$ CCW | 반시계 방향으로 $\frac{\pi}{2}$만큼의 회전 |
| shear | 층밀림 |
| fix origin / send a line to a line | 원점을 고정하다 / 직선을 직선으로 보내다 |
| Set Theory Warm-Up | 집합론 준비 |

## 단원명 (파일 ↔ 제목)
| 파일 | 한국어 제목 | English |
|---|---|---|
| ch01 | 1.1 벡터공간으로서의 ℝⁿ | §1.1 ℝⁿ as a Vector Space |
| ch02 | 1.2 벡터공간과 부분공간 | §1.2 Vector Spaces and Subspaces |
| ch03 | 1.3 일차결합, 생성, 일차독립 | §1.3 Linear Combinations, Span, and Linear Independence |
| ch04 | 1.4 기저와 차원 | §1.4 Basis and Dimension |
| ch05 | 2.1 선형사상: 핵, 상, 동형사상 | §2.1 Linear Maps: Kernel, Image, and Isomorphism |
| identity map $I_V = \mathbb{1}_V$ | 항등사상 |
| zero map $T_0$ (written $0 \in \mathcal{L}(V,W)$) | 영사상 |
| linear operator ($T \in \mathcal{L}(V)$) | 선형연산자 |
| differentiation $D$ | 미분 |
| Take this granted | (이 사실은) 그대로 받아들인다 |
| induction on $n$ | $n$에 대한 귀납법 |
| kernel $\ker(T)$ / null space (FIS) | 핵 / 영공간(FIS의 용어) |
| image $\operatorname{im}(T)$ / range (FIS) | 상 / 치역(FIS의 용어) |
| roots $f^{-1}(0)$ | 근 |
| 1-1 (injective) / onto (surjective) | 단사(일대일) / 전사 |
| Observation | 관찰 |
| nullity $\operatorname{nullity}(T)$ | 퇴화차수(nullity) |
| rank $\operatorname{rank}(T)$, $\operatorname{rk}(T)$ | 계수(rank) |
| Rank-Nullity Theorem (R-N) / Dimension Theorem (FIS) | 계수-퇴화차수 정리 / 차원정리(FIS) |
| plane / line (through the origin) | (원점을 지나는) 평면 / 직선 |
| coordinate vector $[v]_\beta$ / matrix representation $[T]_\beta$ | 좌표벡터 / 행렬표현 |
| matrix–vector multiplication | 행렬-벡터 곱 |
