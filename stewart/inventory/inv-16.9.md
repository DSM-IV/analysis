# §16.9 The Divergence Theorem — PDF p.1276–1282 (인쇄 p.1239–1245)

본문 p.1276(하단)–1280, 연습문제 p.1281–1282. 예제 **3개**(PLAN.md와 일치).

## A. 카드 인벤토리 (원문 순서)

| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입) + Equation (1) | 그린 정리 벡터형의 3차원 확장 / Guessing the 3-D Version | 16.5절의 그린 정리 벡터형 $\int_C\mathbf F\cdot\mathbf n\,ds=\iint_D\operatorname{div}\mathbf F(x,y)\,dA$ ($C$ = 평면영역 $D$의 양의 방향 경계)를 $\mathbb R^3$의 벡터장으로 확장하면 (1) $\displaystyle\iint_S\mathbf F\cdot\mathbf n\,dS=\iiint_E\operatorname{div}\mathbf F(x,y,z)\,dV$ 를 추측하게 되고, 적절한 가정 아래 이는 참이다(**발산정리**). 그린 정리·스토크스 정리와 마찬가지로 **영역 위 도함수의 적분 = 경계 위 원래 함수의 적분** 구조 | 1276 | — | — |
| 2 | def | (본문 정의) | 단순입체영역과 양의 방향 / Simple Solid Region, Outward Orientation | 15.6절의 type 1·2·3을 **동시에** 만족하는 영역 $E$를 **단순입체영역(simple solid region)** 이라 한다(타원면·직육면체로 둘러싸인 영역 등). $E$의 경계는 닫힌곡면이고, 16.7절의 규약대로 **양의 방향 = 바깥쪽**($\mathbf n$이 $E$ 밖을 향함) | 1276 | — | — |
| 3 | rem | (여백 노트) | 다른 이름들 / Gauss's Theorem, Ostrogradsky's Theorem | 정전기학 연구 중 이 정리를 발견한 가우스(K. F. Gauss, 1777–1855)의 이름을 따 **가우스 정리**라고도 하고, 동유럽에서는 1826년에 이 결과를 발표한 오스트로그라드스키(M. Ostrogradsky, 1801–1862)의 이름을 따 **오스트로그라드스키 정리**라 부른다 | 1276 | — | — |
| 4 | thm | The Divergence Theorem | 발산정리 / The Divergence Theorem | $E$가 단순입체영역, $S$가 양의(바깥쪽) 방향을 갖는 $E$의 경계곡면이고, $\mathbf F$의 성분함수들이 $E$를 포함하는 열린 영역에서 연속인 편도함수를 가지면 $$\iint_S\mathbf F\cdot d\mathbf S=\iiint_E\operatorname{div}\mathbf F\,dV$$ | 1276 | 본문(카드 6) | — |
| 5 | rem | (본문, 정리 뒤) | 정리의 뜻 / What It Says | 주어진 조건 아래 **$E$의 경계곡면을 가로지르는 $\mathbf F$의 플럭스** 는 **$E$ 위에서 $\operatorname{div}\mathbf F$의 삼중적분** 과 같다 | 1277 | — | — |
| 6 | note | PROOF + Equations (2)–(6) | 증명 개요 / Proof Outline | $\mathbf F=P\mathbf i+Q\mathbf j+R\mathbf k$ 이면 $\operatorname{div}\mathbf F=P_x+Q_y+R_z$ 이고 양변이 세 항으로 쪼개지므로, (2) $\iint_S P\,\mathbf i\cdot\mathbf n\,dS=\iiint_E\frac{\partial P}{\partial x}dV$, (3) $\iint_S Q\,\mathbf j\cdot\mathbf n\,dS=\iiint_E\frac{\partial Q}{\partial y}dV$, (4) $\iint_S R\,\mathbf k\cdot\mathbf n\,dS=\iiint_E\frac{\partial R}{\partial z}dV$ 만 보이면 된다. (4)는 $E$를 type 1 영역 $\{(x,y)\in D,\ u_1(x,y)\le z\le u_2(x,y)\}$ 로 보고, 15.6.6과 **미적분학의 기본정리**로 (5) $\iiint_E\frac{\partial R}{\partial z}dV=\iint_D[R(x,y,u_2)-R(x,y,u_1)]\,dA$. 한편 $S=S_1$(밑)$\cup S_2$(위)$\cup S_3$(연직 옆면)인데 $S_3$에서는 $\mathbf k\cdot\mathbf n=0$ 이라 기여가 0이므로 (6) $\iint_S R\,\mathbf k\cdot\mathbf n\,dS=\iint_{S_1}+\iint_{S_2}$; 16.7.10을 $\mathbf F=R\mathbf k$ 에 적용하면 위쪽 $S_2$는 $+\iint_D R(x,y,u_2)\,dA$, 아래쪽 $S_1$은 $-\iint_D R(x,y,u_1)\,dA$ 로 (5)와 정확히 일치. (2)(3)은 $E$를 type 2·type 3으로 보고 같은 방식. 여백: **그린 정리의 증명 방식과 매우 닮았다** | 1277–1278 | — | Fig 1 |
| 7 | fig | Figure 1 | 경계곡면의 세 조각 / Splitting the Boundary Surface | type 1 영역 $E$, 정사영 $D$, 밑면 $S_1:z=u_1(x,y)$, 윗면 $S_2:z=u_2(x,y)$, 연직 옆면 $S_3$ (구처럼 $S_3$이 없을 수도 있음) | 1277 | — | 필수 |
| 8 | thm | Equation (7) | 구멍 있는 영역으로의 확장 / Extension to Regions with Cavities | 발산정리는 단순입체영역의 **유한 합집합**으로도 확장된다(16.4절에서 그린 정리를 확장한 방식과 동일). 예: 닫힌곡면 $S_1$(안쪽)과 $S_2$(바깥쪽) 사이의 영역 $E$에서 바깥법선을 각각 $\mathbf n_1,\mathbf n_2$ 라 하면 $E$의 경계는 $S=S_1\cup S_2$ 이고 $\mathbf n=-\mathbf n_1$ (on $S_1$), $\mathbf n=\mathbf n_2$ (on $S_2$). 따라서 (7) $\displaystyle\iiint_E\operatorname{div}\mathbf F\,dV=-\iint_{S_1}\mathbf F\cdot d\mathbf S+\iint_{S_2}\mathbf F\cdot d\mathbf S$ | 1279 | — | Fig 3 |
| 9 | fig | Figure 3 | 두 곡면 사이의 영역 / Region Between Two Closed Surfaces | 안쪽 곡면 $S_1$과 바깥 곡면 $S_2$, 각각의 바깥법선 $\mathbf n_1,\mathbf n_2$ 와 $E$의 경계법선 $-\mathbf n_1$ | 1279 | — | 필수 |
| 10 | thm | Equation (9) | 발산의 물리적 의미 / Divergence as Outward Flux Density | 밀도 $\rho$가 일정한 유체의 속도장 $\mathbf v$에 대해 $\mathbf F=\rho\mathbf v$. 점 $P_0$ 중심, 아주 작은 반지름 $a$의 공 $B_a$(경계구 $S_a$)에서 $\operatorname{div}\mathbf F$의 연속성으로 $\iint_{S_a}\mathbf F\cdot d\mathbf S=\iiint_{B_a}\operatorname{div}\mathbf F\,dV\approx\operatorname{div}\mathbf F(P_0)\,V(B_a)$ 이고, $a\to0$ 에서 (9) $\displaystyle\operatorname{div}\mathbf F(P_0)=\lim_{a\to0}\frac{1}{V(B_a)}\iint_{S_a}\mathbf F\cdot d\mathbf S$. 즉 $\operatorname{div}\mathbf F(P_0)$ 는 $P_0$에서의 **단위부피당 순 유출 플럭스**(이것이 "발산"이라는 이름의 유래) | 1280 | 본문(발산정리 + 근사) | — |
| 11 | def | (본문 정의, Figure 4) | 원천과 흡입구 / Source and Sink | $\operatorname{div}\mathbf F(P)>0$ 이면 $P$ 근처에서 순 흐름이 바깥으로 향하고 $P$를 **원천(source)**, $\operatorname{div}\mathbf F(P)<0$ 이면 안으로 향하고 $P$를 **흡입구(sink)** 라 한다. 예(Fig 4): $\mathbf F=x^2\,\mathbf i+y^2\,\mathbf j$ 이면 $\operatorname{div}\mathbf F=2x+2y$ 이므로 직선 $y=-x$ **위쪽** 점들이 원천, 아래쪽이 흡입구 | 1280 | — | Fig 4 |

