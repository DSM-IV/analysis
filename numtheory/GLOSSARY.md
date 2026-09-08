# 응용정수론 용어집 (Applications of Number Theory Glossary)

소스: MATH463 Applications of Number Theory (2026 Fall, 고려대 최도훈) 강의노트 — 영문 LaTeX. 참고: D. Burton, *Elementary Number Theory* 7e.
대한수학회 용어집 + 기존 과목(la2·analysis2·settheory) 관행을 따른다. 번역·풀이 작성 시 이 표의 용어만 사용할 것.

## 핵심 금칙·주의
- Euclidean algorithm = **유클리드 호제법** ("유클리드 알고리즘" 금지). division algorithm = **나눗셈 알고리즘**(박스 제목·본문 동일; "나눗셈 정리" 금지).
- congruent modulo $n$ = **법 $n$에 대하여 합동** ("모듈로 n" 금지, "n을 법으로" 허용). modulus = **법**. congruence (equation) = **합동식**. 수식 안 `(\bmod\ n)`은 그대로.
- inverse of $a$ modulo $n$ = **법 $n$에 대한 $a$의 역원**, invertible modulo $n$ = **법 $n$에 대하여 가역(역원을 가진다)**. "역수" 금지.
- relatively prime / coprime = **서로소**. greatest common divisor = **최대공약수**(기호 $\gcd(a,b)$ — 원문 이탤릭 $gcd$는 `\gcd`로 정규화, lcm은 `\operatorname{lcm}`).
- Euler $\phi$ function = **오일러 $\phi$ 함수** ("오일러 파이 함수"·"토션트" 금지). Euler's theorem = **오일러 정리**, Fermat little theorem = **페르마 소정리**.
- order of $a$ modulo $n$ = **법 $n$에 대한 $a$의 위수**. primitive root of mod $n$ = **법 $n$의 원시근** ("원시원소" 금지).
- Chinese remainder theorem = **중국인의 나머지 정리** (약칭 CRT는 en 알고리즘 이름에서만).
- continued fraction = **연분수**, simple continued fraction = **단순연분수**, finite/infinite = **유한/무한 연분수**, $k$th convergent = **$k$번째 근사분수** ("컨버전트"·"수렴자" 금지), periodic = **순환**(순환마디 $\overline{b_1,\cdots,b_m}$), best approximation = **최선의 근사**.
- qubit = **큐비트**, bit = **비트**, superposition = **중첩**, collapse = **붕괴**, measurement = **측정**, state = **상태**, tensor product $\otimes$ = **텐서곱**.
- unitary = **유니터리**(대한수학회; la2 용어집의 "유니타리"는 la2 Ch.6 빌드 시 이쪽으로 통일 예정), Hermitian = **에르미트**, conjugate transpose = **켤레전치**(원문 $\overline{A}^{T}$ 그대로).
- gate = **게이트**: AND/OR/NOT 게이트(영문 대문자), quantum gate = **양자 게이트**, classical gate = **고전 게이트**, Hadamard gate = **아다마르 게이트**, CNOT gate = **CNOT 게이트**(controlled not = 제어 NOT), SWAP gate = **SWAP 게이트**, $X$-gate/$Z$-gate = **$X$ 게이트/$Z$ 게이트**, truth table = **진리표**.
- 사람 이름: 유클리드(Euclid), 디오판토스(Diophantus), 오일러(Euler), 페르마(Fermat), 아르틴(Artin), 디피(Diffie)-헬만(Hellman), 리베스트(Rivest)·샤미르(Shamir)·에이들먼(Adleman; 원문 오타 Shadmir/Adeleman은 en verbatim), 피보나치(Fibonacci), 아다마르(Hadamard), 키르히호프(Kirchhoff), 버튼(Burton).
- 사이시옷: 최댓값/최솟값. "정수해"(integral solution)로 통일("정수 해" 금지).

