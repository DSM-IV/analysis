# §16.1 Vector Fields — PDF p.1199–1205 (인쇄 p.1162–1168)

## A. 카드 인벤토리 (원문 순서)
| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | note | (절 도입, ■ Vector Fields in $\mathbb R^2$ and $\mathbb R^3$) | 벡터장의 실제 예 / Examples of Vector Fields | 샌프란시스코만 상공 10 m 풍속 벡터(Fig 1), 노바스코샤 해류·경사 익형 주위 기류(Fig 2)는 각 점에 속도벡터를 대응시킨 **속도장**; 각 점에 힘벡터를 대응시키면 **힘장**(예: 중력장) | 1199 | — | — |
| 2 | def | Definition 1 | $\mathbb R^2$ 위의 벡터장 / Vector Field on $\mathbb R^2$ | 평면영역 $D\subseteq\mathbb R^2$의 각 점 $(x,y)$에 2차원 벡터 $\mathbf F(x,y)$를 대응시키는 함수 | 1200 | — | Fig 3 |
| 3 | note | (Figure 3 본문) | 벡터장 그리기와 성분함수 / Picturing a Field; Component Functions | 화살표 $\mathbf F(x,y)$를 시점 $(x,y)$에 놓아 대표점 몇 개만 그린다; $\mathbf F(x,y)=P(x,y)\,\mathbf i+Q(x,y)\,\mathbf j=\langle P(x,y),Q(x,y)\rangle$, 줄여서 $\mathbf F=P\,\mathbf i+Q\,\mathbf j$. $P,Q$는 **스칼라장** | 1200 | — | — |
| 4 | def | Definition 2 | $\mathbb R^3$ 위의 벡터장 / Vector Field on $\mathbb R^3$ | $E\subseteq\mathbb R^3$의 각 점 $(x,y,z)$에 3차원 벡터를 대응; $\mathbf F=P\,\mathbf i+Q\,\mathbf j+R\,\mathbf k$. §13.1의 벡터함수처럼 연속성을 정의하며, $\mathbf F$ 연속 $\iff$ $P,Q,R$ 모두 연속 | 1200 | — | Fig 4 |
| 5 | rem | (본문 표기 단락) | 위치벡터 표기 $\mathbf F(\mathbf x)$ / Position-Vector Notation | 점 $(x,y,z)$를 위치벡터 $\mathbf x=\langle x,y,z\rangle$와 동일시하여 $\mathbf F(x,y,z)$ 대신 $\mathbf F(\mathbf x)$로 쓴다 — 벡터에 벡터를 대응시키는 함수 | 1200 | — | — |
| 6 | note | (Figures 6–12 본문) | 컴퓨터로 그린 벡터장 읽기 / Reading Computer Plots | 소프트웨어는 화살표 길이를 실제 크기에 비례하되 겹치지 않게 축소해 그린다; Fig 11은 $y$성분이 항상 $-2$라 전체가 $-y$ 방향으로 쏠리고, Fig 12를 속도장으로 보면 입자가 위에서 볼 때 시계방향으로 $z$축을 감으며 상승 | 1201–1202 | — | — |
| 7 | note | (Examples 4–5 본문) | 힘장: 중력장과 전기장 / Force Fields: Gravitational and Electric | 역제곱 법칙형 힘장. 중력장 (3) $\mathbf F(\mathbf x)=-\dfrac{mMG}{|\mathbf x|^3}\mathbf x$, 쿨롱 힘 (4) $\mathbf F(\mathbf x)=\dfrac{\varepsilon qQ}{|\mathbf x|^3}\mathbf x$ ($qQ>0$ 척력, $qQ<0$ 인력), 단위전하당 힘인 **전기장** $\mathbf E(\mathbf x)=\frac1q\mathbf F(\mathbf x)=\dfrac{\varepsilon Q}{|\mathbf x|^3}\mathbf x$ | 1202–1203 | — | Fig 14 |
| 8 | note | ■ Gradient Fields | 기울기 벡터장 / Gradient Vector Fields | 스칼라함수 $f$의 기울기 $\nabla f(x,y)=f_x(x,y)\,\mathbf i+f_y(x,y)\,\mathbf j$ (3변수는 $\nabla f=f_x\mathbf i+f_y\mathbf j+f_z\mathbf k$)는 그 자체로 벡터장이며 이를 **기울기 벡터장**이라 한다. §14.6에 따라 $\nabla f$는 등위곡선에 수직이고, 등위곡선이 촘촘한(경사가 급한) 곳에서 길다 | 1203–1204 | — | Fig 15 |
| 9 | def | (본문 정의문, 굵은 글씨) | 보존적 벡터장과 퍼텐셜 함수 / Conservative Vector Field, Potential Function | 어떤 스칼라함수 $f$가 있어 $\mathbf F=\nabla f$이면 $\mathbf F$를 **보존적 벡터장**, $f$를 $\mathbf F$의 **퍼텐셜 함수**라 한다. 모든 벡터장이 보존적인 것은 아니다 (판정법은 §16.3, §16.5) | 1204 | — | — |
| 10 | rem | (Example 4 후속 검증) | 중력장은 보존적 / The Gravitational Field Is Conservative | $f(x,y,z)=\dfrac{mMG}{\sqrt{x^2+y^2+z^2}}$로 두면 $\nabla f=\mathbf F$ — 예제 4의 중력장은 이 $f$를 퍼텐셜로 갖는 보존장 | 1204 | 직접 계산 | — |
| 11 | fig | Figure 5 | $\mathbf F(x,y)=-y\,\mathbf i+x\,\mathbf j$의 손그림 / Hand Sketch of $\langle -y,x\rangle$ | 대표점 표의 12개 벡터를 시점에 붙여 그린 반시계 회전장 | 1200 | — | 필수 |
| 12 | fig | Figure 15 | 기울기장과 등위곡선 / Gradient Field over a Contour Map | $f(x,y)=x^2y-y^3$의 등위곡선 위에 $\nabla f$를 겹쳐 그려 수직성·길이 관계를 보임 | 1204 | — | 필수 |

