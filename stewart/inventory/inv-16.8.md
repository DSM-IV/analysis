# §16.8 Stokes' Theorem — PDF p.1270–1275 (인쇄 p.1233–1238)

본문 p.1270–1274(상단), 연습문제 p.1274–1275. 예제 **2개**(PLAN.md와 일치).

## A. 카드 인벤토리 (원문 순서)

| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입) | 그린 정리의 3차원판 / Stokes as Higher-Dimensional Green | 그린 정리가 평면영역 $D$ 위의 이중적분과 그 평면 경계곡선의 선적분을 잇는다면, 스토크스 정리는 **곡면** $S$ 위의 곡면적분과 그 경계곡선(공간곡선)의 선적분을 잇는다 | 1270 | — | — |
| 2 | rem | (Figure 1 규약) | 경계곡선의 양의 방향 / Positive Orientation of the Boundary Curve | 단위법선 $\mathbf n$ 이 주어진 유향곡면 $S$는 경계곡선 $C$의 **양의 방향**을 유도한다: 머리를 $\mathbf n$ 방향으로 두고 $C$를 양의 방향으로 걸으면 **곡면이 항상 왼쪽**에 있다 (오른손 법칙) | 1270 | — | Fig 1 |
| 3 | fig | Figure 1 | 방향 규약 / Orientation Convention | 유향곡면 $S$ 위의 법선 $\mathbf n$ 들과 유도된 경계곡선 $C$의 진행 방향 화살표 | 1270 | — | 필수 |
| 4 | thm | Stokes' Theorem | 스토크스 정리 / Stokes' Theorem | $S$가 양의 방향을 갖는 단순·닫힌·조각별 매끄러운 경계곡선 $C$로 둘러싸인 유향 조각별 매끄러운 곡면이고, $\mathbf F$의 성분들이 $S$를 포함하는 $\mathbb R^3$의 열린 영역에서 연속인 편도함수를 가지면 $$\int_C\mathbf F\cdot d\mathbf r=\iint_S\operatorname{curl}\mathbf F\cdot d\mathbf S$$ | 1270 | 본문 — 특수경우만(카드 7) | Fig 1 |
| 5 | rem | Equation (1) + 표기 | 접선성분 vs 법선성분, $\partial S$ 표기 / Tangential vs Normal, the $\partial S$ Notation | $\int_C\mathbf F\cdot d\mathbf r=\int_C\mathbf F\cdot\mathbf T\,ds$, $\iint_S\operatorname{curl}\mathbf F\cdot d\mathbf S=\iint_S\operatorname{curl}\mathbf F\cdot\mathbf n\,dS$ 이므로, 스토크스 정리는 "**경계에서 $\mathbf F$의 접선성분의 선적분 = $S$ 위 $\operatorname{curl}\mathbf F$의 법선성분의 곡면적분**". 양의 방향 경계곡선을 $\partial S$로 쓰면 (1) $\displaystyle\iint_S\operatorname{curl}\mathbf F\cdot d\mathbf S=\int_{\partial S}\mathbf F\cdot d\mathbf r$ | 1270 | — | — |
| 6 | note | (본문) | FTC·그린 정리와의 유비 / Analogy with FTC and Green | 좌변은 도함수를 포함한 적분($\operatorname{curl}\mathbf F$는 $\mathbf F$의 일종의 도함수), 우변은 **경계에서의 $\mathbf F$ 값만** 쓴다 — 미적분학의 기본정리와 같은 구조. 특히 $S$가 $xy$-평면 안의 평평한 영역이고 위쪽 방향이면 $\mathbf n=\mathbf k$ 이고 $\int_C\mathbf F\cdot d\mathbf r=\iint_S(\operatorname{curl}\mathbf F)\cdot\mathbf k\,dA$ — 이는 그린 정리의 벡터형 (16.5.12) 그 자체다. 즉 **그린 정리는 스토크스 정리의 특수경우** | 1270 | — | — |
| 7 | note | PROOF OF A SPECIAL CASE + Equation (2) | 특수경우의 증명 / Proof for a Graph | $S:z=g(x,y)$, $(x,y)\in D$ ($g$는 2계 편도함수 연속, $D$는 단순영역, 경계 $C_1\leftrightarrow C$), $S$는 위쪽 방향. ① 식 16.7.10을 $\mathbf F$ 대신 $\operatorname{curl}\mathbf F$에 적용해 (2) $\displaystyle\iint_S\operatorname{curl}\mathbf F\cdot d\mathbf S=\iint_D\left[-\left(\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z}\right)\frac{\partial z}{\partial x}-\left(\frac{\partial P}{\partial z}-\frac{\partial R}{\partial x}\right)\frac{\partial z}{\partial y}+\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)\right]dA$. ② $C$의 매개화 $x=x(t),y=y(t),z=g(x(t),y(t))$ 에 연쇄법칙을 써서 $\int_C\mathbf F\cdot d\mathbf r=\int_{C_1}\left(P+R\frac{\partial z}{\partial x}\right)dx+\left(Q+R\frac{\partial z}{\partial y}\right)dy$. ③ 여기에 **그린 정리**를 적용하고 다시 연쇄법칙으로 전개하면 항 4개가 상쇄되고 남은 6개가 (2)의 우변과 정확히 일치한다 ($R_{xy}=R_{yx}$ 이용) | 1270–1271 | 본문 | Fig 2 |
| 8 | rem | NOTE + Equation (3) | 경계가 같으면 값도 같다 / Same Boundary, Same Integral | 스토크스 정리는 곡면적분을 **경계곡선 위의 $\mathbf F$ 값만으로** 계산하게 해준다. 따라서 $S_1,S_2$가 같은 유향 경계곡선 $C$를 갖고 정리의 가정을 만족하면 (3) $\displaystyle\iint_{S_1}\operatorname{curl}\mathbf F\cdot d\mathbf S=\int_C\mathbf F\cdot d\mathbf r=\iint_{S_2}\operatorname{curl}\mathbf F\cdot d\mathbf S$. 한 곡면에서 적분이 어렵고 다른 곡면에서 쉬울 때 유용 | 1272 | — | — |
| 9 | def | (본문 정의, Figure 6) | 순환 / Circulation | $\mathbf v$가 유체의 속도장, $C$가 유향 닫힌곡선일 때 $\int_C\mathbf v\cdot d\mathbf r=\int_C\mathbf v\cdot\mathbf T\,ds$ 를 **$C$ 둘레의 $\mathbf v$의 순환(circulation)** 이라 한다. $\mathbf v$의 방향이 $\mathbf T$에 가까울수록 값이 커지므로, 유체가 $C$의 방향대로 돌려는 경향의 척도다(반대 방향이면 음수) | 1273 | — | Fig 6 |
| 10 | fig | Figures 6, 7 | 순환의 부호와 물레방아 / Circulation Sign & Paddle Wheel | $C_1$(양의 순환)·$C_2$(음의 순환)에서 $\mathbf v$와 $\mathbf T$의 상대 방향; 유체 속 작은 물레방아와 축 방향 $\operatorname{curl}\mathbf v$ | 1273–1274 | — | 필수 |
| 11 | thm | Equation (4) | 회전(curl)의 순환 해석 / Curl as Circulation Density | 점 $P_0$ 중심, 반지름 $a$인 작은 원판 $S_a$(경계원 $C_a$)에서 $\operatorname{curl}\mathbf v$의 연속성으로 $\int_{C_a}\mathbf v\cdot d\mathbf r\approx\operatorname{curl}\mathbf v(P_0)\cdot\mathbf n(P_0)\,\pi a^2$ 이고, $a\to0$ 극한에서 (4) $\displaystyle\operatorname{curl}\mathbf v(P_0)\cdot\mathbf n(P_0)=\lim_{a\to0}\frac{1}{\pi a^2}\int_{C_a}\mathbf v\cdot d\mathbf r$. 즉 $\operatorname{curl}\mathbf v\cdot\mathbf n$ 은 축 $\mathbf n$ 둘레의 회전 효과의 척도이고, **회전 효과는 $\operatorname{curl}\mathbf v$ 와 평행한 축에서 최대** | 1274 | 본문(스토크스 정리 + 근사) | Fig 7 |
| 12 | note | (절 마무리) | 정리 16.5.4의 증명 / Proving Theorem 16.5.4 | $\operatorname{curl}\mathbf F=\mathbf 0$ 이 $\mathbb R^3$ 전체에서 성립하면 $\mathbf F$는 보존장이다(16.5.4). 증명: 16.3.3·16.3.4에 의해 모든 닫힌 경로 $C$에 대해 $\int_C\mathbf F\cdot d\mathbf r=0$ 임을 보이면 충분한데, $C$를 경계로 갖는 가향곡면 $S$를 잡으면(고급 기법이 필요하지만 가능) 스토크스 정리로 $\int_C\mathbf F\cdot d\mathbf r=\iint_S\operatorname{curl}\mathbf F\cdot d\mathbf S=\iint_S\mathbf 0\cdot d\mathbf S=0$. 단순하지 않은 곡선은 단순곡선 여러 개로 쪼개 더한다 | 1274 | 본문 | — |

