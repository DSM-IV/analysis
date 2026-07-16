# 미적분학 1 용어집 (Calculus 1 Glossary)

Thomas Calculus 영문판 용어 관행을 따른다. **이 과목은 LA와 방향이 반대다: 한국어 원문(verbatim) → 영어 번역.**
번역·풀이 작성 시 이 표의 용어만 사용할 것.

## 문체 규칙
- **ko-formal = PDF 원문 그대로(verbatim).** 어미("-하시오", "-하여라", "-하라" 혼재)도 원문대로 두고 통일하지 않는다. 원문 오류도 그대로 (역주는 풀이 단계에서).
- **en-formal = 번역.** 문제 서술은 영어 명령문: Show that…, Prove that…, Find…, Compute…, Evaluate…, Determine whether…. "다음을 구하시오" → "Find the following." / "다음이 성립함을 보이시오" → "Show that the following holds."
- 풀이(한국어, Sonnet 작성): "-이다"체. 증명 문제는 "**증명.**"으로 시작해 <div class="qed">$\square$</div>로 종료. 계산 문제는 "**풀이.**"로 시작, qed 없음.
- 풀이(영어): "**Proof.**" + qed / "**Solution.**" no qed. 두 언어 같은 논증.
- 판별 기준: "증명하시오/보이시오/설명하시오"류 → 증명. "구하시오/계산하시오/판정하시오/근사하시오"류 → 풀이. 혼합형(구하고 증명하시오)은 증명으로 분류.
- 수식 TeX는 원문 그대로. **`<` 뒤에 문자가 바로 오는 표기 금지** — `\lt` 또는 공백 (`x < 1`) 사용. HTML 파싱이 깨진다.
- 임용 기출 태그는 양쪽 패널 제목에 그대로 보존: "(임용06-14)", "(임용23B-7)", "(2024(A)-10)". 번역하지 않는다.
- 5지선다(①–⑤)·보기(ㄱ,ㄴ,ㄷ) 형식 유지. 영어 패널에서도 ①–⑤, ㄱ/ㄴ/ㄷ 기호를 그대로 쓴다 (기출 원형 보존).

## 극한과 연속 (U01, U11)
| 한국어 | English |
|---|---|
| 극한의 엄밀한 정의 | precise definition of a limit |
| 우극한 / 좌극한 | right-hand / left-hand limit |
| 수렴 / 발산 | converge / diverge |
| 점근선 (수평/수직/사선) | asymptote (horizontal / vertical / oblique) |
| 연속 / 불연속 | continuous / discontinuous |
| 사잇값 정리 | Intermediate Value Theorem |
| 고정점 정리 | fixed point theorem |
| 디리클레 자 함수 | Dirichlet ruler function |
| 유리수 / 무리수 | rational / irrational number |
| 최대의 정수 ⌊x⌋ | greatest integer, floor $\lfloor x \rfloor$ |
| 수열 / 부분수열 | sequence / subsequence |
| 단조수렴정리 | Monotone Convergence Theorem |
| 단조증가/단조감소(함)수 | monotonically increasing / decreasing |
| 유계 / 상계 / 하계 | bounded / upper bound / lower bound |
| 상한 / 하한 | least upper bound (supremum) / greatest lower bound (infimum) |
| 일반항 | general term |
| 점화식 | recurrence relation |

## 미분과 근사 (U02, U03, U06)
| 한국어 | English |
|---|---|
| 선형화 | linearization |
| 선형근사(식) | linear approximation |
| 미분 $dy$ | differential |
| 이차 근사식 | quadratic approximation |
| 오차(함수) | error (function) $E(x)$ |
| 미분가능 | differentiable |
| 도함수 / 이계도함수 / $n$계도함수 | derivative / second derivative / $n$th derivative |
| 라이프니츠 규칙 | Leibniz's rule |
| 뉴턴의 방법 | Newton's method |
| 근 / 교점 | root / point of intersection |
| 근삿값 | approximate value |
| 평균값 정리 | Mean Value Theorem |
| 코시의 평균값 정리 | Cauchy's Mean Value Theorem |
| 코시-슈바르츠 부등식 | Cauchy–Schwarz inequality |
| 로피탈 정리 | L'Hôpital's Rule |
| 부정형 | indeterminate form |
| 증가율 | growth rate |
| 아래로/위로 볼록 | convex (concave up) / concave (concave down) |
| 상수함수 | constant function |
| 매개변수방정식 | parametric equations |

