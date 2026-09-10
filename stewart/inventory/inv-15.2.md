# §15.2 Double Integrals over General Regions — PDF p.1126–1136 (인쇄 p.1089–1099)

> 본문은 PDF p.1126 하단에서 시작(그 위는 §15.1 연습문제), 본문 종료 p.1134 상단, 연습문제 p.1134–1136.

## A. 카드 인벤토리 (원문 순서)

| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입) + General Regions | 일반 영역으로의 확장 / Integrating over General Regions | 1변수에서는 적분 영역이 항상 구간이지만, 이중적분은 직사각형이 아닌 일반 영역에서도 필요. 유계 영역 $D$를 포함하는 직사각형 $R$을 잡고 (1) $F(x,y)=\begin{cases}f(x,y)&(x,y)\in D\\ 0&(x,y)\in R\setminus D\end{cases}$로 확장 | 1126–1127 | — | Fig 1, 2 |
| 2 | def | Definition (2) | 일반 영역 위 이중적분 / Double Integral over a General Region | (2) $\displaystyle\iint_D f(x,y)\,dA=\iint_R F(x,y)\,dA$ ($F$는 (1)). $D$ 밖에서 $F=0$이므로 $D$를 포함하는 $R$을 무엇으로 잡든 값이 같음 | 1127 | — | — |
| 3 | rem | (Definition 2 뒤 단락) | 부피 해석과 적분가능성 / Volume Interpretation, Integrability | $f\ge0$이면 $\iint_D f\,dA$는 $D$ 위·곡면 $z=f(x,y)$ 아래 입체의 부피. $F$는 $D$의 경계에서 불연속일 수 있으나, $f$가 $D$에서 연속이고 경계곡선이 "충분히 좋으면" $\iint_R F\,dA$, 따라서 $\iint_D f\,dA$가 존재 | 1127–1128 | — | Fig 3, 4 |
| 4 | def | type I region | 제1형 영역 / Type I Region | $D=\{(x,y)\mid a\le x\le b,\ g_1(x)\le y\le g_2(x)\}$, $g_1,g_2$는 $[a,b]$에서 연속 (하나의 식일 필요 없음 — 조각적으로 정의된 연속함수 가능) | 1128 | — | Fig 5 |
| 5 | thm | 식 (3) | 제1형 영역의 반복적분 공식 / Iterated Integral over a Type I Region | (3) $f$가 제1형 영역 $D$에서 연속이면 $\displaystyle\iint_D f(x,y)\,dA=\int_a^b\!\!\int_{g_1(x)}^{g_2(x)} f(x,y)\,dy\,dx$. 안쪽 적분에서는 $f$뿐 아니라 **적분 한계에서도** $x$를 상수 취급 | 1128 | 본문($D\subset R$로 확장한 $F$에 푸비니 정리를 적용하고, $y<g_1$ 또는 $y>g_2$에서 $F=0$임을 이용) | Fig 6 |
| 6 | def | type II region | 제2형 영역 / Type II Region | $D=\{(x,y)\mid c\le y\le d,\ h_1(y)\le x\le h_2(y)\}$, $h_1,h_2$ 연속 | 1129 | — | Fig 7 |
| 7 | thm | 식 (4) | 제2형 영역의 반복적분 공식 / Iterated Integral over a Type II Region | (4) $f$가 제2형 영역 $D$에서 연속이면 $\displaystyle\iint_D f(x,y)\,dA=\int_c^d\!\!\int_{h_1(y)}^{h_2(y)} f(x,y)\,dx\,dy$ | 1129 | (3)과 같은 방법 (본문에서 언급만) | Fig 7 |
| 8 | rem | Example 1 뒤 NOTE | 적분 한계를 그림에서 읽는 법 / Reading the Limits from a Sketch | 이중적분을 세울 때 그림은 필수. 제1형은 **세로 화살표**를 아래 경계 $y=g_1(x)$에서 위 경계 $y=g_2(x)$까지 그어 안쪽 적분의 하한·상한을 읽고, 제2형은 왼쪽 경계에서 오른쪽 경계로 **가로 화살표**를 긋는다. 영역이 두 형 모두일 때는 경계가 한 식으로 쓰이는 쪽이 유리(예제 3) | 1129, 1131–1132 | — | Fig 8, 12 |
| 9 | note | Changing the Order of Integration | 적분 순서 바꾸기 / Changing the Order of Integration | 푸비니 정리로 두 순서 모두 가능하지만 한쪽이 훨씬 어렵거나 아예 불가능할 수 있다. 주어진 반복적분을 (3)/(4)을 **거꾸로** 써서 이중적분으로 되돌리고, $D$를 다른 형으로 다시 기술한 뒤 반대 순서로 적분한다 | 1132 | — | Fig 15, 16 |
| 10 | thm | 성질 (5)(6)(7) | 이중적분의 선형성과 비교 / Linearity and Comparison | (5) $\iint_D[f+g]\,dA=\iint_D f\,dA+\iint_D g\,dA$; (6) $\iint_D cf\,dA=c\iint_D f\,dA$ ($c$ 상수); (7) $D$에서 $f\ge g$이면 $\iint_D f\,dA\ge\iint_D g\,dA$ | 1133 | 직사각형에서는 §4.2와 같은 방법, 일반 영역에서는 Definition 2로부터 | — |
| 11 | thm | 성질 (8) | 영역 분할 / Additivity over Subregions | $D=D_1\cup D_2$이고 $D_1,D_2$가 경계에서만 겹치면 (8) $\iint_D f\,dA=\iint_{D_1}f\,dA+\iint_{D_2}f\,dA$. 제1형·제2형 어느 쪽도 아닌 영역을 두 조각으로 나누어 계산할 때 사용 | 1133 | — | Fig 17, 18 |
| 12 | thm | 성질 (9) | 넓이 공식 / Area as a Double Integral | (9) $\displaystyle\iint_D 1\,dA=A(D)$. 밑면 $D$·높이 $1$인 기둥의 부피가 $A(D)\cdot1$이라는 데서 즉시 | 1133 | 본문(기하적 논증) | Fig 19 |
| 13 | thm | 성질 (10) | 이중적분의 상·하한 추정 / Bounds for a Double Integral | (10) $D$의 모든 점에서 $m\le f(x,y)\le M$이면 $m\cdot A(D)\le\displaystyle\iint_D f(x,y)\,dA\le M\cdot A(D)$ | 1134 | 연습문제 73 (성질 6·7·9를 결합) | Fig 20 |
| 14 | fig | Figure 5 & 7 | 제1형·제2형 영역의 예 / Type I and Type II Regions | 위·아래가 $y=g_1,y=g_2$인 영역 3개와 좌·우가 $x=h_1,x=h_2$인 영역 3개 — 두 형의 구별에 필수 | 1128–1129 | — | — |

