#!/usr/bin/env python3
"""Anchor recomputation for Stewart ET9 §15.6 Triple Integrals."""
import signal
from sympy import *

x, y, z = symbols('x y z', real=True)
r = symbols('r', nonnegative=True); th = symbols('theta', real=True)
rho = symbols('rho', positive=True)

def run(tag, fn):
    def _to(s, f): raise TimeoutError
    signal.signal(signal.SIGALRM, _to); signal.alarm(20)
    try: print(f"[{tag}] {fn()}", flush=True)
    except TimeoutError: print(f"[{tag}] TIMEOUT", flush=True)
    except Exception as e: print(f"[{tag}] ERROR {e!r}", flush=True)
    finally: signal.alarm(0)

# Ex1: x*y*z^2 over B = [0,1]x[-1,2]x[0,3], two different orders
def ex1():
    a = integrate(integrate(integrate(x*y*z**2,(x,0,1)),(y,-1,2)),(z,0,3))
    b = integrate(integrate(integrate(x*y*z**2,(y,-1,2)),(z,0,3)),(x,0,1))
    return f"order dx dy dz: {a}; order dy dz dx: {b}  (textbook 27/4)"
run("Ex1", ex1)

# Ex2: z over E = {0<=x<=1, 0<=y<=x, 0<=z<=12xy}
def ex2():
    v = integrate(integrate(integrate(z,(z,0,12*x*y)),(y,0,x)),(x,0,1))
    return f"{v}  (textbook 4)"
run("Ex2", ex2)

# Ex3: sqrt(x^2+z^2) over region bounded by y = x^2+z^2 and y = 4  (type 3 + polar in xz-plane)
def ex3():
    v = integrate(integrate((4-r**2)*r*r, (r,0,2)), (th,0,2*pi))
    return f"polar in xz-plane: {simplify(v)} = {N(simplify(v))}  (textbook 128*pi/15 = {N(128*pi/15)})"
run("Ex3", ex3)

# Ex3 cross-check: type-1 iterated integral (numeric)
def ex3b():
    import math
    # integral over disk x^2+z^2<=4 of (4-x^2-z^2)*sqrt(x^2+z^2), midpoint rule in Cartesian
    n = 1200; h = 4.0/n; tot = 0.0
    for i in range(n):
        xx = -2 + h*(i+0.5)
        for j in range(n):
            zz = -2 + h*(j+0.5)
            s = xx*xx+zz*zz
            if s <= 4:
                tot += (4-s)*math.sqrt(s)*h*h
    return f"Cartesian midpoint rule over the disk (n=1200): {tot:.5f} vs 128*pi/15 = {float(128*pi/15):.5f}"
run("Ex3-check", ex3b)

# Ex4: the three equivalent orders on E = {0<=x<=1, 0<=y<=x^2, 0<=z<=y}
#      verified with several test integrands f
def ex4():
    tests = [Integer(1), x, y, z, x*y*z, exp(x)+y**2]
    out = []
    for f in tests:
        A = integrate(integrate(integrate(f,(z,0,y)),(y,0,x**2)),(x,0,1))          # given order
        B = integrate(integrate(integrate(f,(x,sqrt(y),1)),(z,0,y)),(y,0,1))       # (a) dx dz dy
        C = integrate(integrate(integrate(f,(y,z,x**2)),(x,sqrt(z),1)),(z,0,1))    # (b) dy dx dz
        out.append(f"f={f}: {simplify(A)} / {simplify(B)} / {simplify(C)} "
                   f"{'OK' if simplify(A-B)==0 and simplify(A-C)==0 else 'MISMATCH'}")
    return "given / (a) dx dz dy / (b) dy dx dz -> " + "; ".join(out)
run("Ex4", ex4)

# Ex5: volume of the tetrahedron x+2y+z=2, x=2y, x=0, z=0
def ex5():
    v = integrate(integrate(integrate(1,(z,0,2-x-2*y)),(y,x/2,1-x/2)),(x,0,1))
    return f"{v}  (textbook 1/3, same as Example 15.2.4)"
run("Ex5", ex5)

# Ex6: center of mass, constant density, E bounded by x=y^2, x=z, z=0, x=1
def ex6():
    lim = lambda f: integrate(integrate(integrate(f,(z,0,x)),(x,y**2,1)),(y,-1,1))
    m   = rho*lim(1)
    Myz = rho*lim(x); Mxz = rho*lim(y); Mxy = rho*lim(z)
    return (f"m = {m}; Myz = {Myz}; Mxz = {Mxz}; Mxy = {Mxy}; "
            f"center = ({simplify(Myz/m)}, {simplify(Mxz/m)}, {simplify(Mxy/m)})  "
            f"(textbook m=4rho/5, Myz=4rho/7, Mxz=0, Mxy=2rho/7, (5/7, 0, 5/14))")
run("Ex6", ex6)
