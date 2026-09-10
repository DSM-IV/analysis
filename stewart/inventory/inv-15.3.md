# §15.3 Double Integrals in Polar Coordinates — PDF p.1137–1143 (인쇄 p.1100–1106)

> 본문은 PDF p.1137 하단에서 시작(그 위는 §15.2 연습문제), 본문 종료 p.1141 중간, 연습문제 p.1142–1143.

## A. 카드 인벤토리 (원문 순서)

| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입) + Review of Polar Coordinates | 극좌표의 복습 / Review of Polar Coordinates | 적분 영역이 원판·원환이면 직교좌표 기술이 복잡하지만 극좌표로는 간단하다. $r^2=x^2+y^2$, $x=r\cos\theta$, $y=r\sin\theta$. 원점 중심 원은 $r=$상수: 단위원판 $\{0\le r\le1,\ 0\le\theta\le2\pi\}$, 반원환 $\{1\le r\le2,\ 0\le\theta\le\pi\}$ | 1137 | — | Fig 1, 2 |
| 2 | def | polar rectangle | 극직사각형 / Polar Rectangle | $R=\{(r,\theta)\mid a\le r\le b,\ \alpha\le\theta\le\beta\}$ — 두 동심원호와 두 반직선으로 둘러싸인 영역 | 1138 | — | Fig 3 |
| 3 | note | (유도 단락) | 극좌표 리만 합과 넓이소 / Polar Riemann Sums and the Area Element | $[a,b]$를 $m$등분, $[\alpha,\beta]$를 $n$등분해 극부분직사각형 $R_{ij}$를 만들면 중심 $r_i^*=\tfrac12(r_{i-1}+r_i)$, $\theta_j^*=\tfrac12(\theta_{j-1}+\theta_j)$이고, 부채꼴 넓이 $\tfrac12r^2\theta$의 차로 $\Delta A_i=\tfrac12(r_i^2-r_{i-1}^2)\Delta\theta=r_i^*\,\Delta r\,\Delta\theta$. 따라서 (1) $\sum\sum f(r_i^*\cos\theta_j^*,r_i^*\sin\theta_j^*)\Delta A_i=\sum\sum g(r_i^*,\theta_j^*)\Delta r\,\Delta\theta$ (단 $g(r,\theta)=r\,f(r\cos\theta,r\sin\theta)$) — 이는 $\int_\alpha^\beta\!\int_a^b g\,dr\,d\theta$의 리만 합 | 1138–1139 | — | Fig 4 |
| 4 | thm | (2) Change to Polar Coordinates in a Double Integral | 이중적분의 극좌표 변환 / Change to Polar Coordinates | $f$가 극직사각형 $R:\ 0\le a\le r\le b,\ \alpha\le\theta\le\beta$ (단 $0\le\beta-\alpha\le2\pi$)에서 연속이면 (2) $\displaystyle\iint_R f(x,y)\,dA=\int_\alpha^\beta\!\!\int_a^b f(r\cos\theta,\,r\sin\theta)\,r\,dr\,d\theta$ | 1139 | 본문(카드 3의 리만 합 극한) | — |
| 5 | rem | Formula 2 뒤 단락 + Figure 5 | 인자 $r$을 잊지 말 것 / Remember the Extra Factor $r$ | 변환 절차: $x=r\cos\theta$, $y=r\sin\theta$로 바꾸고 $r,\theta$의 적분 한계를 정한 뒤 $dA$를 $\boxed{r\,dr\,d\theta}$로 교체. 미소 극직사각형을 변이 $dr$, $r\,d\theta$인 보통 직사각형으로 보면 $dA=r\,dr\,d\theta$로 기억됨 | 1139 | — | Fig 5 |
| 6 | thm | 식 (3) | 일반 극영역에서의 이중적분 / Double Integrals over General Polar Regions | $f$가 $D=\{(r,\theta)\mid\alpha\le\theta\le\beta,\ h_1(\theta)\le r\le h_2(\theta)\}$에서 연속이면 (3) $\displaystyle\iint_D f(x,y)\,dA=\int_\alpha^\beta\!\!\int_{h_1(\theta)}^{h_2(\theta)} f(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta$ — §15.2의 제2형 영역에 대응 | 1140 | 본문 (공식 (2)와 15.2.4의 결합) | Fig 8 |
| 7 | thm | (3)의 특수화 | 극좌표 넓이 공식 / Area in Polar Coordinates | (3)에서 $f=1$, $h_1=0$, $h_2=h(\theta)$로 두면 $\displaystyle A(D)=\iint_D 1\,dA=\int_\alpha^\beta\!\!\int_0^{h(\theta)}r\,dr\,d\theta=\int_\alpha^\beta\tfrac12[h(\theta)]^2\,d\theta$ — §10.4의 공식 10.4.3과 일치 | 1141 | 본문 | — |
| 8 | rem | Example 3 뒤 단락 | 극좌표를 쓰는 이유 / Why Polar Coordinates Help | 예제 3을 직교좌표로 하면 $\int_{-1}^{1}\!\int_{-\sqrt{1-x^2}}^{\sqrt{1-x^2}}(1-x^2-y^2)\,dy\,dx$가 되어 $\int(1-x^2)^{3/2}dx$를 만나 계산이 어렵다. 원·원판·원환 영역이거나 피적분함수가 $x^2+y^2$의 꼴이면 극좌표가 유리 | 1140 | — | — |
| 9 | fig | Figure 3 & 4 | 극직사각형과 그 분할 / Polar Rectangle and Its Subdivision | $r=a,b$의 두 원호와 $\theta=\alpha,\beta$의 두 반직선, 그리고 $r=r_i$·$\theta=\theta_j$의 격자로 잘린 $R_{ij}$와 중심 $(r_i^*,\theta_j^*)$ — $\Delta A_i=r_i^*\Delta r\Delta\theta$ 이해에 필수 | 1138 | — | — |

카드 수: note 2, def 1, thm 3, rem 2, fig 1 = **9**

## B. 예제 기준값

| Example | PDF 쪽 | 유형 | 문제 요지 (영어 재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1139 | 계산 | Integrate $3x+4y^2$ over the upper half of the annulus between the circles $x^2+y^2=1$ and $x^2+y^2=4$. | $\dfrac{15\pi}{2}$ | 극좌표 $\int_0^\pi\!\int_1^2(3r\cos\theta+4r^2\sin^2\theta)r\,dr\,d\theta=\tfrac{15\pi}{2}\approx23.5619$; 직교좌표로 세 조각 분할해도 $\tfrac{15\pi}{2}$ (sympy, 두 방법) | ✔ | $R:\ 1\le r\le2,\ 0\le\theta\le\pi$. $\sin^2\theta=\tfrac12(1-\cos2\theta)$ 사용 |
| 2 | 1140 | 계산 | Convert and evaluate $\displaystyle\int_{-1}^{1}\!\int_0^{\sqrt{1-x^2}}(x^2+y^2)\,dy\,dx$. | $\dfrac{\pi}{4}$ | 극좌표 $\int_0^\pi\!\int_0^1 r^3\,dr\,d\theta=\tfrac\pi4$; 직교좌표 그대로 계산해도 $\tfrac\pi4$ (sympy) | ✔ | 영역은 상반 단위원판 $\{0\le\theta\le\pi,\ 0\le r\le1\}$ |
| 3 | 1140 | 계산 | Find the volume of the solid trapped between the plane $z=0$ and the paraboloid $z=1-x^2-y^2$. | $\dfrac{\pi}{2}$ | 극좌표 $\int_0^{2\pi}\!\int_0^1(1-r^2)r\,dr\,d\theta=\tfrac\pi2$; 직교좌표 $\int_{-1}^{1}\!\int_{-\sqrt{1-x^2}}^{\sqrt{1-x^2}}(1-x^2-y^2)dy\,dx=\tfrac\pi2$ (sympy) | ✔ | 교선 $x^2+y^2=1$ ⇒ 밑면은 단위원판 |
| 4 | 1141 | 계산 | Use a double integral to find the area of one petal of the four-leaved rose $r=\cos2\theta$. | $\dfrac{\pi}{8}$ | $\int_{-\pi/4}^{\pi/4}\!\int_0^{\cos2\theta}r\,dr\,d\theta=\tfrac\pi8$; 넓이 공식 $\int_{-\pi/4}^{\pi/4}\tfrac12\cos^2 2\theta\,d\theta=\tfrac\pi8$ (sympy, 두 방법) | ✔ | 한 잎은 $-\pi/4\le\theta\le\pi/4$. $\cos^2 2\theta=\tfrac12(1+\cos4\theta)$ |
| 5 | 1141 | 계산 | Find the volume of the solid under $z=x^2+y^2$, above the $xy$-plane, and inside the cylinder $x^2+y^2=2x$. | $\dfrac{3\pi}{2}$ | 극좌표 $\int_{-\pi/2}^{\pi/2}\!\int_0^{2\cos\theta}r^3\,dr\,d\theta=\tfrac{3\pi}{2}\approx4.71239$; 직교좌표 수치 적분(중점법칙 $n=2000$, 안쪽 $y$-적분은 해석적) $\approx4.71241$ (sympy + python) | ✔ | 경계원 $(x-1)^2+y^2=1$, 극좌표로 $r=2\cos\theta$. $\cos^4\theta$ 적분에 배각공식 2회 |

예제 수: **5** (모두 계산형)

## C. 그림 필요 목록 (자체 SVG)

| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 1 | 점 $P$의 극좌표 $(r,\theta)$와 직교좌표 $(x,y)$의 관계 | 선택 | 1 |
| Figure 2 | (a) 단위원판 $0\le r\le1$ (b) 반원환 $1\le r\le2,\ 0\le\theta\le\pi$ | **필수** | 1 (예제 1의 영역) |
| Figure 3 | 극직사각형 $a\le r\le b$, $\alpha\le\theta\le\beta$ | **필수** | 9 (=2) |
| Figure 4 | 극직사각형을 원호와 반직선으로 나눈 격자, $R_{ij}$, 중심 $(r_i^*,\theta_j^*)$ | **필수** | 9 (=3) |
| Figure 5 | 미소 극직사각형: 변 $dr$과 $r\,d\theta$, $dA=r\,dr\,d\theta$ | **필수** | 5 |
| Figure 6 | 예제 2의 상반 단위원판 | 선택 | 예제 2 |
| Figure 7 | 예제 3의 포물면 뚜껑 입체 | 선택 | 예제 3 |
| Figure 8 | 일반 극영역 $h_1(\theta)\le r\le h_2(\theta)$ | **필수** | 6 |
| Figure 9 | 네잎장미 $r=\cos2\theta$와 $\theta=\pm\pi/4$로 잘린 한 잎 | **필수** | 예제 4 |
| Figure 10·11 | 원판 $(x-1)^2+y^2=1$ (=$r=2\cos\theta$)과 그 위 포물면 입체 | **필수**(10) | 예제 5 |

## D. ERRATA·판독 불확실
- 없음. pdftotext가 $\theta$·$\pi$·$\alpha$·$\beta$를 대부분 삭제해 텍스트만으로는 판독이 어렵지만, 문맥과 sympy 재계산으로 모든 식과 답이 확정됨.
- 공통과제 표에 교재 표현 정정 지시가 두 건 있음 — F 참조.

## E. 절 요약 (사이트 도입 note 초안)
적분 영역이 원판·원환·장미곡선처럼 원점에서의 거리와 각으로 기술되는 도형이면 직교좌표 반복적분은 $\sqrt{a^2-x^2}$ 같은 한계 때문에 금세 손을 쓸 수 없게 된다. 이때는 영역을 **극직사각형**($a\le r\le b$, $\alpha\le\theta\le\beta$)이나 더 일반적으로 $h_1(\theta)\le r\le h_2(\theta)$로 기술하고 극좌표로 바꾼다. 핵심은 넓이소가 $dA=dx\,dy$가 아니라 $dA=r\,dr\,d\theta$라는 사실이며, 이 여분의 $r$은 극부분직사각형의 넓이 $\Delta A_i=r_i^*\Delta r\,\Delta\theta$에서 나온다 — 이것이 §15.9 변수변환 야코비안의 첫 사례다. 피적분함수가 $x^2+y^2$의 함수일 때도 극좌표가 유리하며, $f=1$로 두면 §10.4의 극좌표 넓이 공식 $A=\int_\alpha^\beta\tfrac12[h(\theta)]^2d\theta$가 그대로 나온다.

## F. 공통과제 문항 (2차 공통과제)
- **과제 제출 문항**: 11, 15, 30, 39, 41
  - 30번: 교재의 "above the ring"은 **"in the $xy$-plane"** 인 ring으로 읽을 것 (공통과제 표의 지시).
- **학습 참고 문항**: 10, 12, 13, 16, 20, 21, 27, 28, 32, 34, 35, 36, 41, 42, 49
  - 35번: 교재의 "below the sphere"를 **"inside the sphere"** 로 정정할 것 (공통과제 표의 지시).
  - 29–31번의 "disk" 또는 "ring"은 **$xy$-평면의** disk/ring임을 고지할 것 (공통과제 표의 지시).
