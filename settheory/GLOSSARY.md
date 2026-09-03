# 집합론 용어집 (Set Theory Glossary)

대한수학회 용어집 관행을 기본으로 한다 (Pinter, *A Book of Set Theory* 기반 강의노트).
번역·풀이 작성 시 이 표의 용어만 사용할 것.

**핵심 금칙·주의**
- **axiom of selection(1.10) = "분리공리"** (체르멜로의 Aussonderung). **"선택공리"는 axiom of choice(4.64) 전용** — 두 공리를 절대 혼동·혼용하지 말 것. 분리공리 첫 등장 시 "(axiom of selection)" 병기.
- class = **모임** ("클래스" 사용 금지), proper class = **고유모임** ("진모임"·"진클래스" 금지).
- sentence(2.1) = **명제** ("문장" 사용 금지 — 참·거짓이 정해지는 서술문이라는 정의에 맞는 표준 국내 용어).
- one-to-one correspondence = **일대일대응**, injective = **단사** ("일대일함수" 금지 — 일대일대응과 혼동 방지).
- 사람 이름: 칸토어(Cantor), 러셀(Russell), 베리(Berry), 체르멜로(Zermelo), 폰 노이만(Von Neumann), 유클리드(Euclid), 힐베르트(Hilbert), 드모르간(De Morgan).

## 문체 규칙
- 문제 서술: "-하라"체 (증명하라, 설명하라, 판정하라).
- **집합론 페이지의 증명/풀이 토글 규칙** (원문 증명 번역과 동일 형식으로 통일): 라벨("증명." / "풀이.") 없이 본문을 바로 시작한다. 증명형은 버튼 "증명 보기/증명 접기 · Proof/Hide Proof" + 끝에 `<div class="qed">□</div>`; 서술·판정·설명형은 버튼 "풀이 보기/풀이 접기 · Solution/Hide Solution" + qed 없음. prove-or-disprove는 증명형으로 취급(반례 포함, qed 있음).
- 수식·기호는 원문 LaTeX 그대로: $\in$, $\ni$("such that"으로 읽는 용법 포함), $\mathcal{U}$, $\mathcal{P}(A)$, $\hat{f}(C)$, $\check{f}(D)$, $\prod_{i\in I}A_i$, $2^A$, $\langle f,A,B\rangle$ 표기 변경 금지.
- 원문의 $\subset$/$\subsetneq$ 표기 관행(Remark 3.12 참조)을 그대로 유지 — $\subseteq$로 바꾸지 말 것.

## §1 역사적 서론·논리 기초
| English | 한국어 |
|---|---|
| paradox | 역설 |
| logical/semantic paradox | 논리적/의미론적 역설 |
| Russell's paradox | 러셀의 역설 |
| Berry's paradox | 베리의 역설 |
| the set of all sets | 모든 집합의 집합 |
| axiom / postulate | 공리 / 공준 |
| definition | 정의 |
| axiomatic method / axiomatic set theory | 공리적 방법 / 공리적 집합론 |
| Euclidean geometry / parallel postulate | 유클리드 기하학 / 평행선 공준 |
| undefined notion | 무정의 용어 |
| membership relation $\in$ | 소속 관계 |
| axiom of selection (Zermelo) | **분리공리** (axiom of selection) |
| the class axiom | 모임 공리 |
| formal language | 형식 언어 |
| statement / property | 명제(서술) / 성질 |

## §2 명제와 논리
| English | 한국어 |
|---|---|
| sentence | 명제 |
| negation $\neg P$ | 부정 |
| conjunction $P \wedge Q$ | 논리곱 |
| disjunction $P \vee Q$ | 논리합 |
| implication $P \implies Q$ | 함의 |
| premise | 전제 |
| converse / inverse / contrapositive | 역 / 이 / 대우 |
| truth table | 진리표 |
| true / false (t/f) | 참 / 거짓 |
| iff, if and only if | 필요충분조건(iff), "일 때 그리고 그럴 때만" — 문맥상 "$P \iff Q$"는 "$P$와 $Q$는 동치이다" |
| equivalent | 동치 |
| sufficient/necessary condition | 충분조건/필요조건 |
| idempotent law | 멱등법칙 |
| commutative law | 교환법칙 |
| associative law | 결합법칙 |
| distributive law | 분배법칙 |
| transitive law | 추이법칙 |
| "such that" ($\ni$) | "~를 만족하는"($\ni$) |

