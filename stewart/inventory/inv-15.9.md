# §15.9 Change of Variables in Multiple Integrals — PDF p.1184–1192 (인쇄 p.1147–1155)

> 본문은 PDF p.1184 상단에서 시작, 본문·예제 종료 p.1190 하단, 연습문제 p.1191–1192.

## A. 카드 인벤토리 (원문 순서)

| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입) | 1변수 치환적분의 복습 / Review of Substitution | 치환법(4.5.5)에서 $x$와 $u$의 역할을 바꿔 쓰면 (1) $\displaystyle\int_a^b f(x)\,dx=\int_c^d f(g(u))\,g'(u)\,du$ ($x=g(u)$, $a=g(c)$, $b=g(d)$), 또는 (2) $\displaystyle\int_a^b f(x)\,dx=\int_c^d f(x(u))\,\frac{dx}{du}\,du$. 이중·삼중적분에도 변수변환이 유용하다 | 1184 | — | — |
| 2 | def | Change of Variables in Double Integrals, 식 (3) | 변환 $T$와 상 / Transformation and Image | 이미 본 예: 극좌표 $x=r\cos\theta$, $y=r\sin\theta$. 일반적으로 $uv$-평면에서 $xy$-평면으로 가는 변환 $T(u,v)=(x,y)$, (3) $x=g(u,v)$, $y=h(u,v)$ (또는 $x=x(u,v)$, $y=y(u,v)$). 보통 $g,h$가 연속인 1계 편도함수를 갖는 **$C^1$ 변환**을 가정. $T(u_1,v_1)=(x_1,y_1)$이면 $(x_1,y_1)$은 $(u_1,v_1)$의 **상(image)**; 서로 다른 두 점의 상이 다르면 **일대일**이고 역변환 $T^{-1}$이 있어 $u=G(x,y)$, $v=H(x,y)$로 풀 수 있다. $S$의 상 $R=T(S)$ | 1184–1185 | — | Fig 1 |
| 3 | note | (유도) 식 (6) | 상 영역의 평행사변형 근사 / Approximating the Image by a Parallelogram | 작은 직사각형 $S$(왼쪽 아래 $(u_0,v_0)$, 변 $\Delta u,\Delta v$)의 상을, 위치벡터 $\mathbf r(u,v)=g(u,v)\mathbf i+h(u,v)\mathbf j$의 접벡터 $\mathbf r_u=\frac{\partial x}{\partial u}\mathbf i+\frac{\partial y}{\partial u}\mathbf j$, $\mathbf r_v=\frac{\partial x}{\partial v}\mathbf i+\frac{\partial y}{\partial v}\mathbf j$가 정하는 평행사변형으로 근사. §12.4에 의해 넓이는 (6) $|(\Delta u\,\mathbf r_u)\times(\Delta v\,\mathbf r_v)|=|\mathbf r_u\times\mathbf r_v|\,\Delta u\,\Delta v$ | 1185–1186 | — | Fig 3, 4, 5 |
| 4 | def | Definition 7 | 야코비안 / The Jacobian | (7) $T$($x=g(u,v)$, $y=h(u,v)$)의 야코비안은 $\dfrac{\partial(x,y)}{\partial(u,v)}=\begin{vmatrix}\dfrac{\partial x}{\partial u}&\dfrac{\partial x}{\partial v}\\[4pt]\dfrac{\partial y}{\partial u}&\dfrac{\partial y}{\partial v}\end{vmatrix}=\dfrac{\partial x}{\partial u}\dfrac{\partial y}{\partial v}-\dfrac{\partial x}{\partial v}\dfrac{\partial y}{\partial u}$. (독일 수학자 C. G. J. Jacobi(1804–1851)의 이름. 코시가 먼저 썼으나 야코비가 다중적분 계산법으로 발전시킴) | 1186 | — | — |
| 5 | rem | 식 (8) | 넓이소의 근사 / The Area Element | (8) $\Delta A\approx\left|\dfrac{\partial(x,y)}{\partial(u,v)}\right|\Delta u\,\Delta v$ (야코비안은 $(u_0,v_0)$에서 평가). $\mathbf r_u\times\mathbf r_v$의 $\mathbf k$ 성분이 곧 야코비안이라는 계산에서 나옴 | 1186 | 본문 | — |
| 6 | thm | Theorem 9 (Change of Variables in a Double Integral) | 이중적분의 변수변환 정리 / Change of Variables in a Double Integral | $T$가 야코비안이 $0$이 아닌 $C^1$ 변환이고 $uv$-평면의 영역 $S$를 $xy$-평면의 영역 $R$ 위로 보내며, $f$가 $R$에서 연속, $R$과 $S$가 평면 제I형 또는 제II형이고, $T$가 ($S$의 경계는 예외로 두고) 일대일이면 (9) $\displaystyle\iint_R f(x,y)\,dA=\iint_S f\big(x(u,v),y(u,v)\big)\left|\frac{\partial(x,y)}{\partial(u,v)}\right|du\,dv$ | 1187 | 직관적 논증만 본문(부분직사각형 $S_{ij}$의 상 $R_{ij}$에 (8) 적용 → 리만 합); 완전한 증명은 고등미적분학 교재 | Fig 6 |
| 7 | rem | Theorem 9 뒤 단락 | $dA$ 교체 규칙과 1변수와의 유비 / Replacing $dA$ | 정리 9는 $x,y$를 $u,v$로 나타내고 $dA=\left|\dfrac{\partial(x,y)}{\partial(u,v)}\right|du\,dv$로 바꾸라는 뜻. 1변수 공식 (2)와 나란한데, 도함수 $dx/du$ 자리에 **야코비안의 절댓값**이 들어간다 | 1187 | — | — |
| 8 | rem | Figure 7 옆 단락 | 극좌표는 정리 9의 특수 경우 / Polar Coordinates as a Special Case | $T(r,\theta)=(r\cos\theta,\ r\sin\theta)$는 $r\theta$-평면의 보통 직사각형을 $xy$-평면의 극직사각형으로 보낸다. $\dfrac{\partial(x,y)}{\partial(r,\theta)}=\begin{vmatrix}\cos\theta&-r\sin\theta\\ \sin\theta&r\cos\theta\end{vmatrix}=r\cos^2\theta+r\sin^2\theta=r>0$이므로 정리 9가 공식 15.3.2를 그대로 준다 | 1188 | 본문 | Fig 7 |
| 9 | rem | Example 2 뒤 NOTE | 변환을 고르는 요령 / Choosing a Transformation | 변환이 주어지지 않으면 먼저 적절한 변수변환을 생각해야 한다. **$f(x,y)$가 적분하기 어려우면 $f$의 꼴이** 변환을 시사하고(예제 3의 $u=x+y$, $v=x-y$), **적분 영역 $R$이 까다로우면** 대응하는 $S$가 간단히 기술되도록 변환을 고른다 | 1188–1189 | — | — |
| 10 | def | 식 (12) | 3변수 야코비안 / The $3\times3$ Jacobian | $x=g(u,v,w)$, $y=h(u,v,w)$, $z=k(u,v,w)$인 변환의 야코비안은 (12) $\dfrac{\partial(x,y,z)}{\partial(u,v,w)}=\begin{vmatrix}x_u&x_v&x_w\\ y_u&y_v&y_w\\ z_u&z_v&z_w\end{vmatrix}$ | 1190 | — | — |
| 11 | thm | 식 (13) | 삼중적분의 변수변환 / Change of Variables in a Triple Integral | 정리 9와 비슷한 가정 아래 (13) $\displaystyle\iiint_R f(x,y,z)\,dV=\iiint_S f\big(x(u,v,w),y(u,v,w),z(u,v,w)\big)\left|\frac{\partial(x,y,z)}{\partial(u,v,w)}\right|du\,dv\,dw$ | 1190 | 정리 9와 같은 방식(본문에서 언급) | — |
| 12 | fig | Figure 5 & 6 | 평행사변형 근사와 격자의 대응 / Parallelogram Approximation and the Grid | $\Delta u\,\mathbf r_u$, $\Delta v\,\mathbf r_v$가 정하는 평행사변형 / $uv$-평면의 격자 $S_{ij}$와 $xy$-평면의 상 $R_{ij}$ — 야코비안이 "넓이 확대율"임을 보여 주므로 필수 | 1186–1187 | — | — |