카드 수: note 2, def 3, thm 6, rem 2, fig 1 = **14**

## B. 예제 기준값

| Example | PDF 쪽 | 유형 | 문제 요지 (영어 재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1129 | 계산 | Integrate $x+2y$ over the region caught between the parabolas $y=2x^2$ and $y=1+x^2$. | $\dfrac{32}{15}$ | $\int_{-1}^{1}\!\int_{2x^2}^{1+x^2}(x+2y)\,dy\,dx=\dfrac{32}{15}$ (sympy) | ✔ | 교점 $x=\pm1$. $D$는 제1형이지만 제2형은 아님. 내부 축약 피적분함수 $-3x^4-x^3+2x^2+x+1$ |
| 2 | 1130 | 계산 | Find the volume under the paraboloid $z=x^2+y^2$ over the plane region bounded by $y=2x$ and $y=x^2$; do it once as a type I region and once as a type II region. | $\dfrac{216}{35}$ (두 방법 모두) | 제1형 $\int_0^2\!\int_{x^2}^{2x}=\dfrac{216}{35}$; 제2형 $\int_0^4\!\int_{y/2}^{\sqrt y}=\dfrac{216}{35}$ (sympy) | ✔ | $D$는 두 형 모두. 제1형 $0\le x\le2,\ x^2\le y\le2x$; 제2형 $0\le y\le4,\ \tfrac12y\le x\le\sqrt y$ |
| 3 | 1131–1132 | 계산 | Integrate $xy$ over the region enclosed by the line $y=x-1$ and the parabola $y^2=2x+6$. | $36$ | 제2형 $\int_{-2}^{4}\!\int_{y^2/2-3}^{y+1}xy\,dx\,dy=36$; 제1형으로 두 조각 분할해도 $36$ (sympy) | ✔ | 교점 $(-1,-2),(5,4)$. 제1형이면 아래 경계가 $g_1(x)=-\sqrt{2x+6}\ (-3\le x\le-1)$, $x-1\ (-1<x\le5)$로 쪼개져 계산량이 늘어남 |
| 4 | 1131–1132 | 계산 | Compute the volume of the tetrahedron cut off by $x+2y+z=2$, $x=2y$, $x=0$, and $z=0$. | $\dfrac{1}{3}$ | $\int_0^1\!\int_{x/2}^{1-x/2}(2-x-2y)\,dy\,dx=\dfrac13$ (sympy) | ✔ | 밑면 $D=\{0\le x\le1,\ x/2\le y\le1-x/2\}$, 높이 $z=2-x-2y$. 축약 피적분함수 $x^2-2x+1$ |
| 5 | 1132 | 계산 | Evaluate $\displaystyle\int_0^1\!\int_x^1\sin(y^2)\,dy\,dx$; the inner integral has no elementary antiderivative, so reverse the order. | $\tfrac12(1-\cos 1)$ | 순서 교환 후 $\int_0^1\!\int_0^y\sin(y^2)\,dx\,dy=\tfrac12-\tfrac12\cos1\approx0.229849$ (sympy) | ✔ | $D=\{0\le x\le1,\ x\le y\le1\}=\{0\le y\le1,\ 0\le x\le y\}$ |
| 6 | 1134 | 해석·응용 (추정) | Use Property 10 to bound $\iint_D e^{\sin x\cos y}\,dA$, $D$ the disk of radius 2 centered at the origin. | $\dfrac{4\pi}{e}\le\displaystyle\iint_D e^{\sin x\cos y}\,dA\le 4\pi e$ | 구간 $[4\pi/e,\,4\pi e]=[4.62291,\,34.15894]$; 실제 값을 극좌표 중점법칙($400\times800$)으로 구하면 $\approx14.4135$ — 구간 내부 (python) | ✔ | $m=e^{-1}$, $M=e$, $A(D)=\pi(2)^2=4\pi$. pdftotext에서 $\pi$가 소실 — PNG p.1134로 확인함 |

예제 수: **6** (계산 5, 해석·응용 1)

## C. 그림 필요 목록 (자체 SVG)

| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 1·2 | 유계 영역 $D$와 그것을 감싸는 직사각형 $R$ | 선택 | 1 |
| Figure 3·4 | $f$의 그래프와 확장함수 $F$의 그래프(경계에서 절벽) | 선택 | 3 |
| Figure 5 | 제1형 영역 3개 (세 번째는 $g_2$가 조각적 정의) | **필수** | 14 (=4) |
| Figure 6 | 제1형 $D$를 감싼 직사각형과 세로 화살표 | 선택 | 5 |
| Figure 7 | 제2형 영역 3개 | **필수** | 14 (=6) |
| Figure 8 | 예제 1의 영역: $y=2x^2$, $y=1+x^2$, 세로 화살표 | **필수** | 예제 1 |
| Figure 9·10 | 예제 2의 $D$를 제1형/제2형으로 각각 본 그림 | **필수** | 예제 2 |
| Figure 11 | 예제 2의 입체(포물면 아래, 포물기둥과 평면 사이) | 선택 | 예제 2 |
| Figure 12 | 예제 3의 영역을 (a) 제1형 (b) 제2형으로 본 두 그림 | **필수** | 예제 3, 카드 8 |
| Figure 13·14 | 예제 4의 사면체 $T$와 밑면 삼각형 $D$ | **필수**(14) | 예제 4 |
| Figure 15·16 | 예제 5의 삼각형 $D$를 제1형/제2형으로 본 그림 | **필수** | 예제 5 |
| Figure 17 | $D=D_1\cup D_2$ | 선택 | 11 |
| Figure 18 | 두 형 어느 쪽도 아닌 영역을 두 조각으로 나눔 | 선택 | 11 |
| Figure 19 | 밑면 $D$, 높이 $1$인 기둥 | 선택 | 12 |
| Figure 20 | $z=m$, $z=f(x,y)$, $z=M$ 사이에 낀 입체 | 선택 | 13 |

## D. ERRATA·판독 불확실
- 예제 6에서 pdftotext가 $\pi$를 모두 삭제해 "$4/e\le\cdots\le4e$"처럼 보임. PNG p.1134를 직접 확인해 **$4\pi/e\le\iint_D e^{\sin x\cos y}dA\le4\pi e$** 임을 확정.
- 그 밖의 ERRATA 없음. 예제 1~5는 sympy로 교재 답과 정확히 일치.

## E. 절 요약 (사이트 도입 note 초안)
직사각형이 아닌 일반 영역 $D$ 위의 이중적분은, $D$를 감싸는 직사각형 $R$ 위에서 $D$ 밖을 $0$으로 채운 확장함수 $F$의 적분으로 정의한다. 실제 계산은 $D$를 **제1형**(위·아래가 $y=g_1(x),y=g_2(x)$)이나 **제2형**(좌·우가 $x=h_1(y),x=h_2(y)$)으로 기술한 뒤 반복적분으로 바꾸는 것이 전부이며, 이때 안쪽 적분의 한계가 바깥 변수의 함수가 된다는 점이 §15.1과 다르다. 영역을 어느 형으로 볼지, 어느 순서로 적분할지에 따라 계산량이 크게 달라지고, $\int\sin(y^2)dy$처럼 한쪽 순서로는 아예 불가능한 경우도 있으므로 **그림을 그리고 순서를 고르는 일**이 핵심 기술이다. 마지막으로 선형성·비교·영역 분할·$\iint_D1\,dA=A(D)$·상하한 추정이라는 다섯 가지 성질이 뒤 절들에서 계속 쓰인다.

## F. 공통과제 문항 (2차 공통과제)
- **과제 제출 문항**: 23, 33, 37, 61, 65
- **학습 참고 문항**: 11, 14, 28, 34, 35, 39, 40, 44, 45, 60, 62, 66, 74, 75, 78
