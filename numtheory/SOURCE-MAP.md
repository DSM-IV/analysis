# 응용정수론 SOURCE-MAP

소스: `numtheory/src/2026_Lectue notes.pdf` (원본 `~/Desktop/26-2/응용정수론/`, 39쪽, **LaTeX 영문**, 2026-09-03 생성본 — 학기 중 갱신 예상)
저자: Choi do hoon (고려대, MATH463 Applications of Number Theory). 참고문헌: D. Burton, *Elementary Number Theory*, McGraw Hill, 2010 (§3 연분수는 Burton Ch.15 기반).
부속: `numtheory/src/응용정수론 OT.docx` — 시험 4회, **모든 시험 문제는 25분 연습시간 문제(= 노트의 Exercise)에서 출제** → Exercise 풀이가 핵심 산출물.

**소스가 영문** → en-formal = verbatim 전사, ko-formal = 번역. 컨벤션은 `analysis2/`와 동일(analysis2/ch01.html 규약 주석) + 아래 numtheory 고유 규칙.
**텍스트 추출 가능**(pdftotext) — 단 분수·연분수·근호·표는 추출 시 깨지므로 빌더는 반드시 PDF 페이지를 Read 도구로 **시각 대조**한다. 추출본: 빌드 시 `pdftotext -layout` 결과를 참고용으로만.
**학기 중 갱신되는 자료** — 갱신 PDF가 오면 아래 인벤토리와 diff하여 증분 추가. 환경 번호(N.M) = 카드 번호.

## 전체 구조 (2026-09-08 계획)

| 단원 | 제목 | 소스 절 | PDF 쪽 | 환경 | 연습문제 | ALGO | NOTE |
|---|---|---|---|---|---|---|---|
| ch01 | 유클리드 호제법과 디오판토스 방정식 | §1.1–1.3 | 2–6 | 13 | 7 | 3 | 8 |
| ch02 | 합동 산술과 법 n의 역원 | §1.4–1.5 | 6–12 | 23 (+REM 1) | 9 | 2 | 6 |
| ch03 | 일차합동식·중국인의 나머지 정리·오일러 φ·원시근 | §1.6–1.9 | 12–17 | 33 (+REM 2·3·4) | 15 | 1 | 7 |
| ch04 | 암호: 디피-헬만 키 교환과 RSA | §2 | 17–19 | 9 | 5 | 2 | 5 |
| ch05 | 유한 연분수 | §3.1 | 20–27 | 20 | 10 | 1 | 5 |
| ch06 | 무한 연분수와 최선의 근사 | §3.2 | 28–31 | 16 | 6 | 1 | 3 |
| ch07 | 큐비트와 게이트 | §4.1–4.4 | 31–36 | 16 | 10 | 0 | 8 |
| ch08 | 측정, 아다마르 게이트와 CNOT 게이트 | §4.5–4.6 | 36–39 | 9 | 5 | 0 | 5 |
| 계 | | | 39쪽 | **139 (+REM 4 = 143)** | **67** | **10** | **47** |

풀이 대상: Exercise 67 중 원문 풀이가 인쇄된 1.8·1.24·1.25를 뺀 **64문항**(1.13은 (2)만) + 원문 증명이 빈칸인 정리 **3.9·3.12·3.30**의 자체 증명 3건 = **67건**.

**진행 상태 (2026-09-08):** 빌드 8/8 · 번역 8/8 · 풀이 67/67 · Opus 적대적 검증 8/8 완료. 최종 수치: 카드 143(+ALGO 10, NOTE 47), 연습문제 67, 토글 ko 88 = en 88, qed 68, verify_structure 8/8 OK, MathJax 컴파일 5,148 세그먼트 0오류. 검증 단계 실질 수정: ch01 §1.3 서술 가정 오타(ERRATA 51), ch02 Example 1.15 (3)·Thm 1.16 (1)(47·48), ch03 CRT 알고리즘 3단계 $m_i$→$M_i$·Thm 1.60 홀수 소수(49), ch05 Thm 3.12 (3) 자체 증명 논증 보완·피보나치 $C_k$ 역전(52), ch06 note06-1 $[1;1,1,1,1,1]$(54)·Thm 3.29 부호(53)·Ex 3.24 귀납 가정 강화, ch07 측정 확률 0·1 뒤바뀜(50). ch04·ch08은 수정 없음(표기 3건 제외).

## 환경 유형 → 카드 클래스

def-card(Definition), thm-card(Theorem/Lemma/Corollary — 배지 THM/LEM/COR), rem-card(Remark — 원문의 별도 카운터 "Remark 1~4"), exam-card(Example), ex-card(Exercise, 마커), note-card(무번호 서술), **algo-card(알고리즘 박스 — numtheory 고유)**. 원문 Proof는 en verbatim + ko 번역으로 토글(라벨 없이 시작, qed □).

## numtheory 고유 규칙 (analysis2 규약에 추가)

1. **카드 id = 원문 환경 번호**: `c{장}-{번호}` (예: Theorem 1.37 → `id="c1-37"`, 배지 `THM 1.37`). 단원 파일(ch01–ch08)과 무관하게 원문 장 번호를 쓴다(analysis2와 동일).
   - 번호 충돌: Definition 3.1과 Theorem 3.1이 둘 다 존재 → `c3-1d`(DEF 3.1) / `c3-1t`(THM 3.1).
   - 원문의 "Remark 1."~"Remark 4."는 별도 카운터 → id `rem1`~`rem4`, 배지 `REM 1` 등, 제목에 src-ref 없음.
   - p7의 "Theorem 1.16 2)."는 새 정리가 아니라 **정리 1.16 (2)의 증명 표제** → c1-16의 en 증명 토글 첫 줄에 `<p><strong>Theorem 1.16 2).</strong></p>`로 verbatim.
