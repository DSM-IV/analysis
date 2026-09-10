#!/usr/bin/env python3
"""§16.5 Curl and Divergence — 예제 기준값 독립 재계산 (sympy)."""
import signal
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

x, y, z, t = symbols('x y z t', real=True)
V = (x, y, z)

def curl(F):
    P, Q, R = F
    return (simplify(diff(R, y) - diff(Q, z)),
            simplify(diff(P, z) - diff(R, x)),
            simplify(diff(Q, x) - diff(P, y)))

def div(F):
    return simplify(sum(diff(Fi, v) for Fi, v in zip(F, V)))

F_ex1 = (x*z, x*y*z, -y**2)

# Ex1 / Ex2: curl F for F = xz i + xyz j - y^2 k ; textbook -y(2+x) i + x j + yz k
def ex1():
    c = curl(F_ex1)
    txt = (-y*(2 + x), x, y*z)
    ok = all(simplify(a - b) == 0 for a, b in zip(c, txt))
    return f"curl F = {c}; 교재 (-y(2+x), x, yz); match={ok}; nonzero -> 비보존(예제 2)"
run("Ex1/Ex2", ex1)

# Ex3: F = y^2 z^3 i + 2xyz^3 j + 3xy^2z^2 k ; curl = 0, potential f = x y^2 z^3 + K
def ex3():
    F = (y**2*z**3, 2*x*y*z**3, 3*x*y**2*z**2)
    c = curl(F)
    f = x*y**2*z**3
    grad = tuple(simplify(diff(f, v)) for v in V)
    okc = all(ci == 0 for ci in c)
    okg = all(simplify(a - b) == 0 for a, b in zip(grad, F))
    return f"curl F = {c} (교재 0); match={okc} | grad(x y^2 z^3) = {grad} == F? {okg}"
run("Ex3", ex3)

# Ex4 / Ex5: div F for F = xz i + xyz j - y^2 k ; textbook z + xz
def ex4():
    d = div(F_ex1)
    ok = simplify(d - (z + x*z)) == 0
    dc = div(curl(F_ex1))
    return f"div F = {d}; 교재 z+xz; match={ok}; 0 이 아니므로 F != curl G (예제 5). 참고 div(curl F)={dc} (정리 11)"
run("Ex4/Ex5", ex4)

# Theorem 3 / 11 spot checks on a generic smooth f, F
def thms():
    f = Function('f')(x, y, z)
    P, Q, R = Function('P')(x, y, z), Function('Q')(x, y, z), Function('R')(x, y, z)
    gradf = tuple(diff(f, v) for v in V)
    c = tuple(simplify(ci) for ci in curl(gradf))
    d = simplify(div(curl((P, Q, R))))
    return f"curl(grad f) = {c} (정리 3: 0); div(curl F) = {d} (정리 11: 0)"
run("Thm3/Thm11", thms)

# Figure 2 and Figure 3 captions
def figs():
    F2a = (sin(y), cos(x), Integer(0)); F2b = (2*x*y, x**2 + y, Integer(0))
    F3a = (1 + x**2, y, Integer(0));    F3b = (-x, y, Integer(0))
    return (f"Fig2(a) curl={curl(F2a)} (교재 -(sin x + cos y) k, k성분 확인: "
            f"{simplify(curl(F2a)[2] + (sin(x)+cos(y)))==0}); Fig2(b) curl={curl(F2b)} (교재 0); "
            f"Fig3(a) div={div(F3a)} (교재 2x+1); Fig3(b) div={div(F3b)} (교재 0)")
run("Figs 2/3", figs)

# Vector form (13): outward unit normal n = (y' i - x' j)/|r'| is unit and perpendicular to T
def normal():
    xt, yt = Function('x')(t), Function('y')(t)
    speed = sqrt(diff(xt, t)**2 + diff(yt, t)**2)
    T = (diff(xt, t)/speed, diff(yt, t)/speed)
    n = (diff(yt, t)/speed, -diff(xt, t)/speed)
    dot = simplify(T[0]*n[0] + T[1]*n[1])
    norm = simplify(n[0]**2 + n[1]**2)
    # concrete check of orientation on the counterclockwise unit circle: n should point outward = (cos t, sin t)
    xc, yc = cos(t), sin(t)
    sc = sqrt(diff(xc, t)**2 + diff(yc, t)**2)
    nc = (simplify(diff(yc, t)/sc), simplify(-diff(xc, t)/sc))
    return f"T.n = {dot} (0이어야); |n|^2 = {norm} (1이어야); 반시계 단위원에서 n(t) = {nc} (외향 (cos t, sin t))"
run("Formula(13) n", normal)
