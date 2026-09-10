# §14.8 Lagrange Multipliers — PDF p.1095–1104 (인쇄 p.1058–1067)

본문 PDF p.1095–1101(인쇄 1058–1064), 연습문제 PDF p.1101–1104(인쇄 1064–1067).

## A. 카드 인벤토리 (원문 순서)

| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입) | 제약이 있는 최적화 / Optimization with a Side Condition | §14.7 Example 6에서 부피 $V=xyz$를 제약 $2xz+2yz+xy=12$ 아래 최대화했다. 이 절에서는 $f(x,y,z)$를 제약(side condition) $g(x,y,z)=k$ 아래 최대·최소화하는 **라그랑주의 방법**을 다룬다 | 1095 | — | — |
| 2 | note | ■ Lagrange Multipliers: One Constraint (기하적 동기) | 등위선이 스치는 순간 / Level Curves That Just Touch | 2변수판: 점이 등위곡선 $g(x,y)=k$ 위에 있을 때 $f(x,y)$의 극값을 찾는다. $f(x,y)=c$인 등위곡선이 $g=k$와 **만나는** 가장 큰 $c$를 찾는 것이고, 그림상 두 곡선이 **접할 때** 일어난다. 접점에서 두 곡선의 법선이 일치하므로 기울기벡터가 평행: $\nabla f(x_0,y_0)=\lambda\nabla g(x_0,y_0)$ | 1095 | — | Fig 1 |
| 3 | thm | Equation (1) | 라그랑주 조건 / The Lagrange Condition | $f$가 $S:g(x,y,z)=k$ 위의 점 $P$에서 극값을 가지면, $S$ 위 $P$를 지나는 곡선 $\mathbf r(t)$에 대해 $h(t)=f(\mathbf r(t))$가 $t_0$에서 극값 ⟹ $h'(t_0)=0=\nabla f(P)\cdot\mathbf r'(t_0)$. 한편 $\nabla g(P)\cdot\mathbf r'(t_0)=0$ (식 14.6.18)이므로 두 기울기벡터는 평행하고, $\nabla g(P)\neq\mathbf 0$이면 $(1)$ $\nabla f(x_0,y_0,z_0)=\lambda\,\nabla g(x_0,y_0,z_0)$인 수 $\lambda$(**라그랑주 승수**)가 존재한다 | 1095–1096 | 본문 (연쇄법칙) | — |
| 4 | rem | 여백 노트 | 라그랑주 / Joseph-Louis Lagrange | 라그랑주 승수는 프랑스-이탈리아 수학자 Joseph-Louis Lagrange(1736–1813)의 이름에서 왔다 (§3.2에 약전) | 1096 | — | — |
| 5 | rem | Method of Lagrange Multipliers (절차 박스) | 라그랑주 승수법 / The Method | $g(x,y,z)=k$ 아래 $f(x,y,z)$의 최대·최소를 찾으려면 (극값이 존재하고 곡면 위에서 $\nabla g\neq\mathbf 0$이라 가정): **1단계** $\nabla f(x,y,z)=\lambda\nabla g(x,y,z)$와 $g(x,y,z)=k$를 만족하는 모든 $x,y,z,\lambda$를 구한다. **2단계** 1단계에서 나온 모든 점에서 $f$를 계산한다 — 가장 큰 값이 최댓값, 가장 작은 값이 최솟값 | 1096 | — | — |
| 6 | note | 성분 형태와 $\lambda=0$ | 성분 방정식과 $\lambda$의 의미 / The Component Equations | 성분으로 쓰면 $f_x=\lambda g_x$, $f_y=\lambda g_y$, $f_z=\lambda g_z$, $g(x,y,z)=k$ — 미지수 4개짜리 방정식 4개(단 $\lambda$의 값 자체는 결론에 필요 없다). 해에서 $\lambda\neq0$이면 $\nabla f$와 $\nabla g$가 평행하고, $\lambda=0$이면 $\nabla f=\mathbf 0$이라 그 점은 $f$ 자체의 임계점이다. 2변수판은 $f_x=\lambda g_x$, $f_y=\lambda g_y$, $g(x,y)=k$의 세 방정식 | 1096 | — | — |
| 7 | rem | 여백 노트 ($\nabla g\neq\mathbf 0$ 가정) | 방법의 전제 / When the Method Can Fail | 유도에서 $\nabla g\neq\mathbf 0$을 가정했다. Exercise 35는 $\nabla g=\mathbf 0$일 때, Exercise 34는 $\nabla g$가 정의되지 않을 때 무엇이 잘못될 수 있는지를 보여 준다 | 1096 | — | — |
| 8 | note | ■ Lagrange Multipliers: Two Constraints (기하) | 두 제약: 곡면들의 교선 위에서 / Two Constraints | $g(x,y,z)=k$와 $h(x,y,z)=c$의 교선 $C$ 위로 점이 제한된다. $\nabla f$는 $C$에 직교하고 $\nabla g$, $\nabla h$도 $C$에 직교하므로, $\nabla f$는 $\nabla g$와 $\nabla h$가 만드는 평면 안에 있다(두 벡터가 $\mathbf 0$이 아니고 평행하지 않다고 가정) | 1100 | 본문 | Fig 7 |
| 9 | thm | Equation (16) | 두 제약의 라그랑주 조건 / Two-Multiplier Condition | $(16)$ $\nabla f(P)=\lambda\,\nabla g(P)+\mu\,\nabla h(P)$. 성분으로 쓰면 $f_x=\lambda g_x+\mu h_x$, $f_y=\lambda g_y+\mu h_y$, $f_z=\lambda g_z+\mu h_z$, $g(x,y,z)=k$, $h(x,y,z)=c$ — 미지수 5개($x,y,z,\lambda,\mu$)짜리 방정식 5개 | 1100 | 본문(위 기하적 논증) | — |
| 10 | fig | Figure 1 | 접하는 등위곡선 / Tangent Level Curves | 제약곡선 $g(x,y)=k$ 위에 $f(x,y)=7,8,9,10,11$의 등위곡선들을 겹쳐 그려, 최댓값에서 두 곡선이 접함을 보인다 | 1095 | — | 필수 |
| 11 | fig | Figure 7 | 두 제약의 기하 / Geometry of Two Constraints | 두 등위곡면 $g=k$, $h=c$의 교선 $C$와 그 위 점 $P$에서의 $\nabla f$, $\nabla g$, $\nabla h$ | 1100 | — | 필수 |