2. **알고리즘 박스**(원문의 테두리 박스 10개) → `<div class="card algo-card" id="algo{단원2자리}-{순번}">`, 배지 `<span class="algo-num">ALGO</span>`, 제목 `<span class="algo-title">한국어 제목 <em>English Title</em></span>`. 본문은 2단(ko `[번역 예정]` / en verbatim): 박스 표제(`[The Euclidean Algorithm]`, `(Algorithm of RSA)`)는 제목으로 흡수, `<p><strong>Input :</strong> …</p>`, `<p><strong>Output :</strong> …</p>`, 단계는 `<ol>`(원문이 1. 2. 3.) 또는 `<p><strong>(a)</strong> …</p>`(원문이 (a)(b)(c)). 목차에 `ALGO` 항목으로 포함. 표제 없는 박스(p3–4 확장 유클리드, p8 거듭제곱, p18 DH, p19 RSA)는 편집 제목을 붙인다.
3. **원문 풀이가 인쇄된 Exercise**(1.8, 1.24, 1.25; 1.13은 (1)만): ex-card에 마커 대신 토글 — en `data-show="Solution" data-hide="Hide Solution"`에 원문 "Proof." 본문 verbatim(라벨 "Proof." 제외, 끝 □는 `<div class="qed">□</div>`), ko 토글 `풀이 보기/풀이 접기`에 `[번역 예정]`. **1.13**은 en 토글에 (1) verbatim 뒤 `<!-- PROOF-EN-PART2 -->`, ko 토글에 `[번역 예정]` 뒤 `<!-- PROOF-KO-PART2 -->` 마커를 두어 풀이 단계에서 (2)를 양 언어로 추가.
4. **증명이 빈칸인 정리**(3.9 "Proof. □", 3.12 "Proof. □", 3.30 "Proof. 추후 추가 □") → thm-card에 토글 없이 `<!-- PROOF-KO -->`/`<!-- PROOF-EN -->` 마커(la2 c2-25 방식). 풀이 단계에서 자체 증명(증명 보기/Proof + qed).
5. **빈칸 채우기 문제**(1.7, 1.23, 1.35, 4.2, 4.12): 원문의 네모 박스는 `$\boxed{\phantom{(A)}}$`가 아니라 라벨이 있으면 `$\boxed{\ (A)\ }$`, 없으면 `$\boxed{\qquad\qquad}$`로 전사. 따옴표(“ ”)는 원문대로.
6. **표**: 위수 표(Example 1.50), mod 7 거듭제곱 표(p16), 이산로그 표(Example 2.2), √2 근사분수 표(Example 3.32), 고전/양자 비교표(p32), 진리표(AND·OR·NOT, CNOT)는 `<div class="table-wrap"><table class="truth-table">…</table></div>`(settheory 마크업; caption은 en 쪽 원문 없으면 생략). 표는 **양 패널에 복제**(번역가는 ko 쪽 헤더 산문만 번역).
7. **그림**(원문 tikz): p34 AND 게이트·NOT 게이트 기호, p35 X·Z 게이트 회로, p38 아다마르 게이트 회로 → 인라인 SVG를 `<figure class="fig">…<figcaption>` 안에, **양 패널 복제**, `currentColor` 사용. NOT 게이트는 원문이 AND와 같은 D자 기호로 그렸으므로 **인쇄된 대로** 재현(ERRATA 참고). p37 측정 도식(v →Ω/measure→ …)은 `\xrightarrow[\text{measure}]{\Omega}`와 `\begin{array}`로 수식 전사.
8. 브라-켓: `|0\rangle`, `|1\rangle`, `\langle`, `\otimes`; 켤레전치 $\overline{A}^{T}$는 원문대로 `\overline{A}^{T}`; `\mathbb{Z}_{>0}`. gcd는 원문이 이탤릭 $gcd(a,b)$로 인쇄 → `\gcd(a,b)`로 정규화(lcm도 `\operatorname{lcm}`), $mod$ 이탤릭 → `\pmod{n}`이 아니라 원문 배치대로 `(\bmod n)` 즉 `a \equiv b \ (\bmod\ n)`. `power(x,N)`은 `\operatorname{power}(x,N)`.
9. 원문 오타·문법 오류는 en에 그대로(아래 ERRATA), ko는 바른 뜻. 정수론 관례상 "for some integer q" 류 `\text{}`는 ko 패널에서 한국어로.
10. 각주·참고문헌: p39 References는 ch08 마지막 note-card(서지만).
11. 원문 §번호 헤더는 `<div class="section-title"><h2>1.4 Modulo arithmetic · 합동 산술</h2></div>`로 단원 안에서 구분.

## ERRATA / 역주 후보 (en verbatim 유지, ko·풀이에서 처리)