## §3 모임과 집합
| English | 한국어 |
|---|---|
| class | 모임 |
| set | 집합 |
| element | 원소 |
| proper class | 고유모임 |
| equal ($A=B$) | 같다(상등) |
| axiom of extent | 외연공리 |
| subclass / strict subclass | 부분모임 / 진부분모임 |
| subset / proper subset | 부분집합 / 진부분집합 |
| axiom of class construction | 모임 구성 공리 |
| intersection $A \cap B$ | 교모임(교집합) |
| union $A \cup B$ | 합모임(합집합) |
| universal class $\mathcal{U}$ | 보편모임 |
| empty class $\emptyset$ | 공모임 |
| empty set | 공집합 |
| disjoint | 서로소 |
| complement $A^c$ | 여모임(여집합) |
| Venn diagram | 벤 다이어그램 |
| absorption laws | 흡수법칙 |
| De Morgan's laws | 드모르간 법칙 |
| difference $A-B$ | 차모임(차집합) |
| singleton | 한원소모임 |
| unordered pair / doubleton | 비순서쌍 / 두원소모임(doubleton) |
| axiom of the empty set | 공집합 공리 |
| axiom of doubleton | 짝공리(axiom of doubleton) |
| axiom of subset | 부분집합 공리 |
| ordered pair $(a,b)$ | 순서쌍 |
| first/second component | 첫째/둘째 성분 |
| Cartesian product $A \times B$ | 데카르트 곱 |
| coordinate diagram | 좌표 다이어그램 |
| graph | 그래프 |
| inverse of a graph $G^{-1}$ | 역그래프 |
| composition of graphs $G \circ H$ | 그래프의 합성 |
| domain / range ($dom\ G$, $ran\ G$ — 원문이 수학 이탤릭; 전사·풀이 모두 이탤릭 유지, \operatorname 금지) | 정의역 / 치역 |
| index class / indexed family of classes $\{A_i\}_{i\in I}$ | 첨수모임 / 모임의 첨수족 |
| union/intersection of the classes $A_i$ | $A_i$들의 합모임/교모임 |
| generalized De Morgan's laws | 일반화된 드모르간 법칙 |
| generalized distributive laws | 일반화된 분배법칙 |
| union/intersection of $\mathscr{A}$ ($\bigcup\mathscr{A}$, $\bigcap\mathscr{A}$) | $\mathscr{A}$의 합모임/교모임 |
| axiom of union | 합집합 공리 |
| power set $\mathcal{P}(A)$ | 멱집합 |
| axiom of power set | 멱집합 공리 |

## §4 함수
| English | 한국어 |
|---|---|
| function / mapping | 함수 / 사상 |
| intuitive/formal definition | 직관적/형식적 정의 |
| codomain / target space | 공역 / 목표공간(target space) |
| image / pre-image | 상 / 원상 |
| $f$ maps $x$ onto $y$ ($x \mapsto y$) | $f$는 $x$를 $y$로 보낸다 |
| injective (INJ) | 단사 |
| surjective (SURJ) | 전사 |
| bijective | 전단사 |
| one-to-one correspondence | 일대일대응 |
| identity function $I_A$ | 항등함수 |
| constant function $K_b$ | 상수함수 |
| inclusion function $E_B$ | 포함함수 |
| characteristic function (indicator function) $C_B$ | 특성함수(지시함수) |
| restriction $f_{[C]}$ | 제한 |
| extension $f^{[C]}$ | 확장 |
| invertible | 가역 |
| inverse function $f^{-1}$ | 역함수 |
| left/right inverse | 왼쪽 역함수 / 오른쪽 역함수 |
| direct image $\hat{f}(C)$ | 직상 |
| inverse image $\check{f}(D)$ | 역상 |
| choice function | 선택함수 |
| axiom of choice | **선택공리** |
| product of a family of classes $\prod_{i\in I}A_i$ | 모임들의 족의 곱 |
| $j$-th coordinate / $j$-th projection $p_j$ | 제$j$좌표 / 제$j$사영 |
| $B^A$ (class of all functions from $A$ to $B$) | $A$에서 $B$로 가는 모든 함수의 모임 $B^A$ |
| axiom of replacement | 치환공리 |

## 단원명 (파일 ↔ 제목)
| 파일 | 한국어 제목 | English |
|---|---|---|
| ch01 | 1. 역사적 서론 | 1. Historical Introduction |
| ch02 | 2. 명제와 논리 | 2. Sentence and Logic |
| ch03 | 3. 모임과 집합 (i): 모임의 대수 | 3. Classes and Sets (i): The Algebra of Classes |
| ch04 | 3. 모임과 집합 (ii): 순서쌍·곱·그래프 | 3. Classes and Sets (ii): Ordered Pairs, Products, and Graphs |
| ch05 | 3. 모임과 집합 (iii): 첨수족과 멱집합 | 3. Classes and Sets (iii): Indexed Families and Power Sets |
| ch06 | 4. 함수 (i): 정의와 기본 성질 | 4. Functions (i): Definitions and Basic Properties |
| ch07 | 4. 함수 (ii): 합성과 역함수 | 4. Functions (ii): Composition and Inverses |
| ch08 | 4. 함수 (iii): 상·선택공리·곱 | 4. Functions (iii): Images, Choice, and Products |