## 문체 규칙 (analysis2·settheory와 동일)
- 문제 서술: "-하라"체. Find/Compute/Calculate = "구하라/계산하라", Solve = "풀어라", Prove/Show = "증명하라", Explain = "설명하라", Express = "나타내라", Evaluate = "값을 구하라", Verify = "확인하라", Estimate = "어림하라", Give an example s.t. = "…인 예를 들어라", Fill the blank(s) = "빈칸을 채워라", Complete the following statement = "다음 명제를 완성하라", Give the definition of = "…의 정의를 말하라", Give the … algorithm = "… 알고리즘을 서술하라".
- 진술·증명: "-이다"체. 증명/풀이 토글은 라벨("증명."/"Proof.") 없이 본문 바로 시작.
  - 증명형(prove/show/verify 포함) → "증명 보기/증명 접기 · Proof/Hide Proof" + `<div class="qed">□</div>`.
  - 계산·판정·설명·빈칸 → "풀이 보기/풀이 접기 · Solution/Hide Solution", qed 없음.
  - 원문 풀이가 인쇄된 Exercise(1.8, 1.13(1), 1.24, 1.25)는 en verbatim(끝 □ 유지) + ko 번역 미러.
- 수식·기호 원문 verbatim: $a \equiv b \ (\bmod\ n)$, $n \mid a-b$, $\gcd(a,b)$, $a^{-1} \ (\bmod\ n)$, $\phi(n)$, $\lfloor x \rfloor$, $[a_0; a_1, \cdots, a_n]$, $C_k = p_k/q_k$, $\overline{b_1,\cdots,b_m}$, $\mathbb{Z}_{>0}$, $|0\rangle, |1\rangle$, $|ab\rangle := |a\rangle \otimes |b\rangle$, $M_{n\times n}(\mathbb{C})$, $\overline{A}^{T}$, $\operatorname{power}(x,N)$.
- display 수식 안 `\text{…}` 영문 산문은 ko 패널에서 한국어로: `\text{for some } q \in \mathbb{Z}` → `(\text{어떤 } q \in \mathbb{Z}\text{에 대하여})`, `\text{ if } N \text{ even}` → `N\text{이 짝수일 때}`, `\text{return}` → 그대로(코드 관례), `\text{measurement } \lambda_i \text{ with prob } |a_i|^2` → `\text{측정값 } \lambda_i,\ \text{확률 } |a_i|^2`.
- 알고리즘 박스: **Input :** → **입력 :**, **Output :** → **출력 :**, **Goal :** → **목표 :**, 단계 번호는 원문 그대로. "return" 은 그대로 둔다.
- 원문 오타·문법 오류(SOURCE-MAP ERRATA)는 en에 그대로, ko는 바른 뜻. 원문 진술이 미완인 정리(Thm 1.51)는 ko에서 결론을 보충하고 `<p><em>역주.</em> …</p>`.

