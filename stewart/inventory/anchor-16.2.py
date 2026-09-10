#!/usr/bin/env python3
"""§16.2 Line Integrals — 예제 기준값 독립 재계산 (sympy)."""
import signal
from sympy import *

def run(label, fn, t=20):
    def h(s, f): raise TimeoutError
    signal.signal(signal.SIGALRM, h); signal.alarm(t)
    try:
        print(f"[{label}] {fn()}", flush=True)
    except Exception as e:
        print(f"[{label}] ERROR {type(e).__name__}: {e}", flush=True)
    finally:
        signal.alarm(0)

t, x, y, z, k = symbols('t x y z k', real=True)

def sc(fexpr, r, a, b):
    """scalar line integral wrt arc length"""
    rp = [diff(c, t) for c in r]
    ds = sqrt(sum(c**2 for c in rp))
    return simplify(integrate(fexpr.subs(dict(zip((x, y, z)[:len(r)], r))) * ds, (t, a, b)))

# Ex1: int_C (2 + x^2 y) ds, C upper half unit circle. textbook: 2*pi + 2/3
run("Ex1", lambda: f"{sc(2 + x**2*y, [cos(t), sin(t)], 0, pi)}  (교재 2π+2/3 = {simplify(2*pi+Rational(2,3))})")

# Ex2: int_C 2x ds, C1: y=x^2 from (0,0)->(1,1); C2: x=1 from (1,1)->(1,2)
def ex2():
    I1 = simplify(integrate(2*t*sqrt(1 + (2*t)**2), (t, 0, 1)))     # param x=t, y=t^2
    I2 = simplify(integrate(2*1, (t, 1, 2)))                        # param x=1, y=t
    tot = simplify(I1 + I2)
    txt = (5*sqrt(5) - 1)/6 + 2
    return f"C1={I1} (교재 (5√5-1)/6={simplify((5*sqrt(5)-1)/6)}), C2={I2}, total={tot}, 교재합={simplify(txt)}, match={simplify(tot-txt)==0}"
run("Ex2", ex2)

# Ex3: semicircle x^2+y^2=1, y>=0, rho = k(1-y). mass, centroid
def ex3():
    r = [cos(t), sin(t)]
    rho = k*(1 - y)
    m = sc(rho, r, 0, pi)
    ybar = simplify(sc(y*rho, r, 0, pi)/m)
    xbar = simplify(sc(x*rho, r, 0, pi)/m)
    txt = (4 - pi)/(2*(pi - 2))
    return (f"m={m} (교재 k(π-2)), xbar={xbar}, ybar={ybar}, "
            f"교재 ybar=(4-π)/(2(π-2))={simplify(txt)}≈{float(txt):.5f}, "
            f"match={simplify(ybar-txt)==0}, ybar num={float(ybar):.5f} (교재 ≈0.38)")
run("Ex3", ex3)

# Ex4: int_C y^2 dx + x dy on two paths from (-5,-3) to (0,2)
def ex4():
    # (a) segment: x=5t-5, y=5t-3
    xa, ya = 5*t - 5, 5*t - 3
    Ia = simplify(integrate(ya**2*diff(xa, t) + xa*diff(ya, t), (t, 0, 1)))
    # (b) parabola x = 4 - y^2, param by y
    yb = t; xb = 4 - t**2
    Ib = simplify(integrate(yb**2*diff(xb, t) + xb*diff(yb, t), (t, -3, 2)))
    # (-C1): x=-5t, y=2-5t
    xc, yc = -5*t, 2 - 5*t
    Ic = simplify(integrate(yc**2*diff(xc, t) + xc*diff(yc, t), (t, 0, 1)))
    return (f"(a)={Ia} (교재 -5/6), (b)={Ib}={float(Ib):.6f} (교재 40 5/6 = {Rational(245,6)}"
            f"={float(Rational(245,6)):.6f}), (-C1)={Ic} (교재 5/6), "
            f"match a={Ia==Rational(-5,6)}, b={Ib==Rational(245,6)}, -C1={Ic==Rational(5,6)}")
run("Ex4", ex4)

# Ex5: int_C y sin z ds, helix x=cos t, y=sin t, z=t, 0..2pi. textbook sqrt(2) pi
run("Ex5", lambda: f"{sc(y*sin(z), [cos(t), sin(t), t], 0, 2*pi)}  (교재 √2 π), match="
                   f"{simplify(sc(y*sin(z),[cos(t),sin(t),t],0,2*pi) - sqrt(2)*pi)==0}")

# Ex6: int_C y dx + z dy + x dz; C1 (2,0,0)->(3,4,5), C2 (3,4,5)->(3,4,0)
def ex6():
    r1 = [2 + t, 4*t, 5*t]
    I1 = simplify(integrate(r1[1]*diff(r1[0], t) + r1[2]*diff(r1[1], t) + r1[0]*diff(r1[2], t), (t, 0, 1)))
    r2 = [Integer(3), Integer(4), 5 - 5*t]
    I2 = simplify(integrate(r2[1]*diff(r2[0], t) + r2[2]*diff(r2[1], t) + r2[0]*diff(r2[2], t), (t, 0, 1)))
    return f"C1={I1}={float(I1)} (교재 24.5), C2={I2} (교재 -15), total={I1+I2}={float(I1+I2)} (교재 9.5)"
run("Ex6", ex6)

# Ex7: work of F = x^2 i - xy j along r(t)=<cos t, sin t>, 0..pi/2. textbook -2/3
def ex7():
    r = [cos(t), sin(t)]
    F = [r[0]**2, -r[0]*r[1]]
    W = simplify(integrate(sum(Fi*diff(ri, t) for Fi, ri in zip(F, r)), (t, 0, pi/2)))
    return f"W={W} (교재 -2/3), match={W==Rational(-2,3)}"
run("Ex7", ex7)

# Ex8: F = xy i + yz j + zx k, twisted cubic r=<t,t^2,t^3>, 0..1. textbook 27/28
def ex8():
    r = [t, t**2, t**3]
    F = [r[0]*r[1], r[1]*r[2], r[2]*r[0]]
    I = simplify(integrate(sum(Fi*diff(ri, t) for Fi, ri in zip(F, r)), (t, 0, 1)))
    return f"I={I} (교재 27/28), match={I==Rational(27,28)}; F(r(t))=({[simplify(f) for f in F]})"
run("Ex8", ex8)
