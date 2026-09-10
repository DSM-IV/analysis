#!/usr/bin/env python3
"""Stewart ET 9e  §14.6 Directional Derivatives and the Gradient Vector
독립 재계산 (anchor) 스크립트. 각 항목 20초 타임아웃.
실행: python3 anchor-14.6.py
"""
import signal, traceback
import sympy as sp

x, y, z = sp.symbols('x y z', real=True)
h = sp.Symbol('h', positive=True)


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


def grad(f, vs):
    return sp.Matrix([sp.diff(f, v) for v in vs])


def unit(v):
    v = sp.Matrix(v)
    return v / sp.sqrt(sum(c**2 for c in v))


# ---------------------------------------------------------------- Example 1
def ex1():
    val = sp.Rational(60 - 50, 75)
    print("[Ex1] Du T ~ (60-50)/75 =", val, "=", sp.N(val, 4),
          "  (textbook: ~0.13 F/mi)", flush=True)


# ---------------------------------------------------------------- Example 2
def ex2():
    f = x**3 - 3 * x * y + 4 * y**2
    th = sp.pi / 6
    u = sp.Matrix([sp.cos(th), sp.sin(th)])
    Du = sp.simplify(grad(f, (x, y)).dot(u))
    book = sp.Rational(1, 2) * (3 * sp.sqrt(3) * x**2 - 3 * x + (8 - 3 * sp.sqrt(3)) * y)
    print("[Ex2] Du f(x,y) =", sp.expand(Du), flush=True)
    print("[Ex2] textbook  = (1/2)[3*sqrt(3)x^2 - 3x + (8-3*sqrt(3))y]", flush=True)
    print("[Ex2] MATCH form:", sp.simplify(Du - book) == 0, flush=True)
    val = sp.simplify(Du.subs({x: 1, y: 2}))
    print("[Ex2] Du f(1,2) =", val, "=", sp.N(val, 8),
          "   (textbook: (13 - 3*sqrt(3))/2)", flush=True)
    print("[Ex2] MATCH value:", sp.simplify(val - (13 - 3 * sp.sqrt(3)) / 2) == 0, flush=True)
    # 정의(극한)로 교차검증
    a, b = u[0], u[1]
    lim = sp.limit((f.subs({x: 1 + h * a, y: 2 + h * b}) - f.subs({x: 1, y: 2})) / h, h, 0)
    print("[Ex2] limit-definition cross-check:", sp.simplify(lim - val) == 0, flush=True)


# ---------------------------------------------------------------- Example 3
def ex3():
    f = sp.sin(x) + sp.exp(x * y)
    g = grad(f, (x, y))
    print("[Ex3] grad f =", g.T, "   (textbook: <cos x + y e^{xy}, x e^{xy}>)", flush=True)
    v = g.subs({x: 0, y: 1})
    print("[Ex3] grad f(0,1) =", v.T, "   (textbook: <2, 0>)", flush=True)
    print("[Ex3] MATCH:", v == sp.Matrix([2, 0]), flush=True)


# ---------------------------------------------------------------- Example 4
def ex4():
    f = x**2 * y**3 - 4 * y
    g = grad(f, (x, y))
    gp = g.subs({x: 2, y: -1})
    u = unit([2, 5])
    Du = sp.simplify(gp.dot(u))
    print("[Ex4] grad f =", g.T, "   (textbook: 2xy^3 i + (3x^2y^2 - 4) j)", flush=True)
    print("[Ex4] grad f(2,-1) =", gp.T, "   (textbook: -4 i + 8 j)", flush=True)
    print("[Ex4] u =", u.T, "  |v| = sqrt(29)", flush=True)
    print("[Ex4] Du f(2,-1) =", Du, "=", sp.N(Du, 8), "   (textbook: 32/sqrt(29))", flush=True)
    print("[Ex4] MATCH:", sp.simplify(Du - 32 / sp.sqrt(29)) == 0, flush=True)


# ---------------------------------------------------------------- Example 5
def ex5():
    f = x * sp.sin(y * z)
    g = grad(f, (x, y, z))
    print("[Ex5a] grad f =", g.T, "   (textbook: <sin yz, xz cos yz, xy cos yz>)", flush=True)
    gp = g.subs({x: 1, y: 3, z: 0})
    print("[Ex5b] grad f(1,3,0) =", gp.T, "   (textbook: <0,0,3>)", flush=True)
    u = unit([1, 2, -1])
    Du = sp.simplify(gp.dot(u))
    print("[Ex5b] Du f(1,3,0) =", Du, "=", sp.N(Du, 8),
          "   (textbook: -3/sqrt(6) = -sqrt(3/2))", flush=True)
    print("[Ex5b] MATCH:", sp.simplify(Du + sp.sqrt(sp.Rational(3, 2))) == 0, flush=True)


