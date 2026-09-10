#!/usr/bin/env python3
"""Stewart ET 9e  §14.8 Lagrange Multipliers
독립 재계산 (anchor) 스크립트. 각 항목 20초 타임아웃.
실행: python3 anchor-14.8.py
"""
import signal, traceback
import sympy as sp

x, y, z = sp.symbols('x y z', real=True)
lam, mu = sp.symbols('lambda mu', real=True)


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


def lagrange(f, gs, vs, mults):
    """grad f = sum(mult_i grad g_i), plus constraints g_i = 0."""
    eqs = [sp.diff(f, v) - sum(m * sp.diff(g, v) for m, g in zip(mults, gs)) for v in vs]
    eqs += list(gs)
    return sp.solve(eqs, list(vs) + list(mults), dict=True)


# ---------------------------------------------------------------- Example 1
def ex1():
    f = x**2 + 2 * y**2
    g = x**2 + y**2 - 1
    sols = lagrange(f, [g], (x, y), (lam,))
    pts = sorted({(s[x], s[y]) for s in sols if s[x].is_real and s[y].is_real})
    print("[Ex1] candidate points:", pts, "   (textbook: (0,1),(0,-1),(1,0),(-1,0))", flush=True)
    for p in pts:
        print(f"[Ex1]   f{p} = {f.subs({x: p[0], y: p[1]})}", flush=True)
    vals = [f.subs({x: p[0], y: p[1]}) for p in pts]
    print("[Ex1] max =", max(vals), "at (0,+-1)   min =", min(vals), "at (+-1,0)", flush=True)
    print("[Ex1] MATCH:", max(vals) == 2 and min(vals) == 1, "   (textbook: max 2, min 1)", flush=True)


# ---------------------------------------------------------------- Example 2
def ex2():
    V = x * y * z
    g = 2 * x * z + 2 * y * z + x * y - 12
    sols = lagrange(V, [g], (x, y, z), (lam,))
    pos = [(s[x], s[y], s[z]) for s in sols
           if all(s[v].is_real for v in (x, y, z)) and s[x] > 0 and s[y] > 0 and s[z] > 0]
    print("[Ex2] positive critical points:", pos, "   (textbook: (2,2,1))", flush=True)
    for p in pos:
        print("[Ex2]   V =", V.subs({x: p[0], y: p[1], z: p[2]}),
              " constraint =", g.subs({x: p[0], y: p[1], z: p[2]}) + 12, flush=True)
    print("[Ex2] MATCH:", pos == [(2, 2, 1)], "   (textbook: max volume 4 m^3)", flush=True)
    print("[Ex2] = §14.7 Example 6 결과와 동일", flush=True)


# ---------------------------------------------------------------- Example 3
def ex3():
    f = (x - 3)**2 + (y - 1)**2 + (z + 1)**2
    g = x**2 + y**2 + z**2 - 4
    sols = lagrange(f, [g], (x, y, z), (lam,))
    pts = [(sp.simplify(s[x]), sp.simplify(s[y]), sp.simplify(s[z])) for s in sols
           if all(s[v].is_real for v in (x, y, z))]
    r11 = sp.sqrt(11)
    book = [(6 / r11, 2 / r11, -2 / r11), (-6 / r11, -2 / r11, 2 / r11)]
    print("[Ex3] solutions:", [tuple(sp.nsimplify(c) for c in p) for p in pts], flush=True)
    print("[Ex3] textbook: (6/sqrt(11), 2/sqrt(11), -2/sqrt(11)) and its negative", flush=True)
    matched = all(any(all(sp.simplify(a - b) == 0 for a, b in zip(p, q)) for q in pts) for p in book)
    print("[Ex3] MATCH set:", matched, flush=True)
    for p in book:
        d2 = sp.simplify(f.subs({x: p[0], y: p[1], z: p[2]}))
        print("[Ex3]   at", tuple(sp.nsimplify(c) for c in p), ": d^2 =", d2,
              " d =", sp.simplify(sp.sqrt(d2)), "=", sp.N(sp.sqrt(d2), 8), flush=True)
    print("[Ex3] closest  = (6/sqrt11, 2/sqrt11, -2/sqrt11),  d = sqrt(11) - 2 =",
          sp.N(r11 - 2, 8), flush=True)
    print("[Ex3] farthest = (-6/sqrt11, -2/sqrt11, 2/sqrt11), d = sqrt(11) + 2 =",
          sp.N(r11 + 2, 8), flush=True)
    print("[Ex3] geometric check |(3,1,-1)| = sqrt(11) =", sp.N(r11, 8),
          "; radius 2  ->  d_min = sqrt(11)-2, d_max = sqrt(11)+2", flush=True)
    print("[Ex3] lambda from textbook: 1 - lambda = +-sqrt(11)/2, lambda = 1 -+ sqrt(11)/2", flush=True)


