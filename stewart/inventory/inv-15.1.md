# §15.1 Double Integrals over Rectangles — PDF p.1113–1125 (인쇄 p.1076–1088)

## A. 카드 인벤토리 (원문 순서)

| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입) + Review of the Definite Integral | 정적분의 복습 / Review of the Definite Integral | 넓이 문제 → 정적분과 같은 방식으로 부피 문제 → 이중적분. $[a,b]$를 $n$등분($\Delta x=(b-a)/n$)하고 표본점 $x_i^*$에서 리만 합 (1) $\sum_{i=1}^n f(x_i^*)\Delta x$, 극한이 (2) $\int_a^b f(x)\,dx=\lim_{n\to\infty}\sum_{i=1}^n f(x_i^*)\Delta x$. $f\ge 0$이면 곡선 아래 넓이 | 1113 | — | Fig 1 |
| 2 | note | Volumes and Double Integrals | 부피와 이중적분 / Volumes and Double Integrals | $R=[a,b]\times[c,d]$, $f\ge0$, $S=\{(x,y,z): 0\le z\le f(x,y),\,(x,y)\in R\}$. $[a,b]$를 $m$등분·$[c,d]$를 $n$등분해 부분직사각형 $R_{ij}=[x_{i-1},x_i]\times[y_{j-1},y_j]$, $\Delta A=\Delta x\,\Delta y$. 표본점 $(x_{ij}^*,y_{ij}^*)$의 기둥 부피 $f(x_{ij}^*,y_{ij}^*)\Delta A$를 더해 (3) $V\approx\sum_{i=1}^m\sum_{j=1}^n f(x_{ij}^*,y_{ij}^*)\Delta A$, 극한으로 (4) $V=\lim_{m,n\to\infty}\sum\sum f(x_{ij}^*,y_{ij}^*)\Delta A$를 **부피의 정의**로 삼음 | 1113–1115 | — | Fig 2, 3, 4, 5 |
| 3 | def | Definition 5 | 이중적분의 정의 / Definition of the Double Integral | (5) $\displaystyle\iint_R f(x,y)\,dA=\lim_{m,n\to\infty}\sum_{i=1}^m\sum_{j=1}^n f(x_{ij}^*,y_{ij}^*)\,\Delta A$ (극한이 존재할 때). 이 합을 **이중 리만 합**이라 함 | 1115–1116 | — | — |
| 4 | rem | (Definition 5 뒤 단락, 여백 주석 포함) | 극한의 정확한 뜻과 적분가능성 / Precise Meaning and Integrability | 임의의 $\varepsilon>0$에 대해 $m,n>N$이고 표본점을 어떻게 잡아도 $\left|\iint_R f\,dA-\sum\sum f(x_{ij}^*,y_{ij}^*)\Delta A\right|<\varepsilon$인 $N$이 존재. 연속함수는 모두 적분가능; 더 일반적으로 $f$가 $R$에서 유계이고 불연속점이 유한 개의 매끄러운 곡선 위에만 있으면 적분가능. 크기가 다른 부분직사각형을 써도 되지만 모든 변의 길이가 $0$으로 가야 함 | 1115 | — | — |
| 5 | rem | 식 (6) | 오른쪽 위 꼭짓점 표본점 / Upper Right-Corner Sample Points | 표본점을 $R_{ij}$의 오른쪽 위 꼭짓점 $(x_i,y_j)$로 잡으면 (6) $\iint_R f(x,y)\,dA=\lim_{m,n\to\infty}\sum_{i=1}^m\sum_{j=1}^n f(x_i,y_j)\,\Delta A$ | 1115 | — | — |
| 6 | thm | (박스: 부피 해석) | 이중적분과 부피 / Volume as a Double Integral | $f(x,y)\ge0$이면 $R$ 위·곡면 $z=f(x,y)$ 아래 입체의 부피는 $V=\iint_R f(x,y)\,dA$ (정의 4와 5의 비교로 즉시) | 1115 | 본문(정의로부터) | — |
| 7 | rem | Midpoint Rule 박스 | 이중적분의 중점법칙 / Midpoint Rule for Double Integrals | $\iint_R f(x,y)\,dA\approx\sum_{i=1}^m\sum_{j=1}^n f(\bar x_i,\bar y_j)\,\Delta A$, 여기서 $\bar x_i$는 $[x_{i-1},x_i]$의, $\bar y_j$는 $[y_{j-1},y_j]$의 중점 | 1117 | — | Fig 10 |
| 8 | note | Iterated Integrals | 반복적분 / Iterated Integrals | $x$를 고정하고 $y$에 대해 적분하는 **부분적분(partial integration)** $A(x)=\int_c^d f(x,y)\,dy$. (7) $\int_a^b A(x)\,dx=\int_a^b\!\left[\int_c^d f(x,y)\,dy\right]dx$, 괄호를 생략해 (8) $\int_a^b\!\int_c^d f(x,y)\,dy\,dx$, 순서를 바꾼 (9) $\int_c^d\!\int_a^b f(x,y)\,dx\,dy$. 항상 **안쪽부터** 계산 | 1118 | — | — |
| 9 | thm | Theorem 10 (Fubini's Theorem) | 푸비니 정리 / Fubini's Theorem | $f$가 $R=\{(x,y):a\le x\le b,\ c\le y\le d\}$에서 연속이면 $\iint_R f\,dA=\int_a^b\!\int_c^d f(x,y)\,dy\,dx=\int_c^d\!\int_a^b f(x,y)\,dx\,dy$. 더 일반적으로 $f$가 유계이고 불연속점이 유한 개의 매끄러운 곡선에만 있으며 반복적분이 존재해도 성립 | 1119 | 정식 증명은 생략; 본문에 $f\ge0$일 때 단면적 $A(x)$를 이용한 직관적 근거($V=\int_a^b A(x)\,dx$) | Fig 11, 12 |
| 10 | rem | Example 5·6 옆 주석 | 부호가 바뀌는 함수의 이중적분 / Sign and Volume Interpretation | 이중적분이 음수여도 문제 없음 — 부피 해석은 $f>0$일 때만 유효. 일반적으로 $\iint_R f\,dA=V_1-V_2$ ($V_1$은 $R$ 위·그래프 아래, $V_2$는 $R$ 아래·그래프 위 부피). 또 적분 순서는 더 쉬운 쪽을 고르는 것이 현명(예 6은 $x$ 먼저가 훨씬 쉬움) | 1120 | — | Fig 13, 14 |
| 11 | thm | 식 (11) | 분리형 피적분함수의 곱 공식 / Product of Single Integrals | $f(x,y)=g(x)h(y)$이고 $R=[a,b]\times[c,d]$이면 (11) $\iint_R g(x)h(y)\,dA=\left(\int_a^b g(x)\,dx\right)\left(\int_c^d h(y)\,dy\right)$ | 1121 | 본문(푸비니 정리에서 $h(y)$를 상수로 빼내어 유도) | — |
| 12 | def | Average Value 절 | 이중적분의 평균값 / Average Value over a Rectangle | $f_{\text{avg}}=\dfrac{1}{A(R)}\iint_R f(x,y)\,dA$ ($A(R)$은 $R$의 넓이). $f\ge0$이면 $A(R)\cdot f_{\text{avg}}=\iint_R f\,dA$ — 밑면 $R$, 높이 $f_{\text{avg}}$인 상자가 곡면 아래 입체와 같은 부피 | 1122 | — | Fig 17 |
| 13 | fig | Figure 3 | 부분직사각형 분할 / Subdividing $R$ | 격자로 나눈 $R_{ij}$, $\Delta x,\Delta y$, 표본점 $(x_{ij}^*,y_{ij}^*)$ 표시 — 정의 이해에 필수 | 1114 | — | — |

카드 수: note 3, def 2, thm 3, rem 4, fig 1 = **13**

## B. 예제 기준값

| Example | PDF 쪽 | 유형 | 문제 요지 (영어 재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1116 | 계산 | Approximate the volume beneath the elliptic paraboloid $z=16-x^2-2y^2$ over the square $R=[0,2]\times[0,2]$ using four congruent subsquares and upper right-corner samples; sketch the solid and the boxes. | $V\approx 34$ | $f(1,1)+f(1,2)+f(2,1)+f(2,2)=13+7+10+4=34$ (sympy) | ✔ | 참값은 예제 7의 $48$. 세분화 시 $41.5\ (m=n=4)$, $44.875\ (8)$, $46.46875\ (16)$ |
| 2 | 1116–1117 | 해석·응용 | Evaluate $\iint_R\sqrt{1-x^2}\,dA$ on $R=[-1,1]\times[-2,2]$ by recognizing it as a volume rather than integrating from the definition. | $2\pi$ | $\int_{-2}^{2}\!\int_{-1}^{1}\sqrt{1-x^2}\,dx\,dy=2\pi\approx6.28319$ (sympy) | ✔ | 반원기둥 $x^2+z^2=1,\ z\ge0$의 부피 $=\tfrac12\pi(1)^2\cdot4$ |
| 3 | 1117 | 계산 | Use the Midpoint Rule with $m=n=2$ to approximate $\iint_R(x-3y^2)\,dA$ over $R=[0,2]\times[1,2]$. | $-\dfrac{95}{8}=-11.875$ | 중점 $\bar x=\tfrac12,\tfrac32$, $\bar y=\tfrac54,\tfrac74$, $\Delta A=\tfrac12$: $-\tfrac{380}{16}\cdot\tfrac12=-\tfrac{95}{8}$ (sympy) | ✔ | 참값 $-12$(예제 5). 세분 시 $-11.5,\,-11.875,\,-11.9687,\,-11.9922,\,-11.9980,\,-11.9995$ |
| 4 | 1118–1119 | 계산 | Compute the two iterated integrals of $x^2y$ over $0\le x\le3,\ 1\le y\le2$, once in each order. | (a) $\dfrac{27}{2}$; (b) $\dfrac{27}{2}$ | (a) $27/2$; (b) $27/2$ (sympy) | ✔ | 두 순서가 같음 → 푸비니 정리의 예시. 중간 함수 $A(x)=\tfrac32x^2$ |
| 5 | 1120 | 계산 | Evaluate $\iint_R(x-3y^2)\,dA$ exactly on $R=[0,2]\times[1,2]$ by Fubini's Theorem in both orders (compare Example 3). | $-12$ (두 순서 모두) | $dy\,dx$: $-12$; $dx\,dy$: $-12$ (sympy) | ✔ | 음수 값 — $f$가 $R$에서 항상 음수이므로 부피가 아님 |
| 6 | 1120 | 계산 | Evaluate $\iint_R y\sin(xy)\,dA$ on $R=[1,2]\times[0,\pi]$, choosing the easier order of integration. | $0$ | $dx\,dy$: $0$; $dy\,dx$: $0$ (sympy) | ✔ | $x$ 먼저가 쉬움 ($\int y\sin(xy)dx=-\cos(xy)$); $y$ 먼저면 부분적분 2회. 답 $0$ ⇒ $V_1=V_2$ |
| 7 | 1121 | 계산 | Find the volume of the solid bounded by $x^2+2y^2+z=16$, the planes $x=2$, $y=2$, and the three coordinate planes. | $48$ | $\int_0^2\!\int_0^2(16-x^2-2y^2)\,dx\,dy=48$ (sympy) | ✔ | 예제 1의 참값 확인 |
| 8 | 1121 | 계산 | Use the product formula (11) to evaluate $\iint_R\sin x\cos y\,dA$ on $R=[0,\pi/2]\times[0,\pi/2]$. | $1$ | 이중적분 $1$, 곱 형태 $\left(\int_0^{\pi/2}\sin x\,dx\right)\left(\int_0^{\pi/2}\cos y\,dy\right)=1\cdot1=1$ (sympy) | ✔ | $f>0$이므로 부피 해석 가능 |
| 9 | 1122–1123 | 해석·응용 | From a contour map of the 20–21 Dec 2006 Colorado snowfall (state modeled as a $388\times276$ mi rectangle), estimate the statewide average snowfall with the Midpoint Rule, $m=n=4$. | $f_{\text{avg}}\approx 12.9$ in (약 13인치) | 16개 표본합 $=207$, $\Delta A=\tfrac{388\cdot276}{16}=6693$ mi², 적분 $\approx1{,}385{,}451$, $f_{\text{avg}}=\tfrac{207}{16}=12.9375$ (sympy) | ✔ | 등고선에서 읽은 표본값 $0,15,8,7,2,25,18.5,11,4.5,28,17,13.5,12,15,17.5,13$ (교재 본문 나열 그대로). $\Delta A$가 약분되어 $f_{\text{avg}}=$ (표본 평균) |

예제 수: **9** (계산 6, 해석·응용 2 [Ex 2, 9], 계산+해석 혼합 없음 — Ex 1은 계산/스케치 혼합)

## C. 그림 필요 목록 (자체 SVG)

| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 1 | 1변수 리만 합: 곡선 $y=f(x)$와 근사 직사각형, $\Delta x$, 표본점 $x_i^*$ | 선택 | 1 |
| Figure 2 | $R$ 위 곡면 $z=f(x,y)$와 그 아래 입체 $S$ | 선택 | 2 |
| Figure 3 | $R$의 격자 분할: $R_{ij}$, $\Delta x$, $\Delta y$, 표본점 $(x_{ij}^*,y_{ij}^*)$ | **필수** | 13 (=2) |
| Figure 4·5 | 부분직사각형 위 기둥 1개 / 기둥 전체 근사 | 선택 | 2 |
| Figure 6 | $[0,2]^2$의 네 정사각형과 오른쪽 위 꼭짓점 $(1,1),(1,2),(2,1),(2,2)$ | **필수** | 예제 1 |
| Figure 7·8 | 근사 상자 그림 / $m=n=4,8,16$ 수렴 그림 | 선택 | 예제 1 |
| Figure 9 | 원기둥 $x^2+z^2=1$ 아래·$R$ 위 반원기둥 입체 | 선택 | 예제 2 |
| Figure 10 | $[0,2]\times[1,2]$의 네 부분직사각형과 중점 $(\tfrac12,\tfrac54)$ 등 | **필수** | 7 (중점법칙), 예제 3 |
| Figure 11·12 | 푸비니 직관: $x$에 수직인 단면 $A(x)$ / $y$에 수직인 단면 | **필수**(11만) | 9 |
| Figure 13 | 평면 $z=x-3y^2$가 $R$ 아래에 있음 | 선택 | 10 |
| Figure 14 | $z=y\sin(xy)$의 위·아래 부피가 상쇄 | 선택 | 10 |
| Figure 15 | 타원포물면과 상자 영역이 자르는 입체 | 선택 | 예제 7 |
| Figure 16 | $z=\sin x\cos y$ 위 입체 | 선택 | 예제 8 |
| Figure 17 | 평균값: 산봉우리를 잘라 골을 메우는 그림 | 선택 | 12 |
| Figure 18·19 | 콜로라도 강설량 등고선도 / 16분할 격자 | 선택(원 그림 대체 어려움 — 표로 대체 권장) | 예제 9 |

## D. ERRATA·판독 불확실
- 없음. pdftotext 인코딩 훼손(괄호 `s…d`, 적분기호 `y`, 등호 `−`, 빼기 `2`)은 문맥으로 모두 복원했고 수치는 sympy로 전부 검증됨.
- 예제 9의 16개 표본값은 등고선도에서 눈으로 읽은 값이므로 교재 본문에 나열된 수열을 그대로 기준값으로 삼음(합 $207$).

## E. 절 요약 (사이트 도입 note 초안)
1변수에서 넓이 문제가 정적분을 낳았듯, 직사각형 $R=[a,b]\times[c,d]$ 위 곡면 아래 입체의 부피 문제가 이중적분을 낳는다. $R$을 격자로 나누어 각 부분직사각형에서 표본점을 골라 만든 이중 리만 합의 극한이 곧 이중적분 $\iint_R f\,dA$이며, $f\ge0$일 때 이 값은 입체의 부피이고 부호가 바뀌면 위·아래 부피의 차가 된다. 정의만으로 계산하기는 어렵지만 **푸비니 정리**가 이중적분을 두 번의 1변수 적분(반복적분)으로 바꿔 주며, 두 적분 순서 중 계산이 쉬운 쪽을 골라도 된다. 피적분함수가 $g(x)h(y)$로 분리되면 이중적분은 두 정적분의 곱으로 간단해진다. 수치적으로는 중점법칙이, 개념적으로는 평균값 $f_{\text{avg}}=\frac{1}{A(R)}\iint_R f\,dA$가 이 절의 나머지 두 축이다.

## F. 공통과제 문항 (2차 공통과제)
- **과제 제출 문항**: (없음 — 표에 미지정)
- **학습 참고 문항**: 20, 21, 22, 24, 25, 29, 30, 32, 33, 45, 46, 47, 49, 53, 55
