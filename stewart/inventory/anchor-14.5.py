#!/usr/bin/env python3
"""Stewart ET 9e  §14.5 The Chain Rule — 독립 재계산 (anchor) 스크립트.
각 항목 20초 타임아웃. 실행: python3 anchor-14.5.py
"""
import signal, traceback
import sympy as sp

x, y, z, t, s, r, u, v = sp.symbols('x y z t s r u v', real=True)


class TO(Exception):
    pass


def _h(a, b):
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
    X, Y = sp.sin(2 * t), sp.cos(t)
    zf = x**2 * y + 3 * x * y**4
    # chain rule
    chain = sp.diff(zf, x).subs({x: X, y: Y}) * sp.diff(X, t) \
        + sp.diff(zf, y).subs({x: X, y: Y}) * sp.diff(Y, t)
    direct = sp.diff(zf.subs({x: X, y: Y}), t)
    print("[Ex1] chain - direct simplifies to 0:", sp.simplify(chain - direct) == 0, flush=True)
    val = sp.simplify(chain.subs(t, 0))
    print("[Ex1] dz/dt at t=0 =", val, "   (textbook: 6)", flush=True)
    print("[Ex1] MATCH:", val == 6, flush=True)


# ---------------------------------------------------------------- Example 2
def ex2():
    T, V = sp.symbols('T V', positive=True)
    P = sp.Rational(831, 100) * T / V
    dPdt = sp.diff(P, T) * sp.Rational(1, 10) + sp.diff(P, V) * sp.Rational(2, 10)
    val = dPdt.subs({T: 300, V: 100})
    print("[Ex2] dP/dt =", sp.simplify(dPdt), flush=True)
    print("[Ex2] value =", val, "=", sp.N(val, 8), "   (textbook: -0.04155, ~0.042 kPa/s decreasing)", flush=True)
    print("[Ex2] MATCH:", sp.nsimplify(val) == sp.Rational(-4155, 100000), flush=True)


# ---------------------------------------------------------------- Example 3
def ex3():
    X, Y = s * t**2, s**2 * t
    zf = sp.exp(x) * sp.sin(y)
    zs = sp.diff(zf, x).subs({x: X, y: Y}) * sp.diff(X, s) \
        + sp.diff(zf, y).subs({x: X, y: Y}) * sp.diff(Y, s)
    zt = sp.diff(zf, x).subs({x: X, y: Y}) * sp.diff(X, t) \
        + sp.diff(zf, y).subs({x: X, y: Y}) * sp.diff(Y, t)
    book_s = t**2 * sp.exp(s * t**2) * sp.sin(s**2 * t) + 2 * s * t * sp.exp(s * t**2) * sp.cos(s**2 * t)
    book_t = 2 * s * t * sp.exp(s * t**2) * sp.sin(s**2 * t) + s**2 * sp.exp(s * t**2) * sp.cos(s**2 * t)
    print("[Ex3] dz/ds =", sp.simplify(zs), flush=True)
    print("[Ex3] dz/dt =", sp.simplify(zt), flush=True)
    print("[Ex3] MATCH ds:", sp.simplify(zs - book_s) == 0,
          " MATCH dt:", sp.simplify(zt - book_t) == 0, flush=True)
    print("[Ex3] cross-check vs direct differentiation:",
          sp.simplify(zs - sp.diff(zf.subs({x: X, y: Y}), s)) == 0,
          sp.simplify(zt - sp.diff(zf.subs({x: X, y: Y}), t)) == 0, flush=True)


# ---------------------------------------------------------------- Example 5
def ex5():
    X = r * s * sp.exp(t)
    Y = r * s**2 * sp.exp(-t)
    Z = r**2 * s * sp.sin(t)
    uf = x**4 * y + y**2 * z**3
    us = (sp.diff(uf, x).subs({x: X, y: Y, z: Z}) * sp.diff(X, s)
          + sp.diff(uf, y).subs({x: X, y: Y, z: Z}) * sp.diff(Y, s)
          + sp.diff(uf, z).subs({x: X, y: Y, z: Z}) * sp.diff(Z, s))
    pt = {r: 2, s: 1, t: 0}
    print("[Ex5] x,y,z at (r,s,t)=(2,1,0):", X.subs(pt), Y.subs(pt), Z.subs(pt),
          "   (textbook: 2, 2, 0)", flush=True)
    val = sp.simplify(us.subs(pt))
    print("[Ex5] du/ds =", val, "   (textbook: 192 = 64*2 + 16*4 + 0*0)", flush=True)
    direct = sp.diff(uf.subs({x: X, y: Y, z: Z}), s).subs(pt)
    print("[Ex5] direct substitution gives", sp.simplify(direct), " MATCH:", sp.simplify(val - direct) == 0, flush=True)