1. Def 1.1 "different **form** zero" (from).
2. p3 §1.2 서술: "ax + by = c has an integral solution if and only if **c|(a, b)**" — 뜻은 $\gcd(a,b) \mid c$ (p4 §1.3에는 바르게 $\gcd(a,b)|c$). ko는 바른 뜻 + 역주.
3. p2·p3 "**Let** introduce …" (Let us) — 문법, verbatim.
4. Ex 1.13 원문 풀이: "we know that **4** = 172 × 500 − 20 × 4250" — 실제로 $172\cdot500 - 20\cdot4250 = 1000$. 일반해 $(500+5n,\,-4250-43n)$은 옳음. 역주.
5. Example 1.19 (5): "$3^40$"처럼 인쇄(윗첨자 중괄호 누락 → $3^{40}$). Def 1.26 "$a^{-}1(\bmod n)$" (→ $a^{-1}$). Example 1.63 "$3^{phi(101)}$" (→ $3^{\phi(101)}$). Example 1.50 (3) 표 헤더 "$2^n(\bmod 1)$" (→ mod 11). **빌드 결정(개정)**: 이런 깨진 윗첨자는 렌더가 틀어지므로 en에서도 정규화한다 — $3^{40}$, $a^{-1}$, $3^{\phi(101)}$, note02-3의 $10^{20}$(원문 `10^2 0`). 표 헤더 mod 1은 en 그대로(ko는 mod 11).
6. p8 거듭제곱 알고리즘 박스 Input: "$n, N \in \mathbb{Z}_{>0}$ and **$n \le 2$**" — verbatim, ko 역주. **검증 결정(ch02)**: 뜻은 법에 대한 조건 $n \ge 2$이다(출력 조건 $0 \le \operatorname{power}(x,N) \lt n$이 뜻을 가지려면 $n \ge 2$; Thm 1.32·1.37도 법에 $n \ge 2$를 요구). 지수 조건 $N \ge 2$로는 읽을 수 없다 — $N = 1$이 이 재귀의 기저 단계다.
7. Ex 1.25 원문 풀이: `= 2((2(power(2,42))²)²)²` 줄이 **두 번** 인쇄됨 — verbatim(중복 유지).
8. Thm 1.29 증명 마지막 줄 "$\gcd(a,n)=1$" 앞에 ⇔ 누락 — verbatim.
9. Thm 1.16 (2) "$(t-b)$ 등"은 문제 없음; (1) "$c \equiv d(\bmod\ n)$" 띄어쓰기 원문대로.
10. p13 CRT 알고리즘 박스: "$M_i = M_i$" (→ $M_i = M/m_i$), "$N_i \in Z$" (→ $\mathbb{Z}$), 3단계 "$x \equiv a_1N_1m_1 + \cdots + a_nN_nm_n(\bmod M)$" — 소문자 $m_i$는 $M_i$의 오타(인쇄된 식으로는 해가 나오지 않는다: Ex 1.42 (1)에서 $2\cdot2\cdot3+4\cdot1\cdot5+6\cdot1\cdot7 = 74 \not\equiv 6 \ (\bmod\ 7)$). ko 역주 필수(풀이는 바른 정의 사용).
11. Thm 1.39 증명은 "(Uniqueness)"만 — 존재성 증명 없음(알고리즘이 존재성). verbatim.
12. Thm 1.46 증명 "the number of the multiple of $p$ below $p^k$" 등 관사·수일치 오류 다수 — verbatim. 같은 증명의 범위 "$a$ $(1 \le a \le n)$"(두 곳)은 이 정리에 $n$이 등장하지 않으므로 $1 \le a \le p^k$의 오타 — en verbatim, ko는 바른 범위 + 역주.
13. **Thm 1.51 진술 미완**: "Let $a$ and $n$ be positive integers such that $\gcd(a,n)=1$." 에서 끝남. 증명 내용상 결론은 "$t$가 $a$의 법 $n$ 위수일 때, $a^m \equiv 1 \ (\bmod\ n) \iff t \mid m$". en verbatim, ko는 결론을 보충하고 역주.
14. Example 1.59 (2) "**Therefor** 2 is not a primitive root" — verbatim.
15. p16 "Then 3 and 5 are primitive **root** of modulo 7" — verbatim.
16. Ex 1.69 "such that $a$ invertible of mod 18" — verbatim.
17. p17 §2.1 "How can Alice and **Bod** establish"; p18 "it is not easy to **proof**"; Ex 2.5 "**Diffe-Helliman**"; p18 §2.2 "Rivest, **Shadmir**, and **Adeleman**" — verbatim.
18. p20 §3.1 첫 전개식 "$\frac{61}{41} = 4 + \frac{5}{14}$" — $\frac{61}{14}$의 오타. verbatim, ko 역주.
19. Def 3.1 / Thm 3.1 번호 충돌(카드 id `c3-1d`/`c3-1t`).
20. Thm 3.8 증명 "Assume that $k = m$ for $2 \le m \lt n$ theorem is true for $k = m$" — 문장 꼬임, verbatim.
21. **Thm 3.9 증명 빈칸**, **Thm 3.12 증명 빈칸**, **Thm 3.30 증명 "추후 추가"**(한국어) → 자체 증명(규칙 4). en 카드에는 증명 자리가 비어 있었음을 `<p><em>Note.</em> The proof is left blank in the notes; the proof below is ours.</p>`로 표시(풀이 단계에서).
22. p26 서술 "For example of theorem **15.8**" (Burton 정리 번호 참조) — verbatim. 같은 단락 "$(x,y) = (2\cdot250, 17\cdot250) = (500, 4250)$" — 부호 오류: $43\cdot2 - 5\cdot17 = 1$이므로 $(500, -4250)$. ko 역주.
23. p26 Cor 3.10 증명 "$d|L.H.S.$" — verbatim.
24. Ex 3.13 (*), 3.33 (2)(*), 3.34 (2)(*), 3.35 (*) — 별표는 난이도 표시(Difficult) → 풀이 단계 Opus 에스컬레이션 대상.
25. p28 연분수 계산 알고리즘 4단계 "If $\xi_m$, then set …" — "$\xi_m \neq 0$" 누락. verbatim, ko 역주.
26. Thm 3.28 진술 "Then $q_n \ge n$ when $n \ge 3$ if $x = [a_0;\cdots,a_m]$, then $n \le m$" — 문장 꼬임(뜻: $q_n \ge n$; 유한이면 $n \le m$ 범위). verbatim.
27. Thm 3.31 진술 "$m \lt n$ and $1 \le b \le q_m$ ($b \in \mathbb{Z}$)" — verbatim. Example 3.32 "**an** best approximation" — verbatim.
28. Ex 3.34 (1) "$\left|\sqrt{15} - \frac{q}{p}\right|$" — 분수가 $q/p$로 인쇄(힌트는 $p_n/q_n$). verbatim, 풀이는 $p/q$ 관례로 서술하고 역주.
29. Ex 3.24 진술 "Given recursive relations for $p_k$ and $q_k$ … such that $[a_0;\cdots,a_k] = p_k/q_k$." — 문장 미완(뜻: 점화식을 제시하고 증명하라). verbatim.
30. p33 "**Assumte** that $T$ : $true$ corresponds 1" — verbatim. Def 4.6 (1) 끝 "Simply," 미완 문장 — verbatim.
31. p34 OR 게이트 진리표 헤더 "$C(A \wedge B)$" — $A \vee B$의 오타. verbatim(표는 en 그대로, ko 표 헤더는 바르게 + 역주).
32. p34 NOT 게이트 그림이 AND와 같은 D자 기호 — 인쇄된 대로 SVG, 역주(표준 기호는 삼각형+버블).
33. Ex 4.16 "**Prove that** matrices corresponding the $X$ gate and $Z$ gate" — 문장 미완(뜻: 대응 행렬을 구하고 확인하라). verbatim.
34. Example 4.19: 두 번째 확률 "$((1+\sqrt2)/\sqrt6)^2$" — 두 번째는 $((1-\sqrt2)/\sqrt6)^2$이어야 함. verbatim, ko 역주.
35. p38·p39 "[Figure.1]~[Figure.4] in the Figure file" — **그림 파일 미제공**(노트에 없음). Ex 4.25는 그림 없이 CNOT·SWAP 기호의 표준 의미로 풀이하고 역주.
36. ﬀ/ﬁ 리거처는 평문으로 정규화(analysis2 정책).
37. Ex 3.13 공식 — 원문은 "$\cdots + 3p_1 + 2p_0 + p_0 + 1$"로 인쇄됨(텍스트 추출본에서 $p_0$ 하나가 빠져 처음엔 오류로 의심했으나 빌더가 250dpi로 확인). $p_0 = 1$이므로 상수 합이 2가 되어 **공식은 옳다**($n=3$: $3\cdot10+3\cdot3+2\cdot1+1+1 = 43$). 증명: $p_k + p_{k-1} = (k+1)p_{k-1} + (p_{k-1}+p_{k-2})$를 반복하면 끝에 $p_0 + p_{-1} = p_0 + 1$. (*) 난이도 표시는 유지.
38. **Example 1.63 (1) 계산 오류**: "$3^5 \equiv 243 \equiv 38 \ (\bmod\ 101)$" — $243 - 2\cdot101 = 41$이므로 $3^{205} \equiv 41 \ (\bmod\ 101)$. en verbatim, ko 역주.
39. Thm 3.28 증명 display "$q_n = a_n q_{-1} + q_{n-2} \ge a_n q_{n-1} + 1 \le q_{n-1} + 1$" — 첨자 $q_{-1}$은 $q_{n-1}$의 오타이고 $\ge \cdots \le$ 사슬도 비정합(뜻: $q_n = a_nq_{n-1}+q_{n-2} \ge q_{n-1} + 1$). en verbatim, ko는 바른 부등식 + 역주.
40. Thm 3.29 증명 다섯째 줄 "$\frac{p_{n-2}}{q_{n-1}}$" — $q_{n-2}$의 오타. en verbatim, ko 역주.
41. p28 note06-1 "$[1;1;1;1;2] = [1;1,1,1,1]$" — 왼쪽 기호의 세미콜론은 쉼표의 오타. en verbatim, ko는 $[1;1,1,1,2]$.
42. Def 4.6 (1) 전개식에 여는 괄호 하나 누락: "$(a|0\rangle + b|1\rangle) \otimes c|0\rangle + d|1\rangle) = \cdots$" — en verbatim, ko는 $\otimes (c|0\rangle + d|1\rangle)$. p34 "”And gate”"류 따옴표(양쪽 닫는 따옴표)와 Ex 4.2의 닫는 따옴표 누락은 en 인쇄대로.
43. Lemma 3.11 증명 display "$q_{m+1} = a_m q_m + a_{m-1} \gt a_{m+1} q_m \ge 1 \cdot q_m = q_m$" — 첨자 오류: $q_{m+1} = a_{m+1}q_m + q_{m-1} \ge a_{m+1} q_m \ge q_m$이어야 함. en verbatim, ko 바른 식 + 역주.
44. Thm 1.46 증명 "$p, 2p, \cdots, p^{k-1}p = p^{k-1}$" — 마지막 배수는 $p^k$(개수가 $p^{k-1}$). en verbatim, ko 역주.
45. p14 note03-2 "$\gcd(a, 9 \gt 1$" 닫는 괄호 누락 — en verbatim, ko는 $\gcd(a,9) \gt 1$.
46. Thm 1.51 증명: "$aqtar$"(이탤릭 단어로 인쇄, 뜻은 $a^{qt}a^r$), 둘째 갈래 "$a^m \equiv a^tq$"($(a^t)^q$), 두 갈래 라벨이 모두 "⇒)"(둘째는 ⇐). en verbatim, ko는 바르게 + 역주.
47. **Example 1.15 (3) 거짓 진술**: p6에 "$1000 \equiv 4 \ (\bmod\ 7)$"로 인쇄 — $1000 - 4 = 996$은 7의 배수가 아니다($1000 = 7 \cdot 142 + 6$). 바른 값은 $1000 \equiv 6 \ (\bmod\ 7)$(예제 1.18 (1)의 $10000 \equiv 4 \ (\bmod\ 7)$은 옳으므로 0을 하나 빠뜨린 오타로 보임). en verbatim, ko는 6으로 바로잡고 역주.
48. **Thm 1.16 (1) 오타**: p6에 "then $a + c \equiv b + d(mod\ n)$ and **$ac \equiv bc(mod\ n)$**" — 인쇄된 결론 $ac \equiv bc$는 $a \equiv b$만으로 얻어지는 약한 주장이고, 가정 $c \equiv d$까지 쓰는 본래의 성질은 $ac \equiv bd$이다(Ex 1.22 풀이가 실제로 쓰는 형태). en verbatim, ko는 $ac \equiv bd$로 바로잡고 역주.
49. **Thm 1.60 진술 오류**: "$n = 2, 4, p^k$ or $2p^k$ for some prime $p$" — $p$는 **홀수인 소수**여야 한다. $p=2$를 허용하면 $n = 2^3 = 8$이 $p^k$ 꼴이 되어 원시근이 존재한다는 결론이 나오지만, 같은 쪽 Example 1.59 (3)이 법 8의 원시근은 없다고 말한다(실제로 $(\mathbb{Z}/2^k)^\times$는 $k \ge 3$이면 순환군이 아니다). en verbatim, ko는 "홀수인 소수" + 역주.
50. **p32 측정 확률의 0·1 뒤바뀜**: "If we measure a qubit $(x,y)$, then we measure **1** with probability $|x|^2$ and **0** with probability $|y|^2$" — 바로 다음 줄에서 $(1,0)=|0\rangle$, $(0,1)=|1\rangle$로 두므로 $x$는 $|0\rangle$의 계수이고, 확률 $|x|^2$로 측정되는 값은 0이어야 한다. 원문 §4.5의 측정 규칙과 Exercise 4.23($v=\frac{1}{\sqrt5}|0\rangle+\frac{2}{\sqrt5}|1\rangle$, $\Omega=\operatorname{diag}(2,1)$에서 측정값 2의 확률이 $1/5$)도 바른 순서를 따른다. en verbatim, ko는 바른 뜻 + 역주(note07-3), Ex 4.4 풀이도 바른 뜻.
51. **p4 §1.3 서술 둘째 가정 오타**: "If $ax_0 + by_0 = c$ and **$ax'_n + by'_n = 0$**, then $a(x_0 - x'_0) + b(y_0 - y'_0) = 0$" — 첨자·우변이 모두 어긋난다. 결론이 성립하려면 $(x'_0, y'_0)$도 $ax+by=c$의 해, 즉 $ax'_0 + by'_0 = c$여야 한다(두 해의 차가 동차방정식의 해). en verbatim, ko는 $ax'_0 + by'_0 = c$로 바로잡고 역주(note01-6).
52. p26 note05-5 피보나치 단락: "Then $C_k = \frac{u_k}{u_{k-1}}$" — 분자·분모가 뒤바뀜. $[0;1,1,\cdots,1]$에서는 $p_k = u_k$, $q_k = u_{k+1}$($u_0=0, u_1=u_2=1$)이므로 $C_k = \frac{u_k}{u_{k+1}}$이고(원문이 바로 위에 적은 $C_0=\frac01, C_1=\frac11, C_2=\frac12, C_3=\frac23$과 일치), 이 번호 매김에서 정리 3.9는 $u_{k+1}u_{k-1}-u_k^2 = (-1)^k$(카시니)를 준다 — 원문의 $(-1)^{k-1}$은 $u_k$를 $(k+1)$번째 피보나치 수로 보는 번호 매김에 해당. 또 이 항등식의 근거는 따름정리 3.10이 아니라 정리 3.9다. en verbatim, ko는 바른 식 + 역주(2026-09-08 ch05 검증에서 추가).
53. **Thm 3.29 진술 부호 오타**: p30에 마지막 항이 "$(-1)^n\frac{1}{q_nq_{n-1}}$"로 인쇄 — 앞의 두 항이 $+\frac{1}{q_1q_0}$, $-\frac{1}{q_2q_1}$이므로 $i$번째 항의 부호는 $(-1)^{i-1}$이고 마지막 항은 $(-1)^{n-1}\frac{1}{q_nq_{n-1}}$이어야 한다(같은 쪽 증명이 얻는 $\Sigma(-1)^{i-1}$과도 일치). 검산: $[1;2,3]=\frac{10}{7}$, $q_0=1,q_1=2,q_2=7$에서 $1+\frac12-\frac1{14}=\frac{10}{7}$(옳음)이지만 인쇄된 부호로는 $1+\frac12+\frac1{14}=\frac{11}{7}$. 아울러 증명 마지막 두 줄의 합 첨자 $\Sigma_{i=1}^{m}$은 $\sum_{i=1}^{n}$의 오타($C_n$을 계산 중). en verbatim, ko는 $(-1)^{n-1}$·$\sum_{i=1}^{n}$으로 바로잡고 역주(2026-09-08 ch06 검증에서 추가).
54. **note06-1 셋째 등식의 오른쪽에 항 하나 누락**(ERRATA 41 보완): p28 "$[1;1;1;1;2] = [1;1,1,1,1]$"에서 왼쪽의 세미콜론을 쉼표로 고쳐 $[1;1,1,1,2]$로 읽으면 값이 $\frac{13}{8}$인데 오른쪽 $[1;1,1,1,1]$은 $\frac85$여서 등식이 성립하지 않는다. $[a_0;\cdots,a_n] = [a_0;\cdots,a_n-1,1]$($a_n \gt 1$)이므로 오른쪽은 $[1;1,1,1,1,1]$이어야 한다(앞의 두 예 $[7]=[6;1]$, $[1;2,2,2]=[1;2,2,1,1]$도 항이 하나 늘어난다). en verbatim, ko는 $[1;1,1,1,2] = [1;1,1,1,1,1]$ + 역주(2026-09-08 ch06 검증에서 추가).

