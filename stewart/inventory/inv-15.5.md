# §15.5 Surface Area — PDF p.1154–1156 (인쇄 p.1117–1119)

> 본문은 PDF p.1154 하단에서 시작(그 위는 §15.4 연습문제), 본문·예제 종료 p.1156 중간, 연습문제 p.1156–(1157).

## A. 카드 인벤토리 (원문 순서)

| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입) + 여백 주석 | 곡면넓이 문제 / The Surface Area Problem | §8.2에서 1변수 미적분으로 회전면의 넓이를 구했다면, 여기서는 두 변수 함수의 그래프 $z=f(x,y)$ ($f_x,f_y$ 연속)로 주어진 곡면 $S$의 넓이를 이중적분으로 구한다. (여백 주석: §16.6에서 더 일반적인 **매개곡면**의 넓이를 다루므로, 그 절을 배울 예정이면 이 절은 생략 가능) | 1154 | — | — |
| 2 | note | (유도 1단계) | 접평면 조각에 의한 근사 / Approximation by Tangent-Plane Pieces | 정의역 $D$를 넓이 $\Delta A=\Delta x\,\Delta y$인 작은 직사각형 $R_{ij}$로 나누고, 원점에 가장 가까운 꼭짓점 $(x_i,y_j)$ 위의 점 $P_{ij}(x_i,y_j,f(x_i,y_j))$를 잡는다. $P_{ij}$에서의 접평면 중 $R_{ij}$ 바로 위에 놓인 **평행사변형의 넓이 $\Delta T_{ij}$** 로 곡면 조각 넓이 $\Delta S_{ij}$를 근사 | 1154–1155 | — | Fig 1 |
| 3 | def | Definition (1) | 곡면넓이의 정의 / Definition of Surface Area | (1) $\displaystyle A(S)=\lim_{m,n\to\infty}\sum_{i=1}^m\sum_{j=1}^n \Delta T_{ij}$ | 1155 | — | — |
| 4 | note | (유도 2단계) | 외적으로 $\Delta T_{ij}$ 계산 / Computing $\Delta T_{ij}$ by a Cross Product | 평행사변형의 두 변 벡터 $\mathbf a=\Delta x\,\mathbf i+f_x(x_i,y_j)\Delta x\,\mathbf k$, $\mathbf b=\Delta y\,\mathbf j+f_y(x_i,y_j)\Delta y\,\mathbf k$ (§14.3: $f_x,f_y$가 두 방향 접선의 기울기). 그러면 $\mathbf a\times\mathbf b=[-f_x\,\mathbf i-f_y\,\mathbf j+\mathbf k]\,\Delta A$이고 $\Delta T_{ij}=|\mathbf a\times\mathbf b|=\sqrt{[f_x]^2+[f_y]^2+1}\;\Delta A$ | 1155 | — | Fig 2 |
| 5 | thm | 공식 (2) | 곡면넓이 공식 / Surface Area Formula | (2) $f_x,f_y$가 연속일 때 $z=f(x,y)$, $(x,y)\in D$인 곡면의 넓이는 $\displaystyle A(S)=\iint_D\sqrt{[f_x(x,y)]^2+[f_y(x,y)]^2+1}\;dA$ | 1155 | 본문(카드 2·4의 근사를 (1)에 넣고 이중적분의 정의를 적용) | — |
| 6 | rem | 공식 (3) + 여백 주석 | 편미분 기호 표기와 호의 길이와의 유비 / Alternative Notation, Analogy with Arc Length | (3) $\displaystyle A(S)=\iint_D\sqrt{1+\left(\frac{\partial z}{\partial x}\right)^2+\left(\frac{\partial z}{\partial y}\right)^2}\,dA$. §8.1의 호의 길이 $L=\int_a^b\sqrt{1+\left(\frac{dy}{dx}\right)^2}dx$와 형태가 나란함. 이 공식이 §8.2의 회전면 넓이 공식과 모순 없음은 §16.6에서 확인 | 1155 | — | — |
| 7 | fig | Figure 2 | 접평면 평행사변형 / The Tangent-Plane Parallelogram | $P_{ij}$에서 두 변 벡터 $\mathbf a,\mathbf b$와 넓이 $\Delta T_{ij}$, 밑면 $\Delta x\times\Delta y$ — $\sqrt{f_x^2+f_y^2+1}$의 출처를 보여 주는 그림이라 필수 | 1155 | — | — |

카드 수: note 3, def 1, thm 1, rem 1, fig 1 = **7**

