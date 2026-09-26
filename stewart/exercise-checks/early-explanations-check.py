#!/usr/bin/env python3
"""Check the §1.1–14.6 explanation expansion against its committed baseline.

Requires SymPy. No authoring scripts are executed and no site content is written.
"""
import collections
import json
from pathlib import Path
import re
import subprocess
import sympy as s
from sympy.core.function import AppliedUndef

REPO = Path(__file__).resolve().parents[2]
CONTENT = REPO / 'stewart' / 'exercise-content'
BASELINE = '47ff417'
counts = collections.Counter()

def normalized(line, exercise_id):
    # Repair an existing misspelled multiplication command, without changing its value.
    if exercise_id in ('stewart9-exercise-7.7-29','stewart9-exercise-7.7-39'):
        return line.replace('\text', r'\text')
    return line.replace(r'\cdou', r'\cdot') if exercise_id == 'stewart9-exercise-2.7-28' else line

for path in CONTENT.glob('s*.json'):
    doc = json.loads(path.read_text())
    section = tuple(map(int, doc['section'].rstrip('*').split('.')))
    if section > (14, 6):
        continue
    relative = path.relative_to(REPO).as_posix()
    before = json.loads(subprocess.check_output(['git', 'show', f'{BASELINE}:{relative}'], cwd=REPO))
    assert {k:v for k,v in before.items() if k != 'exercises'} == {k:v for k,v in doc.items() if k != 'exercises'}, relative
    assert len(before['exercises']) == len(doc['exercises']), relative
    for old, new in zip(before['exercises'], doc['exercises']):
        eid = new['id']
        assert {k:v for k,v in old.items() if k != 'steps'} == {k:v for k,v in new.items() if k != 'steps'}, eid
        assert len(new['steps']['ko']) == len(new['steps']['en']), eid
        for lang in ('ko', 'en'):
            lines = new['steps'][lang]
            assert len(lines) > len(old['steps'][lang]), (eid, lang)
            iterator = iter(lines)
            for line in old['steps'][lang]:
                assert any(normalized(line,eid) == candidate for candidate in iterator), (eid, lang, line)
            assert not any(ord(c)<32 and c not in '\n\r' for line in lines for c in line), eid
            assert not any(r'\cdou' in line or r'\operatorname{Subs}' in line for line in lines), eid
        counts['exercises'] += 1
    counts['sections'] += 1
assert counts['sections'] == 99 and counts['exercises'] == 6236, counts

LOCALS = {str(q):q for q in s.symbols('x y z t r u v a b c k', real=True)}
LOCALS.update(n=s.Symbol('n', integer=True, positive=True))

def expr(text):
    result = s.sympify(text, locals=LOCALS)
    assert not result.atoms(AppliedUndef), text
    assert not result.has(s.Derivative, s.Subs, s.nan, s.zoo), text
    return result

def equal(left, right):
    residual = s.cancel(left-right)
    if residual != 0:
        residual = s.simplify(s.trigsimp(residual))
    if residual != 0 and not residual.free_symbols and (s.sympify(left).has(s.Float) or s.sympify(right).has(s.Float)):
        assert abs(float(residual)) < 1e-12 * max(1,abs(float(left)),abs(float(right))), (left,right,residual)
        counts['floating_comparisons'] += 1
        return
    assert residual == 0, (left, right, residual)

def matrix(values):
    return s.Matrix([expr(v) for v in values])

