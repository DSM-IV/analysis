# §14.3 Partial Derivatives — PDF p.1036–1048 (인쇄 p.999–1011)

- 본문(개념 + 예제): PDF p.1036(하단)–1044(상단) / 연습문제 1–101: PDF p.1044–1048 / Discovery Project(Cobb‑Douglas): PDF p.1048– → **인벤토리 제외**
- 예제 10개(Example 1–10), 번호 공식 (1)–(5), 정리 1개(Clairaut), 이름 붙은 박스 3개(Definition 4 / Notations / Rule)

## A. 카드 인벤토리 (원문 순서)

| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입, Table 1) | 편도함수의 동기 — 체감온도 / Motivating Partial Derivatives | 체감온도 $I=f(T,H)$ 표에서 한 변수를 고정. $H=70$ 고정 → $g(T)=f(T,70)$, 차분 $\frac{f(98,70)-f(96,70)}{2}=4$, $\frac{f(94,70)-f(96,70)}{-2}=3.5$ 를 평균해 $g'(96)\approx 3.75$; $T=96$ 고정 → $G(H)=f(96,H)$, $\frac{130-125}{5}=1$, $\frac{121-125}{-5}=0.8$ 평균해 $G'(70)\approx0.9$. 즉 $f_T(96,70)\approx3.75$, $f_H(96,70)\approx0.9$ (°F당·%당 체감온도 상승률) | 1036–1037 | — | 표(Table 1) 재현 |
| 2 | def | 식 (1)(2)(3) | 한 점에서의 편도함수 / Partial Derivatives at a Point | $y=b$ 고정 시 $g(x)=f(x,b)$ 로 두면 (1) $f_x(a,b)=g'(a)$. 극한 형태로 (2) $f_x(a,b)=\lim_{h\to0}\frac{f(a+h,b)-f(a,b)}{h}$, (3) $f_y(a,b)=\lim_{h\to0}\frac{f(a,b+h)-f(a,b)}{h}$ | 1037–1038 | — | — |
| 3 | def | Definition 4 | 편도함수 (함수로서) / Partial Derivatives (as functions) | $f_x(x,y)=\lim_{h\to0}\frac{f(x+h,y)-f(x,y)}{h}$, $f_y(x,y)=\lim_{h\to0}\frac{f(x,y+h)-f(x,y)}{h}$ — 점 $(a,b)$ 를 움직이면 $f_x,f_y$ 자체가 2변수 함수 | 1038 | — | — |
| 4 | rem | Notations 박스 | 편도함수의 표기 / Notations for Partial Derivatives | $z=f(x,y)$ 일 때 $f_x=\frac{\partial f}{\partial x}=\frac{\partial}{\partial x}f(x,y)=\frac{\partial z}{\partial x}=f_1=D_1f=D_xf$, $f_y$ 도 동일. 주의: $\partial f/\partial x$ 는 미분(differential)의 비로 해석할 수 없음 | 1038 | — | — |
| 5 | rem | Rule 박스 | 편도함수 계산 규칙 / Rule for Finding Partial Derivatives | $f_x$ 는 $y$ 를 상수로 보고 $x$ 로 보통 미분, $f_y$ 는 $x$ 를 상수로 보고 $y$ 로 보통 미분 | 1038 | — | — |
| 6 | note | Interpretations of Partial Derivatives | 기하적 해석 — 자취 곡선의 접선 기울기 / Geometric Interpretation | $z=f(x,y)$ 의 그래프 $S$ 위의 점 $P(a,b,c)$. 평면 $y=b$ 가 자르는 자취 $C_1$ 은 $g(x)=f(x,b)$ 의 그래프이므로 접선 $T_1$ 의 기울기는 $g'(a)=f_x(a,b)$; 평면 $x=a$ 의 자취 $C_2$ 는 $G(y)=f(a,y)$ 의 그래프로 $T_2$ 의 기울기는 $G'(b)=f_y(a,b)$ | 1039 | — | Figure 1 |
| 7 | fig | Figure 1 | 자취와 접선 / Traces and Tangent Lines | 곡면 $S$, 두 수직평면 $y=b$·$x=a$ 의 자취 $C_1,C_2$, 점 $P(a,b,c)$ 와 접선 $T_1,T_2$ (밑면에 $(a,b,0)$) | 1039 | — | 자체 SVG |
| 8 | note | (Fig 2·3 뒤 단락) | 변화율로서의 해석 / Interpretation as Rates of Change | $z=f(x,y)$ 에서 $\partial z/\partial x$ 는 $y$ 를 고정했을 때 $z$ 의 $x$ 에 대한 변화율, $\partial z/\partial y$ 는 $x$ 고정 시 $y$ 에 대한 변화율 (절 도입의 체감온도 예가 그 사례) | 1040 | — | — |
| 9 | def | Functions of Three or More Variables | 3변수 이상 함수의 편도함수 / Partial Derivatives of Functions of Three or More Variables | $f_x(x,y,z)=\lim_{h\to0}\frac{f(x+h,y,z)-f(x,y,z)}{h}$ ($y,z$ 를 상수 취급). 일반적으로 $u=f(x_1,\dots,x_n)$ 이면 $\frac{\partial u}{\partial x_i}=\lim_{h\to0}\frac{f(x_1,\dots,x_i+h,\dots,x_n)-f(x_1,\dots,x_n)}{h}=f_{x_i}=f_i=D_if$. $w=f(x,y,z)$ 의 $f_x$ 는 변화율로는 해석되나, 그래프가 4차원에 있어 기하적 해석은 불가 | 1041 | — | — |
| 10 | def | Higher Derivatives | 이계·고계 편도함수와 표기 / Second and Higher Partial Derivatives | $(f_x)_x=f_{xx}=f_{11}=\frac{\partial^2f}{\partial x^2}=\frac{\partial^2z}{\partial x^2}$, $(f_x)_y=f_{xy}=f_{12}=\frac{\partial^2 f}{\partial y\,\partial x}$, $(f_y)_x=f_{yx}=f_{21}=\frac{\partial^2f}{\partial x\,\partial y}$, $(f_y)_y=f_{yy}=f_{22}=\frac{\partial^2f}{\partial y^2}$. 첨자 $f_{xy}$ 는 **$x$ 먼저, 그다음 $y$**, $\partial^2f/\partial y\,\partial x$ 도 같은 순서(안쪽이 먼저) | 1042 | — | — |
| 11 | thm | Clairaut's Theorem | 클레로 정리 / Clairaut's Theorem | 점 $(a,b)$ 를 포함하는 원판 $D$ 에서 $f$ 가 정의되고 $f_{xy},f_{yx}$ 가 $D$ 에서 모두 연속이면 $f_{xy}(a,b)=f_{yx}(a,b)$ | 1042 | Appendix F (본문에 없음) | — |
| 12 | rem | (Clairaut 뒤 단락) | 3계 이상 편도함수 / Higher‑Order Mixed Partials | $f_{xyy}=(f_{xy})_y=\frac{\partial}{\partial y}\left(\frac{\partial^2f}{\partial y\,\partial x}\right)=\frac{\partial^3f}{\partial y^2\,\partial x}$ 처럼 3계 이상도 정의되며, 연속이면 Clairaut 정리로 $f_{xyy}=f_{yxy}=f_{yyx}$ | 1042 | — | — |
| 13 | def | Partial Differential Equations / Laplace's equation | 라플라스 방정식과 조화함수 / Laplace's Equation and Harmonic Functions | 물리 법칙은 편미분방정식(PDE)으로 표현됨. $\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}=0$ 을 라플라스 방정식이라 하고 그 해를 **조화함수(harmonic function)** 라 함 — 열전도·유체흐름·전위 문제에 등장 | 1043 | — | — |
| 14 | def | The wave equation | 파동방정식 / The Wave Equation | $\frac{\partial^2u}{\partial t^2}=a^2\frac{\partial^2u}{\partial x^2}$. 파형(해파·음파·광파·진동하는 줄)의 운동을 기술하며, $u(x,t)$ 가 시각 $t$·한쪽 끝에서 거리 $x$ 인 지점의 변위일 때 성립. 상수 $a$ 는 줄의 밀도와 장력에 의존 | 1043 | — | Figure 5 |
| 15 | rem | 식 (5) | 3차원 라플라스 방정식 / Three‑Dimensional Laplace Equation | (5) $\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}+\frac{\partial^2u}{\partial z^2}=0$. 지구물리 응용: $u(x,y,z)$ 가 자기장 세기이면 (5)를 만족하며, 그 분포가 철 성분 광물 분포·암석 종류·단층 위치를 반영 | 1044 | — | — |