# ---------------------------------------------------------------- Example 6
def ex6():
    f = sp.Function('f')
    g = f(s**2 - t**2, t**2 - s**2)
    expr = sp.simplify(t * sp.diff(g, s) + s * sp.diff(g, t))
    print("[Ex6] t*g_s + s*g_t =", expr, "   (textbook: 0)", flush=True)
    print("[Ex6] MATCH:", expr == 0, flush=True)


# ---------------------------------------------------------------- Example 7
def ex7():
    f = sp.Function('f')
    X, Y = r**2 + s**2, 2 * r * s
    zz = f(X, Y)
    zr = sp.diff(zz, r)
    zrr = sp.diff(zz, r, 2)
    fx = sp.Derivative(f(x, y), x)
    print("[Ex7a] dz/dr =", zr, flush=True)
    # textbook (b): 2 f_x + 4r^2 f_xx + 8rs f_xy + 4s^2 f_yy
    a, b = sp.symbols('a b')
    book = (2 * sp.Subs(sp.Derivative(f(a, b), a), (a, b), (X, Y))
            + 4 * r**2 * sp.Subs(sp.Derivative(f(a, b), a, a), (a, b), (X, Y))
            + 8 * r * s * sp.Subs(sp.Derivative(f(a, b), a, b), (a, b), (X, Y))
            + 4 * s**2 * sp.Subs(sp.Derivative(f(a, b), b, b), (a, b), (X, Y)))
    print("[Ex7b] textbook       = 2 f_x + 4r^2 f_xx + 8rs f_xy + 4s^2 f_yy", flush=True)
    print("[Ex7b] (sympy의 추상 Subs 객체끼리는 구조 비교가 되지 않으므로,"
          " 구체적인 f 여러 개로 항등식을 검증한다)", flush=True)
    a_, b_ = sp.symbols('a_ b_')
    tests = {
        'exp(x)sin(y)+x^3y^2': lambda X_, Y_: sp.exp(X_) * sp.sin(Y_) + X_**3 * Y_**2,
        'log(1+x^2+y^2)': lambda X_, Y_: sp.log(1 + X_**2 + Y_**2),
        'x^2 y - cos(xy)': lambda X_, Y_: X_**2 * Y_ - sp.cos(X_ * Y_),
    }
    for label, g in tests.items():
        lhs = sp.diff(g(X, Y), r, 2)
        G = g(a_, b_)
        rhs = (2 * sp.diff(G, a_) + 4 * r**2 * sp.diff(G, a_, 2)
               + 8 * r * s * sp.diff(G, a_, b_) + 4 * s**2 * sp.diff(G, b_, 2)).subs({a_: X, b_: Y})
        print(f"[Ex7b] concrete f = {label}: MATCH =", sp.simplify(lhs - rhs) == 0, flush=True)


# ---------------------------------------------------------------- Example 8
def ex8():
    F = x**3 + y**3 - 6 * x * y
    dydx = sp.simplify(-sp.diff(F, x) / sp.diff(F, y))
    book = (2 * y - x**2) / (y**2 - 2 * x)
    print("[Ex8] dy/dx = -Fx/Fy =", dydx, "   (textbook: -(x^2-2y)/(y^2-2x) = (2y-x^2)/(y^2-2x))", flush=True)
    print("[Ex8] MATCH:", sp.simplify(dydx - book) == 0, flush=True)
    yf = sp.Function('y')
    imp = sp.solve(sp.Eq(sp.diff(F.subs(y, yf(x)), x), 0), sp.Derivative(yf(x), x))[0]
    print("[Ex8] implicit-diff cross-check:", sp.simplify(imp - book.subs(y, yf(x))) == 0, flush=True)


# ---------------------------------------------------------------- Example 9
def ex9():
    F = x**3 + y**3 + z**3 + 6 * x * y * z + 4
    zx = sp.simplify(-sp.diff(F, x) / sp.diff(F, z))
    zy = sp.simplify(-sp.diff(F, y) / sp.diff(F, z))
    bx = -(x**2 + 2 * y * z) / (z**2 + 2 * x * y)
    by = -(y**2 + 2 * x * z) / (z**2 + 2 * x * y)
    print("[Ex9] dz/dx =", zx, "   (textbook: -(x^2+2yz)/(z^2+2xy))", flush=True)
    print("[Ex9] dz/dy =", zy, "   (textbook: -(y^2+2xz)/(z^2+2xy))", flush=True)
    print("[Ex9] MATCH:", sp.simplify(zx - bx) == 0, sp.simplify(zy - by) == 0, flush=True)


if __name__ == '__main__':
    for nm, fn in [('Ex1', ex1), ('Ex2', ex2), ('Ex3', ex3), ('Ex5', ex5),
                   ('Ex6', ex6), ('Ex7', ex7), ('Ex8', ex8), ('Ex9', ex9)]:
        run(nm, fn)
    print("[Ex4] 개념형(수형도로 연쇄법칙 식을 써 내려가기) — 수치 재계산 대상 아님", flush=True)