카드 수: note 2, def 3, thm 2, rem 4, fig 1 = **12**

## B. 예제 기준값

| Example | PDF 쪽 | 유형 | 문제 요지 (영어 재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1185 | 계산·스케치 | For the transformation $x=u^2-v^2$, $y=2uv$, determine the image of the unit square $S=[0,1]\times[0,1]$. | 그래프형 — 서술 답: $x$축과 두 포물선 (4) $x=1-\dfrac{y^2}{4}\ (0\le x\le1)$, (5) $x=\dfrac{y^2}{4}-1\ (-1\le x\le0)$로 둘러싸인 영역 $R$ (꼭짓점 $(-1,0),(1,0),(0,2)$) | 네 변의 상을 각각 확인: $v=0\Rightarrow(u^2,0)$ ⇒ $0\le x\le1,\ y=0$; $u=1\Rightarrow x-\left(1-\tfrac{y^2}4\right)=0$; $v=1\Rightarrow x-\left(\tfrac{y^2}4-1\right)=0$; $u=0\Rightarrow(-v^2,0)$ ⇒ $-1\le x\le0,\ y=0$ (sympy, 잔차 모두 $0$) | ✔ | $S$의 경계를 반시계 방향으로 돌면 $R$의 경계도 반시계 방향 |
| 2 | 1188 | 계산 | Use $x=u^2-v^2$, $y=2uv$ to evaluate $\iint_R y\,dA$, where $R$ is bounded by the $x$-axis and the parabolas $y^2=4-4x$, $y^2=4+4x$ with $y\ge0$. | $2$ | $\dfrac{\partial(x,y)}{\partial(u,v)}=\begin{vmatrix}2u&-2v\\2v&2u\end{vmatrix}=4u^2+4v^2>0$; $\int_0^1\!\int_0^1 2uv\,(4u^2+4v^2)\,du\,dv=2$; $xy$-평면 직접 계산 $\int_0^2\!\int_{y^2/4-1}^{1-y^2/4}y\,dx\,dy=2$ (sympy, 두 방법) | ✔ | $R$은 예제 1의 상 $T(S)$ — $S$가 훨씬 단순하다는 것이 변환의 이유 |
| 3 | 1189 | 계산 | Evaluate $\iint_R e^{(x+y)/(x-y)}\,dA$, where $R$ is the trapezoid with vertices $(1,0),(2,0),(0,-2),(0,-1)$. | $\dfrac34\left(e-e^{-1}\right)$ | (10) $u=x+y$, $v=x-y$ ⇒ (11) $x=\tfrac12(u+v)$, $y=\tfrac12(u-v)$; 야코비안 $=-\tfrac12$; $S=\{1\le v\le2,\ -v\le u\le v\}$; $\int_1^2\!\int_{-v}^{v}e^{u/v}\cdot\tfrac12\,du\,dv=\tfrac32\sinh1=\tfrac34(e-e^{-1})\approx1.7628018$; $xy$-평면 수치 적분 $1.762801$ (sympy + python) | ✔ | $R$의 네 변 $y=0,\ x-y=2,\ x=0,\ x-y=1$이 $uv$-평면에서 $u=v,\ v=2,\ u=-v,\ v=1$로 감. sympy는 $\tfrac32\sinh1$로 내놓으며 교재 표현과 기호적으로 동치 |
| 4 | 1190 | 증명 (유도) | Use Formula (13) to derive the spherical-coordinate triple integration formula. | $\dfrac{\partial(x,y,z)}{\partial(\rho,\theta,\phi)}=-\rho^2\sin\phi$이고 $0\le\phi\le\pi$에서 $\sin\phi\ge0$이므로 $\left|\dfrac{\partial(x,y,z)}{\partial(\rho,\theta,\phi)}\right|=\rho^2\sin\phi$ ⇒ 공식 15.8.3 | $3\times3$ 행렬식을 sympy로 계산: $-\rho^2\sin\phi$ (교재와 일치) | ✔ | 부록: 극좌표 야코비안도 재계산 — $\dfrac{\partial(x,y)}{\partial(r,\theta)}=r$ (본문 p.1188과 일치) |

예제 수: **4** (계산 2, 계산·스케치 1, 증명(유도) 1)

## C. 그림 필요 목록 (자체 SVG)

| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 1 | $T$가 $uv$-평면의 $S$를 $xy$-평면의 $R$로 보냄, $T^{-1}$ 화살표 | **필수** | 2 |
| Figure 2 | 예제 1: 단위정사각형 $S$(변 $S_1\!\sim\!S_4$)와 그 상인 포물선 영역 $R$ | **필수** | 예제 1 |
| Figure 3 | 작은 직사각형 $S$와 그 상 $R$, 곡선 $\mathbf r(u,v_0)$, $\mathbf r(u_0,v)$ | 선택 | 3 |
| Figure 4 | 할선벡터 $\mathbf a,\mathbf b$로 만든 근사 평행사변형 | 선택 | 3 |
| Figure 5 | $\Delta u\,\mathbf r_u$, $\Delta v\,\mathbf r_v$가 정하는 평행사변형 | **필수** | 12 (=3) |
| Figure 6 | $uv$-평면의 격자 $S_{ij}$ ↔ $xy$-평면의 상 $R_{ij}$ | **필수** | 12 (=6) |
| Figure 7 | 극좌표 변환: $r\theta$-평면 직사각형 → $xy$-평면 극직사각형 | **필수** | 8 |
| Figure 8 | 예제 2의 영역 $R$ (두 포물선과 $x$축) | 선택(Fig 2와 중복) | 예제 2 |
| Figure 9 | 예제 3: $xy$-평면 사다리꼴 $R$ ↔ $uv$-평면 사다리꼴 $S$ (꼭짓점 $(1,1),(2,2),(-2,2),(-1,1)$) | **필수** | 예제 3 |

## D. ERRATA·판독 불확실
- 없음. 네 예제 모두 sympy 재계산과 일치.
- 예제 3에서 sympy는 $\tfrac32\sinh 1$을 내놓는데 이는 교재의 $\tfrac34(e-e^{-1})$과 기호적으로 동치임을 확인함(수치 $1.7628018$, 그리고 $xy$-평면 직접 수치 적분도 $1.762801$).
- pdftotext에서 (12)의 $3\times3$ 행렬식이 "7 7"처럼 깨져 나옴 — 문맥과 (13), 예제 4의 계산으로 복원.
- 야코비안의 **절댓값**을 취한다는 점(예제 3에서 $J=-\tfrac12$)이 이 절에서 가장 자주 놓치는 부분이므로 카드 6·7에서 강조할 것.

## E. 절 요약 (사이트 도입 note 초안)
1변수 적분에서 치환 $x=g(u)$가 $dx=g'(u)\,du$를 만들었듯, 다중적분에서도 변환 $T(u,v)=(x,y)$가 $dA$를 바꾼다. 작은 직사각형의 상은 접벡터 $\mathbf r_u,\mathbf r_v$가 만드는 평행사변형으로 근사되고, 그 넓이가 $\left|\frac{\partial(x,y)}{\partial(u,v)}\right|\Delta u\,\Delta v$이므로 **야코비안의 절댓값이 곧 넓이 확대율**이다. 이것이 변수변환 정리 $\iint_R f\,dA=\iint_S f\left|\frac{\partial(x,y)}{\partial(u,v)}\right|du\,dv$이며, §15.3의 $dA=r\,dr\,d\theta$와 §15.8의 $dV=\rho^2\sin\phi\,d\rho\,d\theta\,d\phi$는 모두 이 정리의 특수 경우다. 변환이 주어지지 않을 때는 피적분함수의 꼴(예: $e^{(x+y)/(x-y)}$ ⇒ $u=x+y,\ v=x-y$)이나 적분 영역의 모양이 무엇을 새 변수로 삼을지 알려 준다.

## F. 공통과제 문항 (3차 공통과제)
- **과제 제출 문항**: 19, 21, 26, 27, 29, 31
- **학습 참고 문항**: 7~10, 11~16, 17~22, 23(a), 25~30, 31
