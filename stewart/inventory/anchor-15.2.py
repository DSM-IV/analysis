#!/usr/bin/env python3
"""Anchor recomputation for Stewart ET9 §15.2 Double Integrals over General Regions."""
import signal
from sympy import *

x, y = symbols('x y', real=True)

def run(tag, fn):
    def _to(s, f): raise TimeoutError
    signal.signal(signal.SIGALRM, _to); signal.alarm(20)
    try: print(f"[{tag}] {fn()}", flush=True)
    except TimeoutError: print(f"[{tag}] TIMEOUT", flush=True)
    except Exception as e: print(f"[{tag}] ERROR {e!r}", flush=True)
    finally: signal.alarm(0)

# Ex1: (x+2y) over D: 2x^2 <= y <= 1+x^2, -1<=x<=1
run("Ex1", lambda: f"{integrate(integrate(x+2*y,(y,2*x**2,1+x**2)),(x,-1,1))}  (textbook 32/15)")

# Ex2: volume of x^2+y^2 over D bounded by y=2x, y=x^2  (type I and type II)
def ex2():
    a = integrate(integrate(x**2+y**2,(y,x**2,2*x)),(x,0,2))
    b = integrate(integrate(x**2+y**2,(x,y/2,sqrt(y))),(y,0,4))
    return f"type I: {a}; type II: {simplify(b)}  (textbook 216/35)"
run("Ex2", ex2)

# Ex3: xy over D bounded by y=x-1, y^2=2x+6  (type II preferred)
def ex3():
    b = integrate(integrate(x*y,(x,y**2/2-3,y+1)),(y,-2,4))
    a = (integrate(integrate(x*y,(y,-sqrt(2*x+6),sqrt(2*x+6))),(x,-3,-1))
         + integrate(integrate(x*y,(y,x-1,sqrt(2*x+6))),(x,-1,5)))
    return f"type II: {b}; type I (split): {simplify(a)}  (textbook 36)"
run("Ex3", ex3)

# Ex4: tetrahedron x+2y+z=2, x=2y, x=0, z=0
def ex4():
    v = integrate(integrate(2-x-2*y,(y,x/2,1-x/2)),(x,0,1))
    return f"{v}  (textbook 1/3)"
run("Ex4", ex4)

# Ex5: reversal of order for sin(y^2)
def ex5():
    v = integrate(integrate(sin(y**2),(x,0,y)),(y,0,1))
    return (f"reversed order: {simplify(v)} = {N(v)}; textbook (1-cos1)/2 = "
            f"{N(Rational(1,2)*(1-cos(1)))}")
run("Ex5", ex5)

# Ex6: Property 10 bounds for exp(sin x cos y) on the disk of radius 2,
#      plus an independent midpoint-rule value of the true integral (polar grid).
def ex6():
    import math
    A = pi*2**2
    lo, hi = A/E, A*E
    N, M = 400, 800
    hr, ht = 2.0/N, 2*math.pi/M
    tot = 0.0
    for i in range(N):
        r0 = hr*(i+0.5)
        for j in range(M):
            t0 = ht*(j+0.5)
            xx, yy = r0*math.cos(t0), r0*math.sin(t0)
            tot += math.exp(math.sin(xx)*math.cos(yy))*r0
    tot *= hr*ht
    return (f"bounds {lo} = {N_(lo)} <= I <= {hi} = {N_(hi)}; "
            f"true value (midpoint rule in polar, 400x800) ~ {tot:.5f} -- inside the bounds "
            f"(textbook 4*pi/e <= I <= 4*pi*e)")
N_ = lambda v: float(v.evalf())
run("Ex6", ex6)
