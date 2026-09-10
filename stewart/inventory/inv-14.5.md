# §14.5 The Chain Rule — PDF p.1060–1068 (인쇄 p.1023–1031)

본문 PDF p.1060–1066(인쇄 1023–1029), 연습문제 PDF p.1066–1069(인쇄 1029–1032).

## A. 카드 인벤토리 (원문 순서)

| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입) | 연쇄법칙의 확장 / Extending the Chain Rule | 1변수 연쇄법칙 $y=f(x)$, $x=g(t)$ ⟹ $\dfrac{dy}{dt}=\dfrac{dy}{dx}\dfrac{dx}{dt}$를 다변수로 확장한다. 다변수에서는 어떤 변수가 어떤 변수의 함수인가에 따라 여러 버전(Case 1 / Case 2 / General)이 생긴다 | 1060 | — | — |
| 2 | thm | Theorem 1 — The Chain Rule (Case 1) | 연쇄법칙 (경우 1) / Chain Rule, Case 1 | $z=f(x,y)$가 미분가능, $x=g(t)$, $y=h(t)$가 미분가능이면 $z$는 $t$의 미분가능한 함수이고 $\dfrac{dz}{dt}=\dfrac{\partial f}{\partial x}\dfrac{dx}{dt}+\dfrac{\partial f}{\partial y}\dfrac{dy}{dt}$ | 1060 | 본문 (Definition 14.4.7의 $\Delta z=f_x\Delta x+f_y\Delta y+\varepsilon_1\Delta x+\varepsilon_2\Delta y$를 $\Delta t$로 나누고 $\Delta t\to0$) | — |
| 3 | rem | 여백 노트 | 전미분과의 형태적 유사 / Resemblance to the Differential | $\partial z/\partial x$ 표기로 쓰면 $\dfrac{dz}{dt}=\dfrac{\partial z}{\partial x}\dfrac{dx}{dt}+\dfrac{\partial z}{\partial y}\dfrac{dy}{dt}$로, 전미분 $dz=\dfrac{\partial z}{\partial x}dx+\dfrac{\partial z}{\partial y}dy$와 형태가 같다 | 1061 | — | — |
| 4 | thm | Theorem 2 — The Chain Rule (Case 2) | 연쇄법칙 (경우 2) / Chain Rule, Case 2 | $z=f(x,y)$ 미분가능, $x=g(s,t)$, $y=h(s,t)$ 미분가능이면 $\dfrac{\partial z}{\partial s}=\dfrac{\partial z}{\partial x}\dfrac{\partial x}{\partial s}+\dfrac{\partial z}{\partial y}\dfrac{\partial y}{\partial s}$, $\dfrac{\partial z}{\partial t}=\dfrac{\partial z}{\partial x}\dfrac{\partial x}{\partial t}+\dfrac{\partial z}{\partial y}\dfrac{\partial y}{\partial t}$ | 1062 | 본문 ($s$를 고정하고 Theorem 1 적용) | — |
| 5 | rem | 변수 분류 + 수형도 규칙 | 독립·중간·종속 변수와 수형도 / Tree Diagrams | $s,t$는 **독립변수**, $x,y$는 **중간변수**, $z$는 **종속변수**. 중간변수마다 항이 하나씩 생긴다. 수형도에서 $z$부터 목표 독립변수까지의 **각 경로를 따라 편도함수를 곱하고, 모든 경로를 더한다** | 1062–1063 | — | Fig 2 |
| 6 | thm | Theorem 3 — The Chain Rule (General Version) | 연쇄법칙 (일반형) / Chain Rule, General Version | $u$가 $x_1,\dots,x_n$의 미분가능 함수이고 각 $x_j$가 $t_1,\dots,t_m$의 미분가능 함수이면 각 $i=1,\dots,m$에 대해 $\dfrac{\partial u}{\partial t_i}=\dfrac{\partial u}{\partial x_1}\dfrac{\partial x_1}{\partial t_i}+\cdots+\dfrac{\partial u}{\partial x_n}\dfrac{\partial x_n}{\partial t_i}$ (중간변수 개수 $n$만큼의 항) | 1063 | Case 1과 유사(생략) | Fig 3 |
| 7 | note | ■ Implicit Differentiation | 음함수 미분: 2변수 / Implicit Differentiation, $F(x,y)=0$ | $F(x,y)=0$이 $y=f(x)$를 음함수로 정의한다고 보고 Case 1을 적용하면 $F_x\cdot1+F_y\dfrac{dy}{dx}=0$. $F_y\neq0$이면 $(5)$ $\dfrac{dy}{dx}=-\dfrac{\partial F/\partial x}{\partial F/\partial y}=-\dfrac{F_x}{F_y}$ | 1065 | 본문 | — |
| 8 | rem | Implicit Function Theorem (2변수) | 음함수 정리 / Implicit Function Theorem | $F$가 $(a,b)$를 포함하는 원판에서 정의되고 $F(a,b)=0$, $F_y(a,b)\neq0$, $F_x,F_y$가 그 원판에서 연속이면, $F(x,y)=0$은 $(a,b)$ 근방에서 $y$를 $x$의 함수로 정의하고 그 도함수는 $(5)$로 주어진다 (고급 미적분학에서 증명) | 1065 | 인용만 | — |
| 9 | thm | Equations (6) | 음함수 미분: 3변수 / Implicit Differentiation, $F(x,y,z)=0$ | $F(x,y,z)=0$이 $z=f(x,y)$를 정의하고 $F_z\neq0$이면 $(6)$ $\dfrac{\partial z}{\partial x}=-\dfrac{F_x}{F_z}$, $\dfrac{\partial z}{\partial y}=-\dfrac{F_y}{F_z}$ | 1066 | 본문 | — |
| 10 | rem | Implicit Function Theorem (3변수) | 음함수 정리 (3변수판) / Implicit Function Theorem, 3 Variables | $F$가 $(a,b,c)$를 포함하는 구 안에서 정의되고 $F(a,b,c)=0$, $F_z(a,b,c)\neq0$, $F_x,F_y,F_z$가 연속이면 $F(x,y,z)=0$은 $(a,b,c)$ 근방에서 $z$를 $x,y$의 미분가능 함수로 정의하고 편도함수는 $(6)$ | 1066 | 인용만 | — |
| 11 | fig | Figure 2 | 수형도 (Case 2) / Tree Diagram for Case 2 | $z\to x,y\to s,t$의 가지에 각 편도함수를 붙인 도식. 연쇄법칙 암기의 핵심 도구 | 1062 | — | 필수 |

