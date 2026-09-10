# §16.2 Line Integrals — PDF p.1206–1218 (인쇄 p.1169–1181; 본문 p.1206–1216, 연습문제 p.1216–1218)

## A. 카드 인벤토리 (원문 순서)
| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입) | 선적분이란 / What a Line Integral Is | 구간 $[a,b]$ 대신 **곡선** $C$ 위에서 적분하는 것; 이름은 line integral이지만 "curve integral"이 더 적절. 19세기 초 유체 흐름·힘·전기·자기 문제를 풀기 위해 고안됨 | 1206 | — | — |
| 2 | note | ■ Line Integrals in the Plane (도입) | 매개곡선의 분할과 리만합 / Partitioning a Smooth Curve | (1) $x=x(t),\;y=y(t),\;a\le t\le b$, 즉 $\mathbf r(t)=x(t)\mathbf i+y(t)\mathbf j$이고 $C$는 매끄러움($\mathbf r'$ 연속, $\mathbf r'(t)\neq\mathbf 0$, §13.3). $[a,b]$를 $n$등분해 $C$를 길이 $\Delta s_i$인 소호로 나누고 각 소호의 $P_i^*(x_i^*,y_i^*)$에서 $\sum_{i=1}^n f(x_i^*,y_i^*)\,\Delta s_i$ (리만합 꼴) | 1206–1207 | — | Fig 1 |
| 3 | def | Definition 2 | 호의 길이에 대한 선적분 / Line Integral with Respect to Arc Length | (2) $\displaystyle\int_C f(x,y)\,ds=\lim_{n\to\infty}\sum_{i=1}^{n}f(x_i^*,y_i^*)\,\Delta s_i$ (극한이 존재할 때) | 1207 | — | — |
| 4 | thm | Formula (3) | 선적분의 계산 공식 / Evaluation Formula | $f$가 연속이면 극한이 항상 존재하고 (3) $\displaystyle\int_C f(x,y)\,ds=\int_a^b f(x(t),y(t))\sqrt{\Bigl(\tfrac{dx}{dt}\Bigr)^2+\Bigl(\tfrac{dy}{dt}\Bigr)^2}\,dt$. 곡선을 정확히 한 번 지나는 한 **매개변수화에 무관** | 1207 | §10.2 호길이 논증과 같은 방식(개략) | — |
| 5 | rem | (ds 기억법) + NOTE | $ds$의 기억법과 특수한 경우 / Remembering $ds$; a Special Case | $\dfrac{ds}{dt}=\lvert\mathbf r'(t)\rvert=\sqrt{(dx/dt)^2+(dy/dt)^2}$ (식 13.3.7)이므로 모든 것을 $t$로 나타내고 $ds=\sqrt{(dx/dt)^2+(dy/dt)^2}\,dt$로 쓰면 된다. **NOTE**: $C$가 $(a,0)\to(b,0)$ 선분이면 $\int_C f\,ds=\int_a^b f(x,0)\,dx$ — 보통의 정적분으로 환원 | 1207 | — | — |
| 6 | note | (Figure 2 본문) | 선적분의 넓이 해석 / Area Interpretation | $f(x,y)\ge 0$이면 $\int_C f(x,y)\,ds$는 밑변이 $C$, 점 $(x,y)$ 위 높이가 $f(x,y)$인 "울타리(커튼)" 한쪽 면의 넓이 | 1208 | — | Fig 2 |
| 7 | rem | (조각마다 매끄러운 곡선) | 조각마다 매끄러운 곡선 / Piecewise-Smooth Curves | $C=C_1\cup\cdots\cup C_n$ (각 $C_{i+1}$의 시점 = $C_i$의 종점)이면 $\int_C f\,ds=\int_{C_1}f\,ds+\cdots+\int_{C_n}f\,ds$ | 1208 | — | Fig 4 |
| 8 | note | (질량·질량중심 단락) + Formula (4) | 철사의 질량과 질량중심 / Mass and Center of Mass of a Wire | 선밀도가 $\rho(x,y)$인 철사의 질량 $m=\displaystyle\int_C\rho(x,y)\,ds$; 질량중심 $(\bar x,\bar y)$는 (4) $\bar x=\dfrac1m\displaystyle\int_C x\,\rho(x,y)\,ds,\quad \bar y=\dfrac1m\displaystyle\int_C y\,\rho(x,y)\,ds$ | 1209 | — | — |
| 9 | def | Formulas (5), (6) | $x$·$y$에 대한 선적분 / Line Integrals with Respect to $x$ and $y$ | $\Delta s_i$를 $\Delta x_i=x_i-x_{i-1}$ 또는 $\Delta y_i=y_i-y_{i-1}$로 바꾼 것: (5) $\int_C f\,dx=\lim\sum f(x_i^*,y_i^*)\Delta x_i$, (6) $\int_C f\,dy=\lim\sum f(x_i^*,y_i^*)\Delta y_i$. 구별할 때 원래 것을 "호의 길이에 대한 선적분"이라 부름 | 1210 | — | — |
| 10 | thm | Formulas (7) | $dx$·$dy$ 선적분의 계산 / Evaluating the $dx$, $dy$ Integrals | (7) $\displaystyle\int_C f\,dx=\int_a^b f(x(t),y(t))\,x'(t)\,dt$, $\displaystyle\int_C f\,dy=\int_a^b f(x(t),y(t))\,y'(t)\,dt$. 함께 나올 때는 $\displaystyle\int_C P\,dx+Q\,dy$로 줄여 씀 | 1210 | — | — |
| 11 | rem | Equation (8) | 선분의 매개변수 표현 / Parametrizing a Line Segment | (8) $\mathbf r(t)=(1-t)\mathbf r_0+t\,\mathbf r_1,\;0\le t\le1$ ($\mathbf r_0$에서 시작해 $\mathbf r_1$에서 끝남; 식 12.5.4) | 1210 | — | — |
| 12 | rem | (배향 단락, Figure 8) | 곡선의 배향과 부호 / Orientation Matters | 매개변수화는 $t$ 증가 방향을 양의 방향으로 하는 배향을 정한다. 반대 배향 $-C$에 대해 $\displaystyle\int_{-C}f\,dx=-\int_C f\,dx,\ \int_{-C}f\,dy=-\int_C f\,dy$ 이지만 $\displaystyle\int_{-C}f\,ds=\int_C f\,ds$ ($\Delta s_i>0$은 부호가 바뀌지 않으므로) | 1211 | — | Fig 8 |
| 13 | thm | Formula (9), (10) | 공간곡선 위의 선적분 / Line Integrals in Space | $\mathbf r(t)=x(t)\mathbf i+y(t)\mathbf j+z(t)\mathbf k$에 대해 (9) $\displaystyle\int_C f\,ds=\int_a^b f(x(t),y(t),z(t))\sqrt{x'^2+y'^2+z'^2}\,dt=\int_a^b f(\mathbf r(t))\,\lvert\mathbf r'(t)\rvert\,dt$. $f\equiv1$이면 $\int_C ds=L$ (곡선의 길이, 식 13.3.3). 성분별로는 (10) $\displaystyle\int_C P\,dx+Q\,dy+R\,dz$를 모두 $t$로 바꿔 계산 | 1212 | — | — |
| 14 | note | ■ Line Integrals of Vector Fields; Work + (11), (12) | 힘장이 한 일 / Work Done by a Force Field | 변력의 일 $W=\int_a^b f(x)dx$(§5.4), 일정한 힘의 일 $W=\mathbf F\cdot\mathbf D$(§12.3)의 확장. 소호에서 한 일 $\approx[\mathbf F(P_i^*)\cdot\mathbf T(t_i^*)]\Delta s_i$이므로 리만합 (11) $\sum[\mathbf F\cdot\mathbf T]\Delta s_i$의 극한으로 (12) $W=\displaystyle\int_C\mathbf F\cdot\mathbf T\,ds$ — **일은 힘의 접선성분의 호길이 선적분** | 1213–1214 | 리만합 논증(본문) | Fig 11, 12 |
| 15 | def | Definition 13 | 벡터장의 선적분 / Line Integral of a Vector Field | 매끄러운 곡선 $C:\mathbf r(t),\,a\le t\le b$ 위의 연속 벡터장 $\mathbf F$에 대해 (13) $\displaystyle\int_C\mathbf F\cdot d\mathbf r=\int_a^b\mathbf F(\mathbf r(t))\cdot\mathbf r'(t)\,dt=\int_C\mathbf F\cdot\mathbf T\,ds$. $\mathbf F(\mathbf r(t))$는 $x=x(t)$ 등을 대입한 것, 형식적으로 $d\mathbf r=\mathbf r'(t)\,dt$ | 1214 | (12)에서 $\mathbf T=\mathbf r'/\lvert\mathbf r'\rvert$ 대입(본문) | — |
| 16 | rem | NOTE (p.1215) | 벡터장 선적분과 배향 / Orientation Reverses the Sign | $\int_C\mathbf F\cdot d\mathbf r=\int_C\mathbf F\cdot\mathbf T\,ds$이고 호길이 선적분은 배향에 무관하지만, $\mathbf T\mapsto-\mathbf T$가 되므로 $\displaystyle\int_{-C}\mathbf F\cdot d\mathbf r=-\int_C\mathbf F\cdot d\mathbf r$ | 1215 | — | — |
| 17 | thm | Formula (14) | 벡터장 선적분 = 성분 선적분 / Vector and Scalar Forms Agree | $\mathbf F=P\mathbf i+Q\mathbf j+R\mathbf k$이면 $\displaystyle\int_C\mathbf F\cdot d\mathbf r=\int_C P\,dx+Q\,dy+R\,dz$; $\mathbb R^2$에서는 (14) $\displaystyle\int_C\mathbf F\cdot d\mathbf r=\int_C P\,dx+Q\,dy$ ($\mathbf F=P\mathbf i+Q\mathbf j$) | 1215–1216 | 본문 (정의 13 전개) | — |
| 18 | fig | Figure 2 | 선적분의 "울타리" 넓이 / The Fence Picture | 곡선 $C$ 위에 세운 높이 $f(x,y)$의 곡면 조각 | 1208 | — | 필수 |
| 19 | fig | Figure 7 | 같은 두 끝점, 다른 두 경로 / Two Paths, Same Endpoints | 선분 $C_1$과 포물선 $x=4-y^2$의 호 $C_2$가 모두 $(-5,-3)\to(0,2)$ — 선적분 값이 경로에 의존함을 보임 | 1210 | — | 필수 |

## B. 예제 기준값
| Example | PDF 쪽 | 유형 | 문제 요지 (영어 재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1208 | 계산 | Evaluate $\int_C(2+x^{2}y)\,ds$ over the upper half of the unit circle $x^{2}+y^{2}=1$. | $2\pi+\dfrac{2}{3}$ | sympy: $2\pi+\frac23$ | ✔ | 매개변수화 $x=\cos t,\ y=\sin t,\ 0\le t\le\pi$이면 $ds=dt$ |
| 2 | 1208–1209 | 계산 | Evaluate $\int_C 2x\,ds$ where $C$ is the parabolic arc $y=x^{2}$ from $(0,0)$ to $(1,1)$ joined to the vertical segment from $(1,1)$ to $(1,2)$. | $C_1:\dfrac{5\sqrt5-1}{6}$; $C_2:2$; 합 $\dfrac{5\sqrt5-1}{6}+2$ | sympy: $C_1=\frac{5\sqrt5-1}{6}$, $C_2=2$, 합 $=\frac{5\sqrt5}{6}+\frac{11}{6}$ | ✔ | 조각마다 매끄러운 곡선 예 |
| 3 | 1209–1210 | 계산 | A semicircular wire $x^{2}+y^{2}=1,\ y\ge0$ has linear density proportional to its distance from the line $y=1$. Find its center of mass. | $m=k(\pi-2)$; $\bar x=0$ (대칭); $\bar y=\dfrac{4-\pi}{2(\pi-2)}\approx0.38$; 질량중심 $\bigl(0,\ \tfrac{4-\pi}{2(\pi-2)}\bigr)\approx(0,0.38)$ | sympy: $m=k(\pi-2)$, $\bar x=0$, $\bar y=\frac{4-\pi}{2(\pi-2)}=0.37597$ | ✔ | $\rho(x,y)=k(1-y)$ |
| 4 | 1210–1211 | 계산 | Evaluate $\int_C y^{2}\,dx+x\,dy$ from $(-5,-3)$ to $(0,2)$ along (a) the straight segment, (b) the arc of $x=4-y^{2}$. | (a) $-\dfrac{5}{6}$; (b) $40\dfrac{5}{6}=\dfrac{245}{6}$; 덧붙여 $\int_{-C_1}y^2dx+x\,dy=\dfrac56$ | sympy: (a) $-\frac56$; (b) $\frac{245}{6}$; $-C_1$: $\frac56$ | ✔ | 두 값이 다름 → 선적분은 경로에 의존(§16.3에서 경로무관 조건); 배향을 뒤집으면 부호가 바뀜 |
| 5 | 1212 | 계산 | Evaluate $\int_C y\sin z\,ds$ along the circular helix $x=\cos t,\ y=\sin t,\ z=t,\ 0\le t\le2\pi$. | $\sqrt2\,\pi$ | sympy: $\sqrt2\,\pi$ | ✔ | $\lvert\mathbf r'\rvert=\sqrt2$ |
| 6 | 1213 | 계산 | Evaluate $\int_C y\,dx+z\,dy+x\,dz$ where $C$ is the segment from $(2,0,0)$ to $(3,4,5)$ followed by the segment from $(3,4,5)$ to $(3,4,0)$. | $C_1=24.5$; $C_2=-15$; 합 $=9.5$ | sympy: $C_1=\frac{49}{2}=24.5$, $C_2=-15$, 합 $=\frac{19}{2}=9.5$ | ✔ | 식 (8)로 두 선분을 매개변수화; 이 적분은 $\mathbf F=y\mathbf i+z\mathbf j+x\mathbf k$의 $\int_C\mathbf F\cdot d\mathbf r$와 같음 |
| 7 | 1215 | 계산 | Find the work done by $\mathbf F(x,y)=x^{2}\mathbf i-xy\,\mathbf j$ along the quarter-circle $\mathbf r(t)=\cos t\,\mathbf i+\sin t\,\mathbf j,\ 0\le t\le\pi/2$. | $W=-\dfrac{2}{3}$ | sympy: $-\frac23$ | ✔ | 음수 — 힘장이 운동을 방해함 |
| 8 | 1215 | 계산 | Evaluate $\int_C\mathbf F\cdot d\mathbf r$ for $\mathbf F(x,y,z)=xy\,\mathbf i+yz\,\mathbf j+zx\,\mathbf k$ along the twisted cubic $x=t,\ y=t^{2},\ z=t^{3},\ 0\le t\le1$. | $\dfrac{27}{28}$ | sympy: $\frac{27}{28}$ ($\mathbf F(\mathbf r(t))=\langle t^3,t^5,t^4\rangle$) | ✔ | — |

## C. 그림 필요 목록 (자체 SVG)
| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 2 | 곡선 $C$ 위에 세운 높이 $f(x,y)$의 "울타리" — 선적분의 넓이 해석 | 필수 | 18 (카드 6) |
| Figure 7 | $(-5,-3)\to(0,2)$의 두 경로: 선분 $C_1$과 포물선 $x=4-y^2$의 호 $C_2$ | 필수 | 19 (예제 4) |
| Figure 1 | 매끄러운 곡선의 소호 분할 $P_0,\dots,P_n$과 $\Delta s_i$, $t_i^*\in[t_{i-1},t_i]$ | 선택 | 2 |
| Figure 4 / 5 | 조각마다 매끄러운 곡선 $C=C_1\cup\cdots\cup C_5$; 예제 2의 $C=C_1\cup C_2$ | 선택 | 7 / 예제 2 |
| Figure 8 | $C$와 $-C$의 배향(시점 $A$, 종점 $B$) | 선택 | 12 |
| Figure 6 | 반원 철사의 질량중심 위치 $(0,0.38)$ | 선택 | 예제 3 |
| Figure 3, 9, 10, 12, 13, 14 | 단위원 상반부 / 나선 / 예제 6의 꺾인 경로 / 일의 리만합 도해 / 예제 7·8의 장과 곡선 | 선택(대부분 생략 가능) | — |

## D. ERRATA·판독 불확실
- 없음. 교재의 모든 예제 최종답이 sympy 재계산과 일치.
- 판독 참고: pdftotext에서 밀도 기호 $\rho$가 통째로 탈락해 "sx, yd represents the linear density"처럼 보이지만, PNG p‑1209에서 $\rho(x,y)$임을 확인함. 마찬가지로 예제 3의 답 "42 / 2s 2 2d"는 $\dfrac{4-\pi}{2(\pi-2)}$임을 PNG로 확인.

## E. 절 요약 (사이트 도입 note 초안)
선적분은 구간이 아니라 곡선 $C$ 위에서 하는 적분으로, 곡선을 소호로 나눠 만든 리만합 $\sum f(x_i^*,y_i^*)\Delta s_i$의 극한으로 정의한다. 매개변수 $t$로 모든 것을 바꾸고 $ds=\lvert\mathbf r'(t)\rvert\,dt$를 쓰면 보통의 정적분으로 계산되며, 곡선을 한 번만 지나는 한 값은 매개변수화에 의존하지 않는다. $\Delta s_i$ 대신 $\Delta x_i,\Delta y_i$를 쓰면 $x$·$y$에 대한 선적분 $\int_C P\,dx+Q\,dy$가 나오는데, 이쪽은 곡선의 배향을 뒤집으면 부호가 바뀐다(호길이 선적분은 바뀌지 않는다). 힘장 $\mathbf F$가 곡선을 따라 한 일은 접선성분의 선적분 $W=\int_C\mathbf F\cdot\mathbf T\,ds=\int_C\mathbf F\cdot d\mathbf r=\int_a^b\mathbf F(\mathbf r(t))\cdot\mathbf r'(t)\,dt$이고, 성분으로 풀어 쓰면 $\int_C P\,dx+Q\,dy+R\,dz$와 같다. 선적분의 값은 두 끝점만이 아니라 **경로 전체**에 의존한다는 점이 중요하며(예제 4), 언제 경로에 무관해지는지는 §16.3에서 다룬다.

## F. 공통과제 문항
- 3차 공통과제, 16.2 Line Integrals
  - **과제 제출 문항**: 8, 18, 22, 36, 41, 43
  - **학습 참고 문항**: 1~8, 9~18, 21~24, 35~38, 41~43
