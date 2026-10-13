#!/usr/bin/env python3
"""Structural checks for stewart/exams (run after build_exams.py).

- data: problem numbers 1..N, points sum = exam points attribute
- solutions: every problem has ko+en blocks with an answer-box; one grading-box each; no '$'
- math delimiters balanced, forbidden terms absent
- built pages: card count = problem count, ko/en toggle counts equal, unique ids, local links exist, tags balanced
Exit 1 on any error.
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from build_exams import EXAMS, parse_exam  # noqa: E402

FORBIDDEN_KO = ["잠재함수", "원통좌표", "그래디언트", "박판", "기울기벡터", "제I형", "제II형"]
VOID = {"meta", "link", "br", "img", "input", "hr", "circle", "line", "polygon", "polyline", "path", "rect", "ellipse", "use"}


class TagBalance(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.errors = [], []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack or self.stack[-1] != tag:
            self.errors.append(f"unexpected </{tag}> (open: {self.stack[-3:]})")
            if tag in self.stack:
                while self.stack and self.stack.pop() != tag:
                    pass
        else:
            self.stack.pop()


def balanced(text, a, b):
    text = text.replace("\\\\[", "")  # LaTeX row spacing like \\[2mm] is not a display delimiter
    return text.count(a) == text.count(b)


def main():
    errors, summary = [], []
    for eid, *_ in EXAMS:
        if not (ROOT / "data" / f"{eid}.html").exists():
            continue
        meta, probs, sols = parse_exam(eid)
        nums = [int(p["n"]) for p in probs]
        if nums != list(range(1, len(nums) + 1)):
            errors.append(f"{eid}: problem numbers {nums}")
        pts = sum(int(p["pts"]) for p in probs)
        if str(pts) != meta.get("points"):
            errors.append(f"{eid}: points sum {pts} != {meta.get('points')}")
        n_sol = 0
        for p in probs:
            for w in FORBIDDEN_KO:
                if w in p["ko"] or w in p["title_ko"]:
                    errors.append(f"{eid} #{p['n']} data ko: forbidden term {w}")
            for lang in ("ko", "en"):
                body = p[lang]
                if not (balanced(body, r"\(", r"\)") and balanced(body, r"\[", r"\]")):
                    errors.append(f"{eid} #{p['n']} statement {lang}: unbalanced math delimiters")
            ko, en = sols.get((p["n"], "ko")), sols.get((p["n"], "en"))
            if ko is None and en is None:
                continue
            if ko is None or en is None:
                errors.append(f"{eid} #{p['n']}: missing {'ko' if ko is None else 'en'} solution")
                continue
            n_sol += 1
            for lang, body in (("ko", ko), ("en", en)):
                tag = f"{eid} #{p['n']} {lang}"
                if "$" in body:
                    errors.append(f"{tag}: '$' delimiter")
                if not (balanced(body, r"\(", r"\)") and balanced(body, r"\[", r"\]")):
                    errors.append(f"{tag}: unbalanced math delimiters")
                if "answer-box" not in body:
                    errors.append(f"{tag}: no answer-box")
                if body.count("grading-box") != 1:
                    errors.append(f"{tag}: grading-box count {body.count('grading-box')}")
                if lang == "ko":
                    for w in FORBIDDEN_KO:
                        if w in body:
                            errors.append(f"{tag}: forbidden term {w}")
                if r"d\sigma" in body:
                    errors.append(f"{tag}: d\\sigma")
        page = (ROOT / f"{eid}.html").read_text(encoding="utf-8")
        cards = re.findall(r'<article class="card ex-card exam-problem" id="([^"]+)"', page)
        if len(cards) != len(probs) or len(set(cards)) != len(cards):
            errors.append(f"{eid}.html: cards {len(cards)} vs problems {len(probs)} / duplicate ids")
        if page.count('class="proof-content"') != page.count('class="en-proof-content"'):
            errors.append(f"{eid}.html: ko/en toggle count mismatch")
        tb = TagBalance()
        tb.feed(re.sub(r"<script.*?</script>", "", page, flags=re.S))
        if tb.errors or [t for t in tb.stack if t not in ("html", "body")]:
            errors.append(f"{eid}.html: tag balance {tb.errors[:3]} open={tb.stack[-4:]}")
        for href in re.findall(r'href="([^"#:]+)(?:#[^"]*)?"', page):
            if href.startswith("http") or href.startswith("//"):
                continue
            if not (ROOT / href).resolve().exists():
                errors.append(f"{eid}.html: broken link {href}")
        summary.append(f"{eid}: {len(probs)} problems, {pts} pts, solutions {n_sol}/{len(probs)}")
    idx = (ROOT / "index.html").read_text(encoding="utf-8")
    for href in re.findall(r'href="([^"#:]+)"', idx):
        if not href.startswith("http") and not (ROOT / href).resolve().exists():
            errors.append(f"index.html: broken link {href}")
    print("\n".join(summary))
    if errors:
        print(f"\n{len(errors)} error(s):")
        print("\n".join("  - " + e for e in errors))
        return 1
    print("\nOK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
