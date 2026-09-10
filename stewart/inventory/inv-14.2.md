# §14.2 Limits and Continuity — PDF p.1026–1035 (인쇄 p.989–998)

본문(설명·예제) PDF p.1026–1035(인쇄 989–998), 연습문제 PDF p.1035–1036(인쇄 998–999).
※ PDF p.1026 윗부분은 §14.1 연습문제 71–81이고, §14.2 절 제목은 같은 쪽 아래쪽부터 시작한다.

## A. 카드 인벤토리 (원문 순서)

| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입, Table 1·2) | 수치표로 본 두 극한 / A Numerical Comparison | $(x,y)\to(0,0)$에서 $f(x,y)=\dfrac{\sin(x^2+y^2)}{x^2+y^2}$의 값은 1에 접근하지만 $g(x,y)=\dfrac{x^2-y^2}{x^2+y^2}$의 값은 어느 수에도 접근하지 않는다. 즉 $\lim_{(x,y)\to(0,0)}\frac{\sin(x^2+y^2)}{x^2+y^2}=1$이고 $\lim_{(x,y)\to(0,0)}\frac{x^2-y^2}{x^2+y^2}$는 존재하지 않는다 | 1026–1027 | — | — |
| 2 | def | **1** Definition | 이변수함수의 극한 (ε-δ) / Limit of a Function of Two Variables | $D$가 $(a,b)$에 임의로 가까운 점들을 포함할 때, $\lim_{(x,y)\to(a,b)}f(x,y)=L$이란: 모든 $\varepsilon>0$에 대해 어떤 $\delta>0$이 있어 $(x,y)\in D$이고 $0<\sqrt{(x-a)^2+(y-b)^2}<\delta$이면 $|f(x,y)-L|<\varepsilon$ | 1027 | — | — |
| 3 | note | (Definition 1 뒤 단락, Figure 1·2) | 정의의 기하적 의미 / Geometric Reading of the Definition | 다른 표기 $\lim_{x\to a,\,y\to b}f(x,y)=L$, $f(x,y)\to L$ as $(x,y)\to(a,b)$. $|f(x,y)-L|$은 두 수의 거리, $\sqrt{(x-a)^2+(y-b)^2}$는 두 점의 거리. 구간 $(L-\varepsilon,L+\varepsilon)$이 주어지면 $(a,b)$ 중심 반지름 $\delta$인 원판 $D_\delta$가 존재해 $f(D_\delta\setminus\{(a,b)\})\subset(L-\varepsilon,L+\varepsilon)$; 곡면 $S$의 대응 부분이 두 수평평면 $z=L\pm\varepsilon$ 사이에 놓인다 | 1027–1028 | — | Fig 1, 2 |
| 4 | note | Showing That a Limit Does Not Exist | 접근 방향이 무한히 많다 / Infinitely Many Paths | 일변수에서는 좌·우 두 방향뿐이지만, 이변수에서는 $(x,y)$가 정의역 안에 있기만 하면 어떤 방식으로든 $(a,b)$에 접근할 수 있다. 정의 1은 **거리**만 언급하고 방향은 언급하지 않으므로, 극한이 존재하면 접근 방식에 무관하게 같은 값이어야 한다 | 1028 | — | Fig 3 |
| 5 | thm | (무번호 박스) | 경로 판정법 / Two-Path Test | 경로 $C_1$을 따라 $f(x,y)\to L_1$, 경로 $C_2$를 따라 $f(x,y)\to L_2$이고 $L_1\ne L_2$이면 $\lim_{(x,y)\to(a,b)}f(x,y)$는 존재하지 않는다 | 1028 | 없음(정의 1에서 즉시) | — |
| 6 | rem | Properties of Limits + **(2)** | 극한 법칙 / Limit Laws | 합·차·상수배·곱·몫 법칙(§1.6)이 이변수로 확장된다(몫은 분모의 극한이 $0$이 아닐 때). 특수 극한 (2): $\lim_{(x,y)\to(a,b)}x=a$, $\lim_{(x,y)\to(a,b)}y=b$, $\lim_{(x,y)\to(a,b)}c=c$ (증명은 연습문제 54) | 1030 | 연습문제 54 | — |
| 7 | thm | **(3)**, **(4)** | 다항·유리함수의 극한은 직접대입 / Limits of Polynomials and Rational Functions | 다항함수 $p$(항 $cx^my^n$의 합)에 대해 (3) $\lim_{(x,y)\to(a,b)}p(x,y)=p(a,b)$. 유리함수 $q=p/r$에 대해 $(a,b)$가 $q$의 정의역에 있으면 (4) $\lim_{(x,y)\to(a,b)}q(x,y)=\dfrac{p(a,b)}{r(a,b)}=q(a,b)$ | 1030 | 본문(극한 법칙 + (2)) | — |
| 8 | rem | (Example 5 뒤 단락, 식 **(5)**) | 조임정리도 성립 / The Squeeze Theorem Extends | 조임정리는 이변수 이상에서도 성립한다. 예제 6에서 쓰는 부등식 (5): $\dfrac{3x^2|y|}{x^2+y^2}\le 3|y|=3\sqrt{y^2}\le 3\sqrt{x^2+y^2}$ | 1031 | — | — |
| 9 | def | **6** Definition | 연속 / Continuity at a Point | $f$가 $(a,b)$에서 연속이라 함은 $\lim_{(x,y)\to(a,b)}f(x,y)=f(a,b)$인 것. $D$의 모든 점에서 연속이면 $f$는 $D$에서 연속 | 1032 | — | — |
| 10 | note | (Definition 6 뒤 단락) | 연속함수의 대수 / Building Continuous Functions | 연속의 직관: $(x,y)$가 조금 변하면 $f(x,y)$도 조금 변한다(그래프에 구멍·끊김 없음). (3)에서 모든 다항함수는 $\mathbb R^2$에서 연속, (4)에서 유리함수는 그 정의역에서 연속. 연속함수의 합·차·곱·몫도 각자의 정의역에서 연속 | 1032 | — | — |
| 11 | note | (Example 9 뒤 단락) | 합성함수의 연속 / Continuity of Composites | $f$가 이변수 연속함수이고 $g$가 $f$의 치역에서 정의된 일변수 연속함수이면 $h=g\circ f$, 즉 $h(x,y)=g(f(x,y))$도 연속 | 1033 | 서술만(증명 생략) | — |
| 12 | note | Functions of Three or More Variables | 삼변수 이상의 극한·연속 / Limits and Continuity in Higher Dimensions | $\lim_{(x,y,z)\to(a,b,c)}f=L$의 ε-δ 정의는 거리 $\sqrt{(x-a)^2+(y-b)^2+(z-c)^2}$로 같은 꼴. 연속은 $\lim_{(x,y,z)\to(a,b,c)}f=f(a,b,c)$. 예: $f(x,y,z)=\dfrac1{x^2+y^2+z^2-1}$은 단위구면 $x^2+y^2+z^2=1$ 위에서만 불연속 | 1034 | — | — |
| 13 | def | **7** | $\mathbb R^n$에서의 극한 (통합 정의) / Limit in $\mathbb R^n$ | $f$가 $D\subset\mathbb R^n$에서 정의될 때 $\lim_{\mathbf x\to\mathbf a}f(\mathbf x)=L$이란: 모든 $\varepsilon>0$에 대해 어떤 $\delta>0$이 있어 $\mathbf x\in D$이고 $0<|\mathbf x-\mathbf a|<\delta$이면 $|f(\mathbf x)-L|<\varepsilon$. $n=1$이면 일변수 정의, $n=2$이면 정의 1, $n=3$이면 삼변수 정의. 연속은 $\lim_{\mathbf x\to\mathbf a}f(\mathbf x)=f(\mathbf a)$ | 1034 | — | — |
| 14 | fig | Figure 3 + 4 + 5 | 경로에 따라 달라지는 극한 / Different Paths, Different Limits | $(a,b)$로 여러 방향에서 접근하는 그림(Fig 3), $x$축 위 $f=1$·$y$축 위 $f=-1$(Fig 4), $x$·$y$축 위 $f=0$·직선 $y=x$ 위 $f=\tfrac12$(Fig 5)을 한 세트로 | 1028–1029 | — | — |

