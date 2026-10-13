# 기출 풀이 적대적 검증 브리프 (stewart/exams)

역할: 다른 모델이 쓴 기출 풀이를 **틀린 곳을 찾는다는 전제로** 검증하고, 확인된 오류는 직접 고친다.

## 대상
- 문제: `stewart/exams/data/<id>.html`
- 풀이: `stewart/exams/solutions/<id>.html` (`<sol n= lang=ko|en>` 블록)
- 원본 시험지 PNG: `/private/tmp/claude-501/-Users-chalrs-analysis/260387b9-67de-47e0-a8ba-65192faa8bb0/scratchpad/exams/png/<id>-1.png … -5.png`
- 규칙: `stewart/exams/SOLVER-BRIEF.md`(형식·품질 기준), `stewart/GLOSSARY.md`(용어·금칙어)

## 할 일
1. **독립 기준값**: `stewart/exams/inventory/anchor-<id>.py`를 새로 쓴다. sympy(필요하면 mpmath 수치적분)로 모든 문항·소문항의 최종 답을 **풀이를 보지 않고** 직접 계산하고 `PASS/FAIL` 표를 출력한다(풀이의 답을 상수로 적어 두고 비교). `python3 -I`로 실행해 exit 0이어야 한다. 순서 바꾸기·좌표 변환 문항은 시험 함수(예: `1+x+y^2+z`)를 넣어 원래 적분과 변환한 적분의 수치값을 비교한다. 극한 DNE는 두 경로의 극한값을, 극값 문제는 임계점·헤세 행렬·후보값을 계산한다.
2. **전사 대조**: data의 영어 원문(en)을 PNG와 문항별로 비교(지수, 부호, 적분 구간, 적분 순서 dz dx dy 등). ko 번역이 원문과 같은 수학적 내용인지 확인.
3. **논리 감사** (ko·en 둘 다): 
   - 극한 존재 증명이 실제 부등식으로 닫히는가, DNE면 두 경로가 정의역 안에서 원점으로 가는가.
   - 극값: 임계점 누락, D·f_xx 계산, 분류.
   - 최대·최소: 내부+경계 모두 검사했는가, 라그랑주 모든 경우를 풀었는가.
   - 적분: 영역 부등식·경계·자코비안(r, ρ²sinφ)·대칭 논증.
   - 중간 계산 오류(최종 답이 맞아도 중간식 오류는 CRITICAL).
   - ko와 en의 수식·답 일치, 답 상자·채점 포인트 상자 존재.
4. **SVG**: 그림의 곡선·교점·라벨이 수학적으로 맞는지(좌표 변환 후 실제 위치), 영역이 올바르게 칠해졌는지, viewBox 밖으로 나가지 않는지.
5. **형식**: `$` 사용 금지, `\(\)`/`\[\]` 짝, HTML 태그 균형, 금칙어, 긴 디스플레이 식은 aligned로 분할.
- **구면좌표 적분 순서 예외:** 기본은 `d\rho\,d\theta\,d\phi`(Stewart)이지만, \(\phi\)의 구간이 \(\theta\)에 의존하면(예: \(\phi\ge\cot^{-1}(\sin\theta)\)) 반드시 `d\rho\,d\phi\,d\theta`로 쓴다 — 이것은 금칙어 위반이 아니므로 "고치지" 말 것. 경계가 순서와 맞는지가 우선.
6. 확인된 오류는 `solutions/<id>.html`에서 **직접 수정**한다(data의 전사 오류도 확실하면 수정하되 보고에 명시). 수정 후 `python3 stewart/exams/build_exams.py` 실행.

## 보고 (최종 메시지, 300단어 이내)
- anchor 결과: 문항 수 / PASS 수 / FAIL 내역
- CRITICAL(수학 오류·답 오류·논리 결함·전사 오류) 목록과 각 수정 내용
- MINOR(문체·형식·그림 미세) 목록과 수정 여부
- 남은 의문점(없으면 "없음")