## 챕터별 인벤토리 (id = 카드 id; 쪽 = PDF 쪽)

### ch01.html — 유클리드 호제법과 디오판토스 방정식 / The Euclidean Algorithm and the Diophantine Equation ax + by = c
§1.1–1.3, pp2–6. 환경 13 (DEF 1, THM 3, EXAM 2, EX 7) + ALGO 3 + NOTE 8. Exercise: 1.5, 1.6, 1.7, 1.8(원문 풀이), 1.11, 1.12, 1.13(원문 풀이 (1)만).

| id | 배지 | 쪽 | 내용 |
|---|---|---|---|
| note01-1 | NOTE | 2 | Notation. $\mathbb{Z}$ (resp. $\mathbb{Q},\mathbb{R},\mathbb{C}$) … |
| c1-1 | DEF 1.1 | 2 | gcd 정의 ("different form zero") |
| c1-2 | EXAM 1.2 | 2 | $a = 3\cdot5^2\cdot7$, $b = 2\cdot5^2\cdot7\cdot11$, $\gcd = 5^2\cdot7$ |
| note01-2 | NOTE | 2 | How to find gcd? prime factorization is hard … Let introduce … |
| algo01-1 | ALGO | 2 | [The Division Algorithm] Input/Output |
| algo01-2 | ALGO | 2 | [The Euclidean Algorithm] Input/Output + 1–4 |
| c1-3 | EXAM 1.3 | 2–3 | (1) gcd(15,3) (2) gcd(15,6) |
| note01-3 | NOTE | 3 | For some nonzero integers … $r_3 = 0$ … remaining proof omitted (호제법 정당성 스케치) |
| note01-4 | NOTE | 3 | §1.2 도입: Let $a,b,c\in\mathbb{Z}$. How to solve $ax+by=c$? … |
| c1-4 | THM 1.4 | 3 | $T=\{ax+by\}$ = multiples of gcd (증명 없음) |
| note01-5 | NOTE | 3 | For example $\{6x+9y\}=\{3n\}$. Remark … iff $c|(a,b)$ [ERRATA 2] … Let introduce an algorithm … |
| algo01-3 | ALGO | 3–4 | (표제 없음) 확장 유클리드: Input $ax+by=c$, $c=\gcd$; 1–5 ($m_i, n_i$) — 편집 제목 "An Integral Solution of ax + by = gcd(a, b)" |
| c1-5 | EX 1.5 | 4 | gcd(65,105) by prime factorization |
| c1-6 | EX 1.6 | 4 | (1) gcd(65,105) (2) gcd(202,98) by Euclid |
| c1-7 | EX 1.7 | 4 | 빈칸: "$ax+by=c$ … has an integral solution iff ▢" |
| c1-8 | EX 1.8 | 4 | $56x+72y=8$ — **원문 풀이 verbatim 토글** (답 $(4,-3)$) |
| note01-6 | NOTE | 4–5 | §1.3 Notation(solution = integer solution) … homogeneous equation is important |
| c1-9 | THM 1.9 | 5 | 일반해 = 특수해 + 동차해 (증명 없음) |
| note01-7 | NOTE | 5 | To find all solutions … $a=a'\gcd$, $b=b'\gcd$ … ⇒ 사슬 |
| c1-10 | THM 1.10 | 5 | 동차방정식의 모든 해 $x = \frac{b}{\gcd}n$, $y=-\frac{a}{\gcd}n$ |
| note01-8 | NOTE | 5 | To summarize … 1. particular solution 2. general solution |
| c1-11 | EX 1.11 | 5 | (1) $120x+24y=0$ (2) $256x+30y=0$ |
| c1-12 | EX 1.12 | 5–6 | particular solution: $172x+20y=1000$; $278x+102y=2$ (p6 불릿) |
| c1-13 | EX 1.13 | 6 | all solutions (1)(2) — **원문 풀이 (1)만**, PART2 마커 [ERRATA 4] |

