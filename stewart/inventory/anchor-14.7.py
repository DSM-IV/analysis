#!/usr/bin/env python3
"""Stewart ET 9e  §14.7 Maximum and Minimum Values
독립 재계산 (anchor) 스크립트. 각 항목 20초 타임아웃.
실행: python3 anchor-14.7.py
"""
import signal, traceback
import sympy as sp

x, y, z = sp.symbols('x y z', real=True)


class TO(Exception):
    pass


def _hnd(a, b):
    raise TO()


def run(name, fn):
    signal.signal(signal.SIGALRM, _hnd)
    signal.alarm(20)
    try:
        fn()
    except TO:
        print(f"[{name}] TIMEOUT", flush=True)
    except Exception:
        print(f"[{name}] ERROR", flush=True)
        traceback.print_exc()
    finally:
        signal.alarm(0)
    print(flush=True)


def classify(f, pt):
    """Second Derivatives Test at pt = (a, b)."""
    fxx = sp.diff(f, x, 2).subs({x: pt[0], y: pt[1]})
    fyy = sp.diff(f, y, 2).subs({x: pt[0], y: pt[1]})
    fxy = sp.diff(f, x, y).subs({x: pt[0], y: pt[1]})
    D = sp.simplify(fxx * fyy - fxy**2)
    if D > 0 and fxx > 0:
        kind = 'local minimum'
    elif D > 0 and fxx < 0:
        kind = 'local maximum'
    elif D < 0:
        kind = 'saddle point'
    else:
        kind = 'inconclusive (D = 0)'
    return fxx, fyy, fxy, D, kind


# ---------------------------------------------------------------- Example 1
def ex1():
    f = x**2 + y**2 - 2 * x - 6 * y + 14
    crit = sp.solve([sp.diff(f, x), sp.diff(f, y)], [x, y], dict=True)
    print("[Ex1] fx, fy =", sp.diff(f, x), ",", sp.diff(f, y), flush=True)
    print("[Ex1] critical points:", crit, "   (textbook: (1,3))", flush=True)
    print("[Ex1] completed square:", sp.simplify(f - (4 + (x - 1)**2 + (y - 3)**2)) == 0,
          "  -> f = 4 + (x-1)^2 + (y-3)^2", flush=True)
    print("[Ex1] f(1,3) =", f.subs({x: 1, y: 3}),
          "   (textbook: absolute minimum 4)", flush=True)


# ---------------------------------------------------------------- Example 2
def ex2():
    f = y**2 - x**2
    crit = sp.solve([sp.diff(f, x), sp.diff(f, y)], [x, y], dict=True)
    print("[Ex2] critical points:", crit, "   (textbook: (0,0) only)", flush=True)
    print("[Ex2] on x-axis (y=0): f =", f.subs(y, 0), "< 0 for x != 0", flush=True)
    print("[Ex2] on y-axis (x=0): f =", f.subs(x, 0), "> 0 for y != 0", flush=True)
    print("[Ex2] -> f(0,0)=0 is neither max nor min; no extreme value (saddle)", flush=True)
    print("[Ex2] Second Derivatives Test:", classify(f, (0, 0)), flush=True)


# ---------------------------------------------------------------- Example 3
def ex3():
    f = x**4 + y**4 - 4 * x * y + 1
    crit = sp.solve([sp.diff(f, x), sp.diff(f, y)], [x, y], dict=True)
    real = [(c[x], c[y]) for c in crit if c[x].is_real and c[y].is_real]
    print("[Ex3] real critical points:", real, "   (textbook: (0,0), (1,1), (-1,-1))", flush=True)
    print("[Ex3] D(x,y) =", sp.expand(sp.diff(f, x, 2) * sp.diff(f, y, 2) - sp.diff(f, x, y)**2),
          "   (textbook: 144 x^2 y^2 - 16)", flush=True)
    for p in sorted(real, key=lambda t: (t[0], t[1])):
        fxx, fyy, fxy, D, kind = classify(f, p)
        print(f"[Ex3] {p}: f = {f.subs({x: p[0], y: p[1]})}, fxx = {fxx}, D = {D} -> {kind}", flush=True)
    print("[Ex3] textbook: (0,0) saddle (D=-16); (1,1) and (-1,-1) local minima with f = -1 (D=128)", flush=True)


