# §15.7 Triple Integrals in Cylindrical Coordinates — PDF p.1170–1176 (인쇄 p.1133–1139)

> 본문은 PDF p.1170 하단에서 시작(그 위는 §15.6 연습문제), 본문·예제 종료 p.1174 하단, 연습문제 p.1175–1176.

## A. 카드 인벤토리 (원문 순서)

| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입) | 평면 극좌표의 복습 / Review of Polar Coordinates | 평면에서 극좌표가 곡선·영역을 편하게 기술하듯(§10.3), 공간에서도 대응하는 좌표계가 있다. $x=r\cos\theta$, $y=r\sin\theta$, $r^2=x^2+y^2$, $\tan\theta=y/x$ | 1170 | — | Fig 1 |
| 2 | def | Cylindrical Coordinates, 식 (1)(2) | 원기둥좌표 / Cylindrical Coordinates | 점 $P$를 $(r,\theta,z)$로 나타낸다: $r,\theta$는 $P$의 $xy$-평면 정사영의 극좌표, $z$는 $xy$-평면에서 $P$까지의 **부호 있는 거리**. (1) 원기둥→직교: $x=r\cos\theta,\ y=r\sin\theta,\ z=z$. (2) 직교→원기둥: $r^2=x^2+y^2,\ \tan\theta=\dfrac{y}{x},\ z=z$ (극좌표처럼 $\theta$의 선택은 무한히 많음) | 1171 | — | Fig 2 |
| 3 | rem | Example 1 뒤 단락 + Figures 4–6 | 좌표면과 사용처 / Coordinate Surfaces and When to Use Them | $r=c$는 축이 $z$축인 원기둥(이름의 유래), $\theta=c$는 원점을 지나는 수직평면, $z=c$는 수평평면. 원기둥좌표는 **한 축에 대한 대칭**이 있는 문제에 유용하며, 그 대칭축을 $z$축으로 잡는다 | 1171–1172 | — | Fig 4, 5, 6 |
| 4 | note | (유도) 식 (3) | 극좌표 정사영을 갖는 제1형 영역 / Type 1 Region with a Polar Projection | $E=\{(x,y,z)\mid(x,y)\in D,\ u_1(x,y)\le z\le u_2(x,y)\}$이고 정사영 $D$가 극좌표로 $D=\{(r,\theta)\mid\alpha\le\theta\le\beta,\ h_1(\theta)\le r\le h_2(\theta)\}$로 기술된다고 하자. 15.6.6에 의해 (3) $\displaystyle\iiint_E f\,dV=\iint_D\left[\int_{u_1(x,y)}^{u_2(x,y)}f(x,y,z)\,dz\right]dA$ | 1172 | — | Fig 8 |
| 5 | thm | 공식 (4) | 원기둥좌표에서의 삼중적분 / Triple Integration in Cylindrical Coordinates | (4) $\displaystyle\iiint_E f(x,y,z)\,dV=\int_\alpha^\beta\!\!\int_{h_1(\theta)}^{h_2(\theta)}\!\!\int_{u_1(r\cos\theta,\,r\sin\theta)}^{u_2(r\cos\theta,\,r\sin\theta)} f(r\cos\theta,\,r\sin\theta,\,z)\;r\,dz\,dr\,d\theta$ | 1172 | 본문(식 (3)과 15.3.3(극좌표 이중적분)의 결합) | — |
| 6 | rem | Formula 4 뒤 단락 + Figure 9 | 부피소 $dV=r\,dz\,dr\,d\theta$와 사용 시점 / The Volume Element, and When to Convert | 변환 절차: $x=r\cos\theta,\ y=r\sin\theta$로 바꾸고 $z$는 그대로 두며 $z,r,\theta$의 적분 한계를 정한 뒤 $dV$를 $\boxed{r\,dz\,dr\,d\theta}$로 교체. 미소상자의 변이 $dr,\ r\,d\theta,\ dz$이므로 $dV=r\,dz\,dr\,d\theta$. **$E$가 원기둥좌표로 쉽게 기술되거나 $f$에 $x^2+y^2$이 들어 있을 때** 쓸 만하다 | 1173 | — | Fig 9 |
| 7 | fig | Figure 2 & 9 | 원기둥좌표와 부피소 / Cylindrical Coordinates and $dV$ | $P(r,\theta,z)$와 그 $xy$-평면 정사영 $(r,\theta,0)$ / 변이 $dr$, $r\,d\theta$, $dz$인 미소상자 — 좌표 정의와 인자 $r$의 출처 | 1171, 1173 | — | — |

