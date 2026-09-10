#!/usr/bin/env python3
"""Anchor recomputation for Stewart ET9 §15.1 Double Integrals over Rectangles.
Each example is recomputed independently (sympy) with a 20 s alarm timeout."""
import signal, sys
from sympy import *

x, y, z = symbols('x y z', real=True)

def run(tag, fn):
    def _to(sig, frm): raise TimeoutError
    signal.signal(signal.SIGALRM, _to); signal.alarm(20)
    try:
        print(f"[{tag}] {fn()}", flush=True)
    except TimeoutError:
        print(f"[{tag}] TIMEOUT", flush=True)
    except Exception as e:
        print(f"[{tag}] ERROR {e!r}", flush=True)
    finally:
        signal.alarm(0)

# Ex 1: Riemann sum, upper-right corners, m=n=2, R=[0,2]^2, f=16-x^2-2y^2
def ex1():
    f = lambda a, b: 16 - a**2 - 2*b**2
    dA = Rational(1)
    s = sum(f(i, j) for i in (1, 2) for j in (1, 2)) * dA
    return f"V ~ {s}  (textbook 34)"
run("Ex1", ex1)

# Ex 2: integral of sqrt(1-x^2) over [-1,1]x[-2,2]
def ex2():
    v = integrate(integrate(sqrt(1 - x**2), (x, -1, 1)), (y, -2, 2))
    return f"{simplify(v)} = {N(v)}  (textbook 2*pi = {N(2*pi)})"
run("Ex2", ex2)

# Ex 3: Midpoint Rule m=n=2 for (x-3y^2) on [0,2]x[1,2]
def ex3():
    f = lambda a, b: a - 3*b**2
    xs = [Rational(1,2), Rational(3,2)]; ys = [Rational(5,4), Rational(7,4)]
    dA = Rational(1,2)
    s = sum(f(a,b) for a in xs for b in ys)*dA
    return f"{s} = {N(s)}  (textbook -95/8 = -11.875)"
run("Ex3", ex3)

# Ex 4: iterated integrals both orders of x^2*y
def ex4():
    a = integrate(integrate(x**2*y, (y,1,2)), (x,0,3))
    b = integrate(integrate(x**2*y, (x,0,3)), (y,1,2))
    return f"(a) {a}  (b) {b}   (textbook 27/2 both)"
run("Ex4", ex4)

# Ex 5: exact double integral of (x-3y^2) on [0,2]x[1,2], both orders
def ex5():
    a = integrate(integrate(x-3*y**2, (y,1,2)), (x,0,2))
    b = integrate(integrate(x-3*y**2, (x,0,2)), (y,1,2))
    return f"order dy dx: {a}; order dx dy: {b}  (textbook -12)"
run("Ex5", ex5)

# Ex 6: y*sin(x*y) on [1,2]x[0,pi], both orders
def ex6():
    a = integrate(integrate(y*sin(x*y), (x,1,2)), (y,0,pi))
    b = integrate(integrate(y*sin(x*y), (y,0,pi)), (x,1,2))
    return f"dx dy: {simplify(a)}; dy dx: {simplify(b)} = {N(simplify(b))}  (textbook 0)"
run("Ex6", ex6)

# Ex 7: volume under 16-x^2-2y^2 over [0,2]^2
def ex7():
    v = integrate(integrate(16-x**2-2*y**2, (x,0,2)), (y,0,2))
    return f"{v}  (textbook 48)"
run("Ex7", ex7)

# Ex 8: sin x cos y over [0,pi/2]^2 via product rule
def ex8():
    v = integrate(integrate(sin(x)*cos(y), (x,0,pi/2)), (y,0,pi/2))
    p = integrate(sin(x),(x,0,pi/2))*integrate(cos(y),(y,0,pi/2))
    return f"double {v}; product form {p}  (textbook 1)"
run("Ex8", ex8)

# Ex 9: Colorado average snowfall, Midpoint Rule m=n=4
def ex9():
    vals = [0,15,8,7,2,25,18.5,11,4.5,28,17,13.5,12,15,17.5,13]
    A = 388*276
    dA = Rational(388*276,16)
    tot = sum(Rational(str(v)) for v in vals)
    integral = dA*tot
    favg = integral/A
    return (f"sum of 16 samples = {tot}; dA = {dA} mi^2; integral ~ {integral} = {N(integral)}; "
            f"favg = {favg} = {N(favg,6)} in  (textbook ~12.9, i.e. ~13 in)")
run("Ex9", ex9)
