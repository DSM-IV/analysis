# §16.10 Summary — PDF p.1283 (인쇄 p.1246)

절 전체가 한 쪽짜리 **정리 요약표** 하나다. 예제 **0개**, 연습문제 없음.
(PDF p.1284 이후의 Chapter 16 Review — Concept Check / True-False Quiz / Exercises — 와 Problems Plus는 **이 인벤토리 범위 밖**.)

## A. 카드 인벤토리 (원문 순서)

| # | 카드 | 원문 라벨 | 제목 (한국어 / English) | 내용 요지 (수식 포함, TeX) | PDF 쪽 | 증명 | 그림 |
|---|---|---|---|---|---|---|---|
| 1 | rem | 16.10 Summary (요약표) | 벡터적분 5대 정리 요약 / The Five Theorems at a Glance | 16장의 주요 결과는 모두 **미적분학의 기본정리의 고차원판**이다. 좌변은 영역 위 "도함수"의 적분, 우변은 **그 영역의 경계에서의 원래 함수 값**만 사용한다(가정은 생략). ① *곡선과 그 경계(끝점)* — 미적분학의 기본정리 $\displaystyle\int_a^b F'(x)\,dx=F(b)-F(a)$; 선적분의 기본정리 $\displaystyle\int_C\nabla f\cdot d\mathbf r=f(\mathbf r(b))-f(\mathbf r(a))$. ② *곡면과 그 경계* — 그린 정리 $\displaystyle\iint_D\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dA=\int_C P\,dx+Q\,dy$; 스토크스 정리 $\displaystyle\iint_S\operatorname{curl}\mathbf F\cdot d\mathbf S=\int_C\mathbf F\cdot d\mathbf r$. ③ *입체와 그 경계* — 발산정리 $\displaystyle\iiint_E\operatorname{div}\mathbf F\,dV=\iint_S\mathbf F\cdot d\mathbf S$ | 1283 | — | 요약 도해 |
| 2 | fig | (요약표 우측 삽화 5종) | 경계의 사다리 / The Boundary Ladder | 각 행 오른쪽 삽화를 하나의 도해로: 구간 $[a,b]$의 끝점 $a,b$ → 곡선 $C$의 끝점 $\mathbf r(a),\mathbf r(b)$ → 평면영역 $D$의 경계곡선 $C$ → 유향곡면 $S$(법선 $\mathbf n$)의 경계곡선 $C$ → 입체 $E$의 경계곡면 $S$(바깥법선 $\mathbf n$). 차원이 하나씩 올라가면서 "경계"도 0차원 → 1차원 → 2차원으로 올라간다 | 1283 | — | 필수 |

카드 수: **note 0, def 0, thm 0, rem 1, fig 1 — 합계 2**

## B. 예제 기준값

이 절에는 예제가 **0개**다. (요약표만 있고 풀이 예시는 없음.)

재계산 스크립트: `/Users/chalrs/analysis/stewart/inventory/anchor-16.10.py` — 수치 anchor는 없고, 요약표 다섯 항등식의 내부 정합성(선적분 기본정리 ← 연쇄법칙+FTC, 그린 정리 ← 평평한 스토크스 $\mathbf n=\mathbf k$, 발산정리의 2차원 형태)만 sympy로 확인한다. 실행 결과 이상 없음.

## C. 그림 필요 목록 (자체 SVG)

| 원문 Figure | 내용 | 필수/선택 | 소속 카드 # |
|---|---|---|---|
| 요약표 삽화 1 | 구간 $[a,b]$ 와 끝점 $a,b$ (점 두 개) | **필수** (통합 도해의 1행) | 2 |
| 요약표 삽화 2 | 곡선 $C$ 와 끝점 $\mathbf r(a),\mathbf r(b)$ | **필수** (2행) | 2 |
| 요약표 삽화 3 | 평면영역 $D$ 와 양의 방향 경계곡선 $C$ | **필수** (3행) | 2 |
| 요약표 삽화 4 | 유향곡면 $S$, 법선 $\mathbf n$, 경계곡선 $C$ | **필수** (4행) | 2 |
| 요약표 삽화 5 | 입체 $E$, 경계곡면 $S$, 바깥법선 $\mathbf n$ | **필수** (5행) | 2 |

→ 사이트에서는 **5행짜리 표 + 각 행 옆의 작은 SVG 5개**(또는 한 장의 통합 SVG)로 구성하는 것을 권장. 표 자체가 이 절의 전부이므로 rem 카드 안에 표를 그대로 두고, fig는 그 표의 오른쪽 열로 붙이는 편이 원문 구조와 맞는다.

## D. ERRATA·판독 불확실

- pdftotext 추출본에서 요약표의 행 배치와 삽화 캡션이 뒤섞였으나(예: 세 번째 행에 `C`·`S` 라벨이 겹쳐 나옴), PNG p-1283으로 표 전체를 시각 확인함. 표는 3개 구역("Curves and their boundaries (endpoints)", "Surfaces and their boundaries", "Solids and their boundaries")에 총 **5개 행**.
- 그린 정리 행의 우변은 $\int_C P\,dx+Q\,dy$ (원문 그대로, $\oint$ 기호를 쓰지 않음).
- 스토크스 정리·발산정리 행에는 가정이 **의도적으로 생략**되어 있다("without hypotheses"). 사이트에서도 이 점을 명시하고 §16.8·§16.9 카드로 링크할 것.
- PLAN.md의 예제 수(0)는 정확.

## E. 절 요약 (사이트 도입 note 초안)

16장의 다섯 정리는 모두 같은 문장을 차원만 바꿔 말한 것이다. 왼쪽에는 영역 위에서 어떤 "도함수"를 적분하고 — $F'$, $\nabla f$, $Q_x-P_y$, $\operatorname{curl}\mathbf F$, $\operatorname{div}\mathbf F$ — 오른쪽에는 그 영역의 **경계에서만** 원래 함수의 값을 본다. 구간의 경계는 두 끝점, 곡선의 경계도 두 끝점, 평면영역과 곡면의 경계는 닫힌곡선, 입체의 경계는 닫힌곡면이다. 그래서 미적분학의 기본정리 → 선적분의 기본정리 → 그린 정리 → 스토크스 정리 → 발산정리가 한 줄로 이어지며, 실제로 그린 정리는 곡면이 $xy$-평면에 평평하게 놓인 스토크스 정리이고, 발산정리는 그린 정리의 플럭스 형태를 한 차원 올린 것이다. 이 표를 외우기보다 "도함수를 안에서 적분 = 원함수를 경계에서 적분"이라는 한 문장을 기억하는 편이 낫다.

## F. 공통과제 문항 (4차 공통과제)

- **과제 제출 문항**: 36, 37, 38
- **학습 참고 문항**: 2~9, 10, 11~14, 15~19, 24, 25, 26-(a), 27~30, 31~40

※ 이 번호들은 §16.10 자체가 아니라 **Chapter 16 Review Exercises**(PDF p.1285~) 번호다. 과제표에는 "16.10 Summary (Review)" 행으로 실려 있다. 사이트의 §16.10 페이지에서는 번호만 안내하고 문제·풀이는 싣지 않는다.
