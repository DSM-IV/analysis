# 기출 풀이 작성 브리프 (stewart/exams)

미적분학및연습II(MATH162) 지난 시험의 **자체 풀이**를 한국어·영어로 작성한다. 학생이 시험 직전에 보고 "답안지에 이렇게 쓰면 된다"를 익히는 용도다.

## 입력과 출력
- 문제: `stewart/exams/data/<id>.html` (읽기 전용 — 문제 문장·번호를 바꾸지 말 것. 전사 오류가 의심되면 보고만).
- 원본 시험지 이미지(확인용): `/private/tmp/claude-501/-Users-chalrs-analysis/260387b9-67de-47e0-a8ba-65192faa8bb0/scratchpad/exams/png/<id>-<쪽>.png` (5쪽).
- **출력: `stewart/exams/solutions/<id>.html` 하나만 쓴다.** 형식:

```html
<sol n="1" lang="ko">
…한국어 풀이 HTML…
</sol>
<sol n="1" lang="en">
…English solution HTML…
</sol>
```
문항마다 ko·en 두 블록, 문항 번호는 data 파일의 `n`과 같다. 다른 파일(HTML 페이지, data, CSS)은 수정하지 않는다. 다 쓴 뒤 `python3 stewart/exams/build_exams.py`를 실행해 "solutions 10/10"이 나오는지 확인한다.

## 풀이 HTML 규칙
- 수식: 인라인 `\( … \)`, 디스플레이 `\[ … \]`. `$` 금지. 긴 식은 `\begin{aligned} … \\ … \end{aligned}`로 줄을 나눠 휴대폰 폭에서도 넘치지 않게 한다(한 줄 ≈ 45자 이하).
- 소문항이 있으면 `<h4>(a)</h4>`, `<h4>(b)</h4>`로 나눈다.
- 본문은 `<p>`와 디스플레이 수식. 단계가 길면 `<ol><li>`도 가능.
- 각 소문항(또는 문항) 끝에 답 상자:
  - ko: `<div class="answer-box"><p><strong>답.</strong> …</p></div>`
  - en: `<div class="answer-box"><p><strong>Answer.</strong> …</p></div>`
- 문항 맨 끝에 채점 포인트 상자 하나:
  - ko: `<div class="grading-box"><p><strong>채점 포인트 · 자주 하는 실수</strong></p><ul><li>…</li></ul></div>`
  - en: `<div class="grading-box"><p><strong>Key steps · Common mistakes</strong></p><ul><li>…</li></ul></div>`
  - 2–4개 항목: 답안에 꼭 있어야 할 단계(예: 판정법 이름, 경계 검사, 극한 경로 두 개), 자주 틀리는 지점.
- 그림: "Sketch the region" 문항, 적분영역·입체 영역이 핵심인 문항(극좌표 변환, 순서 바꾸기)은 **인라인 SVG**를 ko 블록에 넣는다(en 블록에도 같은 SVG를 넣되 라벨은 영어/수식만). 형식:
  `<figure class="fig"><svg viewBox="0 0 W H" role="img" aria-label="…">…</svg><figcaption>…</figcaption></figure>`
  - 좌표축은 회색(`#8b95a1`), 영역 채우기 `#0aa65b` opacity .18, 경계선 `#0a8a4c` 1.5px, 라벨 `font-size="12"` `fill="#333"`. 단순하고 정확하게(교점 좌표를 계산해 찍을 것). 스캔·외부 이미지 금지.
- 표기: 문제의 표기를 그대로 쓴다. 공식 이름은 Stewart 기준(예: Second Derivatives Test, Clairaut's Theorem, Fubini's Theorem). 한국어 용어는 `stewart/GLOSSARY.md`를 따른다(편도함수, 방향도함수, 기울기 벡터, 접평면, 선형근사/선형화, 이계도함수 판정법, 임계점, 안장점, 라그랑주 승수, 반복적분, 극좌표, 원기둥좌표, 구면좌표, 질량중심, 얇은 판(lamina), 제1형/제2형 영역 — 로마숫자 금지; 금칙어: 그래디언트·원통좌표·박판).
- 수식 규약(검증에서 반복 지적): 구면좌표는 `\phi`(`\varphi` 금지)와 적분 순서 `d\rho\,d\theta\,d\phi`; 부등호 `<`는 HTML과 충돌하므로 수식 안에서 `\lt`; "조임정리"(붙여 씀); 그림 라벨이 선·축과 겹치지 않게 배치.
- **구면좌표 적분 순서 예외:** 기본은 `d\rho\,d\theta\,d\phi`(Stewart)이지만, \(\phi\)의 구간이 \(\theta\)에 의존하면(예: \(\phi\ge\cot^{-1}(\sin\theta)\)) 반드시 `d\rho\,d\phi\,d\theta`로 쓴다 — 이것은 금칙어 위반이 아니므로 "고치지" 말 것. 경계가 순서와 맞는지가 우선.
- 한국어 문체: 평서체(‘-다’). en은 같은 내용의 자연스러운 영어(번역투 금지). ko·en의 수식·단계·답은 일치해야 한다.

## 풀이 품질 기준 (시험 답안 수준)
- "풀이 과정을 자세히 기술"하는 시험이다. 생략 없이, 답안지에 그대로 옮겨 쓸 수 있는 흐름으로 쓴다. 단, 장황한 설명은 피한다(문항당 ko 기준 대략 8–25줄).
- 극한: 존재하면 부등식(squeeze)·극좌표 등 **엄밀한 근거**로, 존재하지 않으면 **서로 다른 값을 주는 두 경로**를 명시.
- 극값: 임계점 전부, 판별식 \(D=f_{xx}f_{yy}-f_{xy}^2\) 표, 각 점의 분류와 함숫값.
- 최댓값·최솟값(닫힌 유계 영역): 내부 임계점 + 경계(라그랑주 또는 매개화) + 후보 비교.
- 라그랑주: 연립방정식을 **모든 경우**(예: \(x=0\) 또는 \(\lambda=\dots\))로 나눠 풀고 후보표로 비교.
- 적분: 영역을 부등식으로 쓰고, 좌표 변환·순서 변환의 경계를 근거와 함께 제시. 대칭으로 0이 되는 항은 대칭 근거를 쓴다.
- 최종 답은 정확값(필요하면 근삿값 병기).

## 기준값
브리프 아래 표의 값은 감독자가 sympy·수치적분으로 계산한 기준값이다. **풀이는 직접 유도**하고 마지막에 기준값과 맞는지 확인한다. 끝까지 불일치하면 억지로 맞추지 말고 최종 보고에 "불일치: 문항, 내 값, 근거"를 적는다.

## 완료 보고 (최종 메시지)
- 작성 문항 수, build 결과 줄, SVG를 넣은 문항, 기준값 불일치·전사 의심 사항(없으면 "없음"). 200단어 이내.