## 적분 (U04, U05, U08, U09, U10)
| 한국어 | English |
|---|---|
| 리만적분(가능) | Riemann integral (integrable) |
| 분할 / 소구간 / 노름 $\|P\|$ | partition / subinterval / norm |
| $n$등분 | division into $n$ equal subintervals |
| 상합 / 하합 | upper sum / lower sum |
| 균등연속 | uniformly continuous |
| 정적분 / 부정적분 | definite / indefinite integral |
| 평균값 $\operatorname{av}(f)$ | average value |
| 미적분학의 기본정리 | Fundamental Theorem of Calculus |
| 회전체 / 회전면 | solid / surface of revolution |
| 원판 | disk |
| 원주각 방법(shell method) | shell method |
| 호의 길이 (함수) | arc length (function) |
| 겉넓이 / 밑넓이 / 넓이 | surface area / area under the curve / area |
| 부피 | volume |
| 토러스 | torus |
| 성망형(astroid) | astroid |
| 카발리에리의 원리 | Cavalieri's principle |
| 부분적분법 | integration by parts |
| 치환적분법 | substitution |
| 삼각치환(법) | trigonometric substitution |
| 부분분수 | partial fractions |
| 수치적분 | numerical integration |
| 사다리꼴 근사 | Trapezoidal Rule |
| 심프슨 공식 | Simpson's Rule |
| 오차의 한계 | error bound |
| 오차함수(error function) | error function $\operatorname{erf}(x)$ |
| 사인적분함수 | sine-integral function $\operatorname{Si}(x)$ |
| 수렴속도 | rate of convergence |
| 이상적분 | improper integral |
| (극한)비교판정법 | (Limit) Comparison Test |
| 감마함수 | Gamma function |
| 스털링 공식 | Stirling's formula |
| 특이적분 | (임용 기출 표기) improper integral — 원문 병기 유지 |

## 여러 가지 함수 (U07)
| 한국어 | English |
|---|---|
| 역삼각함수 | inverse trigonometric functions |
| 쌍곡함수 / 역쌍곡함수 | hyperbolic / inverse hyperbolic functions |
| 예각 | acute angle |
| 접선의 기울기 | slope of the tangent line |
| $y$축 대칭 / 원점 대칭 | even (symmetric about the $y$-axis) / odd (symmetric about the origin) |
| 부채꼴 | circular sector |

## 급수 (U12, U13, U14)
| 한국어 | English |
|---|---|
| 급수 / 무한급수 | series / infinite series |
| 부분합 | partial sum |
| 조화급수 | harmonic series |
| $p$-급수 | $p$-series |
| 양항급수 | series of positive terms |
| 적분판정법 | Integral Test |
| 비판정법 | Ratio Test |
| 근판정법 | Root Test |
| 교대급수 (판정법) | alternating series (Alternating Series Test) |
| 절대수렴 / 조건수렴 | absolute / conditional convergence |
| 재배열 | rearrangement |
| 코시 응집 판정법 | Cauchy condensation test |
| 라비 판정법 | Raabe's test |
| 오일러 상수 | Euler's constant |
| 로그평균 | logarithmic mean |
| 멱급수 (거듭제곱급수) | power series |
| 수렴반경 / 수렴범위(수렴구간) | radius / interval of convergence |
| 확률질량함수 / 기댓값 | probability mass function / expected value |
| 테일러 급수 / 테일러 다항식 | Taylor series / Taylor polynomial |
| 매클로린 급수 | Maclaurin series |
| 나머지항 | remainder (term) |
| 테일러 정리 | Taylor's Theorem |
| 해석함수 | analytic function |
| 이항계수 / 일반화된 이항계수 | binomial coefficient / generalized binomial coefficient |
| 오일러 공식 | Euler's formula |
| 제1종 완전타원적분 | complete elliptic integral of the first kind |
| 라이프니츠 공식 | Leibniz's formula |
| 홀수차항 / 짝수차항 | odd-degree / even-degree terms |