## B. 예제 기준값

| Example | PDF 쪽 | 유형 | 문제 요지 (영어 재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1156 | 계산 | Find the area of the piece of the surface $z=x^2+2y+2$ lying over the triangle in the $xy$-plane with vertices $(0,0)$, $(1,0)$, $(1,1)$. | $\dfrac{1}{12}\left(27-5\sqrt5\right)$ | $T=\{0\le x\le1,\ 0\le y\le x\}$, 피적분함수 $\sqrt{(2x)^2+2^2+1}=\sqrt{4x^2+5}$; $\int_0^1\!\int_0^x\sqrt{4x^2+5}\,dy\,dx=\dfrac94-\dfrac{5\sqrt5}{12}=\dfrac{27-5\sqrt5}{12}\approx1.3183050$ (sympy, 기호적으로 동치 확인) | ✔ | 안쪽 적분 후 $\int_0^1 x\sqrt{4x^2+5}\,dx$ ⇒ $\tfrac18\cdot\tfrac23(4x^2+5)^{3/2}\big|_0^1$ |
| 2 | 1156 | 계산 | Find the area of the part of the paraboloid $z=x^2+y^2$ that lies below the plane $z=9$. | $\dfrac{\pi}{6}\left(37\sqrt{37}-1\right)$ | 밑면은 반지름 3의 원판, 피적분함수 $\sqrt{1+4(x^2+y^2)}$; 극좌표 $\int_0^{2\pi}\!\int_0^3\sqrt{1+4r^2}\,r\,dr\,d\theta=\dfrac{\pi(37\sqrt{37}-1)}{6}\approx117.31870$ (sympy, 기호적으로 동치 확인) | ✔ | 교선 $x^2+y^2=9,\ z=9$. $\tfrac18(1+4r^2)^{1/2}(8r)$ 꼴로 치환 |

예제 수: **2** (모두 계산형)

## C. 그림 필요 목록 (자체 SVG)

| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 1 | 곡면 $S$, 부분직사각형 $R_{ij}$, 그 위의 곡면 조각 $\Delta S_{ij}$와 접평면 조각 $\Delta T_{ij}$ | **필수** | 2 |
| Figure 2 | $P_{ij}$에서의 평행사변형과 두 변 벡터 $\mathbf a,\mathbf b$ | **필수** | 7 (=4) |
| Figure 3 | 예제 1의 삼각형 $T$: $(0,0),(1,0),(1,1)$, 경계 $y=x$ | **필수** | 예제 1 |
| Figure 4 | 예제 1의 곡면 조각(포물기둥 위 삼각 조각) | 선택 | 예제 1 |
| Figure 5 | 예제 2의 포물면과 $z=9$로 잘린 부분, 밑면 반지름 3의 원판 | **필수** | 예제 2 |

## D. ERRATA·판독 불확실
- 없음. 두 예제 모두 sympy와 기호적으로 완전히 일치.
- 이 절은 §16.6(매개곡면)에서 다시 다뤄지므로, 사이트에서 §16.6을 함께 다룰 때는 상호 링크를 걸 것 (교재 여백 주석의 지시).

## E. 절 요약 (사이트 도입 note 초안)
곡면 $z=f(x,y)$의 넓이는 정의역 $D$를 잘게 나누어 각 조각 위에서 곡면을 **접평면 조각(평행사변형)** 으로 바꿔치기하고 그 넓이들을 더한 극한으로 정의한다. 평행사변형의 두 변 벡터가 $\Delta x\,\mathbf i+f_x\Delta x\,\mathbf k$와 $\Delta y\,\mathbf j+f_y\Delta y\,\mathbf k$이므로 외적의 크기에서 곧바로 인자 $\sqrt{f_x^2+f_y^2+1}$이 나오고, 곡면넓이는 $A(S)=\iint_D\sqrt{f_x^2+f_y^2+1}\,dA$가 된다. 이 인자는 1변수의 호의 길이에서 나오는 $\sqrt{1+(dy/dx)^2}$의 2차원판이며, 실제 계산은 §15.2의 제1/제2형 반복적분이나 §15.3의 극좌표(포물면·구면처럼 $x^2+y^2$이 나올 때)로 귀착된다. 더 일반적인 매개곡면의 넓이는 §16.6에서 다룬다.

## F. 공통과제 문항 (2차 공통과제)
- **과제 제출 문항**: 6, 10, 14, 25
- **학습 참고 문항**: 1~2, 3~14, 23, 26
