#!/usr/bin/env python3
"""§16.4 Green's Theorem — 예제 기준값 독립 재계산 (sympy)."""
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

x, y, t, r, th = symbols('x y t r theta', real=True)
a, b = symbols('a b', positive=True)

def lineint(P, Q, rx, ry, t0, t1):
    sub = {x: rx, y: ry}
    return simplify(integrate(P.subs(sub)*diff(rx, t) + Q.subs(sub)*diff(ry, t), (t, t0, t1)))

# Ex1: int_C x^4 dx + xy dy over triangle (0,0)->(1,0)->(0,1)->(0,0). textbook 1/6
def ex1():
    P, Q = x**4, x*y
    dbl = simplify(integrate(integrate(diff(Q, x) - diff(P, y), (y, 0, 1 - x)), (x, 0, 1)))
    # direct line integral over the three sides
    s1 = lineint(P, Q, t, Integer(0), 0, 1)                 # (0,0)->(1,0)
    s2 = lineint(P, Q, 1 - t, t, 0, 1)                      # (1,0)->(0,1)
    s3 = lineint(P, Q, Integer(0), 1 - t, 0, 1)             # (0,1)->(0,0)
    direct = simplify(s1 + s2 + s3)
    return f"double={dbl}, direct line integral={direct} (sides {s1},{s2},{s3}); 교재 1/6; match={dbl==Rational(1,6)==direct}"
run("Ex1", ex1)

# Ex2: int_C (3y - e^{sin x}) dx + (7x + sqrt(y^4+1)) dy, C: x^2+y^2=9. textbook 36 pi
def ex2():
    P, Q = 3*y - exp(sin(x)), 7*x + sqrt(y**4 + 1)
    integrand = simplify(diff(Q, x) - diff(P, y))           # should be 4
    dbl = simplify(integrate(integrate(integrand*r, (r, 0, 3)), (th, 0, 2*pi)))
    return f"Qx-Py={integrand}; double={dbl} (=4*area of disk r=3 = {4*pi*9}); 교재 36π; match={dbl==36*pi}"
run("Ex2", ex2)

# Ex3: area of ellipse x^2/a^2 + y^2/b^2 = 1 via A = 1/2 int x dy - y dx. textbook pi a b
def ex3():
    rx, ry = a*cos(t), b*sin(t)
    A3 = simplify(Rational(1,2)*integrate(rx*diff(ry, t) - ry*diff(rx, t), (t, 0, 2*pi)))
    A1 = simplify(integrate(rx*diff(ry, t), (t, 0, 2*pi)))                 # int x dy
    A2 = simplify(-integrate(ry*diff(rx, t), (t, 0, 2*pi)))                # -int y dx
    return f"A(1/2 form)={A3}, A(x dy)={A1}, A(-y dx)={A2}; 교재 πab; match={A3==pi*a*b==A1==A2}"
run("Ex3", ex3)

# Ex4: int_C y^2 dx + 3xy dy, C boundary of semiannulus 1<=r<=2, 0<=theta<=pi. textbook 14/3
def ex4():
    P, Q = y**2, 3*x*y
    integrand = simplify(diff(Q, x) - diff(P, y))            # y
    dbl = simplify(integrate(integrate((r*sin(th))*r, (r, 1, 2)), (th, 0, pi)))
    # direct: boundary = outer arc r=2 (0->pi), segment (-2,0)->(-1,0), inner arc r=1 (pi->0), segment (1,0)->(2,0)
    o = lineint(P, Q, 2*cos(t), 2*sin(t), 0, pi)
    s_left = lineint(P, Q, t, Integer(0), -2, -1)
    i = lineint(P, Q, cos(t), sin(t), pi, 0)
    s_right = lineint(P, Q, t, Integer(0), 1, 2)
    direct = simplify(o + s_left + i + s_right)
    return (f"Qx-Py={integrand}; double={dbl}; direct boundary integral={direct} "
            f"(outer {o}, inner {i}, segs {s_left},{s_right}); 교재 14/3; match={dbl==Rational(14,3)==direct}")
run("Ex4", ex4)

# Ex5: F = (-y i + x j)/(x^2+y^2); show closed integral = 2 pi around origin
def ex5():
    P = -y/(x**2 + y**2); Q = x/(x**2 + y**2)
    curlish = simplify(diff(Q, x) - diff(P, y))              # 0 away from origin
    Py, Qx = simplify(diff(P, y)), simplify(diff(Q, x))
    circ = lineint(P, Q, a*cos(t), a*sin(t), 0, 2*pi)        # circle of radius a
    # a non-circular closed curve enclosing the origin (ellipse 3cos t, 2 sin t):
    # sympy's symbolic antiderivative is discontinuous on [0,2pi], so evaluate the
    # integral over four quarter-periods and also numerically.
    ell_int = ((-2*sin(t))*(-3*sin(t)) + (3*cos(t))*(2*cos(t))) / ((3*cos(t))**2 + (2*sin(t))**2)
    ell_pieces = sum(integrate(ell_int, (t, k*pi/2, (k+1)*pi/2)) for k in range(4))
    ell = simplify(ell_pieces)
    ell_num = N(Integral(ell_int, (t, 0, 2*pi)).evalf())
    ok = (circ == 2*pi) and abs(float(ell_num) - float(2*pi)) < 1e-9
    return (f"Py={Py}, Qx={Qx}, Qx-Py={curlish} (원점 제외 0); circle radius a: {circ}; "
            f"ellipse (3cos t,2sin t): {ell} (numeric {ell_num}, 2π={N(2*pi)}); "
            f"교재 2π; match={ok}")
run("Ex5", ex5, 60)