### ch02.html — 합동 산술과 법 n의 역원 / Modulo Arithmetic and Inverses Modulo n
§1.4–1.5, pp6–12. 환경 23 (DEF 2, THM 6, EXAM 6, EX 9) + REM 1 + ALGO 2 + NOTE 6. Exercise: 1.21, 1.22, 1.23, 1.24(원문 풀이), 1.25(원문 풀이), 1.33, 1.34, 1.35, 1.36.

| id | 배지 | 쪽 | 내용 |
|---|---|---|---|
| c1-14 | DEF 1.14 | 6 | congruent modulo $n$ |
| rem1 | REM 1 | 6 | $a \equiv b \iff r_1 = r_2$ |
| c1-15 | EXAM 1.15 | 6 | (1)(2)(3) [ERRATA 47] |
| c1-16 | THM 1.16 | 6–7 | (1)(2) [ERRATA 48] + p7 "Theorem 1.16 2)." 증명 verbatim |
| c1-17 | EXAM 1.17 | 6 | (1) $3\cdot6\equiv3\cdot x$ (2) $3\cdot4\equiv3\cdot8 \pmod 6$ 반례 |
| c1-18 | EXAM 1.18 | 7 | (1)(2)(3) 곱의 나머지 |
| note02-1 | NOTE | 7 | Consider the formula $a^x \equiv y$ … RSA password |
| c1-19 | EXAM 1.19 | 7 | (1)–(5) $3^{40} \pmod{11}$, 6 multiplications [ERRATA 5] |
| note02-2 | NOTE | 7–8 | 2-digit(이진) expression … count of multiplications 1. 2. |
| c1-20 | THM 1.20 | 8 | $2\lfloor\log_2 r\rfloor$ multiplication (증명 없음) |
| note02-3 | NOTE | 8 | 1 billion multiplications/sec, $N=10^{20}$: 3000 years vs 0.1 micro seconds |
| algo02-1 | ALGO | 8 | (Algorithm for powers mod $n$) recursive $\operatorname{power}(x,N)$ eq (1) [ERRATA 6] |
| c1-21 | EX 1.21 | 8 | $24x+9y=3$ |
| c1-22 | EX 1.22 | 8 | $1001\cdot409 \pmod 9$ |
| c1-23 | EX 1.23 | 8 | 빈칸: "$a^N(\bmod n)$ using only ▢ times multiplications." |
| c1-24 | EX 1.24 | 8–9 | $2^{341} \pmod{340}$ by 2-digit expression — **원문 풀이 verbatim** (답 32) |
| c1-25 | EX 1.25 | 9–10 | 알고리즘 step by step — **원문 풀이 verbatim** [ERRATA 7] |
| note02-4 | NOTE | 10 | §1.5 도입 $3\times7\equiv1 \pmod 5$ |
| c1-26 | DEF 1.26 | 10 | inverse $a^{-1} \pmod n$ [ERRATA 5] |
| c1-27 | EXAM 1.27 | 10 | (1)(2)(3) 2 has no inverse mod 10 |
| note02-5 | NOTE | 10 | Let's fix $n$. Which integer $a$ is invertible? |
| c1-28 | THM 1.28 | 10 | $a\equiv b \Rightarrow \gcd(a,n)=\gcd(b,n)$ + Proof |
| c1-29 | THM 1.29 | 10–11 | invertible iff $\gcd(n,a)=1$ + Proof (p11) [ERRATA 8] |
| c1-30 | THM 1.30 | 11 | + Proof |
| note02-6 | NOTE | 11 | invertible of $a$ modulo $n$ is associated with $a \pmod n$; prime $p$ |
| c1-31 | EXAM 1.31 | 11 | 1,5,7,11 invertible mod 12 |
| c1-32 | THM 1.32 | 11 | (1) 역원 유일 (2) $(a^{-1})^{-1}=a$ + Proof |
| algo02-2 | ALGO | 12 | [Inverse mod $n$ Algorithm] |
| c1-33 | EX 1.33 | 12 | invertible $0\le a\le19$ mod 20 |
| c1-34 | EX 1.34 | 12 | prove inverse unique |
| c1-35 | EX 1.35 | 12 | 빈칸 (A)(B) |
| c1-36 | EX 1.36 | 12 | $14^{-1} \pmod{23}$ |