# ---------------------------------------------------------------- Example 4
def ex4():
    f = 10 * x**2 * y - 5 * x**2 - 4 * y**2 - x**4 - 2 * y**4
    fx, fy = sp.diff(f, x), sp.diff(f, y)
    print("[Ex4] fx =", sp.expand(fx), "   (textbook: 20xy - 10x - 4x^3)", flush=True)
    print("[Ex4] fy =", sp.expand(fy), "   (textbook: 10x^2 - 8y - 8y^3)", flush=True)
    # branch x = 0
    print("[Ex4] x=0 branch: fy becomes", sp.factor(fy.subs(x, 0)), "-> y = 0, critical point (0,0)", flush=True)
    # branch 10y - 5 - 2x^2 = 0  => x^2 = 5y - 2.5
    cubic = sp.expand(sp.Rational(5, 1) * (5 * y - sp.Rational(5, 2)) - 4 * y - 4 * y**3)
    print("[Ex4] other branch cubic (from 5x^2 - 4y - 4y^3 = 0 with x^2 = 5y-2.5):",
          sp.expand(-cubic), "= 0   (textbook: 4y^3 - 21y + 12.5 = 0)", flush=True)
    roots = sp.nroots(sp.Poly(4 * y**3 - 21 * y + sp.Rational(25, 2), y))
    print("[Ex4] roots y =", [sp.N(r, 6) for r in roots],
          "   (textbook: -2.5452, 0.6468, 1.8984)", flush=True)
    pts = [(sp.Integer(0), sp.Integer(0))]
    for r in roots:
        val = 5 * r - sp.Rational(5, 2)
        if val > 0:
            xs = sp.sqrt(val)
            pts.append((xs, r))
            pts.append((-xs, r))
        else:
            print(f"[Ex4] y = {sp.N(r,6)}: x^2 = {sp.N(val,6)} < 0 -> no real x", flush=True)
    for p in pts:
        fxx, fyy, fxy, D, kind = classify(f, p)
        print(f"[Ex4] ({sp.N(p[0],4)}, {sp.N(p[1],4)}): f = {sp.N(f.subs({x: p[0], y: p[1]}),4)}, "
              f"fxx = {sp.N(fxx,4)}, D = {sp.N(D,6)} -> {kind}", flush=True)
    print("[Ex4] textbook chart: (0,0) f=0.00 fxx=-10.00 D=80.00 local max; "
          "(+-2.64,1.90) f=8.50 fxx=-55.93 D=2488.72 local max; "
          "(+-0.86,0.65) f=-1.48 fxx=-5.87 D=-187.64 saddle", flush=True)
    print("[Ex4] absolute maximum: f(+-2.64, 1.90) ~ 8.50; highest points (+-2.64, 1.90, 8.50)", flush=True)


# ---------------------------------------------------------------- Example 5
def ex5():
    f = (x - 1)**2 + y**2 + (6 - x - 2 * y)**2      # d^2 with z = 4 - x - 2y
    fx, fy = sp.expand(sp.diff(f, x)), sp.expand(sp.diff(f, y))
    print("[Ex5] fx =", fx, "   (textbook: 4x + 4y - 14)", flush=True)
    print("[Ex5] fy =", fy, "   (textbook: 4x + 10y - 24)", flush=True)
    sol = sp.solve([fx, fy], [x, y], dict=True)[0]
    print("[Ex5] critical point:", (sol[x], sol[y]), "   (textbook: (11/6, 5/3))", flush=True)
    fxx, fyy, fxy, D, kind = classify(f, (sol[x], sol[y]))
    print(f"[Ex5] fxx={fxx}, fxy={fxy}, fyy={fyy}, D={D} -> {kind}   (textbook: D=24>0, fxx=4>0)", flush=True)
    d = sp.sqrt(f.subs(sol))
    print("[Ex5] minimum distance =", sp.simplify(d), "=", sp.N(d, 8),
          "   (textbook: (5/6)sqrt(6))", flush=True)
    print("[Ex5] MATCH:", sp.simplify(d - sp.Rational(5, 6) * sp.sqrt(6)) == 0, flush=True)
    # 벡터(점-평면 거리 공식)로 교차검증
    d2 = sp.Abs(1 + 2 * 0 + (-2) - 4) / sp.sqrt(1**2 + 2**2 + 1**2)
    print("[Ex5] point-plane distance formula |1+0-2-4|/sqrt(6) =", sp.simplify(d2), "=", sp.N(d2, 8),
          " MATCH:", sp.simplify(d - d2) == 0, flush=True)