카드 수: **note 3, def 6, thm 1, rem 4, fig 1 = 15**

## B. 예제 기준값

| Example | PDF 쪽 | 유형 | 문제 요지 (영어 재서술) | 교재 최종답 (TeX) | 독립 재계산 (sympy) | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1039 | 계산 | For the polynomial $f(x,y)=x^3+x^2y^3-2y^2$, evaluate both first partials at the point $(2,1)$. | $f_x=3x^2+2xy^3$, $f_x(2,1)=16$; $f_y=3x^2y^2-4y$, $f_y(2,1)=8$ | $f_x=3x^2+2xy^3\to16$; $f_y=3x^2y^2-4y\to8$ | ✅ | — |
| 2 | 1039 | 계산 | Differentiate the composite $f(x,y)=\sin\!\big(x/(1+y)\big)$ with respect to each variable, using the one‑variable Chain Rule. | $\dfrac{\partial f}{\partial x}=\cos\!\Big(\dfrac{x}{1+y}\Big)\cdot\dfrac{1}{1+y}$; $\dfrac{\partial f}{\partial y}=-\cos\!\Big(\dfrac{x}{1+y}\Big)\cdot\dfrac{x}{(1+y)^2}$ | 동일 | ✅ | — |
| 3 | 1039–1040 | 계산 + 해석 | For the paraboloid $f(x,y)=4-x^2-2y^2$, compute the two first partials at $(1,1)$ and read them as slopes of tangent lines to the traces through $(1,1,1)$. | $f_x=-2x$, $f_x(1,1)=-2$; $f_y=-4y$, $f_y(1,1)=-4$. 자취: 평면 $y=1$ 에서 포물선 $z=2-x^2$ 의 $(1,1,1)$ 접선 기울기 $-2$; 평면 $x=1$ 에서 포물선 $z=3-2y^2$ 의 접선 기울기 $-4$ (둘 다 양의 방향으로 하강) | $f_x=-2x\to-2$, $f_y=-4y\to-4$; 자취 $z|_{y=1}=2-x^2$, $z|_{x=1}=3-2y^2$ | ✅ | Figure 2·3 |
| 4 | 1040 | 해석·응용 | With BMI modeled by $B(m,h)=m/h^{2}$ ($m$ in kg, $h$ in m), find both partials and interpret them numerically for $m=64$, $h=1.68$. | $\dfrac{\partial B}{\partial m}=\dfrac{1}{h^2}$, $\dfrac{\partial B}{\partial m}(64,1.68)\approx0.35\ \mathrm{(kg/m^2)/kg}$; $\dfrac{\partial B}{\partial h}=-\dfrac{2m}{h^3}$, $\dfrac{\partial B}{\partial h}(64,1.68)\approx-27\ \mathrm{(kg/m^2)/m}$. 해석: 체중 1 kg 증가 시 $B(64,1.68)\approx22.68$ 에서 약 $0.35$ 증가; 키 1 cm 증가 시 약 $27(0.01)=0.27$ 감소 | $1/h^2=0.354308$, $-2m/h^3=-26.9949$, $B=22.6757$ | ✅ | 교재의 $\approx0.35,\ \approx-27,\ \approx22.68$ 은 모두 반올림 |
| 5 | 1041 | 계산 (음함수) | The equation $x^3+y^3+z^3+6xyz+4=0$ defines $z$ implicitly as a function of $x,y$; find both partials and evaluate them at $(-1,1,2)$. | $\dfrac{\partial z}{\partial x}=-\dfrac{x^2+2yz}{z^2+2xy}$, $\dfrac{\partial z}{\partial y}=-\dfrac{y^2+2xz}{z^2+2xy}$; 점 $(-1,1,2)$ 에서 $\dfrac{\partial z}{\partial x}=-\dfrac52$, $\dfrac{\partial z}{\partial y}=\dfrac32$ | 두 방법 일치 — (A) $F(x,y,Z(x,y))=0$ 직접 미분, (B) $-F_x/F_z,\ -F_y/F_z$; 값 $-5/2$, $3/2$ ($F(-1,1,2)=0$ 확인) | ✅ | Figure 4(음함수 곡면 플롯)은 참고용 |
| 6 | 1041 | 계산 | Compute all three first partials of $f(x,y,z)=e^{xy}\ln z$. | $f_x=ye^{xy}\ln z$, $f_y=xe^{xy}\ln z$, $f_z=\dfrac{e^{xy}}{z}$ | 동일 | ✅ | $z>0$ |
| 7 | 1042 | 계산 | Find all four second partials of the Example 1 function $f(x,y)=x^3+x^2y^3-2y^2$. | $f_{xx}=6x+2y^3$, $f_{xy}=6xy^2$, $f_{yx}=6xy^2$, $f_{yy}=6x^2y-4$ | 동일 ($f_{xy}=f_{yx}$ 확인) | ✅ | Clairaut 정리의 예시로 이어짐 |
| 8 | 1043 | 계산 | For $f(x,y,z)=\sin(3x+yz)$, compute the fourth‑order mixed partial $f_{xxyz}$. | $f_x=3\cos(3x+yz)$, $f_{xx}=-9\sin(3x+yz)$, $f_{xxy}=-9z\cos(3x+yz)$, $f_{xxyz}=-9\cos(3x+yz)+9yz\sin(3x+yz)$ | $9\big(yz\sin(3x+yz)-\cos(3x+yz)\big)$ — 동일 | ✅ | — |
| 9 | 1043 | 증명(show) | Verify that $u(x,y)=e^{x}\sin y$ is harmonic, i.e. satisfies Laplace's equation. | $u_{xx}=e^x\sin y$, $u_{yy}=-e^x\sin y$ 이므로 $u_{xx}+u_{yy}=0$ — 라플라스 방정식의 해 | $u_{xx}+u_{yy}=0$ | ✅ | — |
| 10 | 1043 | 증명(show) | Verify that the traveling wave $u(x,t)=\sin(x-at)$ satisfies the wave equation $u_{tt}=a^2u_{xx}$. | $u_{xx}=-\sin(x-at)$, $u_{tt}=-a^2\sin(x-at)=a^2u_{xx}$ — 파동방정식의 해 | $u_{tt}-a^2u_{xx}=0$ | ✅ | — |

