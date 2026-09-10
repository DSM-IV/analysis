#!/usr/bin/env python3
"""Stewart ET 9e  §14.4 Tangent Planes and Linear Approximations
독립 재계산 (anchor) 스크립트.  각 항목은 20초 타임아웃.
실행: python3 anchor-14.4.py
"""
import signal, sys, traceback
import sympy as sp

x, y, z, t, r, h, eps = sp.symbols('x y z t r h epsilon', real=True)


class TO(Exception):
    pass


def _h(s, f):
    raise TO()


def run(name, fn):
    signal.signal(signal.SIGALRM, _h)
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


# ---------------------------------------------------------------- Example 1
def ex1():
    f = 2 * x**2 + y**2
    fx, fy = sp.diff(f, x), sp.diff(f, y)
    a, b = 1, 1
    z0 = f.subs({x: a, y: b})
    plane = sp.expand(z0 + fx.subs({x: a, y: b}) * (x - a) + fy.subs({x: a, y: b}) * (y - b))
    print("[Ex1] fx, fy =", fx, ",", fy, "  fx(1,1)=", fx.subs({x: 1, y: 1}),
          " fy(1,1)=", fy.subs({x: 1, y: 1}), flush=True)
    print("[Ex1] tangent plane z =", plane, "   (textbook: 4x + 2y - 3)", flush=True)
    print("[Ex1] MATCH:", sp.simplify(plane - (4 * x + 2 * y - 3)) == 0, flush=True)


# ---------------------------------------------------------------- Example 2
def ex2():
    f = x * sp.exp(x * y)
    fx, fy = sp.diff(f, x), sp.diff(f, y)
    a, b = 1, 0
    L = sp.expand(f.subs({x: a, y: b}) + fx.subs({x: a, y: b}) * (x - a)
                  + fy.subs({x: a, y: b}) * (y - b))
    print("[Ex2] fx =", sp.simplify(fx), "  fy =", sp.simplify(fy), flush=True)
    print("[Ex2] fx(1,0)=", fx.subs({x: 1, y: 0}), " fy(1,0)=", fy.subs({x: 1, y: 0}), flush=True)
    print("[Ex2] L(x,y) =", L, "   (textbook: x + y)", flush=True)
    print("[Ex2] L(1.1,-0.1) =", sp.nsimplify(L.subs({x: sp.Rational(11, 10), y: sp.Rational(-1, 10)})),
          "   (textbook: 1)", flush=True)
    exact = f.subs({x: sp.Rational(11, 10), y: sp.Rational(-1, 10)})
    print("[Ex2] exact f(1.1,-0.1) =", sp.N(exact, 8), "   (textbook: 0.98542)", flush=True)


# ---------------------------------------------------------------- Example 3
def ex3():
    # Table-based: f(96,70)=125, f_T(96,70)~3.75, f_H(96,70)~0.9
    T, H = sp.symbols('T H', real=True)
    L = 125 + sp.Rational(15, 4) * (T - 96) + sp.Rational(9, 10) * (H - 70)
    print("[Ex3] L(T,H) =", sp.expand(L), flush=True)
    v = L.subs({T: 97, H: 72})
    print("[Ex3] L(97,72) =", v, "=", sp.N(v), "   (textbook: 130.55 -> I ~ 131F)", flush=True)


# ---------------------------------------------------------------- Example 4
def ex4():
    f = x**2 + 3 * x * y - y**2
    dz = sp.diff(f, x) * sp.Symbol('dx') + sp.diff(f, y) * sp.Symbol('dy')
    print("[Ex4a] dz =", dz, "   (textbook: (2x+3y)dx + (3x-2y)dy)", flush=True)
    dxv, dyv = sp.Rational(5, 100), sp.Rational(-4, 100)
    dzv = dz.subs({x: 2, y: 3, sp.Symbol('dx'): dxv, sp.Symbol('dy'): dyv})
    print("[Ex4b] dz =", dzv, "=", sp.N(dzv), "   (textbook: 0.65)", flush=True)
    Dz = f.subs({x: sp.Rational(205, 100), y: sp.Rational(296, 100)}) - f.subs({x: 2, y: 3})
    print("[Ex4b] Delta z =", sp.nsimplify(Dz), "=", sp.N(Dz), "   (textbook: 0.6449)", flush=True)


# ---------------------------------------------------------------- Example 5
def ex5():
    V = sp.pi * r**2 * h / 3
    dr, dh = sp.symbols('dr dh')
    dV = sp.diff(V, r) * dr + sp.diff(V, h) * dh
    print("[Ex5a] dV =", sp.simplify(dV), "   (textbook: (2*pi*r*h/3)dr + (pi*r^2/3)dh)", flush=True)
    est = sp.simplify(dV.subs({r: 10, h: 25, dr: eps, dh: eps}))
    print("[Ex5a] dV at r=10,h=25,dr=dh=eps :", est, "   (textbook: 200*pi*eps)", flush=True)
    print("[Ex5a] MATCH:", sp.simplify(est - 200 * sp.pi * eps) == 0, flush=True)
    val = est.subs(eps, sp.Rational(1, 10))
    print("[Ex5b] eps=0.1 -> dV =", val, "=", sp.N(val, 6), "   (textbook: ~63 cm^3)", flush=True)
    Vol = V.subs({r: 10, h: 25})
    print("[Ex5b] V =", Vol, "=", sp.N(Vol, 6), "  relative error =", sp.N(val / Vol, 4),
          "   (textbook: 2618, 0.024 = 2.4%)", flush=True)


# ---------------------------------------------------------------- Example 6
def ex6():
    dx, dy, dz_ = sp.symbols('dx dy dz')
    V = x * y * z
    dV = sp.diff(V, x) * dx + sp.diff(V, y) * dy + sp.diff(V, z) * dz_
    print("[Ex6a] dV =", dV, "   (textbook: yz dx + xz dy + xy dz)", flush=True)
    est = sp.expand(dV.subs({x: 75, y: 60, z: 40, dx: eps, dy: eps, dz_: eps}))
    print("[Ex6a] dV =", est, "   (textbook: 9900*eps)", flush=True)
    print("[Ex6a] MATCH:", sp.simplify(est - 9900 * eps) == 0, flush=True)
    val = est.subs(eps, sp.Rational(2, 10))
    print("[Ex6b] eps=0.2 -> dV =", val, "   (textbook: 1980 cm^3)", flush=True)
    Vol = 75 * 60 * 40
    print("[Ex6b] V =", Vol, "  relative error =", sp.N(sp.Rational(int(val), Vol), 4),
          "   (textbook: about 1%)", flush=True)


if __name__ == '__main__':
    for nm, fn in [('Ex1', ex1), ('Ex2', ex2), ('Ex3', ex3), ('Ex4', ex4),
                   ('Ex5', ex5), ('Ex6', ex6)]:
        run(nm, fn)
