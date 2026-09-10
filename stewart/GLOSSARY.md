# Stewart 교재 섹션 용어집·표기 규약 (stewart/GLOSSARY.md)

대상: Stewart, *Calculus: Early Transcendentals* 9e, §12.6·14·15·16. 이 섹션은 **Stewart 표기를 그대로** 따른다(강의 교안 calc2/의 Thomas 표기와 다름). `calc2/GLOSSARY.md`의 공통 용어(벡터·미분·적분 기본어)는 상속하되, 아래 표가 우선한다.

## 1. 문체·구조 규칙
- **언어 방향**: ko = 해석(주 언어, 재서술), en = 재서술 요약. **원문 영어 산문을 그대로 옮기지 않는다.** 정의·정리의 수학적 진술(수식·조건)은 정확히 옮기고, 설명 문단은 요지만 쓴다.
- 카드 종류: `note`(절 도입·개념 해설), `def`(정의), `thm`(정리·번호 공식), `rem`(NOTE/WARNING/표기 박스), `exam`(Example). 원문 번호는 `<span class="src-ref">Definition 7</span>`, `Theorem 8`, `Eq. (6)`, `Example 5`, `Table 1`로 카드 제목 끝에 표시.
- **번호 체계(명문화)**: 카드 배지(`DEF 3`, `THM 10`)는 그 절 페이지 안의 카드 순번이고, 본문·풀이에서 정의·정리를 인용할 때는 **원문 라벨**("정의 1", "정리 8", "식 (6)")을 쓴다. formal-box 머리말도 원문 라벨("정의 4.", "클레로 정리."). 번호 공식 라벨 카드의 머리말은 "식 (2) — 접평면의 방정식." 형식.
- 카드 id: 개념 `c{절}-{순번}` (예 `c14-3-4`), 예제 `ex{절}-{번호}` (예 `ex14-3-5`), 도입 note는 순번에 포함.
- 예제 문제문: **재서술**(문장 구조를 바꾸고 조건은 정확히). ko는 "-하라"체. en은 Find / Show that / Evaluate / Determine / Sketch.
- 풀이: 계산·구하기 = "**풀이.**"/"**Solution.**" (qed 없음); 보이기·증명 = "**증명.**"/"**Proof.**" + qed $\square$. 교재 풀이와 **다른 서술**로 자체 작성(방법이 같아도 문장·전개 순서를 베끼지 않음). 교재와 다른 방법이 자연스러우면 병기.
- 정리 증명: 원문에 증명이 있으면 토글 "증명 보기/Proof"에 **요지 재서술**(원문 문장 전재 금지). Appendix 증명·생략된 증명은 "증명은 교재 Appendix F 참조"만.
- 수식: TeX. **`<` 뒤에 문자 금지** — `\lt` 또는 공백. 벡터 `\mathbf{F}`, 단위벡터 `\mathbf{i},\mathbf{j},\mathbf{k}`, 성분 `\langle a, b, c\rangle`.
- 그림: 교재 그림 전재 금지. 필요한 그림만 자체 SVG(양 패널에 복제).

