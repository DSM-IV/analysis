# §14.1 Functions of Several Variables — PDF p.1009–1025 (인쇄 p.972–988)

본문(설명·예제) PDF p.1009–1021(인쇄 972–984), 연습문제 PDF p.1021–1026(인쇄 984–989).

## A. 카드 인벤토리 (원문 순서)

| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입) | 다변수함수를 보는 네 관점 / Four Viewpoints | 다변수함수를 언어적(서술)·수치적(값의 표)·대수적(명시적 공식)·시각적(그래프·등위곡선)으로 다룬다. 동기 예: 지표 온도 $T=f(x,y)$(경도·위도), 원기둥 부피 $V(r,h)=\pi r^2h$ | 1009 | — | — |
| 2 | def | Definition (이변수함수) | 이변수함수 / Function of Two Variables | 집합 $D\subset\mathbb R^2$의 각 순서쌍 $(x,y)$에 유일한 실수 $f(x,y)$를 대응시키는 규칙. $D$는 정의역, 치역은 $\{f(x,y)\mid (x,y)\in D\}$ | 1009 | — | — |
| 3 | note | (정의 뒤 단락, Figure 1) | 표기·화살표 그림·정의역 관례 / Notation, Arrow Diagram, Domain Convention | $z=f(x,y)$에서 $x,y$는 독립변수, $z$는 종속변수. 정의역 $D\subset\mathbb R^2$를 $xy$-평면의 부분집합으로, 치역을 $z$-축 위의 수 집합으로 그리는 화살표 그림(Figure 1). 공식만 주어지고 정의역이 명시되지 않으면 **식이 실수를 정의하는 모든 $(x,y)$** 가 정의역 | 1009 | — | Fig 1 |
| 4 | note | (Example 4 도입 서술) | 콥-더글러스 생산함수 / Cobb-Douglas Production Function | 노동 $L$·자본 $K$로 생산 $P$를 모형화: (1) $P(L,K)=bL^{\alpha}K^{1-\alpha}$. 1899–1922년 미국 자료를 최소제곱으로 적합하면 (2) $P(L,K)=1.01L^{0.75}K^{0.25}$. 정의역은 $\{(L,K)\mid L\ge0,\ K\ge0\}$ | 1011–1012 | — | — |
| 5 | def | Definition (그래프) | 그래프 / Graph of a Function of Two Variables | 정의역 $D$를 갖는 $f$의 그래프는 $z=f(x,y)$, $(x,y)\in D$인 모든 점 $(x,y,z)\in\mathbb R^3$의 집합 — 곧 곡면 $S$이며, $D$의 바로 위(또는 아래)에 놓인다 | 1012 | — | Fig 5 |
| 6 | note | (Example 5 뒤 단락) | 일차함수와 평면 / Linear Functions | $f(x,y)=ax+by+c$를 일차함수라 하고, 그래프 $z=ax+by+c$ 즉 $ax+by-z+c=0$은 평면(§12.5). 일변수 미적분의 일차함수처럼 다변수 미적분에서 중심 역할 | 1012 | — | — |
| 7 | rem | NOTE (Example 6 뒤) | 구면 전체는 한 함수의 그래프가 아니다 / A Sphere Is Not a Graph | $x^2+y^2+z^2=9$의 위 반구는 $g(x,y)=\sqrt{9-x^2-y^2}$, 아래 반구는 $h(x,y)=-\sqrt{9-x^2-y^2}$. 구면 전체는 $x,y$의 한 함수로 나타낼 수 없다 | 1013 | — | — |
| 8 | rem | (Figure 10 단락) | 컴퓨터로 그린 그래프 / Computer-Generated Graphs | 여러 시점에서 회전시켜 보면 곡면의 모양을 잘 파악할 수 있다. 예: $f(x,y)=(x^2+3y^2)e^{-x^2-y^2}$(원점 부근을 빼면 $xy$-평면에 가까움), $\sin x+\sin y$, $\dfrac{\sin x\sin y}{xy}$ | 1014 | — | — |
| 9 | def | Definition (등위곡선) | 등위곡선과 등고선도 / Level Curves and Contour Maps | $f$의 등위곡선은 $f(x,y)=k$($k$는 치역의 상수)인 곡선. 등위곡선들의 모음이 등고선도(contour map)이며, 특별한 언급이 없으면 $k$를 등간격으로 잡는다 | 1014 | — | — |
| 10 | note | (Figure 11–14 단락) | 등위곡선과 수평 자취 / Level Curves vs. Horizontal Traces | 등위곡선 $f(x,y)=k$는 그래프를 수평평면 $z=k$로 자른 자취를 $xy$-평면에 사영한 것. 등위곡선이 촘촘하면 곡면이 가파르고, 성기면 완만하다. 실제 예: 지형도의 등고선, 등온선(isothermal), 등압선(isobar, 연습문제 34), 강수량 등고선도 | 1015–1016 | — | Fig 11 |
| 11 | note | Functions of Three or More Variables (절 마무리 포함) | 삼변수 이상·$n$변수 함수 / Functions of Three or More Variables | 삼변수함수는 $D\subset\mathbb R^3$의 각 $(x,y,z)$에 $f(x,y,z)$를 대응(예 $T=f(x,y,t)$). 그래프는 4차원이라 그릴 수 없으므로 **등위곡면** $f(x,y,z)=k$로 파악한다. 일반적으로 $z=f(x_1,\dots,x_n)$이고, 예로 (3) $C=c_1x_1+\cdots+c_nx_n=\mathbf c\cdot\mathbf x$. 세 가지 관점: $n$개 실변수의 함수 / 한 점 변수의 함수 / 한 벡터 변수 $\mathbf x=\langle x_1,\dots,x_n\rangle$의 함수 | 1019–1021 | — | — |
| 12 | fig | Figure 11 | 등위곡선 ↔ 수평 자취 / Lifting Level Curves to the Surface | 곡면과 수평평면 $z=k$의 자취, 그리고 그것을 $xy$-평면에 내린 등위곡선을 한 그림에 (카드 10의 삽화) | 1015 | — | — |

