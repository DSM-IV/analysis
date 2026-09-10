#!/usr/bin/env python3
"""Anchor recomputation for Stewart ET9 §15.4 Applications of Double Integrals."""
import signal
from sympy import *

x, y, t = symbols('x y t', real=True)
r = symbols('r', nonnegative=True)
th = symbols('theta', real=True)
a, K, rho = symbols('a K rho', positive=True)

def run(tag, fn):
    def _to(s, f): raise TimeoutError
    signal.signal(signal.SIGALRM, _to); signal.alarm(20)
    try: print(f"[{tag}] {fn()}", flush=True)
    except TimeoutError: print(f"[{tag}] TIMEOUT", flush=True)
    except Exception as e: print(f"[{tag}] ERROR {e!r}", flush=True)
    finally: signal.alarm(0)

# Ex1: total charge, sigma = x*y on triangle bounded by y=1-x, y=1, 0<=x<=1
run("Ex1", lambda: f"Q = {integrate(integrate(x*y,(y,1-x,1)),(x,0,1))} C  (textbook 5/24)")

# Ex2: triangular lamina (0,0),(1,0),(0,2), rho = 1+3x+y
def ex2():
    d = 1+3*x+y
    m  = integrate(integrate(d,      (y,0,2-2*x)), (x,0,1))
    My = integrate(integrate(x*d,    (y,0,2-2*x)), (x,0,1))
    Mx = integrate(integrate(y*d,    (y,0,2-2*x)), (x,0,1))
    return f"m = {m}; My = {My}; Mx = {Mx}; center = ({My/m}, {Mx/m})  (textbook m=8/3, (3/8, 11/16))"
run("Ex2", ex2)

# Ex3: upper half disk radius a, rho = K*sqrt(x^2+y^2) = K*r
def ex3():
    dens = K*r
    m  = integrate(integrate(dens*r, (r,0,a)), (th,0,pi))
    Mx = integrate(integrate(r*sin(th)*dens*r, (r,0,a)), (th,0,pi))
    My = integrate(integrate(r*cos(th)*dens*r, (r,0,a)), (th,0,pi))
    return (f"m = {simplify(m)}; Mx = {simplify(Mx)}; My = {simplify(My)}; "
            f"center = ({simplify(My/m)}, {simplify(Mx/m)})  (textbook m=K*pi*a^3/3, (0, 3a/(2pi)))")
run("Ex3", ex3)

# Ex4: homogeneous disk radius a, density rho -> Ix, Iy, I0
def ex4():
    Ix = rho*integrate(integrate((r*sin(th))**2*r, (r,0,a)), (th,0,2*pi))
    Iy = rho*integrate(integrate((r*cos(th))**2*r, (r,0,a)), (th,0,2*pi))
    I0 = rho*integrate(integrate(r**2*r, (r,0,a)), (th,0,2*pi))
    m  = rho*pi*a**2
    return (f"Ix = {simplify(Ix)}; Iy = {simplify(Iy)}; I0(direct) = {simplify(I0)}; "
            f"Ix+Iy = {simplify(Ix+Iy)}; I0/m = {simplify(I0/m)} = a^2/2 so I0 = m a^2/2  "
            f"(textbook rho*pi*a^4/4, same, rho*pi*a^4/2)")
run("Ex4", ex4)

# Ex5: radius of gyration about the x-axis of that disk
def ex5():
    Ix = rho*pi*a**4/4; m = rho*pi*a**2
    ybar2 = simplify(Ix/m)
    return f"ybar^2 = {ybar2}; ybar = {sqrt(ybar2)}  (textbook a/2)"
run("Ex5", ex5)

# Ex6: joint density C(x+2y) on [0,10]^2
def ex6():
    C = symbols('C', positive=True)
    tot = integrate(integrate(C*(x+2*y), (y,0,10)), (x,0,10))
    Cval = solve(Eq(tot,1), C)[0]
    P = integrate(integrate(Cval*(x+2*y), (y,2,10)), (x,0,7))
    return f"total = {tot} -> C = {Cval}; P(X<=7, Y>=2) = {P} = {N(P,6)}  (textbook 1/1500, 868/1500 ~ 0.5787)"
run("Ex6", ex6)

# Ex7: independent exponential waiting times, means 10 and 5; P(X+Y<20)
def ex7():
    f = Rational(1,50)*exp(-x/10)*exp(-y/5)
    P = simplify(integrate(integrate(f, (y,0,20-x)), (x,0,20)))
    closed = 1 + exp(-4) - 2*exp(-2)
    return (f"P(X+Y<20) = {P} = {N(P,6)}; textbook closed form 1+e^-4-2e^-2 = {N(closed,6)}; "
            f"equal? {simplify(P-closed)==0}")
run("Ex7", ex7)

# Ex8: bivariate normal, sigma=0.01, window = mean +/- 0.02 = +/- 2 sigma
def ex8():
    from sympy import erf
    # P(|X-mu|<2 sigma) for one variable
    p1 = erf(2/sqrt(2))
    both = p1**2
    return (f"P(|X-4|<0.02) = P(|Z|<2) = erf(sqrt(2)) = {N(p1,6)}; "
            f"joint (independent) = {N(both,6)} ~ 0.91; "
            f"P(either differs by more than 0.02) = {N(1-both,6)}  (textbook ~0.91 and 0.09)")
run("Ex8", ex8)