## 2. Stewart 표기 규약 (반드시 준수 — calc2와 다른 곳)
| 항목 | 이 섹션(Stewart) | calc2(Thomas) — 쓰지 말 것 |
|---|---|---|
| 벡터 성분 | $\langle a_1, a_2, a_3\rangle$, 또는 $a_1\mathbf i+a_2\mathbf j+a_3\mathbf k$ | $(a_1,a_2,a_3)$ |
| 평면 벡터장 | $\mathbf F = P\,\mathbf i + Q\,\mathbf j$ | $M\mathbf i+N\mathbf j$ |
| 공간 벡터장 | $\mathbf F = P\,\mathbf i + Q\,\mathbf j + R\,\mathbf k$ | $M\mathbf i+N\mathbf j+P\mathbf k$ |
| 그린 정리 | $\displaystyle\oint_C P\,dx+Q\,dy=\iint_D\Big(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Big)dA$ | $(N_x-M_y)\,dx\,dy$, 영역 $R$ |
| 평면 영역 문자 | 직사각형 $R$(15.1), 일반 영역 $D$ | $R$ |
| 입체 영역 문자 | $E$ (일반), $B$(직육면체); $D$는 $E$의 좌표평면 정사영 | $D$ |
| 면적소·플럭스 | $dS$; $\displaystyle\iint_S \mathbf F\cdot d\mathbf S=\iint_S\mathbf F\cdot\mathbf n\,dS$ | $d\sigma$, $\iint\mathbf F\cdot\mathbf n\,d\sigma$ |
| 회전·발산 | $\operatorname{curl}\mathbf F$, $\operatorname{div}\mathbf F$ (병기: $\nabla\times\mathbf F$, $\nabla\cdot\mathbf F$) | $\nabla\times\mathbf F$만 |
| 라플라시안 | $\nabla^2 f=\operatorname{div}(\nabla f)$ | — |
| 구면좌표 | $(\rho,\theta,\phi)$, $dV=\rho^2\sin\phi\,d\rho\,d\theta\,d\phi$ ($\phi$: 양의 $z$축에서 잰 각, $0\le\phi\le\pi$) | $(\rho,\phi,\theta)$, $d\rho\,d\phi\,d\theta$ |
| 원기둥좌표 | $(r,\theta,z)$, $dV=r\,dz\,dr\,d\theta$ | 동일(용어 "원통좌표계") |
| 영역 유형 | 평면: **제1형/제2형 영역**(Type I/II 병기), 입체: **제1형/제2형/제3형 입체**(type 1/2/3 병기) — 둘 다 아라비아숫자, 명사(영역/입체)로 구분. 로마숫자 "제I형" 금지 | 없음 |
| 야코비안 | $\dfrac{\partial(x,y)}{\partial(u,v)}$ | 동일 |
| 방향도함수 | $D_{\mathbf u}f(x_0,y_0)$, $\mathbf u=\langle a,b\rangle$ 단위벡터 | 동일 |
| 기울기 | $\nabla f=\langle f_x,f_y\rangle$ | $(f_x,f_y)$ |
| 편도함수 표기 | $f_x=\partial f/\partial x=f_1=D_1 f=D_x f$ (rem 카드로 소개) | $f_x$, $\partial f/\partial x$만 |
| 접평면 (그래프) | $z-z_0=f_x(x_0,y_0)(x-x_0)+f_y(x_0,y_0)(y-y_0)$ 우선; 등위면형은 14.6 | 등위면형만 |
| 법선 | 대칭방정식 $\dfrac{x-x_0}{F_x}=\dfrac{y-y_0}{F_y}=\dfrac{z-z_0}{F_z}$ + 매개변수식 | 매개변수식 |
| 선형화·전미분 | $L(x,y)$, $dz=f_x\,dx+f_y\,dy$, $\Delta z$ | $dV$만 |
| 라그랑주 | 목적 $f$, 제약 $g(x,y,z)=k$; $\nabla f=\lambda\nabla g$; 두 제약 $\nabla f=\lambda\nabla g+\mu\nabla h$ | 문자 혼용 |
| 평균값 | $f_{\text{avg}}$ | $\operatorname{Avg}(f)$ |
| 스칼라 정사영 | $\operatorname{comp}_{\mathbf a}\mathbf b$, 벡터 정사영 $\operatorname{proj}_{\mathbf a}\mathbf b$ | 기호 없음 |
| 곡선 향 반전 | $-C$ | 서술 |
| 이차곡면 표준형 | $z$축 대칭 6종 (Table 1): 쌍곡포물면 $\dfrac{z}{c}=\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}$ | $\dfrac{y^2}{b^2}-\dfrac{x^2}{a^2}=\dfrac zc$ |

