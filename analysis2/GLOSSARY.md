# 해석학2 용어집 (Analysis II Glossary)

대한수학회 용어집 + 기존 해석학1(루트) 관행을 따른다 (Rudin, *Principles of Mathematical Analysis* 기반 강의노트).
번역·풀이 작성 시 이 표의 용어만 사용할 것.

**핵심 금칙·주의**
- uniformly continuous = **균등연속** ("고른연속" 금지), uniform convergence = **균등수렴** ("고른수렴"·"평등수렴" 금지).
- Riemann-Stieltjes = **리만-스틸체스** (스틸티예스·스틸티어스 금지).
- compact = **콤팩트** ("옹골집합" 금지), Heine-Borel = 하이네-보렐.
- L'Hospital's rule = **로피탈 법칙** (en은 원문 표기 L'Hospital 그대로; "로피탈의 정리" 금지).
- 사이시옷: 최댓값/최솟값/극댓값/극솟값 (최대값·극대값 금지).
- one-to-one = 일대일 (함수 성질로는 단사); "일대일함수" 금지.
- 사람 이름: 롤(Rolle), 코시(Cauchy), 다르부(Darboux), 테일러(Taylor), 리만(Riemann), 스틸체스(Stieltjes), 하이네(Heine)-보렐(Borel), 루딘(Rudin).

## 문체 규칙 (settheory와 동일)
- 문제 서술: "-하라"체. 진술·증명: "-이다"체.
- 증명/풀이 토글: 라벨("증명."/"Proof.") 없이 본문 바로 시작. 증명형(prove-or-disprove 포함)은 "증명 보기/증명 접기 · Proof/Hide Proof" + `<div class="qed">□</div>`; 서술·판정·설명형은 "풀이 보기/풀이 접기 · Solution/Hide Solution", qed 없음.
- 수식·기호 원문 verbatim: $\lim_{x\to c^+}$, $\lim_{x\downarrow c}$, $f^{(n)}$, $U(P,f,\alpha)$, $L(P,f,\alpha)$, $\int_a^{\bar{b}}$(상적분 표기는 원문 그대로 $\bar{\int_a^b}$/$\underline{\int_a^b}$ 계열), $\Delta x_i$, $\Delta\alpha_i$, $b \wedge d$, $a \vee c$, $I(x-s)$, $I_A(x)$.

## §1 미분
| English | 한국어 |
|---|---|
| metric space / metric (distance function) | 거리공간 / 거리함수 |
| point | 점 |
| limit / right limit / left limit | 극한 / 우극한 / 좌극한 |
| limit point | 극한점 |
| continuous at / on | ~에서/~에서(위에서) 연속 |
| left/right continuous | 좌연속 / 우연속 |
| differentiable / derivative | 미분가능 / 도함수 |
| (value) $f'(x)$ at a point | 미분계수 |
| angle | 각 |
| cosine / sine | 코사인 / 사인 |
| chain rule | 연쇄법칙 |
| intuitive proof / rigorous proof | 직관적 증명 / 엄밀한 증명 |
| local maximum / local minimum | 극대 / 극소 (극댓값·극솟값) |
| maximum / minimum | 최댓값 / 최솟값 |
| Rolle's theorem | 롤의 정리 |
| mean-value theorem | 평균값 정리 |
| Cauchy's mean-value theorem | 코시 평균값 정리 |
| monotonically increasing/decreasing | 단조증가 / 단조감소 |
| strictly increasing/decreasing | 순증가 / 순감소 |
| constant (function) | 상수(함수) |
| upper/lower bound | 상계 / 하계 |
| bounded above/below | 위로 유계 / 아래로 유계 |
| the least upper bound / supremum | 최소상계 / 상한 |
| the greatest lower bound / infimum | 최대하계 / 하한 |
| reduction to absurdity | 귀류법 |
| intermediate value theorem | 중간값 정리 |
| intermediate value property | 중간값 성질 |
| Darboux Theorem | 다르부 정리 |
| L'Hospital's rule | 로피탈 법칙 |
| $n$-times differentiable / $n$-th derivative | $n$번 미분가능 / $n$계 도함수 |
| a generalization of the mean-value theorem | 평균값 정리의 일반화 |
| Taylor's theorem | 테일러 정리 |
| polynomial | 다항식 |
| best polynomial approximation | 최선의 다항식 근사 |
| without loss of generality | 일반성을 잃지 않고 |

## §2 리만-스틸체스 적분
| English | 한국어 |
|---|---|
| partition | 분할 |
| refinement / common refinement | 세분 / 공통 세분 |
| upper sum / lower sum | 상합 / 하합 |
| upper/lower Riemann integral | 상리만적분 / 하리만적분 |
| Riemann-integrable / the Riemann integral | 리만 적분가능 / 리만 적분 |
| Riemann-Stieltjes integrable with respect to $\alpha$ | $\alpha$에 관하여 리만-스틸체스 적분가능 |
| upper and lower Riemann-Stieltjes integral | 상·하 리만-스틸체스 적분 |
| dummy variable | 더미 변수(dummy variable) |
| uniformly continuous | 균등연속 |
| index set | 첨수집합 |
| collection of sets / family of sets | 집합들의 모임 / 집합들의 족 |
| open cover / subcover / finite subcover | 열린 덮개 / 부분덮개 / 유한 부분덮개 |
| compact | 콤팩트 |
| Heine-Borel Theorem | 하이네-보렐 정리 |
| points of discontinuity | 불연속점 |
| countable subset | 가산 부분집합 |
| linear property | 선형성(선형 성질) |
| unit step function | 단위계단함수 |
| indicator function | 지시함수 |
| converge / absolutely converge | 수렴 / 절대수렴 |
| change of variable | 변수변환 |
| the fundamental theorem of calculus | 미적분학의 기본정리 |
| integration by parts | 부분적분 |
| product rule of differentiation | 곱의 미분법 |

## §3 함수열
| English | 한국어 |
|---|---|
| sequence of functions | 함수열 |
| series of functions | 함수급수 |
| converges to $f$ pointwise | $f$로 점별수렴한다 |
| the (pointwise) limit / limit function | (점별) 극한 / 극한함수 |
| converges to $f$ uniformly | $f$로 균등수렴한다 |
| counter example | 반례 |

## 단원명 (파일 ↔ 제목)
| 파일 | 한국어 제목 | English |
|---|---|---|
| ch01 | 1. 미분 (i): 극한·연속·도함수 | 1. Differentiation (i): Limits, Continuity, and the Derivative |
| ch02 | 1. 미분 (ii): 평균값 정리와 그 응용 | 1. Differentiation (ii): The Mean-Value Theorems and Applications |
| ch03 | 1. 미분 (iii): 로피탈 법칙과 테일러 정리 | 1. Differentiation (iii): L'Hospital's Rule and Taylor's Theorem |
| ch04 | 2. 리만-스틸체스 적분 (i): 정의와 적분가능성 판정 | 2. The Riemann-Stieltjes Integral (i): Definitions and the Integrability Criterion |
| ch05 | 2. 리만-스틸체스 적분 (ii): 적분가능 함수와 연산 | 2. The Riemann-Stieltjes Integral (ii): Integrable Functions and Algebraic Properties |
| ch06 | 2. 리만-스틸체스 적분 (iii): 계단함수·변수변환·미적분학의 기본정리 | 2. The Riemann-Stieltjes Integral (iii): Step Functions, Change of Variable, and the FTC |
| ch07 | 3. 함수열과 함수급수 | 3. Sequence and Series of Functions |