**anchor 불일치: 0건** (재계산 스크립트 `/Users/chalrs/analysis/stewart/inventory/anchor-14.3.py`, 절 도입의 표 기반 추정치 $f_T(96,70)=3.75$·$f_H(96,70)=0.9$ 도 재현 확인)

## C. 그림 필요 목록 (자체 SVG)

| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 1 (p.1039) | 곡면 $S$ 와 수직평면 $y=b$, $x=a$ 의 자취 $C_1,C_2$, 점 $P(a,b,c)$, 접선 $T_1,T_2$, 밑점 $(a,b,0)$ | **필수** — 절의 핵심 기하 해석 | 7 |
| Table 1 (p.1036) | 체감온도 표 ($T=90\!-\!100$ °F × $H=50\!-\!90$ %), $T=96$ 행·$H=70$ 열 강조 | **필수** (SVG가 아닌 HTML 표로 재현; 수치는 공개 NWS 자료 성격) | 1 |
| Figure 2·3 (p.1040) | $z=4-x^2-2y^2$ 와 평면 $y=1$ / $x=1$ 의 자취 포물선, 점 $(1,1,1)$ | 선택 (Example 3 이해를 크게 도움 — 하나의 2‑패널 SVG 권장) | Example 3 |
| Figure 4 (p.1041) | $x^3+y^3+z^3+6xyz+4=0$ 음함수 곡면과 점 $(-1,1,2)$ | 선택 (재현 난도 높음, 생략 가능) | Example 5 |
| Figure 5 (p.1043) | 진동하는 줄의 변위 $u(x,t)$ 스케치 | 선택 (간단한 곡선 1개 — 저비용, 권장) | 14 |

