#!/usr/bin/env python3
"""Anchor recomputation for Stewart ET9 §15.5 Surface Area."""
import signal
from sympy import *

x, y = symbols('x y', real=True)
r = symbols('r', nonnegative=True); th = symbols('theta', real=True)

def run(tag, fn):
    def _to(s, f): raise TimeoutError
    signal.signal(signal.SIGALRM, _to); signal.alarm(20)
    try: print(f"[{tag}] {fn()}", flush=True)
    except TimeoutError: print(f"[{tag}] TIMEOUT", flush=True)
    except Exception as e: print(f"[{tag}] ERROR {e!r}", flush=True)
    finally: signal.alarm(0)

# Ex1: z = x^2 + 2y + 2 over triangle (0,0),(1,0),(1,1):  0<=x<=1, 0<=y<=x
def ex1():
    f = x**2 + 2*y + 2
    integrand = sqrt(diff(f,x)**2 + diff(f,y)**2 + 1)
    A = simplify(integrate(integrate(integrand, (y,0,x)), (x,0,1)))
    book = Rational(1,12)*(27 - 5*sqrt(5))
    return (f"integrand = sqrt({simplify(diff(f,x)**2+diff(f,y)**2+1)}); A = {A} = {N(A,10)}; "
            f"book (27-5*sqrt5)/12 = {N(book,10)}; equal? {simplify(A-book)==0}")
run("Ex1", ex1)

# Ex2: z = x^2 + y^2 under z = 9  ->  disk of radius 3
def ex2():
    f = x**2 + y**2
    integrand = sqrt(diff(f,x)**2 + diff(f,y)**2 + 1)   # sqrt(1+4(x^2+y^2))
    A = simplify(integrate(integrate(sqrt(1+4*r**2)*r, (r,0,3)), (th,0,2*pi)))
    book = pi/6*(37*sqrt(37) - 1)
    return (f"integrand = {simplify(integrand)}; A(polar) = {A} = {N(A,10)}; "
            f"book pi/6*(37*sqrt37 - 1) = {N(book,10)}; equal? {simplify(A-book)==0}")
run("Ex2", ex2)
