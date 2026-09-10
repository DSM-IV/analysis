# §14.6 Directional Derivatives and the Gradient Vector — PDF p.1069–1082 (인쇄 p.1032–1045)

본문 PDF p.1069–1080(인쇄 1032–1043), 연습문제 PDF p.1080–1083(인쇄 1043–1046).

## A. 카드 인벤토리 (원문 순서)

| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입) | 임의의 방향에서의 변화율 / Rates of Change in Any Direction | 캘리포니아·네바다 기온 등온선 지도에서, Reno의 $T_x$는 동쪽으로, $T_y$는 북쪽으로 갈 때의 기온 변화율이다. 남동쪽처럼 **임의의 방향**으로 갈 때의 변화율을 재는 것이 **방향도함수** | 1069 | — | Fig 1 |
| 2 | note | ■ Directional Derivatives (유도) | 방향도함수의 기하적 유도 / Geometric Setup | 편도함수의 극한 정의 $(1)$을 상기. 단위벡터 $\mathbf u=\langle a,b\rangle$ 방향으로 $P$를 지나는 수직평면이 곡면 $S:z=f(x,y)$와 만나 곡선 $C$를 만든다. $\overrightarrow{P'Q'}=h\mathbf u$이므로 $x=x_0+ha$, $y=y_0+hb$이고, $\dfrac{\Delta z}{h}=\dfrac{f(x_0+ha,y_0+hb)-f(x_0,y_0)}{h}$의 $h\to0$ 극한이 $C$의 접선 기울기 | 1070 | 본문(유도) | Fig 2, Fig 3 |
| 3 | def | Definition 2 | 방향도함수 (2변수) / Directional Derivative | 단위벡터 $\mathbf u=\langle a,b\rangle$에 대해 $D_{\mathbf u}f(x_0,y_0)=\displaystyle\lim_{h\to0}\frac{f(x_0+ha,\;y_0+hb)-f(x_0,y_0)}{h}$ (극한이 존재할 때). $\mathbf u=\mathbf i$면 $D_{\mathbf i}f=f_x$, $\mathbf u=\mathbf j$면 $D_{\mathbf j}f=f_y$ — 편도함수는 방향도함수의 특수한 경우 | 1070 | — | — |
| 4 | thm | Theorem 3 | 방향도함수 계산 공식 / Computing the Directional Derivative | $f$가 미분가능이면 임의의 단위벡터 $\mathbf u=\langle a,b\rangle$에 대해 $D_{\mathbf u}f(x,y)=f_x(x,y)\,a+f_y(x,y)\,b$ | 1071 | 본문 ($g(h)=f(x_0+ha,y_0+hb)$에 Case 1 연쇄법칙; 식 $(4)(5)$) | — |
| 5 | rem | Equation (6) | 각도 표현 / Angle Form | $\mathbf u$가 양의 $x$축과 각 $\theta$를 이루면 $\mathbf u=\langle\cos\theta,\sin\theta\rangle$이고 $(6)$ $D_{\mathbf u}f(x,y)=f_x\cos\theta+f_y\sin\theta$ | 1072 | — | Fig 5 |
| 6 | note | ■ The Gradient Vector | 기울기벡터의 도입 / Introducing the Gradient | $(7)$ $D_{\mathbf u}f=\langle f_x,f_y\rangle\cdot\langle a,b\rangle=\langle f_x,f_y\rangle\cdot\mathbf u$ — 방향도함수가 두 벡터의 내적으로 쓰인다. 첫 벡터를 $f$의 **기울기(gradient)** 라 하고 $\nabla f$ 또는 $\operatorname{grad}f$로 쓴다("del f") | 1072 | — | — |
| 7 | def | Definition 8 | 기울기벡터 (2변수) / The Gradient Vector | $\nabla f(x,y)=\langle f_x(x,y),\,f_y(x,y)\rangle=\dfrac{\partial f}{\partial x}\mathbf i+\dfrac{\partial f}{\partial y}\mathbf j$ | 1073 | — | — |
| 8 | thm | Equation (9) | 방향도함수 = 기울기와의 내적 / $D_{\mathbf u}f=\nabla f\cdot\mathbf u$ | $(9)$ $D_{\mathbf u}f(x,y)=\nabla f(x,y)\cdot\mathbf u$ — $\nabla f$의 $\mathbf u$ 방향 스칼라사영 | 1073 | (7)에서 바로 | — |
| 9 | def | Definition 10 + (11) | 방향도함수 (3변수) / Directional Derivative in Space | $\mathbf u=\langle a,b,c\rangle$에 대해 $D_{\mathbf u}f(x_0,y_0,z_0)=\displaystyle\lim_{h\to0}\frac{f(x_0+ha,y_0+hb,z_0+hc)-f(x_0,y_0,z_0)}{h}$. 벡터 표기로 $(11)$ $D_{\mathbf u}f(\mathbf x_0)=\lim_{h\to0}\dfrac{f(\mathbf x_0+h\mathbf u)-f(\mathbf x_0)}{h}$ (2변수·3변수 공통) | 1074 | — | — |
| 10 | thm | Equations (12)(13)(14) | 3변수 기울기와 계산 공식 / Gradient in Space | $(12)$ $D_{\mathbf u}f=f_x a+f_y b+f_z c$; $(13)$ $\nabla f=\langle f_x,f_y,f_z\rangle=\dfrac{\partial f}{\partial x}\mathbf i+\dfrac{\partial f}{\partial y}\mathbf j+\dfrac{\partial f}{\partial z}\mathbf k$; $(14)$ $D_{\mathbf u}f(x,y,z)=\nabla f(x,y,z)\cdot\mathbf u$ | 1074 | Theorem 3과 같은 방법 | — |
| 11 | thm | Theorem 15 | 방향도함수의 최대화 / Maximizing the Directional Derivative | $f$가 미분가능일 때 $D_{\mathbf u}f(\mathbf x)$의 **최댓값은 $\lvert\nabla f(\mathbf x)\rvert$** 이고, $\mathbf u$가 $\nabla f(\mathbf x)$와 같은 방향일 때 달성된다 | 1075 | 본문 ($D_{\mathbf u}f=\lvert\nabla f\rvert\lvert\mathbf u\rvert\cos\theta=\lvert\nabla f\rvert\cos\theta$, $\cos\theta\le1$) | — |
| 12 | note | ■ Tangent Planes to Level Surfaces | 등위곡면의 접평면 유도 / Setting Up Tangent Planes to Level Surfaces | $S:F(x,y,z)=k$ 위의 곡선 $\mathbf r(t)$에 대해 $(16)$ $F(x(t),y(t),z(t))=k$. 연쇄법칙으로 $(17)$ $F_x x'+F_y y'+F_z z'=0$, 즉 $\nabla F\cdot\mathbf r'(t)=0$이고 $(18)$ $\nabla F(x_0,y_0,z_0)\cdot\mathbf r'(t_0)=0$. 따라서 $\nabla F(P)$는 $S$ 위 모든 곡선의 접벡터에 수직 → 이를 **법선벡터**로 삼아 접평면을 정의한다 | 1077 | 본문 | Fig 10 |
| 13 | thm | Equation (19) | 등위곡면의 접평면 / Tangent Plane to a Level Surface | $(19)$ $F_x(x_0,y_0,z_0)(x-x_0)+F_y(x_0,y_0,z_0)(y-y_0)+F_z(x_0,y_0,z_0)(z-z_0)=0$ | 1077 | (18)과 평면의 표준형 | — |
| 14 | thm | Equation (20) | 법선 / The Normal Line | $S$의 $P$에서의 **법선**은 $P$를 지나고 접평면에 수직인 직선. 방향벡터는 $\nabla F(P)$이므로 대칭방정식은 $(20)$ $\dfrac{x-x_0}{F_x(P)}=\dfrac{y-y_0}{F_y(P)}=\dfrac{z-z_0}{F_z(P)}$ | 1077 | — | — |
| 15 | rem | $z=f(x,y)$ 특수 경우 | §14.4와의 일관성 / Consistency with §14.4 | $z=f(x,y)$는 $F(x,y,z)=f(x,y)-z=0$의 등위곡면($k=0$). $F_x=f_x$, $F_y=f_y$, $F_z=-1$이므로 $(19)$가 $(14.4.2)$로 환원된다 — 새 정의는 §14.4의 정의를 포함한다 | 1078 | — | — |
| 16 | rem | Properties of the Gradient Vector (요약 박스) | 기울기벡터의 성질 / Properties of the Gradient | $\nabla f(\mathbf x)\neq\mathbf 0$일 때: ① $D_{\mathbf u}f(\mathbf x)=\nabla f(\mathbf x)\cdot\mathbf u$; ② $\nabla f(\mathbf x)$는 $f$가 **가장 빠르게 증가하는 방향**이고 그 최대 변화율은 $\lvert\nabla f(\mathbf x)\rvert$; ③ $\nabla f(\mathbf x)$는 $\mathbf x$를 지나는 **등위곡선/등위곡면에 수직** | 1079 | — | Fig 12 |
| 17 | note | ■ Significance of the Gradient Vector | 기울기의 의미와 최급경사 곡선 / Steepest Ascent and Gradient Fields | 등위곡면 위를 움직이면 $f$가 전혀 변하지 않으므로, 수직 방향으로 움직일 때 최대 증가가 일어난다는 것은 직관적으로 자연스럽다. 지형도에서 등고선에 수직인 곡선이 **최급경사(steepest ascent) 곡선**. 각 점 $(a,b)$에 $\nabla f(a,b)$를 그린 것이 **기울기 벡터장**이며, 벡터들은 "오르막"을 향하고 등위선에 수직이다 | 1079 | — | Fig 13, Fig 14 |
| 18 | fig | Figure 3 | 방향도함수의 기하 / Geometry of $D_{\mathbf u}f$ | 곡면 $S$, 수직평면, 곡선 $C$, 접선 $T$, $\overrightarrow{P'Q'}=h\mathbf u$ | 1070 | — | 필수 |
| 19 | fig | Figure 10 | $\nabla F$와 접평면 / $\nabla F$ ⟂ Level Surface | 등위곡면 $S$, 그 위의 곡선 $C$, $\mathbf r'(t_0)$, 접평면, 법선벡터 $\nabla F(P)$ | 1077 | — | 필수 |
| 20 | fig | Figure 12 | $\nabla f$와 등위곡선 / $\nabla f$ ⟂ Level Curve | 등위곡선 $f(x,y)=k$와 그에 수직인 $\nabla f(x_0,y_0)$ | 1079 | — | 필수 |