카드 수: note 6, def 3, thm 0, rem 2, fig 1 — 합계 **12**.

## B. 예제 기준값 (예제 16개)

| Example | PDF 쪽 | 유형 | 문제 요지 (영어 재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1009–1010 | 계산 + 스케치 | For (a) $f(x,y)=\dfrac{\sqrt{x+y+1}}{x-1}$ and (b) $f(x,y)=x\ln(y^2-x)$, compute $f(3,2)$ and describe/sketch the natural domain. | (a) $f(3,2)=\dfrac{\sqrt6}{2}$; $D=\{(x,y)\mid x+y+1\ge0,\ x\ne1\}$ (직선 $y=-x-1$ 위쪽 닫힌 영역에서 직선 $x=1$ 제외); (b) $f(3,2)=3\ln1=0$; $D=\{(x,y)\mid x<y^2\}$ (포물선 $x=y^2$의 왼쪽) | sympy: $\sqrt6/2$, $0$; 부등식 조건 동일 | ✅ | Figure 2·3 정의역 스케치 |
| 2 | 1010 | 계산 | Find the domain and the range of $g(x,y)=\sqrt{9-x^2-y^2}$. | $D=\{(x,y)\mid x^2+y^2\le9\}$(중심 $O$, 반지름 3인 원판); 치역 $[0,3]$ | sympy: $r\in[0,3]$에서 $\sqrt{9-r^2}$의 값역 $[0,3]$ | ✅ | — |
| 3 | 1010–1011 | 해석·응용 (표) | Read the wind-chill index $W=f(T,v)$ from a table of measured values and state the value at one entry. | $f(-5,50)=-15$ — 기온 $-5^\circ$C, 풍속 50 km/h면 무풍 $-15^\circ$C처럼 느껴진다 | 표 판독(재계산 대상 아님) | ✅ | **pdftotext에서 음수 부호가 소실되어 "f(25,50)=215"처럼 보임 — PNG p-1011 확인 결과 $f(-5,50)=-15$** |
| 4 | 1011–1012 | 계산·응용 | Use the fitted Cobb-Douglas model $P=1.01L^{0.75}K^{0.25}$ to predict production in 1910 and 1920, and state its domain. | $P(147,208)\approx161.9$ (실제 159), $P(194,407)\approx235.8$ (실제 231); $D=\{(L,K)\mid L\ge0,K\ge0\}$ | sympy: $161.92921$, $235.81492$ | ✅ | — |
| 5 | 1012 | 스케치·그래프 | Sketch the graph of $f(x,y)=6-3x-2y$. | 그래프형 — 서술 답: 평면 $3x+2y+z=6$; 절편 $x=2,\ y=3,\ z=6$ (제1팔분공간 삼각형 조각을 그림) | sympy로 절편 $2,3,6$ 확인 | ✅ | Figure 6 |
| 6 | 1012 | 스케치·그래프 | Sketch the graph of $g(x,y)=\sqrt{9-x^2-y^2}$. | 그래프형 — 서술 답: 양변 제곱하면 $x^2+y^2+z^2=9$이고 $z\ge0$이므로 **반지름 3인 구의 위 반구** | 대수 확인(제곱·부호 조건) | ✅ | Figure 7 |
| 7 | 1013 | 그래프(컴퓨터) | Use technology to graph the Cobb-Douglas function $P(L,K)=1.01L^{0.75}K^{0.25}$ on $0\le L,K\le300$. | 그래프형 — 서술 답: 수직 자취로 그린 곡면에서 $L$ 또는 $K$가 커지면 $P$가 증가(단조 증가면) | 편도함수 부호로 확인 가능(단조성) | ✅ | Figure 8 |
| 8 | 1013 | 계산 + 스케치 | Find the domain, the range, and sketch the graph of $h(x,y)=4x^2+y^2$. | $D=\mathbb R^2$; 치역 $[0,\infty)$; 그래프 $z=4x^2+y^2$는 **타원포물면**(수평 자취는 타원, 수직 자취는 포물선) | sympy/직접 확인 | ✅ | Figure 9, §12.6 Example 4와 동일 곡면 |
| 9 | 1017 | 해석 (등고선 판독) | Estimate two function values from a given contour map. | 그래프형 — 서술 답: $f(1,3)\approx73$ (70과 80 등고선 사이), $f(4,5)\approx56$ | 그림 판독(재계산 대상 아님) | ✅ | Figure 15 |
| 10 | 1017 | 계산 + 스케치 | Sketch the level curves of $f(x,y)=6-3x-2y$ for $k=-6,0,6,12$. | $3x+2y+(k-6)=0$ — 기울기 $-\tfrac32$인 평행선족. $k=-6,0,6,12$일 때 각각 $3x+2y-12=0$, $3x+2y-6=0$, $3x+2y=0$, $3x+2y+6=0$. $k$가 등간격이면 등간격 평행선 | sympy: 네 직선과 기울기 $-3/2$ 모두 일치 | ✅ | Figure 16 |
| 11 | 1017–1018 | 계산 + 스케치 | Sketch the level curves of $g(x,y)=\sqrt{9-x^2-y^2}$ for $k=0,1,2,3$. | $x^2+y^2=9-k^2$ — 중심 $(0,0)$, 반지름 $\sqrt{9-k^2}$인 동심원족. 반지름은 $3,\ 2\sqrt2,\ \sqrt5,\ 0$ | sympy: $3,\ 2\sqrt2\approx2.82843,\ \sqrt5\approx2.23607,\ 0$ | ✅ | Figure 17; $k=3$은 점 $(0,0)$ |
| 12 | 1018 | 계산 + 스케치 | Sketch some level curves of $h(x,y)=4x^2+y^2+1$. | $\dfrac{x^2}{\tfrac14(k-1)}+\dfrac{y^2}{k-1}=1$ — $k>1$에서 반축이 $\tfrac12\sqrt{k-1}$($x$방향), $\sqrt{k-1}$($y$방향)인 타원족 | sympy: 항등식 차 $=0$, 반축 일치 | ✅ | Figure 18(a)(b); 등위곡선을 들어 올리면 타원포물면 |
| 13 | 1018 | 그래프(컴퓨터) | Draw a contour plot of the Cobb-Douglas production function. | 그래프형 — 서술 답: 등위곡선에 생산량 $P$ 값을 붙인 곡선족(예 $P=140$). 고정된 $P$에 대해 $L$이 커지면 $K$가 작아진다(대체 관계) | — | ✅ | Figure 19 |
| 14 | 1019 | 계산 | Find the domain of $f(x,y,z)=\ln(z-y)+xy\sin z$. | $D=\{(x,y,z)\in\mathbb R^3\mid z>y\}$ — 평면 $z=y$ 위쪽의 반공간 | 조건 $z-y>0$ 확인 | ✅ | — |
| 15 | 1020 | 계산 | Find the level surfaces of $f(x,y,z)=x^2+y^2+z^2$. | $x^2+y^2+z^2=k\ (k\ge0)$ — 반지름 $\sqrt k$인 동심 구면족 | sympy: $k=1,2,3$에서 반지름 $1,\sqrt2,\sqrt3$ | ✅ | Figure 21; $k=0$은 원점 한 점 |
| 16 | 1020 | 계산 | Describe the level surfaces of $f(x,y,z)=x^2-y-z^2$. | $x^2-y-z^2=k$, 즉 $y=x^2-z^2-k$ — 쌍곡포물면족 ($k=0,\pm5$을 그림) | sympy: $y=x^2-z^2-k$ | ✅ | Figure 22 |

anchor 스크립트: `/Users/chalrs/analysis/stewart/inventory/anchor-14.1.py` (예제 1,2,4,5,6,8,10,11,12,14,15,16 재계산; 3·7·9·13은 표 판독/컴퓨터 그림이라 대상 외). **불일치 0건.**

## C. 그림 필요 목록 (자체 SVG)

| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 1 | 화살표 그림: $xy$-평면의 정의역 $D$ → $z$-축 위의 치역 | 선택 | 3 |
| Figure 2 | 예제 1(a) 정의역: 직선 $y=-x-1$ 위쪽, 직선 $x=1$ 제외 | 필수 | 예제 1 |
| Figure 3 | 예제 1(b) 정의역: 포물선 $x=y^2$의 왼쪽 영역 | 필수 | 예제 1 |
| Figure 4 | 예제 2 정의역: 원판 $x^2+y^2\le9$ | 필수 | 예제 2 |
| Figure 5 | 그래프의 정의: 곡면 $S$가 정의역 $D$ 위에 놓인 모습 | 선택 | 5 |
| Figure 6 | 예제 5: 평면 $3x+2y+z=6$의 제1팔분공간 조각(절편 2, 3, 6) | 필수 | 예제 5 |
| Figure 7 | 예제 6: 위 반구 $z=\sqrt{9-x^2-y^2}$ | 필수 | 예제 6 |
| Figure 9 | 예제 8: 타원포물면 $z=4x^2+y^2$ | 선택 | 예제 8 |
| Figure 11 | 등위곡선 ↔ 수평 자취(들어 올리기) | 필수 | 12 (카드 10 삽화) |
| Figure 15 | 예제 9 등고선도(50/60/70/80 등고선, 두 봉우리) | 필수 | 예제 9 |
| Figure 16 | 예제 10: 평행선족 $k=-6,0,6,12$ | 필수 | 예제 10 |
| Figure 17 | 예제 11: 동심원족 $k=0,1,2,3$ | 필수 | 예제 11 |
| Figure 18(a) | 예제 12: 동심 타원족 등고선도 | 필수 | 예제 12 |
| Figure 19 | 예제 13: 콥-더글러스 등고선도($P=100,140,180,220$) | 선택 | 예제 13 |
| Figure 21 | 예제 15: 동심 구면 $k=1,2,3$ | 선택 | 예제 15 |
| Figure 22 | 예제 16: 쌍곡포물면 $k=0,\pm5$ | 선택 | 예제 16 |
| Figure 8, 10, 12, 13, 14, 20 | 컴퓨터 렌더링·실제 지도·강수량 지도 등 사진성 그림 | 제외 | — |

## D. ERRATA·판독 불확실

- **예제 3(중요)**: pdftotext가 음수 부호를 지워 "actual temperature is 25°C … about 215°C … $f(25,50)=215$"로 읽힌다. PNG `p-1011.png` 원본 확인 결과 실제 값은 기온 $-5^\circ$C, 풍속 50 km/h, 체감 $-15^\circ$C, 즉 $\boxed{f(-5,50)=-15}$. 표 1의 온도 행도 $5,0,-5,-10,\dots,-40$이다.
- pdftotext 전반의 기호 손상: `s…d`=괄호, `−`=`=`, `2`=`−`, `1`=`+`, `h…j`=집합괄호, `[`=`\in`, `<`=`\le`, `.`=`>`. 본 인벤토리의 수식은 모두 PNG(p-1011, p-1017, p-1018) 대조 후 복원했다.
- 예제 4의 (1)식은 PNG에서 $P(L,K)=bL^{\alpha}K^{1-\alpha}$ (지수 $\alpha$, $1-\alpha$)로 확인.
- 그 밖의 판독 불확실 항목 없음.

## E. 절 요약 (사이트 도입 note 초안)

두 개 이상의 변수에 의존하는 양을 다루기 위해 이변수함수 $z=f(x,y)$를 정의하고, 이를 서술·수치표·공식·그림의 네 가지 방식으로 파악한다. 공식만 주어진 경우 정의역은 식이 실수를 정의하는 모든 점의 집합이며, 예제 1·2처럼 부등식으로 표현되는 평면 영역이 된다. 함수의 시각화 방법은 두 가지인데, 하나는 $\mathbb R^3$의 곡면인 그래프 $z=f(x,y)$이고 다른 하나는 지도 제작에서 빌려온 등고선도, 즉 등위곡선 $f(x,y)=k$들의 모음이다. 등위곡선은 그래프를 수평평면 $z=k$로 자른 자취를 $xy$-평면에 사영한 것이어서, 선이 촘촘한 곳은 곡면이 가파르다는 정보를 그대로 읽어 준다. 마지막으로 같은 개념을 삼변수 이상으로 확장해 등위곡면 $f(x,y,z)=k$와 $n$변수 함수 $f(\mathbf x)$의 벡터 표기까지 정리한다.

## F. 공통과제 문항

- 과제 제출 문항: **없음** (1차 공통과제 표에서 14.1 행의 제출·참고 칸이 모두 비어 있음)
- 학습 참고 문항: **없음**
