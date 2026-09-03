# 해석학2 SOURCE-MAP

소스: `[2026-08-28] Lecture note (해석학2).pdf` (리포 루트, 60쪽, 영문)
저자: Ildoo Kim (Korea University). 교재 기반: W. Rudin, *Principles of Mathematical Analysis* (McGraw-Hill).
**소스가 영문** → en-formal = verbatim 전사, ko-formal = 번역. 컨벤션은 `settheory/`와 동일 (settheory/ch01.html의 컨벤션 주석 참조).
**학기 중 갱신되는 자료** — §3은 이제 막 시작(9개 환경). 갱신 PDF가 오면 아래 인벤토리와 diff하여 증분 추가. 환경 번호(N.M) = 카드 번호.

## 전체 구조

| 섹션 | 제목 | PDF 페이지 | 환경 수 | Exercise |
|---|---|---|---|---|
| §1 | Differentiation | 1–24 | 73 | 30 |
| §2 | The Riemann-Stieltjes integral | 25–55 | 65 | 23 |
| §3 | Sequence and series of functions (진행 중) | 56–60 | 9 | 2 |
| 계 | | 60쪽 | **147** | **55** |

§1은 3분할, §2는 3분할, §3은 1페이지 → **7페이지(ch01–ch07)**. 이후 학기 진행에 따라 ch07 확장 또는 ch08+ 추가.

## 환경 유형 → 카드 클래스 (settheory와 동일)

def-card(Definition/Notation), thm-card(Theorem/Lemma/Corollary), rem-card(Remark), exam-card(Example), ex-card(Exercise, PROOF 마커), note-card(무번호 서술). 원문 Proof는 en verbatim + ko 번역으로 토글(라벨 없이 시작, qed □).

## 그림 (SVG 재현 필요, ch01)

- p6 Def 1.28 각의 정의: 원 + 두 선분 + 호 ℓ (흑백, 손그림풍 호 표시)
- p7 단위원: P(cos θ, sin θ) 청색 점·선분, θ 분홍 호살표, O·1 라벨 — 원본 색상 재현

## Difficult 표시 문항 (풀이 단계에서 Opus 에스컬레이션 대상)

- Ex 1.23 **(Difficult!)**: 닫힌구간 연속성 정의가 왜 나쁜지 설명
- Ex 1.29 (Difficult(?)): (cos x)' = -sin x, (sin x)' = cos x 증명 (각의 길이 정의로부터)
- Ex 1.33 (Difficult(?)): 유리수 p에 대해 x^p 미분

## ERRATA / 역주 후보 (en verbatim 유지, 풀이·역주에서 처리)

1. Thm 1.44(iii) "for all x **=** (a, b)" — $x \in (a,b)$의 오타.
2. Lemma 1.65 "there **exist exists** a c ∈ (a,b)" — 중복 오타.
3. Example 2.7 "if x is **a** irrational number"; Example 2.8 "there exist **a** i₀"; Remark 2.3 "be **an another** partition"; Thm 2.37 증명 끝 "We **left** the proof of (iii), (iv), and (v) as an exercise." — 문법 오류 verbatim.
4. Def 2.1 분할 정의가 ≤(비강한 부등호) 사용 — 통상 정의와 다르나 verbatim.
5. Taylor(1.73) 증명의 $(\alpha-\alpha)^{n-k}$ 항 — 인쇄된 그대로(값 0) 유지.
6. Ex 2.60 앵커: RS 적분가능 ⇒ 유계? **반증** — α가 상수함수이면 임의의(무계 포함) f에 대해 U=L=0으로 적분가능. Def 2.11은 "bounded f"를 가정하지만 Def 2.12의 적분가능성 자체는 상·하적분 존재·상등만 요구.
7. §3 미완(학기 진행 중). References는 마지막 note-card로 (Rudin 서지만; 학과 주소·이메일은 게시하지 않음 — settheory와 동일).
8. Ex 1.16/1.19의 "(i)"는 항목 라벨(문항이 (i),(ii)… 항목으로 구성) — 괄호 이름 아님.
9. **빌드 단계 확정 원문 오류 (verbatim 전사됨)**: Thm 2.15 증명 `(j = 1, \ldots, k\}` 괄호-중괄호 불일치; Thm 2.20(iii) 증명 "Recall that $P=\{x_1,\ldots,x_n\}$"($x_0$이어야 함); Thm 2.24 증명 끝 "$\cap D$"(문맥상 $[a,b]$); Exam 2.8 상적분 구간 $\overline{\int_a^b}$(문맥상 $[0,1]$); Lemma 2.49 증명 $\sup_{x\in[a,,b]}$ 이중 쉼표; Cor 2.58 증명 $(y\in[a,b])$($[A,B]$이어야 함); Thm 1.55 증명이 극소 상황에 "Theorem 1.37"(극대 정리) 인용; Rem 1.49 "has a infimum", Def 1.48 "an lower bound" 등 관사 오류 다수; Thm 2.40/2.42 "a bounded functions"/"integrable functions" 수일치 오류; **Exam 1.34(ii) "f is differentiable x = 0 and $f'(x) = 0$"**(문맥상 $f'(0) = 0$ — 바로 뒤 계산이 $\lim_{t\to0}\frac{f(t)-f(0)}{t-0}$이다; ch01 감사에서 확인, en·ko 모두 원문대로 $f'(x) = 0$ 유지).
10. ﬀ/ﬃ 리거처는 전 챕터에서 평문으로 정규화(sufficient/difficult) — 코드포인트 충실성보다 렌더 동일성 우선(집합론과 동일 정책).
12. **§3 원문 오류 (verbatim 전사됨, 풀이·역주 후보)**: Def 3.1 ",or" 붙임; Exam 3.5/3.6 "since $f$ is continuous"($f_n$이어야 함), Exam 3.6 "on $[a,b]$"($[0,1]$); **Exam 3.6의 로피탈 사슬에 Exam 3.5의 2가 복사됨**(1이어야 함) + 불필요한 선행 마이너스; Thm 3.9 진술 "$f_n \to f$ converges to $f$" 중복, 증명 "such that … such that" 중복; §3에서만 "L'Hôpital"(곡절 악센트) 표기 — §1의 "L'Hospital"과 원문 내 불일치.
13. [향후 손질] ch01 Def 1.17 ko가 점에서의 값 $f'(x)$를 "도함수"로 옮김(원문 "a derivative of f at x" 직역) — GLOSSARY·ch02~ch07은 점값을 "미분계수"로 씀. 페이지 단위 일괄 결정 필요(Ex 1.19의 좌·우 표기 연동).
11. note-card id는 `note{챕터}-{순번}` (ch04의 컨벤션 주석 예시 `note{페이지}`는 구식 표현 — id 실체는 note04-1).

