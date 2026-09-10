# §16.3 The Fundamental Theorem for Line Integrals — PDF p.1219–1228 (인쇄 p.1182–1191; 본문 p.1219–1226, 연습문제 p.1226–1228)

## A. 카드 인벤토리 (원문 순서)
| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입) | 미적분학 기본정리의 선적분판 / From the FTC to Line Integrals | §4.3의 미적분학 기본정리 제2부 (1) $\displaystyle\int_a^b F'(x)\,dx=F(b)-F(a)$ — 도함수의 정적분은 **끝점의 값만으로** 결정된다. 기울기 $\nabla f$를 $f$의 도함수로 보면 선적분에도 같은 결과가 성립 | 1219 | — | — |
| 2 | thm | Theorem 2 | 선적분의 기본정리 / The Fundamental Theorem for Line Integrals | $C$가 $\mathbf r(t),\ a\le t\le b$인 매끄러운 곡선이고 $f$가 미분가능하며 $\nabla f$가 $C$ 위에서 연속이면 $$\int_C\nabla f\cdot d\mathbf r=f(\mathbf r(b))-f(\mathbf r(a))$$ | 1219 | 본문(연쇄법칙 + FTC (1)) | Fig 1 |
| 3 | rem | NOTE 1 / NOTE 2 / NOTE 3 | 정리 2 읽는 법 / Reading Theorem 2 | **NOTE 1** 보존장(퍼텐셜 $f$의 기울기장)의 선적분은 $f$의 **순변화**: 평면 $A(x_1,y_1)\to B(x_2,y_2)$이면 $\int_C\nabla f\cdot d\mathbf r=f(x_2,y_2)-f(x_1,y_1)$, 공간이면 $f(x_2,y_2,z_2)-f(x_1,y_1,z_1)$. **NOTE 2** 시점·종점이 같은 두 매끄러운 곡선 $C_1,C_2$에 대해 $\int_{C_1}\nabla f\cdot d\mathbf r=\int_{C_2}\nabla f\cdot d\mathbf r$. **NOTE 3** 조각마다 매끄러운 곡선에서도 성립(조각으로 나눠 더하면 됨) | 1219–1220 | — | — |
| 4 | note | ■ Independence of Path (도입) | 경로 무관성과 닫힌 곡선 / Independence of Path; Closed Curves | 일반적으로 $\int_{C_1}\mathbf F\cdot d\mathbf r\neq\int_{C_2}\mathbf F\cdot d\mathbf r$(예제 16.2.4). 정의역 $D$의 시점·종점이 같은 임의의 두 **경로**(조각마다 매끄러운 곡선)에 대해 값이 같으면 $\int_C\mathbf F\cdot d\mathbf r$가 **경로에 무관**하다고 한다 — 보존장의 선적분은 경로에 무관. $\mathbf r(b)=\mathbf r(a)$이면 **닫힌 곡선** | 1220–1221 | — | Fig 2, 3 |
| 5 | thm | Theorem 3 | 경로 무관 ⟺ 닫힌 경로에서 0 / Path Independence vs. Closed Paths | $\displaystyle\int_C\mathbf F\cdot d\mathbf r$가 $D$에서 경로에 무관 $\iff$ $D$ 안의 **모든 닫힌 경로** $C$에 대해 $\displaystyle\int_C\mathbf F\cdot d\mathbf r=0$ | 1221 | 본문 ($C=C_1\cup(-C_2)$ 분해, 양방향) | Fig 4 |
| 6 | rem | (물리 해석) | 보존력이 닫힌 경로에서 하는 일 / Work Around a Closed Path | 보존적 힘장(중력장·전기장 등)이 물체를 닫힌 경로를 따라 옮길 때 하는 일은 $0$ | 1221 | — | — |
| 7 | def | (본문 정의 단락) | 열린 영역·연결 영역 / Open and Connected Regions | $D$가 **열린 영역**: 모든 점 $P\in D$에 대해 $P$를 중심으로 하고 $D$에 완전히 포함되는 원판이 존재(경계점을 포함하지 않음). $D$가 **연결 영역**: $D$의 임의의 두 점을 $D$ 안의 경로로 이을 수 있음 | 1221 | — | — |
| 8 | thm | Theorem 4 | 경로 무관이면 보존장 / Path-Independent $\Rightarrow$ Conservative | $\mathbf F$가 열린 연결 영역 $D$에서 연속이고 $\int_C\mathbf F\cdot d\mathbf r$가 $D$에서 경로에 무관하면 $\mathbf F$는 $D$에서 보존적이다 — 즉 $\nabla f=\mathbf F$인 $f$가 존재 | 1221–1222 | 본문 ($f(x,y)=\int_{(a,b)}^{(x,y)}\mathbf F\cdot d\mathbf r$로 두고 수평·수직 선분 + FTC 제1부로 $f_x=P,\ f_y=Q$) | Fig 5, 6 |
| 9 | note | ■ Conservative Vector Fields and Potential Functions (도입) | 보존장 판정과 퍼텐셜 찾기 / Testing for Conservativeness | 두 물음: (i) $\mathbf F$가 보존적인지 어떻게 아는가? (ii) 보존적이면 퍼텐셜 $f$를 어떻게 찾는가? $\mathbf F=\nabla f$이면 $P=f_x,\ Q=f_y$이고 클레로 정리로 $\dfrac{\partial P}{\partial y}=f_{yx}=f_{xy}=\dfrac{\partial Q}{\partial x}$ | 1222 | — | — |
| 10 | thm | Theorem 5 | 보존장의 필요조건 / Necessary Condition | $\mathbf F(x,y)=P(x,y)\mathbf i+Q(x,y)\mathbf j$가 보존적이고 $P,Q$가 정의역 $D$에서 연속인 1계 편도함수를 가지면 $D$ 전체에서 $\dfrac{\partial P}{\partial y}=\dfrac{\partial Q}{\partial x}$ | 1222 | 본문(클레로 정리) | — |
| 11 | def | (본문 정의, Figure 7) | 단순곡선 / Simple Curve | 끝점 사이에서 자기 자신과 만나지 않는 곡선. 단순닫힌곡선은 $\mathbf r(a)=\mathbf r(b)$이지만 $a<t_1<t_2<b$에 대해 $\mathbf r(t_1)\neq\mathbf r(t_2)$ | 1222 | — | Fig 7 |
| 12 | def | (본문 정의, Figure 8) | 단순연결 영역 / Simply-Connected Region | 평면의 연결 영역 $D$ 중, $D$ 안의 모든 단순닫힌곡선이 $D$의 점들만을 둘러싸는 영역. 직관적으로 **구멍이 없고** 서로 떨어진 두 조각으로 이루어지지 않은 영역 | 1223 | — | Fig 8 |
| 13 | thm | Theorem 6 | 보존장 판정법(평면) / Test for Conservative Fields in the Plane | $\mathbf F=P\mathbf i+Q\mathbf j$가 열린 **단순연결** 영역 $D$ 위의 벡터장이고 $P,Q$가 연속인 1계 편도함수를 가지며 $D$ 전체에서 $\dfrac{\partial P}{\partial y}=\dfrac{\partial Q}{\partial x}$이면 $\mathbf F$는 보존적 | 1223 | §16.4 그린 정리의 따름결과로 개략 증명 | — |
| 14 | rem | ("partial integration" 절차) | 퍼텐셜 함수 구하는 절차 / Finding a Potential by Partial Integration | $f_x=P$를 $x$에 대해 적분하면 적분상수가 $y$의 함수 $g(y)$가 된다 $\Rightarrow$ $y$로 미분해 $f_y=Q$와 비교하여 $g'(y)$를 얻고 다시 적분. 3변수는 $f_x=P$ → $g(y,z)$ → $f_y=Q$로 $g_y$ 결정 → $h(z)$ → $f_z=R$로 $h'(z)$ 결정 | 1223–1225 | — | — |
| 15 | note | ■ Conservation of Energy + (15), (16) | 에너지 보존 법칙 / The Law of Conservation of Energy | 뉴턴 제2법칙 $\mathbf F(\mathbf r(t))=m\mathbf r''(t)$에서 $W=\int_C\mathbf F\cdot d\mathbf r=\dfrac m2\displaystyle\int_a^b\frac{d}{dt}\lvert\mathbf r'(t)\rvert^2dt$이므로 (15) $W=\tfrac12m\lvert\mathbf v(b)\rvert^2-\tfrac12m\lvert\mathbf v(a)\rvert^2$, 즉 (16) $W=K(B)-K(A)$ (운동에너지 $K=\tfrac12m\lvert\mathbf v\rvert^2$의 변화). $\mathbf F$가 보존적이면 퍼텐셜 에너지 $P=-f$로 두어 $\mathbf F=-\nabla P$이고 $W=P(A)-P(B)$이므로 $$P(A)+K(A)=P(B)+K(B)$$ — **에너지 보존 법칙**. 벡터장을 "보존적(conservative)"이라 부르는 이유 | 1225–1226 | 본문(정리 13.2.3 공식 4 + FTC + 정리 2) | — |
| 16 | fig | Figure 7 | 곡선의 종류 / Types of Curves | 단순·비단순 × 닫힘·열림 4가지 곡선 | 1222 | — | 필수 |
| 17 | fig | Figure 8 | 단순연결 영역 / Simply-Connected Regions | 단순연결 영역 1개와 단순연결이 아닌 영역 2개(구멍 있음, 두 조각) | 1223 | — | 필수 |