### ch03.html — 일차합동식·중국인의 나머지 정리·오일러 φ 함수·원시근 / Linear Congruences, CRT, Euler's φ and Primitive Roots
§1.6–1.9, pp12–17. 환경 33 (DEF 3, THM 9, COR 1, EXAM 5, EX 15) + REM 3 + ALGO 1 + NOTE 7. Exercise: 1.40–1.43, 1.53–1.57, 1.64–1.69 (전부 풀이 대상).

| id | 배지 | 쪽 | 내용 |
|---|---|---|---|
| c1-37 | THM 1.37 | 12 | $\gcd(a,n)=1 \Rightarrow ax\equiv b$ unique solution + Proof |
| c1-38 | EXAM 1.38 | 12 | $3x\equiv2 \pmod 8$ → $x\equiv6$ |
| rem2 | REM 2 | 12 | (1) $3x\equiv0 \pmod 6$ not unique (2) $a^{-n}$ 정의, $a^ma^{m'}\equiv a^{m+m'}$ |
| note03-1 | NOTE | 12–13 | §1.7 도입 worked example $x\equiv4,9,3 \pmod{7,11,13}$ → $900$ |
| c1-39 | THM 1.39 | 13 | CRT + Proof (Uniqueness) [ERRATA 11] |
| algo03-1 | ALGO | 13 | [Chinese remainder theorem] 1–3 [ERRATA 10] |
| c1-40 | EX 1.40 | 13 | $13x\equiv4 \pmod{80}$ |
| c1-41 | EX 1.41 | 13 | $3x\equiv0 \pmod{18}$ |
| c1-42 | EX 1.42 | 13 | (1) $x\equiv2,4,6 \pmod{3,5,7}$ (2) $x\equiv2,4,2$ |
| c1-43 | EX 1.43 | 13 | $x^2+1\equiv0 \pmod{85}$ |
| c1-44 | DEF 1.44 | 14 | Euler phi |
| rem3 | REM 3 | 14 | $\phi(n)$ = number of invertible |
| c1-45 | EXAM 1.45 | 14 | $\phi(12)=4$ |
| note03-2 | NOTE | 14 | How to find $\phi(n)$: steps 1, 2; $\phi(9)=6$ |
| c1-46 | THM 1.46 | 14 | $\phi(p^k)=p^{k-1}(p-1)$ + Proof |
| note03-3 | NOTE | 14 | Let $n=p_1^{a_1}\cdots p_m^{a_m}$ … |
| c1-47 | THM 1.47 | 14 | $\phi(mn)=\phi(m)\phi(n)$ (증명 없음) |
| note03-4 | NOTE | 14 | $\phi(540)=144$ |
| rem4 | REM 4 | 14 | $\phi(3)\phi(3)\ne\phi(9)$ |
| c1-48 | THM 1.48 | 14–15 | $\phi(n)=n\prod(1-1/p_i)$ + Proof (p15) |
| note03-5 | NOTE | 15 | For given $n,a$, find $m$ with $a^m\equiv1$ |
| c1-49 | DEF 1.49 | 15 | order of $a$ modulo $n$ |
| c1-50 | EXAM 1.50 | 15 | (1)(2)(3) 표 2개 (mod 5, mod 11) [ERRATA 5] |
| c1-51 | THM 1.51 | 15 | 진술 미완 [ERRATA 13] + Proof ($t \mid m$) |
| c1-52 | COR 1.52 | 15–16 | $1,a,\dots,a^{t-1}$ distinct + Proof (p16) |
| c1-53 | EX 1.53 | 16 | $\phi(2010)$ |
| c1-54 | EX 1.54 | 16 | example $\phi(mn)\ne\phi(m)\phi(n)$ |
| c1-55 | EX 1.55 | 16 | least $a$ with $\phi(n)\ne a$ for all $n$ |
| c1-56 | EX 1.56 | 16 | invertible count mod 524 |
| c1-57 | EX 1.57 | 16 | order of 7 mod 18 |
| c1-58 | DEF 1.58 | 16 | primitive root |
| c1-59 | EXAM 1.59 | 16 | (1)(2)(3) mod 5, 7, 8 [ERRATA 14] |
| c1-60 | THM 1.60 | 16 | primitive root exists iff $n=2,4,p^k,2p^k$ (증명 없음) |
| note03-6 | NOTE | 16 | (Artin conjecture) |
| c1-61 | THM 1.61 | 16 | Euler's theorem (증명 없음) |
| note03-7 | NOTE | 16 | Let's confirm for mod 7 + 표 + "3 and 5 are primitive root" |
| c1-62 | THM 1.62 | 17 | Fermat little theorem + Proof |
| c1-63 | EXAM 1.63 | 17 | (1) $3^{205} \pmod{101}$ (2) $5^{10000} \pmod{18}$ [ERRATA 5] |
| c1-64 | EX 1.64 | 17 | $a^p\equiv a \pmod p$ |
| c1-65 | EX 1.65 | 17 | primitive roots mod 12 |
| c1-66 | EX 1.66 | 17 | primitive roots mod 10 |
| c1-67 | EX 1.67 | 17 | $6^{10004} \pmod{11}$ |
| c1-68 | EX 1.68 | 17 | $2^{10000} \pmod{13}$ |
| c1-69 | EX 1.69 | 17 | count invertible mod 18 |

### ch04.html — 암호: 디피-헬만 키 교환과 RSA / Cryptology: Diffie-Hellman Key Exchange and RSA
§2, pp17–19. 환경 9 (DEF 1, EXAM 3, EX 5) + ALGO 2 + NOTE 5. Exercise: 2.4, 2.5, 2.6, 2.8, 2.9.

