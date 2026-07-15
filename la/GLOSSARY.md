# 선형대수학 용어집 (Linear Algebra Glossary)

Friedberg-Insel-Spence 『Linear Algebra』 한국어판 관행을 따른다.
번역·해설 작성 시 이 표의 용어만 사용할 것. (일차결합/일차독립 계열 — "선형결합/선형독립" 사용 금지. 단, transformation은 "선형변환".)

## 문체 규칙
- 문제 서술: "-하라"체. (증명하라, 구하라, 판정하라, 보여라 대신 "보여라" → "증명하라"/"보이라" 중 **증명하라** 사용)
- 증명: "**증명.**"으로 시작, $\square$로 종료. 계산 풀이는 "**풀이.**"로 시작.
- 수식·기호는 원문 LaTeX 그대로 유지. $M_{m\times n}(F)$, $P_n(F)$, $\mathcal{F}(S,F)$, $\mathcal{L}(V,W)$ 표기 변경 금지.

## 기본 대수 구조
| English | 한국어 |
|---|---|
| vector space | 벡터공간 |
| field | 체 |
| scalar (multiplication) | 스칼라 (곱) |
| subspace | 부분공간 |
| zero vector / zero vector space | 영벡터 / 영벡터공간 |
| sum (of subsets) $S_1+S_2$ | 합 |
| direct sum $W_1 \oplus W_2$ | 직합 |
| coset $v+W$ | 잉여류 |
| quotient space $V/W$ | 몫공간 |
| even/odd function | 짝함수/홀함수 |

## 행렬 기초
| English | 한국어 |
|---|---|
| matrix / entry | 행렬 / 성분 |
| row / column | 행 / 열 |
| square matrix | 정사각행렬 |
| zero matrix $O$ | 영행렬 |
| identity matrix $I$ | 항등행렬 |
| transpose $A^t$ | 전치행렬 |
| trace $\operatorname{tr}(A)$ | 대각합 |
| symmetric / skew-symmetric | 대칭행렬 / 반대칭행렬 |
| (upper) triangular | (상)삼각행렬 |
| diagonal matrix | 대각행렬 |
| invertible / inverse | 가역 / 역행렬(역변환) |
| nilpotent | 멱영 |
| orthogonal matrix | 직교행렬 |
| unitary matrix | 유니타리 행렬 |
| submatrix | 부분행렬 |

## 생성·독립·기저
| English | 한국어 |
|---|---|
| linear combination | 일차결합 |
| span(S) / S generates V | 생성공간 $\operatorname{span}(S)$ / $S$가 $V$를 생성한다 |
| generating set | 생성집합 |
| linearly independent / dependent | 일차독립 / 일차종속 |
| basis / standard basis | 기저 / 표준기저 |
| ordered basis / standard ordered basis | 순서기저 / 표준순서기저 |
| dimension | 차원 |
| finite(infinite)-dimensional | 유한(무한)차원 |
| maximal element / chain | 극대원소 / 사슬 |
| Zorn's lemma | 초른 보조정리 (Zorn's lemma) |

## 선형변환
| English | 한국어 |
|---|---|
| linear transformation | 선형변환 |
| linear operator | 선형연산자 |
| identity/zero transformation | 항등변환/영변환 |
| null space (kernel) $\operatorname{Ker}T$ | 영공간(핵) |
| range (image) $\operatorname{Im}T$ | 상 |
| rank / nullity | 계수(rank) / 퇴화차수(nullity) |
| one-to-one (injective) / onto (surjective) | 단사 / 전사 |
| isomorphism / isomorphic | 동형사상 / 동형 |
| projection (on $W_1$ along $W_2$) | ($W_2$를 따라 $W_1$ 위로의) 사영 |
| $T$-invariant subspace | $T$-불변 부분공간 |
| restriction $T|_W$ | 제한 |
| additive | 가법적 |
| well-defined | 잘 정의된 |
| First Isomorphism Theorem | 제1동형정리 |
| matrix representation $[T]_\beta^\gamma$ | 행렬표현 |
| coordinate vector $[x]_\beta$ | 좌표벡터 |
| left-multiplication transformation $L_A$ | 왼쪽곱변환 $L_A$ |
| change of coordinates | 좌표변환 |
| similar matrices | 닮은 행렬 (닮음) |
| reflection / rotation | 반사 / 회전 |

## 쌍대공간
| English | 한국어 |
|---|---|
| linear functional | 선형범함수 |
| dual space $V^*$ / dual basis | 쌍대공간 / 쌍대기저 |
| double dual $V^{**}$ | 이중쌍대공간 |
| annihilator $S^\perp$ | 소멸자 |
| transpose of $T$ ($T^t$) | 전치사상 |

## 행렬연산·연립방정식
| English | 한국어 |
|---|---|
| elementary row/column operation | 기본행연산 / 기본열연산 |
| elementary matrix | 기본행렬 |
| rank of a matrix | 행렬의 계수(rank) |
| system of linear equations | 연립일차방정식 |
| coefficient matrix / augmented matrix | 계수행렬 / 첨가행렬 |
| homogeneous | 동차 |
| consistent | 해를 갖는 (consistent) |
| Gaussian elimination | 가우스 소거법 |
| (reduced) row echelon form | (기약)행사다리꼴 |
| equivalent (relation) | 동치 (관계) |
| reflexive / symmetric / transitive | 반사적 / 대칭적 / 추이적 |

## 행렬식
| English | 한국어 |
|---|---|
| determinant | 행렬식 |
| cofactor / cofactor expansion | 여인수 / 여인수전개 |
| classical adjoint $\operatorname{adj}(A)$ | 고전적 수반행렬 |
| Cramer's rule | 크라머 공식 |
| Vandermonde matrix | 방데르몽드 행렬 |
| Wronskian | 론스키안 |
| $n$-linear function | $n$중선형함수 |
| alternating | 교대적 (alternating) |
| parallelogram | 평행사변형 |

## 단원명 (파일 ↔ 제목)
| 파일 | 한국어 제목 | English |
|---|---|---|
| ch01 | 벡터공간 | Vector Space |
| ch02 | 생성과 일차독립 | Span and Linear Independence |
| ch03 | 기저와 차원 | Bases and Dimension |
| ch04 | 기저의 존재성 | Existence of a Basis |
| ch05 | 선형변환 | Linear Transformation |
| ch06 | 선형변환과 행렬 | Linear Transformation and Matrix |
| ch07 | 좌표변환 | Change of Coordinates |
| ch08 | 쌍대공간 | Dual Space |
| ch09 | 기본행렬연산 | Elementary Matrix Operation |
| ch10 | 연립일차방정식 | System of Linear Equations |
| ch11 | 행렬식의 정의 | Definition of Determinants |
| ch12 | 행렬식의 성질 | Properties of Determinants |
