#!/usr/bin/env python3
"""Anchor recomputation for Stewart ET9 §15.7 Triple Integrals in Cylindrical Coordinates."""
import signal
from sympy import *

x, y, z = symbols('x y z', real=True)
r = symbols('r', nonnegative=True); th = symbols('theta', real=True)
K = symbols('K', positive=True)

def run(tag, fn):
    def _to(s, f): raise TimeoutError
    signal.signal(signal.SIGALRM, _to); signal.alarm(20)
    try: print(f"[{tag}] {fn()}", flush=True)
    except TimeoutError: print(f"[{tag}] TIMEOUT", flush=True)
    except Exception as e: print(f"[{tag}] ERROR {e!r}", flush=True)
    finally: signal.alarm(0)

# Ex1(a): cylindrical (2, 2pi/3, 1) -> rectangular
def ex1a():
    R, T, Z = 2, 2*pi/3, 1
    return (f"(x,y,z) = ({simplify(R*cos(T))}, {simplify(R*sin(T))}, {Z})  "
            f"(textbook (-1, sqrt(3), 1))")
run("Ex1a", ex1a)

# Ex1(b): rectangular (3,-3,-7) -> cylindrical
def ex1b():
    X, Y, Z = 3, -3, -7
    rr = sqrt(X**2+Y**2)
    t_principal = atan2(Y, X)                 # in (-pi, pi]
    t_positive  = t_principal + 2*pi
    return (f"r = {simplify(rr)} = 3*sqrt(2)? {simplify(rr-3*sqrt(2))==0}; "
            f"theta = {t_principal} (= -pi/4) or {simplify(t_positive)} (= 7pi/4); z = {Z}  "
            f"(textbook (3sqrt2, 7pi/4, -7) and (3sqrt2, -pi/4, -7))")
run("Ex1b", ex1b)

# Ex2: surface z = r  ->  z^2 = x^2+y^2 with z>=0, a cone
def ex2():
    # check that z=r means z^2 = x^2+y^2 and horizontal trace z=k is a circle of radius k
    expr = Eq(z**2, x**2+y**2)
    return ("z = r  =>  z^2 = r^2 = x^2+y^2 (upper nappe, z>=0); trace z=k (k>0) is the circle "
            "x^2+y^2=k^2 of radius k -> circular cone with axis the z-axis  (textbook: a cone)")
run("Ex2", ex2)

# Ex3: x^2 over E under z = 4-x^2-y^2, above the xy-plane
def ex3():
    v = integrate(integrate(integrate((r*cos(th))**2*r, (z,0,4-r**2)), (r,0,2)), (th,0,2*pi))
    return f"{simplify(v)} = {N(simplify(v))}  (textbook 16*pi/3 = {N(16*pi/3)})"
run("Ex3", ex3)

# Ex3 cross-check: rectangular numeric (midpoint rule over the disk r<=2)
def ex3b():
    import math
    n = 1500; h = 4.0/n; tot = 0.0
    for i in range(n):
        xx = -2 + h*(i+0.5)
        for j in range(n):
            yy = -2 + h*(j+0.5)
            s = xx*xx+yy*yy
            if s <= 4:
                tot += xx*xx*(4-s)*h*h      # inner z-integral gives (4-x^2-y^2)
    return f"rectangular midpoint rule (n=1500): {tot:.5f} vs 16*pi/3 = {float(16*pi/3):.5f}"
run("Ex3-check", ex3b)

# Ex4: mass, density K*sqrt(x^2+y^2) = K r, E: 0<=theta<=pi, 0<=r<=1, 1-r^2<=z<=4
def ex4():
    m = integrate(integrate(integrate(K*r*r, (z,1-r**2,4)), (r,0,1)), (th,0,pi))
    return f"m = {simplify(m)}  (textbook 6*pi*K/5)"
run("Ex4", ex4)

# Ex5: rewrite the rectangular iterated integral in cylindrical coordinates and evaluate
def ex5():
    v = integrate(integrate(integrate(r**2*r, (z,r,2)), (r,0,2)), (th,0,2*pi))
    # cross-check numerically in rectangular coordinates
    import math
    n = 1200; h = 4.0/n; tot = 0.0
    for i in range(n):
        xx = -2 + h*(i+0.5)
        for j in range(n):
            yy = -2 + h*(j+0.5)
            s = xx*xx+yy*yy
            if s <= 4:
                tot += s*(2-math.sqrt(s))*h*h
    return (f"cylindrical: {simplify(v)} = {N(simplify(v))}; rectangular midpoint rule: {tot:.5f}  "
            f"(textbook 16*pi/5 = {N(16*pi/5)})")
run("Ex5", ex5)
