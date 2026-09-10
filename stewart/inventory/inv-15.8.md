# §15.8 Triple Integrals in Spherical Coordinates — PDF p.1177–1183 (인쇄 p.1140–1146)

> 본문은 PDF p.1177 상단에서 시작, 본문·예제 종료 p.1180 하단, 연습문제 p.1181–1183.

## A. 카드 인벤토리 (원문 순서)

| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | def | (절 도입) + Spherical Coordinates | 구면좌표 / Spherical Coordinates | 점 $P$의 구면좌표 $(\rho,\theta,\phi)$: $\rho=|OP|$은 원점에서 $P$까지의 거리, $\theta$는 원기둥좌표에서와 같은 각, $\phi$는 양의 $z$축과 선분 $OP$가 이루는 각. 범위는 $\rho\ge0$, $0\le\phi\le\pi$. 구·원뿔로 둘러싸인 영역의 삼중적분을 간단하게 만든다 | 1177 | — | Fig 1 |
| 2 | rem | Figures 2–4 | 좌표면 / Coordinate Surfaces | $\rho=c$는 원점 중심 반지름 $c$의 **구**(이름의 유래), $\theta=c$는 **수직 반평면**, $\phi=c$는 $z$축을 축으로 하는 **반원뿔**($0<c<\pi/2$이면 위쪽, $\pi/2<c<\pi$이면 아래쪽). 구면좌표는 **한 점에 대한 대칭**이 있는 문제에 유용하며 그 점을 원점으로 잡는다 | 1177 | — | Fig 2, 3, 4 |
| 3 | thm | 식 (1)(2) | 구면좌표와 직교좌표의 변환 / Conversion Formulas | 삼각형 $OPQ$, $OPP'$에서 $z=\rho\cos\phi$, $r=\rho\sin\phi$이고 $x=r\cos\theta,\ y=r\sin\theta$이므로 (1) $x=\rho\sin\phi\cos\theta$, $y=\rho\sin\phi\sin\theta$, $z=\rho\cos\phi$. 거리공식에서 (2) $\rho^2=x^2+y^2+z^2$ (직교→구면 변환에 사용) | 1177 | 본문(그림 5의 두 직각삼각형) | Fig 5 |
| 4 | rem | Example 2 옆 WARNING 박스 | 표기에 대한 경고 / Notation Warning | 구면좌표의 표기에는 보편적 합의가 없다. 대부분의 **물리학** 교재는 $\theta$와 $\phi$의 뜻을 서로 바꾸고, $\rho$ 대신 $r$을 쓴다 | 1178 | — | — |
| 5 | def | spherical wedge | 구면쐐기 / Spherical Wedge | 직육면체에 대응하는 영역 $E=\{(\rho,\theta,\phi)\mid a\le\rho\le b,\ \alpha\le\theta\le\beta,\ c\le\phi\le d\}$ (단 $a\ge0$, $\beta-\alpha\le2\pi$, $d-c\le\pi$) | 1178 | — | Fig 7 |
| 6 | note | (유도) | 구면쐐기의 부피와 리만 합 / Volume of a Spherical Wedge | $E$를 구 $\rho=\rho_i$, 반평면 $\theta=\theta_j$, 반원뿔 $\phi=\phi_k$로 잘게 나누면 $E_{ijk}$는 변이 $\Delta\rho$, $\rho_i\,\Delta\phi$, $\rho_i\sin\phi_k\,\Delta\theta$인 직육면체로 근사되어 $\Delta V_{ijk}\approx\rho_i^2\sin\phi_k\,\Delta\rho\,\Delta\theta\,\Delta\phi$. 평균값 정리(연습 51)로 어떤 점 $(\tilde\rho_i,\tilde\theta_j,\tilde\phi_k)$에서 **정확히** $\Delta V_{ijk}=\tilde\rho_i^2\sin\tilde\phi_k\,\Delta\rho\,\Delta\theta\,\Delta\phi$. 이 합은 $F(\rho,\theta,\phi)=f(\rho\sin\phi\cos\theta,\rho\sin\phi\sin\theta,\rho\cos\phi)\,\rho^2\sin\phi$의 리만 합 | 1178–1179 | — | Fig 7 (a)(b)(c) |
| 7 | thm | 공식 (3) | 구면좌표에서의 삼중적분 / Triple Integration in Spherical Coordinates | (3) $\displaystyle\iiint_E f(x,y,z)\,dV=\int_c^d\!\!\int_\alpha^\beta\!\!\int_a^b f(\rho\sin\phi\cos\theta,\ \rho\sin\phi\sin\theta,\ \rho\cos\phi)\;\rho^2\sin\phi\;d\rho\,d\theta\,d\phi$, $E$는 구면쐐기 | 1179 | 본문(카드 6의 리만 합 극한) | — |
| 8 | rem | Formula 3 뒤 단락 + Figure 8 | 부피소와 일반화·사용 시점 / Volume Element, Extension, When to Use | 변환 절차: (1)의 대입 후 $dV$를 $\boxed{\rho^2\sin\phi\;d\rho\,d\theta\,d\phi}$로 교체. 더 일반적인 영역 $E=\{\alpha\le\theta\le\beta,\ c\le\phi\le d,\ g_1(\theta,\phi)\le\rho\le g_2(\theta,\phi)\}$에도 같은 공식이 적용되며 $\rho$의 한계만 $g_1,g_2$로 바뀐다. **적분 영역의 경계가 구나 원뿔일 때** 쓰는 것이 보통 | 1179 | — | Fig 8 |
| 9 | fig | Figure 7 & 8 | 구면쐐기와 부피소 / Spherical Wedge and $dV$ | 구면쐐기 $E_{ijk}$의 세 변 $\Delta\rho$, $\rho\,\Delta\phi$, $\rho\sin\phi\,\Delta\theta$(옆면도·평면도 포함) — 인자 $\rho^2\sin\phi$의 출처를 보여 주므로 필수 | 1178–1179 | — | — |

