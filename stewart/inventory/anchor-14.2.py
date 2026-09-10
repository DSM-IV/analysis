#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stewart ET 9e  §14.2 Limits and Continuity
예제 최종답 독립 재계산 (anchor).
각 항목은 signal.alarm(20)으로 타임아웃, print(..., flush=True).
"""
import signal
import sympy as sp

x, y, z, t, m, r = sp.symbols('x y z t m r', real=True)
th = sp.Symbol('theta', real=True)
eps = sp.Symbol('varepsilon', positive=True)


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


def path_limit(expr, sub, var, point=0):
    """expr를 경로 sub(치환 dict)로 제한한 뒤 var -> point 극한."""
    return sp.limit(sp.simplify(expr.subs(sub)), var, point)


# ------------------------------------------------------------------- 절 도입
def intro():
    print("Intro  comparison of two functions at (0,0)", flush=True)
    f = sp.sin(x**2 + y**2) / (x**2 + y**2)
    fp = f.subs({x: r * sp.cos(th), y: r * sp.sin(th)})
    print("  sin(x^2+y^2)/(x^2+y^2): polar form ->", sp.simplify(fp),
          " limit r->0+ =", sp.limit(sp.simplify(fp), r, 0, '+'), "(= 1)", flush=True)
    g = (x**2 - y**2) / (x**2 + y**2)
    gp = sp.simplify(g.subs({x: r * sp.cos(th), y: r * sp.sin(th)}))
    print("  (x^2-y^2)/(x^2+y^2): polar form ->", gp,
          " depends on theta only => limit DNE", flush=True)


# ---------------------------------------------------------------- Example 1
def ex1():
    print("Example 1  lim (x^2-y^2)/(x^2+y^2) at (0,0)", flush=True)
    f = (x**2 - y**2) / (x**2 + y**2)
    Lx = path_limit(f, {y: 0}, x)
    Ly = path_limit(f, {x: 0}, y)
    print("  along x-axis (y=0):", Lx, flush=True)
    print("  along y-axis (x=0):", Ly, flush=True)
    print("  1 != -1  =>  limit DOES NOT EXIST :", Lx != Ly, flush=True)


# ---------------------------------------------------------------- Example 2
def ex2():
    print("Example 2  lim xy/(x^2+y^2) at (0,0)", flush=True)
    f = x * y / (x**2 + y**2)
    print("  along x-axis:", path_limit(f, {y: 0}, x), flush=True)
    print("  along y-axis:", path_limit(f, {x: 0}, y), flush=True)
    Ld = path_limit(f, {y: x}, x)
    print("  along y = x :", Ld, "(= 1/2)", flush=True)
    print("  0 != 1/2  =>  limit DOES NOT EXIST :", Ld != 0, flush=True)
    print("  (general line y = m x:", sp.simplify(f.subs(y, m * x)), ")", flush=True)


# ---------------------------------------------------------------- Example 3
def ex3():
    print("Example 3  lim x*y^2/(x^2+y^4) at (0,0)", flush=True)
    f = x * y**2 / (x**2 + y**4)
    fl = sp.simplify(f.subs(y, m * x))
    print("  restricted to y = m x:", fl,
          " -> limit x->0 :", sp.limit(fl, x, 0), flush=True)
    print("  along x = 0 (y-axis):", path_limit(f, {x: 0}, y), flush=True)
    fp = sp.simplify(f.subs(x, y**2))
    print("  along the parabola x = y^2:", fp,
          " -> limit y->0 :", sp.limit(fp, y, 0), "(= 1/2)", flush=True)
    print("  every line gives 0 but the parabola gives 1/2  =>  limit DOES NOT EXIST",
          flush=True)


# ---------------------------------------------------------------- Example 4
def ex4():
    print("Example 4  lim (x^2 y^3 - x^3 y^2 + 3x + 2y) at (1,2)", flush=True)
    p = x**2 * y**3 - x**3 * y**2 + 3 * x + 2 * y
    v = p.subs({x: 1, y: 2})
    print("  polynomial => direct substitution:", sp.simplify(v), "(textbook 11)",
          flush=True)
    print("  iterated check:", sp.limit(sp.limit(p, x, 1), y, 2), flush=True)


# ---------------------------------------------------------------- Example 5
def ex5():
    print("Example 5  lim (x^2 y + 1)/(x^3 y^2 - 2x) at (-2,3)", flush=True)
    q = (x**2 * y + 1) / (x**3 * y**2 - 2 * x)
    num = (x**2 * y + 1).subs({x: -2, y: 3})
    den = (x**3 * y**2 - 2 * x).subs({x: -2, y: 3})
    v = sp.nsimplify(sp.simplify(q.subs({x: -2, y: 3})))
    print("  numerator at (-2,3):", num, "; denominator:", den, flush=True)
    print("  value =", v, "=", sp.N(v, 8), " (textbook -13/68)", flush=True)
    print("  matches -13/68 :", sp.simplify(v + sp.Rational(13, 68)) == 0, flush=True)


# ---------------------------------------------------------------- Example 6
def ex6():
    print("Example 6  lim 3x^2 y/(x^2+y^2) at (0,0)", flush=True)
    f = 3 * x**2 * y / (x**2 + y**2)
    fp = sp.simplify(f.subs({x: r * sp.cos(th), y: r * sp.sin(th)}))
    print("  polar form:", fp, " (|.| <= 3r -> 0)", flush=True)
    print("  limit r->0+ (any theta):", sp.limit(fp, r, 0, '+'), flush=True)
    # bound (5): |3x^2 y|/(x^2+y^2) <= 3|y| <= 3 sqrt(x^2+y^2)
    a, b = sp.symbols('a b', positive=True)
    bnd = sp.simplify(3 * b - 3 * a**2 * b / (a**2 + b**2))
    print("  bound check  3|y| - 3x^2|y|/(x^2+y^2) =", sp.factor(bnd),
          " >= 0 :", sp.simplify(sp.factor(bnd)).could_extract_minus_sign() is False,
          flush=True)
    print("  delta = eps/3  =>  3*sqrt(x^2+y^2) < 3*delta =",
          sp.simplify(3 * (eps / 3)), "= eps  OK", flush=True)
    # numeric sanity on a shrinking circle
    worst = max(abs(float(f.subs({x: 1e-6 * sp.cos(sp.Rational(j, 20) * sp.pi),
                                  y: 1e-6 * sp.sin(sp.Rational(j, 20) * sp.pi)})))
                for j in range(1, 40))
    print(f"  numeric: max |f| on circle r=1e-6 is {worst:.3e} (<= 3r = 3e-6)",
          flush=True)


# ---------------------------------------------------------------- Example 7
def ex7():
    print("Example 7  continuity of f = (x^2-y^2)/(x^2+y^2)", flush=True)
    print("  rational function, denominator 0 only at (0,0)", flush=True)
    print("  => continuous on D = {(x,y) | (x,y) != (0,0)}; not defined (hence"
          " discontinuous) at the origin", flush=True)


# ---------------------------------------------------------------- Example 8
def ex8():
    print("Example 8  g = (x^2-y^2)/(x^2+y^2) for (x,y)!=(0,0), g(0,0)=0", flush=True)
    f = (x**2 - y**2) / (x**2 + y**2)
    print("  path limits:", path_limit(f, {y: 0}, x), "and", path_limit(f, {x: 0}, y),
          "=> lim at (0,0) DNE (Example 1)", flush=True)
    print("  => g is DISCONTINUOUS at (0,0) even though g(0,0) is defined", flush=True)


# ---------------------------------------------------------------- Example 9
def ex9():
    print("Example 9  f = 3x^2 y/(x^2+y^2) for (x,y)!=(0,0), f(0,0)=0", flush=True)
    f = 3 * x**2 * y / (x**2 + y**2)
    fp = sp.simplify(f.subs({x: r * sp.cos(th), y: r * sp.sin(th)}))
    print("  lim at (0,0) =", sp.limit(fp, r, 0, '+'), "= f(0,0) = 0 (Example 6)",
          flush=True)
    print("  => f is CONTINUOUS at (0,0), hence continuous on all of R^2", flush=True)


# --------------------------------------------------------------- Example 10
def ex10():
    print("Example 10  h = exp(-(x^2+y^2))", flush=True)
    print("  h = g o f with f = x^2+y^2 (polynomial, continuous on R^2)"
          " and g(t) = e^{-t} (continuous on R)", flush=True)
    print("  => continuous on R^2 (everywhere)", flush=True)


# --------------------------------------------------------------- Example 11
def ex11():
    print("Example 11  h = arctan(y/x)", flush=True)
    print("  f = y/x is rational, continuous except on the line x = 0;"
          " g(t) = arctan t is continuous on R", flush=True)
    print("  => h continuous on {(x,y) | x != 0}; discontinuous where x = 0"
          " (a break above the y-axis)", flush=True)
    # sanity: the two one-sided limits across x=0 at (0,1) disagree
    print("  check at (0,1): x->0^+ gives",
          sp.limit(sp.atan(1 / x), x, 0, '+'), "; x->0^- gives",
          sp.limit(sp.atan(1 / x), x, 0, '-'), flush=True)


if __name__ == '__main__':
    for lab, fn in [
        ("Intro", intro), ("Ex1", ex1), ("Ex2", ex2), ("Ex3", ex3), ("Ex4", ex4),
        ("Ex5", ex5), ("Ex6", ex6), ("Ex7", ex7), ("Ex8", ex8), ("Ex9", ex9),
        ("Ex10", ex10), ("Ex11", ex11),
    ]:
        item(lab, fn)
