# §16.7 Surface Integrals — PDF p.1257–1269 (인쇄 p.1220–1232)

본문 p.1257(하단)–1267(상단), 연습문제 p.1267–1269. 예제 **6개**(PLAN.md의 "5"는 과소 집계 — D 참조).

## A. 카드 인벤토리 (원문 순서)

| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입) | 곡면적분이란 / What a Surface Integral Is | 선적분:호길이 = 곡면적분:곡면넓이. 세 변수 함수 $f$의 정의역이 곡면 $S$를 포함할 때, $f\equiv1$이면 값이 $S$의 넓이가 되도록 $\iint_S f\,dS$를 정의한다. 매개곡면을 먼저 다루고 그래프꼴 $z=g(x,y)$는 특수한 경우로 처리 | 1257–1258 | — | — |
| 2 | note | (본문, Figure 1) | 패치 분할과 리만 합 / Patches and the Riemann Sum | $D$를 소사각형 $R_{ij}$($\Delta u\times\Delta v$)로 나누면 $S$가 패치 $S_{ij}$로 나뉜다. 각 패치의 점 $P_{ij}^*$에서 $f$를 재고 패치 넓이 $\Delta S_{ij}$를 곱해 $\sum_i\sum_j f(P_{ij}^*)\,\Delta S_{ij}$ 를 만든다 | 1258 | — | Fig 1 |
| 3 | def | Definition (1) | 곡면적분 / Surface Integral | (1) $\displaystyle\iint_S f(x,y,z)\,dS=\lim_{m,n\to\infty}\sum_{i=1}^{m}\sum_{j=1}^{n}f(P_{ij}^*)\,\Delta S_{ij}$. 선적분 정의 (16.2.2), 이중적분 정의 (15.1.5)와 같은 꼴 | 1258 | — | — |
| 4 | thm | Equation (2) | 매개곡면 위의 계산 공식 / Evaluating over a Parametric Surface | 패치 넓이를 접평면의 평행사변형 $\Delta S_{ij}\approx|\mathbf r_u\times\mathbf r_v|\,\Delta u\,\Delta v$ 로 근사하면, 성분이 연속이고 $\mathbf r_u,\mathbf r_v$가 $D$ 내부에서 $\mathbf 0$이 아니고 평행하지 않을 때 (2) $\displaystyle\iint_S f(x,y,z)\,dS=\iint_D f(\mathbf r(u,v))\,|\mathbf r_u\times\mathbf r_v|\,dA$. 여백: $S$가 꼭 한 번만 덮인다고 가정하며, 적분값은 **매개화에 무관** | 1258 | 정의 1에서 유도(개요) | — |
| 5 | rem | (본문, (2) 뒤) | 선적분과의 대응, 넓이의 회수 / Analogy and $\iint_S 1\,dS$ | $\int_C f\,ds=\int_a^b f(\mathbf r(t))|\mathbf r'(t)|\,dt$ 와 같은 구조. 또 $\iint_S 1\,dS=\iint_D|\mathbf r_u\times\mathbf r_v|\,dA=A(S)$. 사용 시 $f(\mathbf r(u,v))$ 는 $f$의 식에 $x=x(u,v)$ 등을 대입해 얻는다 | 1259 | — | — |
| 6 | thm | (무번호 공식, 응용) | 얇은 판의 질량과 질량중심 / Mass and Center of Mass | 밀도(단위넓이당 질량) $\rho(x,y,z)$인 얇은 판 $S$의 질량 $m=\iint_S\rho\,dS$, 질량중심 $(\bar x,\bar y,\bar z)$ 는 $\bar x=\frac1m\iint_S x\rho\,dS$, $\bar y=\frac1m\iint_S y\rho\,dS$, $\bar z=\frac1m\iint_S z\rho\,dS$. 관성모멘트도 같은 방식(연습 41) | 1259 | — | — |
| 7 | thm | Equations (3), (4) | 그래프 위의 곡면적분 / Surface Integrals over Graphs | $z=g(x,y)$ 를 $x,y$로 매개화하면 $\mathbf r_x=\mathbf i+g_x\mathbf k$, $\mathbf r_y=\mathbf j+g_y\mathbf k$, (3) $\mathbf r_x\times\mathbf r_y=-\frac{\partial g}{\partial x}\mathbf i-\frac{\partial g}{\partial y}\mathbf j+\mathbf k$, $|\mathbf r_x\times\mathbf r_y|=\sqrt{\left(\frac{\partial z}{\partial x}\right)^2+\left(\frac{\partial z}{\partial y}\right)^2+1}$, 따라서 (4) $\displaystyle\iint_S f\,dS=\iint_D f(x,y,g(x,y))\sqrt{\left(\frac{\partial z}{\partial x}\right)^2+\left(\frac{\partial z}{\partial y}\right)^2+1}\,dA$ | 1260 | 본문((2)의 특수화) | — |
| 8 | rem | (본문, (4) 뒤) | 다른 좌표평면으로의 정사영 / Projecting onto $yz$- or $xz$-plane | $S:\ y=h(x,z)$ 이고 $D$가 $xz$-평면으로의 정사영이면 $\displaystyle\iint_S f\,dS=\iint_D f(x,h(x,z),z)\sqrt{\left(\frac{\partial y}{\partial x}\right)^2+\left(\frac{\partial y}{\partial z}\right)^2+1}\,dA$; $x=k(y,z)$ 도 마찬가지 | 1260 | — | — |
| 9 | def | (본문 정의) | 조각별 매끄러운 곡면 위의 적분 / Piecewise-Smooth Surfaces | $S$가 경계에서만 만나는 매끄러운 조각 $S_1,\dots,S_n$의 합집합이면 $\displaystyle\iint_S f\,dS=\iint_{S_1}f\,dS+\cdots+\iint_{S_n}f\,dS$ | 1260 | — | — |
| 10 | note | (Oriented Surfaces 도입) | 비가향 곡면: 뫼비우스 띠 / Nonorientable: the Möbius Strip | 벡터장의 곡면적분을 정의하려면 뫼비우스 띠 같은 **비가향** 곡면을 배제해야 한다. 긴 직사각 종이를 반 바퀴 꼬아 짧은 변을 붙이면 만들어진다. 점 $P$에서 출발한 개미가 모서리를 넘지 않고 "반대쪽"을 거쳐 $P$로 돌아오므로 면이 **하나뿐**이다(연습 16.6.32에 매개방정식) | 1262 | — | Fig 4, 5 |
| 11 | fig | Figures 4, 5 | 뫼비우스 띠 / Möbius Strip | 반 바퀴 꼬아 $A\!-\!D$, $B\!-\!C$ 를 붙이는 구성 도해와 완성된 띠 | 1262 | — | 필수 |
| 12 | def | (본문 정의) | 유향곡면 / Oriented Surface | 경계점을 제외한 모든 점에서 접평면을 갖는 곡면에는 단위법선 $\mathbf n_1$ 과 $\mathbf n_2=-\mathbf n_1$ 둘이 있다. $S$ 위에서 **연속적으로 변하는** 단위법선 $\mathbf n$을 고를 수 있으면 $S$를 **유향곡면(oriented surface)**, 그 선택을 **방향(orientation)** 이라 한다. 가향곡면의 방향은 정확히 두 가지 | 1262 | — | Fig 6, 7 |
| 13 | fig | Figures 6, 7 | 가향곡면의 두 방향 / Two Orientations | 한 점의 $\mathbf n_1,\mathbf n_2=-\mathbf n_1$, 그리고 곡면 전체에 연속적으로 배치된 두 가지 법선장 | 1262 | — | 필수 |
| 14 | thm | Equation (5) | 그래프의 위쪽 방향 / Upward Orientation of a Graph | $z=g(x,y)$ 에서 식 (3)이 주는 자연스러운 방향은 (5) $\displaystyle\mathbf n=\frac{-\frac{\partial g}{\partial x}\mathbf i-\frac{\partial g}{\partial y}\mathbf j+\mathbf k}{\sqrt{1+\left(\frac{\partial g}{\partial x}\right)^2+\left(\frac{\partial g}{\partial y}\right)^2}}$. $\mathbf k$ 성분이 양수이므로 **위쪽 방향** | 1262 | — | — |
| 15 | thm | Equation (6) | 매개곡면이 유도하는 방향 / Orientation Induced by $\mathbf r(u,v)$ | 매끄러운 가향곡면 $S:\mathbf r(u,v)$ 는 (6) $\displaystyle\mathbf n=\frac{\mathbf r_u\times\mathbf r_v}{|\mathbf r_u\times\mathbf r_v|}$ 로 자동으로 방향이 정해지고, 반대 방향은 $-\mathbf n$ | 1262 | — | — |
| 16 | rem | (본문 예시 + 규약) | 구면의 양의 방향과 닫힌곡면 규약 / Positive Orientation of a Closed Surface | 구면 $\mathbf r(\phi,\theta)$ 에서 $\mathbf r_\phi\times\mathbf r_\theta=a^2\sin^2\!\phi\cos\theta\,\mathbf i+a^2\sin^2\!\phi\sin\theta\,\mathbf j+a^2\sin\phi\cos\phi\,\mathbf k$, $|\mathbf r_\phi\times\mathbf r_\theta|=a^2\sin\phi$ 이므로 $\mathbf n=\frac1a\mathbf r(\phi,\theta)$ — 위치벡터와 같은 방향, 즉 **바깥쪽**. 매개변수 순서를 바꾸면 $\mathbf r_\theta\times\mathbf r_\phi=-\mathbf r_\phi\times\mathbf r_\theta$ 로 안쪽. **닫힌곡면**(입체 $E$의 경계)의 규약: **바깥쪽 법선 = 양의 방향**, 안쪽 = 음의 방향 | 1263 | — | Fig 8, 9 |
| 17 | fig | Figures 8, 9 | 닫힌곡면의 양·음 방향 / Positive vs Negative Orientation | 구면 위 바깥쪽 법선장(양)과 안쪽 법선장(음) | 1263 | — | 필수 |
| 18 | note | (Flux 도입, Figures 10, 11) | 유체 흐름으로 본 플럭스 / Motivating Flux by Fluid Flow | 밀도 $\rho$, 속도장 $\mathbf v$ 인 유체가 (흐름을 막지 않는 그물 같은) 유향곡면 $S$를 지날 때, 단위넓이·단위시간당 흐름률은 벡터장 $\rho\mathbf v$. 패치 $S_{ij}$ 를 통과하는 질량률은 $(\rho\mathbf v\cdot\mathbf n)A(S_{ij})$ 로 근사되고, 합의 극한이 곡면적분이 된다 | 1263–1264 | — | Fig 10, 11 |
| 19 | thm | Equation (7) | 흐름률 / Rate of Flow | (7) $\displaystyle\iint_S\rho\mathbf v\cdot\mathbf n\,dS=\iint_S\rho(x,y,z)\,\mathbf v(x,y,z)\cdot\mathbf n(x,y,z)\,dS$ = $S$를 지나는 흐름률(단위시간당 질량). $\mathbf F=\rho\mathbf v$ 로 두면 $\iint_S\mathbf F\cdot\mathbf n\,dS$ | 1264 | — | — |
| 20 | def | Definition 8 | 벡터장의 곡면적분(플럭스) / Surface Integral of a Vector Field; Flux | 유향곡면 $S$(단위법선 $\mathbf n$) 위의 연속 벡터장 $\mathbf F$에 대해 (8) $\displaystyle\iint_S\mathbf F\cdot d\mathbf S=\iint_S\mathbf F\cdot\mathbf n\,dS$. 이를 $\mathbf F$의 $S$를 가로지르는 **플럭스(flux)** 라 한다. 즉 벡터장의 곡면적분 = **법선 성분**의 곡면적분 | 1264 | — | — |
| 21 | thm | Equation (9) | 매개곡면에서의 플럭스 계산 / Computing Flux from $\mathbf r(u,v)$ | 정의 8과 식 (2)·(6)에서 (9) $\displaystyle\iint_S\mathbf F\cdot d\mathbf S=\iint_D\mathbf F\cdot(\mathbf r_u\times\mathbf r_v)\,dA$, $D$는 매개변수영역. 식 (6)이 주는 방향을 가정하며 반대 방향이면 $-1$배. 여백: 선적분 $\int_C\mathbf F\cdot d\mathbf r=\int_a^b\mathbf F(\mathbf r(t))\cdot\mathbf r'(t)\,dt$ (16.2.13)와 대응 | 1264 | 본문 | — |
| 22 | thm | Equation (10) | 그래프 위의 플럭스 / Flux over $z=g(x,y)$ | $\mathbf F=P\mathbf i+Q\mathbf j+R\mathbf k$, $\mathbf F\cdot(\mathbf r_x\times\mathbf r_y)=-P\frac{\partial g}{\partial x}-Q\frac{\partial g}{\partial y}+R$ 이므로 (10) $\displaystyle\iint_S\mathbf F\cdot d\mathbf S=\iint_D\left(-P\frac{\partial g}{\partial x}-Q\frac{\partial g}{\partial y}+R\right)dA$. **위쪽 방향** 가정, 아래쪽이면 $-1$배. $y=h(x,z)$, $x=k(y,z)$ 형태도 유사(연습 37, 38) | 1265 | 본문 | — |
| 23 | rem | Equation (11) | 전기다발과 가우스 법칙 / Electric Flux and Gauss's Law | 전기장 $\mathbf E$에 대해 $\iint_S\mathbf E\cdot d\mathbf S$ 를 $S$를 통과하는 **전기다발**이라 한다. 정전기학의 가우스 법칙: 닫힌곡면 $S$가 둘러싼 순전하는 (11) $Q=\varepsilon_0\iint_S\mathbf E\cdot d\mathbf S$, 여기서 $\varepsilon_0$ 는 진공 유전율($\text{SI}$에서 $\varepsilon_0\approx8.8542\times10^{-12}\ \mathrm{C^2/N\cdot m^2}$) | 1266–1267 | — | — |
| 24 | thm | (무번호 공식, 응용) | 열류 / Heat Flow | 물체 안의 온도가 $u(x,y,z)$ 일 때 **열류 벡터장** 은 $\mathbf F=-K\nabla u$ ($K$ = 물질의 열전도도, 실험적 상수). $S$를 가로지르는 열 흐름률은 $\displaystyle\iint_S\mathbf F\cdot d\mathbf S=-K\iint_S\nabla u\cdot d\mathbf S$ | 1267 | — | — |

