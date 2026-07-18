# 미적분학 2 용어집 (Calculus 2 Glossary)

Thomas Calculus 영문판 용어 관행을 따른다. **calc1과 동일: 한국어 원문(verbatim) → 영어 번역.**
번역·풀이 작성 시 이 표의 용어만 사용할 것. calc1 용어집(`calc1/GLOSSARY.md`)의 문체 규칙·공통 용어를 그대로 상속하고, 이 파일은 calc2 신규 용어를 추가한다.

## 문체 규칙 (calc1 상속 + calc2 보강)
- **ko-formal = PDF 원문 그대로(verbatim).** 어미("-하시오", "-하여라" 혼재)도 원문대로. 원문 오류도 그대로 (역주는 풀이 단계에서).
- **en-formal = 번역.** Show that… / Prove that… / Find… / Compute… / Evaluate… / Determine whether… / Sketch… / Parametrize….
- 풀이: 증명 = "**증명.**"…qed $\square$ / "**Proof.**"…qed. 계산 = "**풀이.**" / "**Solution.**" qed 없음. "보이시오/증명하시오/확인하시오/판별하시오(참·거짓)"류 → 증명, "구하시오/계산하시오/나타내시오/근사하시오"류 → 풀이. 혼합형은 증명.
- 수식 TeX 원문 그대로. **`<` 뒤에 문자 금지** — `\lt` 또는 공백. 벡터는 `\mathbf{u}`, 점 위 화살표는 `\overrightarrow{OP}`.
- 임용 태그 보존, 선다형 ①–⑤·〈보기〉 ㄱㄴㄷ 기호 양쪽 패널 유지, 〈보기〉의 EN 라벨은 **`<List>`**.
- 좌표계 문자: 원통 $(r, \theta, z)$, 구면 $(\rho, \phi, \theta)$ ($\phi$ = z축에서 잰 각). 곡률 $\kappa$, 열률 $\tau$.

## 벡터와 공간 기하 (U01, U02)
| 한국어 | English |
|---|---|
| 공간벡터 / 평면벡터 | vector in space / vector in the plane |
| 시점 / 종점 | initial point / terminal point |
| 성분 | component |
| 크기 $\lvert\mathbf{v}\rvert$ | magnitude |
| 단위벡터 | unit vector |
| 표준단위벡터 $\mathbf{i},\mathbf{j},\mathbf{k}$ | standard unit vectors |
| 방향 | direction |
| 속력 / 속도 | speed / velocity |
| 내적 | dot product |
| 외적 | cross product |
| (벡터) 정사영 $\operatorname{proj}_{\mathbf v}\mathbf u$ | (vector) projection |
| 스칼라 성분 | scalar component |
| 수직 / 평행 | perpendicular (orthogonal) / parallel |
| 이등분(하다) | bisect |
| 무게중심 | centroid |
| 방향코사인 | direction cosine |
| 평행육면체 | parallelepiped |
| 삼각뿔 (사면체) | tetrahedron |
| 정사면체 | regular tetrahedron |
| 평행사변형 | parallelogram |
| 스칼라 삼중적 | scalar triple product |
| 매개변수방정식 | parametric equations |
| 법선벡터 / 법선 | normal vector / normal line |
| 꼬인 위치 | skew (lines) |
| 위치관계 | relative position |
| 주면 | cylinder |
| 생성 곡선 | generating curve |
| 이차곡면 | quadric surface |
| 타원면 | ellipsoid |
| 타원형 포물면 | elliptical paraboloid |
| 타원형 뿔면 | elliptical cone |
| 일엽쌍곡면 | hyperboloid of one sheet |
| 이엽쌍곡면 | hyperboloid of two sheets |
| 쌍곡포물면 | hyperbolic paraboloid |
| 반사광 | reflected ray |