| id | 배지 | 쪽 | 내용 |
|---|---|---|---|
| note04-1 | NOTE | 17 | §2.1 도입 Alice, Bob, public channel … hard to find $N$ [ERRATA 17] |
| c2-1 | DEF 2.1 | 17 | discrete logarithm problem |
| c2-2 | EXAM 2.2 | 17 | $2^N\equiv3 \pmod{11}$ 표 → $N=8$ |
| note04-2 | NOTE | 18 | To get $N$, compute all … $10^{100}$ possible $N$ |
| algo04-1 | ALGO | 18 | (Algorithm of Diffie-Hellman key exchange) Goal + 1–4 |
| note04-3 | NOTE | 18 | Eavesdropper(Eve) … not easy to proof |
| c2-3 | EXAM 2.3 | 18 | $a=2,p=11,s=4,t=8$ → key 4 |
| c2-4 | EX 2.4 | 18 | $3^N\equiv9 \pmod{13}$ |
| c2-5 | EX 2.5 | 18 | give the DH algorithm |
| c2-6 | EX 2.6 | 18 | $p=13$, base 3, $s=6$, $t=5$ |
| note04-4 | NOTE | 18–19 | §2.2 도입 RSA 1977 … public-key cryptosystem |
| algo04-2 | ALGO | 19 | (Algorithm of RSA) 1–4 + Public key/message/Encryption/Decryption |
| note04-5 | NOTE | 19 | range of the message … $y^d\equiv\cdots\equiv x$ |
| c2-7 | EXAM 2.7 | 19 | $p=5,q=11$, $(55,3)$, $d=27$, $4\to9\to4$ |
| c2-8 | EX 2.8 | 19 | $(N,e)=(323,11)$, message 316: (1)(2)(3) |
| c2-9 | EX 2.9 | 19 | estimate $\phi(N)/N$ |

### ch05.html — 유한 연분수 / Finite Continued Fractions
§3.1, pp20–27. 환경 20 (DEF 3, THM 4, COR 1, LEM 1, EXAM 1, EX 10) + ALGO 1 + NOTE 5. Exercise: 3.4, 3.5, 3.6, 3.13(*), 3.14, 3.15, 3.16, 3.17, 3.18, 3.19. 자체 증명: THM 3.9, 3.12.

| id | 배지 | 쪽 | 내용 |
|---|---|---|---|
| note05-1 | NOTE | 20 | [1, Chapter 15] … §3.1 도입 $61/14$ 전개 [ERRATA 18] |
| c3-1d | DEF 3.1 | 20–21 | (1) finite continued fraction (2) simple |
| c3-1t | THM 3.1 | 21 | rational ⇒ finite SCF; "The key point of proof … Euclid's algorithm." + Proof |
| c3-2 | EXAM 3.2 | 22 | $19/51$ |
| c3-3 | DEF 3.3 | 23 | $[a_0;a_1,\cdots,a_n]$ |
| note05-2 | NOTE | 23 | $19/51=[0;2,1,2,6]=[0;2,1,2,5,1]$; Remark $[\dots,a_n]=[\dots,a_n-1,1]$ |
| algo05-1 | ALGO | 23 | [Simple continued fraction algorithm] (a)(b)(c) |
| c3-4 | EX 3.4 | 23 | $172/51$, $71/55$ |
| c3-5 | EX 3.5 | 23 | $118/303$ |
| c3-6 | EX 3.6 | 23 | $[-2;2,4,6,8]$, $[0;1,2,3,4,3,2,1]$ |
| c3-7 | DEF 3.7 | 23 | $k$th convergent $C_k$ |
| note05-3 | NOTE | 24 | convergents of $19/51$; $p_k,q_k$ 정의; $C_0,C_1,C_2$ 직접 계산; $p_{-2},q_{-2},p_{-1},q_{-1}$ |
| c3-8 | THM 3.8 | 25 | $C_k=p_k/q_k$ + Proof [ERRATA 20] |
| note05-4 | NOTE | 25 | specific example $19/51$: $p_k,q_k$ 표식 계산 |
| c3-9 | THM 3.9 | 26 | $p_kq_{k-1}-q_kp_{k-1}=(-1)^{k-1}$ — **증명 빈칸 → 마커** |
| c3-10 | COR 3.10 | 26 | $\gcd(p_k,q_k)=1$ + Proof |
| note05-5 | NOTE | 26 | Summary; Fibonacci $[0;1,1,\dots,1]$ [ERRATA 52]; theorem 15.8 예: $172x+20y=1000$, $43/5=[8;1,1,2]$ [ERRATA 22] |
| c3-11 | LEM 3.11 | 26–27 | $q_{k-1}\le q_k$ + Proof (p27) |
| c3-12 | THM 3.12 | 27 | (1)(2)(3) 짝·홀 근사분수 — **증명 빈칸 → 마커** |
| c3-13 | EX 3.13 | 27 | (*) $p_n$ of $[1;2,3,\cdots,n,n+1]$ |
| c3-14 | EX 3.14 | 27 | $q_k\ge2^{(k-1)/2}$ |
| c3-15 | EX 3.15 | 27 | convergents of $[1;2,3,3,2,1]$, $[-3;1,1]$ |
| c3-16 | EX 3.16 | 27 | SCF of 3.1416, 3.14159 |
| c3-17 | EX 3.17 | 27 | $p_k/p_{k-1}=[a_k;\cdots,a_0]$, $q_k/q_{k-1}=[a_k;\cdots,a_1]$ |
| c3-18 | EX 3.18 | 27 | (1) $19x+51y=1$ (2) $18x+5y=24$ |
| c3-19 | EX 3.19 | 27 | verify Thm 3.12 for $[1;1,1,1,1,1,1,1]$ |

### ch06.html — 무한 연분수와 최선의 근사 / Infinite Continued Fractions and Best Approximations
§3.2, pp28–31. 환경 16 (THM 5, COR 1, DEF 2, EXAM 2, EX 6) + ALGO 1 + NOTE 3. Exercise: 3.24, 3.25, 3.26, 3.33, 3.34, 3.35. 자체 증명: THM 3.30.

