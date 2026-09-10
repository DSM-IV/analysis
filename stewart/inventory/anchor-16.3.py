#!/usr/bin/env python3
"""§16.3 The Fundamental Theorem for Line Integrals — 예제 기준값 독립 재계산 (sympy)."""
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

x, y, z, t = symbols('x y z t', real=True)
m, M, G = symbols('m M G', positive=True)

# Ex1: work of gravitational field from (3,4,12) to (2,2,0)
def ex1():
    f = m*M*G/sqrt(x**2 + y**2 + z**2)
    W = simplify(f.subs({x:2, y:2, z:0}) - f.subs({x:3, y:4, z:12}))
    txt = m*M*G*(1/(2*sqrt(2)) - Rational(1,13))
    return (f"W = {W}; 교재 mMG(1/(2√2) - 1/13) = {simplify(txt)}; "
            f"match={simplify(W-txt)==0}; num factor={float(1/(2*sqrt(2))-Rational(1,13)):.6f}")
run("Ex1", ex1)

# Ex2: conservativeness test
def ex2():
    Pa, Qa = x - y, x - 2
    Pb, Qb = 3 + 2*x*y, x**2 - 3*y**2
    a = (diff(Pa, y), diff(Qa, x))
    b = (diff(Pb, y), diff(Qb, x))
    return (f"(a) Py={a[0]}, Qx={a[1]} -> equal? {simplify(a[0]-a[1])==0} (교재: 비보존)"
            f" | (b) Py={b[0]}, Qx={b[1]} -> equal? {simplify(b[0]-b[1])==0} (교재: 보존, D=R^2 단순연결)")
run("Ex2", ex2)

# Ex3: potential of F = (3+2xy) i + (x^2-3y^2) j ; textbook f = 3x + x^2 y - y^3 + K
def ex3():
    f = 3*x + x**2*y - y**3
    grad = (simplify(diff(f, x)), simplify(diff(f, y)))
    ok = grad == (3 + 2*x*y, x**2 - 3*y**2)
    return f"grad(3x + x^2 y - y^3) = {grad}; == F? {ok}"
run("Ex3", ex3)

# Ex4: line integral along r(t) = e^t sin t i + e^t cos t j, 0..pi.  textbook e^{3pi}+1
def ex4():
    f = 3*x + x**2*y - y**3
    r0 = (E**0*sin(0), E**0*cos(0))                 # (0, 1)
    r1 = (exp(pi)*sin(pi), exp(pi)*cos(pi))         # (0, -e^pi)
    val_fte = simplify(f.subs({x:r1[0], y:r1[1]}) - f.subs({x:r0[0], y:r0[1]}))
    # direct parametric evaluation (independent method)
    rx, ry = exp(t)*sin(t), exp(t)*cos(t)
    P = 3 + 2*rx*ry; Q = rx**2 - 3*ry**2
    direct = simplify(integrate(P*diff(rx, t) + Q*diff(ry, t), (t, 0, pi)))
    # Solution 2 of the text: straight segment x=0, y=s, s from 1 to -e^pi  (text params r(t)=t j, -1..e^pi on -y)
    s = symbols('s', real=True)
    seg = simplify(integrate((0**2 - 3*s**2)*1, (s, 1, -exp(pi))))
    txt = exp(3*pi) + 1
    return (f"endpoints r(0)={r0}, r(pi)={r1}; FTC value={val_fte}; direct param integral={simplify(direct)}; "
            f"straight-segment value={seg}; 교재 e^(3pi)+1={txt}; "
            f"match FTC={simplify(val_fte-txt)==0}, match direct={simplify(direct-txt)==0}, match seg={simplify(seg-txt)==0}")
run("Ex4", ex4, 60)

# Ex5: potential of F = y^2 i + (2xy + e^{3z}) j + 3y e^{3z} k ; textbook f = x y^2 + y e^{3z} + K
def ex5():
    f = x*y**2 + y*exp(3*z)
    grad = tuple(simplify(diff(f, v)) for v in (x, y, z))
    F = (y**2, 2*x*y + exp(3*z), 3*y*exp(3*z))
    ok = all(simplify(a-b) == 0 for a, b in zip(grad, F))
    return f"grad f = {grad}; == F? {ok}"
run("Ex5", ex5)