카드 수: **note 2, def 2, thm 4, rem 2, fig 2 — 합계 12**

## B. 예제 기준값

| Example | PDF 쪽 | 유형 | 문제 요지 (영어 재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1278 | 계산 | Find the flux of $\mathbf F(x,y,z)=z\,\mathbf i+y\,\mathbf j+x\,\mathbf k$ over the unit sphere $x^2+y^2+z^2=1$. | $\operatorname{div}\mathbf F=\frac{\partial}{\partial x}(z)+\frac{\partial}{\partial y}(y)+\frac{\partial}{\partial z}(x)=1$. $S$는 단위공 $B$의 경계이므로 $\iint_S\mathbf F\cdot d\mathbf S=\iiint_B 1\,dV=V(B)=\frac43\pi(1)^3=\boxed{\dfrac{4\pi}{3}}$ | sympy: $\operatorname{div}\mathbf F=1$, $V(B)=4\pi/3$; **2차 방법**(구면 매개화 직접 곡면적분, = 예제 16.7.4) $=4\pi/3$ | ✓ | 여백: 예제 16.7.4의 풀이와 비교할 것 — 같은 답을 훨씬 짧게 |
| 2 | 1278–1279 | 계산 | Evaluate $\iint_S\mathbf F\cdot d\mathbf S$ for $\mathbf F=xy\,\mathbf i+\left(y^2+e^{xz^2}\right)\mathbf j+\sin(xy)\,\mathbf k$, where $S$ is the boundary of the solid $E$ bounded by the parabolic cylinder $z=1-x^2$ and the planes $z=0$, $y=0$, $y+z=2$. | 직접 하면 곡면 4조각을 적분해야 하지만 $\operatorname{div}\mathbf F=y+2y+0=3y$ 로 훨씬 간단. $E$를 type 3으로 $\{-1\le x\le1,\ 0\le z\le1-x^2,\ 0\le y\le2-z\}$ 라 쓰면 $\iint_S\mathbf F\cdot d\mathbf S=\iiint_E 3y\,dV=3\int_{-1}^{1}\!\!\int_0^{1-x^2}\!\!\int_0^{2-z}y\,dy\,dz\,dx=-\frac12\int_{-1}^1[(x^2+1)^3-8]\,dx=-2\int_0^1(x^6+3x^4+3x^2-7)\,dx=\boxed{\dfrac{184}{35}}$ | sympy: $\operatorname{div}\mathbf F=3y$, 삼중적분 $=184/35\approx5.2571428571$; **적분 순서를 바꾼 2차 계산**도 $184/35$ | ✓ | $e^{xz^2}$, $\sin(xy)$ 항은 발산에서 소거됨 |
| 3 | 1279–1280 | 증명(show) | Using the Divergence Theorem, show that the electric flux of $\mathbf E(\mathbf x)=\dfrac{\varepsilon Q}{|\mathbf x|^3}\mathbf x$ (charge $Q$ at the origin) through **any** closed surface $S$ enclosing the origin equals $4\pi\varepsilon Q$. | $S$ 안쪽에 들어가는 반지름 $a$의 구 $S_1$(원점 중심)을 잡고 $E$를 그 사이 영역이라 하면 (7)에서 (8) $\iiint_E\operatorname{div}\mathbf E\,dV=-\iint_{S_1}\mathbf E\cdot d\mathbf S+\iint_S\mathbf E\cdot d\mathbf S$. 원점 밖에서 $\operatorname{div}\mathbf E=0$(연습 25)이므로 $\iint_S\mathbf E\cdot d\mathbf S=\iint_{S_1}\mathbf E\cdot d\mathbf S$. $S_1$ 위의 법선은 $\mathbf x/|\mathbf x|$ 이므로 $\mathbf E\cdot\mathbf n=\frac{\varepsilon Q}{|\mathbf x|^4}\mathbf x\cdot\mathbf x=\frac{\varepsilon Q}{|\mathbf x|^2}=\frac{\varepsilon Q}{a^2}$, 따라서 $\iint_S\mathbf E\cdot d\mathbf S=\frac{\varepsilon Q}{a^2}A(S_1)=\frac{\varepsilon Q}{a^2}\cdot4\pi a^2=\boxed{4\pi\varepsilon Q}$ | sympy: $\operatorname{div}\mathbf E=0$ (원점 제외), $\frac{\varepsilon Q}{a^2}\cdot4\pi a^2=4\pi\varepsilon Q$ | ✓ | 단일 전하에 대한 가우스 법칙(16.7.11)의 특수경우; $\varepsilon=1/(4\pi\varepsilon_0)$ 이므로 $Q=\varepsilon_0\iint_S\mathbf E\cdot d\mathbf S$ 와 정합 |

예제 수: **3** (계산 2, 증명 1). anchor 불일치: **0건**.
재계산 스크립트: `/Users/chalrs/analysis/stewart/inventory/anchor-16.9.py`

## C. 그림 필요 목록 (자체 SVG)

| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 1 | type 1 영역 $E$, 정사영 $D$, 경계 세 조각 $S_1$(밑, $z=u_1$)·$S_2$(위, $z=u_2$)·$S_3$(연직 옆면) | **필수** | 7 |
| Figure 2 | 예제 2의 입체: 포물기둥 $z=1-x^2$, 평면 $z=0$, $y=0$, $y+z=2$ 로 둘러싸인 영역 | 선택 | 예제 2 |
| Figure 3 | 안쪽 닫힌곡면 $S_1$과 바깥 닫힌곡면 $S_2$ 사이의 영역 $E$, 법선 $\mathbf n_1,\mathbf n_2$ 와 $-\mathbf n_1$ | **필수** | 9 |
| Figure 4 | 벡터장 $\mathbf F=x^2\mathbf i+y^2\mathbf j$ 의 화살표 그림, 원천 $P_1$과 흡입구 $P_2$, 경계선 $y=-x$ | 선택 | 11 |

## D. ERRATA·판독 불확실

- pdftotext 인코딩 왜곡으로 여러 곳에서 $\pi$ 와 부호가 탈락한다. PNG로 확인한 정확한 값:
  - 예제 3: $\iint_S\mathbf E\cdot d\mathbf S=\mathbf{4\pi\varepsilon Q}$, $A(S_1)=4\pi a^2$ (p-1280).
  - 식 (9): $\operatorname{div}\mathbf F(P_0)=\lim_{a\to0}\frac{1}{V(B_a)}\iint_{S_a}\mathbf F\cdot d\mathbf S$ (p-1280).
  - Figure 4 논의: $\operatorname{div}\mathbf F=2x+2y>0\iff y>\mathbf{-x}$, 경계선은 $y=\mathbf{-x}$ (추출본의 `y . 2x`, `y − 2x` 는 각각 $y>-x$, $y=-x$).
- 예제 2의 $j$ 성분은 $y^2+e^{xz^2}$ (추출본의 `y 2 1 e xz` 는 $y^2+e^{xz^2}$; PNG p-1278에서 확인).
- 예제 3의 $\varepsilon$ 은 추출본에서 `«`로 나타난다. 정전기 상수 관계는 $\varepsilon=1/(4\pi\varepsilon_0)$.
- 그 외 판독 불확실 없음. PLAN.md의 예제 수(3)는 정확.

## E. 절 요약 (사이트 도입 note 초안)

발산정리는 그린 정리의 벡터형(플럭스 형태)을 한 차원 올린 것이다. 입체영역 $E$가 type 1·2·3을 동시에 만족하는 단순입체영역이고 그 경계곡면 $S$에 바깥쪽 방향을 주면, $\iint_S\mathbf F\cdot d\mathbf S=\iiint_E\operatorname{div}\mathbf F\,dV$ 가 성립한다 — 경계를 가로지르는 플럭스가 내부의 발산을 모두 더한 것과 같다는 뜻이다. 증명은 $\operatorname{div}\mathbf F$의 세 항을 따로 다루고, 각 항에서 $E$를 알맞은 type으로 보아 미적분학의 기본정리와 16.7.10을 쓰면 되며, 연직 옆면이 $\mathbf k\cdot\mathbf n=0$ 으로 사라지는 것이 핵심이다. 정리는 단순입체영역의 유한 합집합, 특히 두 닫힌곡면 사이의 "구멍 뚫린" 영역으로도 확장되어(식 (7)), 원점의 점전하가 만드는 전기다발이 곡면 모양과 무관하게 $4\pi\varepsilon Q$ 임을 보이는 데 쓰인다. 끝으로 $\operatorname{div}\mathbf F(P_0)=\lim_{a\to0}\frac1{V(B_a)}\iint_{S_a}\mathbf F\cdot d\mathbf S$ 는 발산이 **단위부피당 순 유출률**임을 말해주며, 값이 양이면 원천, 음이면 흡입구다.

## F. 공통과제 문항 (4차 공통과제)

- **과제 제출 문항**: 2, 7, 11, 15, 20
- **학습 참고 문항**: 1~4, 5~17, 19, 20, 26, 27, 29