## 벡터 함수와 공간 운동 (U03, U04)
| 한국어 | English |
|---|---|
| 벡터 함수 | vector function |
| 위치벡터 | position vector |
| 속도벡터 / 가속도벡터 | velocity / acceleration vector |
| 나선 | helix |
| 접선 | tangent line |
| 호의 길이 (함수) | arc length (function) |
| 재매개화 | reparametrization |
| 단위접선벡터 $\mathbf{T}$ | unit tangent vector |
| 주단위법선벡터 $\mathbf{N}$ | principal unit normal vector |
| 단위종법선벡터 $\mathbf{B}$ | unit binormal vector |
| 곡률 $\kappa$ | curvature |
| 곡률반경(곡률반지름) | radius of curvature |
| 곡률중심 | center of curvature |
| 접촉원 | osculating circle |
| 접촉평면 | osculating plane |
| 법평면 | normal plane |
| 교정면 | rectifying plane |
| 열률 (비틀림률, 꼬임률) | torsion |
| 전곡률 | total curvature |
| 신개선 | involute |
| 정칙곡선 (정규곡선) | regular curve |
| 단위속력곡선 | unit speed curve |
| 접선벡터장 / 법벡터장 | tangent / normal vector field |
| $\mathbf{T}$방향 성분 / $\mathbf{N}$방향 성분 | tangential / normal component (of acceleration) |
| 극좌표 단위벡터 $\mathbf{u}_r, \mathbf{u}_\theta$ | polar unit vectors |
| 각운동량 (보존법칙) | angular momentum (conservation law) |
| 자취 | trace (path) |

## 다변수함수: 극한·연속·편도함수 (U05, U06)
| 한국어 | English |
|---|---|
| 다변수함수 | function of several variables |
| 정의역 / 치역 | domain / range |
| 열린집합 / 닫힌집합 | open set / closed set |
| 내부 / 경계 | interior / boundary |
| 유계 | bounded |
| 등위선 / 등위면 | level curve / level surface |
| 극한값 | limit |
| (원점에서) 연속 | continuous (at the origin) |
| 편도함수 | partial derivative |
| 편미분 | partial differentiation |
| 이계 편도함수 | second-order partial derivative |
| 혼합 편도함수 | mixed partial derivative |
| 순간변화율 | instantaneous rate of change |
| 합성저항 | combined (equivalent) resistance |
| 연쇄법칙 | Chain Rule |
| 음함수 (미분법) | implicit function (implicit differentiation) |
| 독립변수 / 종속변수 | independent / dependent variable |
| 동차함수 | homogeneous function |
| 라이프니츠 정리 | Leibniz's rule |
| 이상기체 / 내부에너지 | ideal gas / internal energy |

## 편도함수의 활용 (U07, U08)
| 한국어 | English |
|---|---|
| 기울기 벡터 $\nabla f$ | gradient (vector) |
| 방향도함수 $D_{\mathbf u}f$ | directional derivative |
| 접평면 | tangent plane |
| 법선 | normal line |
| 선형화 / 선형근사 | linearization / linear approximation |
| 변화량 | change |
| 오차의 한계 | error bound |
| 상대오차 | relative error |
| 극값 / 극댓값 / 극솟값 | local extreme value / local maximum / local minimum |
| 최댓값 / 최솟값 | (absolute) maximum / minimum |
| 임계점 | critical point |
| 안장점 | saddle point |
| 이계도함수 판정법 | Second Derivative Test |
| 라그랑주 승수(법) | Lagrange multiplier(s) (method of) |
| 제약조건 | constraint |
| 이차근사식 / 3차근사식 | quadratic / cubic approximation |
| 테일러급수 | Taylor series |
| 추세선 | trend line |
| 동형 / 이형 (혈액형) | homozygous / heterozygous |
| 체감온도 | wind-chill temperature |

## 중적분 (U09, U10)
| 한국어 | English |
|---|---|
| 이중적분 | double integral |
| 삼중적분 | triple integral |
| 중적분 | multiple integral |
| 반복적분 | iterated integral |
| 적분 순서(를 바꾸다) | (reverse the) order of integration |
| 평균값 | average value |
| 분포함수 | distribution function |
| 원통좌표계 | cylindrical coordinates |
| 구면좌표계 | spherical coordinates |
| 변환 / 변수변환 | transformation / change of variables |
| 야코비안 | Jacobian |
| 감마함수 | Gamma function |
| 제1팔분공간 | first octant |
| 공통영역 | common region (intersection) |
| 대칭성 | symmetry |