## D. ERRATA·판독 불확실

- pdftotext 산출물에서 §14.3 시작 직전(PDF p.1036 좌측)에 **§14.2 연습문제 45–59**가 섞여 들어온다. 절 텍스트 앞부분을 그대로 쓰면 안 됨 — §14.3 본문은 "14.3 Partial Derivatives / Partial Derivatives of Functions of Two Variables" 헤더부터 시작.
- pdftotext 인코딩 특성상 `−`는 `=`, 숫자 `2`는 종종 `−`(마이너스)로 나온다(예: 원문 `fx sx, yd − 22x` = $f_x(x,y)=-2x$). 본 인벤토리의 모든 수식은 PDF p.1036·1038·1039·1041·1042·1043 PNG를 직접 확인해 확정했다.
- Definition 4 박스의 라벨이 `Definitio`로 잘리는 것은 pdftotext 아티팩트이며 원문은 **Definition**.
- 판독 불확실 항목: **없음**.

## E. 절 요약 (사이트 도입 note 초안)

여러 변수의 함수에서 한 변수만 남기고 나머지를 상수로 고정하면 익숙한 1변수 미분을 그대로 쓸 수 있고, 이렇게 얻은 도함수가 편도함수다. 체감온도 표에서 습도를 70 %로 고정한 채 온도만 바꿔 보면 기울기 $f_T(96,70)\approx3.75$ 가 나오는데, 이것이 편도함수의 원래 의미 — "다른 변수를 붙잡아 둔 채의 변화율" — 를 그대로 보여 준다. 기하적으로 $f_x(a,b)$ 와 $f_y(a,b)$ 는 곡면 $z=f(x,y)$ 를 수직평면 $y=b$, $x=a$ 로 자른 자취 곡선의 접선 기울기이며, 계산 규칙은 "미분하지 않는 변수는 상수로 취급"이 전부여서 연쇄법칙·음함수 미분도 1변수 때와 똑같이 쓰인다. 편도함수를 다시 미분한 이계 편도함수에서는 미분 순서가 문제가 되는데, 혼합편도 $f_{xy}$ 와 $f_{yx}$ 가 연속이면 두 값이 같다는 것이 클레로 정리다. 마지막으로 라플라스 방정식 $u_{xx}+u_{yy}=0$ 과 파동방정식 $u_{tt}=a^2u_{xx}$ 처럼 물리 법칙을 담은 편미분방정식이 등장하며, 주어진 함수가 그 해인지 확인하는 것도 편도함수 계산으로 끝난다.

## F. 공통과제 문항 (§14.3)

- **과제 제출 문항**: 23, 26, 44, 50, 60, 67 — *풀이 게재 금지*(계획서 규정)
- **학습 참고 문항**: 9\~36, 37\~40, 41\~44, 45\~46, 47\~52, 53\~56, 57\~64, 65\~66, 68, 101(b), (c), (d)