카드 수: note 2, def 0, thm 4, rem 4, fig 1 — 합계 **11개**(fig 제외 시 10개).

## B. 예제 기준값

| Example | PDF 쪽 | 유형 | 문제 요지 (재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1061 | 계산 | With $z=x^2y+3xy^4$, $x=\sin 2t$, $y=\cos t$, evaluate $dz/dt$ at $t=0$. | $\dfrac{dz}{dt}=(2xy+3y^4)(2\cos 2t)+(x^2+12xy^3)(-\sin t)$; at $t=0$, $x=0,y=1$ ⟹ $\dfrac{dz}{dt}\Big|_{t=0}=6$ | sympy: 연쇄법칙 결과와 직접대입 미분이 항등적으로 일치, $t=0$에서 값 $=6$ | ✔ | 곡선 $C:(\sin2t,\cos t)$ 위에서 $z$의 변화율로 해석 (Fig 1) |
| 2 | 1061–1062 | 해석·응용 | For one mole of ideal gas $PV=8.31T$, find $dP/dt$ when $T=300$ K, $dT/dt=0.1$ K/s, $V=100$ L, $dV/dt=0.2$ L/s. | $\dfrac{dP}{dt}=\dfrac{8.31}{V}\dfrac{dT}{dt}-\dfrac{8.31T}{V^2}\dfrac{dV}{dt}=-0.04155$ ⟹ 압력이 약 $0.042$ kPa/s로 **감소** | sympy: $\dfrac{dP}{dt}=-\dfrac{831}{20000}=-0.04155$ | ✔ | — |
| 3 | 1062 | 계산 | For $z=e^{x}\sin y$ with $x=st^2$, $y=s^2t$, find $\partial z/\partial s$ and $\partial z/\partial t$. | $\dfrac{\partial z}{\partial s}=t^2e^{st^2}\sin(s^2t)+2ste^{st^2}\cos(s^2t)$; $\dfrac{\partial z}{\partial t}=2ste^{st^2}\sin(s^2t)+s^2e^{st^2}\cos(s^2t)$ | sympy: $z_s=te^{st^2}\big(2s\cos(s^2t)+t\sin(s^2t)\big)$, $z_t=se^{st^2}\big(s\cos(s^2t)+2t\sin(s^2t)\big)$ — 교재 식과 항등적으로 동일하며 직접 미분과도 일치 | ✔ | — |
| 4 | 1063 | 개념 | Write out the Chain Rule when $w=f(x,y,z,t)$ and $x,y,z,t$ are each functions of $u,v$. | $\dfrac{\partial w}{\partial u}=\dfrac{\partial w}{\partial x}\dfrac{\partial x}{\partial u}+\dfrac{\partial w}{\partial y}\dfrac{\partial y}{\partial u}+\dfrac{\partial w}{\partial z}\dfrac{\partial z}{\partial u}+\dfrac{\partial w}{\partial t}\dfrac{\partial t}{\partial u}$, $v$에 대해서도 동일 | 개념형 — 재계산 대상 아님 ($n=4$, $m=2$인 Theorem 3의 직접 적용) | — | 수형도 Fig 3 |
| 5 | 1063 | 계산 | With $u=x^4y+y^2z^3$, $x=rse^{t}$, $y=rs^2e^{-t}$, $z=r^2s\sin t$, find $\partial u/\partial s$ at $(r,s,t)=(2,1,0)$. | $(r,s,t)=(2,1,0)$에서 $x=2,y=2,z=0$; $\dfrac{\partial u}{\partial s}=(64)(2)+(16)(4)+(0)(0)=192$ | sympy: $x,y,z=2,2,0$; 연쇄법칙 $=192$, 직접대입 미분도 $192$ | ✔ | — |
| 6 | 1064 | 증명(show) | If $g(s,t)=f(s^2-t^2,\;t^2-s^2)$ with $f$ differentiable, show $t\,g_s+s\,g_t=0$. | $g_s=2s f_x-2s f_y$, $g_t=-2t f_x+2t f_y$ ⟹ $t\,g_s+s\,g_t=(2st f_x-2st f_y)+(-2st f_x+2st f_y)=0$ | sympy (추상 `Function`): $t\,g_s+s\,g_t$가 항등적으로 $0$ | ✔ | — |
| 7 | 1064 | 계산 | If $z=f(x,y)$ has continuous second-order partials and $x=r^2+s^2$, $y=2rs$, find (a) $\partial z/\partial r$; (b) $\partial^2 z/\partial r^2$. | (a) $\dfrac{\partial z}{\partial r}=2r\dfrac{\partial z}{\partial x}+2s\dfrac{\partial z}{\partial y}$; (b) $\dfrac{\partial^2z}{\partial r^2}=2\dfrac{\partial z}{\partial x}+4r^2\dfrac{\partial^2z}{\partial x^2}+8rs\dfrac{\partial^2z}{\partial x\partial y}+4s^2\dfrac{\partial^2z}{\partial y^2}$ | sympy: (a) 동일. (b) 추상 `Subs` 객체는 구조 비교가 안 되므로 구체적인 $f$ 세 개($e^x\sin y+x^3y^2$, $\ln(1+x^2+y^2)$, $x^2y-\cos xy$)로 항등식 검증 → 모두 일치 | ✔ | 혼합 2계 편도함수의 상등(Clairaut)을 쓴다 |
| 8 | 1065 | 계산 | Find $y'$ if $x^3+y^3=6xy$. | $F=x^3+y^3-6xy$, $\dfrac{dy}{dx}=-\dfrac{3x^2-6y}{3y^2-6x}=-\dfrac{x^2-2y}{y^2-2x}$ | sympy: $-F_x/F_y=\dfrac{x^2-2y}{2x-y^2}$ (= 교재 식과 동일), 고전적 음함수 미분과도 일치 | ✔ | §2.6 Example 2와 비교하라는 여백 노트 |
| 9 | 1066 | 계산 | Find $\partial z/\partial x$ and $\partial z/\partial y$ if $x^3+y^3+z^3+6xyz+4=0$. | $\dfrac{\partial z}{\partial x}=-\dfrac{x^2+2yz}{z^2+2xy}$, $\dfrac{\partial z}{\partial y}=-\dfrac{y^2+2xz}{z^2+2xy}$ | sympy: $-F_x/F_z$, $-F_y/F_z$가 각각 교재 식과 항등적으로 일치 | ✔ | §14.3 Example 5와 비교하라는 여백 노트 |

예제 수: **9개** (계산 6, 증명 1, 해석·응용 1, 개념 1).
※ 지시서에는 "예제 9개"로 되어 있고 실제로도 9개다(Example 1–9).

## C. 그림 필요 목록 (자체 SVG)

| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 2 | Case 2 수형도: $z\to x,y\to s,t$, 각 가지에 편도함수 | **필수** | 5 (fig 카드 11) |
| Figure 3 | Example 4 수형도: $w\to x,y,z,t\to u,v$ | 필수 (Example 4 풀이의 핵심) | Ex 4 |
| Figure 4 | Example 5 수형도: $u\to x,y,z\to r,s,t$ | 선택 | Ex 5 |
| Figure 5 | Example 7 수형도: $z_x$(또는 $z_y$)$\to x,y\to r,s$ — 2계 도함수 계산용 | 선택 | Ex 7 |
| Figure 1 | 곡선 $x=\sin 2t$, $y=\cos t$ (Example 1의 경로) | 선택 (2D, 간단) | Ex 1 |

수형도는 모두 노드+간선 구조라 인라인 SVG로 만들기 쉽고, 이 절의 학습 효과 대부분을 담당한다.

## D. ERRATA·판독 불확실

- pdftotext에서 `−`가 `=`, `1`이 `+`, `2`가 `−`, `y`가 `/`, `«`가 $\varepsilon$, `l`이 $\to$로 뒤바뀐다. Theorem 1 증명 중 `1 10 10`은 실제로는 극한 $\varepsilon_1\to0$, $\varepsilon_2\to0$ 자리에 0이 대입된 것.
- Example 7(b) 유도에서 원문의 번호 `4`는 곱의 법칙을 적용한 중간식 $(4)$이며, 카드로 만들 만한 독립 공식이 아니라 예제 내부 식이므로 A 표에서 제외했다.
- 교재 본문의 수학적 오류는 발견하지 못했다. 재계산 9/9 일치(개념형 Example 4 제외 시 8/8).

## E. 절 요약 (사이트 도입 note 초안)

합성함수의 미분법인 연쇄법칙은 다변수에서 "어떤 변수가 어떤 변수의 함수인지"에 따라 여러 모습을 띤다. $z=f(x,y)$이고 $x,y$가 한 변수 $t$의 함수면 $dz/dt=z_x x'(t)+z_y y'(t)$(경우 1), $x,y$가 두 변수 $s,t$의 함수면 $s,t$ 각각에 대해 같은 꼴의 편도함수 공식이 성립한다(경우 2). 일반형은 중간변수 하나마다 항이 하나씩 생기는 규칙으로 요약되며, **수형도**에서 종속변수로부터 독립변수까지의 각 경로를 따라 편도함수를 곱하고 모든 경로를 더하면 된다고 외우면 편하다. 이 규칙을 $F(x,y)=0$이나 $F(x,y,z)=0$에 적용하면 음함수 미분 공식 $dy/dx=-F_x/F_y$, $\partial z/\partial x=-F_x/F_z$가 바로 나온다. 이때 그 공식이 실제로 적용 가능한 조건은 음함수 정리가 보장한다.

## F. 공통과제 문항 (1차 공통과제)

- 과제 제출 문항: **12, 19, 27, 38, 49**
- 학습 참고 문항: **3~8, 11~16, 17~20, 25~30, 31~34, 35~38, 49~50, 51~55**
