#!/usr/bin/env python3
"""Anchor recomputation for Stewart ET9 §15.3 Double Integrals in Polar Coordinates."""
import signal
from sympy import *

x, y = symbols('x y', real=True)
r = symbols('r', nonnegative=True)
th = symbols('theta', real=True)

def run(tag, fn):
    def _to(s, f): raise TimeoutError
    signal.signal(signal.SIGALRM, _to); signal.alarm(20)
    try: print(f"[{tag}] {fn()}", flush=True)
    except TimeoutError: print(f"[{tag}] TIMEOUT", flush=True)
    except Exception as e: print(f"[{tag}] ERROR {e!r}", flush=True)
    finally: signal.alarm(0)

# Ex1: (3x+4y^2) over upper half ring 1<=r<=2, 0<=th<=pi
def ex1():
    f = 3*(r*cos(th)) + 4*(r*sin(th))**2
    v = integrate(integrate(f*r, (r,1,2)), (th,0,pi))
    return f"polar: {simplify(v)} = {N(simplify(v))}  (textbook 15*pi/2 = {N(15*pi/2)})"
run("Ex1", ex1)

# Ex1 cross-check: rectangular, upper half ring split into three x-slabs
def ex1b():
    A = integrate(integrate(3*x+4*y**2, (y,0,sqrt(4-x**2))), (x,-2,-1))
    B = integrate(integrate(3*x+4*y**2, (y,sqrt(1-x**2),sqrt(4-x**2))), (x,-1,1))
    C = integrate(integrate(3*x+4*y**2, (y,0,sqrt(4-x**2))), (x,1,2))
    v = simplify(A+B+C)
    return f"rectangular (3 slabs): {v} = {N(v)}"
run("Ex1-check", ex1b)

# Ex2: (x^2+y^2) over upper half disk radius 1
def ex2():
    v = integrate(integrate(r**2*r, (r,0,1)), (th,0,pi))
    w = integrate(integrate(x**2+y**2, (y,0,sqrt(1-x**2))), (x,-1,1))
    return f"polar: {v}; rectangular: {simplify(w)}  (textbook pi/4)"
run("Ex2", ex2)

# Ex3: volume under 1-x^2-y^2 over unit disk
def ex3():
    v = integrate(integrate((1-r**2)*r, (r,0,1)), (th,0,2*pi))
    w = integrate(integrate(1-x**2-y**2, (y,-sqrt(1-x**2),sqrt(1-x**2))), (x,-1,1))
    return f"polar: {v}; rectangular: {simplify(w)}  (textbook pi/2)"
run("Ex3", ex3)

# Ex4: area of one loop of the four-leaved rose r = cos 2*theta
def ex4():
    v = integrate(integrate(r, (r,0,cos(2*th))), (th,-pi/4,pi/4))
    w = integrate(Rational(1,2)*cos(2*th)**2, (th,-pi/4,pi/4))   # formula 10.4.3
    return f"double integral: {simplify(v)}; 1/2 * int h^2 dtheta: {simplify(w)}  (textbook pi/8)"
run("Ex4", ex4)

# Ex5: volume under z=x^2+y^2 inside cylinder x^2+y^2=2x  (polar)
def ex5():
    v = simplify(integrate(integrate(r**2*r, (r,0,2*cos(th))), (th,-pi/2,pi/2)))
    return f"polar: {v} = {N(v)}  (textbook 3*pi/2 = {N(3*pi/2)})"
run("Ex5", ex5)

# Ex5 cross-check: numeric midpoint rule in rectangular coordinates over (x-1)^2+y^2<=1
def ex5b():
    import math
    n = 2000
    h = 2.0/n
    tot = 0.0
    for i in range(n):
        xx = h*(i+0.5)
        d = 1-(xx-1)**2
        if d <= 0: continue
        yb = math.sqrt(d)
        # exact inner integral in y: int (x^2+y^2) dy from -yb to yb = 2*x^2*yb + 2*yb^3/3
        tot += (2*xx*xx*yb + 2*yb**3/3)*h
    return f"rectangular (numeric, exact inner y-integral, n=2000): {tot:.6f}  vs 3*pi/2 = {float(3*pi/2):.6f}"
run("Ex5-check", ex5b)
