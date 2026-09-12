#!/usr/bin/env python3
"""Build verified Stewart exercise pages from exercise-content/*.json.

Only content marked ``math-verified`` is accepted.  The source strings are
plain text (with MathJax ``\\(...\\)`` and ``\\[...\\]`` allowed), never HTML.

Usage:
    python3 stewart/build_exercises.py
    python3 stewart/build_exercises.py --check
    python3 stewart/build_exercises.py --section 14.3
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
CONTENT_DIR = HERE / "exercise-content"
OUTPUT_DIR = HERE / "exercises"
ID_RE = re.compile(r"^[a-z0-9]+(?:[.-][a-z0-9]+)*$")
HTML_TAG_RE = re.compile(r"<\s*/?\s*[A-Za-z][^>]*>")
PLACEHOLDER_RE = re.compile(r"\[(?:TBD|TODO|번역 예정|해석 예정)\]", re.I)
MATH_RE = re.compile(r"(?<!\\)\\\((.*?)\\\)|(?<!\\)\\\[(.*?)\\\]", re.S)
KINDS = {
    "exercise": {"ko": "연습문제", "en": "Exercises", "card": "EXERCISE"},
    "review": {"ko": "복습문제", "en": "Review Exercises", "card": "REVIEW"},
    "problems-plus": {"ko": "심화문제", "en": "Problems Plus", "card": "PROBLEMS PLUS"},
}


class ContentError(ValueError):
    """A content file is incomplete or does not meet the publishing contract."""


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if "id" in values and values["id"] is not None:
            self.ids.append(values["id"])
        if tag == "a" and values.get("href"):
            self.hrefs.append(values["href"])


def fail(where: str, message: str) -> None:
    raise ContentError(f"{where}: {message}")


def require_string(value: Any, where: str) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(where, "must be a non-empty string")
    prose = re.sub(r"\\\(.*?\\\)|\\\[.*?\\\]", "", value, flags=re.S)
    if HTML_TAG_RE.search(prose):
        fail(where, "HTML markup is not allowed; use plain text and MathJax only")
    if PLACEHOLDER_RE.search(value):
        fail(where, "contains a publishing placeholder")
    return value.strip()


def require_pair(value: Any, where: str) -> dict[str, str]:
    if not isinstance(value, dict) or set(value) != {"ko", "en"}:
        fail(where, "must contain exactly ko and en")
    return {
        "ko": require_string(value["ko"], f"{where}.ko"),
        "en": require_string(value["en"], f"{where}.en"),
    }


def require_matching_math(pair: dict[str, str], where: str) -> None:
    """Require the problem and final-answer formulas to match across languages."""
    def formulas(text: str) -> list[str]:
        return [re.sub(r"\s+", "", re.sub(r"\\text\{[^{}]*\}", "", inline or display)) for inline, display in MATH_RE.findall(text)]
    if formulas(pair["ko"]) != formulas(pair["en"]):
        fail(where, "Korean and English MathJax expressions must match in order")


def require_pages(value: Any, where: str) -> list[int]:
    if not isinstance(value, list) or not value:
        fail(where, "must be a non-empty list of page numbers")
    if any(not isinstance(page, int) or page < 1 for page in value):
        fail(where, "must contain positive integer page numbers")
    return value


def normalize_number(value: Any, where: str) -> str:
    number = str(value)
    if not re.fullmatch(r"\d+(?:[.-][A-Za-z0-9]+)?", number):
        fail(where, "must be a problem number, optionally with a subpart")
    return number


def main_number(number: str) -> str:
    """Return the source problem number, ignoring an optional subpart label."""
    return re.split(r"[.-]", number, maxsplit=1)[0]


def require_figure(value: Any, where: str) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != {"src", "alt", "caption"}:
        fail(where, "must contain exactly src, alt, and caption")
    src = require_string(value["src"], f"{where}.src")
    prefix = "../exercise-content/assets/"
    if not src.startswith(prefix) or not src.endswith(".svg") or ".." in src[len(prefix):]:
        fail(f"{where}.src", "must be a local SVG below ../exercise-content/assets/")
    asset = (OUTPUT_DIR / src).resolve()
    assets_root = (CONTENT_DIR / "assets").resolve()
    if not asset.is_relative_to(assets_root) or not asset.is_file():
        fail(f"{where}.src", "does not point to an existing local SVG")
    return {"src": src, "alt": require_pair(value["alt"], f"{where}.alt"), "caption": require_pair(value["caption"], f"{where}.caption")}


def require_source(value: Any, where: str, *, root: bool) -> dict[str, Any]:
    if not isinstance(value, dict):
        fail(where, "must be an object")
    required = ("title", "edition", "language", "printedPages", "pdfPages") if root else ("printedPage", "pdfPage")
    missing = [key for key in required if key not in value]
    if missing:
        fail(where, f"is missing {', '.join(missing)}")
    if root:
        edition = value["edition"]
        if isinstance(edition, int) and edition > 0:
            edition_text = str(edition)
        else:
            edition_text = require_string(edition, f"{where}.edition")
        return {
            "title": require_string(value["title"], f"{where}.title"),
            "edition": edition_text,
            "language": require_string(value["language"], f"{where}.language"),
            "printedPages": require_pages(value["printedPages"], f"{where}.printedPages"),
            "pdfPages": require_pages(value["pdfPages"], f"{where}.pdfPages"),
        }
    for key in required:
        if not isinstance(value[key], int) or value[key] < 1:
            fail(f"{where}.{key}", "must be a positive integer")
    return {key: value[key] for key in required}


def validate_document(raw: Any, path: Path) -> dict[str, Any]:
    where = str(path.relative_to(HERE))
    if not isinstance(raw, dict):
        fail(where, "top level must be an object")
    for key in ("section", "source", "exercises"):
        if key not in raw:
            fail(where, f"is missing {key}")
    section = require_string(raw["section"], f"{where}.section")
    if not re.fullmatch(r"\d+\.\d+", section):
        fail(f"{where}.section", "must look like 14.3")
    if not isinstance(raw["exercises"], list) or not raw["exercises"]:
        fail(f"{where}.exercises", "must be a non-empty list")
    kind = raw.get("kind", raw.get("scope", {}).get("kind", "exercise"))
    if kind not in KINDS:
        fail(f"{where}.kind", "must be exercise, review, or problems-plus")

    exercises: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    seen_numbers: set[str] = set()
    required = ("id", "number", "subparts", "topic", "statement", "hint", "steps", "answer", "check", "status")
    for index, item in enumerate(raw["exercises"], start=1):
        item_where = f"{where}.exercises[{index}]"
        if not isinstance(item, dict):
            fail(item_where, "must be an object")
        missing = [key for key in required if key not in item]
        if missing:
            fail(item_where, f"is missing {', '.join(missing)}")
        exercise_id = require_string(item["id"], f"{item_where}.id")
        if not ID_RE.fullmatch(exercise_id):
            fail(f"{item_where}.id", "may contain only lowercase letters, digits, dots, and hyphens")
        if exercise_id in seen_ids:
            fail(f"{item_where}.id", "duplicates another exercise id")
        seen_ids.add(exercise_id)
        number = normalize_number(item["number"], f"{item_where}.number")
        if number in seen_numbers:
            fail(f"{item_where}.number", "duplicates another exercise number")
        seen_numbers.add(number)
        if not isinstance(item["subparts"], list) or any(not isinstance(part, str) for part in item["subparts"]):
            fail(f"{item_where}.subparts", "must be a list of plain-text labels")
        subparts = [require_string(part, f"{item_where}.subparts[{part_index}]") for part_index, part in enumerate(item["subparts"], 1)]
        if not isinstance(item["steps"], dict) or set(item["steps"]) != {"ko", "en"}:
            fail(f"{item_where}.steps", "must contain exactly ko and en step lists")
        steps: dict[str, list[str]] = {}
        for language in ("ko", "en"):
            language_steps = item["steps"][language]
            if not isinstance(language_steps, list) or not language_steps:
                fail(f"{item_where}.steps.{language}", "must be a non-empty list")
            steps[language] = [
                require_string(step, f"{item_where}.steps.{language}[{step_index}]")
                for step_index, step in enumerate(language_steps, 1)
            ]
        if item["status"] != "math-verified":
            fail(f"{item_where}.status", "must be math-verified before publication")

        statement = require_pair(item["statement"], f"{item_where}.statement")
        answer = require_pair(item["answer"], f"{item_where}.answer")
        # Statements can split math spans differently in translation. Their
        # equivalence is checked against the source during content review.
        require_matching_math(answer, f"{item_where}.answer")
        normalized: dict[str, Any] = {
            "id": exercise_id,
            "number": number,
            "subparts": subparts,
            "topic": require_pair(item["topic"], f"{item_where}.topic"),
            "statement": statement,
            "hint": require_pair(item["hint"], f"{item_where}.hint"),
            "steps": steps,
            "answer": answer,
            "check": require_pair(item["check"], f"{item_where}.check"),
            "status": item["status"],
        }
        if "source" in item:
            normalized["source"] = require_source(item["source"], f"{item_where}.source", root=False)
        if "conceptHref" in item:
            href = require_string(item["conceptHref"], f"{item_where}.conceptHref")
            if not href.startswith("../") or any(character in href for character in '"<>'):
                fail(f"{item_where}.conceptHref", "must be a safe relative link beginning ../")
            normalized["conceptHref"] = href
        if "figure" in item:
            normalized["figure"] = require_figure(item["figure"], f"{item_where}.figure")
        exercises.append(normalized)

    normalized_document = {
        "section": section,
        "kind": kind,
        "source": require_source(raw["source"], f"{where}.source", root=True),
        "exercises": exercises,
    }
    if "scope" in raw:
        scope = raw["scope"]
        if not isinstance(scope, dict) or set(scope) != {"kind", "numbers", "total", "note"}:
            fail(f"{where}.scope", "must contain exactly kind, numbers, total, and note")
        if scope["kind"] != kind:
            fail(f"{where}.scope.kind", "must match the document kind")
        if not isinstance(scope["numbers"], list) or any(not isinstance(number, int) for number in scope["numbers"]):
            fail(f"{where}.scope.numbers", "must be a list of integer problem numbers")
        exercise_numbers = [int(exercise["number"]) for exercise in exercises if exercise["number"].isdigit()]
        if scope["numbers"] != exercise_numbers:
            fail(f"{where}.scope.numbers", "must match the published exercise numbers in order")
        if scope["total"] != len(exercises):
            fail(f"{where}.scope.total", "must match the number of published exercises")
        normalized_document["scope"] = {
            "kind": kind,
            "numbers": scope["numbers"],
            "total": scope["total"],
            "note": require_pair(scope["note"], f"{where}.scope.note"),
        }
    return normalized_document


def validate_manifest(raw: Any, path: Path) -> list[dict[str, Any]]:
    """Validate the inventory owned by the coordinator, not by page authors.

    ``completedNumbers`` is the publishing ledger.  A content document must
    contain exactly that set, so a forgotten or duplicated item fails the build.
    ``total`` may be absent or null until the source inventory is complete.
    """
    where = str(path.relative_to(HERE))
    if not isinstance(raw, dict) or set(raw) != {"sections"}:
        fail(where, "must contain exactly a sections list")
    if not isinstance(raw["sections"], list) or not raw["sections"]:
        fail(f"{where}.sections", "must be a non-empty list")
    sections: list[dict[str, Any]] = []
    seen_sections: set[str] = set()
    for index, item in enumerate(raw["sections"], 1):
        item_where = f"{where}.sections[{index}]"
        if not isinstance(item, dict):
            fail(item_where, "must be an object")
        required = {"section", "completedNumbers"}
        if not required.issubset(item):
            fail(item_where, "is missing section or completedNumbers")
        allowed = {"section", "kind", "title", "total", "expectedNumbers", "completedNumbers"}
        extra = set(item) - allowed
        if extra:
            fail(item_where, "has unsupported fields: " + ", ".join(sorted(extra)))
        section = require_string(item["section"], f"{item_where}.section")
        if not re.fullmatch(r"\d+\.\d+", section):
            fail(f"{item_where}.section", "must look like 15.6")
        if section in seen_sections:
            fail(f"{item_where}.section", "duplicates another section")
        seen_sections.add(section)
        kind = item.get("kind", "exercise")
        if kind not in KINDS:
            fail(f"{item_where}.kind", "must be exercise, review, or problems-plus")
        title = require_pair(item["title"], f"{item_where}.title") if "title" in item else {"ko": KINDS[kind]["ko"], "en": KINDS[kind]["en"]}
        total = item.get("total")
        if total is not None and (not isinstance(total, int) or total < 0):
            fail(f"{item_where}.total", "must be a non-negative integer or null")
        completed_raw = item["completedNumbers"]
        if not isinstance(completed_raw, list):
            fail(f"{item_where}.completedNumbers", "must be a list")
        completed = [normalize_number(number, f"{item_where}.completedNumbers[{number_index}]") for number_index, number in enumerate(completed_raw, 1)]
        if len(completed) != len(set(completed)):
            fail(f"{item_where}.completedNumbers", "contains duplicate problem numbers")
        expected: list[str] | None = None
        if "expectedNumbers" in item:
            expected_raw = item["expectedNumbers"]
            if not isinstance(expected_raw, list):
                fail(f"{item_where}.expectedNumbers", "must be a list")
            expected = [normalize_number(number, f"{item_where}.expectedNumbers[{number_index}]") for number_index, number in enumerate(expected_raw, 1)]
            if len(expected) != len(set(expected)):
                fail(f"{item_where}.expectedNumbers", "contains duplicate problem numbers")
            expected_main = {main_number(number) for number in expected}
            if any(main_number(number) not in expected_main for number in completed):
                fail(f"{item_where}.completedNumbers", "contains a problem absent from expectedNumbers")
            if total is not None and total != len(expected):
                fail(f"{item_where}.total", "must equal the number of expectedNumbers")
        if total is not None and len({main_number(number) for number in completed}) > total:
            fail(f"{item_where}.completedNumbers", "has more distinct problem numbers than total")
        sections.append({
            "section": section,
            "kind": kind,
            "title": title,
            "total": total,
            "expectedNumbers": expected,
            "completedNumbers": completed,
        })
    return sections


def read_manifest() -> list[dict[str, Any]] | None:
    path = CONTENT_DIR / "manifest.json"
    if not path.exists():
        return None
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ContentError(f"{path.relative_to(HERE)}: invalid JSON: {error}") from error
    return [entry for entry in validate_manifest(raw, path) if entry["kind"] == "exercise"]


def apply_manifest(documents: list[dict[str, Any]], manifest: list[dict[str, Any]] | None) -> list[dict[str, Any]]:
    if manifest is None:
        for document in documents:
            document["display"] = {"title": {"ko": KINDS[document["kind"]]["ko"], "en": KINDS[document["kind"]]["en"]}, "total": None}
        return [{
            "section": document["section"], "kind": document["kind"],
            "title": document["display"]["title"], "total": None,
            "completedNumbers": [exercise["number"] for exercise in document["exercises"]],
        } for document in documents]

    document_by_section = {document["section"]: document for document in documents}
    manifest_by_section = {entry["section"]: entry for entry in manifest}
    unknown_documents = sorted(set(document_by_section) - set(manifest_by_section))
    if unknown_documents:
        raise ContentError("content exists for sections absent from manifest: " + ", ".join(unknown_documents))
    for entry in manifest:
        document = document_by_section.get(entry["section"])
        if entry["completedNumbers"] and document is None:
            raise ContentError(f"manifest section {entry['section']}: completedNumbers has no content document")
        if document is None:
            continue
        actual = [exercise["number"] for exercise in document["exercises"]]
        if document["kind"] != entry["kind"]:
            raise ContentError(f"manifest section {entry['section']}: kind does not match content document")
        if actual != entry["completedNumbers"]:
            raise ContentError(
                f"manifest section {entry['section']}: completedNumbers must exactly match content numbers "
                f"(manifest: {', '.join(entry['completedNumbers']) or 'none'}; content: {', '.join(actual) or 'none'})"
            )
        document["display"] = {"title": entry["title"], "total": entry["total"]}
    return manifest


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def paragraphs(value: str) -> str:
    return "\n".join(f"<p>{esc(part).replace(chr(10), '<br>')}</p>" for part in re.split(r"\n\s*\n", value))


def page_range(pages: list[int]) -> str:
    return ", ".join(str(page) for page in pages)


def published_problem_count(numbers: list[str]) -> int:
    return len({main_number(number) for number in numbers})


def per_exercise_source(exercise: dict[str, Any], document: dict[str, Any]) -> str:
    item_label = {"exercise": "Exercise", "review": "Review", "problems-plus": "Problems Plus"}[document["kind"]]
    source = exercise.get("source")
    if source:
        return f"{item_label} {esc(exercise['number'])} · p. {source['printedPage']} · PDF p. {source['pdfPage']}"
    root = document["source"]
    return f"{item_label} {esc(exercise['number'])} · pp. {page_range(root['printedPages'])} · PDF pp. {page_range(root['pdfPages'])}"


def subparts_markup(exercise: dict[str, Any]) -> str:
    if not exercise["subparts"] or all(re.fullmatch(r"[a-zA-Z0-9().-]+", part) for part in exercise["subparts"]):
        return ""
    return "<ul>" + "".join(f"<li>{esc(part)}</li>" for part in exercise["subparts"]) + "</ul>"


def figure_markup(exercise: dict[str, Any], language: str) -> str:
    figure = exercise.get("figure")
    if not figure:
        return ""
    return f'<figure class="fig"><img src="{esc(figure["src"])}" alt="{esc(figure["alt"][language])}" style="max-width:100%;height:auto"><figcaption>{esc(figure["caption"][language])}</figcaption></figure>'


def panel(exercise: dict[str, Any], language: str) -> str:
    korean = language == "ko"
    panel_class = "ko-panel" if korean else "en-panel"
    formal_class = "formal" if korean else "en-formal"
    label_class = "ko-label" if korean else "en-label"
    lang_attr = "" if korean else ' lang="en"'
    label = "한국어" if korean else "English"
    statement_label = "문제 요약" if korean else "Problem summary"
    hint_show, hint_hide = ("힌트 보기", "힌트 접기") if korean else ("Hint", "Hide Hint")
    solution_show, solution_hide = ("풀이 보기", "풀이 접기") if korean else ("Solution", "Hide Solution")
    hint_label = "힌트" if korean else "Hint"
    solution_label = "해설" if korean else "Solution"
    answer_label = "최종 답" if korean else "Final answer"
    check_label = "검산·주의점" if korean else "Check and conditions"
    steps = "".join(f"<li>{paragraphs(step)}</li>" for step in exercise["steps"][language])
    return f'''    <div class="{panel_class}"{lang_attr}>
      <span class="panel-label {label_class}">{label}</span>
      <div class="{formal_class}">
        <p><strong>{statement_label}</strong></p>
        {paragraphs(exercise["statement"][language])}
        {subparts_markup(exercise)}
        {figure_markup(exercise, language)}
      </div>
      <button class="proof-toggle" type="button" onclick="toggleProof(this)" data-show="{hint_show}" data-hide="{hint_hide}"><span class="arrow">&#9654;</span> {hint_show}</button>
      <div class="{'proof-content' if korean else 'en-proof-content'}">
        <p><strong>{hint_label}.</strong> {esc(exercise["hint"][language])}</p>
      </div>
      <button class="proof-toggle" type="button" onclick="toggleProof(this)" data-show="{solution_show}" data-hide="{solution_hide}"><span class="arrow">&#9654;</span> {solution_show}</button>
      <div class="{'proof-content' if korean else 'en-proof-content'}">
        <p><strong>{solution_label}.</strong></p>
        <ol>{steps}</ol>
        <div class="formal-box"><p><strong>{answer_label}.</strong> {esc(exercise["answer"][language])}</p></div>
        <div class="formal-box"><p><strong>{check_label}.</strong> {esc(exercise["check"][language])}</p></div>
      </div>
    </div>'''


def exercise_card(exercise: dict[str, Any], document: dict[str, Any]) -> str:
    concept = ""
    if "conceptHref" in exercise:
        concept = f'\n      <a class="ref-link" href="{esc(exercise["conceptHref"])}">개념 보기 · Concept</a>'
    return f'''<article class="card ex-card" id="{esc(exercise["id"])}">
  <div class="card-head">
    <span class="ex-num">{KINDS[document["kind"]]["card"]} {esc(exercise["number"])}</span>
    <span class="ex-title">{esc(exercise["topic"]["ko"])}<em>{esc(exercise["topic"]["en"])}</em><span class="src-ref">{per_exercise_source(exercise, document)}</span></span>{concept}
  </div>
  <div class="card-body">
{panel(exercise, "ko")}
{panel(exercise, "en")}
  </div>
</article>'''


def source_label(entry: dict[str, Any]) -> str:
    return "§" + entry["section"] if entry["kind"] == "exercise" else entry["section"].split(".")[0] + "장"


def section_page(document: dict[str, Any]) -> str:
    section = document["section"]
    source = document["source"]
    labels = KINDS[document["kind"]]
    reference = source_label(document)
    display = document["display"]
    title = display["title"]
    total = display["total"]
    published_count = published_problem_count([exercise["number"] for exercise in document["exercises"]])
    progress = f"검증 완료 {published_count} / 전체 {total}문항" if total is not None else f"검증 완료 {published_count}문항 · 전체 문항 수 확인 중"
    cards = "\n\n".join(exercise_card(exercise, document) for exercise in document["exercises"])
    toc = "\n".join(
        f'      <li><a href="#{esc(exercise["id"])}"><span class="toc-num">{esc(labels["card"][:3])} {esc(exercise["number"])}</span>{esc(exercise["topic"]["ko"])} <em>{esc(exercise["topic"]["en"])}</em></a></li>'
        for exercise in document["exercises"]
    )
    course = 1 if int(section.split(".")[0]) <= 13 else 2
    course_href = f"../../calc{course}/index.html"
    course_label = f"미적분학 {course}"
    exercise_index = "../../calc1/stewart.html" if course == 1 else "index.html"
    note_name = f's{section.replace(".", "-")}.html'
    note_href = "../" + note_name if (HERE / note_name).exists() else course_href
    note_ko = f"§{section} 개념 페이지" if (HERE / note_name).exists() else "관련 개념 목록"
    note_en = f"§{section} concept page" if (HERE / note_name).exists() else "concept index"
    nav = f'      <a href="{note_href}" class="active">{esc(reference)}</a>'
    scope_note = ""
    if "scope" in document:
        scope_note = f'''\n  <div class="card note-card">
    <div class="card-body">
      <div class="ko-panel"><span class="panel-label ko-label">공개 범위</span><div class="formal">{paragraphs(document["scope"]["note"]["ko"])}</div></div>
      <div class="en-panel" lang="en"><span class="panel-label en-label">Published scope</span><div class="en-formal">{paragraphs(document["scope"]["note"]["en"])}</div></div>
    </div>
  </div>'''
    return f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(reference)} {esc(labels["ko"])}와 해설 | Stewart 미적분학 교재 노트</title>
<meta name="description" content="Stewart Calculus {esc(source["edition"])} {esc(reference)}의 검증된 {esc(labels["ko"])} 해설입니다.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://univmathsurvive.com/stewart/exercises/s{section.replace('.', '-')}.html">
<script>
MathJax = {{
  tex: {{inlineMath: [['\\\\(', '\\\\)']], displayMath: [['\\\\[', '\\\\]']], packages: {{'[+]': ['ams']}}}},
  options: {{skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre']}}
}};
</script>
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-chtml.min.js"></script>
<link rel="stylesheet" media="print" onload="this.media='all'" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link rel="stylesheet" href="../style.css">
<link rel="stylesheet" href="exercise.css">
</head>
<body>

<a href="#main-content" class="skip-link">본문으로 건너뛰기</a>

<nav class="site-nav" aria-label="사이트 탐색">
  <div class="nav-inner">
    <a class="logo" href="../../index.html" aria-label="대학수학생존 홈"><span class="logo-mark" aria-hidden="true">√</span>대학수학생존</a>
    <div class="nav-links">
      <a href="../index.html">Stewart</a>
      <a href="{course_href}">{course_label}</a>
      <span class="nav-sep">·</span>
{nav}
    </div>
  </div>
</nav>

<header>
  <p class="subtitle">{esc(title["ko"])} · {esc(title["en"])} · {esc(reference)}</p>
  <h1>{esc(reference)} {esc(labels["ko"])}와 해설<span>{esc(labels["en"])} and Solutions</span></h1>
  <p class="header-desc">교재 문제를 학습 목적으로 요약하고, 수학 검증을 마친 자체 해설을 한국어와 영어로 제공합니다.</p>
  <div class="lang-badge"><span class="ko">한국어</span><span class="en">English</span></div>
</header>

<div class="lang-toggle-bar">
  <label><input type="checkbox" id="toggle-ko" checked onchange="toggleLang()">한국어 표시</label>
  <span class="sep">|</span>
  <label><input type="checkbox" id="toggle-en" checked onchange="toggleLang()">English 표시</label>
  <span class="sep">|</span>
  <span style="color:var(--ink-faint); font-size:.7rem;">왼쪽: 한국어 · 오른쪽: English</span>
</div>

<main id="main-content" role="main">
  <nav class="toc" aria-label="문제 목차">
    <h3>{esc(labels["ko"])} · {esc(labels["en"])}</h3>
    <ol>
{toc}
    </ol>
  </nav>

  <div class="card note-card">
    <div class="card-body">
      <div class="ko-panel"><span class="panel-label ko-label">연결</span><div class="formal"><p><a href="{note_href}">{esc(note_ko)}</a>에서 정의와 예제를 확인할 수 있습니다. <a href="{exercise_index}">연습문제 목록</a>으로 돌아갑니다.</p></div></div>
      <div class="en-panel" lang="en"><span class="panel-label en-label">Links</span><div class="en-formal"><p>Review definitions and examples on the <a href="{note_href}">{esc(note_en)}</a>, or return to the <a href="{exercise_index}">exercise index</a>.</p></div></div>
    </div>
  </div>

  <div class="section-title"><h2>검증된 해설 · Verified solutions</h2></div>
  <p class="intro-text">출처: {esc(source["title"])}, {esc(source["edition"])}, {esc(source["language"])} · 인쇄본 쪽 {page_range(source["printedPages"])} / PDF 쪽 {page_range(source["pdfPages"])} · {progress}</p>
{scope_note}

{cards}
</main>

<footer class="site-footer">
  <div>
    <a href="../../index.html">홈</a>
    <a href="../index.html">Stewart 홈</a>
    <a href="{course_href}">{course_label}</a>
    <a href="../../about.html">소개</a>
    <a href="../../privacy.html">개인정보처리방침</a>
  </div>
  <p class="footer-copy">Stewart, <em>Calculus</em>의 내용을 학습 목적으로 재서술·해석한 개인 노트입니다. 원문 텍스트·그림은 수록하지 않습니다.</p>
</footer>

<script src="../common.js"></script>
<button class="scroll-top" id="scrollTop" type="button" onclick="window.scrollTo({{top:0,behavior:'smooth'}})" aria-label="맨 위로">&#8593;</button>
</body>
</html>
'''


def progress_label(entry: dict[str, Any]) -> str:
    completed = published_problem_count(entry["completedNumbers"])
    if entry["total"] is None:
        return f"검증 완료 {completed}문항 · 전체 문항 수 확인 중"
    return f"검증 완료 {completed} / 전체 {entry['total']}문항"


def index_page(entries: list[dict[str, Any]], documents: list[dict[str, Any]]) -> str:
    published_sections = {document["section"] for document in documents}
    total_published = sum(len(document["exercises"]) for document in documents)
    rows = "\n".join(
        f'''    <article class="chapter-card" id="exercise-card-s{entry["section"].replace('.', '-')}">
      <div class="card-top">
        <span class="ch-num">{esc(source_label(entry))}</span>
        <h3>{esc(entry["title"]["ko"])} {esc(KINDS[entry["kind"]]["ko"])}</h3>
        <p class="ch-en-title">{esc(entry["title"]["en"])} · {esc(KINDS[entry["kind"]]["en"])}</p>
        <p class="ch-count">{progress_label(entry)} · Math verified</p>
      </div>
      <div class="card-actions">{f'<a href="s{entry["section"].replace(".", "-")}.html">문제와 해설 보기</a>' if entry["section"] in published_sections else '<span style="color:var(--ink-faint);text-align:center;padding:10px;font-size:14px;font-weight:700">검증된 문항 준비 중</span>'}</div>
    </article>'''
        for entry in entries
    )
    return f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Stewart 연습문제와 해설 | 대학수학생존</title>
<meta name="description" content="Stewart Calculus의 검증된 연습문제 해설 목록입니다.">
<link rel="stylesheet" media="print" onload="this.media='all'" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link rel="stylesheet" href="../style.css">
<link rel="stylesheet" href="exercise.css">
</head>
<body>
<a href="#main-content" class="skip-link">본문으로 건너뛰기</a>
<nav class="site-nav" aria-label="사이트 탐색"><div class="nav-inner"><a class="logo" href="../../index.html" aria-label="대학수학생존 홈"><span class="logo-mark" aria-hidden="true">√</span>대학수학생존</a><div class="nav-links"><a href="../index.html">Stewart</a><a href="index.html" class="active">연습문제</a></div></div></nav>
<header><p class="subtitle">Stewart · Calculus</p><h1>연습문제와 해설<span>Exercises and Solutions</span></h1><p class="header-desc">문제 요약, 힌트, 단계별 해설, 최종 답과 검산을 함께 제공합니다.</p><p class="header-desc">{len(documents)}개 문제 모음 · {total_published:,}문항 · 한국어·English</p></header>
<main id="main-content"><div class="section-title"><h2>절별 문제 · Browse exercises</h2></div><div class="chapter-grid">
{rows}
</div></main>
<footer class="site-footer"><div><a href="../../index.html">홈</a><a href="../index.html">Stewart 홈</a><a href="../../about.html">소개</a></div><p class="footer-copy">학습 목적으로 재서술·해석한 개인 노트입니다.</p></footer>
</body>
</html>
'''


def validate_output(page: str, expected_ids: list[str], name: str) -> None:
    parser = PageParser()
    parser.feed(page)
    parser.close()
    duplicate_ids = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
    if duplicate_ids:
        raise ContentError(f"{name}: duplicate HTML ids: {', '.join(duplicate_ids)}")
    missing_ids = sorted(set(expected_ids) - set(parser.ids))
    if missing_ids:
        raise ContentError(f"{name}: missing exercise anchors: {', '.join(missing_ids)}")
    missing_toc_links = sorted({f"#{item}" for item in expected_ids} - set(parser.hrefs))
    if missing_toc_links:
        raise ContentError(f"{name}: missing table-of-contents links: {', '.join(missing_toc_links)}")
    if "[번역 예정]" in page or "[해석 예정]" in page:
        raise ContentError(f"{name}: contains a publishing placeholder")
    if "MathJax" not in page or "toggleProof(this)" not in page:
        raise ContentError(f"{name}: MathJax or solution toggle is missing")


def read_documents(section: str | None) -> list[dict[str, Any]]:
    if not CONTENT_DIR.exists():
        raise ContentError(f"{CONTENT_DIR.relative_to(HERE)} does not exist")
    manifest = read_manifest()
    if manifest is None:
        raise ContentError("an approved exercise manifest is required before publishing content")
    approved_names = {f"s{entry['section'].replace('.', '-')}.json" for entry in manifest}
    paths = sorted(path for path in CONTENT_DIR.glob("s*.json") if path.name in approved_names)
    if section:
        requested = CONTENT_DIR / f"s{section.replace('.', '-')}.json"
        paths = [requested] if requested.exists() and requested.name in approved_names else []
    if not paths:
        raise ContentError("no verified exercise content files were found")
    documents = []
    for path in paths:
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            raise ContentError(f"{path.relative_to(HERE)}: invalid JSON: {error}") from error
        # Review and Problems Plus may remain as archived source material.
        # They must never re-enter the published exercise catalog.
        if isinstance(raw, dict) and raw.get("kind", raw.get("scope", {}).get("kind", "exercise")) != "exercise":
            continue
        document = validate_document(raw, path)
        expected_name = f"s{document['section'].replace('.', '-')}.json"
        if path.name != expected_name:
            fail(str(path.relative_to(HERE)), f"filename must be {expected_name}")
        documents.append(document)
    if not documents:
        raise ContentError("no verified ordinary exercise content was found")
    return documents


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate content and ensure generated pages are current")
    parser.add_argument("--section", help="build or check one section, for example 14.3")
    args = parser.parse_args()
    try:
        all_documents = read_documents(args.section)
        manifest = read_manifest()
        if args.section and manifest is not None:
            manifest = [entry for entry in manifest if entry["section"] == args.section]
        entries = apply_manifest(all_documents, manifest)
        documents = all_documents
        if args.section:
            documents = [document for document in all_documents if document["section"] == args.section]
            if not documents:
                raise ContentError(f"no verified content was found for section {args.section}")
        rendered: dict[Path, str] = {}
        for document in documents:
            output = OUTPUT_DIR / f"s{document['section'].replace('.', '-')}.html"
            page = section_page(document)
            validate_output(page, [exercise["id"] for exercise in document["exercises"]], str(output.relative_to(HERE)))
            rendered[output] = page
        if not args.section:
            rendered[OUTPUT_DIR / "index.html"] = index_page(entries, all_documents)
        rendered = {path: "\n".join(line.rstrip() for line in page.splitlines()) + "\n" for path, page in rendered.items()}
        if args.check:
            stale = [str(path.relative_to(HERE)) for path, page in rendered.items() if not path.exists() or path.read_text(encoding="utf-8") != page]
            if stale:
                raise ContentError("generated pages are missing or stale: " + ", ".join(stale))
            print(f"OK: {len(documents)} content file(s), {sum(len(d['exercises']) for d in documents)} verified exercise(s), generated pages are current")
            return 0
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        for path, page in rendered.items():
            path.write_text(page, encoding="utf-8")
            print(f"wrote {path.relative_to(HERE)}")
        print(f"OK: {len(documents)} section(s), {sum(len(d['exercises']) for d in documents)} verified exercise(s)")
        return 0
    except ContentError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