카드 수: note 6, def 3, thm 2, rem 2, fig 1 — 합계 **14**.

## B. 예제 기준값 (예제 11개)

| Example | PDF 쪽 | 유형 | 문제 요지 (영어 재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1028–1029 | 증명(show) | Show that $\dfrac{x^2-y^2}{x^2+y^2}$ has no limit at the origin. | $x$축을 따라 $f\to1$, $y$축을 따라 $f\to-1$이므로 두 경로의 극한이 달라 **극한이 존재하지 않는다** | sympy: $y=0$에서 $1$, $x=0$에서 $-1$; 극좌표로 $\cos2\theta$ (θ 의존) | ✅ | 절 도입의 수치 추측을 확인 |
| 2 | 1029 | 증명(show) | Decide whether $\dfrac{xy}{x^2+y^2}$ has a limit at the origin. | 두 축을 따라서는 $0$이지만 $y=x$를 따라서는 $f(x,x)=\dfrac{x^2}{2x^2}=\tfrac12\to\tfrac12$. 값이 다르므로 **극한 없음** | sympy: 축 $0$, $y=x$에서 $1/2$; 일반 직선 $y=mx$에서 $\dfrac{m}{m^2+1}$ | ✅ | Figure 6의 능선이 $y=x$ 위 $f=\tfrac12$ |
| 3 | 1029–1030 | 증명(show) | Decide whether $\dfrac{xy^2}{x^2+y^4}$ has a limit at the origin. | 원점을 지나는 **모든 직선**을 따라서는 $0$($f(x,mx)=\dfrac{m^2x}{1+m^4x^2}$, $x=0$에서도 $0$)이지만 포물선 $x=y^2$을 따라서는 $f(y^2,y)=\dfrac{y^4}{2y^4}=\tfrac12$. 따라서 **극한 없음** | sympy: 직선 $0$, 포물선 $1/2$ | ✅ | 직선만으로는 판정 불가함을 보이는 예 (Figure 7의 능선) |
| 4 | 1031 | 계산 | Evaluate $\lim_{(x,y)\to(1,2)}(x^2y^3-x^3y^2+3x+2y)$. | $=1^2\cdot2^3-1^3\cdot2^2+3\cdot1+2\cdot2=\mathbf{11}$ (다항식이므로 직접대입) | sympy: $11$ (반복극한도 $11$) | ✅ | (3)의 응용 |
| 5 | 1031 | 계산 | Evaluate $\lim_{(x,y)\to(-2,3)}\dfrac{x^2y+1}{x^3y^2-2x}$. | $=\dfrac{(-2)^2(3)+1}{(-2)^3(3)^2-2(-2)}=\dfrac{13}{-68}=-\dfrac{13}{68}$ | sympy: 분자 $13$, 분모 $-68$, 값 $-13/68\approx-0.191176$ | ✅ | (4)의 응용; pdftotext에서 음부호가 소실되어 "13/68"로 보이나 PNG p-1031에서 $-\tfrac{13}{68}$ 확인 |
| 6 | 1031–1032 | 계산 + 증명 | Find $\lim_{(x,y)\to(0,0)}\dfrac{3x^2y}{x^2+y^2}$, once from the ε-δ definition and once by the Squeeze Theorem. | $=\mathbf 0$. 풀이 1: $\delta=\varepsilon/3$로 잡으면 $\left|\frac{3x^2y}{x^2+y^2}\right|\le3\sqrt{x^2+y^2}<3\delta=\varepsilon$. 풀이 2: $-3|y|\le\frac{3x^2y}{x^2+y^2}\le3|y|$이고 $\pm3|y|\to0$이므로 조임정리 | sympy: 극좌표 $3r\sin\theta\cos^2\theta\to0$; 부등식 $3|y|-\frac{3x^2|y|}{x^2+y^2}=\frac{3|y|^3}{x^2+y^2}\ge0$ 확인; $r=10^{-6}$ 원 위 최대 $|f|\approx1.15\times10^{-6}\le3r$ | ✅ | $\delta=\varepsilon/3$ 검증 완료 |
| 7 | 1032 | 개념 | Where is $\dfrac{x^2-y^2}{x^2+y^2}$ continuous? | 유리함수이므로 정의역에서 연속: $D=\{(x,y)\mid(x,y)\ne(0,0)\}$. 원점에서는 정의되지 않아 불연속 | 분모의 영점 집합 $\{(0,0)\}$ 확인 | ✅ | — |
| 8 | 1032 | 개념 | Is $g(x,y)=\dfrac{x^2-y^2}{x^2+y^2}$ for $(x,y)\ne(0,0)$, $g(0,0)=0$ continuous at the origin? | $g(0,0)$이 정의되어 있어도 예제 1에 의해 $\lim_{(x,y)\to(0,0)}g$가 존재하지 않으므로 **원점에서 불연속** | 예제 1의 경로 극한 재사용 | ✅ | — |
| 9 | 1033 | 개념 | Is $f(x,y)=\dfrac{3x^2y}{x^2+y^2}$ for $(x,y)\ne(0,0)$, $f(0,0)=0$ continuous? | 원점 밖에서는 유리함수라 연속이고, 예제 6에서 $\lim_{(x,y)\to(0,0)}f=0=f(0,0)$이므로 원점에서도 연속. 따라서 **$\mathbb R^2$ 전체에서 연속** | sympy: 극한 $0=f(0,0)$ | ✅ | Figure 8 |
| 10 | 1033 | 개념 | Where is $h(x,y)=e^{-(x^2+y^2)}$ continuous? | $f=x^2+y^2$는 $\mathbb R^2$에서 연속인 다항식, $g(t)=e^{-t}$는 $\mathbb R$에서 연속이므로 합성 $h=g\circ f$는 **$\mathbb R^2$ 전체에서 연속** | 합성 논증 확인 | ✅ | Figure 9 (종 모양 곡면) |
| 11 | 1033–1034 | 개념 | Where is $h(x,y)=\arctan(y/x)$ continuous? | $f=y/x$는 $x=0$을 뺀 곳에서 연속인 유리함수, $\arctan$은 어디서나 연속. 따라서 $h$는 $\{(x,y)\mid x\ne0\}$에서 연속이고 **직선 $x=0$에서 불연속** | sympy: $(0,1)$ 근처에서 $x\to0^+$이면 $\pi/2$, $x\to0^-$이면 $-\pi/2$ (도약 불연속) | ✅ | Figure 10 (y축 위쪽에서 끊김) |

anchor 스크립트: `/Users/chalrs/analysis/stewart/inventory/anchor-14.2.py` (절 도입 비교 + 예제 1–11 전부 재계산/검증). **불일치 0건.**

## C. 그림 필요 목록 (자체 SVG)

| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 1 | 화살표 그림: 원판 $D_\delta$ → 구간 $(L-\varepsilon,L+\varepsilon)$ | 필수 | 3 |
| Figure 2 | 곡면 $S$가 두 수평평면 $z=L\pm\varepsilon$ 사이에 놓이는 그림 | 선택 | 3 |
| Figure 3 | 점 $(a,b)$로 여러 방향에서 접근하는 경로들 | 필수 | 4 / 14 |
| Figure 4 | 예제 1: $x$축 위 $f=1$, $y$축 위 $f=-1$ | 필수 | 예제 1 / 14 |
| Figure 5 | 예제 2: 두 축 위 $f=0$, 직선 $y=x$ 위 $f=\tfrac12$ | 필수 | 예제 2 / 14 |
| Figure 6 | 예제 2 곡면 $\dfrac{xy}{x^2+y^2}$ — $y=x$ 위의 능선 | 선택 | 예제 2 |
| Figure 7 | 예제 3 곡면 $\dfrac{xy^2}{x^2+y^4}$ — 포물선 $x=y^2$ 위의 능선 | 선택 | 예제 3 |
| Figure 8, 9, 10 | 예제 9·10·11의 컴퓨터 렌더링 곡면 | 제외(선택) | 예제 9·10·11 |
| Table 1, Table 2 | 절 도입의 수치표(그림이 아니라 HTML 표로 재현) | 필수(표) | 1 |

## D. ERRATA·판독 불확실

- pdftotext 기호 손상은 §14.1과 동일 패턴(`s…d`=괄호, `−`=`=`, `2`=`−`, `1`=`+`, `.`=`>`, `,`=`<`). 특히 **음수 부호가 통째로 사라진다**: 예제 2의 "$f(x,y)\to 21$"은 실제로 $\to\tfrac12$, 예제 5의 "$-2\ 13/68$"은 실제로 $=-\tfrac{13}{68}$, 예제 1의 "$f\to 21$"은 $\to-1$. PNG p-1027, p-1029, p-1031로 모두 대조·복원했다.
- Definition 1과 (7)의 $\delta$ 기호는 텍스트에서 공백으로 빠져 있으나 PNG p-1027에서 $\delta$ 확인.
- 예제 3의 직선 제한식은 PNG에서 $f(x,mx)=\dfrac{x(mx)^2}{x^2+(mx)^4}=\dfrac{m^2x^3}{x^2+m^4x^4}=\dfrac{m^2x}{1+m^4x^2}$ 확인.
- 그 밖의 판독 불확실 항목 없음. 교재 답의 오류는 발견되지 않았다.

## E. 절 요약 (사이트 도입 note 초안)

이변수함수의 극한 $\lim_{(x,y)\to(a,b)}f(x,y)=L$을 ε-δ로 정의하고, 일변수와 결정적으로 다른 점을 다룬다. 평면에서는 $(a,b)$로 접근하는 경로가 무한히 많고 정의는 거리만 요구하므로, 극한이 존재하려면 **모든** 경로에서 같은 값이 나와야 한다. 따라서 서로 다른 두 경로에서 다른 값이 나오면 극한이 없다고 결론지을 수 있으며(예제 1–3), 원점을 지나는 모든 직선에서 같은 값이 나와도 극한의 존재가 보장되지 않는다는 점이 예제 3의 교훈이다. 극한의 존재를 보일 때는 극한 법칙과 다항·유리함수의 직접대입, 그리고 ε-δ 정의나 조임정리로 크기를 눌러 잡는 방법을 쓴다. 연속은 "직접대입이 통한다"는 성질로 정의되며, 다항식·유리함수·연속함수의 합성이 모두 연속임을 확인한 뒤 같은 개념을 $\mathbb R^n$으로 확장한다.

## F. 공통과제 문항

- 과제 제출 문항: **23, 30, 31, 49, 53**
- 학습 참고 문항: **19–30, 31–34, 51–53, 57**(57은 "포함 여부 결정"으로 표기됨)

※ `$S/stewart/sec/s14.2.txt`는 PDF p.1035(연습문제 1–44)까지만 담고 있고, 45–57번은 PDF p.1036(= `s14.3.txt` 첫 쪽)에 이어진다.