카드 수: **note 4, def 1, thm 2, rem 3, fig 2 — 합계 12**

## B. 예제 기준값

| Example | PDF 쪽 | 유형 | 문제 요지 (영어 재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1272 | 계산 | Evaluate $\int_C\mathbf F\cdot d\mathbf r$ for $\mathbf F=-y^2\,\mathbf i+x\,\mathbf j+z^2\,\mathbf k$, where $C$ is the ellipse cut from the cylinder $x^2+y^2=1$ by the plane $y+z=2$, oriented counterclockwise seen from above. | $\operatorname{curl}\mathbf F=(1+2y)\,\mathbf k$. 경계가 $C$인 가장 편한 곡면은 평면 $y+z=2$ 안의 타원영역 $S$(위쪽 방향), 정사영 $D$는 단위원판. 식 16.7.10을 $z=g(x,y)=2-y$ 로 적용하면 $\int_C\mathbf F\cdot d\mathbf r=\iint_D(1+2y)\,dA=\int_0^{2\pi}\!\!\int_0^1(1+2r\sin\theta)\,r\,dr\,d\theta=\frac12(2\pi)+0=\boxed{\pi}$ | sympy: 곡면적분 $=\pi$; **독립 2차 방법**(타원 $\mathbf r(t)=(\cos t,\sin t,2-\sin t)$ 위 직접 선적분) $=\pi$ | ✓ | 두 방법 모두 $\pi$ — 교재 답 확정 |
| 2 | 1272–1273 | 계산 | Use Stokes' Theorem to compute $\iint_S\operatorname{curl}\mathbf F\cdot d\mathbf S$ for $\mathbf F=xz\,\mathbf i+yz\,\mathbf j+xy\,\mathbf k$, where $S$ is the part of the sphere $x^2+y^2+z^2=4$ inside the cylinder $x^2+y^2=1$ and above the $xy$-plane. | 경계 $C$: 두 식을 빼면 $z^2=3$, $z>0$ 이므로 $x^2+y^2=1,\ z=\sqrt3$; $\mathbf r(t)=\cos t\,\mathbf i+\sin t\,\mathbf j+\sqrt3\,\mathbf k$. **해 1**: $\mathbf F(\mathbf r(t))\cdot\mathbf r'(t)=-\sqrt3\cos t\sin t+\sqrt3\sin t\cos t=0$ → 적분 $\boxed{0}$. **해 2**(식 (3) 이용): 같은 경계를 갖는 평면 원판 $S_1\subset\{z=\sqrt3\}$ 로 바꾸면 $\mathbf n=\mathbf k$, $\operatorname{curl}\mathbf F=(x-y)\mathbf i+(x-y)\mathbf j$ 이므로 $\operatorname{curl}\mathbf F\cdot\mathbf k=0$ → $\boxed{0}$ | sympy: $\operatorname{curl}\mathbf F=(x-y,\,x-y,\,0)$; 해 1 = 0, 해 2 = 0, **3차 방법**(구면 캡 $0\le\phi\le\arcsin\frac12$ 위 직접 곡면적분) = 0 | ✓ | 세 방법 모두 0 |

예제 수: **2** (둘 다 계산형). anchor 불일치: **0건**.
재계산 스크립트: `/Users/chalrs/analysis/stewart/inventory/anchor-16.8.py`

## C. 그림 필요 목록 (자체 SVG)

| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 1 | 유향곡면 $S$, 법선 $\mathbf n$ 들, 유도된 경계곡선 $C$의 양의 방향 (왼쪽에 곡면이 놓이는 걷기 규약) | **필수** | 3 |
| Figure 2 | 증명용: 그래프 $S:z=g(x,y)$, 정사영 $D$, 대응 경계 $C\leftrightarrow C_1$ | 선택 | 7 |
| Figure 3 | 예제 1: 원기둥 $x^2+y^2=1$ 과 평면 $y+z=2$ 가 자르는 타원 $C$ 및 타원영역 $S$, 정사영 $D$ | 선택 | 예제 1 |
| Figures 4, 5 | 예제 2: 구 $x^2+y^2+z^2=4$ 의 캡 $S$ 와 경계원 $C$; 대체 곡면 $S_1$(평면 $z=\sqrt3$ 안의 원판) | 선택 | 예제 2 |
| Figure 6 | $C_1$에서 양의 순환, $C_2$에서 음의 순환 — $\mathbf v$와 $\mathbf T$의 각도 | **필수** | 10 |
| Figure 7 | 유체 속 작은 물레방아와 $\operatorname{curl}\mathbf v$ 축 | **필수** | 10 |

## D. ERRATA·판독 불확실

- pdftotext 인코딩 왜곡으로 식 (4)에서 $\pi$ 가 탈락해 `lim 1/a²` 로 보이지만, 원문(PNG p-1274)은 $\displaystyle\operatorname{curl}\mathbf v(P_0)\cdot\mathbf n(P_0)=\lim_{a\to0}\frac{1}{\pi a^2}\int_{C_a}\mathbf v\cdot d\mathbf r$ 이다. **$\pi a^2$ 확인 완료**.
- 예제 1의 벡터장은 $\mathbf F=-y^2\,\mathbf i+x\,\mathbf j+z^2\,\mathbf k$ (텍스트의 `2y 2 i` 는 $-y^2\mathbf i$). PNG p-1272에서 확인.
- §16.8 증명에서 곡면은 $z=g(x,y)$ (pdftotext의 `t`는 $g$). PNG p-1271에서 확인.
- 그 외 판독 불확실 없음. PLAN.md의 예제 수(2)는 정확.

## E. 절 요약 (사이트 도입 note 초안)

스토크스 정리는 그린 정리를 공간으로 끌어올린 것이다. 유향곡면 $S$와 그 경계곡선 $C$가 오른손 법칙(법선 $\mathbf n$ 방향으로 서서 걸을 때 곡면이 왼쪽)으로 짝지어질 때, $\int_C\mathbf F\cdot d\mathbf r=\iint_S\operatorname{curl}\mathbf F\cdot d\mathbf S$ 가 성립한다. 말로 하면 "경계에서 접선성분의 선적분 = 곡면에서 회전의 법선성분의 곡면적분"이며, 좌변은 경계 값만, 우변은 도함수를 쓰므로 미적분학의 기본정리와 같은 골격이다. 곡면이 $xy$-평면 안에 평평하게 놓이면 그대로 그린 정리가 되고, 증명도 $S$가 그래프인 경우 16.7.10과 그린 정리, 연쇄법칙만으로 얻어진다. 실전에서 가장 유용한 성질은 **경계곡선만 같으면 어떤 곡면을 써도 값이 같다**는 것(식 (3))이어서, 계산하기 쉬운 곡면으로 갈아타면 된다. 마지막으로 $\operatorname{curl}\mathbf v\cdot\mathbf n=\lim_{a\to0}\frac{1}{\pi a^2}\int_{C_a}\mathbf v\cdot d\mathbf r$ 은 회전벡터가 **단위넓이당 순환**임을 알려주며, 물레방아는 축을 $\operatorname{curl}\mathbf v$ 에 맞출 때 가장 빨리 돈다.

## F. 공통과제 문항 (4차 공통과제)

- **과제 제출 문항**: 4, 9, 13, 14, 22
- **학습 참고 문항**: 1~6, 7~14, 15-(a), 16-(a), 17~24
