# §15.6 Triple Integrals — PDF p.1157–1169 (인쇄 p.1120–1132)

> 본문은 PDF p.1157 하단에서 시작(그 위는 §15.5 연습문제), 본문 종료 p.1167 상단, 연습문제 p.1167–1169.

## A. 카드 인벤토리 (원문 순서)

| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입) + Triple Integrals over Rectangular Boxes | 삼중적분의 도입 / Setting Up Triple Integrals | 1변수 함수의 정적분, 2변수 함수의 이중적분과 같은 방식으로 3변수 함수의 삼중적분을 정의한다. 가장 간단한 경우는 직육면체 (1) $B=\{(x,y,z)\mid a\le x\le b,\ c\le y\le d,\ r\le z\le s\}$ | 1157 | — | — |
| 2 | def | 식 (2) | 삼중 리만 합 / Triple Riemann Sum | $[a,b]$를 $l$등분, $[c,d]$를 $m$등분, $[r,s]$를 $n$등분해 $lmn$개의 부분상자 $B_{ijk}=[x_{i-1},x_i]\times[y_{j-1},y_j]\times[z_{k-1},z_k]$, 각 부피 $\Delta V=\Delta x\,\Delta y\,\Delta z$. (2) $\displaystyle\sum_{i=1}^l\sum_{j=1}^m\sum_{k=1}^n f(x_{ijk}^*,y_{ijk}^*,z_{ijk}^*)\,\Delta V$ | 1158 | — | Fig 1 |
| 3 | def | Definition 3 | 삼중적분의 정의 / Definition of the Triple Integral | (3) $\displaystyle\iiint_B f(x,y,z)\,dV=\lim_{l,m,n\to\infty}\sum_{i=1}^l\sum_{j=1}^m\sum_{k=1}^n f(x_{ijk}^*,y_{ijk}^*,z_{ijk}^*)\,\Delta V$ (극한이 존재할 때). $f$가 연속이면 항상 존재하고, 표본점을 $(x_i,y_j,z_k)$로 잡으면 표현이 간단해짐 | 1158 | — | — |
| 4 | thm | Theorem 4 (Fubini's Theorem for Triple Integrals) | 삼중적분에 대한 푸비니 정리 / Fubini's Theorem for Triple Integrals | $f$가 $B=[a,b]\times[c,d]\times[r,s]$에서 연속이면 (4) $\displaystyle\iiint_B f\,dV=\int_r^s\!\!\int_c^d\!\!\int_a^b f(x,y,z)\,dx\,dy\,dz$. **여섯 가지 적분 순서 모두 같은 값**을 준다 (예: $\int_a^b\!\int_r^s\!\int_c^d f\,dy\,dz\,dx$) | 1158 | 생략(이중적분 푸비니와 같은 이유) | — |
| 5 | def | Triple Integrals over General Regions | 일반 입체영역 위의 삼중적분 / Triple Integrals over General Solids | 유계 입체 $E$를 직육면체 $B$에 넣고 $E$ 위에서는 $f$, $B\setminus E$에서는 $0$인 $F$를 만들어 $\displaystyle\iiint_E f\,dV=\iiint_B F\,dV$로 정의. $f$가 연속이고 $E$의 경계가 "충분히 매끄러우면" 존재하며, §15.2의 성질 5–8이 그대로 성립 | 1159 | — | — |
| 6 | def | type 1 region, 식 (5) | 제1형 입체영역 / Type 1 Solid Region | (5) $E=\{(x,y,z)\mid (x,y)\in D,\ u_1(x,y)\le z\le u_2(x,y)\}$, $D$는 $E$의 $xy$-평면 정사영. 아래 경계면 $z=u_1(x,y)$, 위 경계면 $z=u_2(x,y)$ | 1159 | — | Fig 2 |
| 7 | thm | 식 (6)(7)(8) | 제1형 영역의 반복적분 / Iterated Integrals over a Type 1 Region | (6) $\displaystyle\iiint_E f\,dV=\iint_D\left[\int_{u_1(x,y)}^{u_2(x,y)}f(x,y,z)\,dz\right]dA$ (안쪽 적분에서 $x,y$는 상수). $D$가 평면 제I형이면 (7) $\displaystyle\int_a^b\!\!\int_{g_1(x)}^{g_2(x)}\!\!\int_{u_1(x,y)}^{u_2(x,y)}f\,dz\,dy\,dx$, 평면 제II형이면 (8) $\displaystyle\int_c^d\!\!\int_{h_1(y)}^{h_2(y)}\!\!\int_{u_1(x,y)}^{u_2(x,y)}f\,dz\,dx\,dy$ | 1159–1160 | (15.2.3)과 같은 논법(본문에서 언급) | Fig 3, 4 |
| 8 | def | type 2 region, 식 (10) | 제2형 입체영역 / Type 2 Solid Region | $E=\{(x,y,z)\mid (y,z)\in D,\ u_1(y,z)\le x\le u_2(y,z)\}$, $D$는 $yz$-평면 정사영, 뒷면 $x=u_1$, 앞면 $x=u_2$. (10) $\displaystyle\iiint_E f\,dV=\iint_D\left[\int_{u_1(y,z)}^{u_2(y,z)}f\,dx\right]dA$ | 1161 | — | Fig 8 |
| 9 | def | type 3 region, 식 (11) | 제3형 입체영역 / Type 3 Solid Region | $E=\{(x,y,z)\mid (x,z)\in D,\ u_1(x,z)\le y\le u_2(x,z)\}$, $D$는 $xz$-평면 정사영, 왼쪽면 $y=u_1$, 오른쪽면 $y=u_2$. (11) $\displaystyle\iiint_E f\,dV=\iint_D\left[\int_{u_1(x,z)}^{u_2(x,z)}f\,dy\right]dA$. (10)(11) 각각 $D$가 평면 제I형이냐 제II형이냐에 따라 두 가지 표현 | 1161 | — | Fig 9 |
| 10 | rem | Example 3 옆 여백 주석 | 적분 한계를 세우는 규칙 / Rules for the Limits | 삼중적분에서 가장 어려운 단계는 **적분 영역의 식을 세우는 것**(예제 2의 식 (9)). 기억할 것: 안쪽 적분의 한계는 변수를 최대 2개, 가운데 적분의 한계는 최대 1개 포함하고, 바깥 적분의 한계는 **반드시 상수** | 1163 | — | — |
| 11 | note | Changing the Order of Integration | 적분 순서 바꾸기 / Changing the Order of Integration | 여섯 가지 순서가 모두 같은 값을 주므로, 한 순서로 어려운 반복적분을 다른 순서로 다시 쓰면 쉬워질 수 있다. 방법: 주어진 반복적분에서 $E$를 읽어 내고, $E$를 세 좌표평면에 정사영한 $D_1,D_2,D_3$를 각각 두 가지 방식으로 기술한 뒤 원하는 형(제1/2/3형)으로 다시 쓴다 | 1163 | — | Fig 14, 15 |
| 12 | note | Applications of Triple Integrals + 식 (12) | 삼중적분의 해석과 부피 / Interpretation, and Volume | $f\ge0$이어도 $\iiint_E f\,dV$는 4차원 "초부피"라 시각화에 쓸모없다. 그러나 $f\equiv1$이면 (12) $\displaystyle V(E)=\iiint_E dV$가 곧 $E$의 부피. 실제로 (6)에 $f=1$을 넣으면 $\iint_D[u_2(x,y)-u_1(x,y)]\,dA$가 되어 §15.2의 두 곡면 사이 부피와 일치 | 1164 | 본문 | — |
| 13 | thm | 식 (13)(14) | 질량과 좌표평면에 대한 모멘트 / Mass and Moments | 밀도(단위부피당 질량)가 $\rho(x,y,z)$일 때 (13) $\displaystyle m=\iiint_E\rho(x,y,z)\,dV$. 좌표평면에 대한 모멘트 (14) $\displaystyle M_{yz}=\iiint_E x\rho\,dV$, $\displaystyle M_{xz}=\iiint_E y\rho\,dV$, $\displaystyle M_{xy}=\iiint_E z\rho\,dV$ | 1165 | 본문(삼중 리만 합의 극한) | Fig 18 |
| 14 | def | 식 (15) | 질량중심과 중심(centroid) / Center of Mass and Centroid | (15) $\bar x=\dfrac{M_{yz}}{m}$, $\bar y=\dfrac{M_{xz}}{m}$, $\bar z=\dfrac{M_{xy}}{m}$. 밀도가 상수이면 이 점을 $E$의 **중심(centroid)** 이라 함 | 1166 | — | — |
| 15 | thm | 식 (16) | 좌표축에 대한 관성모멘트 / Moments of Inertia | (16) $\displaystyle I_x=\iiint_E (y^2+z^2)\rho\,dV$, $\displaystyle I_y=\iiint_E (x^2+z^2)\rho\,dV$, $\displaystyle I_z=\iiint_E (x^2+y^2)\rho\,dV$ | 1166 | §15.4와 같은 논법 | — |
| 16 | rem | (16) 뒤 단락 | 전하와 세 확률변수 / Charge and Trivariate Probability | 전하밀도 $\sigma$이면 $\displaystyle Q=\iiint_E\sigma(x,y,z)\,dV$. 연속확률변수 $X,Y,Z$의 결합밀도 $f$는 $P((X,Y,Z)\in E)=\displaystyle\iiint_E f\,dV$를 만족하고, 특히 $P(a\le X\le b,\ c\le Y\le d,\ r\le Z\le s)=\int_a^b\!\int_c^d\!\int_r^s f\,dz\,dy\,dx$이며 $f\ge0$, $\int_{-\infty}^{\infty}\!\!\int_{-\infty}^{\infty}\!\!\int_{-\infty}^{\infty} f\,dz\,dy\,dx=1$ | 1166 | — | — |
| 17 | fig | Figure 2, 8, 9 | 제1·2·3형 입체영역 / Type 1, 2, 3 Solid Regions | 각각 $xy$-, $yz$-, $xz$-평면으로의 정사영 $D$와 위/아래(뒤/앞, 왼/오른) 경계면을 표시 — 세 유형의 구별에 필수 | 1159, 1161 | — | — |

카드 수: note 3, def 7, thm 4, rem 2, fig 1 = **17**

## B. 예제 기준값

| Example | PDF 쪽 | 유형 | 문제 요지 (영어 재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1159 | 계산 | Evaluate $\iiint_B xyz^2\,dV$ over the box $B=[0,1]\times[-1,2]\times[0,3]$. | $\dfrac{27}{4}$ | 순서 $dx\,dy\,dz$: $27/4$; 순서 $dy\,dz\,dx$: $27/4$ (sympy, 두 순서) | ✔ | 여섯 순서 중 어느 것을 써도 같음 |
| 2 | 1160 | 계산 | Evaluate $\iiint_E z\,dV$ where $E$ is the first-octant solid capped by $z=12xy$ and cut by $y=x$ and $x=1$. | $4$ | $E=\{0\le x\le1,\ 0\le y\le x,\ 0\le z\le12xy\}$; $\int_0^1\!\int_0^x\!\int_0^{12xy} z\,dz\,dy\,dx=4$ (sympy) | ✔ | 축약 후 $72\int_0^1\!\int_0^x x^2y^2\,dy\,dx=24\int_0^1x^5dx$. 상수 $12$는 오타가 아니라 원문 그대로 |
| 3 | 1161–1163 | 계산 | Evaluate $\iiint_E\sqrt{x^2+z^2}\,dV$ over the solid bounded by the paraboloid $y=x^2+z^2$ and the plane $y=4$. | $\dfrac{128\pi}{15}$ | 제3형 + $xz$-평면 극좌표: $\int_0^{2\pi}\!\int_0^2(4-r^2)\,r\cdot r\,dr\,d\theta=\dfrac{128\pi}{15}\approx26.80826$; 직교 중점법칙($1200^2$)으로 $26.80826$ (sympy + python) | ✔ | 제1형으로 세우면 $\int_{-2}^{2}\!\int_{x^2}^{4}\!\int_{-\sqrt{y-x^2}}^{\sqrt{y-x^2}}$가 되어 계산이 매우 어려움 — 제3형 + 극좌표가 정답 경로 |
| 4 | 1163–1164 | 개념 (재표현) | Rewrite $\int_0^1\!\int_0^{x^2}\!\int_0^{y} f(x,y,z)\,dz\,dy\,dx$ as a triple integral over a solid, then re-express it (a) in the order $dx\,dz\,dy$ and (b) in the order $dy\,dx\,dz$. | (a) $\displaystyle\int_0^1\!\!\int_0^{y}\!\!\int_{\sqrt y}^{1} f\,dx\,dz\,dy$; (b) $\displaystyle\int_0^1\!\!\int_{\sqrt z}^{1}\!\!\int_{z}^{x^2} f\,dy\,dx\,dz$ | 시험 피적분함수 $f=1,\ x,\ y,\ z,\ xyz,\ e^x+y^2$ 여섯 개 모두에서 세 표현의 값이 일치 (각각 $\tfrac1{10},\tfrac1{12},\tfrac1{21},\tfrac1{42},\tfrac1{80},\ \tfrac{9e}{2}-\tfrac{431}{36}$) (sympy) | ✔ | $E$는 $z=0$, $x=1$, $y=z$와 포물기둥 $y=x^2$($x=\sqrt y$)로 둘러싸인 입체. 정사영 $D_1=\{0\le x\le1,0\le y\le x^2\}=\{0\le y\le1,\sqrt y\le x\le1\}$, $D_2=\{0\le y\le1,0\le z\le y\}=\{0\le z\le1,z\le y\le1\}$, $D_3=\{0\le x\le1,0\le z\le x^2\}=\{0\le z\le1,\sqrt z\le x\le1\}$ |
| 5 | 1165 | 계산 | Use a triple integral to compute the volume of the tetrahedron bounded by $x+2y+z=2$, $x=2y$, $x=0$, $z=0$. | $\dfrac13$ | $\int_0^1\!\int_{x/2}^{1-x/2}\!\int_0^{2-x-2y}dz\,dy\,dx=\dfrac13$ (sympy) | ✔ | 예제 15.2.4와 같은 입체 — 삼중적분은 부피 계산에 필수가 아니라 세우는 또 하나의 방법일 뿐 |
| 6 | 1166–1167 | 계산 | Find the center of mass of the constant-density solid bounded by the parabolic cylinder $x=y^2$ and the planes $x=z$, $z=0$, $x=1$. | $m=\dfrac{4\rho}{5}$; $M_{yz}=\dfrac{4\rho}{7}$, $M_{xz}=0$, $M_{xy}=\dfrac{2\rho}{7}$; 질량중심 $\left(\dfrac57,\,0,\,\dfrac5{14}\right)$ | $E=\{-1\le y\le1,\ y^2\le x\le1,\ 0\le z\le x\}$: $m=\tfrac{4\rho}{5}$, $M_{yz}=\tfrac{4\rho}{7}$, $M_{xz}=0$, $M_{xy}=\tfrac{2\rho}{7}$, 질량중심 $\left(\tfrac57,0,\tfrac5{14}\right)$ (sympy) | ✔ | $E$와 $\rho$가 $xz$-평면에 대칭이므로 $M_{xz}=0$, $\bar y=0$ |

예제 수: **6** (계산 5, 개념·재표현 1)

## C. 그림 필요 목록 (자체 SVG)

| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 1 | 직육면체 $B$와 부분상자 $B_{ijk}$, $\Delta x,\Delta y,\Delta z$ | 선택 | 2 |
| Figure 2 | 제1형 입체영역: 아래 $z=u_1(x,y)$, 위 $z=u_2(x,y)$, 정사영 $D$ | **필수** | 17 (=6) |
| Figure 3·4 | 정사영 $D$가 평면 제I형 / 제II형인 제1형 입체 | 선택 | 7 |
| Figure 5·6 | 예제 2의 입체 $E$와 $xy$-평면 정사영(삼각형 $0\le y\le x\le1$) | **필수** | 예제 2 |
| Figure 7 | 예제 2를 $dz\,dy\,dx$ 순서로 훑어 나가는 3단 그림 | 선택(애니메이션/3컷으로 좋음) | 예제 2, 카드 11 |
| Figure 8 | 제2형 입체영역: 뒤 $x=u_1(y,z)$, 앞 $x=u_2(y,z)$, 정사영 $D$ | **필수** | 17 (=8) |
| Figure 9 | 제3형 입체영역: 왼쪽 $y=u_1(x,z)$, 오른쪽 $y=u_2(x,z)$, 정사영 $D$ | **필수** | 17 (=9) |
| Figure 10·11 | 예제 3의 입체와 $xy$-평면 정사영 $D_1$ (포물선 영역) | 선택 | 예제 3 |
| Figure 12·13 | 예제 3의 입체와 $xz$-평면 정사영 $D_3$ (원판 $x^2+z^2\le4$) | **필수** | 예제 3 |
| Figure 14·15 | 예제 4의 입체 $E$와 세 좌표평면 정사영 $D_1,D_2,D_3$ | **필수** | 예제 4, 카드 11 |
| Figure 16·17 | 예제 5의 사면체와 $xy$-평면 정사영 | 선택(§15.2 Fig 13·14와 동일) | 예제 5 |
| Figure 18 | $E$를 감싼 상자와 부분상자 $B_{ijk}$의 질량 근사 | 선택 | 13 |
| Figure 19 | 예제 6의 입체와 정사영 $D$ ($x=y^2$, $x=1$) | **필수** | 예제 6 |

## D. ERRATA·판독 불확실
- 없음. 여섯 예제 모두 sympy 재계산과 일치.
- 예제 2의 상면 $z=12xy$에서 계수 $12$는 pdftotext 훼손이 아니라 원문 그대로임을 계산으로 확인(답 $4$가 나오려면 $12$여야 함).
- 예제 4는 계산형이 아니라 **재표현형**이므로, 세 표현의 동치성을 여섯 개의 시험 피적분함수로 검증하는 방식으로 anchor를 삼았음.

## E. 절 요약 (사이트 도입 note 초안)
삼중적분은 이중적분의 한 차원 확장이다. 직육면체를 부분상자로 나눈 삼중 리만 합의 극한으로 정의하고, 푸비니 정리에 의해 **여섯 가지 순서**의 반복적분 중 어느 것으로든 계산할 수 있다. 일반 입체영역은 어느 좌표평면으로 정사영하느냐에 따라 제1형($z$가 두 곡면 사이), 제2형($x$가 두 곡면 사이), 제3형($y$가 두 곡면 사이)으로 기술되며, 문제의 난이도는 어느 형을 고르느냐에 크게 좌우된다(예제 3에서 제1형은 사실상 계산 불가, 제3형+극좌표는 몇 줄). 실제로 삼중적분에서 가장 어려운 단계는 계산이 아니라 **영역의 부등식을 세우는 것**이며, "안쪽 한계는 변수 2개, 가운데는 1개, 바깥은 상수"가 검산 규칙이다. 응용으로는 $f=1$일 때의 부피, 그리고 §15.4의 질량·모멘트·질량중심·관성모멘트·전하·확률이 모두 3차원으로 그대로 옮겨 온다.

## F. 공통과제 문항 (2차 공통과제)
- **과제 제출 문항**: 12, 22, 40, 42, 44
- **학습 참고 문항**: 1~2, 3~8, 9~12, 13~22, 23~26, 31~32, 33~36, 37~38, 39~40, 41~42, 43~46, 57~58, 59