## 챕터별 인벤토리 (번호 = 소스 환경 번호 = 카드 id)

### ch01.html — 1. Differentiation (i): Limits, Continuity, and the Derivative / 미분 (i): 극한·연속·도함수
- PDF pages 1–10, 환경 1.1–1.34, **카드 34개**, Exercise 14개: 1.8, 1.9, 1.10, 1.11, 1.13, 1.14, 1.16, 1.19, 1.22, 1.23, 1.29, 1.31, 1.32, 1.33
  - `1.1` Definition — p1
  - `1.2` Remark — p1
  - `1.3` Definition — p1
  - `1.4` Definition — p2
  - `1.5` Example — p2
  - `1.6` Definition — p2
  - `1.7` Remark — p2
  - `1.8` Exercise — p2
  - `1.9` Exercise — p2
  - `1.10` Exercise — p3
  - `1.11` Exercise — p3
  - `1.12` Theorem — p3
  - `1.13` Exercise — p3
  - `1.14` Exercise — p3
  - `1.15` Definition — p3
  - `1.16` Exercise — p3
  - `1.17` Definition — p3
  - `1.18` Remark — p4
  - `1.19` Exercise — p4
  - `1.20` Example — p4
  - `1.21` Theorem — p4
  - `1.22` Exercise — p5
  - `1.23` Exercise (Diﬀicult!) — p5
  - `1.24` Remark — p5
  - `1.25` Theorem — p5
  - `1.26` Definition — p6
  - `1.27` Corollary — p6
  - `1.28` Definition — p6
  - `1.29` Exercise (Diﬀicult(?) — p7
  - `1.30` Theorem (Chain Rule) — p7
  - `1.31` Exercise — p8
  - `1.32` Exercise — p8
  - `1.33` Exercise (Diﬀicult(?) — p8
  - `1.34` Example — p9

### ch02.html — 1. Differentiation (ii): The Mean-Value Theorems and Applications / 미분 (ii): 평균값 정리와 그 응용
- PDF pages 10–17, 환경 1.35–1.60, **카드 26개**, Exercise 11개: 1.36, 1.39, 1.45, 1.46, 1.47, 1.52, 1.54, 1.56, 1.58, 1.59, 1.60
  - `1.35` Definition — p10
  - `1.36` Exercise — p10
  - `1.37` Theorem — p10
  - `1.38` Corollary — p10
  - `1.39` Exercise — p11
  - `1.40` Theorem (Rolle’s theorem) — p11
  - `1.41` Theorem (Mean-value theorem) — p11
  - `1.42` Theorem (Cauchy’s mean-value theorem) — p12
  - `1.43` Definition — p12
  - `1.44` Theorem — p12
  - `1.45` Exercise — p13
  - `1.46` Exercise — p13
  - `1.47` Exercise — p13
  - `1.48` Definition — p13
  - `1.49` Remark — p13
  - `1.50` Lemma — p14
  - `1.51` Theorem (Intermediate value theorem) — p14
  - `1.52` Exercise — p15
  - `1.53` Lemma — p16
  - `1.54` Exercise — p16
  - `1.55` Theorem (Darboux Theorem) — p16
  - `1.56` Exercise — p17
  - `1.57` Corollary — p17
  - `1.58` Exercise — p17
  - `1.59` Exercise — p17
  - `1.60` Exercise — p17

### ch03.html — 1. Differentiation (iii): L'Hospital's Rule and Taylor's Theorem / 미분 (iii): 로피탈 법칙과 테일러 정리
- PDF pages 18–24, 환경 1.61–1.73, **카드 13개**, Exercise 5개: 1.62, 1.63, 1.66, 1.67, 1.69
  - `1.61` Definition — p18
  - `1.62` Exercise — p18
  - `1.63` Exercise — p18
  - `1.64` Remark — p18
  - `1.65` Lemma — p19
  - `1.66` Exercise — p20
  - `1.67` Exercise — p20
  - `1.68` Theorem (L’Hospital’s rule) — p20
  - `1.69` Exercise — p21
  - `1.70` Definition — p21
  - `1.71` Theorem (A generalization of the mean-value theorem) — p22
  - `1.72` Corollary — p23
  - `1.73` Theorem (Taylor’s theorem) — p24

### ch04.html — 2. The Riemann-Stieltjes Integral (i): Definitions and the Integrability Criterion / 리만-스틸체스 적분 (i): 정의와 적분가능성 판정
- PDF pages 25–36, 환경 2.1–2.25, **카드 25개**, Exercise 5개: 2.9, 2.10, 2.17, 2.22, 2.25
  - `2.1` Definition — p25
  - `2.2` Remark — p26
  - `2.3` Remark — p26
  - `2.4` Theorem — p26
  - `2.5` Corollary — p27
  - `2.6` Definition (The Riemann integral) — p27
  - `2.7` Example — p27
  - `2.8` Example — p28
  - `2.9` Exercise — p29
  - `2.10` Exercise — p29
  - `2.11` Definition — p29
  - `2.12` Definition — p29
  - `2.13` Remark — p30
  - `2.14` Definition — p30
  - `2.15` Theorem — p30
  - `2.16` Corollary — p31
  - `2.17` Exercise — p31
  - `2.18` Corollary — p31
  - `2.19` Theorem — p32
  - `2.20` Theorem — p33
  - `2.21` Definition — p34
  - `2.22` Exercise — p34
  - `2.23` Remark — p34
  - `2.24` Theorem — p35
  - `2.25` Exercise — p36

### ch05.html — 2. The Riemann-Stieltjes Integral (ii): Integrable Functions and Algebraic Properties / 리만-스틸체스 적분 (ii): 적분가능 함수와 연산
- PDF pages 36–46, 환경 2.26–2.43, **카드 18개**, Exercise 9개: 2.28, 2.30, 2.33, 2.34, 2.36, 2.38, 2.39, 2.41, 2.43
  - `2.26` Theorem — p36
  - `2.27` Theorem — p37
  - `2.28` Exercise — p38
  - `2.29` Corollary — p38
  - `2.30` Exercise — p38
  - `2.31` Lemma — p38
  - `2.32` Theorem — p39
  - `2.33` Exercise — p40
  - `2.34` Exercise — p40
  - `2.35` Theorem — p41
  - `2.36` Exercise — p42
  - `2.37` Theorem — p42
  - `2.38` Exercise — p45
  - `2.39` Exercise (Linear property of the Riemann-Stieltjes integral) — p45
  - `2.40` Theorem — p45
  - `2.41` Exercise — p46
  - `2.42` Theorem — p46
  - `2.43` Exercise — p46

### ch06.html — 2. The Riemann-Stieltjes Integral (iii): Step Functions, Change of Variable, and the FTC / 리만-스틸체스 적분 (iii): 계단함수·변수변환·미적분학의 기본정리
- PDF pages 46–56, 환경 2.44–2.65, **카드 22개**, Exercise 9개: 2.46, 2.50, 2.51, 2.52, 2.55, 2.56, 2.60, 2.62, 2.63
  - `2.44` Definition — p46
  - `2.45` Theorem — p47
  - `2.46` Exercise — p48
  - `2.47` Theorem — p49
  - `2.48` Lemma — p50
  - `2.49` Lemma — p50
  - `2.50` Exercise — p52
  - `2.51` Exercise — p52
  - `2.52` Exercise — p52
  - `2.53` Theorem — p52
  - `2.54` Corollary — p52
  - `2.55` Exercise — p52
  - `2.56` Exercise — p52
  - `2.57` Theorem — p52
  - `2.58` Corollary (Change of variable) — p54
  - `2.59` Theorem — p54
  - `2.60` Exercise — p54
  - `2.61` Theorem — p54
  - `2.62` Exercise — p55
  - `2.63` Exercise — p55
  - `2.64` Theorem (The fundamental theorem of calculus) — p55
  - `2.65` Theorem (Integration by parts) — p56

### ch07.html — 3. Sequence and Series of Functions / 함수열과 함수급수
- PDF pages 56–60, 환경 3.1–3.9, **카드 9개**, Exercise 2개: 3.4, 3.8
  - `3.1` Definition — p56
  - `3.2` Example — p57
  - `3.3` Example — p58
  - `3.4` Exercise — p58
  - `3.5` Example — p58
  - `3.6` Example — p59
  - `3.7` Definition — p60
  - `3.8` Exercise — p60
  - `3.9` Theorem — p60