카드 수: note 5, def 3, thm 6, rem 3, fig 3 — 합계 **20개**(fig 제외 시 17개).

## B. 예제 기준값

| Example | PDF 쪽 | 유형 | 문제 요지 (재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1071 | 해석·응용 | From the isothermal weather map, estimate the directional derivative of the temperature at Reno in the southeast direction. | $\mathbf u=(\mathbf i-\mathbf j)/\sqrt2$ 방향으로 등온선 $T=50$과 $T=60$ 사이 거리 약 $75$ mi ⟹ $D_{\mathbf u}T\approx\dfrac{60-50}{75}=\dfrac{10}{75}\approx0.13\;^\circ\text{F/mi}$ | $10/75=2/15=0.1333$ | ✔ | 지도 판독값이므로 근사치 |
| 2 | 1072 | 계산 | For $f(x,y)=x^3-3xy+4y^2$ and $\mathbf u$ at angle $\theta=\pi/6$ from the positive $x$-axis, find $D_{\mathbf u}f(x,y)$ and $D_{\mathbf u}f(1,2)$. | $D_{\mathbf u}f=\tfrac12\big[3\sqrt3\,x^2-3x+(8-3\sqrt3)y\big]$; $D_{\mathbf u}f(1,2)=\dfrac{13-3\sqrt3}{2}$ | sympy: $\nabla f\cdot\langle\cos\tfrac\pi6,\sin\tfrac\pi6\rangle$이 교재 식과 항등적으로 일치, $(1,2)$에서 $\tfrac{13}{2}-\tfrac{3\sqrt3}{2}=3.9019238$. Definition 2의 극한 정의로도 교차검증 일치 | ✔ | — |
| 3 | 1073 | 계산 | If $f(x,y)=\sin x+e^{xy}$, find $\nabla f$ and $\nabla f(0,1)$. | $\nabla f=\langle\cos x+ye^{xy},\;xe^{xy}\rangle$; $\nabla f(0,1)=\langle2,0\rangle$ | sympy: 동일, $\nabla f(0,1)=\langle2,0\rangle$ | ✔ | — |
| 4 | 1073 | 계산 | Find the directional derivative of $f(x,y)=x^2y^3-4y$ at $(2,-1)$ in the direction of $\mathbf v=2\mathbf i+5\mathbf j$. | $\nabla f=2xy^3\mathbf i+(3x^2y^2-4)\mathbf j$, $\nabla f(2,-1)=-4\mathbf i+8\mathbf j$; $\lvert\mathbf v\rvert=\sqrt{29}$, $\mathbf u=\tfrac{2}{\sqrt{29}}\mathbf i+\tfrac{5}{\sqrt{29}}\mathbf j$; $D_{\mathbf u}f(2,-1)=\dfrac{32}{\sqrt{29}}$ | sympy: $\nabla f(2,-1)=\langle-4,8\rangle$, $D_{\mathbf u}f=\dfrac{32\sqrt{29}}{29}=5.9422508$ | ✔ | $\mathbf v$가 단위벡터가 아니므로 반드시 정규화 |
| 5 | 1074–1075 | 계산 | For $f(x,y,z)=x\sin yz$: (a) find $\nabla f$; (b) find the directional derivative at $(1,3,0)$ in the direction of $\mathbf v=\mathbf i+2\mathbf j-\mathbf k$. | (a) $\nabla f=\langle\sin yz,\;xz\cos yz,\;xy\cos yz\rangle$; (b) $\nabla f(1,3,0)=\langle0,0,3\rangle$, $\mathbf u=\tfrac{1}{\sqrt6}\langle1,2,-1\rangle$, $D_{\mathbf u}f=-\dfrac{3}{\sqrt6}=-\sqrt{\dfrac32}$ | sympy: (a) 동일; (b) $\nabla f(1,3,0)=\langle0,0,3\rangle$, $D_{\mathbf u}f=-\dfrac{\sqrt6}{2}=-1.2247449=-\sqrt{3/2}$ | ✔ | — |
| 6 | 1075–1076 | 계산 | For $f(x,y)=xe^{y}$: (a) find the rate of change at $P(2,0)$ toward $Q\!\left(\tfrac12,2\right)$; (b) find the direction of maximum increase and that maximum rate. | (a) $\nabla f(2,0)=\langle1,2\rangle$, $\overrightarrow{PQ}=\langle-\tfrac32,2\rangle$, $\mathbf u=\langle-\tfrac35,\tfrac45\rangle$, $D_{\mathbf u}f(2,0)=1$; (b) 방향 $\nabla f(2,0)=\langle1,2\rangle$, 최대 변화율 $\sqrt5$ | sympy: $\lvert\overrightarrow{PQ}\rvert=\tfrac52$, $\mathbf u=\langle-\tfrac35,\tfrac45\rangle$, $D_{\mathbf u}f=1$, $\lvert\nabla f(2,0)\rvert=\sqrt5=2.2360680$ | ✔ | pdftotext가 $Q(\tfrac12,2)$를 "Q(21,2)"로 오독. PNG p-1075로 $Q\!\left(\tfrac12,2\right)$ 확인 |
| 7 | 1076 | 계산·응용 | Temperature is $T(x,y,z)=\dfrac{80}{1+x^2+2y^2+3z^2}$ (°C, meters). At $(1,1,-2)$, in which direction does $T$ increase fastest, and what is the maximum rate? | $\nabla T=\dfrac{160}{(1+x^2+2y^2+3z^2)^2}(-x\mathbf i-2y\mathbf j-3z\mathbf k)$; $\nabla T(1,1,-2)=\tfrac58(-\mathbf i-2\mathbf j+6\mathbf k)$ — 즉 $-\mathbf i-2\mathbf j+6\mathbf k$ 방향(단위벡터 $\tfrac{1}{\sqrt{41}}(-\mathbf i-2\mathbf j+6\mathbf k)$); 최대 증가율 $\tfrac58\sqrt{41}\approx4\;^\circ$C/m | sympy: $\nabla T$ 형태 일치, $\nabla T(1,1,-2)=\langle-\tfrac58,-\tfrac54,\tfrac{15}{4}\rangle=\tfrac58\langle-1,-2,6\rangle$, $\lvert\nabla T\rvert=\tfrac{5\sqrt{41}}{8}=4.0019526$ | ✔ | 교재 "$\approx4$"는 $4.0020$의 반올림 |
| 8 | 1077–1078 | 계산 | Find the tangent plane and the normal line to the ellipsoid $\dfrac{x^2}{4}+y^2+\dfrac{z^2}{9}=3$ at $(-2,1,-3)$. | $F_x=\tfrac x2$, $F_y=2y$, $F_z=\tfrac{2z}{9}$; $(-2,1,-3)$에서 $-1,\;2,\;-\tfrac23$. 접평면 $-1(x+2)+2(y-1)-\tfrac23(z+3)=0$ → $3x-6y+2z+18=0$; 법선 $\dfrac{x+2}{-1}=\dfrac{y-1}{2}=\dfrac{z+3}{-2/3}$ | sympy: 편도함수와 값 모두 일치, 접평면 $\times(-3)$ 후 $3x-6y+2z+18=0$; $F(-2,1,-3)=3$ (점이 곡면 위) | ✔ | — |
| 9 | 1078 | 계산 | Find the tangent plane to $z=2x^2+y^2$ at $(1,1,3)$ using the level-surface method. | $F=2x^2+y^2-z$ ($k=0$), $F_x=4x$, $F_y=2y$, $F_z=-1$; $(1,1,3)$에서 $4,2,-1$. $4(x-1)+2(y-1)-(z-3)=0$ → $z=4x+2y-3$ | sympy: 동일, $z=4x+2y-3$ | ✔ | §14.4 Example 1과 같은 답 — 두 정의의 일관성 확인용 |

예제 수: **9개** (계산 7, 계산·응용 1, 해석·응용 1).
※ 지시서에는 "예제 7개"로 되어 있으나 원문에는 Example 1–9로 **9개**가 있다(뒤의 Example 8·9는 등위곡면 접평면·법선 파트).

## C. 그림 필요 목록 (자체 SVG)

| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 1 / Figure 4 | 캘리포니아·네바다 등온선 지도와 Reno에서 남동 방향 직선 | 선택 (간략 도식으로 대체 가능) | 1 / Ex 1 |
| Figure 2 | 단위벡터 $\mathbf u=\langle a,b\rangle$ (평면) | 선택 (매우 단순) | 2 |
| Figure 3 | 곡면 $S$ · 수직평면 · 곡선 $C$ · 접선 $T$ · $\overrightarrow{P'Q'}=h\mathbf u$ | **필수** | 2 (fig 카드 18) |
| Figure 5 | 각 $\theta$로 표현한 단위벡터 $\langle\cos\theta,\sin\theta\rangle$ | 선택 | 5 |
| Figure 7 | $\nabla f(2,-1)$과 $\mathbf v$를 등위선 위에 겹쳐 그림 (Example 4) | 선택 | Ex 4 |
| Figure 8 | $f=xe^y$의 등위선과 $\nabla f(2,0)$ (등위선에 수직) | 선택 | Ex 6 |
| Figure 10 | 등위곡면 $S$, 곡선 $C$, $\mathbf r'(t_0)$, 접평면, $\nabla F(P)$ | **필수** | 12 (fig 카드 19) |
| Figure 12 | 등위곡선 $f(x,y)=k$와 수직인 $\nabla f(x_0,y_0)$ | **필수** | 16 (fig 카드 20) |
| Figure 13 | 지형도의 최급경사 곡선(등고선에 수직) | 선택 | 17 |
| Figure 14 | $f=x^2-y^2$의 기울기 벡터장 + 등위선 | 선택 (설명력 큼) | 17 |

## D. ERRATA·판독 불확실

- pdftotext가 그리스 문자 $\theta$를 통째로 날려서 `u − k cos , sin l`처럼 나온다. PNG로 $\mathbf u=\langle\cos\theta,\sin\theta\rangle$ 확인.
- **Example 6의 점 $Q$**: 텍스트에는 `Q ( 21, 2)`로 나오는데 PNG p-1075에서 $Q\!\left(\tfrac12,2\right)$임을 확인했다. $\overrightarrow{PQ}=\langle-\tfrac32,2\rangle$, $\lvert\overrightarrow{PQ}\rvert=\tfrac52$라야 교재의 $\mathbf u=\langle-\tfrac35,\tfrac45\rangle$과 맞는다. ($Q(-1,2)$로 읽으면 $\mathbf u=\langle-3,2\rangle/\sqrt{13}$이 되어 답이 달라진다.)
- Definition 2 / Definition 10의 라벨이 `Definitio`로 보인다 — PNG에서도 동일한, PDF 자체의 글리프 누락. 실제 단어는 `Definition`.
- Example 7의 $\nabla T$에서 pdftotext가 부호를 `2`로 뭉개어 `(2x i 2 2y j 2 3z k)`로 보이나, 실제는 $(-x\mathbf i-2y\mathbf j-3z\mathbf k)$. sympy 재계산으로 확정.
- 교재 오류 없음. 재계산 9/9 일치.

## E. 절 요약 (사이트 도입 note 초안)

편도함수 $f_x,f_y$는 $x$축·$y$축 방향의 변화율만 알려 준다. 임의의 단위벡터 $\mathbf u=\langle a,b\rangle$ 방향의 변화율이 **방향도함수** $D_{\mathbf u}f$이며, $f$가 미분가능하면 $D_{\mathbf u}f=f_x a+f_y b$로 간단히 계산된다. 이 식은 $\nabla f=\langle f_x,f_y\rangle$라는 **기울기벡터**와 $\mathbf u$의 내적, 즉 $D_{\mathbf u}f=\nabla f\cdot\mathbf u$로 쓸 수 있고, 여기서 기울기벡터의 두 가지 핵심 성질이 따라 나온다. 첫째, $\lvert\nabla f\rvert\lvert\mathbf u\rvert\cos\theta$ 형태이므로 $f$는 $\nabla f$ 방향으로 가장 빠르게 증가하며 그 최대 증가율이 정확히 $\lvert\nabla f\rvert$다. 둘째, 등위곡면 $F(x,y,z)=k$ 위의 곡선을 연쇄법칙으로 미분하면 $\nabla F\cdot\mathbf r'=0$이므로 $\nabla F$는 등위곡선·등위곡면에 수직이고, 이를 법선벡터로 삼아 접평면 $F_x(x-x_0)+F_y(y-y_0)+F_z(z-z_0)=0$과 법선을 얻는다. 이 정의는 $z=f(x,y)$일 때 §14.4의 접평면 공식으로 정확히 환원된다.

## F. 공통과제 문항 (1차 공통과제)

- 과제 제출 문항: **17, 30, 34, 45, 51, 62**
- 학습 참고 문항: **4~7, 8~12, 13~19, 21~25, 27~32, 35, 38, 45~46, 47~52, 55~69**
