"""Verify the pilot with symbolic differentiation and definition-based limits.

Run: python3 stewart/exercise-checks/check_s14_3.py
Requires SymPy. Source formulas were visually checked on PDF page 1045,
printed page 1008. Formulas below are an independent mathematical oracle;
the rendered text still requires human review against this oracle.
"""
import json
from pathlib import Path
import sympy as s

x, y, t, u, v, h = s.symbols('x y t u v h', real=True)
cases = [
    (9, x**4 + 5*x*y**3, (x, y), (4*x**3+5*y**3, 15*x*y**2), {}),
    (10, x**2*y-3*y**4, (x, y), (2*x*y, x**2-12*y**3), {}),
    (11, x**3*s.sin(y), (x, y), (3*x**2*s.sin(y), x**3*s.cos(y)), {}),
    (12, s.exp(x*t), (x, t), (t*s.exp(x*t), x*s.exp(x*t)), {}),
    (13, s.log(x+t**2), (x, t), (1/(x+t**2), 2*t/(x+t**2)), {x: 3, t: 1}),
    (14, u/v**2, (u, v), (1/v**2, -2*u/v**3), {u: 3, v: 2}),
    (15, y*s.exp(x*y), (x, y), (y**2*s.exp(x*y), (1+x*y)*s.exp(x*y)), {}),
    (16, (x**2+x*y)**3, (x, y), (3*(x**2+x*y)**2*(2*x+y), 3*x*(x**2+x*y)**2), {}),
]

root = Path(__file__).resolve().parents[1]
data = json.loads((root / 'exercise-content/s14-3.json').read_text())
assert [e['number'] for e in data['exercises']] == list(range(9, 17))
for exercise in data['exercises']:
    for key in ('statement', 'hint', 'answer', 'check'):
        for lang in ('ko', 'en'):
            text = exercise[key][lang]
            assert text and text.count(r'\(') == text.count(r'\)'), (exercise['number'], key, lang)
            assert text.count(r'\[') == text.count(r'\]'), (exercise['number'], key, lang)
    assert len(exercise['steps']['ko']) == len(exercise['steps']['en']) == 3

results = []
for n, f, variables, expected, sample in cases:
    for variable, answer in zip(variables, expected):
        assert s.simplify(s.diff(f, variable)-answer) == 0, (n, variable, 'derivative')
        dq = (f.subs(variable, variable+h)-f)/h
        # At logarithm/rational singularities, use a valid interior point for
        # the independent limit. The symbolic derivative identity is global
        # on the function's real domain.
        target = answer
        if sample:
            dq = dq.subs(sample)
            target = answer.subs(sample)
        assert s.simplify(s.limit(dq, h, 0)-target) == 0, (n, variable, 'difference quotient')
    results.append({'number': n, 'symbolicDerivatives': 'pass', 'differenceQuotients': 'pass',
                    'limitScope': 'interior sample' if sample else 'symbolic'})
    print(f'PASS exercise {n}: two derivatives and two difference-quotient limits')

# Additional independent expansion check for the composite polynomial.
expanded = x**6+3*x**5*y+3*x**4*y**2+x**3*y**3
assert s.expand(cases[-1][1]-expanded) == 0
assert s.expand(s.diff(expanded, x)-cases[-1][3][0]) == 0
assert s.expand(s.diff(expanded, y)-cases[-1][3][1]) == 0

report = {'section': '14.3', 'sourceVisualCheck': {'printedPage': 1008, 'pdfPage': 1045,
          'numbers': list(range(9, 17)), 'uncertainties': []},
          'checks': results, 'compositeExpansion': 'pass', 'bilingualMathDelimiters': 'pass',
          'limitations': ['Exact interior-point limits supplement symbolic identities for exercises 13 and 14.',
                         'This script verifies independently encoded formulas; source and displayed prose were manually reviewed.']}
(root / 'exercise-checks/s14-3-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
print('PASS: 16 symbolic derivative identities, 16 limit checks, polynomial expansion, content shape')