카드 수: **note 4, def 4, thm 9, rem 4, fig 3 — 합계 24**

## B. 예제 기준값

| Example | PDF 쪽 | 유형 | 문제 요지 (영어 재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1259 | 계산 | Compute $\iint_S x^2\,dS$ over the unit sphere $x^2+y^2+z^2=1$. | 구면좌표 매개화 $\mathbf r(\phi,\theta)$, $|\mathbf r_\phi\times\mathbf r_\theta|=\sin\phi$; $\iint_S x^2dS=\int_0^{2\pi}\!\cos^2\theta\,d\theta\int_0^{\pi}\!\sin^3\phi\,d\phi=\pi\cdot\frac43=\boxed{\dfrac{4\pi}{3}}$ | sympy: $4\pi/3$ | ✓ | $\cos^2\theta=\frac12(1+\cos2\theta)$, $\sin^2\phi=1-\cos^2\phi$ 사용 |
| 2 | 1260 | 계산 | Evaluate $\iint_S y\,dS$ where $S$ is the graph $z=x+y^2$ over $0\le x\le1$, $0\le y\le2$. | $z_x=1$, $z_y=2y$ → $dS=\sqrt{2+4y^2}\,dA$; $\iint_S y\,dS=\int_0^1\!dx\,\sqrt2\int_0^2 y\sqrt{1+2y^2}\,dy=\sqrt2\cdot\frac14\cdot\frac23(1+2y^2)^{3/2}\big|_0^2=\boxed{\dfrac{13\sqrt2}{3}}$ | sympy: $13\sqrt2/3\approx6.128258770$ | ✓ | 식 (4) 적용 |
| 3 | 1260–1261 | 계산 | Evaluate $\iint_S z\,dS$ where $S$ is the closed surface made of the cylinder side $S_1: x^2+y^2=1$, the bottom disk $S_2: x^2+y^2\le1$ in $z=0$, and the top $S_3$: the part of $z=1+x$ above $S_2$. | $S_1$: $\mathbf r(\theta,z)=(\cos\theta,\sin\theta,z)$, $|\mathbf r_\theta\times\mathbf r_z|=1$, $0\le z\le1+\cos\theta$ → $\iint_{S_1}z\,dS=\frac{3\pi}{2}$; $S_2$: $z=0$ → $0$; $S_3$: $dS=\sqrt2\,dA$ → $\sqrt2\,\pi$. 합 $=\boxed{\left(\frac32+\sqrt2\right)\pi}$ | sympy: $S_1=3\pi/2$, $S_2=0$, $S_3=\sqrt2\pi$, 합 $=\pi(3+2\sqrt2)/2\approx9.15527192$ | ✓ | 조각별 매끄러운 곡면 정의 사용; Fig 3은 축 배치를 바꿔 그린 것 |
| 4 | 1265 | 계산 | Find the flux of $\mathbf F(x,y,z)=z\,\mathbf i+y\,\mathbf j+x\,\mathbf k$ across the unit sphere (outward). | $\mathbf F(\mathbf r(\phi,\theta))\cdot(\mathbf r_\phi\times\mathbf r_\theta)=2\sin^2\phi\cos\phi\cos\theta+\sin^3\phi\sin^2\theta$; $\int_0^{2\pi}\cos\theta\,d\theta=0$ 이므로 첫 항은 사라지고 $\iint_S\mathbf F\cdot d\mathbf S=\int_0^{\pi}\!\sin^3\phi\,d\phi\int_0^{2\pi}\!\sin^2\theta\,d\theta=\frac43\cdot\pi=\boxed{\dfrac{4\pi}{3}}$ | sympy: $4\pi/3$ | ✓ | 밀도 1의 속도장으로 보면 단위시간당 통과 질량 $4\pi/3$. 가우스 법칙(11)을 적용하면 $Q=\frac43\pi\varepsilon_0$ (p.1267) |
| 5 | 1266 | 계산 | Evaluate $\iint_S\mathbf F\cdot d\mathbf S$ for $\mathbf F=y\,\mathbf i+x\,\mathbf j+z\,\mathbf k$, where $S$ is the (positively oriented) boundary of the solid bounded by $z=1-x^2-y^2$ and $z=0$. | $S_1$(위쪽 향한 포물면): 식 (10)의 피적분 $=1+4xy-x^2-y^2$; 극좌표로 $\int_0^{2\pi}\!\!\int_0^1(r-r^3+4r^3\cos\theta\sin\theta)\,dr\,d\theta=\frac14(2\pi)+0=\frac{\pi}{2}$. $S_2$(아래쪽 향한 원판, $\mathbf n=-\mathbf k$): $\mathbf F\cdot\mathbf n=-z=0$ → $0$. 합 $=\boxed{\dfrac{\pi}{2}}$ | sympy: $S_1=\pi/2$, $S_2=0$, 합 $=\pi/2$ | ✓ | 닫힌곡면이므로 바깥쪽(양의) 방향 규약 |
| 6 | 1267 | 계산·응용 | The temperature $u$ in a metal ball is proportional to the squared distance from the center. Find the rate of heat flow across the sphere $S$ of radius $a$ centered at the ball's center. | $u=C(x^2+y^2+z^2)$, $\mathbf F=-K\nabla u=-2KC(x\mathbf i+y\mathbf j+z\mathbf k)$; 바깥쪽 단위법선 $\mathbf n=\frac1a(x\mathbf i+y\mathbf j+z\mathbf k)$ 이므로 $\mathbf F\cdot\mathbf n=-\frac{2KC}{a}(x^2+y^2+z^2)=-2aKC$ ($S$ 위에서). 따라서 $\iint_S\mathbf F\cdot d\mathbf S=-2aKC\cdot A(S)=-2aKC(4\pi a^2)=\boxed{-8KC\pi a^3}$ | sympy: $-8\pi CKa^3$ | ✓ | 매개화 없이 대칭성으로 $\mathbf n$을 직접 사용; 음수 = 열이 안쪽으로(중심 방향) 흐름 |

예제 수: **6** (전부 계산형, 6번은 응용 성격). anchor 불일치: **0건**.
재계산 스크립트: `/Users/chalrs/analysis/stewart/inventory/anchor-16.7.py`

## C. 그림 필요 목록 (자체 SVG)

| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 1 | $D$의 소사각형 $R_{ij}$ → 패치 $S_{ij}$, 표본점 $P_{ij}^*$ | 선택 (§16.6 Fig 16/17 재사용 가능) | 2 |
| Figure 2 | 예제 2의 곡면 $z=x+y^2$ 위 직사각 정의역 | 선택 | 예제 2 |
| Figure 3 | 예제 3의 입체: 원기둥 옆면 $S_1$, 밑면 원판 $S_2$, 경사 뚜껑 $S_3:z=1+x$ | 선택 | 예제 3 |
| Figures 4, 5 | 뫼비우스 띠와 그 구성(직사각 띠를 반 바퀴 꼬아 $A\!-\!D$, $B\!-\!C$ 접합) | **필수** | 11 |
| Figures 6, 7 | 한 점의 두 단위법선 $\mathbf n_1,\mathbf n_2$; 곡면 위 두 가지 연속 법선장 | **필수** | 13 |
| Figures 8, 9 | 구면의 바깥쪽(양)·안쪽(음) 방향 법선장 | **필수** | 17 |
| Figures 10, 11 | 유체 흐름 $\mathbf F=\rho\mathbf v$ 가 $S$를 통과, 패치 $S_{ij}$ 와 법선 $\mathbf n$ | 선택 | 18 |
| Figure 12 | 단위구면 위 예제 4의 벡터장 $\mathbf F=z\mathbf i+y\mathbf j+x\mathbf k$ | 선택 | 예제 4 |
| Figure 13 | 예제 5의 입체: 포물면 뚜껑 $S_1$ + 원판 밑면 $S_2$ | 선택 | 예제 5 |

## D. ERRATA·판독 불확실

- **PLAN.md 예제 수 오류**: §16.7은 5개가 아니라 **6개**(Example 1–6, PDF p.1259·1260·1260·1265·1266·1267).
- 본문 함수 이름 표기: §16.7의 그래프는 $z=g(x,y)$ ($t$처럼 보이는 것은 pdftotext가 $g$를 잘못 읽은 것). §16.6에서는 같은 자리에 $f$를 썼으므로 사이트에서는 **§16.7은 $g$** 로 통일한다(PNG p-1259/p-1260에서 확인).
- pdftotext 인코딩 왜곡(`−`→`=`, `1`→`+`, `2`→`−`, `3`→`×`, `s…d`→`(…)`, `k…l`→`⟨…⟩`, `y`→`∫`, `<`→`≤`, `«0`→`ε₀`, 그리스 문자 θ·φ·ρ 탈락)은 PNG(p-1257 ~ p-1267)로 전부 대조 확인함.
- Definition 8이 pdftotext에서 "Definitio"로 잘렸으나 원문은 "Definition".
- 그 외 판독 불확실 없음.

## E. 절 요약 (사이트 도입 note 초안)

곡면적분은 선적분을 한 차원 올린 것이다. 곡면을 작은 패치로 쪼개 $\sum f(P_{ij}^*)\Delta S_{ij}$ 의 극한으로 $\iint_S f\,dS$ 를 정의하면, 매개화 $\mathbf r(u,v)$ 를 통해 $\iint_D f(\mathbf r(u,v))|\mathbf r_u\times\mathbf r_v|\,dA$ 라는 계산 가능한 이중적분이 되고, 그래프 $z=g(x,y)$ 에서는 $dS=\sqrt{1+z_x^2+z_y^2}\,dA$ 로 단순해진다. $f\equiv1$이면 곡면넓이가, $f=\rho$이면 얇은 판의 질량과 질량중심이 나온다. 벡터장을 적분하려면 먼저 곡면에 **방향**을 주어야 하는데, 뫼비우스 띠처럼 연속적인 단위법선을 고를 수 없는 곡면은 제외되고, 닫힌곡면에서는 바깥쪽 법선을 양의 방향으로 약속한다. 이때 플럭스 $\iint_S\mathbf F\cdot d\mathbf S=\iint_S\mathbf F\cdot\mathbf n\,dS$ 는 매개곡면에서 $\iint_D\mathbf F\cdot(\mathbf r_u\times\mathbf r_v)\,dA$, 그래프에서 $\iint_D(-Pg_x-Qg_y+R)\,dA$ 로 계산되며, 유체의 유량·전기다발(가우스 법칙)·열 흐름률이 모두 이 하나의 적분으로 표현된다.

## F. 공통과제 문항 (4차 공통과제)

- **과제 제출 문항**: 8, 16, 19, 24, 27, 39
- **학습 참고 문항**: 5~20, 21~32, 37~40