rows = json.loads(Path(__file__).with_name('early-explanations-math.json').read_text())
for row in rows:
    kind = row['kind']
    try:
        if kind == 'derivative':
            equal(s.diff(expr(row['function']), expr(row['variable'])), expr(row['derivative']))
        elif kind == 'antiderivative':
            v = expr(row['variable']); primitive = expr(row['primitive'])
            equal(s.diff(primitive, v), expr(row['integrand']))
            if 'value' in row:
                equal(primitive.subs(v, expr(row['upper'])) - primitive.subs(v, expr(row['lower'])), expr(row['value']))
        elif kind == 'limit':
            actual = s.limit(expr(row['function']), expr(row['variable']), expr(row['point']), dir=row['direction'])
            expected = expr(row['value'])
            assert actual == expected or s.simplify(actual-expected) == 0, (actual, expected)
        elif kind == 'partial_derivative':
            f = expr(row['function'])
            for v, derivative in row['derivatives'].items():
                equal(s.diff(f, expr(v)), expr(derivative))
        elif kind == 'implicit_derivative':
            f = expr(row['relation']); x,y = expr('x'),expr('y')
            equal(s.diff(f,x)+s.diff(f,y)*expr(row['derivative']), 0)
        elif kind == 'curve_derivatives':
            curve = matrix(row['curve']); velocity = matrix(row['velocity'])
            for a,b in zip(curve.diff(expr('t')),velocity):equal(a,b)
            equal(velocity.dot(velocity),expr(row['speed_squared']))
        elif kind == 'tangent_plane':
            f = expr(row['function']); plane = expr(row['linearization']); x,y=expr('x'),expr('y')
            point = dict(zip((x,y), map(expr,row['point'])))
            equal(plane.subs(point), f.subs(point))
            for v in (x,y):equal(s.diff(plane,v),s.diff(f,v).subs(point))
        elif kind == 'directional_derivative':
            f=expr(row['function']); point=matrix(row['point']); direction=matrix(row['direction'])
            variables=[expr(v)for v in ('x','y','z')[:len(point)]]
            gradient=matrix([str(s.diff(f,v))for v in variables]).subs(dict(zip(variables,point)))
            unit=direction/s.sqrt(direction.dot(direction))
            equal(unit.dot(unit),1)
            equal(gradient.dot(unit),expr(row['answer']))
        elif kind == 'multivariable_chain':
            f=expr(row['outer']); inner={expr(k):expr(v)for k,v in row['inner'].items()}
            composed=f.subs(inner,simultaneous=True)
            equal(composed,expr(row['substituted']))
            for variable in set().union(*(q.free_symbols for q in inner.values())):
                chain=sum(s.diff(f,v).subs(inner,simultaneous=True)*s.diff(g,variable)for v,g in inner.items())
                equal(chain,s.diff(composed,variable))
        elif kind == 'series_algebra':
            n=expr('n');term=expr(row['term']);ratio=expr(row['successive_ratio'])
            equal(s.combsimp(term.subs(n,n+1)/term),ratio)
        elif kind == 'vector_arithmetic':
            a,b=matrix(row['a']),matrix(row['b'])
            equal((a+b).dot(a+b),a.dot(a)+2*a.dot(b)+b.dot(b))
            if len(a)==3:
                equal(a.cross(b).dot(a),0);equal(a.cross(b).dot(b),0)
        elif kind == 'point_arithmetic':
            points=list(map(matrix,row['points'].values()))
            for a in points:
                for b in points:equal((b-a).dot(b-a),(a-b).dot(a-b))
        else:
            raise AssertionError(kind)
    except Exception as exc:
        raise AssertionError(f"{row['id']} ({kind}): {exc}") from exc
    counts['math_records'] += 1
    counts[kind] += 1

# Specific regressions: products next to parentheses must not become function calls.
lookup={(r['id'],r['kind']):r for r in rows}
t=expr('t')
chain=lookup[('stewart9-exercise-14.5-1','multivariable_chain')]
equal(s.diff(expr(chain['substituted']),t),15*t**4+36*t**3)
equal(expr(lookup[('stewart9-exercise-14.6-4','directional_derivative')]['answer']),3+6*s.sqrt(3))
equal(expr(lookup[('stewart9-exercise-14.6-25','directional_derivative')]['answer']),-s.Rational(18,7))
print('PASS:', json.dumps(dict(counts),ensure_ascii=False,sort_keys=True))