## §1 정수론 복습 (Review of number theory)
| English | 한국어 |
|---|---|
| integer / rational / real / complex number | 정수 / 유리수 / 실수 / 복소수 |
| greatest common divisor $\gcd(a,b)$ | 최대공약수 |
| prime / prime factorization | 소수 / 소인수분해 |
| division algorithm | 나눗셈 알고리즘 |
| Euclidean algorithm (Euclid's algorithm) | 유클리드 호제법 |
| input / output | 입력 / 출력 |
| quotient / remainder | 몫 / 나머지 |
| multiple of / divisor of / $d \mid n$ ($d$ divides $n$) | 배수 / 약수 / $d$가 $n$을 나눈다 |
| Diophantine equation $ax + by = c$ | 디오판토스 방정식 |
| integral solution (integer solution) | 정수해 |
| particular solution / general solution | 특수해 / 일반해 |
| homogeneous equation $ax + by = 0$ | 동차방정식 |
| arbitrary integer | 임의의 정수 |
| congruent modulo $n$, $a \equiv b \ (\bmod\ n)$ | 법 $n$에 대하여 합동 |
| modulo arithmetic | 합동 산술 |
| (multiplicative) inverse of $a$ modulo $n$, $a^{-1}$ | 법 $n$에 대한 $a$의 (곱셈) 역원 |
| invertible modulo $n$ | 법 $n$에 대하여 가역 |
| unique / uniqueness | 유일한 / 유일성 |
| 2-digit expression (binary expression) | 이진 표현(원문 "2-digit expression"은 "2진 표현"으로 옮기고 첫 등장에 영문 병기) |
| multiplication (count) | 곱셈 (횟수) |
| recursive algorithm | 재귀 알고리즘 |
| Chinese remainder theorem (CRT) | 중국인의 나머지 정리 |
| pairwise relatively prime | 쌍마다 서로소 |
| system (of congruences) | 연립합동식 |
| least common multiple $\operatorname{lcm}$ | 최소공배수 |
| Euler $\phi$ function, Euler phi function | 오일러 $\phi$ 함수 |
| order of $a$ modulo $n$ | 법 $n$에 대한 $a$의 위수 |
| least positive integer | 최소의 양의 정수 |
| distinct (integers modulo $n$) | (법 $n$에 대하여) 서로 다른 |
| primitive root of mod $n$ | 법 $n$의 원시근 |
| Artin conjecture | 아르틴 추측 |
| Euler's theorem / Fermat little theorem | 오일러 정리 / 페르마 소정리 |
| It is possible to calculate … | …를 계산할 수 있다 |
| contradiction | 모순 |

## §2 암호 (Cryptology)
| English | 한국어 |
|---|---|
| cryptology | 암호학(단원 제목은 "암호") |
| Diffie-Hellman key exchange | 디피-헬만 키 교환 |
| public channel / secret key | 공개 채널 / 비밀키 |
| discrete logarithm problem | 이산로그 문제 |
| base $a$ | 밑 $a$ |
| eavesdropper (Eve) | 도청자(이브) |
| RSA (algorithm) | RSA (알고리즘) |
| encryption scheme | 암호 방식 |
| public-key cryptosystem | 공개키 암호체계 |
| public key $(N, e)$ / private key | 공개키 / 개인키 |
| message / encryption / decryption | 메시지 / 암호화 / 복호화 |
| announce (public key) | (공개키를) 공개하다 |
| Alice, Bob (A, B) | 앨리스, 밥 (A, B) |

## §3 연분수 (Continued Fractions)
| English | 한국어 |
|---|---|
| (finite / infinite) continued fraction | (유한 / 무한) 연분수 |
| simple continued fraction | 단순연분수 |
| symbol $[a_0; a_1, \cdots, a_n]$ | 기호 $[a_0; a_1, \cdots, a_n]$ |
| $k$th convergent $C_k$ | $k$번째 근사분수 |
| numerator / denominator | 분자 / 분모 |
| relatively prime | 서로소 |
| Fibonacci number | 피보나치 수 |
| odd / even script (index) | 홀수 / 짝수 번째(첨자) |
| uniqueness of a simple continued fraction | 단순연분수의 유일성 |
| integral part $[x_m]$ | 정수 부분 |
| periodic continued fraction, $\overline{b_1,\cdots,b_m}$ | 순환연분수, 순환마디 |
| irrational number | 무리수 |
| best approximation | 최선의 근사 |
| accuracy to four decimal places | 소수 넷째 자리까지의 정확도 |
| linear Diophantine equation | 일차 디오판토스 방정식 |

## §4 양자컴퓨터 기초 (Basic of Quantum computer)
| English | 한국어 |
|---|---|
| quantum computer / classical computer | 양자컴퓨터 / 고전컴퓨터 |
| analog computer / digital computer | 아날로그 컴퓨터 / 디지털 컴퓨터 |
| Kirchhoff's current law | 키르히호프 전류 법칙 |
| particle / wave | 입자 / 파동 |
| superposition / collapse / measurement | 중첩 / 붕괴 / 측정 |
| bit / qubit / two-qubit / $n$-qubit | 비트 / 큐비트 / 2-큐비트 / $n$-큐비트 |
| unit information | 정보의 단위 |
| unit vector | 단위벡터 |
| probability | 확률 |
| tensor (product) $\otimes$ | 텐서곱 |
| linear combination | 일차결합 |
| classical gate / quantum gate | 고전 게이트 / 양자 게이트 |
| digital logic circuit | 디지털 논리 회로 |
| And gate / Or gate / Not gate | AND 게이트 / OR 게이트 / NOT 게이트 |
| truth table | 진리표 |
| input data / output data | 입력 / 출력 |
| universal gate theorem | 범용 게이트 정리 |
| unitary (matrix) | 유니터리 (행렬) |
| controlled not gate (CNOT) | 제어 NOT 게이트 (CNOT 게이트) |
| $X$-gate / $Z$-gate / single gate | $X$ 게이트 / $Z$ 게이트 / 단일 게이트 |
| Hermitian matrix | 에르미트 행렬 |
| diagonalizable / eigenvalue / eigenvector | 대각화가능 / 고유값 / 고유벡터 |
| orthonormal basis | 정규직교기저 |
| inner product | 내적 |
| state | 상태 |
| new state | 새 상태 |
| Hadamard gate | 아다마르 게이트 |
| SWAP gate | SWAP 게이트 |
| symbol (for a gate) | (게이트) 기호 |
