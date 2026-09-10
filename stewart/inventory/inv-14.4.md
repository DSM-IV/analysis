# §14.4 Tangent Planes and Linear Approximations — PDF p.1049–1059 (인쇄 p.1012–1022)

본문 PDF p.1049–1056(인쇄 1012–1019), 연습문제 PDF p.1056–1059(인쇄 1019–1022).

## A. 카드 인벤토리 (원문 순서)

| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입) | 확대하면 평면이 된다 / Zooming In Toward a Point | 1변수에서 그래프를 확대하면 접선과 구별되지 않듯, 미분가능한 $z=f(x,y)$의 그래프를 한 점 근처에서 확대하면 **접평면**과 구별되지 않는다. 따라서 $f$를 2변수 일차함수로 근사할 수 있고, 미분(differential) 개념도 확장된다 | 1049 | — | — |
| 2 | note | ■ Tangent Planes | 접평면의 정의와 유도 / Defining the Tangent Plane | $S:z=f(x,y)$, $P(x_0,y_0,z_0)\in S$. 수직평면 $y=y_0$, $x=x_0$이 $S$와 만나 생긴 곡선 $C_1,C_2$의 $P$에서의 접선 $T_1,T_2$를 모두 포함하는 평면이 **접평면**. $P$를 지나 $S$ 위에 놓인 임의 곡선의 접선도 이 평면에 놓인다(§14.6). $P$를 지나는 평면을 $(1)$ $z-z_0=a(x-x_0)+b(y-y_0)$로 쓰고 $y=y_0$, $x=x_0$을 대입해 $a=f_x(x_0,y_0)$, $b=f_y(x_0,y_0)$을 얻는다 | 1049–1050 | 본문(유도) | Fig 1 |
| 3 | thm | Equation (2) | 접평면의 방정식 / Equation of a Tangent Plane | $f$의 편도함수가 연속이면 $z=f(x,y)$의 $P(x_0,y_0,z_0)$에서의 접평면은 $(2)$ $z-z_0=f_x(x_0,y_0)(x-x_0)+f_y(x_0,y_0)(y-y_0)$ | 1050 | 본문(카드 2에서 유도) | — |
| 4 | rem | 여백 노트 | 접선과의 유비 / Analogy with the Tangent Line | 1변수 접선 $y-y_0=f'(x_0)(x-x_0)$와 $(2)$의 형태가 완전히 대응 | 1050 | — | — |
| 5 | note | ■ Linear Approximations | 선형화와 선형근사 / Linearization and Linear Approximation | $(3)$ $L(x,y)=f(a,b)+f_x(a,b)(x-a)+f_y(a,b)(y-b)$를 $(a,b)$에서 $f$의 **선형화**, $(4)$ $f(x,y)\approx L(x,y)$를 **선형근사(접평면 근사)** 라 한다. 예: $f=2x^2+y^2$, $L(x,y)=4x+2y-3$이면 $L(1.1,0.95)=3.3$ 대 참값 $3.3225$(좋음), $L(2,3)=11$ 대 참값 $17$(나쁨) | 1051 | — | Fig 2, Fig 3 |
| 6 | note | Figure 4 논의 | 편도함수만으로는 부족하다 / Partials May Exist Yet the Graph Behave Badly | $f(x,y)=\dfrac{xy}{x^2+y^2}$ $((x,y)\neq(0,0))$, $f(0,0)=0$은 원점에서 $f_x(0,0)=f_y(0,0)=0$이지만 $f_x,f_y$가 불연속. 선형근사는 $f\approx0$인데 직선 $y=x$ 위에서는 항상 $f=\tfrac12$. 이런 병적 함수를 배제하려고 **미분가능성**을 정의한다 | 1052 | — | Fig 4 |
| 7 | note | 증분 (5)(6) | 증분 $\Delta z$ / The Increment | 1변수: $\Delta y=f(a+\Delta x)-f(a)$이고 미분가능하면 $(5)$ $\Delta y=f'(a)\Delta x+\varepsilon\,\Delta x$, $\varepsilon\to0$. 2변수: $(6)$ $\Delta z=f(a+\Delta x,\,b+\Delta y)-f(a,b)$ | 1052 | — | — |
| 8 | def | Definition 7 | 2변수 함수의 미분가능성 / Differentiability | $z=f(x,y)$가 $(a,b)$에서 **미분가능**하다 $\iff$ $\Delta z=f_x(a,b)\Delta x+f_y(a,b)\Delta y+\varepsilon_1\Delta x+\varepsilon_2\Delta y$ 꼴로 쓸 수 있다. 여기서 $\varepsilon_1,\varepsilon_2$는 $\Delta x,\Delta y$의 함수이고 $(\Delta x,\Delta y)\to(0,0)$일 때 $\varepsilon_1,\varepsilon_2\to0$. 즉 접평면이 그래프를 잘 근사한다는 뜻 | 1052 | — | — |
| 9 | thm | Theorem 8 | 미분가능성의 충분조건 / Sufficient Condition for Differentiability | $f_x,f_y$가 $(a,b)$ 근방에 존재하고 $(a,b)$에서 연속이면 $f$는 $(a,b)$에서 미분가능 | 1052 | Appendix F | — |
| 10 | note | ■ Differentials | 미분(전미분) / Differentials and the Total Differential | 1변수: $dx$는 독립변수, $(9)$ $dy=f'(x)\,dx$. 2변수: $dx,dy$를 독립변수로 두고 **전미분** $(10)$ $dz=f_x(x,y)\,dx+f_y(x,y)\,dy=\dfrac{\partial z}{\partial x}dx+\dfrac{\partial z}{\partial y}dy$ (표기 $df$도 씀). $dx=x-a,\;dy=y-b$로 두면 선형근사는 $f(x,y)\approx f(a,b)+dz$. 기하적으로 $dz$는 접평면의 높이 변화, $\Delta z$는 곡면의 높이 변화 | 1054 | — | Fig 6, Fig 7 |
| 11 | note | ■ Functions of Three or More Variables | 3변수 이상으로의 확장 / Extension to Three or More Variables | 선형근사 $f(x,y,z)\approx f(a,b,c)+f_x(a,b,c)(x-a)+f_y(a,b,c)(y-b)+f_z(a,b,c)(z-c)$, 증분 $\Delta w=f(x+\Delta x,y+\Delta y,z+\Delta z)-f(x,y,z)$, 미분 $dw=\dfrac{\partial w}{\partial x}dx+\dfrac{\partial w}{\partial y}dy+\dfrac{\partial w}{\partial z}dz$ | 1055–1056 | — | — |
| 12 | fig | Figure 1 | 접평면과 두 접선 / Tangent Plane Contains $T_1,T_2$ | 곡면 $S$, 곡선 $C_1,C_2$, 접선 $T_1,T_2$, 점 $P$ — 접평면 정의의 그림 | 1049 | — | 필수 |
| 13 | fig | Figure 7 | $dz$와 $\Delta z$의 기하 / Geometry of $dz$ vs $\Delta z$ | 곡면과 접평면 위에서 $(a,b)\to(a+\Delta x,b+\Delta y)$일 때의 두 높이 변화 비교 | 1054 | — | 필수 |

