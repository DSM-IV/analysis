#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stewart ET 9e  §14.1 Functions of Several Variables
예제 최종답 독립 재계산 (anchor).
각 항목은 signal.alarm(20)으로 타임아웃, print(..., flush=True).
"""
import signal
import sympy as sp

x, y, z, k, L, K, h, m = sp.symbols('x y z k L K h m', real=True)


class TO(Exception):
    pass


def _alarm(sig, frame):
    raise TO()


signal.signal(signal.SIGALRM, _alarm)


def item(label, fn):
    signal.alarm(20)
    try:
        fn()
    except TO:
        print(f"[{label}] TIMEOUT (20s)", flush=True)
    except Exception as e:  # noqa: BLE001
        print(f"[{label}] ERROR: {type(e).__name__}: {e}", flush=True)
    finally:
        signal.alarm(0)
    print("", flush=True)


# ---------------------------------------------------------------- Example 1
def ex1():
    print("Example 1  domain / value", flush=True)
    fa = sp.sqrt(x + y + 1) / (x - 1)
    va = fa.subs({x: 3, y: 2})
    print("  (a) f(3,2) =", sp.simplify(va), " = sqrt(6)/2 ?",
          sp.simplify(va - sp.sqrt(6) / 2) == 0, flush=True)
    # domain (a): x+y+1 >= 0 and x != 1
    print("  (a) domain: {(x,y) | x+y+1 >= 0, x != 1}"
          "  i.e. y >= -x-1 with the line x=1 removed", flush=True)
    fb = x * sp.log(y**2 - x)
    vb = fb.subs({x: 3, y: 2})
    print("  (b) f(3,2) =", sp.simplify(vb), "(= 3*ln(1) = 0)", flush=True)
    print("  (b) domain: {(x,y) | y**2 - x > 0} = {x < y^2}", flush=True)


# ---------------------------------------------------------------- Example 2
def ex2():
    print("Example 2  g = sqrt(9-x^2-y^2): domain & range", flush=True)
    print("  domain: 9-x^2-y^2 >= 0  <=>  x^2+y^2 <= 9  (disk, center O, r=3)",
          flush=True)
    r = sp.Symbol('r', nonnegative=True)
    g = sp.sqrt(9 - r**2)
    print("  range: g(r) for r in [0,3] ->",
          "max =", sp.simplify(g.subs(r, 0)), ", min =", sp.simplify(g.subs(r, 3)),
          "=> [0,3]", flush=True)


# ---------------------------------------------------------------- Example 4
def ex4():
    print("Example 4  Cobb-Douglas P = 1.01 L^0.75 K^0.25", flush=True)
    P = sp.Rational(101, 100) * L**sp.Rational(3, 4) * K**sp.Rational(1, 4)
    p1910 = P.subs({L: 147, K: 208})
    p1920 = P.subs({L: 194, K: 407})
    print("  P(147,208) =", sp.N(p1910, 8), " (textbook ~161.9; actual 159)", flush=True)
    print("  P(194,407) =", sp.N(p1920, 8), " (textbook ~235.8; actual 231)", flush=True)
    print("  domain: {(L,K) | L >= 0, K >= 0}", flush=True)


# ---------------------------------------------------------------- Example 5
def ex5():
    print("Example 5  graph of f = 6-3x-2y (plane 3x+2y+z=6)", flush=True)
    eq = sp.Eq(3 * x + 2 * y + z, 6)
    print("  x-intercept:", sp.solve(eq.subs({y: 0, z: 0}), x), flush=True)
    print("  y-intercept:", sp.solve(eq.subs({x: 0, z: 0}), y), flush=True)
    print("  z-intercept:", sp.solve(eq.subs({x: 0, y: 0}), z), flush=True)


# ---------------------------------------------------------------- Example 6
def ex6():
    print("Example 6  graph of g = sqrt(9-x^2-y^2)", flush=True)
    print("  z^2 = 9-x^2-y^2  =>  x^2+y^2+z^2 = 9 with z >= 0",
          "=> upper hemisphere of the sphere of radius 3", flush=True)


# ---------------------------------------------------------------- Example 8
def ex8():
    print("Example 8  h = 4x^2 + y^2: domain, range, graph", flush=True)
    print("  domain: R^2  (defined for every (x,y))", flush=True)
    print("  range: [0, oo)  since 4x^2 >= 0, y^2 >= 0; h(0,0)=0", flush=True)
    print("  graph z = 4x^2+y^2 : elliptic paraboloid;",
          "trace z=c>0 is the ellipse 4x^2+y^2=c, vertical traces are parabolas",
          flush=True)


# --------------------------------------------------------------- Example 10
def ex10():
    print("Example 10  level curves of f = 6-3x-2y, k = -6,0,6,12", flush=True)
    for kv in (-6, 0, 6, 12):
        eq = sp.Eq(6 - 3 * x - 2 * y, kv)
        lhs = sp.expand(3 * x + 2 * y + (kv - 6))
        sol = sp.solve(eq, y)[0]
        print(f"  k={kv:3d}:  {lhs} = 0   (y = {sp.simplify(sol)}, slope"
              f" {sp.diff(sol, x)})", flush=True)


# --------------------------------------------------------------- Example 11
def ex11():
    print("Example 11  level curves of g = sqrt(9-x^2-y^2), k = 0,1,2,3", flush=True)
    for kv in (0, 1, 2, 3):
        rad = sp.sqrt(9 - kv**2)
        print(f"  k={kv}:  x^2+y^2 = {9 - kv**2}  -> circle radius {sp.simplify(rad)}"
              f" = {sp.N(rad, 6)}", flush=True)


# --------------------------------------------------------------- Example 12
def ex12():
    print("Example 12  level curves of h = 4x^2+y^2+1", flush=True)
    lhs = sp.simplify((4 * x**2 + y**2 + 1 - k) / (k - 1))
    print("  4x^2+y^2+1 = k  =>  x^2/((k-1)/4) + y^2/(k-1) = 1", flush=True)
    chk = sp.simplify(x**2 / ((k - 1) / 4) + y**2 / (k - 1) - 1
                      - (4 * x**2 + y**2 + 1 - k) / (k - 1))
    print("  identity check (should be 0):", chk, flush=True)
    print("  semiaxes: a = sqrt((k-1)/4) = (1/2)sqrt(k-1)  (x-dir),"
          "  b = sqrt(k-1)  (y-dir);  ellipses for k > 1", flush=True)
    print("  (residual expr kept for reference:", lhs, ")", flush=True)


# --------------------------------------------------------------- Example 14
def ex14():
    print("Example 14  domain of f = ln(z-y) + x*y*sin(z)", flush=True)
    print("  need z-y > 0  =>  D = {(x,y,z) in R^3 | z > y}"
          "  (open half-space above the plane z = y)", flush=True)


# --------------------------------------------------------------- Example 15
def ex15():
    print("Example 15  level surfaces of f = x^2+y^2+z^2", flush=True)
    print("  x^2+y^2+z^2 = k, k >= 0 : concentric spheres of radius sqrt(k)"
          "  (k=0 gives the single point O)", flush=True)
    for kv in (1, 2, 3):
        print(f"    k={kv}: radius {sp.sqrt(kv)} = {sp.N(sp.sqrt(kv), 6)}", flush=True)


# --------------------------------------------------------------- Example 16
def ex16():
    print("Example 16  level surfaces of f = x^2 - y - z^2", flush=True)
    sol = sp.solve(sp.Eq(x**2 - y - z**2, k), y)[0]
    print("  x^2 - y - z^2 = k  =>  y =", sp.simplify(sol),
          " : hyperbolic paraboloids (k = 0, +-5 drawn)", flush=True)


if __name__ == '__main__':
    for lab, fn in [
        ("Ex1", ex1), ("Ex2", ex2), ("Ex4", ex4), ("Ex5", ex5), ("Ex6", ex6),
        ("Ex8", ex8), ("Ex10", ex10), ("Ex11", ex11), ("Ex12", ex12),
        ("Ex14", ex14), ("Ex15", ex15), ("Ex16", ex16),
    ]:
        item(lab, fn)
    print("Examples 3, 7, 9, 13 are table / computer-graph / contour-reading items"
          " -- no symbolic recomputation.", flush=True)