카드 수: note 1, def 2, thm 2, rem 3, fig 1 = **9**

## B. 예제 기준값

| Example | PDF 쪽 | 유형 | 문제 요지 (영어 재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1177–1178 | 계산 (좌표변환) | Plot the point whose spherical coordinates are $\left(2,\tfrac\pi4,\tfrac\pi3\right)$ and convert it to rectangular coordinates. | $\left(\sqrt{\tfrac32},\ \sqrt{\tfrac32},\ 1\right)$ | $x=y=2\sin\tfrac\pi3\cos\tfrac\pi4=\dfrac{\sqrt6}{2}=1.2247449$, $z=2\cos\tfrac\pi3=1$; $\sqrt{3/2}=1.2247449$ (sympy) | ✔ | $\sqrt{6}/2=\sqrt{3/2}$ — 표기만 다름 |
| 2 | 1178 | 계산 (좌표변환) | Find spherical coordinates for the rectangular point $\left(0,\ 2\sqrt3,\ -2\right)$. | $\left(4,\ \tfrac\pi2,\ \tfrac{2\pi}3\right)$ | $\rho=\sqrt{0+12+4}=4$; $\cos\phi=\tfrac{-2}{4}=-\tfrac12\Rightarrow\phi=\tfrac{2\pi}3$; $\cos\theta=\dfrac{x}{\rho\sin\phi}=0$ 이고 $y>0$이므로 $\theta=\tfrac\pi2$ (sympy, `atan2` 확인) | ✔ | $y=2\sqrt3>0$이므로 $\theta=3\pi/2$가 아님 |
| 3 | 1179–1180 | 계산 | Evaluate $\iiint_B e^{(x^2+y^2+z^2)^{3/2}}\,dV$ over the unit ball $B$. | $\dfrac{4\pi}{3}\left(e-1\right)$ | $\int_0^\pi\!\int_0^{2\pi}\!\int_0^1 e^{\rho^3}\rho^2\sin\phi\;d\rho\,d\theta\,d\phi=\dfrac{4\pi(e-1)}{3}\approx7.1975221$ (sympy, 기호적으로 동치 확인) | ✔ | $x^2+y^2+z^2=\rho^2$이므로 피적분함수는 $e^{\rho^3}$. 직교좌표로는 사실상 계산 불가 |
| 4 | 1180 | 계산 | Use spherical coordinates to find the volume of the solid above the cone $z=\sqrt{x^2+y^2}$ and inside the sphere $x^2+y^2+z^2=z$. | $\dfrac{\pi}{8}$ | 구면: $\rho=\cos\phi$, 원뿔: $\phi=\pi/4$; $E=\{0\le\theta\le2\pi,\ 0\le\phi\le\tfrac\pi4,\ 0\le\rho\le\cos\phi\}$: $\int_0^{2\pi}\!\int_0^{\pi/4}\!\int_0^{\cos\phi}\rho^2\sin\phi\;d\rho\,d\phi\,d\theta=\dfrac\pi8$; 원기둥좌표 교차검증 $\int_0^{2\pi}\!\int_0^{1/2}\left(\tfrac12+\sqrt{\tfrac14-r^2}-r\right)r\,dr\,d\theta=\dfrac\pi8$ (sympy, 두 좌표계) | ✔ | 구는 원점을 지나고 중심이 $(0,0,\tfrac12)$, 반지름 $\tfrac12$. 원뿔식 $\rho\cos\phi=\rho\sin\phi\Rightarrow\phi=\pi/4$ |

예제 수: **4** (모두 계산형; 1·2는 좌표변환)

## C. 그림 필요 목록 (자체 SVG)

| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 1 | 점 $P(\rho,\theta,\phi)$: $\rho=|OP|$, $\theta$, $\phi$ | **필수** | 1 |
| Figure 2·3·4 | 좌표면 $\rho=c$(구), $\theta=c$(반평면), $\phi=c$(반원뿔, 두 경우) | **필수** | 2 |
| Figure 5 | 직각삼각형 $OPQ$, $OPP'$로부터 $z=\rho\cos\phi$, $r=\rho\sin\phi$ | **필수** | 3 |
| Figure 6 | 예제 1의 점 $(2,\pi/4,\pi/3)$ | 선택 | 예제 1 |
| Figure 7 (a)(b)(c) | 구면쐐기 $E_{ijk}$, 옆면도, 평면도 — 세 변 $\Delta\rho$, $\rho\Delta\phi$, $\rho\sin\phi\,\Delta\theta$ | **필수** | 9 (=6) |
| Figure 8 | 부피소 $dV=\rho^2\sin\phi\,d\rho\,d\theta\,d\phi$ | **필수** | 9 (=8) |
| Figure 9 | 예제 4의 입체(원뿔 위, 구 $\rho=\cos\phi$ 안) | **필수** | 예제 4 |
| Figure 10 | 예제 4를 $\rho\to\phi\to\theta$ 순서로 훑는 3컷 | 선택 | 예제 4 |

## D. ERRATA·판독 불확실
- 없음. 네 예제 모두 sympy와 일치.
- **WARNING 박스**(카드 4)는 지침대로 `rem` 카드로 처리했다. 사이트에서는 물리학 관례($\theta\leftrightarrow\phi$, $r$ 대신 $\rho$)와 혼동하지 않도록 눈에 띄게 배치할 것.
- pdftotext가 $\rho,\theta,\phi,\pi$를 모두 삭제해 원문만으로는 판독 불가 — PNG p.1177을 직접 확인해 정의와 (1)(2)를 확정했다.
- 예제 1의 교재 답 $\left(\sqrt{3/2},\sqrt{3/2},1\right)$은 $\left(\tfrac{\sqrt6}{2},\tfrac{\sqrt6}{2},1\right)$과 같은 값(표기 차이).

## E. 절 요약 (사이트 도입 note 초안)
구면좌표 $(\rho,\theta,\phi)$는 원점까지의 거리 $\rho$, $z$축 둘레의 각 $\theta$, 양의 $z$축과 이루는 각 $\phi$로 점을 나타낸다. 좌표면이 각각 구·수직 반평면·반원뿔이므로, 적분 영역의 경계가 **구나 원뿔**이거나 피적분함수가 $x^2+y^2+z^2$의 함수일 때 삼중적분이 극적으로 간단해진다. 핵심은 부피소 $dV=\rho^2\sin\phi\,d\rho\,d\theta\,d\phi$이고, 이 인자는 구면쐐기의 세 변 $\Delta\rho$, $\rho\Delta\phi$, $\rho\sin\phi\,\Delta\theta$의 곱에서 나온다. 주의: 구면좌표 기호는 표준화되어 있지 않아 물리학 교재는 $\theta$와 $\phi$를 바꿔 쓰고 $\rho$ 대신 $r$을 쓴다.

## F. 공통과제 문항 (2차 공통과제)
- **과제 제출 문항**: 18, 20, 31, 43
- **학습 참고 문항**: 1~2, 3~4, 5~6, 7~8, 9~10, 11~14, 15~16, 17~18, 19~20, 21~22, 23~36, 37~40, 42, 43~45