## B. 예제 기준값
| Example | PDF 쪽 | 유형 | 문제 요지 (영어 재서술) | 교재 최종답 (TeX) | 독립 재계산 | 일치 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 1200–1201 | 스케치·그래프 | Draw representative arrows for the planar field $\mathbf F(x,y)=-y\,\mathbf i+x\,\mathbf j$ and identify the geometric pattern they form. | 그래프형 — 서술 답: 모든 화살표가 원점 중심의 원에 접한다. 근거 $\mathbf x\cdot\mathbf F(\mathbf x)=(x\mathbf i+y\mathbf j)\cdot(-y\mathbf i+x\mathbf j)=-xy+yx=0$이고 $|\mathbf F(x,y)|=\sqrt{(-y)^2+x^2}=\sqrt{x^2+y^2}=|\mathbf x|$ (원의 반지름과 같은 크기, 반시계 방향 회전장) | sympy: $\mathbf x\cdot\mathbf F=0$, $|\mathbf F|^2-|\mathbf x|^2=0$; 표의 12개 대표값 전부 재현 | ✔ | — |
| 2 | 1201 | 스케치·그래프 | Sketch the space field $\mathbf F(x,y,z)=z\,\mathbf k$. | 그래프형 — 서술 답: 모든 벡터가 연직($\mathbf k$ 방향)이며 $xy$평면 위($z>0$)에서는 위쪽, 아래($z<0$)에서는 아래쪽을 향하고, 크기 $|z|$는 $xy$평면에서 멀어질수록 커진다 | — (스케치형) | — | — |
| 3 | 1202 | 개념 | Interpret the steady velocity $\mathbf V(x,y,z)$ of fluid in a pipe as a vector field. | $\mathbf V$는 정의역 $E$(관 내부)에서 정의된 $\mathbb R^3$의 벡터장 = **속도장**이며, 화살표 길이가 그 점의 속력을 나타낸다. 예제 1의 장은 바퀴의 반시계 회전 속도장으로 볼 수 있다 | — (개념형) | — | — |
| 4 | 1202–1203 | 해석·응용 | Using Newton's law of gravitation, write the gravitational force field produced by a mass $M$ at the origin acting on mass $m$ at $\mathbf x$, in vector and component form. | (3) $\mathbf F(\mathbf x)=-\dfrac{mMG}{\lvert\mathbf x\rvert^{3}}\,\mathbf x$; 성분형 $\mathbf F(x,y,z)=\dfrac{-mMGx}{(x^2+y^2+z^2)^{3/2}}\mathbf i+\dfrac{-mMGy}{(x^2+y^2+z^2)^{3/2}}\mathbf j+\dfrac{-mMGz}{(x^2+y^2+z^2)^{3/2}}\mathbf k$ | sympy: $\lvert\mathbf F\rvert=mMG/r^{2}$ 확인, 성분형 $=-\dfrac{mMG}{\lvert\mathbf x\rvert^3}\mathbf x$ 확인 | ✔ | 물리학에서는 $\mathbf r$ 표기로 $\mathbf F=-(mMG/r^3)\mathbf r$ |
| 5 | 1203 | 해석·응용 | Using Coulomb's law, write the electric force a charge $Q$ at the origin exerts on a charge $q$ at $\mathbf x$, and the resulting electric field (force per unit charge). | (4) $\mathbf F(\mathbf x)=\dfrac{\varepsilon qQ}{\lvert\mathbf x\rvert^{3}}\,\mathbf x$ ($qQ>0$ 척력, $qQ<0$ 인력); $\mathbf E(\mathbf x)=\dfrac1q\mathbf F(\mathbf x)=\dfrac{\varepsilon Q}{\lvert\mathbf x\rvert^{3}}\,\mathbf x$ | sympy: $\lvert\mathbf F\rvert=\varepsilon\lvert qQ\rvert/r^2$ 확인 | ✔ | 식 (3)과 (4)의 형태가 같음(둘 다 역제곱 힘장) |
| 6 | 1204 | 계산 | For $f(x,y)=x^{2}y-y^{3}$, find $\nabla f$ and describe its relation to the contour map of $f$. | $\nabla f(x,y)=2xy\,\mathbf i+(x^{2}-3y^{2})\,\mathbf j$; 기울기 벡터는 등위곡선에 수직이고 등위곡선이 촘촘한 곳에서 길다 | sympy: $\nabla f=(2xy,\;x^2-3y^2)$ | ✔ | — |

