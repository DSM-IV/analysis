# §15.4 Applications of Double Integrals — PDF p.1144–1153 (인쇄 p.1107–1116)

> 본문은 PDF p.1144 중간에서 시작(그 위는 §15.3 연습문제), 본문 종료 p.1152 하단, 연습문제 p.1153–(1155).

## A. 카드 인벤토리 (원문 순서)

| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입) | 이중적분의 물리적 응용 / Physical Applications | 부피(§15.1–15.3), 곡면넓이(§15.5) 외에 질량·전하·질량중심·관성모멘트를 다루고, 같은 아이디어가 **두 확률변수의 결합확률밀도함수**에도 그대로 적용됨을 본다 | 1144 | — | — |
| 2 | def | Density and Mass | 면밀도 / Area Density | 라미나가 $xy$-평면의 영역 $D$를 차지하고 점 $(x,y)$에서의 밀도(단위넓이당 질량)가 연속함수 $\rho(x,y)$일 때 $\rho(x,y)=\lim\dfrac{\Delta m}{\Delta A}$ ($\Delta m,\Delta A$는 $(x,y)$를 품은 작은 직사각형의 질량과 넓이, 변의 길이 $\to0$) | 1144 | — | Fig 1, 2 |
| 3 | thm | 식 (1) | 라미나의 질량 / Mass of a Lamina | (1) $\displaystyle m=\lim_{k,l\to\infty}\sum_{i=1}^k\sum_{j=1}^l \rho(x_{ij}^*,y_{ij}^*)\,\Delta A=\iint_D \rho(x,y)\,dA$ | 1145 | 본문(리만 합의 극한; $D$ 밖에서 $\rho=0$으로 확장) | Fig 2 |
| 4 | thm | 식 (2) | 총 전하 / Total Electric Charge | 전하밀도(단위넓이당 전하)가 $\sigma(x,y)$이면 (2) $\displaystyle Q=\iint_D \sigma(x,y)\,dA$. 다른 종류의 밀도도 같은 방식으로 다룸 | 1145 | (1)과 동일 | — |
| 5 | thm | 식 (3)(4) | 좌표축에 대한 모멘트 / Moments about the Axes | 입자의 모멘트 = 질량 × 축까지의 부호 있는 거리. (3) $\displaystyle M_x=\iint_D y\,\rho(x,y)\,dA$ ($x$축에 대한 모멘트), (4) $\displaystyle M_y=\iint_D x\,\rho(x,y)\,dA$ ($y$축에 대한 모멘트) | 1145 | 본문(리만 합의 극한) | Fig 2 |
| 6 | def | Definition (5) | 질량중심 / Center of Mass | $m\bar x=M_y$, $m\bar y=M_x$가 되도록 정의: (5) $\bar x=\dfrac{M_y}{m}=\dfrac1m\displaystyle\iint_D x\,\rho(x,y)\,dA$, $\bar y=\dfrac{M_x}{m}=\dfrac1m\displaystyle\iint_D y\,\rho(x,y)\,dA$, $m=\displaystyle\iint_D\rho(x,y)\,dA$. 질량이 전부 $(\bar x,\bar y)$에 모인 것처럼 행동 — 그 점에서 받치면 수평으로 균형을 이룸 | 1146 | — | Fig 4 |
| 7 | def | 식 (6)(7) | 관성모멘트(2차 모멘트) / Moments of Inertia | 질량 $m$인 입자의 축에 대한 관성모멘트는 $mr^2$ ($r$은 축까지 거리). 라미나에 대해 (6) $\displaystyle I_x=\iint_D y^2\rho(x,y)\,dA$, (7) $\displaystyle I_y=\iint_D x^2\rho(x,y)\,dA$ | 1147 | 본문(리만 합의 극한) | — |
| 8 | def | 식 (8) | 극관성모멘트 / Polar Moment of Inertia | (8) $\displaystyle I_0=\iint_D (x^2+y^2)\,\rho(x,y)\,dA$ (원점에 대한 관성모멘트). 항상 $I_0=I_x+I_y$ | 1148 | 본문(피적분함수 분해) | — |
| 9 | rem | Example 4 뒤 단락 | 관성모멘트의 의미 / What the Moment of Inertia Means | 밀도 $\rho$, 반지름 $a$인 원판은 $m=\rho\pi a^2$이므로 $I_0=\dfrac{\rho\pi a^4}{2}=\tfrac12 ma^2$ — 질량이나 반지름을 키우면 관성모멘트가 커진다. 관성모멘트는 **회전운동에서 질량이 직선운동에서 하는 역할**을 한다(바퀴를 돌리거나 멈추기 어렵게 만드는 양) | 1148–1149 | — | — |
| 10 | def | 식 (9)(10) | 회전반지름 / Radius of Gyration | (9) $mR^2=I$를 만족하는 수 $R$ — 질량 전부가 축에서 거리 $R$에 모여 있을 때 같은 관성모멘트를 갖는다. 특히 (10) $m\bar{\bar y}^2=I_x$, $m\bar{\bar x}^2=I_y$이고, 점 $(\bar{\bar x},\bar{\bar y})$는 좌표축에 대한 관성모멘트를 바꾸지 않고 질량을 집중시킬 수 있는 점 (질량중심과의 유비) | 1149 | — | — |
| 11 | def | Probability | 결합확률밀도함수 / Joint Density Function | 연속확률변수 쌍 $X,Y$에 대해 $P((X,Y)\in D)=\displaystyle\iint_D f(x,y)\,dA$를 만족하는 $f$. 직사각형이면 $P(a\le X\le b,\ c\le Y\le d)=\displaystyle\int_a^b\!\!\int_c^d f(x,y)\,dy\,dx$. 성질: $f(x,y)\ge0$이고 $\displaystyle\iint_{\mathbb R^2}f\,dA=\int_{-\infty}^{\infty}\!\!\int_{-\infty}^{\infty}f(x,y)\,dx\,dy=1$ (이 이상적분은 팽창하는 원판/정사각형 위 적분의 극한, 연습 15.3.50 참조) | 1149–1150 | — | Fig 7 |
| 12 | def | independent random variables | 독립확률변수와 지수분포 / Independent Variables, Exponential Density | $X,Y$의 개별 밀도가 $f_1,f_2$일 때 결합밀도가 곱 $f(x,y)=f_1(x)f_2(y)$이면 **독립**. 대기시간 모형: $f(t)=\begin{cases}0&t<0\\ \mu^{-1}e^{-t/\mu}&t\ge0\end{cases}$ ($\mu$는 평균 대기시간) | 1151 | — | — |
| 13 | def | 식 (11) | 기댓값($X$-평균, $Y$-평균) / Expected Values | (11) $\displaystyle\mu_1=\iint_{\mathbb R^2} x\,f(x,y)\,dA$, $\displaystyle\mu_2=\iint_{\mathbb R^2} y\,f(x,y)\,dA$ | 1152 | — | — |
| 14 | rem | (11) 뒤 단락 | 확률과 질량의 유비 / Probability as Distributed Mass | (11)은 (3)(4)의 $M_x,M_y$와 형태가 같다. 확률은 연속적으로 분포된 질량처럼 생각할 수 있고 — 밀도함수를 적분해 얻는다 — 총 "확률질량"이 $1$이므로 (5)에 비추어 $\mu_1,\mu_2$는 확률분포의 **질량중심 좌표**로 볼 수 있다 | 1152 | — | — |
| 15 | rem | normal distribution | 정규분포 밀도함수 / Normal Density | 확률변수가 정규분포를 따른다는 것은 밀도가 $f(x)=\dfrac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/(2\sigma^2)}$ 꼴이라는 뜻 ($\mu$ 평균, $\sigma$ 표준편차). 두 정규변수가 독립이면 결합밀도는 두 밀도의 곱(이변량정규) | 1152 | — | Fig 9 |
| 16 | fig | Figure 2 | 부분직사각형의 질량 근사 / Approximating Mass on $R_{ij}$ | $D$를 감싼 격자와 $R_{ij}$, 표본점 $(x_{ij}^*,y_{ij}^*)$, 질량 $\approx\rho(x_{ij}^*,y_{ij}^*)\Delta A$ — (1)(3)(4)(6)(7)(8)이 모두 이 그림에서 나옴 | 1144 | — | — |