## B. 예제 기준값
| Example | PDF 쪽 | 유형 | 문제 요지 (영어 재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1220 | 계산 (응용) | Use the Fundamental Theorem to find the work the gravitational field $\mathbf F(\mathbf x)=-\dfrac{mMG}{\lvert\mathbf x\rvert^{3}}\mathbf x$ does in moving a mass $m$ from $(3,4,12)$ to $(2,2,0)$ along any piecewise-smooth path. | $W=f(2,2,0)-f(3,4,12)=\dfrac{mMG}{\sqrt8}-\dfrac{mMG}{13}=mMG\Bigl(\dfrac{1}{2\sqrt2}-\dfrac1{13}\Bigr)$ | sympy: $\dfrac{mMG(13\sqrt2-4)}{52}$ (= 같은 값, 계수 $\approx0.27663$) | ✔ | 퍼텐셜 $f=\dfrac{mMG}{\sqrt{x^2+y^2+z^2}}$ (§16.1 예제 4) |
| 2 | 1223 | 개념 (판정) | Decide whether each planar field is conservative: (a) $\mathbf F=(x-y)\mathbf i+(x-2)\mathbf j$; (b) $\mathbf F=(3+2xy)\mathbf i+(x^{2}-3y^{2})\mathbf j$. | (a) $\partial P/\partial y=-1\neq1=\partial Q/\partial x$이므로 정리 5에 의해 **보존적이 아님**; (b) $\partial P/\partial y=2x=\partial Q/\partial x$이고 정의역이 $\mathbb R^2$(열린 단순연결)이므로 정리 6에 의해 **보존적** | sympy: (a) $(-1,\,1)$ 불일치; (b) $(2x,\,2x)$ 일치 | ✔ | Fig 9/10의 벡터장 그림과 일치 (닫힌 곡선 위 벡터가 곡선 방향과 대체로 같으면 $\oint>0$) |
| 3 | 1224 | 계산 | Find a potential function $f$ with $\nabla f=\mathbf F$ for $\mathbf F(x,y)=(3+2xy)\mathbf i+(x^{2}-3y^{2})\mathbf j$. | $f(x,y)=3x+x^{2}y-y^{3}+K$ | sympy: $\nabla(3x+x^2y-y^3)=(3+2xy,\;x^2-3y^2)=\mathbf F$ | ✔ | 부분적분법(카드 14) 시연: (7)(8) → (9) $f=3x+x^2y+g(y)$ → (10) $f_y=x^2+g'(y)$ → $g'(y)=-3y^2$ |
| 4 | 1224–1225 | 계산 | Evaluate $\int_C\mathbf F\cdot d\mathbf r$ for $\mathbf F=(3+2xy)\mathbf i+(x^{2}-3y^{2})\mathbf j$ along $\mathbf r(t)=e^{t}\sin t\,\mathbf i+e^{t}\cos t\,\mathbf j,\ 0\le t\le\pi$. | $e^{3\pi}+1$ (풀이 1: 끝점 $\mathbf r(0)=(0,1)$, $\mathbf r(\pi)=(0,-e^{\pi})$에 정리 2 적용, $f(0,-e^\pi)-f(0,1)=e^{3\pi}-(-1)$. 풀이 2: 경로무관성으로 $(0,1)\to(0,-e^{\pi})$인 선분 $C_1$으로 대체) | sympy 3가지 방법 모두 $e^{3\pi}+1$: (i) 정리 2, (ii) 원래 매개변수 $t$로 직접 적분, (iii) 직선 $C_1$ | ✔ | 직접 적분(ii)까지 일치하므로 경로무관성도 수치로 확인됨 |
| 5 | 1225 | 계산 | Find $f$ with $\nabla f=\mathbf F$ for $\mathbf F(x,y,z)=y^{2}\mathbf i+(2xy+e^{3z})\mathbf j+3ye^{3z}\mathbf k$. | $f(x,y,z)=xy^{2}+ye^{3z}+K$ | sympy: $\nabla(xy^2+ye^{3z})=(y^2,\;2xy+e^{3z},\;3ye^{3z})=\mathbf F$ | ✔ | (11)–(14) 단계: $f=xy^2+g(y,z)$ → $g_y=e^{3z}$ → $g=ye^{3z}+h(z)$ → $h'(z)=0$. $\mathbb R^3$의 보존장 판정법은 §16.5 |

## C. 그림 필요 목록 (자체 SVG)
| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 7 | 곡선의 종류 4분류: 단순·닫히지 않음 / 비단순·닫히지 않음 / 단순닫힘 / 비단순닫힘 | 필수 | 16 (카드 11) |
| Figure 8 | 단순연결 영역 vs. 단순연결이 아닌 영역(구멍 있는 영역, 분리된 두 조각) | 필수 | 17 (카드 12) |
| Figure 2 / 4 | 같은 끝점을 갖는 두 경로 $C_1,C_2$; 닫힌 경로를 $C_1$과 $C_2$로 분해 | 선택 | 4, 5 |
| Figure 5 / 6 | 정리 4의 증명 도해: $(a,b)\to(x_1,y)\to(x,y)$ 수평 선분, $(a,b)\to(x,y_1)\to(x,y)$ 수직 선분 | 선택 | 8 |
| Figure 1 | 평면·공간에서 시점 $A$·종점 $B$를 잇는 곡선 $C$ | 선택 | 2 |
| Figure 3 | 닫힌 곡선 | 선택 | 4 |
| Figure 9 / 10 / 11 | 예제 2(a)·2(b)의 벡터장 컴퓨터 플롯, 예제 4의 나선 경로와 대체 선분 | 선택 | 예제 2, 4 |

## D. ERRATA·판독 불확실
- 없음. 교재의 모든 예제 최종답이 sympy 재계산과 일치 (예제 4는 세 가지 방법으로 교차 검증).
- 판독 참고: pdftotext에서 예제 4의 답이 "e  3 2 s21d − e 3 1 1"로 뭉개져 나오지만 $f(0,-e^{\pi})=e^{3\pi}$, $f(0,1)=-1$이므로 $e^{3\pi}+1$이 맞음(재계산으로 확정).

## E. 절 요약 (사이트 도입 note 초안)
기울기장 $\nabla f$의 선적분은 경로 전체가 아니라 **두 끝점에서의 $f$ 값**만으로 결정된다: $\int_C\nabla f\cdot d\mathbf r=f(\mathbf r(b))-f(\mathbf r(a))$. 이것이 선적분판 미적분학 기본정리이며, 보존장의 선적분이 경로에 무관하다는 뜻이다. 경로 무관성은 "모든 닫힌 경로에서 적분이 0"과 동치이고(정리 3), 열린 연결 영역에서는 거꾸로 경로에 무관한 연속 벡터장은 반드시 보존적이다(정리 4). 평면에서 보존성을 실제로 판정할 때는 $\partial P/\partial y=\partial Q/\partial x$를 확인하는데, 이 조건은 항상 필요조건이고(정리 5), 정의역이 **열린 단순연결** 영역이면 충분조건이기도 하다(정리 6). 보존적임을 알면 $f_x=P$를 $x$로 적분한 뒤 $f_y=Q$와 비교하는 부분적분법으로 퍼텐셜 함수를 찾을 수 있다. 마지막으로, 보존적 힘장 아래에서는 운동에너지와 퍼텐셜 에너지의 합이 일정하다는 에너지 보존 법칙이 따라 나오며, 이것이 "보존적"이라는 이름의 유래다.

## F. 공통과제 문항
- 3차 공통과제, 16.3 The Fundamental Theorem for Line Integrals
  - **과제 제출 문항**: 14, 17, 24, 29, 41
  - **학습 참고 문항**: 3~10, 13~15, 17~24, 25~26, 29~30, 36, 41