# ---------------------------------------------------------------- Example 6
def ex6():
    f = x * sp.exp(y)
    g = grad(f, (x, y))
    gp = g.subs({x: 2, y: 0})
    print("[Ex6a] grad f =", g.T, "  grad f(2,0) =", gp.T, "   (textbook: <1,2>)", flush=True)
    PQ = sp.Matrix([sp.Rational(1, 2) - 2, 2 - 0])   # P(2,0) -> Q(1/2, 2)
    u = unit(PQ)
    print("[Ex6a] PQ =", PQ.T, " |PQ| =", sp.sqrt(sum(c**2 for c in PQ)),
          " u =", u.T, "   (textbook: <-3/5, 4/5>)", flush=True)
    Du = sp.simplify(gp.dot(u))
    print("[Ex6a] Du f(2,0) =", Du, "   (textbook: 1)", flush=True)
    mag = sp.sqrt(sum(c**2 for c in gp))
    print("[Ex6b] max direction = grad f(2,0) = <1,2>;  max rate = |grad f| =",
          mag, "=", sp.N(mag, 8), "   (textbook: sqrt(5))", flush=True)
    print("[Ex6] MATCH:", Du == 1 and sp.simplify(mag - sp.sqrt(5)) == 0, flush=True)


# ---------------------------------------------------------------- Example 7
def ex7():
    T = 80 / (1 + x**2 + 2 * y**2 + 3 * z**2)
    g = sp.simplify(grad(T, (x, y, z)))
    print("[Ex7] grad T =", g.T, flush=True)
    print("[Ex7] textbook: 160/(1+x^2+2y^2+3z^2)^2 * (-x i - 2y j - 3z k)", flush=True)
    book = 160 / (1 + x**2 + 2 * y**2 + 3 * z**2)**2 * sp.Matrix([-x, -2 * y, -3 * z])
    print("[Ex7] MATCH form:", sp.simplify(g - book) == sp.zeros(3, 1), flush=True)
    gp = sp.simplify(g.subs({x: 1, y: 1, z: -2}))
    print("[Ex7] grad T(1,1,-2) =", gp.T, "   (textbook: (5/8)(-i - 2j + 6k))", flush=True)
    print("[Ex7] MATCH point:", gp == sp.Rational(5, 8) * sp.Matrix([-1, -2, 6]), flush=True)
    mag = sp.simplify(sp.sqrt(sum(c**2 for c in gp)))
    print("[Ex7] max rate = |grad T| =", mag, "=", sp.N(mag, 8),
          "   (textbook: (5/8)sqrt(41) ~ 4 C/m)", flush=True)
    print("[Ex7] MATCH rate:", sp.simplify(mag - sp.Rational(5, 8) * sp.sqrt(41)) == 0, flush=True)
    print("[Ex7] unit direction =", unit([-1, -2, 6]).T,
          "   (textbook: (-i - 2j + 6k)/sqrt(41))", flush=True)


# ---------------------------------------------------------------- Example 8
def ex8():
    F = x**2 / 4 + y**2 + z**2 / 9
    g = grad(F, (x, y, z))
    P = {x: -2, y: 1, z: -3}
    gp = g.subs(P)
    print("[Ex8] Fx,Fy,Fz =", g.T, "   (textbook: x/2, 2y, 2z/9)", flush=True)
    print("[Ex8] at (-2,1,-3):", gp.T, "   (textbook: -1, 2, -2/3)", flush=True)
    plane = sp.expand(gp[0] * (x + 2) + gp[1] * (y - 1) + gp[2] * (z + 3))
    print("[Ex8] tangent plane:", plane, "= 0", flush=True)
    print("[Ex8] times -3 :", sp.expand(-3 * plane), "= 0   (textbook: 3x - 6y + 2z + 18 = 0)", flush=True)
    print("[Ex8] MATCH plane:", sp.simplify(-3 * plane - (3 * x - 6 * y + 2 * z + 18)) == 0, flush=True)
    print("[Ex8] point on ellipsoid? F(-2,1,-3) =", F.subs(P), "   (must be 3)", flush=True)
    print("[Ex8] normal line: (x+2)/(-1) = (y-1)/2 = (z+3)/(-2/3)", flush=True)


# ---------------------------------------------------------------- Example 9
def ex9():
    F = 2 * x**2 + y**2 - z
    g = grad(F, (x, y, z))
    P = {x: 1, y: 1, z: 3}
    gp = g.subs(P)
    print("[Ex9] Fx,Fy,Fz =", g.T, " at (1,1,3):", gp.T, "   (textbook: 4, 2, -1)", flush=True)
    plane = sp.expand(gp[0] * (x - 1) + gp[1] * (y - 1) + gp[2] * (z - 3))
    print("[Ex9] tangent plane:", plane, "= 0  ->  z =", sp.solve(sp.Eq(plane, 0), z)[0],
          "   (textbook: z = 4x + 2y - 3)", flush=True)
    print("[Ex9] MATCH:", sp.simplify(sp.solve(sp.Eq(plane, 0), z)[0] - (4 * x + 2 * y - 3)) == 0,
          " (= §14.4 Example 1 결과와 동일)", flush=True)


if __name__ == '__main__':
    for nm, fn in [('Ex1', ex1), ('Ex2', ex2), ('Ex3', ex3), ('Ex4', ex4), ('Ex5', ex5),
                   ('Ex6', ex6), ('Ex7', ex7), ('Ex8', ex8), ('Ex9', ex9)]:
        run(nm, fn)
