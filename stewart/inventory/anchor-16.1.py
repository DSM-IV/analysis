#!/usr/bin/env python3
"""§16.1 Vector Fields — 예제 기준값 독립 재계산 (sympy)."""
import signal, sys
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

x, y, z = symbols('x y z', real=True)
m, M, G, q, Q, eps = symbols('m M G q Q varepsilon', positive=True)

# --- Example 1: F = -y i + x j -------------------------------------------
def ex1():
    F = Matrix([-y, x]); X = Matrix([x, y])
    dot = simplify((X.T * F)[0])
    magdiff = simplify(F.dot(F) - X.dot(X))
    tbl = {(1,0):(0,1), (2,2):(-2,2), (3,0):(0,3), (0,1):(-1,0), (-2,2):(-2,-2),
           (0,3):(-3,0), (-1,0):(0,-1), (-2,-2):(2,-2), (-3,0):(0,-3),
           (0,-1):(1,0), (2,-2):(2,2), (0,-3):(3,0)}
    ok = all(tuple(F.subs({x:a, y:b})) == v for (a,b), v in tbl.items())
    return f"x.F = {dot} (expect 0); |F|^2-|x|^2 = {magdiff} (expect 0); table(12 pts) matches = {ok}"
run("Ex1", ex1)

# --- Example 4: gravitational field --------------------------------------
def ex4():
    X = Matrix([x, y, z]); r = sqrt(x**2 + y**2 + z**2)
    Fvec = -m*M*G/r**3 * X                       # formula (3)
    comp = Matrix([-m*M*G*x/(x**2+y**2+z**2)**Rational(3,2),
                   -m*M*G*y/(x**2+y**2+z**2)**Rational(3,2),
                   -m*M*G*z/(x**2+y**2+z**2)**Rational(3,2)])
    same = simplify(Fvec - comp) == zeros(3,1)
    mag = simplify(sqrt(Fvec.dot(Fvec)))         # expect mMG/r^2
    magok = simplify(mag - m*M*G/r**2) == 0
    # potential f = mMG/r  ->  grad f = F ?
    f = m*M*G/r
    grad = Matrix([diff(f, v) for v in (x, y, z)])
    consok = simplify(grad - Fvec) == zeros(3,1)
    return f"component form == (3): {same}; |F| = mMG/r^2: {magok}; grad(mMG/r) == F: {consok}"
run("Ex4", ex4)

# --- Example 5: Coulomb field / electric field ---------------------------
def ex5():
    X = Matrix([x, y, z]); r = sqrt(x**2 + y**2 + z**2)
    Fvec = eps*q*Q/r**3 * X                      # formula (4)
    mag = simplify(sqrt(Fvec.dot(Fvec)))
    magok = simplify(mag - eps*q*Q/r**2) == 0
    E = simplify(Fvec/q)
    Eok = simplify(E - eps*Q/r**3 * X) == zeros(3,1)
    return f"|F| = eps*q*Q/r^2: {magok}; E = F/q = eps*Q*x/|x|^3: {Eok}"
run("Ex5", ex5)

# --- Example 6: gradient field of f = x^2 y - y^3 ------------------------
def ex6():
    f = x**2*y - y**3
    grad = (simplify(diff(f, x)), simplify(diff(f, y)))
    ok = grad == (2*x*y, x**2 - 3*y**2)
    return f"grad f = {grad}; matches 2xy i + (x^2-3y^2) j: {ok}"
run("Ex6", ex6)