# ---------------------------------------------------------------- Example 6
def ex6():
    V = x * y * (12 - x * y) / (2 * (x + y))
    Vx, Vy = sp.simplify(sp.diff(V, x)), sp.simplify(sp.diff(V, y))
    print("[Ex6] V(x,y) = (12xy - x^2y^2)/(2(x+y))", flush=True)
    print("[Ex6] Vx =", sp.factor(sp.simplify(Vx)), flush=True)
    print("[Ex6]      textbook: y^2(12 - 2xy - x^2) / (2(x+y)^2)", flush=True)
    bx = y**2 * (12 - 2 * x * y - x**2) / (2 * (x + y)**2)
    by = x**2 * (12 - 2 * x * y - y**2) / (2 * (x + y)**2)
    print("[Ex6] MATCH Vx:", sp.simplify(Vx - bx) == 0, " MATCH Vy:", sp.simplify(Vy - by) == 0, flush=True)
    sol = sp.solve([12 - 2 * x * y - x**2, 12 - 2 * x * y - y**2], [x, y], dict=True)
    pos = [(s[x], s[y]) for s in sol if s[x].is_real and s[y].is_real and s[x] > 0 and s[y] > 0]
    print("[Ex6] positive solutions:", pos, "   (textbook: x = y = 2)", flush=True)
    a, b = pos[0]
    c = (12 - a * b) / (2 * (a + b))
    print("[Ex6] z =", c, "   (textbook: 1);  V = xyz =", a * b * c, "   (textbook: 4 m^3)", flush=True)
    print("[Ex6] surface-area check 2xz+2yz+xy =", sp.simplify(2 * a * c + 2 * b * c + a * b),
          "   (must be 12)", flush=True)
    fxx, fyy, fxy, D, kind = classify(V, (a, b))
    print(f"[Ex6] Second Derivatives Test at (2,2): fxx={fxx}, D={D} -> {kind}", flush=True)


# ---------------------------------------------------------------- Example 7
def ex7():
    f = x**2 - 2 * x * y + 2 * y
    sol = sp.solve([sp.diff(f, x), sp.diff(f, y)], [x, y], dict=True)[0]
    print("[Ex7] critical point:", (sol[x], sol[y]), " f =", f.subs(sol),
          "   (textbook: (1,1), f = 1)", flush=True)
    print("[Ex7] boundary of D = [0,3] x [0,2]:", flush=True)
    edges = {
        'L1 (y=0, 0<=x<=3)': (f.subs(y, 0), x, 0, 3),
        'L2 (x=3, 0<=y<=2)': (f.subs(x, 3), y, 0, 2),
        'L3 (y=2, 0<=x<=3)': (f.subs(y, 2), x, 0, 3),
        'L4 (x=0, 0<=y<=2)': (f.subs(x, 0), y, 0, 2),
    }
    allvals = [(f.subs(sol), '(1,1) critical')]
    for lbl, (g, var, lo, hi) in edges.items():
        cands = [lo, hi] + [c for c in sp.solve(sp.diff(g, var), var) if c.is_real and lo <= c <= hi]
        vals = [(sp.simplify(g.subs(var, c)), c) for c in cands]
        print(f"[Ex7]   {lbl}: g = {sp.expand(g)}, min = {min(vals)[0]} at {var}={min(vals)[1]}, "
              f"max = {max(vals)[0]} at {var}={max(vals)[1]}", flush=True)
        allvals += [(v, f"{lbl} {var}={c}") for v, c in vals]
    lo = min(allvals, key=lambda t: t[0])
    hi = max(allvals, key=lambda t: t[0])
    print("[Ex7] absolute minimum =", lo, "   (textbook: 0, at (0,0) and (2,2))", flush=True)
    print("[Ex7] absolute maximum =", hi, "   (textbook: 9, at (3,0))", flush=True)
    print("[Ex7] check f(0,0) =", f.subs({x: 0, y: 0}), " f(2,2) =", f.subs({x: 2, y: 2}),
          " f(3,0) =", f.subs({x: 3, y: 0}), flush=True)


if __name__ == '__main__':
    for nm, fn in [('Ex1', ex1), ('Ex2', ex2), ('Ex3', ex3), ('Ex4', ex4),
                   ('Ex5', ex5), ('Ex6', ex6), ('Ex7', ex7)]:
        run(nm, fn)