카드 수: note 1, def 8, thm 3, rem 3, fig 1 = **16**

## B. 예제 기준값

| Example | PDF 쪽 | 유형 | 문제 요지 (영어 재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1144 | 계산 | Charge with surface density $\sigma(x,y)=xy$ C/m² sits on the triangle bounded by $y=1-x$, $y=1$ and $x=1$ (vertices $(0,1),(1,0),(1,1)$); find the total charge. | $Q=\dfrac{5}{24}$ C | $\int_0^1\!\int_{1-x}^{1}xy\,dy\,dx=\dfrac{5}{24}$ (sympy) | ✔ | 축약 피적분함수 $\tfrac12(2x^2-x^3)$ |
| 2 | 1146 | 계산 | Find the mass and center of mass of the triangular lamina with vertices $(0,0),(1,0),(0,2)$ whose density is $\rho(x,y)=1+3x+y$. | $m=\dfrac83$, 질량중심 $\left(\dfrac38,\dfrac{11}{16}\right)$ | $m=8/3$, $M_y=1$, $M_x=11/6$ ⇒ $(\bar x,\bar y)=(3/8,\,11/16)$ (sympy) | ✔ | 위쪽 경계 $y=2-2x$ |
| 3 | 1147 | 계산 | A semicircular lamina (upper half of $x^2+y^2=a^2$) has density proportional to the distance from the centre; locate its center of mass. | $m=\dfrac{K\pi a^3}{3}$, 질량중심 $\left(0,\dfrac{3a}{2\pi}\right)$ | 극좌표 $\rho=Kr$: $m=\dfrac{\pi K a^3}{3}$, $M_x=\dfrac{Ka^4}{2}$, $M_y=0$ ⇒ $\left(0,\dfrac{3a}{2\pi}\right)$ (sympy) | ✔ | 대칭성으로 $\bar x=0$. 균일밀도(예 8.3.4)일 때의 $\left(0,\dfrac{4a}{3\pi}\right)$보다 원점에서 **더 멀다** — $\tfrac{3}{2\pi}=0.47746>\tfrac{4}{3\pi}=0.42441$ (밀도가 $r$에 비례해 질량이 바깥쪽으로 쏠림). *Opus 검증 2026-09-10: 이 칸의 원래 기술 "원점에 가까움"은 오류였음* |
| 4 | 1148 | 계산 | Compute $I_x$, $I_y$, $I_0$ for a homogeneous disk of radius $a$, constant density $\rho$, centred at the origin. | $I_x=I_y=\dfrac{\rho\pi a^4}{4}$, $I_0=\dfrac{\rho\pi a^4}{2}$ | 극좌표: $I_x=I_y=\dfrac{\pi\rho a^4}{4}$; 직접 계산한 $I_0=\dfrac{\pi\rho a^4}{2}=I_x+I_y$ (sympy) | ✔ | $m=\rho\pi a^2$이므로 $I_0=\tfrac12 ma^2$ (바퀴의 관성모멘트) |
| 5 | 1149 | 계산 | Find the radius of gyration about the $x$-axis for the disk of Example 4. | $\bar{\bar y}=\dfrac{a}{2}$ | $\bar{\bar y}^2=\dfrac{I_x}{m}=\dfrac{\rho\pi a^4/4}{\rho\pi a^2}=\dfrac{a^2}{4}$ ⇒ $\bar{\bar y}=a/2$ (sympy) | ✔ | 원판 반지름의 절반 |
| 6 | 1150 | 계산 | For the joint density $f(x,y)=C(x+2y)$ on $[0,10]\times[0,10]$ (zero elsewhere), find $C$ and then $P(X\le7,\,Y\ge2)$. | $C=\dfrac{1}{1500}$; $P=\dfrac{868}{1500}\approx0.5787$ | $\iint f=1500C=1\Rightarrow C=\tfrac1{1500}$; $P=\tfrac{217}{375}=\tfrac{868}{1500}\approx0.578667$ (sympy) | ✔ | — |
| 7 | 1151 | 해석·응용 | Ticket-line wait $X$ and popcorn-line wait $Y$ are independent exponential variables with means 10 and 5 minutes; find $P(X+Y<20)$. | $1+e^{-4}-2e^{-2}\approx0.7476$ | $\displaystyle\int_0^{20}\!\!\int_0^{20-x}\tfrac1{50}e^{-x/10}e^{-y/5}\,dy\,dx=1+e^{-4}-2e^{-2}\approx0.747645$ (sympy, 기호적으로 교재 표현과 동치 확인) | ✔ | 결합밀도 $f=\tfrac1{50}e^{-x/10}e^{-y/5}$ ($x,y\ge0$); 영역은 삼각형 $x+y<20$. 약 75% |
| 8 | 1152 | 해석·응용 | Bearing diameters $X\sim N(4.0,0.01^2)$ and lengths $Y\sim N(6.0,0.01^2)$ are independent; write the joint density and find the probability that at least one of the two deviates from its mean by more than 0.02 cm. | $f(x,y)=\dfrac{5000}{\pi}e^{-5000[(x-4)^2+(y-6)^2]}$; $P(3.98<X<4.02,\ 5.98<Y<6.02)\approx0.91$, 구하는 확률 $\approx1-0.91=0.09$ | $0.02=2\sigma$이므로 한 변수당 $P=\operatorname{erf}(\sqrt2)=0.954500$; 독립이므로 결합 $=0.954500^2=0.911070\approx0.91$; $1-0.911070=0.08893\approx0.09$ (sympy) | ✔ | 교재는 "계산기/컴퓨터로 추정"이라 하며 $0.91$로 반올림 — 정확값 $0.91107$이므로 여집합은 $0.0889$ (교재의 $0.09$는 반올림 결과) |

예제 수: **8** (계산 6, 해석·응용 2)

## C. 그림 필요 목록 (자체 SVG)

| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 1 | 영역 $D$를 차지한 라미나와 점 $(x,y)$ | 선택 | 2 |
| Figure 2 | $D$를 덮은 격자, $R_{ij}$, 표본점 $(x_{ij}^*,y_{ij}^*)$ | **필수** | 16 (=3,5,7,8) |
| Figure 3 | 예제 1의 삼각형 $D$ ($y=1-x$, $y=1$) | **필수** | 예제 1 |
| Figure 4 | 질량중심 $(\bar x,\bar y)$에서 균형 잡힌 라미나 | 선택 | 6 |
| Figure 5 | 예제 2의 삼각형 $(0,0),(1,0),(0,2)$와 질량중심 $\left(\tfrac38,\tfrac{11}{16}\right)$ | **필수** | 예제 2 |
| Figure 6 | 예제 3의 반원판과 질량중심 $\left(0,\tfrac{3a}{2\pi}\right)$ | **필수** | 예제 3 |
| Figure 7 | 결합밀도 곡면 아래·직사각형 $[a,b]\times[c,d]$ 위 부피 = 확률 | **필수** | 11 |
| Figure 8 | 예제 7의 삼각영역 $x+y<20$ ($x,y\ge0$) | **필수** | 예제 7 |
| Figure 9 | 이변량정규 결합밀도의 종 모양 곡면 | 선택 | 15, 예제 8 |

## D. ERRATA·판독 불확실
- ERRATA 없음. 교재의 8개 예제 답이 모두 sympy 재계산과 일치.
- 예제 8의 $\approx0.91$은 교재의 반올림값이며 정확값은 $0.911070$. 따라서 여집합 확률도 정확히는 $0.0889$(교재 $0.09$). 문제 없음이나 사이트 풀이에서는 두 자리 반올림을 밝히는 편이 좋음.
- 회전반지름 $\bar{\bar x},\bar{\bar y}$는 교재에서 이중 윗줄(double overbar) 기호를 쓰나 pdftotext에서 질량중심의 $\bar x,\bar y$와 구별되지 않음. 여기서는 $\bar{\bar x},\bar{\bar y}$로 표기해 구분함.
- pdftotext가 $\rho,\sigma,\mu,\pi$ 등 그리스 문자를 대부분 삭제 — 문맥으로 복원했고, 예제 답과 sympy 결과의 일치로 검증됨.

## E. 절 요약 (사이트 도입 note 초안)
이 절은 이중적분을 "밀도를 적분해 총량을 얻는 장치"로 다시 읽는다. 면밀도 $\rho(x,y)$를 적분하면 질량 $m=\iint_D\rho\,dA$, 전하밀도를 적분하면 총 전하가 되고, 여기에 $x$나 $y$를 곱해 적분하면 모멘트 $M_y,M_x$가 되어 질량중심 $(\bar x,\bar y)=(M_y/m,\,M_x/m)$이 나온다. 거리의 **제곱**을 곱하면 관성모멘트 $I_x,I_y,I_0=I_x+I_y$가 되며, 이는 회전운동에서 질량이 직선운동에서 하는 역할을 하고 $mR^2=I$로 회전반지름을 정의한다. 놀랍게도 같은 형식이 확률에도 그대로 통해서, 결합확률밀도 $f(x,y)$의 적분이 확률이고 총 "확률질량"이 $1$이므로 기댓값 $\mu_1,\mu_2$는 곧 확률분포의 질량중심이다. 계산은 대개 §15.2의 제1/제2형 반복적분이나 §15.3의 극좌표로 귀착된다.

## F. 공통과제 문항 (2차 공통과제)
- **과제 제출 문항**: 7, 12, 18
- **학습 참고 문항**: 3~4, 5~12, 13~22, 23~26