카드 수: note 4, def 0, thm 2, rem 3, fig 2 — 합계 **11개**(fig 제외 시 9개).
※ 이 절에는 번호 붙은 **정의(Definition) 박스가 없다**. 핵심 결과는 식 $(1)$·$(16)$과 절차 박스다.

## B. 예제 기준값

| Example | PDF 쪽 | 유형 | 문제 요지 (재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1096–1097 | 계산 | Find the extreme values of $f(x,y)=x^2+2y^2$ on the circle $x^2+y^2=1$. | $(2)$ $2x=2\lambda x$, $(3)$ $4y=2\lambda y$, $(4)$ $x^2+y^2=1$. $(2)$에서 $x=0$ 또는 $\lambda=1$ ⟹ 후보 $(0,\pm1)$, $(\pm1,0)$. $f(0,\pm1)=2$, $f(\pm1,0)=1$ ⟹ **최댓값 $f(0,\pm1)=2$, 최솟값 $f(\pm1,0)=1$** | sympy(라그랑주 연립 풀이): 후보 $(-1,0),(0,-1),(0,1),(1,0)$; 값 $1,2,2,1$; 최대 $2$, 최소 $1$ | ✔ | 기하적으로 $z=x^2+2y^2$를 $x^2+y^2=1$ 위로 올린 곡선 $C$의 최고·최저점 |
| 2 | 1097–1098 | 계산·응용 | Redo the lidless-box problem (maximize $V=xyz$ subject to $2xz+2yz+xy=12$) with Lagrange multipliers. | $(5)$ $yz=\lambda(2z+y)$, $(6)$ $xz=\lambda(2z+x)$, $(7)$ $xy=\lambda(2x+2y)$, $(8)$ 제약. 각각 $x,y,z$를 곱해 $(9)(10)(11)$을 얻고 비교하면 $x=y$, $y=2z$. $(8)$에 넣어 $12z^2=12$ ⟹ $z=1$, $x=y=2$ ⟹ **최대 부피 $4\ \mathrm{m^3}$** | sympy: 양의 해는 $(x,y,z)=(2,2,1)$뿐, $V=4$, 제약값 $12$ 확인 | ✔ | §14.7 Example 6과 동일한 답 — 두 방법의 일관성 확인 |
| 3 | 1098–1099 | 계산 | Find the points on the sphere $x^2+y^2+z^2=4$ closest to and farthest from $(3,1,-1)$. | $f=d^2=(x-3)^2+(y-1)^2+(z+1)^2$, $g=x^2+y^2+z^2=4$. $(12)(13)(14)$에서 $x=\dfrac{3}{1-\lambda}$, $y=\dfrac{1}{1-\lambda}$, $z=-\dfrac{1}{1-\lambda}$. $(15)$에 넣어 $(1-\lambda)^2=\dfrac{11}{4}$, $1-\lambda=\pm\dfrac{\sqrt{11}}{2}$, $\lambda=1\mp\dfrac{\sqrt{11}}{2}$. **가장 가까운 점 $\left(\dfrac{6}{\sqrt{11}},\dfrac{2}{\sqrt{11}},-\dfrac{2}{\sqrt{11}}\right)$, 가장 먼 점 $\left(-\dfrac{6}{\sqrt{11}},-\dfrac{2}{\sqrt{11}},\dfrac{2}{\sqrt{11}}\right)$** | sympy: 실수해가 정확히 그 두 점; $d^2=15-4\sqrt{11}$ (가까움, $d=\sqrt{11}-2=1.3166248$), $d^2=15+4\sqrt{11}$ (멀음, $d=\sqrt{11}+2=5.3166248$). $\lvert(3,1,-1)\rvert=\sqrt{11}=3.3166248$, 반지름 $2$이므로 기하적으로도 $\sqrt{11}\mp2$ | ✔ | 교재는 거리값을 명시하지 않고 점만 제시. 재계산의 $\sqrt{11}\mp2$는 보조 확인값 |
| 4 | 1099–1100 | 계산 | Find the extreme values of $f(x,y)=x^2+2y^2$ on the disk $D=\{(x,y)\mid x^2+y^2\le1\}$. | 절차 $(14.7.9)$: 내부 임계점은 $f_x=2x=0$, $f_y=4y=0$에서 $(0,0)$, $f(0,0)=0$. 경계값은 Example 1에서 $f(\pm1,0)=1$, $f(0,\pm1)=2$. ⟹ **최댓값 $f(0,\pm1)=2$, 최솟값 $f(0,0)=0$** | sympy: 내부 임계점 $(0,0)$, $f=0$; 경계 후보값 $\{1,1,2,2\}$; 최대 $2$, 최소 $0$ | ✔ | 라그랑주법이 §14.7 절차의 "2단계(경계)"를 담당한다는 것이 요점 |
| 5 | 1101 | 계산 | Find the maximum of $f(x,y,z)=x+2y+3z$ on the curve of intersection of the plane $x-y+z=1$ and the cylinder $x^2+y^2=1$. | $(17)$ $1=\lambda+2x\mu$, $(18)$ $2=-\lambda+2y\mu$, $(19)$ $3=\lambda$, $(20)$ $x-y+z=1$, $(21)$ $x^2+y^2=1$. $\lambda=3$ ⟹ $x=-\dfrac{1}{\mu}$, $y=\dfrac{5}{2\mu}$; $(21)$에서 $\mu^2=\dfrac{29}{4}$, $\mu=\pm\dfrac{\sqrt{29}}{2}$ ⟹ $x=\mp\dfrac{2}{\sqrt{29}}$, $y=\pm\dfrac{5}{\sqrt{29}}$, $z=1\pm\dfrac{7}{\sqrt{29}}$, $f=3\pm\sqrt{29}$. **최댓값 $3+\sqrt{29}$** | sympy: 실수해 두 개 — $\left(-\tfrac{2}{\sqrt{29}},\tfrac{5}{\sqrt{29}},1+\tfrac{7}{\sqrt{29}}\right)$에서 $\lambda=3$, $\mu=\tfrac{\sqrt{29}}{2}$, $f=3+\sqrt{29}=8.3851648$; 다른 해에서 $f=3-\sqrt{29}=-2.3851648$. 두 점 모두 제약 두 개를 만족 | ✔ | 최솟값 $3-\sqrt{29}$도 같은 계산에서 나오지만 교재는 최댓값만 묻는다 |

예제 수: **5개** (계산 4, 계산·응용 1).
※ 지시서에는 "예제 3개"로 되어 있으나 원문에는 Example 1–5로 **5개**가 있다(Example 4는 §14.7 절차와의 연결, Example 5가 두 제약 예제).

## C. 그림 필요 목록 (자체 SVG)

| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 1 | 제약곡선 $g(x,y)=k$와 $f=7,8,9,10,11$ 등위곡선 — 최댓값에서 접함 | **필수** (라그랑주법의 직관 전부) | 2 (fig 카드 10) |
| Figure 2 | $z=x^2+2y^2$와 원기둥 $x^2+y^2=1$의 교선 $C$ | 선택 (3D) | Ex 1 |
| Figure 3 | $f=x^2+2y^2$의 등위선과 원 $x^2+y^2=1$이 접하는 그림 | 선택 (2D라 쉬움, Fig 1의 구체화) | Ex 1 |
| Figure 4 | 구 $x^2+y^2+z^2=4$와 최근접점 $P$, 외부점 $(3,1,-1)$ | 선택 | Ex 3 |
| Figure 5 / Figure 6 | 원판 $D$ 위 $f$의 그래프 / $D$에 겹친 등위선도 | 선택 (Fig 6은 2D) | Ex 4 |
| Figure 7 | 교선 $C$ 위 점 $P$에서의 $\nabla f$, $\nabla g$, $\nabla h$ | **필수** | 8 (fig 카드 11) |
| Figure 8 | 원기둥 $x^2+y^2=1$과 평면 $x-y+z=1$이 만드는 타원 | 선택 | Ex 5 |

## D. ERRATA·판독 불확실

- pdftotext가 그리스 문자 $\lambda$, $\mu$를 통째로 날린다(예: `=f sx, y, zd −  =tsx, y, zd`는 실제로 $\nabla f=\lambda\nabla g$). 또 $g$가 `t`로, $\nabla$가 `=`로, $\Leftrightarrow$가 `›?`로 나온다. PNG 및 재계산으로 모두 확정.
- Example 5의 $(17)$ `1 −  1 2x`는 $1=\lambda+2x\mu$. 뒤의 "$2x\mu=-2$, $x=-1/\mu$"와 재계산으로 확인.
- Example 3의 `s1 2 d2 − 11/4`는 $(1-\lambda)^2=\dfrac{11}{4}$.
- 교재 오류 없음. 재계산 5/5 일치.

## E. 절 요약 (사이트 도입 note 초안)

제약조건 $g=k$ 아래에서 $f$의 최대·최소를 찾을 때, 제약을 풀어 변수를 소거하는 대신 기울기벡터를 이용하는 방법이 **라그랑주 승수법**이다. 핵심 직관은 등위곡선 그림에 있다: 제약곡선을 따라가며 $f$의 값을 키우다 보면, 값이 더 이상 커질 수 없는 순간에 $f$의 등위곡선과 제약곡선이 **접한다**. 접점에서는 두 곡선의 법선이 같은 방향이므로 $\nabla f=\lambda\nabla g$가 성립하고, 이 식과 제약식을 함께 푼 뒤 나온 후보점들에서 $f$ 값을 비교하기만 하면 된다. 승수 $\lambda$ 자체의 값은 결론에 필요 없다. 제약이 두 개면 $\nabla f$가 $\nabla g$와 $\nabla h$가 만드는 평면 안에 놓이므로 $\nabla f=\lambda\nabla g+\mu\nabla h$가 되어, 미지수 다섯 개짜리 연립방정식을 풀게 된다. 이 방법은 §14.7의 "닫힌·유계 집합에서 절대극값 찾기" 절차에서 경계 부분을 담당하는 도구이기도 하다.

## F. 공통과제 문항 (2차 공통과제)

- 과제 제출 문항: **7, 11, 27, 33, 57**
- 학습 참고 문항: **6, 12, 28, 31, 32, 61**
