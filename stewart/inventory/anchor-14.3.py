#!/usr/bin/env python3
"""§14.3 Partial Derivatives — 예제 1~10 최종답 독립 재계산 (sympy).

각 항목은 signal.alarm(20)으로 타임아웃을 걸고, 결과를 flush 출력한다.
교재 최종답(anchor)과 sympy 결과를 simplify(diff)==0 으로 대조한다.
"""
import signal
import sys
import sympy as sp

x, y, z, t, h, m, a, b, u, v = sp.symbols('x y z t h m a b u v', real=True)


class Timeout(Exception):
    pass


def _handler(signum, frame):
    raise Timeout()


def item(label):
    """항목 단위 데코레이터: 20초 타임아웃 + flush 출력."""
    def deco(fn):
        print(f"\n=== {label} ===", flush=True)
        signal.signal(signal.SIGALRM, _handler)
        signal.alarm(20)
        try:
            fn()
        except Timeout:
            print("  !! TIMEOUT (20s)", flush=True)
        except Exception as e:  # noqa: BLE001
            print(f"  !! ERROR: {type(e).__name__}: {e}", flush=True)
        finally:
            signal.alarm(0)
        return fn
    return deco


def chk(name, got, want):
    """got == want 판정 (기호식은 simplify(got-want)==0)."""
    if isinstance(got, sp.Expr) or isinstance(want, sp.Expr):
        ok = sp.simplify(sp.sympify(got) - sp.sympify(want)) == 0
    else:
        ok = got == want
    print(f"  {name}: sympy = {got}", flush=True)
    print(f"  {'':{len(name)}}  교재  = {want}   -> {'MATCH' if ok else 'MISMATCH'}",
          flush=True)
    return ok


# ---------------------------------------------------------------- Example 1
@item("Example 1  f = x^3 + x^2 y^3 - 2 y^2;  f_x(2,1), f_y(2,1)")
def ex1():
    f = x**3 + x**2*y**3 - 2*y**2
    fx, fy = sp.diff(f, x), sp.diff(f, y)
    chk("f_x(x,y)", sp.expand(fx), 3*x**2 + 2*x*y**3)
    chk("f_y(x,y)", sp.expand(fy), 3*x**2*y**2 - 4*y)
    chk("f_x(2,1)", fx.subs({x: 2, y: 1}), sp.Integer(16))
    chk("f_y(2,1)", fy.subs({x: 2, y: 1}), sp.Integer(8))


# ---------------------------------------------------------------- Example 2
@item("Example 2  f = sin(x/(1+y));  f_x, f_y")
def ex2():
    f = sp.sin(x/(1 + y))
    chk("df/dx", sp.simplify(sp.diff(f, x)),
        sp.cos(x/(1 + y)) * 1/(1 + y))
    chk("df/dy", sp.simplify(sp.diff(f, y)),
        -sp.cos(x/(1 + y)) * x/(1 + y)**2)


# ---------------------------------------------------------------- Example 3
@item("Example 3  f = 4 - x^2 - 2y^2;  f_x(1,1), f_y(1,1)")
def ex3():
    f = 4 - x**2 - 2*y**2
    fx, fy = sp.diff(f, x), sp.diff(f, y)
    chk("f_x(x,y)", fx, -2*x)
    chk("f_y(x,y)", fy, -4*y)
    chk("f_x(1,1)", fx.subs({x: 1, y: 1}), sp.Integer(-2))
    chk("f_y(1,1)", fy.subs({x: 1, y: 1}), sp.Integer(-4))
    # 자취(trace) 확인: y=1 -> z = 2 - x^2 ; x=1 -> z = 3 - 2y^2
    chk("trace y=1", sp.expand(f.subs(y, 1)), 2 - x**2)
    chk("trace x=1", sp.expand(f.subs(x, 1)), 3 - 2*y**2)