## 3. 번역어 (Stewart 원어 → 한국어)
| English | 한국어 | 비고 |
|---|---|---|
| trace (of a surface) | 자취 | 좌표평면에 평행한 평면과의 교선 |
| cylinder / rulings | 주면 / 모선 | |
| quadric surface | 이차곡면 | |
| ellipsoid / elliptic paraboloid / hyperbolic paraboloid / cone / hyperboloid of one (two) sheet(s) | 타원면 / 타원포물면 / 쌍곡포물면 / 원뿔면 / 일엽(이엽)쌍곡면 | "타원형 포물면" 대신 **타원포물면** |
| function of two (several) variables | 이변수(다변수) 함수 | |
| domain / range | 정의역 / 치역 | |
| level curve / contour map / level surface | 등위선 / 등고선 지도 | 등위면 |
| limit / continuous | 극한 / 연속 | ε-δ: 임의의 $\varepsilon>0$에 대해 … $\delta>0$이 존재 |
| Squeeze Theorem | 조임정리 | |
| partial derivative / second partial derivative / mixed partial derivative | 편도함수 / 이계 편도함수 / 혼합 편도함수 | |
| Clairaut's Theorem | 클레로 정리 | "Clairaut 정리" 병기 가능 |
| partial differential equation / Laplace's equation / wave equation / heat equation | 편미분방정식 / 라플라스 방정식 / 파동방정식 / 열방정식 | |
| harmonic function | 조화함수 | |
| tangent plane / normal line | 접평면 / 법선 | |
| linear approximation / linearization / differentiable / differential (total differential) / increment | 선형근사 / 선형화 / 미분가능 / 미분(전미분) / 증분 | $dz$ = 미분, $\Delta z$ = 증분 |
| Chain Rule / intermediate variable / tree diagram | 연쇄법칙 / 중간변수 / 수형도 | |
| implicit differentiation / Implicit Function Theorem | 음함수 미분법 / 음함수 정리 | |
| directional derivative / gradient (vector) | 방향도함수 / 기울기 벡터 | "그래디언트" 금지 |
| local (absolute) maximum / minimum | 극댓값·극솟값 (최댓값·최솟값) | local = 극, absolute = 최 |
| critical point / saddle point / Second Derivatives Test | 임계점 / 안장점 / 이계도함수 판정법 | |
| closed set / bounded set / boundary point / Extreme Value Theorem | 닫힌집합 / 유계집합 / 경계점 / 극값정리 | |
| Lagrange multiplier / constraint | 라그랑주 승수 / 제약조건 | |
| double integral / iterated integral / Fubini's Theorem / Midpoint Rule / Riemann sum | 이중적분 / 반복적분 / 푸비니 정리 / 중점법칙 / 리만합 | |
| partial integration (with respect to $y$) | ($y$에 관한) 편적분 | 한 변수만 적분(다른 변수는 상수). "부분적분"(integration by parts)과 구별 |
| type I (II) region / type 1 (2, 3) solid | 평면: 제1형(제2형) 영역 — "Type I" 병기 | 입체: 제1형(제2형, 제3형) 입체 — "type 1" 병기 |
| polar rectangle | 극좌표 직사각형 | |
| density / mass / moment / center of mass / moment of inertia / radius of gyration / lamina | 밀도 / 질량 / 모멘트 / 질량중심 / 관성모멘트 / 회전반지름 / 얇은 판 | |
| joint density function / expected value | 결합확률밀도함수 / 기댓값 | |
| surface area | 곡면 넓이 | "겉넓이"도 허용 |
| triple integral / cylindrical coordinates / spherical coordinates / spherical wedge | 삼중적분 / 원기둥좌표 / 구면좌표 / 구면 쐐기 | "원통좌표계" 금지 |
| transformation / image / one-to-one / Jacobian / change of variables | 변환 / 상 / 일대일 / 야코비안 / 변수변환 | |
| vector field / gradient field / conservative vector field / potential function | 벡터장 / 기울기 벡터장 / 보존적 벡터장 / 퍼텐셜 함수 | "잠재함수" 금지 |
| line integral (with respect to arc length / x / y) | (호의 길이·$x$·$y$에 관한) 선적분 | |
| work / orientation / piecewise-smooth curve | 일 / 향 / 조각적으로 매끄러운 곡선 | |
| Fundamental Theorem for Line Integrals / independence of path / closed curve / simple curve / simply-connected region / open region / connected region | 선적분의 기본정리 / 경로 독립 / 닫힌곡선 / 단순곡선 / 단순연결영역 / 열린 영역 / 연결 영역 | |
| conservation of energy / kinetic (potential) energy | 에너지 보존 / 운동(퍼텐셜) 에너지 | |
| Green's Theorem / positive orientation | 그린 정리 / 양의 향 (반시계 방향) | |
| curl / divergence / irrotational / incompressible | 회전 / 발산 / 비회전 / 비압축 | "컬·다이버전스" 금지 |
| parametric surface / grid curves / smooth surface / surface of revolution | 매개곡면 / 격자곡선 / 매끄러운 곡면 / 회전면 | |
| surface integral / oriented surface / orientable surface / Möbius strip / closed surface / outward normal | 면적분 / 유향곡면(향이 정해진) / 가향곡면(향을 줄 수 있는) / 뫼비우스 띠 / 닫힌곡면 / 바깥 법선 | orientable=가향, oriented=유향으로 구분 |
| flux / heat flow / electric flux / Gauss's Law | 플럭스 / 열류 / 전기다발 / 가우스 법칙 | "유출" 금지 (플럭스로 통일) |
| Stokes' Theorem / boundary curve / circulation | 스토크스 정리 / 경계곡선 / 순환 | |
| Divergence Theorem (Gauss's Theorem) / simple solid region / source / sink | 발산정리 (가우스 정리) / 단순 입체 영역 / 원천 / 흡입 | |

## 4. 금칙어 (grep 대상)
- KO: 잠재함수 → **퍼텐셜 함수**; 유출 → **플럭스**; 원통좌표(계) → **원기둥좌표**; 타원형 포물면 → **타원포물면**; 컬·다이버전스·그래디언트; 순환밀도·발산밀도(Thomas 용어) 사용 금지.
- 수식: `d\sigma` 금지(→ `dS`); 성분 `M\mathbf{i}+N\mathbf{j}` 금지(→ `P,Q,R`); `\iiint_D` 금지(→ `\iiint_E`); 구면좌표 `d\rho\,d\phi\,d\theta` 순서 금지(→ `d\rho\,d\theta\,d\phi`).
- EN: Stoke's → **Stokes'**; Green theorem → **Green's Theorem**; Fubini theorem → **Fubini's Theorem**.

## 5. 절 파일명·제목
| 파일 | § | 한국어 제목 | English |
|---|---|---|---|
| s12-6 | 12.6 | 주면과 이차곡면 | Cylinders and Quadric Surfaces |
| s14-1 | 14.1 | 다변수함수 | Functions of Several Variables |
| s14-2 | 14.2 | 극한과 연속 | Limits and Continuity |
| s14-3 | 14.3 | 편도함수 | Partial Derivatives |
| s14-4 | 14.4 | 접평면과 선형근사 | Tangent Planes and Linear Approximations |
| s14-5 | 14.5 | 연쇄법칙 | The Chain Rule |
| s14-6 | 14.6 | 방향도함수와 기울기 벡터 | Directional Derivatives and the Gradient Vector |
| s14-7 | 14.7 | 최댓값과 최솟값 | Maximum and Minimum Values |
| s14-8 | 14.8 | 라그랑주 승수법 | Lagrange Multipliers |
| s15-1 | 15.1 | 직사각형 위의 이중적분 | Double Integrals over Rectangles |
| s15-2 | 15.2 | 일반 영역 위의 이중적분 | Double Integrals over General Regions |
| s15-3 | 15.3 | 극좌표에서의 이중적분 | Double Integrals in Polar Coordinates |
| s15-4 | 15.4 | 이중적분의 응용 | Applications of Double Integrals |
| s15-5 | 15.5 | 곡면 넓이 | Surface Area |
| s15-6 | 15.6 | 삼중적분 | Triple Integrals |
| s15-7 | 15.7 | 원기둥좌표에서의 삼중적분 | Triple Integrals in Cylindrical Coordinates |
| s15-8 | 15.8 | 구면좌표에서의 삼중적분 | Triple Integrals in Spherical Coordinates |
| s15-9 | 15.9 | 중적분의 변수변환 | Change of Variables in Multiple Integrals |
| s16-1 | 16.1 | 벡터장 | Vector Fields |
| s16-2 | 16.2 | 선적분 | Line Integrals |
| s16-3 | 16.3 | 선적분의 기본정리 | The Fundamental Theorem for Line Integrals |
| s16-4 | 16.4 | 그린 정리 | Green's Theorem |
| s16-5 | 16.5 | 회전과 발산 | Curl and Divergence |
| s16-6 | 16.6 | 매개곡면과 그 넓이 | Parametric Surfaces and Their Areas |
| s16-7 | 16.7 | 면적분 | Surface Integrals |
| s16-8 | 16.8 | 스토크스 정리 | Stokes' Theorem |
| s16-9 | 16.9 | 발산정리 | The Divergence Theorem |
| s16-10 | 16.10 | 요약 | Summary |
