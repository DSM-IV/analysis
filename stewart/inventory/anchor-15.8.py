#!/usr/bin/env python3
"""Anchor recomputation for Stewart ET9 §15.8 Triple Integrals in Spherical Coordinates."""
import signal
from sympy import *

x, y, z = symbols('x y z', real=True)
rho = symbols('rho', nonnegative=True)
th = symbols('theta', real=True); ph = symbols('phi', real=True)

def run(tag, fn):
    def _to(s, f): raise TimeoutError
    signal.signal(signal.SIGALRM, _to); signal.alarm(20)
    try: print(f"[{tag}] {fn()}", flush=True)
    except TimeoutError: print(f"[{tag}] TIMEOUT", flush=True)
    except Exception as e: print(f"[{tag}] ERROR {e!r}", flush=True)
    finally: signal.alarm(0)

# Ex1: spherical (2, pi/4, pi/3) -> rectangular  (Stewart order: rho, theta, phi)
def ex1():
    R, T, P = 2, pi/4, pi/3
    X = simplify(R*sin(P)*cos(T)); Y = simplify(R*sin(P)*sin(T)); Z = simplify(R*cos(P))
    return (f"(x,y,z) = ({X}, {Y}, {Z}) = ({N(X,8)}, {N(Y,8)}, {N(Z,8)}); "
            f"sqrt(3/2) = {N(sqrt(Rational(3,2)),8)}  (textbook (sqrt(3/2), sqrt(3/2), 1))")
run("Ex1", ex1)

# Ex2: rectangular (0, 2*sqrt(3), -2) -> spherical
def ex2():
    X, Y, Z = 0, 2*sqrt(3), -2
    R = sqrt(X**2+Y**2+Z**2)
    P = acos(Z/R)
    T = atan2(Y, X)
    return (f"rho = {simplify(R)}; phi = acos({simplify(Z/R)}) = {simplify(P)} (=2pi/3); "
            f"theta = {simplify(T)} (=pi/2)  (textbook (4, pi/2, 2pi/3))")
run("Ex2", ex2)

# Ex3: exp((x^2+y^2+z^2)^{3/2}) over the unit ball
def ex3():
    v = integrate(integrate(integrate(exp(rho**3)*rho**2*sin(ph), (rho,0,1)), (th,0,2*pi)), (ph,0,pi))
    book = Rational(4,3)*pi*(E-1)
    return (f"{simplify(v)} = {N(simplify(v),10)}; book 4pi(e-1)/3 = {N(book,10)}; "
            f"equal? {simplify(v-book)==0}")
run("Ex3", ex3)

# Ex4: volume above the cone z = sqrt(x^2+y^2) and below the sphere x^2+y^2+z^2 = z
def ex4():
    v = integrate(integrate(integrate(rho**2*sin(ph), (rho,0,cos(ph))), (ph,0,pi/4)), (th,0,2*pi))
    return f"{simplify(v)} = {N(simplify(v),10)}  (textbook pi/8 = {N(pi/8,10)})"
run("Ex4", ex4)

# Ex4 cross-check: cylindrical coordinates.  Sphere x^2+y^2+(z-1/2)^2 = 1/4, cone z = r.
# The cone meets the sphere where r = z and r^2+z^2 = z  ->  z = 1/2, r = 1/2.
def ex4b():
    r = symbols('r', nonnegative=True)
    top = Rational(1,2) + sqrt(Rational(1,4) - r**2)     # upper half of the sphere
    v = integrate(integrate((top - r)*r, (r,0,Rational(1,2))), (th,0,2*pi))
    return f"cylindrical: {simplify(v)} = {N(simplify(v),10)}"
run("Ex4-check", ex4b)
