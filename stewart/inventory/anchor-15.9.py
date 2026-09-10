#!/usr/bin/env python3
"""Anchor recomputation for Stewart ET9 §15.9 Change of Variables in Multiple Integrals."""
import signal
from sympy import *

x, y, z = symbols('x y z', real=True)
u, v, w = symbols('u v w', real=True)
rho = symbols('rho', nonnegative=True)
th = symbols('theta', real=True); ph = symbols('phi', real=True)
r = symbols('r', nonnegative=True)

def run(tag, fn):
    def _to(s, f): raise TimeoutError
    signal.signal(signal.SIGALRM, _to); signal.alarm(20)
    try: print(f"[{tag}] {fn()}", flush=True)
    except TimeoutError: print(f"[{tag}] TIMEOUT", flush=True)
    except Exception as e: print(f"[{tag}] ERROR {e!r}", flush=True)
    finally: signal.alarm(0)

def jac2(X, Y, a, b):
    return simplify(Matrix([[diff(X,a), diff(X,b)],[diff(Y,a), diff(Y,b)]]).det())

# Ex1: image of the unit square under x = u^2 - v^2, y = 2uv
def ex1():
    X, Y = u**2 - v**2, 2*u*v
    out = []
    # S1: v = 0, 0<=u<=1
    out.append(f"S1(v=0): (x,y)=({X.subs(v,0)}, {Y.subs(v,0)}) -> segment 0<=x<=1, y=0")
    # S2: u = 1  ->  x = 1-v^2, y = 2v  =>  x = 1 - y^2/4
    xs, ys = X.subs(u,1), Y.subs(u,1)
    elim = simplify(xs - (1 - ys**2/4))
    out.append(f"S2(u=1): x=1-y^2/4? residual {elim} (0<=x<=1)")
    # S3: v = 1  ->  x = u^2-1, y = 2u  =>  x = y^2/4 - 1
    xs, ys = X.subs(v,1), Y.subs(v,1)
    elim = simplify(xs - (ys**2/4 - 1))
    out.append(f"S3(v=1): x=y^2/4-1? residual {elim} (-1<=x<=0)")
    # S4: u = 0  ->  x = -v^2, y = 0
    out.append(f"S4(u=0): (x,y)=({X.subs(u,0)}, {Y.subs(u,0)}) -> segment -1<=x<=0, y=0")
    return " | ".join(out) + "  (textbook: region bounded by the x-axis and x=1-y^2/4, x=y^2/4-1)"
run("Ex1", ex1)

# Ex2: int_R y dA under x = u^2-v^2, y = 2uv over S = [0,1]^2
def ex2():
    X, Y = u**2 - v**2, 2*u*v
    J = jac2(X, Y, u, v)
    val = integrate(integrate(Y*Abs(J), (u,0,1)), (v,0,1))
    # direct check in the xy-plane: 0<=y<=2, y^2/4-1 <= x <= 1-y^2/4
    direct = integrate(integrate(y, (x, y**2/4-1, 1-y**2/4)), (y,0,2))
    return f"Jacobian = {J} (=4u^2+4v^2); transformed integral = {val}; direct xy integral = {direct}  (textbook 2)"
run("Ex2", ex2)

# Ex3: int_R exp((x+y)/(x-y)) dA over the trapezoid (1,0),(2,0),(0,-2),(0,-1)
def ex3():
    X, Y = (u+v)/2, (u-v)/2
    J = jac2(X, Y, u, v)
    val = simplify(integrate(integrate(exp(u/v)*Abs(J), (u,-v,v)), (v,1,2)))
    book = Rational(3,4)*(E - 1/E)
    return (f"x=(u+v)/2, y=(u-v)/2; Jacobian = {J} (=-1/2); S = {{1<=v<=2, -v<=u<=v}}; "
            f"value = {val} = {N(val,10)}; book 3(e-1/e)/4 = {N(book,10)}; equal? {simplify(expand(val.rewrite(exp) - book))==0}")
run("Ex3", ex3)

# Ex3 cross-check: numeric integration in the xy-plane over the trapezoid
def ex3b():
    import math
    # region: 0<=x, y<=0, 1 <= x-y <= 2  ->  for each x in [0,2], y from max(-2+x... ) ; use x-y=s in [1,2]
    # parametrize by x in [0,2], y in [x-2, x-1] intersected with x>=0, y<=0
    n = 3000; tot = 0.0; hx = 2.0/n
    for i in range(n):
        xx = hx*(i+0.5)
        ylo, yhi = xx-2, xx-1
        ylo = max(ylo, -2.0); yhi = min(yhi, 0.0)
        if yhi <= ylo: continue
        m = 400; hy = (yhi-ylo)/m
        s = 0.0
        for j in range(m):
            yy = ylo + hy*(j+0.5)
            s += math.exp((xx+yy)/(xx-yy))*hy
        tot += s*hx
    return f"numeric xy integral over the trapezoid: {tot:.6f} vs 3(e-1/e)/4 = {float(Rational(3,4)*(E-1/E)):.6f}"
run("Ex3-check", ex3b)

# Ex4: 3x3 Jacobian of the spherical transformation
def ex4():
    X = rho*sin(ph)*cos(th); Y = rho*sin(ph)*sin(th); Z = rho*cos(ph)
    J = simplify(Matrix([[diff(X,rho), diff(X,th), diff(X,ph)],
                         [diff(Y,rho), diff(Y,th), diff(Y,ph)],
                         [diff(Z,rho), diff(Z,th), diff(Z,ph)]]).det())
    return (f"d(x,y,z)/d(rho,theta,phi) = {J} (= -rho^2 sin phi); "
            f"|J| = rho^2 sin phi for 0<=phi<=pi (sin phi >= 0) -> recovers Formula 15.8.3  "
            f"(textbook -rho^2 sin phi)")
run("Ex4", ex4)

# Bonus: polar transformation is the special case J = r  (text, p.1188)
def polar():
    J = jac2(r*cos(th), r*sin(th), r, th)
    return f"d(x,y)/d(r,theta) = {J} (= r > 0) -> recovers Formula 15.3.2"
run("Polar", polar)