카드 수: note 2, def 1, thm 1, rem 2, fig 1 = **7**

## B. 예제 기준값

| Example | PDF 쪽 | 유형 | 문제 요지 (영어 재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1171 | 계산 (좌표변환) | (a) Plot the point with cylindrical coordinates $\left(2,\tfrac{2\pi}{3},1\right)$ and give its rectangular coordinates. (b) Give cylindrical coordinates for the rectangular point $(3,-3,-7)$. | (a) $\left(-1,\sqrt3,1\right)$; (b) $\left(3\sqrt2,\ \tfrac{7\pi}{4},\ -7\right)$ 또는 $\left(3\sqrt2,\ -\tfrac{\pi}{4},\ -7\right)$ | (a) $(2\cos\tfrac{2\pi}3,\,2\sin\tfrac{2\pi}3,\,1)=(-1,\sqrt3,1)$; (b) $r=\sqrt{9+9}=3\sqrt2$, $\operatorname{atan2}(-3,3)=-\tfrac\pi4$ (또는 $+2\pi$ 하여 $\tfrac{7\pi}4$), $z=-7$ (sympy) | ✔ | (b)에서 $(3,-3)$은 $xy$-평면 4사분면이므로 $\theta=-\tfrac\pi4+2n\pi$. $\theta$ 선택은 무한히 많음 |
| 2 | 1172 | 개념·스케치 | Describe the surface given in cylindrical coordinates by $z=r$. | 그래프형 — 서술 답: 축이 $z$축인 (위쪽 반쪽) 원뿔. 직교좌표로 $z^2=x^2+y^2$ ($z\ge0$) | $z=r\Rightarrow z^2=r^2=x^2+y^2$이고 $z\ge0$; 수평 자취 $z=k>0$은 반지름 $k$의 원 $x^2+y^2=k^2$ ⇒ $z$축을 축으로 하는 원뿔 (sympy/손 계산) | ✔ | $\theta$가 식에 없으므로 자유롭게 변함 = 회전면. §12.6 표 1과 대조 |
| 3 | 1173 | 계산 | Evaluate $\iiint_E x^2\,dV$ where $E$ is the region under the paraboloid $z=4-x^2-y^2$ and above the $xy$-plane. | $\dfrac{16\pi}{3}$ | $E=\{0\le\theta\le2\pi,\ 0\le r\le2,\ 0\le z\le4-r^2\}$: $\int_0^{2\pi}\!\int_0^2\!\int_0^{4-r^2}(r\cos\theta)^2 r\,dz\,dr\,d\theta=\dfrac{16\pi}{3}\approx16.75516$; 직교 중점법칙($1500^2$) $16.75516$ (sympy + python) | ✔ | 포물면이 $xy$-평면과 만나는 원은 $r=2$. $\cos^2\theta$ 적분에 배각공식 |
| 4 | 1174 | 계산 | A solid inside the cylinder $x^2+y^2=1$, on the $y\ge0$ side of the $xz$-plane, below $z=4$ and above $z=1-x^2-y^2$, has density proportional to the distance from the cylinder's axis. Find its mass. | $m=\dfrac{6\pi K}{5}$ ($K$는 비례상수) | $E=\{0\le\theta\le\pi,\ 0\le r\le1,\ 1-r^2\le z\le4\}$, $\rho=K\sqrt{x^2+y^2}=Kr$: $\int_0^\pi\!\int_0^1\!\int_{1-r^2}^{4}(Kr)\,r\,dz\,dr\,d\theta=\dfrac{6\pi K}{5}$ (sympy) | ✔ | 축약 후 $K\int_0^\pi d\theta\int_0^1(3r^2+r^4)dr$. pdftotext에서 $\pi$가 소실되어 "6K/5"처럼 보이나 정답은 $6\pi K/5$ |
| 5 | 1174 | 계산 | Convert $\displaystyle\int_{-2}^{2}\!\int_{-\sqrt{4-x^2}}^{\sqrt{4-x^2}}\!\int_{\sqrt{x^2+y^2}}^{2}(x^2+y^2)\,dz\,dy\,dx$ to cylindrical coordinates and evaluate. | $\dfrac{16\pi}{5}$ | $E=\{0\le\theta\le2\pi,\ 0\le r\le2,\ r\le z\le2\}$: $\int_0^{2\pi}\!\int_0^2\!\int_r^2 r^2\cdot r\,dz\,dr\,d\theta=\dfrac{16\pi}{5}\approx10.05310$; 직교 중점법칙($1200^2$) $10.05310$ (sympy + python) | ✔ | 아래 경계는 원뿔 $z=\sqrt{x^2+y^2}$, 위 경계는 평면 $z=2$, 정사영은 원판 $x^2+y^2\le4$ |

예제 수: **5** (계산 4, 개념·스케치 1)

## C. 그림 필요 목록 (자체 SVG)

| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 1 | 평면 극좌표 $(r,\theta)$와 $(x,y)$ | 선택 | 1 |
| Figure 2 | 점 $P(r,\theta,z)$와 $xy$-평면 정사영 $(r,\theta,0)$ | **필수** | 7 (=2) |
| Figure 3 | 예제 1(a)의 점 $\left(2,\tfrac{2\pi}3,1\right)$ | 선택 | 예제 1 |
| Figure 4·5·6 | 좌표면 $r=c$(원기둥), $\theta=c$(수직평면), $z=c$(수평평면) | **필수** | 3 |
| Figure 7 | 원뿔 $z=r$ | **필수** | 예제 2 |
| Figure 8 | 극좌표로 기술되는 정사영 $D$를 갖는 제1형 입체 $E$ | **필수** | 4 |
| Figure 9 | 부피소: 변이 $dr$, $r\,d\theta$, $dz$인 미소상자 | **필수** | 7 (=6) |
| Figure 10 | 예제 3의 포물면 뚜껑 입체 | 선택 | 예제 3 |
| Figure 11 | 예제 3을 $dz\,dr\,d\theta$ 순서로 훑는 3컷 | 선택 | 예제 3 |
| Figure 12 | 예제 4의 입체(원기둥 안, $z=4$ 아래, $z=1-r^2$ 위, 반쪽) | **필수** | 예제 4 |
| Figure 13 | 예제 5의 입체(원뿔 $z=\sqrt{x^2+y^2}$ 위, 평면 $z=2$ 아래) | **필수** | 예제 5 |

## D. ERRATA·판독 불확실
- 없음. 다섯 예제 모두 sympy(및 직교좌표 수치 재계산)와 일치.
- pdftotext가 $\theta$·$\pi$를 삭제해 예제 3~5의 답이 "16/3", "6K/5", "16/5"처럼 보이나, 재계산 결과 각각 $\dfrac{16\pi}{3}$, $\dfrac{6\pi K}{5}$, $\dfrac{16\pi}{5}$ 임을 확정.
- 예제 4의 "to the right of the $xz$-plane"은 $y\ge0$ 쪽, 즉 $0\le\theta\le\pi$를 뜻함(교재의 영역 기술과 일치).

## E. 절 요약 (사이트 도입 note 초안)
원기둥좌표 $(r,\theta,z)$는 평면 극좌표에 높이 $z$를 그대로 얹은 좌표계로, $r=c$가 원기둥, $\theta=c$가 수직평면, $z=c$가 수평평면이 된다. $z$축에 대한 회전대칭이 있는 입체(원기둥·원뿔·포물면·구)나 피적분함수에 $x^2+y^2$이 들어 있는 삼중적분은 이 좌표에서 훨씬 간단해진다. 핵심 공식은 $dV=r\,dz\,dr\,d\theta$이며, 이는 §15.3의 $dA=r\,dr\,d\theta$에 $dz$를 곱한 것 — 즉 제1형 입체영역의 안쪽 $z$-적분(§15.6)과 극좌표 이중적분(§15.3)을 이어 붙인 결과다. 실전에서는 직교좌표 반복적분을 보고 정사영이 원판인지, 경계면이 $r$만의 식인지 살펴 변환 여부를 판단한다.

## F. 공통과제 문항 (2차 공통과제)
- **과제 제출 문항**: 15, 17, 22, 27, 31
- **학습 참고 문항**: 1~2, 3~4, 5~6, 7~8, 9~10, 11~12, 13, 15~16, 17~18, 19~30, 31~32