## 매개화·극좌표·이차곡선 (U15, U16, U17)
| 한국어 | English |
|---|---|
| 매개화 / 재매개화 | parametrization / reparametrization |
| 자취 | trace (path) |
| 사이클로이드 | cycloid |
| 트로코이드 | trochoid |
| 하이포사이클로이드 / 에피사이클로이드 | hypocycloid / epicycloid |
| 극좌표(계) / 직교좌표(계) | polar / Cartesian coordinates |
| 극방정식 / 극곡선 | polar equation / polar curve |
| 수선의 발 | foot of the perpendicular |
| 이차곡선 | conic section |
| 이심률 | eccentricity |
| 준선 / 초점 / 꼭짓점 / 중심 | directrix / focus / vertex / center |
| 타원 / 쌍곡선 / 포물선 | ellipse / hyperbola / parabola |
| 장축 / 긴반지름 | major axis / semi-major axis |
| 당들랭의 구 | Dandelin sphere |
| 직원뿔 / 모선 | right circular cone / generating line (slant edge) |

## 금칙어 (banned terms — grep 대상)
- EN: ~~L'Hopital's theorem~~ → **L'Hôpital's Rule**; ~~trapezoid rule~~ → **Trapezoidal Rule**; ~~Simpson's rule~~ 소문자 rule 금지 → **Simpson's Rule**; ~~radius of convergency~~ → convergence
- KO(풀이 작성 시): ~~미분방정식~~ 오용 주의(U04 문제05만 해당); 수열 극한에서 ~~자연상수~~ → **자연로그의 밑 $e$** 또는 그냥 $e$; ~~절댓값~~은 표준어이므로 사용 (절대값 금지)
- 풀이에서 고윳값/고유값 등 LA 용어 불필요 — 등장 시 재검토

## 단원명 (파일 ↔ 제목)
| 파일 | 한국어 제목 | English |
|---|---|---|
| ch01 | 극한의 엄밀한 정의 | Precise Definition of a Limit |
| ch02 | 선형화와 미분 | Linearization and Differentials |
| ch03 | 뉴턴의 방법 | Newton's Method |
| ch04 | 리만적분 | The Riemann Integral |
| ch05 | 정적분의 활용 | Applications of Definite Integrals |
| ch06 | 로피탈 정리 | L'Hôpital's Rule |
| ch07 | 여러 가지 함수 | Transcendental Functions |
| ch08 | 적분의 계산 | Techniques of Integration |
| ch09 | 수치적분 | Numerical Integration |
| ch10 | 이상적분 | Improper Integrals |
| ch11 | 수열의 극한 | Limits of Sequences |
| ch12 | 급수 판정법 | Convergence Tests for Series |
| ch13 | 멱급수 | Power Series |
| ch14 | 테일러 급수 | Taylor Series |
| ch15 | 곡선의 매개화 | Parametrizations of Curves |
| ch16 | 극좌표계 | Polar Coordinates |
| ch17 | 이차곡선 | Conic Sections |

## 카드 구조 (LA 대비 변경점)
- 3단계: **예제**(exam) / **유제**(follow-up) / **문제**(problem). 예제·유제는 본 빌드에서 풀이 작성, 문제는 `<!-- PROOF-KO -->`/`<!-- PROOF-EN -->` 마커 유지.
- id 규칙: 예제 N → `ex{N}` (ex01), 유제 N-M → `yu{N}-{M}` (yu01-1), 유제 N(접미사 없음) → `yu{N}` (yu02), 문제 N → `pr{N}` (pr01). 두 자리 zero-pad.
- 배지: 예제 `<span class="ex-num">예제 01</span>`, 유제 `<span class="ex-num yu-num">유제 01-1</span>`, 문제 `<span class="pr-num">문제 01</span>`. (style.css에 `.yu-num` 색상 변형 추가)
- 카드 클래스: 예제·유제 = `card ex-card`, 문제 = `card pr-card`.
- 섹션: `<div class="section-title"><h2>예제·유제 · Examples &amp; Exercises</h2></div>` (원문 순서대로 예제/유제 교차 배치) / `<div class="section-title"><h2>문제 · Problems</h2></div>`
- 배치 순서는 PDF 원문 순서 그대로 (예제 01 → 유제 01-1 → 유제 01-2 → 예제 02 → …).
- en-formal 번역 전 placeholder는 `[번역 예정]` (검증 스크립트가 grep).
