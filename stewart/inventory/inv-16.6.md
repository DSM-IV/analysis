# §16.6 Parametric Surfaces and Their Areas — PDF p.1245–1256 (인쇄 p.1208–1219)

본문 p.1245(하단)–1255(상단), 연습문제 p.1255–1256. 예제 **11개**(PLAN.md의 "8"은 과소 집계 — D 참조).

## A. 카드 인벤토리 (원문 순서)

| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입) | 매개곡면으로 가는 길 / Why Parametric Surfaces | 지금까지 다룬 곡면은 원기둥·이차곡면·$z=f(x,y)$의 그래프·등위면뿐. 공간곡선을 한 변수 벡터함수 $\mathbf r(t)$로 기술했듯, **두 변수** 벡터함수 $\mathbf r(u,v)$로 훨씬 일반적인 곡면을 기술하고 그 넓이를 구한다. 일반 넓이 공식을 먼저 세우고 특수한 곡면(그래프·회전면)에 적용하는 순서 | 1245 | — | — |
| 2 | def | Equations (1), (2) | 매개곡면 / Parametric Surface | $uv$-평면의 영역 $D$ 위에서 정의된 벡터함수 (1) $\mathbf r(u,v)=x(u,v)\,\mathbf i+y(u,v)\,\mathbf j+z(u,v)\,\mathbf k$ 에 대해, (2) $x=x(u,v),\ y=y(u,v),\ z=z(u,v)$, $(u,v)\in D$ 를 만족하는 점 $(x,y,z)\in\mathbb R^3$ 전체를 **매개곡면** $S$, (2)를 $S$의 **매개변수방정식**이라 한다. $(u,v)$가 $D$를 훑을 때 위치벡터 $\mathbf r(u,v)$의 끝점이 $S$를 그린다 | 1245 | — | Fig 1 |
| 3 | fig | Figure 1 | 매개변수영역과 곡면 / Parameter Domain → Surface | $uv$-평면의 $D$와 점 $(u,v)$ → $\mathbf r$ → $xyz$-공간의 $S$와 점 $\mathbf r(u,v)$ | 1246 | — | 필수 |
| 4 | def | (본문 정의, Figure 4) | 격자곡선 / Grid Curves | $S$ 위의 두 곡선족: $u=u_0$ 고정 시 $\mathbf r(u_0,v)$ 가 곡선 $C_1$, $v=v_0$ 고정 시 $\mathbf r(u,v_0)$ 가 곡선 $C_2$. 이들을 **격자곡선**이라 하며 $uv$-평면의 수직·수평선에 대응한다 | 1246–1247 | — | Fig 4 |
| 5 | rem | NOTE (Ex 4 뒤) + 여백 노트 | 격자곡선은 위도·경도선 / Grid Curves as Latitude & Longitude | 구면에서 $\phi$ 일정 격자곡선 = 위도원, $\theta$ 일정 격자곡선 = 자오선(경도). 일반 매개곡면에서 $(u,v)$ 값을 주는 것은 지도의 위도·경도를 주는 것과 같다. 여백: $x^2+y^2+z^2=1$을 $z$에 대해 풀어 두 반구를 따로 그리면 직사각 격자 때문에 적도 부근이 빠져 보이지만(Fig 8), 예제 4의 매개화로 그리면 매끄럽다(Fig 9) | 1248 | — | Fig 7 |
| 6 | note | (Ex 6 뒤 본문) | 그래프는 언제나 매개곡면 / Graphs as Parametric Surfaces | $z=f(x,y)$ 꼴 곡면은 $x,y$ 자체를 매개변수로 삼아 $x=x,\ y=y,\ z=f(x,y)$, 즉 $\mathbf r(x,y)=x\,\mathbf i+y\,\mathbf j+f(x,y)\,\mathbf k$ 로 항상 매개화된다 | 1249 | — | — |
| 7 | rem | (Ex 7 앞뒤 본문) | 매개화는 유일하지 않다 / Parametrizations Are Not Unique | 한 곡면에 여러 매개화(parametrization)가 가능하며 목적에 따라 유불리가 갈린다. 정의역 $D$를 바꾸는 것만으로 곡면의 일부만 잘라낼 수 있다(예: 원뿔에서 극좌표 매개화를 쓰면 $z\le1$ 부분은 $0\le r\le\tfrac12$) | 1249–1250 | — | Fig 11 |
| 8 | thm | Equations (3) | 회전면의 매개방정식 / Surfaces of Revolution | $y=f(x)$, $a\le x\le b$, $f(x)\ge0$ 를 $x$축 둘레로 회전한 곡면 $S$는 회전각 $\theta$를 써서 (3) $x=x,\quad y=f(x)\cos\theta,\quad z=f(x)\sin\theta$, 정의역 $a\le x\le b,\ 0\le\theta\le2\pi$. $y$축·$z$축 회전도 같은 방식으로 변형 가능(연습 30) | 1250 | — | Fig 12 |
| 9 | fig | Figure 12 | 회전면의 회전각 / Rotation Angle for a Surface of Revolution | $y=f(x)$ 곡선, 점 $(x,y,z)$, 반지름 $f(x)$와 각 $\theta$의 관계 | 1250 | — | 필수 |
| 10 | thm | Equations (4), (5) | 접벡터 $\mathbf r_u,\mathbf r_v$ / Tangent Vectors | 격자곡선 $C_1$($u=u_0$)의 $P_0$에서의 접벡터 (4) $\mathbf r_v=\frac{\partial x}{\partial v}(u_0,v_0)\mathbf i+\frac{\partial y}{\partial v}(u_0,v_0)\mathbf j+\frac{\partial z}{\partial v}(u_0,v_0)\mathbf k$, 격자곡선 $C_2$($v=v_0$)의 접벡터 (5) $\mathbf r_u=\frac{\partial x}{\partial u}\mathbf i+\frac{\partial y}{\partial u}\mathbf j+\frac{\partial z}{\partial u}\mathbf k$ (모두 $(u_0,v_0)$에서 평가) | 1251 | — | Fig 14 |
| 11 | def | (본문 정의) | 매끄러운 곡면과 접평면 / Smooth Surface, Tangent Plane | $\mathbf r_u\times\mathbf r_v$가 결코 $\mathbf 0$이 아니면 $S$를 **매끄럽다(smooth)** 고 한다(모서리가 없다). 매끄러운 곡면의 **접평면**은 $\mathbf r_u,\mathbf r_v$를 포함하는 평면이고, $\mathbf r_u\times\mathbf r_v$가 그 법선벡터다 | 1251 | — | Fig 14 |
| 12 | fig | Figure 14 | 접벡터와 접평면 / Tangent Vectors and Tangent Plane | $D$의 $(u_0,v_0)$ → $P_0$, 격자곡선 $C_1,C_2$와 접벡터 $\mathbf r_u,\mathbf r_v$ | 1251 | — | 필수 |
| 13 | note | (Surface Area 도입) | 넓이 정의의 착상: 패치와 평행사변형 / Motivating the Area Definition | 직사각형 $D$를 소구간 $R_{ij}$로 분할하면 그 상 $S_{ij}$(**패치**)의 두 변은 $\Delta u\,\mathbf r_u^*$, $\Delta v\,\mathbf r_v^*$ 로 근사된다(편도함수 ≈ 차분몫). 이 평행사변형의 넓이는 $|\mathbf r_u^*\times\mathbf r_v^*|\,\Delta u\,\Delta v$ 이고, $\sum_i\sum_j|\mathbf r_u^*\times\mathbf r_v^*|\Delta u\Delta v$ 는 $\iint_D|\mathbf r_u\times\mathbf r_v|\,du\,dv$ 의 리만 합이다 | 1252 | — | Fig 16, 17 |
| 14 | def | Definition 6 | 매개곡면의 넓이 / Surface Area | 매끄러운 매개곡면 $S:\mathbf r(u,v)$, $(u,v)\in D$ 가 $D$ 전체에서 **꼭 한 번만** 덮일 때 (6) $A(S)=\iint_D|\mathbf r_u\times\mathbf r_v|\,dA$, 여기서 $\mathbf r_u=\frac{\partial x}{\partial u}\mathbf i+\frac{\partial y}{\partial u}\mathbf j+\frac{\partial z}{\partial u}\mathbf k$, $\mathbf r_v=\frac{\partial x}{\partial v}\mathbf i+\frac{\partial y}{\partial v}\mathbf j+\frac{\partial z}{\partial v}\mathbf k$ | 1252 | — | — |
| 15 | fig | Figure 17 | 패치의 평행사변형 근사 / Approximating a Patch | 패치 $S_{ij}$와 그것을 근사하는 평행사변형 $\Delta u\,\mathbf r_u^*$, $\Delta v\,\mathbf r_v^*$ | 1252 | — | 필수 |
| 16 | thm | Equations (7), (8) | 그래프의 법선벡터와 그 크기 / Normal for $z=f(x,y)$ | $z=f(x,y)$ 를 $x,y$로 매개화하면 $\mathbf r_x=\mathbf i+\frac{\partial f}{\partial x}\mathbf k$, $\mathbf r_y=\mathbf j+\frac{\partial f}{\partial y}\mathbf k$ 이고 (7) $\mathbf r_x\times\mathbf r_y=-\frac{\partial f}{\partial x}\mathbf i-\frac{\partial f}{\partial y}\mathbf j+\mathbf k$, (8) $|\mathbf r_x\times\mathbf r_y|=\sqrt{\left(\frac{\partial f}{\partial x}\right)^2+\left(\frac{\partial f}{\partial y}\right)^2+1}=\sqrt{1+\left(\frac{\partial z}{\partial x}\right)^2+\left(\frac{\partial z}{\partial y}\right)^2}$ | 1253 | 본문 | — |
| 17 | thm | Equation (9) | 그래프꼴 곡면의 넓이 / Area of a Graph | (9) $A(S)=\displaystyle\iint_D\sqrt{1+\left(\frac{\partial z}{\partial x}\right)^2+\left(\frac{\partial z}{\partial y}\right)^2}\,dA$. 여백 주석: 8.1절 호길이 $L=\int_a^b\sqrt{1+(dy/dx)^2}\,dx$ 와 형태가 닮았다 | 1254 | 본문((8)에서 즉시) | — |
| 18 | thm | (무번호, 절 마무리) | 회전면 넓이 공식과의 일관성 / Consistency with §8.2.4 | 정의 6이 1변수 미적분의 회전면 넓이 공식과 모순되지 않음을 확인: (3)의 매개화에서 $\mathbf r_x=\mathbf i+f'(x)\cos\theta\,\mathbf j+f'(x)\sin\theta\,\mathbf k$, $\mathbf r_\theta=-f(x)\sin\theta\,\mathbf j+f(x)\cos\theta\,\mathbf k$, $|\mathbf r_x\times\mathbf r_\theta|=f(x)\sqrt{1+[f'(x)]^2}$ 이므로 $A=\int_0^{2\pi}\!\!\int_a^b f\sqrt{1+(f')^2}\,dx\,d\theta=2\pi\int_a^b f(x)\sqrt{1+[f'(x)]^2}\,dx$ (= 식 8.2.4) | 1254–1255 | 본문 | — |

카드 수: **note 3, def 4, thm 5, rem 2, fig 4 — 합계 18**

## B. 예제 기준값

| Example | PDF 쪽 | 유형 | 문제 요지 (영어 재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1246 | 스케치·개념 | Identify and sketch the surface traced by $\mathbf r(u,v)=2\cos u\,\mathbf i+v\,\mathbf j+2\sin u\,\mathbf k$. | $x^2+z^2=4$ with $y=v$ free — a **circular cylinder of radius 2 whose axis is the $y$-axis**. (그래프형 — 서술 답: $y$ 고정 단면이 모두 반지름 2인 원) | sympy: $x^2+z^2=4$ (항등적으로 4) | ✓ | 매개변수 제한이 없어 전체 원기둥; $0\le u\le\pi/2,\ 0\le v\le3$ 으로 제한하면 길이 3의 사분원기둥(Fig 3) |
| 2 | 1247 | 스케치·개념 | Graph $\mathbf r(u,v)=\langle(2+\sin v)\cos u,\ (2+\sin v)\sin u,\ u+\cos v\rangle$ on $0\le u\le4\pi$, $0\le v\le2\pi$ and say which grid curves have $u$ constant and which have $v$ constant. | 나선 튜브(spiral tube). $v$ 일정 격자곡선 = 나선(spiral) 곡선; $u$ 일정 격자곡선 = 원처럼 보이는 곡선. 근거: $u=u_0$이면 $z=u_0+\cos v\in[u_0-1,u_0+1]$ | sympy: $x^2+y^2=(2+\sin v)^2$ ($u$ 무관) → $v$ 고정 시 반지름 일정 + $z=u+\text{const}$ = 나선; $u$ 고정 시 연직평면 $\theta=u_0$ 안의 닫힌 곡선(원) | ✓ | 그래프형 |
| 3 | 1247 | 증명(유도) | Find a vector function representing the plane through the point with position vector $\mathbf r_0$ containing two nonparallel vectors $\mathbf a,\mathbf b$. | $\mathbf r(u,v)=\mathbf r_0+u\,\mathbf a+v\,\mathbf b$, $u,v\in\mathbb R$; 성분으로 $x=x_0+ua_1+vb_1$, $y=y_0+ua_2+vb_2$, $z=z_0+ua_3+vb_3$ | sympy: $\mathbf r_u\times\mathbf r_v=\mathbf a\times\mathbf b$ (상수) → 법선이 고정된 평면 | ✓ | $\overrightarrow{P_0P}=u\mathbf a+v\mathbf b$ (평행사변형 법칙) |
| 4 | 1248 | 계산 | Find a parametric representation of the sphere $x^2+y^2+z^2=a^2$. | $x=a\sin\phi\cos\theta,\ y=a\sin\phi\sin\theta,\ z=a\cos\phi$; $\mathbf r(\phi,\theta)=a\sin\phi\cos\theta\,\mathbf i+a\sin\phi\sin\theta\,\mathbf j+a\cos\phi\,\mathbf k$, $D=[0,\pi]\times[0,2\pi]$ | sympy: $x^2+y^2+z^2=a^2$ 항등 | ✓ | 구면좌표 $\rho=a$; $\phi$ 일정 = 위도원, $\theta$ 일정 = 자오선 |
| 5 | 1248 | 계산 | Find a parametric representation of the cylinder $x^2+y^2=4$, $0\le z\le1$. | $x=2\cos\theta,\ y=2\sin\theta,\ z=z$; $\mathbf r(\theta,z)=2\cos\theta\,\mathbf i+2\sin\theta\,\mathbf j+z\,\mathbf k$, $D=\{(\theta,z)\mid 0\le\theta\le2\pi,\ 0\le z\le1\}$ | sympy: $x^2+y^2=4$ 항등 | ✓ | 원기둥좌표 $r=2$ |
| 6 | 1249 | 계산 | Find a vector function for the elliptic paraboloid $z=x^2+2y^2$. | $x=x,\ y=y,\ z=x^2+2y^2$; $\mathbf r(x,y)=x\,\mathbf i+y\,\mathbf j+(x^2+2y^2)\,\mathbf k$ | 직접 대입 — 항등 | ✓ | 그래프꼴의 표준 매개화 |
| 7 | 1249–1250 | 계산 | Find a parametric representation of $z=2\sqrt{x^2+y^2}$ (upper half of $z^2=4x^2+4y^2$), in two ways. | 해 1: $\mathbf r(x,y)=x\,\mathbf i+y\,\mathbf j+2\sqrt{x^2+y^2}\,\mathbf k$; 해 2: $\mathbf r(r,\theta)=r\cos\theta\,\mathbf i+r\sin\theta\,\mathbf j+2r\,\mathbf k$, $r\ge0,\ 0\le\theta\le2\pi$ | sympy: 해 2에서 $z^2-4(x^2+y^2)=0$ 항등 | ✓ | $z\le1$ 부분은 해 2에서 $D=\{0\le r\le\frac12,\ 0\le\theta\le2\pi\}$ (Fig 11) |
| 8 | 1250 | 계산·스케치 | Find parametric equations for the surface obtained by revolving $y=\sin x$, $0\le x\le2\pi$, about the $x$-axis, and graph it. | $x=x,\ y=\sin x\cos\theta,\ z=\sin x\sin\theta$; $0\le x\le2\pi,\ 0\le\theta\le2\pi$ | sympy: $y^2+z^2=\sin^2x$ 항등 | ✓ | 식 (3) 직접 적용; 그래프는 두 개의 방추형(Fig 13) |
| 9 | 1251 | 계산 | Find the tangent plane at $(1,1,3)$ to the surface $x=u^2$, $y=v^2$, $z=u+2v$. | $\mathbf r_u=2u\,\mathbf i+\mathbf k$, $\mathbf r_v=2v\,\mathbf j+2\mathbf k$, $\mathbf r_u\times\mathbf r_v=-2v\,\mathbf i-4u\,\mathbf j+4uv\,\mathbf k$; $(u,v)=(1,1)$에서 $\mathbf n=-2\,\mathbf i-4\,\mathbf j+4\,\mathbf k$; 접평면 $-2(x-1)-4(y-1)+4(z-3)=0$, 즉 $\boxed{x+2y-2z+3=0}$ | sympy: $\mathbf r_u\times\mathbf r_v=[-2v,\,-4u,\,4uv]$, $\mathbf n=[-2,-4,4]$, 평면 $-2X-4Y+4Z-6=0\Rightarrow X+2Y-2Z+3=0$ | ✓ | Fig 15의 자기교차 곡면 |
| 10 | 1253 | 계산 | Find the surface area of a sphere of radius $a$. | $|\mathbf r_\phi\times\mathbf r_\theta|=a^2\sin\phi$ (단, $\sin\phi\ge0$ on $[0,\pi]$); $A=\int_0^{2\pi}\!\!\int_0^{\pi}a^2\sin\phi\,d\phi\,d\theta=a^2(2\pi)(2)=\boxed{4\pi a^2}$ | sympy: $|\mathbf r_\phi\times\mathbf r_\theta|=a^2|\sin\phi|$; 적분 $=4\pi a^2$ | ✓ | 교차곱 성분 $a^2\sin^2\phi\cos\theta,\ a^2\sin^2\phi\sin\theta,\ a^2\sin\phi\cos\phi$ |
| 11 | 1254 | 계산 | Find the area of the part of the paraboloid $z=x^2+y^2$ lying below the plane $z=9$. | 피적분 $\sqrt{1+4(x^2+y^2)}$, $D$: 원점 중심 반지름 3인 원판; 극좌표로 $A=\int_0^{2\pi}\!\!\int_0^3 r\sqrt{1+4r^2}\,dr\,d\theta=2\pi\cdot\frac1{12}(1+4r^2)^{3/2}\big|_0^3=\boxed{\frac{\pi}{6}\left(37\sqrt{37}-1\right)}$ | sympy: $\pi(37\sqrt{37}-1)/6\approx117.3187007098$ | ✓ | 교재 인쇄본의 계수 $2\pi(\tfrac18)(\tfrac23)=\tfrac{\pi}{6}$ 확인 |

예제 수: **11** (계산 7, 스케치·개념 3, 증명·유도 1). anchor 불일치: **0건**.
재계산 스크립트: `/Users/chalrs/analysis/stewart/inventory/anchor-16.6.py`

## C. 그림 필요 목록 (자체 SVG)

| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 1 | $uv$-평면 영역 $D$ → $\mathbf r$ → 공간의 매개곡면 $S$ (사상 도식) | 필수 | 3 |
| Figure 2 / 3 | $x^2+z^2=4$ 원기둥 전체와 $0\le u\le\pi/2$, $0\le v\le3$ 사분원기둥 | 선택 | 예제 1 |
| Figure 4 | $D$의 수직·수평선 → 곡면 위 격자곡선 $C_1$($u=u_0$), $C_2$($v=v_0$) | 필수 | 4 |
| Figure 7 | 구면의 격자곡선: 위도원($\phi=c$)과 자오선($\theta=k$), 정의역 사각형 $[0,\pi]\times[0,2\pi]$ | 선택 | 5 |
| Figure 11 | 정의역 축소 $0\le r\le\frac12$ → 반원뿔 (매개화 유연성) | 선택 | 7 |
| Figure 12 | $x$축 회전면: 곡선 $y=f(x)$, 반지름 $f(x)$, 회전각 $\theta$, 점 $(x,y,z)$ | 필수 | 9 |
| Figure 14 | 접벡터 $\mathbf r_u,\mathbf r_v$ 와 접평면, 격자곡선 $C_1,C_2$ | 필수 | 12 |
| Figure 16 / 17 | 소사각형 $R_{ij}$ → 패치 $S_{ij}$, 그리고 $\Delta u\,\mathbf r_u^*,\ \Delta v\,\mathbf r_v^*$ 평행사변형 근사 | 필수 | 15 |
| Figure 18 | 포물면 $z=x^2+y^2$ 와 $z=9$ 절단, 정사영 원판 $D$ (반지름 3) | 선택 | 예제 11 |

## D. ERRATA·판독 불확실

- **PLAN.md 예제 수 오류**: §16.6은 8개가 아니라 **11개**(Example 1–11, PDF p.1246·1247·1247·1248·1248·1249·1249·1250·1251·1253·1254). 전체 예제 합계 145도 그만큼 재확인 필요.
- pdftotext 출력에서 Stewart 폰트 인코딩이 깨져 `−`→`=`, `1`→`+`, `2`→`−`, `3`→`×`, `s…d`→`(…)`, `k…l`→`⟨…⟩`, `y`→`∫`, `<`→`≤`, `−x`→`∂x`, `=`→`∇` 로 나타난다. 본 인벤토리의 모든 수식은 PNG(p-1245 ~ p-1256)로 시각 확인함.
- Definition 6이 pdftotext에서 "Definitio"로 잘렸으나 원문은 "Definition" (판독 확인 완료).
- 그 외 판독 불확실 없음.

## E. 절 요약 (사이트 도입 note 초안)

곡선을 한 개의 매개변수 $t$로 기술했던 것처럼, 곡면은 두 개의 매개변수 $u,v$를 갖는 벡터함수 $\mathbf r(u,v)$로 기술한다. 이때 $uv$-평면의 정의역 $D$가 곡면 위의 "지도"가 되고, $u$ 또는 $v$를 고정해 얻는 격자곡선은 위도선·경도선의 역할을 한다. 그래프 $z=f(x,y)$, 구면, 원기둥, 원뿔, 회전면은 모두 이 틀 안에서 자연스럽게 매개화되며, 매개화는 결코 유일하지 않아 문제에 맞는 좌표를 고르는 것이 요령이다. 한 점에서 두 격자곡선의 접벡터 $\mathbf r_u,\mathbf r_v$가 접평면을 결정하고, 그 외적 $\mathbf r_u\times\mathbf r_v$가 법선벡터가 된다. 곡면을 작은 패치로 쪼개 각각을 평행사변형으로 근사하면 넓이는 $A(S)=\iint_D|\mathbf r_u\times\mathbf r_v|\,dA$ 로 정의되고, 그래프꼴에서는 $\iint_D\sqrt{1+z_x^2+z_y^2}\,dA$, 회전면에서는 1변수 미적분의 $2\pi\int_a^b f\sqrt{1+(f')^2}\,dx$ 로 각각 환원된다.

## F. 공통과제 문항 (4차 공통과제)

- **과제 제출 문항**: 23, 36, 47, 50, 60-(a), 62
- **학습 참고 문항**: 13~18, 19~26, 29, 30, 33~36, 39~50, 59-(a), 60-(a), 61~63
