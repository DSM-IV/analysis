#!/usr/bin/env python3
"""Insert/check bilingual worked-example supplements without rewriting page markup.

Edit example-details.json, then run this script. --check verifies coverage and
that every published supplement exactly matches its source. No dependencies.
"""
import argparse
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
BLOCK = re.compile(r'<!-- EXAMPLE-DETAIL-(KO|EN) -->.*?<!-- /EXAMPLE-DETAIL-\1 -->\n?', re.S)
MATH = re.compile(r'\$\$.*?\$\$|(?<!\$)\$(?!\$).*?(?<!\$)\$(?!\$)', re.S)


class ExampleParser(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=False)
        self.lines = [0]
        for line in source.splitlines(keepends=True):
            self.lines.append(self.lines[-1] + len(line))
        self.divs = []
        self.examples = set()
        self.proofs = {}
        self.feed(source)
        self.close()
        assert not self.divs, 'Unclosed div'

    def source_offset(self):
        line, col = self.getpos()
        return self.lines[line - 1] + col

    def handle_starttag(self, tag, attrs):
        if tag != 'div':
            return
        attrs = dict(attrs)
        classes = attrs.get('class', '').split()
        example = self.divs[-1]['example'] if self.divs else None
        if 'exam-card' in classes:
            example = attrs['id']
            assert example not in self.examples, f'Duplicate example {example}'
            self.examples.add(example)
        node = {'example': example, 'proof': None, 'qed': None}
        if example and ('proof-content' in classes or 'en-proof-content' in classes):
            node['proof'] = (example, 'en' if 'en-proof-content' in classes else 'ko')
        if 'qed' in classes:
            for parent in reversed(self.divs):
                if parent['proof']:
                    parent['qed'] = self.source_offset()
                    break
        self.divs.append(node)

    def handle_endtag(self, tag):
        if tag != 'div':
            return
        assert self.divs, 'Unexpected closing div'
        node = self.divs.pop()
        if node['proof']:
            assert node['proof'] not in self.proofs, f'Duplicate solution {node["proof"]}'
            self.proofs[node['proof']] = node['qed'] if node['qed'] is not None else self.source_offset()


def render(language, text):
    label = '풀이 보충' if language == 'ko' else 'Further explanation'
    parts = [f'<!-- EXAMPLE-DETAIL-{language.upper()} -->',
             '<div class="example-detail">', f'<p><strong>{label}.</strong></p>']
    for part in re.split(r'(\$\$.*?\$\$)', text, flags=re.S):
        if not part.strip():
            continue
        if part.startswith('$$'):
            parts.append(f'<div class="math-display">{html.escape(part, quote=False)}</div>')
        else:
            parts.append(f'<p>{html.escape(part.strip(), quote=False)}</p>')
    parts.extend(['</div>', f'<!-- /EXAMPLE-DETAIL-{language.upper()} -->'])
    return '\n'.join(parts) + '\n'


def build(check=False):
    notes = json.loads((ROOT / 'example-details.json').read_text())
    for key, languages in notes.items():
        assert set(languages) == {'ko', 'en'}, f'Missing language: {key}'
        for lang, text in languages.items():
            assert text.strip(), f'Empty supplement: {key}/{lang}'
            assert '$' not in MATH.sub('', text), f'Unbalanced math: {key}/{lang}'
            assert not any(c in text for c in '\t\r'), f'Escaped control character: {key}/{lang}'
            assert lang != 'en' or not re.search('[가-힣]', text), f'Korean in English: {key}'
    coverage = set()
    changes = []
    pages = 0
    for path in sorted(ROOT.glob('s[0-9]*-*.html')):
        original = path.read_text()
        base = BLOCK.sub('', original)
        parsed = ExampleParser(base)
        if not parsed.examples:
            continue
        pages += 1
        assert not (coverage & parsed.examples), f'Duplicate IDs in {path.name}'
        coverage.update(parsed.examples)
        assert parsed.examples <= notes.keys(), f'Missing details for {parsed.examples - notes.keys()}'
        expected = {(key, lang) for key in parsed.examples for lang in ('ko', 'en')}
        assert set(parsed.proofs) == expected, f'Missing solution panel in {path.name}'
        result = base
        for (key, lang), pos in sorted(parsed.proofs.items(), key=lambda x: x[1], reverse=True):
            result = result[:pos] + render(lang, notes[key][lang]) + result[pos:]
        assert BLOCK.sub('', result) == base, 'Unexpected modification outside supplements'
        if result != original:
            changes.append((path, result))
    assert coverage == notes.keys(), f'Unused details: {notes.keys() - coverage}'
    if check and changes:
        raise SystemExit('Stale example supplements: ' + ', '.join(path.name for path, _ in changes))
    if not check:
        for path, result in changes:
            path.write_text(result)
    print(f'{pages} sections / {len(coverage)} examples / {2 * len(coverage)} language panels: '
          + ('current' if check else f'{len(changes)} pages updated'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    build(parser.parse_args().check)