카드 수: note 6, def 1, thm 2, rem 1, fig 2 — 합계 **12개**(fig 제외 시 10개).

## B. 예제 기준값

| Example | PDF 쪽 | 유형 | 문제 요지 (재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1050 | 계산 | Find the tangent plane to the elliptic paraboloid $z=2x^2+y^2$ at $(1,1,3)$. | $z-3=4(x-1)+2(y-1)$, 즉 $z=4x+2y-3$ | sympy: $f_x=4x,\,f_y=2y$, $f_x(1,1)=4$, $f_y(1,1)=2$, 접평면 $z=4x+2y-3$ | ✔ | §14.6 Example 9에서 level surface 방법으로 재확인 |
| 2 | 1053 | 계산 | Show $f(x,y)=xe^{xy}$ is differentiable at $(1,0)$, find its linearization there, and use it to approximate $f(1.1,-0.1)$. | $f_x=e^{xy}+xye^{xy}$, $f_y=x^2e^{xy}$ 모두 연속 → Thm 8로 미분가능; $L(x,y)=x+y$; $f(1.1,-0.1)\approx1$ (참값 $1.1e^{-0.11}\approx0.98542$) | sympy: $f_x=(xy+1)e^{xy}$, $f_y=x^2e^{xy}$, $f_x(1,0)=f_y(1,0)=1$, $L=x+y$, $L(1.1,-0.1)=1$, 참값 $0.98541755$ | ✔ | — |
| 3 | 1053 | 해석·응용 | Using the National Weather Service heat-index table $I=f(T,H)$, build the linear approximation near $T=96^\circ$F, $H=70\%$ and estimate the heat index at $T=97^\circ$F, $H=72\%$. | $f(T,H)\approx125+3.75(T-96)+0.9(H-70)$; $f(97,72)\approx130.55$ → $I\approx131^\circ$F | sympy: $L=\tfrac{15}{4}T+\tfrac{9}{10}H-298$, $L(97,72)=\tfrac{2611}{20}=130.55$ | ✔ | $f_T\approx3.75$, $f_H\approx0.9$는 §14.3 도입부의 표 추정값을 그대로 사용 |
| 4 | 1054–1055 | 계산 | For $z=f(x,y)=x^2+3xy-y^2$: (a) find $dz$; (b) compare $\Delta z$ and $dz$ when $x$ goes $2\to2.05$ and $y$ goes $3\to2.96$. | (a) $dz=(2x+3y)\,dx+(3x-2y)\,dy$; (b) $dz=0.65$, $\Delta z=0.6449$ | sympy: (a) 동일; (b) $dz=13/20=0.65$, $\Delta z=6449/10000=0.6449$ | ✔ | $dz$가 $\Delta z$에 매우 가깝고 계산이 더 쉽다는 것이 요점 |
| 5 | 1055 | 해석·응용 | A right circular cone is measured as $r=10$ cm, $h=25$ cm, each with error at most $\varepsilon$ cm. (a) Estimate the maximum error in the computed volume by differentials; (b) evaluate it for $\varepsilon=0.1$ cm. | (a) $dV=\dfrac{2\pi rh}{3}dr+\dfrac{\pi r^2}{3}dh$, $\Delta V\approx dV=\dfrac{500\pi}{3}\varepsilon+\dfrac{100\pi}{3}\varepsilon=200\pi\varepsilon$ cm³; (b) $20\pi\approx63$ cm³ (측정 부피 $\approx2618$ cm³ 대비 상대오차 $\approx2.4\%$) | sympy: $dV=\frac{\pi r}{3}(2h\,dr+r\,dh)$, 대입 시 $200\pi\varepsilon$; $\varepsilon=0.1$ → $20\pi=62.8319$; $V=2500\pi/3=2617.99$, 상대오차 $0.0240$ | ✔ | 교재의 "about 63"은 $20\pi=62.83$의 반올림 |
| 6 | 1056 | 해석·응용 | A rectangular box is measured as $75\times60\times40$ cm, each dimension correct to within $\varepsilon$ cm. (a) Estimate the largest error in the computed volume; (b) evaluate for $\varepsilon=0.2$ cm. | (a) $dV=yz\,dx+xz\,dy+xy\,dz$, $\Delta V\approx dV=(2400+3000+4500)\varepsilon=9900\varepsilon$ cm³; (b) $1980$ cm³ (부피의 약 1%) | sympy: $dV=yz\,dx+xz\,dy+xy\,dz=9900\varepsilon$; $\varepsilon=0.2$ → $1980$; $V=180000$, 상대오차 $0.0110$ | ✔ | 교재 "only about 1%" = 정확히 1.1% |

예제 수: **6개** (계산 3, 해석·응용 3).

## C. 그림 필요 목록 (자체 SVG)

| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 1 | 곡면 $S$ 위 점 $P$, 곡선 $C_1,C_2$와 접선 $T_1,T_2$, 이들을 담는 접평면 | 필수 | 2 (fig 카드 12) |
| Figure 2 (a)(b)(c) | $z=2x^2+y^2$과 $(1,1,3)$에서의 접평면 — 확대할수록 일치 | 선택 (3D, 애니메이션/정지 3컷) | 5 |
| Figure 3 | $f=2x^2+y^2$의 등위선을 $(1,1)$ 근처로 확대 → 등간격 평행선에 접근 | 선택 (2D라 SVG로 쉬움) | 5 |
| Figure 4 | $f=xy/(x^2+y^2)$의 3차원 그래프(원점에서 찢어짐) | 선택 | 6 |
| Figure 6 | 1변수 $\Delta y$ 대 $dy$ (곡선 vs 접선) | 선택 (개념 대비용, 2D) | 10 |
| Figure 7 | 3차원 $\Delta z$ 대 $dz$ (곡면 vs 접평면) | 필수 | 10 (fig 카드 13) |
| Figure 8 | $z=x^2+3xy-y^2$ 곡면 (Example 4 시각화) | 선택 | Ex 4 |

## D. ERRATA·판독 불확실

- pdftotext에서 그리스 문자 $\pi$, $\varepsilon$이 자주 탈락한다. Example 5의 `500 100 / 3 3`·`200«`는 PNG(p-1055) 및 재계산으로 $\dfrac{500\pi}{3}\varepsilon+\dfrac{100\pi}{3}\varepsilon=200\pi\varepsilon$임을 확인했다.
- Definition 7의 원문 라벨이 `Definitio`로 보인다. 이는 pdftotext 문제가 아니라 **PDF 렌더링 자체의 글리프 누락**(PNG p-1052에서도 `Definitio`)이며, 실제 단어는 `Definition`이다. 이 책의 모든 Definition 박스에서 동일하게 나타난다.
- 교재 본문 Example 5(b)의 "$dV=200\pi(0.1)\approx63$"은 $62.83$의 반올림. ERRATA 아님.
- 그 외 오류 없음.

## E. 절 요약 (사이트 도입 note 초안)

1변수에서 미분가능한 함수의 그래프를 한 점 근처로 확대하면 접선과 구별되지 않듯이, 2변수 함수 $z=f(x,y)$의 그래프를 확대하면 **접평면**과 구별되지 않는다. 접평면은 그 점을 지나며 곡면 위에 놓인 모든 곡선의 접선을 담는 평면이고, 편도함수가 연속이면 그 방정식은 $z-z_0=f_x(x_0,y_0)(x-x_0)+f_y(x_0,y_0)(y-y_0)$이다. 이 접평면을 나타내는 일차함수 $L(x,y)$를 **선형화**라 부르고 $f(x,y)\approx L(x,y)$를 **선형근사**라 한다. 그런데 편도함수가 존재한다는 것만으로는 이 근사가 좋다는 보장이 없어서($f=xy/(x^2+y^2)$가 반례), 증분 $\Delta z$가 $f_x\Delta x+f_y\Delta y$에 오차항 $\varepsilon_1\Delta x+\varepsilon_2\Delta y$만 더한 꼴로 쓰이는 것을 **미분가능**으로 정의하며, 편도함수가 연속이면 충분하다(Theorem 8). 마지막으로 전미분 $dz=f_x\,dx+f_y\,dy$는 접평면의 높이 변화로서 실제 변화 $\Delta z$의 좋은 근사이고, 오차 추정 같은 응용에 바로 쓰인다.

## F. 공통과제 문항 (1차 공통과제)

- 과제 제출 문항: **8, 17, 27, 37, 40, 41**
- 학습 참고 문항: **3~10, 15~22, 31~38, 42, 53, 54**