# ---------------------------------------------------------------- Example 4
@item("Example 4  B(m,h) = m/h^2;  B_m, B_h at (64, 1.68)")
def ex4():
    hh = sp.Symbol('h', positive=True)
    B = m/hh**2
    Bm, Bh = sp.diff(B, m), sp.diff(B, hh)
    chk("B_m", Bm, 1/hh**2)
    chk("B_h", Bh, -2*m/hh**3)
    vals = {m: sp.Rational(64), hh: sp.Rational(168, 100)}
    bm = sp.N(Bm.subs(vals), 6)
    bh = sp.N(Bh.subs(vals), 6)
    b0 = sp.N(B.subs(vals), 6)
    print(f"  B_m(64,1.68) = {bm}   교재 ~= 0.35   -> "
          f"{'MATCH' if abs(bm - 0.35) < 0.005 else 'MISMATCH'}", flush=True)
    print(f"  B_h(64,1.68) = {bh}   교재 ~= -27    -> "
          f"{'MATCH' if abs(bh + 27) < 0.5 else 'MISMATCH'}", flush=True)
    print(f"  B(64,1.68)   = {b0}   교재 ~= 22.68  -> "
          f"{'MATCH' if abs(b0 - 22.68) < 0.01 else 'MISMATCH'}", flush=True)


# ---------------------------------------------------------------- Example 5
@item("Example 5  x^3+y^3+z^3+6xyz+4=0;  z_x, z_y  and values at (-1,1,2)")
def ex5():
    Z = sp.Function('Z')(x, y)
    F = x**3 + y**3 + z**3 + 6*x*y*z + 4
    # 방법 A: 음함수 미분 (F(x,y,Z(x,y)) = 0 을 x, y 로 미분)
    G = F.subs(z, Z)
    zx = sp.solve(sp.Eq(sp.diff(G, x), 0), sp.Derivative(Z, x))[0]
    zy = sp.solve(sp.Eq(sp.diff(G, y), 0), sp.Derivative(Z, y))[0]
    zx = sp.simplify(zx.subs(Z, z))
    zy = sp.simplify(zy.subs(Z, z))
    chk("dz/dx (A)", zx, -(x**2 + 2*y*z)/(z**2 + 2*x*y))
    chk("dz/dy (A)", zy, -(y**2 + 2*x*z)/(z**2 + 2*x*y))
    # 방법 B: -F_x/F_z, -F_y/F_z
    zxB = sp.simplify(-sp.diff(F, x)/sp.diff(F, z))
    zyB = sp.simplify(-sp.diff(F, y)/sp.diff(F, z))
    chk("dz/dx (B)", zxB, -(x**2 + 2*y*z)/(z**2 + 2*x*y))
    chk("dz/dy (B)", zyB, -(y**2 + 2*x*z)/(z**2 + 2*x*y))
    P = {x: -1, y: 1, z: 2}
    print(f"  점 (-1,1,2) 가 곡면 위: F = {F.subs(P)} (0 이어야 함)", flush=True)
    chk("dz/dx at P", sp.nsimplify(zx.subs(P)), sp.Rational(-5, 2))
    chk("dz/dy at P", sp.nsimplify(zy.subs(P)), sp.Rational(3, 2))


# ---------------------------------------------------------------- Example 6
@item("Example 6  f = e^(xy) ln z;  f_x, f_y, f_z")
def ex6():
    zz = sp.Symbol('z', positive=True)
    f = sp.exp(x*y)*sp.log(zz)
    chk("f_x", sp.diff(f, x), y*sp.exp(x*y)*sp.log(zz))
    chk("f_y", sp.diff(f, y), x*sp.exp(x*y)*sp.log(zz))
    chk("f_z", sp.diff(f, zz), sp.exp(x*y)/zz)


