# §16.4 Green's Theorem — PDF p.1229–1235 (인쇄 p.1192–1198; 본문 p.1229–1234, 연습문제 p.1234–1235)

## A. 카드 인벤토리 (원문 순서)
| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입) ■ Green's Theorem | 그린 정리가 잇는 두 적분 / What Green's Theorem Relates | 단순닫힌곡선 $C$ 위의 **선적분**과 $C$가 둘러싼 평면영역 $D$ 위의 **이중적분** 사이의 관계. $D$는 $C$ 내부의 점과 $C$ 위의 점을 모두 포함한다고 본다 | 1229 | — | Fig 1 |
| 2 | rem | (배향 규약) | 양의 배향 / Positive Orientation | 단순닫힌곡선 $C$의 **양의 배향**은 반시계 방향으로 한 바퀴 도는 것. 동치로, $\mathbf r(t)$가 $C$를 지날 때 영역 $D$가 항상 **왼쪽**에 놓임 | 1229 | — | Fig 2 |
| 3 | thm | Green's Theorem (박스) | 그린 정리 / Green's Theorem | $C$가 평면의 양으로 배향된 조각마다 매끄러운 단순닫힌곡선, $D$가 $C$로 둘러싸인 영역이고 $P,Q$가 $D$를 포함하는 열린 영역에서 연속인 편도함수를 가지면 $$\oint_C P\,dx+Q\,dy=\iint_D\Bigl(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Bigr)dA$$ 좌변은 $\mathbf F=P\mathbf i+Q\mathbf j$에 대한 $\int_C\mathbf F\cdot d\mathbf r$와 같음 | 1229 | 본문 (단순영역, 카드 6) | — |
| 4 | rem | NOTE (표기) + (1) | $\oint$ 와 $\partial D$ 표기 / Notation | 양의 배향임을 나타낼 때 $\displaystyle\oint_C P\,dx+Q\,dy$ 로 쓴다. $D$의 양으로 배향된 경계곡선을 $\partial D$로 쓰면 (1) $\displaystyle\iint_D\Bigl(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Bigr)dA=\int_{\partial D}P\,dx+Q\,dy$ | 1229 | — | — |
| 5 | note | (FTC 비교 단락) | 이중적분판 미적분학 기본정리 / Green's Theorem as a 2-D FTC | (1)과 $\int_a^b F'(x)dx=F(b)-F(a)$를 비교하면: 두 경우 모두 좌변은 **도함수**($F'$, $Q_x$, $P_y$)의 적분, 우변은 **정의역의 경계**에서의 원래 함수($F$, $P$, $Q$) 값. 1차원에서는 경계가 두 점 $a,b$ | 1229–1230 | — | — |
| 6 | note | PROOF (단순영역의 경우) | 그린 정리의 증명 (단순영역) / Proof for a Simple Region | $D$가 type I이자 type II인 **단순영역**일 때: (2) $\displaystyle\int_C P\,dx=-\iint_D\frac{\partial P}{\partial y}dA$와 (3) $\displaystyle\int_C Q\,dy=\iint_D\frac{\partial Q}{\partial x}dA$를 각각 보이고 더한다. (2)는 $D=\{(x,y)\mid a\le x\le b,\ g_1(x)\le y\le g_2(x)\}$로 두어 (4) $\iint_D P_y\,dA=\int_a^b[P(x,g_2(x))-P(x,g_1(x))]\,dx$ (FTC)를 얻고, $C=C_1\cup C_2\cup C_3\cup C_4$로 나눠 $C_2,C_4$에서 $dx=0$, $C_1$·$-C_3$을 $x$로 매개변수화해 비교 | 1230–1231 | 본문 (전체 일반 증명은 어려움) | Fig 3 |
| 7 | note | (역방향 사용 단락) | 그린 정리를 거꾸로 쓰기 / Using the Theorem in Reverse | 보통은 이중적분이 더 쉽지만(예제 1·2) 반대인 경우도 있다. 예: $C$ 위에서 $P=Q=0$이면 $D$ 안에서 $P,Q$가 무엇이든 $\displaystyle\iint_D(Q_x-P_y)\,dA=\oint_C P\,dx+Q\,dy=0$ | 1231 | — | — |
| 8 | thm | ■ Finding Areas…, Formula (5) | 그린 정리로 넓이 구하기 / Areas by Green's Theorem | $Q_x-P_y=1$이 되도록 $(P,Q)=(0,x),\,(-y,0),\,(-\tfrac12y,\tfrac12x)$를 택하면 (5) $$A=\oint_C x\,dy=-\oint_C y\,dx=\tfrac12\oint_C x\,dy-y\,dx$$ | 1231–1232 | 본문 (그린 정리 적용) | — |
| 9 | note | (플래니미터) | 플래니미터 / The Planimeter | 19세기에 발명된, 경계곡선을 따라 그리면 영역의 넓이를 재는 기계 장치. 극 플래니미터는 바퀴가 굴러간 거리가 넓이에 비례하며, 식 (5)로 그 원리를 설명할 수 있다 | 1232 | — | Fig 5 (사진) |
| 10 | note | ■ Extended Versions… (합집합) | 단순영역의 유한 합집합으로 확장 / Extension to Finite Unions | $D=D_1\cup D_2$ (각각 단순, 겹치지 않음)이고 $\partial D_1=C_1\cup C_3$, $\partial D_2=C_2\cup(-C_3)$일 때 두 식을 더하면 $C_3$와 $-C_3$의 선적분이 상쇄되어 $\oint_{C_1\cup C_2}P\,dx+Q\,dy=\iint_D(Q_x-P_y)dA$. 겹치지 않는 단순영역의 임의의 유한 합집합에 대해 성립 | 1232–1233 | 본문 | Fig 6, 7 |
| 11 | note | (구멍 있는 영역) | 구멍 있는 영역으로의 확장 / Regions with Holes | 단순연결이 아닌 영역에도 확장된다. 경계 $C=C_1\cup C_2$(바깥·안쪽 단순닫힌곡선)를 **$D$가 항상 왼쪽**이 되도록 배향하면 바깥 $C_1$은 반시계, 안쪽 $C_2$는 시계 방향. 절단선으로 $D=D'\cup D''$로 나눠 각각에 그린 정리를 적용하면 공통 절단선 적분이 상쇄되어 $\displaystyle\iint_D(Q_x-P_y)\,dA=\oint_{C_1}+\oint_{C_2}=\oint_C P\,dx+Q\,dy$ | 1233 | 본문 | Fig 9, 10 |
| 12 | thm | SKETCH OF PROOF OF THEOREM 16.3.6 | 평면 보존장 판정법의 증명 개요 / Sketch Proof of Theorem 16.3.6 | 열린 단순연결 $D$에서 $P_y=Q_x$이면, $D$ 안의 임의의 단순닫힌경로 $C$와 그것이 둘러싼 $R$에 대해 그린 정리로 $\oint_C\mathbf F\cdot d\mathbf r=\iint_R(Q_x-P_y)dA=0$. 단순하지 않은 닫힌 곡선은 단순곡선들로 쪼개 더하면 되므로 모든 닫힌 곡선에서 $0$ → 정리 16.3.3에 의해 경로에 무관 → $\mathbf F$는 보존적 | 1234 | 본문(개요) | — |
| 13 | fig | Figure 2 | 양의 배향과 음의 배향 / Positive vs. Negative Orientation | 같은 영역 $D$의 경계를 반시계·시계로 도는 두 그림 | 1229 | — | 필수 |
| 14 | fig | Figures 9–10 | 구멍 있는 영역의 경계 배향 / Boundary Orientation for a Region with a Hole | 바깥 $C_1$ 반시계, 안쪽 $C_2$ 시계; 절단선으로 $D',D''$로 분할 | 1233 | — | 필수 |
| 15 | fig | Figure 8 | 예제 4의 반환형 영역 / The Semiannular Region | 상반평면에서 $x^2+y^2=1$과 $x^2+y^2=4$ 사이 영역과 그 경계 배향 | 1233 | — | 선택 |
| 16 | fig | Figure 3 | 증명의 $C_1\!\sim\! C_4$ 분해 / Decomposition in the Proof | type I 영역 $g_1(x)\le y\le g_2(x)$의 경계 네 조각 | 1230 | — | 선택 |

## B. 예제 기준값
| Example | PDF 쪽 | 유형 | 문제 요지 (영어 재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1231 | 계산 | Use Green's Theorem to evaluate $\oint_C x^{4}\,dx+xy\,dy$ around the triangle with vertices $(0,0),(1,0),(0,1)$ traversed in that order. | $\dfrac16$ | sympy 이중적분 $\int_0^1\!\!\int_0^{1-x}y\,dy\,dx=\frac16$; 세 변 직접 선적분 합 $\frac15-\frac1{30}+0=\frac16$ | ✔ | 직접 계산하려면 세 변에 대해 세 개의 적분이 필요 — 그린 정리가 훨씬 간단 |
| 2 | 1231 | 계산 | Use Green's Theorem to evaluate $\oint_C(3y-e^{\sin x})\,dx+\bigl(7x+\sqrt{y^{4}+1}\bigr)dy$ around the circle $x^{2}+y^{2}=9$. | $36\pi$ | sympy: $Q_x-P_y=4$, $\iint_D 4\,dA=4\cdot\pi\cdot3^2=36\pi$ | ✔ | 극좌표를 쓰지 않고 "$D$는 반지름 3인 원판"이라는 사실만 써도 됨 |
| 3 | 1232 | 계산 | Find the area enclosed by the ellipse $\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}=1$ using formula (5). | $A=\pi ab$ | sympy: 식 (5)의 세 형태 $\oint x\,dy$, $-\oint y\,dx$, $\tfrac12\oint x\,dy-y\,dx$ 모두 $\pi ab$ | ✔ | 매개변수화 $x=a\cos t,\ y=b\sin t,\ 0\le t\le2\pi$ |
| 4 | 1233 | 계산 | Use the extended Green's Theorem to evaluate $\oint_C y^{2}\,dx+3xy\,dy$ where $C$ is the boundary of the upper-half semiannular region between $x^{2}+y^{2}=1$ and $x^{2}+y^{2}=4$. | $\dfrac{14}{3}$ | sympy: $Q_x-P_y=y$, $\int_0^{\pi}\!\!\int_1^2 (r\sin\theta)\,r\,dr\,d\theta=\frac{14}3$; 경계 4조각 직접 선적분 $\frac{16}3-\frac23+0+0=\frac{14}3$ | ✔ | $D$는 단순영역이 아니지만 $y$축이 두 단순영역으로 나눔 |
| 5 | 1233–1234 | 증명(show) | Show that $\oint_C\mathbf F\cdot d\mathbf r=2\pi$ for **every** positively oriented simple closed path enclosing the origin, where $\mathbf F(x,y)=\dfrac{-y\,\mathbf i+x\,\mathbf j}{x^{2}+y^{2}}$. | $\displaystyle\oint_C\mathbf F\cdot d\mathbf r=2\pi$. 증명: $C$ 안쪽에 원점 중심 반지름 $a$인 반시계 원 $C'$을 잡고 $D$를 $C$와 $C'$ 사이 영역으로 두면 $\partial D=C\cup(-C')$이고 $Q_x-P_y=\dfrac{y^2-x^2}{(x^2+y^2)^2}-\dfrac{y^2-x^2}{(x^2+y^2)^2}=0$이므로 확장 그린 정리로 $\oint_C=\oint_{C'}$; $\mathbf r(t)=a\cos t\,\mathbf i+a\sin t\,\mathbf j$로 계산하면 $\int_0^{2\pi}\!dt=2\pi$ | sympy: $Q_x-P_y=0$ (원점 제외); 반지름 $a$ 원에서 $2\pi$ (모든 $a>0$); 원이 아닌 타원 $(3\cos t,2\sin t)$에서도 $2\pi$ (경로무관 확인) | ✔ | 이 $\mathbf F$는 $P_y=Q_x$이지만 정의역 $\mathbb R^2\setminus\{0\}$이 단순연결이 아니어서 **보존적이 아님** — 정리 16.3.6의 단순연결 가정이 필수임을 보여주는 예. sympy가 타원 적분의 심볼릭 원시함수를 불연속으로 잡아 $\pi$를 주므로 4등분·수치적분으로 확인함(anchor 스크립트에 반영) |

## C. 그림 필요 목록 (자체 SVG)
| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 2 | 양의 배향(반시계, $D$가 왼쪽)과 음의 배향(시계) | 필수 | 13 (카드 2) |
| Figure 9 + 10 | 구멍 있는 영역: 바깥 $C_1$ 반시계 / 안쪽 $C_2$ 시계, 절단선에 의한 $D',D''$ 분할 | 필수 | 14 (카드 11) |
| Figure 8 | 예제 4의 반환형 영역 $1\le r\le2,\ 0\le\theta\le\pi$와 경계 | 선택 | 15 (예제 4) |
| Figure 3 | 증명의 type I 영역과 $C_1,C_2,C_3,C_4$ | 선택 | 16 (카드 6) |
| Figure 6 + 7 | $D=D_1\cup D_2$와 상쇄되는 공통 경계 $C_3$; 여러 단순영역의 합집합 | 선택 | 10 |
| Figure 11 | 예제 5의 $C$와 내부의 작은 원 $C'$ | 선택 | 예제 5 |
| Figure 4 | 예제 1의 삼각형 영역 | 선택 | 예제 1 |
| Figure 5 | 극 플래니미터 사진 | 제외 | — |

## D. ERRATA·판독 불확실
- 교재 오류 없음 — 5개 예제 최종답 모두 sympy 재계산과 일치 (예제 1·4는 그린 정리 쪽과 직접 선적분 쪽 **두 방법**으로 교차 확인).
- 재계산 도구 주의: 예제 5의 검증용 타원 경로 적분에서 sympy의 심볼릭 원시함수가 $[0,2\pi]$에서 불연속이라 $\pi$가 나온다. 구간을 4등분해 더하거나 수치적분하면 $2\pi$ — 교재 답이 옳고 sympy 쪽이 함정이다. (anchor-16.4.py에 두 방법 모두 기록)

## E. 절 요약 (사이트 도입 note 초안)
그린 정리는 평면의 단순닫힌곡선 위의 선적분을 그 곡선이 둘러싼 영역의 이중적분으로 바꿔 준다: $\oint_C P\,dx+Q\,dy=\iint_D(Q_x-P_y)\,dA$. 여기서 곡선은 항상 영역이 왼쪽에 오도록(반시계) 양의 배향을 준다. 좌변이 경계에서의 함수값, 우변이 도함수의 적분이라는 점에서 이 정리는 이중적분판 미적분학 기본정리로 볼 수 있고, 증명은 영역이 type I이면서 type II인 단순영역일 때 $\int_C P\,dx=-\iint_D P_y\,dA$와 $\int_C Q\,dy=\iint_D Q_x\,dA$를 각각 보인 뒤 더하는 방식이다. 실제 계산에서는 대개 이중적분 쪽이 훨씬 쉽지만, $Q_x-P_y=1$이 되도록 $P,Q$를 고르면 거꾸로 선적분으로 넓이를 구할 수도 있다: $A=\oint_C x\,dy=-\oint_C y\,dx=\tfrac12\oint_C x\,dy-y\,dx$. 겹치지 않는 단순영역의 유한 합집합, 나아가 구멍이 있어 단순연결이 아닌 영역까지 정리가 확장되며(절단선 위의 선적분이 서로 상쇄된다), 이 확장판을 쓰면 원점을 둘러싸는 임의의 닫힌 경로에서 $\oint(-y\,dx+x\,dy)/(x^2+y^2)=2\pi$ 같은 결과를 얻고 §16.3의 보존장 판정법(정리 16.3.6)도 증명할 수 있다.

## F. 공통과제 문항
- 3차 공통과제, 16.4 Green's Theorem
  - **과제 제출 문항**: 3, 9, 15, 17, 25, 31
  - **학습 참고 문항**: 5~12, 13~18, 21~23, 25, 31~33