## C. 그림 필요 목록 (자체 SVG)
| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| Figure 5 | $\mathbf F(x,y)=-y\,\mathbf i+x\,\mathbf j$: $(\pm1,0),(0,\pm1),(\pm2,\pm2),(\pm3,0),(0,\pm3)$ 등에서의 화살표 — 원점 중심 원에 접하는 반시계 회전장 | 필수 | 11 (예제 1) |
| Figure 15 | $f(x,y)=x^{2}y-y^{3}$의 등위곡선 + $\nabla f$ 화살표 격자 (수직성, 촘촘한 곳에서 긴 화살표) | 필수 | 12 (예제 6) |
| Figure 3 / 4 | 벡터장 도시 개념도($\mathbf F(x,y)$를 $(x,y)$에 붙여 그림) | 선택 | 2, 4 |
| Figure 9 | $\mathbf F=z\,\mathbf k$ 3차원 스케치 | 선택 | 예제 2 |
| Figure 14 | 중력장(원점을 향하는 화살표, 원점에서 멀수록 짧음) | 선택 | 7 |
| Figures 1, 2, 6–8, 10–13 | 실사 사진·컴퓨터 플롯 | 제외(재현 불필요) | — |

## D. ERRATA·판독 불확실
- 없음. (pdftotext에서 `−`=`=`/`∂`, `1`=`+`, `2`=`−`, `s…d`=`(…)`, `k…l`=`⟨…⟩`, `y`=`/`, `=`=`∇`로 글리프가 치환되어 나오지만 PNG p‑1200~p‑1204로 전부 대조 확인함.)

## E. 절 요약 (사이트 도입 note 초안)
벡터장은 평면 또는 공간의 각 점에 벡터 하나를 대응시키는 함수로, 바람·해류의 속도장과 중력·전기력 같은 힘장이 대표적인 예다. 성분함수로 쓰면 $\mathbf F=P\,\mathbf i+Q\,\mathbf j$ 또는 $\mathbf F=P\,\mathbf i+Q\,\mathbf j+R\,\mathbf k$이고, 각 성분이 연속일 때 벡터장이 연속이다. 벡터장을 이해하는 가장 좋은 방법은 대표점 몇 곳에서 $\mathbf F(x,y)$를 그 점에 시점을 두고 그려 보는 것으로, 예컨대 $\mathbf F=-y\,\mathbf i+x\,\mathbf j$는 원점 중심의 원에 접하는 반시계 회전장이 된다. 스칼라함수의 기울기 $\nabla f$는 그 자체가 벡터장(기울기 벡터장)이며, 등위곡선에 수직이고 경사가 급한 곳에서 길어진다. 어떤 벡터장이 스칼라함수의 기울기로 표현되면 이를 보존적 벡터장, 그 스칼라함수를 퍼텐셜 함수라 하는데, 중력장이 그 대표적인 예이고 보존성 판정법은 §16.3과 §16.5에서 다룬다.

## F. 공통과제 문항
- 3차 공통과제, 16.1 Vector Fields: **과제 제출 문항 없음 / 학습 참고 문항 없음** (공통과제 표에 단원명만 있고 문항 지정이 비어 있음).