## 벡터해석 (U11–U14)
| 한국어 | English |
|---|---|
| 벡터장 | vector field |
| 기울기 벡터장 | gradient (vector) field |
| 선적분 | line integral |
| 일 | work |
| 유동 | flow |
| 순환 | circulation |
| 유출 | flux |
| 밀도 | density |
| 질량중심 | center of mass |
| 중력장 / 중력가속도 | gravitational field / gravitational acceleration |
| 보존적 벡터장 | conservative vector field |
| 잠재함수 | potential function |
| 닫힌 벡터장 | closed vector field |
| 완전형식 | exact (differential) form |
| 단순닫힌곡선 | simple closed curve |
| 단순연결영역 | simply connected region |
| 순환밀도 | circulation density |
| 발산밀도 | flux density (divergence) |
| 그린 정리 | Green's Theorem |
| 그린 제1정리 / 제2정리 | Green's first / second identity |
| 회전 $\nabla\times\mathbf{F}$ | curl |
| 발산 $\nabla\cdot\mathbf{F}$ | divergence |
| 심장형 곡선 | cardioid |
| 면적분 | surface integral |
| 매개화(하다) / 매개화된 곡면 | parametrize / parametrized surface |
| 회전면 | surface of revolution |
| 향 / 유향곡면 | orientation / oriented surface |
| (곡면을) 가로지르는 | across (the surface) |
| (곡면을) 빠져나오는 | outward through (the surface) |
| 겉넓이 | surface area |
| 스토크스 정리 | Stokes' Theorem |
| 발산 정리 | Divergence Theorem |
| 라플라스 방정식 | Laplace equation |
| 조화함수 | harmonic function |
| 일급 / 이급 벡터장(함수) | of class $C^1$ / $C^2$ |
| 패러데이 법칙 | Faraday's law |
| 전기장 / 자기장 | electric / magnetic field |

## 금칙어 (banned terms — grep 대상)
- KO: ~~컬~~ → **회전**; ~~다이버전스~~ → **발산**; ~~그라디언트~~/~~그래디언트~~ → **기울기 벡터**; ~~포텐셜 함수~~ → **잠재함수**; ~~플럭스~~ → **유출**; ~~벡터곱~~ → **외적**; ~~스칼라곱~~(내적 의미) → **내적**; ~~법선벡터~~를 "단위종법선벡터" 자리에 오용 금지
- EN: ~~Stoke's Theorem~~ → **Stokes' Theorem**; ~~Green theorem~~ → **Green's Theorem**; ~~divergence theorem~~ 소문자 → **Divergence Theorem**; ~~Laplace's equation~~ → **Laplace equation** (원문 병기 형식 유지); ~~cross-product~~ → **cross product**; ~~dot-product~~ → **dot product**
- 주의: "노름"은 calc2에서 사용하지 않음 — 벡터 크기는 magnitude $\lvert\mathbf v\rvert$. (calc1 U04의 분할 노름 $\|P\|$와 무관)

## 단원명 (파일 ↔ 제목)
| 파일 | 한국어 제목 | English |
|---|---|---|
| ch01 | 공간벡터와 그 연산 | Vectors in Space and Their Operations |
| ch02 | 도형의 방정식 | Equations of Lines, Planes, and Surfaces |
| ch03 | 벡터 함수 | Vector Functions |
| ch04 | 공간 운동 | Motion in Space |
| ch05 | 다변수함수의 극한과 연속 | Limits and Continuity of Multivariable Functions |
| ch06 | 편도함수와 그 계산 | Partial Derivatives and Their Computation |
| ch07 | 편도함수의 활용-변화율과 접평면 | Applications of Partial Derivatives: Rates of Change and Tangent Planes |
| ch08 | 편도함수의 활용-극값과 테일러급수 | Applications of Partial Derivatives: Extreme Values and Taylor Series |
| ch09 | 이중적분 | Double Integrals |
| ch10 | 삼중적분 | Triple Integrals |
| ch11 | 벡터장과 선적분 | Vector Fields and Line Integrals |
| ch12 | 선적분의 성질과 그린 정리 | Properties of Line Integrals and Green's Theorem |
| ch13 | 면적분 | Surface Integrals |
| ch14 | 스토크스 정리와 발산 정리 | Stokes' Theorem and the Divergence Theorem |

## 카드 구조 (calc1과 동일)
- id 규칙: 예제 N → `ex{N}`, 유제 N-M → `yu{N}-{M}`, 유제 N(단독) → `yu{N}`, 문제 N → `pr{N}`. 두 자리 zero-pad. **U02의 중복 유제 02-3은 `yu02-3a`/`yu02-3b`** (표시 라벨은 둘 다 "유제 02-3").
- 배지: `<span class="ex-num">예제 01</span>` / `<span class="ex-num yu-num">유제 01-1</span>` / `<span class="pr-num">문제 01</span>`.
- 카드 클래스: 예제·유제 = `card ex-card`, 문제 = `card pr-card`. 배치는 PDF 원문 순서 그대로.
- 섹션: `예제·유제 · Examples &amp; Exercises` / `문제 · Problems`.
- en-formal 번역 전 placeholder는 `[번역 예정]`.