# ---------------------------------------------------------------- Example 4
def ex4():
    f = x**2 + 2 * y**2
    interior = sp.solve([sp.diff(f, x), sp.diff(f, y)], [x, y], dict=True)
    print("[Ex4] interior critical point:", interior, " f =", f.subs(interior[0]),
          "   (textbook: (0,0), f = 0)", flush=True)
    bvals = {(0, 1): f.subs({x: 0, y: 1}), (0, -1): f.subs({x: 0, y: -1}),
             (1, 0): f.subs({x: 1, y: 0}), (-1, 0): f.subs({x: -1, y: 0})}
    print("[Ex4] boundary values (from Example 1):", bvals, flush=True)
    allv = [f.subs(interior[0])] + list(bvals.values())
    print("[Ex4] absolute max =", max(allv), "at (0,+-1);  absolute min =", min(allv), "at (0,0)", flush=True)
    print("[Ex4] MATCH:", max(allv) == 2 and min(allv) == 0, "   (textbook: max 2, min 0)", flush=True)


# ---------------------------------------------------------------- Example 5
def ex5():
    f = x + 2 * y + 3 * z
    g = x - y + z - 1
    hh = x**2 + y**2 - 1
    sols = lagrange(f, [g, hh], (x, y, z), (lam, mu))
    out = []
    for s in sols:
        if all(s[v].is_real for v in (x, y, z)):
            p = (sp.simplify(s[x]), sp.simplify(s[y]), sp.simplify(s[z]))
            out.append((p, sp.simplify(f.subs({x: p[0], y: p[1], z: p[2]})),
                        sp.simplify(s[lam]), sp.simplify(s[mu])))
    for p, v, l, m in out:
        print("[Ex5] point", p, " f =", v, "=", sp.N(v, 8), "  lambda =", l, " mu =", m, flush=True)
    vals = [v for _, v, _, _ in out]
    mx = max(vals, key=lambda t: sp.N(t))
    print("[Ex5] maximum value =", sp.simplify(mx), "=", sp.N(mx, 8),
          "   (textbook: 3 + sqrt(29))", flush=True)
    print("[Ex5] MATCH:", sp.simplify(mx - (3 + sp.sqrt(29))) == 0, flush=True)
    print("[Ex5] textbook intermediate: lambda = 3, x = -1/mu, y = 5/(2mu), mu^2 = 29/4,"
          " mu = +-sqrt(29)/2, x = -+2/sqrt29, y = +-5/sqrt29, z = 1 +- 7/sqrt29", flush=True)
    r29 = sp.sqrt(29)
    for sgn in (1, -1):
        px, py = -sgn * 2 / r29, sgn * 5 / r29
        pz = 1 + sgn * 7 / r29
        print("[Ex5]   textbook point:", (sp.nsimplify(px), sp.nsimplify(py), sp.nsimplify(pz)),
              " constraints:", sp.simplify(px - py + pz), "(=1?)", sp.simplify(px**2 + py**2), "(=1?)",
              " f =", sp.simplify(px + 2 * py + 3 * pz), flush=True)


if __name__ == '__main__':
    for nm, fn in [('Ex1', ex1), ('Ex2', ex2), ('Ex3', ex3), ('Ex4', ex4), ('Ex5', ex5)]:
        run(nm, fn)