# ---------------------------------------------------------------- Example 7
@item("Example 7  f = x^3 + x^2 y^3 - 2y^2;  second partials")
def ex7():
    f = x**3 + x**2*y**3 - 2*y**2
    chk("f_xx", sp.expand(sp.diff(f, x, 2)), 6*x + 2*y**3)
    chk("f_xy", sp.expand(sp.diff(f, x, y)), 6*x*y**2)
    chk("f_yx", sp.expand(sp.diff(f, y, x)), 6*x*y**2)
    chk("f_yy", sp.expand(sp.diff(f, y, 2)), 6*x**2*y - 4)


# ---------------------------------------------------------------- Example 8
@item("Example 8  f = sin(3x + yz);  f_xxyz")
def ex8():
    f = sp.sin(3*x + y*z)
    chk("f_x", sp.diff(f, x), 3*sp.cos(3*x + y*z))
    chk("f_xx", sp.diff(f, x, 2), -9*sp.sin(3*x + y*z))
    chk("f_xxy", sp.diff(f, x, 2, y), -9*z*sp.cos(3*x + y*z))
    chk("f_xxyz", sp.diff(f, x, 2, y, z),
        -9*sp.cos(3*x + y*z) + 9*y*z*sp.sin(3*x + y*z))


# ---------------------------------------------------------------- Example 9
@item("Example 9  u = e^x sin y  solves  u_xx + u_yy = 0")
def ex9():
    U = sp.exp(x)*sp.sin(y)
    chk("u_x", sp.diff(U, x), sp.exp(x)*sp.sin(y))
    chk("u_y", sp.diff(U, y), sp.exp(x)*sp.cos(y))
    chk("u_xx", sp.diff(U, x, 2), sp.exp(x)*sp.sin(y))
    chk("u_yy", sp.diff(U, y, 2), -sp.exp(x)*sp.sin(y))
    chk("u_xx + u_yy", sp.simplify(sp.diff(U, x, 2) + sp.diff(U, y, 2)),
        sp.Integer(0))


# --------------------------------------------------------------- Example 10
@item("Example 10  u = sin(x - a t)  solves  u_tt = a^2 u_xx")
def ex10():
    U = sp.sin(x - a*t)
    uxx = sp.diff(U, x, 2)
    utt = sp.diff(U, t, 2)
    chk("u_x", sp.diff(U, x), sp.cos(x - a*t))
    chk("u_t", sp.diff(U, t), -a*sp.cos(x - a*t))
    chk("u_xx", uxx, -sp.sin(x - a*t))
    chk("u_tt", utt, -a**2*sp.sin(x - a*t))
    chk("u_tt - a^2 u_xx", sp.simplify(utt - a**2*uxx), sp.Integer(0))


# ------------------------------------------- 절 도입 (heat index 수치 추정)
@item("Section opening  Table 1 heat-index estimates  f_T(96,70), f_H(96,70)")
def opening():
    # Table 1: 행 T = 94, 96, 98 / 열 H = 65, 70, 75
    f = {(94, 70): 118, (96, 70): 125, (98, 70): 133,
         (96, 65): 121, (96, 75): 130}
    fwd = (f[(98, 70)] - f[(96, 70)]) / 2          # h = 2
    bwd = (f[(94, 70)] - f[(96, 70)]) / -2         # h = -2
    fT = (fwd + bwd) / 2
    print(f"  g'(96) 전진 {fwd}, 후진 {bwd}, 평균 {fT}  교재 ~= 3.75 -> "
          f"{'MATCH' if abs(fT - 3.75) < 1e-9 else 'MISMATCH'}", flush=True)
    fwd2 = (f[(96, 75)] - f[(96, 70)]) / 5         # h = 5
    bwd2 = (f[(96, 65)] - f[(96, 70)]) / -5        # h = -5
    fH = (fwd2 + bwd2) / 2
    print(f"  G'(70) 전진 {fwd2}, 후진 {bwd2}, 평균 {fH}  교재 ~= 0.9  -> "
          f"{'MATCH' if abs(fH - 0.9) < 1e-9 else 'MISMATCH'}", flush=True)


print("\n--- done ---", flush=True)
sys.exit(0)