| id | 배지 | 쪽 | 내용 |
|---|---|---|---|
| c3-20 | THM 3.20 | 28 | Uniqueness of a simple continued fraction (증명 없음) |
| c3-21 | COR 3.21 | 28 | exactly two ways (증명 없음) |
| note06-1 | NOTE | 28 | $[7]=[6;1]$ …; irrational $x=\lim[a_0;\cdots,a_n]$; notation |
| algo06-1 | ALGO | 28 | [Computing a simple continued fraction] 1–5 [ERRATA 25] |
| note06-2 | NOTE | 28 | $\pi=[3;7,15,1,292,\cdots]$ |
| c3-22 | DEF 3.22 | 28 | periodic $[a_0;\cdots,a_n,\overline{b_1,\cdots,b_m}]$ |
| c3-23 | EXAM 3.23 | 28–29 | $x=[3;6,\overline{1,4}]$, $y=(1+\sqrt2)/2$, $x=(14-\sqrt2)/4$ |
| c3-24 | EX 3.24 | 29 | recursive relations for $p_k,q_k$ [ERRATA 29] |
| c3-25 | EX 3.25 | 29 | (1) $[\overline{2;3}]$ (2) $[2;\overline{1,2,1}]$ |
| c3-26 | EX 3.26 | 29 | (1) $\sqrt{n^2+1}$ (2) $\sqrt{n^2+2}$ (3) $\sqrt{n^2+2n}$ |
| note06-3 | NOTE | 29 | question: best approximation |
| c3-27 | DEF 3.27 | 29 | best approximation |
| c3-28 | THM 3.28 | 29 | $q_n\ge n$ + Proof [ERRATA 26] |
| c3-29 | THM 3.29 | 30 | alternating sum formula + Proof |
| c3-30 | THM 3.30 | 30 | $|x-p_m/q_m|\lt1/(q_{m+1}q_m)$ — **"추후 추가" → 마커** |
| c3-31 | THM 3.31 | 30–31 | convergent is best approximation (증명 없음) [ERRATA 27] |
| c3-32 | EXAM 3.32 | 31 | $\sqrt2=[1;\overline2]$, 표, $41/29$ |
| c3-33 | EX 3.33 | 31 | $x=[1;3,1,5,1,7,1,\cdots]$ (1) $b\le23$ (2)(*) $b\le239$ |
| c3-34 | EX 3.34 | 31 | (1) $\sqrt{15}$, $1/50^2$ + Hint (2)(*) four decimal places [ERRATA 28] |
| c3-35 | EX 3.35 | 31 | (*) $(1+\sqrt{10})/3$ vs $18/13$ |

### ch07.html — 큐비트와 게이트 / Qubits and Gates
§4.1–4.4, pp31–36. 환경 16 (DEF 4, EXAM 2, EX 10) + NOTE 8 + 그림 4(SVG) + 표 5. Exercise: 4.2–4.5, 4.11–4.16.

| id | 배지 | 쪽 | 내용 |
|---|---|---|---|
| note07-1 | NOTE | 31–32 | §4 도입 3단락 (analog/digital, Kirchhoff, superposition & collapse) |
| note07-2 | NOTE | 32 | A bit is the unit information … |
| c4-1 | DEF 4.1 | 32 | qubit = unit vector of $\mathbb{C}^2$ |
| note07-3 | NOTE | 32 | $e_1,e_2$; measure with prob $|x|^2$; $|0\rangle,|1\rangle$; $a|0\rangle+b|1\rangle$; 비교표(formal-table) |
| c4-2 | EX 4.2 | 32 | 빈칸 (a)(b) |
| c4-3 | EX 4.3 | 32–33 | Explain (1)(2)(3) |
| c4-4 | EX 4.4 | 33 | What is a qubit? |
| c4-5 | EX 4.5 | 33 | (1) $(2,4)$ (2) $(7,2)$ (3) $(1/\sqrt2,-1/\sqrt2)$ |
| c4-6 | DEF 4.6 | 33 | (1) two-qubit ⊗ 전개 (2) $n$-qubit [ERRATA 30] |
| note07-4 | NOTE | 33 | $|ac|^2+\cdots=1$; $|ab\rangle:=|a\rangle\otimes|b\rangle$ |
| note07-5 | NOTE | 33 | §4.3 도입 classical gate; Assunte … |
| c4-7 | DEF 4.7 | 33–34 | And/Or gate 그림(SVG) + (1) AND 진리표·$AB\equiv C$ (2) OR 진리표 [ERRATA 31]·$(A+1)(B+1)+1$ (3) NOT 그림(SVG, ERRATA 32)·진리표 |
| note07-6 | NOTE | 34 | universal gate theorem |
| c4-8 | DEF 4.8 | 34–35 | §4.4 (1) unitary (2) quantum gate 1-qubit; $U(x_1|0\rangle+x_2|1\rangle)$ |
| c4-9 | EXAM 4.9 | 35 | quantum "not" gate $U$ |
| note07-7 | NOTE | 35 | $n$-qubit $\in\mathbb{C}^{2^n}$; unitary sends $n$-qubit to $n$-qubit |
| c4-10 | EXAM 4.10 | 35–36 | (1) CNOT 진리표 + 행렬 (2) X·Z gate 회로(SVG 2) + "Compute to find …" |
| note07-8 | NOTE | 36 | every quantum gate = 1-qubit gates + CNOT |
| c4-11 | EX 4.11 | 36 | definition of unitary |
| c4-12 | EX 4.12 | 36 | 빈칸 (a)(b)(c) |
| c4-13 | EX 4.13 | 36 | CNOT on $(x|0\rangle+y|1\rangle)\otimes\frac{|0\rangle+|1\rangle}{\sqrt2}$ |
| c4-14 | EX 4.14 | 36 | matrix of $U$ (Hadamard) |
| c4-15 | EX 4.15 | 36 | 2-qubit gate 순열 → 행렬 |
| c4-16 | EX 4.16 | 36 | X·Z gate 행렬 [ERRATA 33] |

### ch08.html — 측정, 아다마르 게이트와 CNOT 게이트 / Measurement, the Hadamard Gate and the CNOT Gate
§4.5–4.6, pp36–39. 환경 9 (DEF 1, EXAM 3, EX 5) + NOTE 5 + 그림 1(SVG). Exercise: 4.21–4.25.

| id | 배지 | 쪽 | 내용 |
|---|---|---|---|
| note08-1 | NOTE | 36 | §4.5 $H:=\mathbb{C}^n$ with inner product |
| c4-17 | DEF 4.17 | 36 | state |
| note08-2 | NOTE | 37 | Hermitian $\Omega$, orthonormal eigenbasis, measurement 확률 $|a_i|^2$, collapse; 측정 도식(array); "Let's better understand …" |
| c4-18 | EXAM 4.18 | 37 | $v=(1/2,\sqrt3/2)$, $\Omega=\operatorname{diag}(-2,1)$ |
| c4-19 | EXAM 4.19 | 37 | $v_1,v_2$, $v=\frac1{\sqrt3}|0\rangle+\frac{\sqrt2}{\sqrt3}|1\rangle$ [ERRATA 34] |
| c4-20 | EXAM 4.20 | 37–38 | $\Omega|0\rangle=\lambda_1|0\rangle$, $v=\frac1{\sqrt2}(|0\rangle+|1\rangle)$, prob 1/2 |
| c4-21 | EX 4.21 | 38 | definition of Hermitian |
| c4-22 | EX 4.22 | 38 | explain "measure" (1)(2)(3) |
| c4-23 | EX 4.23 | 38 | $v=\frac1{\sqrt5}|0\rangle+\frac2{\sqrt5}|1\rangle$, $\Omega=\operatorname{diag}(2,1)$ (1)(2) |
| note08-3 | NOTE | 38 | §4.6 Hadamard gate 회로(SVG); $|+\rangle,|-\rangle$; 행렬 $\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ |
| note08-4 | NOTE | 38 | symbols for CNOT·SWAP; $B\oplus A$; [Figure.1][Figure.2] [ERRATA 35] |
| c4-24 | EX 4.24 | 39 | Explain the Hadamard gate |
| c4-25 | EX 4.25 | 39 | [Figure.3][Figure.4] states [ERRATA 35] |
| note08-5 | NOTE | 39 | References [1] Burton |
