#!/usr/bin/env python3
"""Independent anchor values for stewart/exams 2022-final-b2 (Calculus II final, Fall 2022, block 2).

Every final answer is recomputed from the problem statement (sympy exact values plus a direct
numerical evaluation that does not use the theorem the solution relies on) and compared with the
constant written in solutions/2022-final-b2.html (SOL_* below).

Problem 8 additionally checks the orientation geometry: with P(t,psi) = (x(t), rho(t)cos psi,
rho(t)sin psi) the normal P_t x P_psi is +i on the rim circle (t = pi/3) and -i at the vertex
(t = pi), so no orientation of S is "+x" everywhere.  Both orientations are integrated directly.

Run: python3 -I stewart/exams/inventory/anchor-2022-final-b2.py   (exit 0 = all PASS)
"""
import math
import sys

import mpmath as mp
import sympy as sp

x, y, z, t, th, ps, r = sp.symbols("x y z t theta psi r", real=True)
ROWS = []


def check(label, ok, mine, sol):
    ROWS.append((label, bool(ok), str(mine), str(sol)))


def close(a, b, tol=1e-9):
    return abs(float(a) - float(b)) < tol * max(1.0, abs(float(b)))


# ---------- Gauss-Legendre (pure Python) and periodic trapezoid ----------
def gauss_legendre(n):
    nodes, weights = [], []
    for i in range(1, n + 1):
        xi = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(100):
            p0, p1 = 1.0, xi
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * xi * p1 - (k - 1) * p0) / k
            dp = n * (xi * p1 - p0) / (xi * xi - 1)
            dx = p1 / dp
            xi -= dx
            if abs(dx) < 1e-15:
                break
        nodes.append(xi)
        weights.append(2 / ((1 - xi * xi) * dp * dp))
    return nodes, weights


GLN, GLW = gauss_legendre(80)


def gl(f, a, b):
    h, m = (b - a) / 2, (b + a) / 2
    return h * sum(w * f(m + h * s) for s, w in zip(GLN, GLW))


def gl_split(f, a, b, pieces=8):
    step = (b - a) / pieces
    return sum(gl(f, a + i * step, a + (i + 1) * step) for i in range(pieces))


def trap_periodic(f, n=160):
    h = 2 * math.pi / n
    return h * sum(f(i * h) for i in range(n))


# ---------------- Solution constants (copied from solutions/2022-final-b2.html) ----------------
SOL_1 = 2 * sp.pi * sp.sin(1)
SOL_2 = (0, sp.Rational(-3, 5), 0)
SOL_2_mass = 80
SOL_3 = sp.pi / 2 + sp.exp(sp.pi / 2) - 1
SOL_4 = 5 - sp.exp(2)
SOL_5 = sp.pi**2 / 2
SOL_6 = 2 * sp.pi * (2 * sp.sqrt(2) - 1) / 9
SOL_7 = 2 * sp.pi**2
SOL_8_main = 3 * sp.pi / 8          # normal +i at the vertex (into the cup) == disk x=1/2 with +i
SOL_8_other = -3 * sp.pi / 8        # normal +i along the rim circle (outward of the enclosed solid)
SOL_9 = 3 * sp.pi
SOL_10a = 36
SOL_10a_detA = -18
SOL_10b = sp.Rational(-1, 10)

# ---------------- 1 ----------------
# exact via Q = u^2+v^2, |J| = 2/sqrt3
ex1 = sp.sqrt(3) * (2 / sp.sqrt(3)) * sp.integrate(sp.cos(r**2) * r, (r, 0, 1)) * 2 * sp.pi
# numeric directly in xy-polar: x^2-xy+y^2 = r^2 (1 - cos sin) <= 1
def p1_inner(a):
    q = 1 - math.cos(a) * math.sin(a)
    R = 1 / math.sqrt(q)
    return gl(lambda s: math.sqrt(3) * math.cos(s * s * q) * s, 0, R)
num1 = trap_periodic(p1_inner, 200)
check("1 exact 2*pi*sin1", sp.simplify(ex1 - SOL_1) == 0, sp.simplify(ex1), SOL_1)
check("1 direct xy-polar numeric", close(num1, SOL_1), f"{num1:.12f}", f"{float(SOL_1):.12f}")
check("1 wrong-Jacobian trap value 3pi/2 sin1",
      sp.simplify(sp.sqrt(3) * sp.sqrt(3) / 2 * sp.pi * sp.sin(1) - 3 * sp.pi / 2 * sp.sin(1)) == 0, "3pi/2 sin1", "3pi/2 sin1")

# ---------------- 2 ----------------
R2 = sp.Matrix([0, t**2 - 1, 2 * t])
ds = sp.sqrt(sum(c**2 for c in R2.diff(t)))
dens = 15 * sp.sqrt(R2[1] + 2)
m2 = sp.simplify(sp.integrate(sp.simplify(dens * ds), (t, -1, 1)))
cm = tuple(sp.simplify(sp.integrate(sp.simplify(R2[i] * dens * ds), (t, -1, 1)) / m2) for i in range(3))
check("2 mass", m2 == SOL_2_mass, m2, SOL_2_mass)
check("2 center of mass", all(sp.simplify(cm[i] - SOL_2[i]) == 0 for i in range(3)), cm, SOL_2)

# ---------------- 3 ----------------
def f3(tt):
    X, Y, Z = math.cos(tt) ** 2, math.sin(tt) ** 3, tt
    dX, dY, dZ = -2 * math.cos(tt) * math.sin(tt), 3 * math.sin(tt) ** 2 * math.cos(tt), 1.0
    q = X * X + Y * Y
    return (-Y / q) * dX + (X / q) * dY + math.exp(Z) * dZ
num3 = gl_split(f3, 0, math.pi / 2, 16)
minq = min(math.cos(s) ** 4 + math.sin(s) ** 6 for s in [i * (math.pi / 2) / 4000 for i in range(4001)])
check("3 path avoids z-axis (min x^2+y^2 > 0) and stays in x,y >= 0", minq > 0.1, f"min={minq:.4f}", ">0")
check("3 direct line integral", close(num3, SOL_3), f"{num3:.12f}", f"{float(SOL_3):.12f}")

# ---------------- 4 ----------------
def f4(a):
    rr = 1 + math.cos(a)
    X, Y = rr * math.cos(a), rr * math.sin(a)
    dX = -math.sin(a) * math.cos(a) - rr * math.sin(a)
    dY = -math.sin(a) * math.sin(a) + rr * math.cos(a)
    P = math.exp(X) + math.atan(Y)
    Q = 3 * X * Y + X / (1 + Y * Y)
    return P * dX + Q * dY
num4 = gl_split(f4, 0, math.pi, 16)
green4 = sp.integrate(sp.integrate(3 * r * sp.sin(th) * r, (r, 0, 1 + sp.cos(th))), (th, 0, sp.pi))
seg4 = sp.integrate(sp.exp(x), (x, 0, 2))
check("4 curve ends at origin (r(pi)=0), starts at (2,0)", (1 + sp.cos(sp.pi)) == 0, "r(pi)=0", "origin")
check("4 Green double integral = 4", sp.simplify(green4 - 4) == 0, green4, 4)
check("4 closing segment = e^2-1", sp.simplify(seg4 - (sp.exp(2) - 1)) == 0, seg4, "e^2-1")
check("4 direct line integral (theta increasing)", close(num4, SOL_4), f"{num4:.12f}", f"{float(SOL_4):.12f}")

# ---------------- 5 ----------------
def seg(p, q, s):
    return [p[i] + s * (q[i] - p[i]) for i in range(3)]
pts = [(sp.pi, 0, 0), (0, 0, 0), (0, sp.pi, 0), (0, 0, sp.pi)]
tot5 = 0
for k in range(3):
    X, Y, Z = seg(pts[k], pts[k + 1], t)
    integrand = (X + Y**2) * sp.diff(X, t) + X * Z * sp.diff(Y, t) + (Y + Z) * sp.diff(Z, t)
    tot5 += sp.integrate(integrand, (t, 0, 1))
check("5 three segments", sp.simplify(tot5 - SOL_5) == 0, sp.simplify(tot5), SOL_5)

# ---------------- 6 ----------------
def p6_inner(yy):
    h = math.sqrt(max(0.0, 1 - yy * yy)) / 3
    return gl(lambda zz: math.sqrt(1 + yy * yy + 9 * zz * zz), -h, h)
# endpoint sqrt singularity -> use substitution y = sin(u)
num6b = gl(lambda u: p6_inner(math.sin(u)) * math.cos(u), -math.pi / 2, math.pi / 2)
check("6 direct area integral over y^2+9z^2<=1", close(num6b, SOL_6, 1e-8), f"{num6b:.12f}", f"{float(SOL_6):.12f}")

# ---------------- 7 ----------------
# torus: ((2+cos v)cos u, (2+cos v) sin u, sin v), v in [0,pi] gives z>=0
u, v = sp.symbols("u v", real=True)
T = sp.Matrix([(2 + sp.cos(v)) * sp.cos(u), (2 + sp.cos(v)) * sp.sin(u), sp.sin(v)])
N7 = T.diff(v).cross(T.diff(u))  # check direction below
N7 = sp.simplify(N7)
# outward of tube: compare with (T - tube centre)
centre = sp.Matrix([2 * sp.cos(u), 2 * sp.sin(u), 0])
outdot = sp.simplify(N7.dot(T - centre))
sgn = 1 if float(outdot.subs({u: 0.3, v: 1.0})) > 0 else -1
N7 = sgn * N7
kcomp = sp.lambdify((u, v), N7[2], "math")
upward_ok = all(kcomp(0.7, i * math.pi / 200) >= -1e-12 for i in range(201))
F7 = sp.Matrix([T[1], -T[0], T[2]])
f7 = sp.lambdify((u, v), sp.simplify(F7.dot(N7)), "math")
num7 = gl(lambda vv: trap_periodic(lambda uu: f7(uu, vv), 64), 0, math.pi)
check("7 outward normal of half-torus is upward (k-comp >= 0)", upward_ok, upward_ok, True)
check("7 annulus z=0: F.(-k) = -z = 0", True, 0, 0)
check("7 direct flux through S", close(num7, SOL_7), f"{num7:.12f}", f"{float(SOL_7):.12f}")

# ---------------- 8 ----------------
xt = (2 - 2 * sp.cos(th)) * sp.cos(th)
rt = (2 - 2 * sp.cos(th)) * sp.sin(th)
Pp = sp.Matrix([xt, rt * sp.cos(ps), rt * sp.sin(ps)])
N8 = Pp.diff(th).cross(Pp.diff(ps))
N8s = sp.Matrix([rt * sp.diff(rt, th), -sp.diff(xt, th) * rt * sp.cos(ps), -sp.diff(xt, th) * rt * sp.sin(ps)])
check("8 N = P_t x P_psi = (rho rho', -x' rho cos, -x' rho sin)", sp.simplify(N8 - N8s) == sp.zeros(3, 1), "match", "match")
xp = sp.diff(xt, th)
rp = sp.diff(rt, th)
check("8 x' = 2 sin(t)(2cos t - 1)", sp.simplify(xp - 2 * sp.sin(th) * (2 * sp.cos(th) - 1)) == 0, sp.factor(xp), "2sin(2cos-1)")
check("8 rho' = 2(1-cos)(1+2cos) (zero at 2pi/3)",
      sp.simplify(rp - 2 * (1 - sp.cos(th)) * (1 + 2 * sp.cos(th))) == 0 and sp.simplify(rp.subs(th, 2 * sp.pi / 3)) == 0, "ok", "ok")
check("8 x' = 0 at t=pi/3 and t=pi", sp.simplify(xp.subs(th, sp.pi / 3)) == 0 and sp.simplify(xp.subs(th, sp.pi)) == 0, "ok", "ok")
xpf = sp.lambdify(th, xp, "math")
check("8 x decreasing on (pi/3, pi)", all(xpf(math.pi / 3 + (i + 0.5) * (2 * math.pi / 3) / 500) < 0 for i in range(500)), "x'<0", "x'<0")
check("8 endpoints (1/2, sqrt3/2) and (-4, 0)",
      sp.simplify(xt.subs(th, sp.pi / 3) - sp.Rational(1, 2)) == 0 and sp.simplify(rt.subs(th, sp.pi / 3) - sp.sqrt(3) / 2) == 0
      and sp.simplify(xt.subs(th, sp.pi) + 4) == 0 and sp.simplify(rt.subs(th, sp.pi)) == 0, "ok", "ok")
Nf = sp.lambdify((th, ps), list(N8), "math")
def unit(a, b):
    n = [float(c) for c in Nf(a, b)]
    m = math.sqrt(sum(c * c for c in n))
    return [c / m for c in n]
n_rim = unit(math.pi / 3, 0.4)
n_vtx = unit(math.pi - 1e-6, 0.4)
check("8 P_t x P_psi is +i on the rim circle", close(n_rim[0], 1, 1e-9), [round(c, 6) for c in n_rim], "+i")
check("8 P_t x P_psi is -i at the vertex (limit)", close(n_vtx[0], -1, 1e-6), [round(c, 6) for c in n_vtx], "-i")
# curl F
Fx = x + sp.exp(z) * y**2 + z**2 * y
Fy = x**2 * sp.sin(y) + x * y**2 * sp.cosh(y)
Fz = x * y - sp.exp(x * z) * sp.cos(z)
curl = sp.Matrix([sp.diff(Fz, y) - sp.diff(Fy, z), sp.diff(Fx, z) - sp.diff(Fz, x), sp.diff(Fy, x) - sp.diff(Fx, y)])
check("8 (curl F)_x = x", sp.simplify(curl[0] - x) == 0, curl[0], "x")
curl_on = curl.subs({x: Pp[0], y: Pp[1], z: Pp[2]})
f8 = sp.lambdify((th, ps), curl_on.dot(N8), "math")
flux_N = gl_split(lambda a: trap_periodic(lambda b: f8(a, b), 128), math.pi / 3, math.pi, 8)
check("8 direct flux, orientation +i at vertex (= -N)", close(-flux_N, SOL_8_main, 1e-8), f"{-flux_N:.12f}", f"{float(SOL_8_main):.12f}")
check("8 direct flux, orientation +i on rim (= +N)", close(flux_N, SOL_8_other, 1e-8), f"{flux_N:.12f}", f"{float(SOL_8_other):.12f}")
# Stokes: rim circle x=1/2, radius sqrt3/2, ccw seen from +x: (1/2, a cos s, a sin s)
a8 = math.sqrt(3) / 2
Ff = sp.lambdify((x, y, z), [Fx, Fy, Fz], "math")
def f8line(s):
    X, Y, Z = 0.5, a8 * math.cos(s), a8 * math.sin(s)
    Fv = [float(c) for c in Ff(X, Y, Z)]
    return Fv[1] * (-a8 * math.sin(s)) + Fv[2] * (a8 * math.cos(s))
line8 = trap_periodic(f8line, 256)
check("8 rim line integral (ccw from +x) = disk flux with +i", close(line8, SOL_8_main, 1e-9), f"{line8:.12f}", f"{float(SOL_8_main):.12f}")

# ---------------- 9 ----------------
def f9(rr):
    Z = 2 - rr * rr
    return (2 * rr * rr + Z) / (rr * rr + Z * Z) ** 1.5 * rr  # F.(2x,2y,1) r, angular part trivial
num9 = 2 * math.pi * gl_split(f9, 0, math.sqrt(3), 8)
dist_min = min(math.sqrt(rr * rr + (2 - rr * rr) ** 2) for rr in [i * math.sqrt(3) / 2000 for i in range(2001)])
bottom = 2 * sp.pi * sp.integrate(r / (r**2 + 1) ** sp.Rational(3, 2), (r, 0, sp.sqrt(3)))
check("9 origin inside E (dist to paraboloid > 1, to base = 1)", dist_min > 1, f"{dist_min:.4f}", ">1")
check("9 bottom disk flux (outward -k) = pi", sp.simplify(bottom - sp.pi) == 0, bottom, "pi")
check("9 direct flux through paraboloid", close(num9, SOL_9), f"{num9:.12f}", f"{float(SOL_9):.12f}")

# ---------------- 10 ----------------
A = sp.Matrix([[3, 5, -2, 6], [1, 2, -1, 1], [2, 4, 1, 5], [3, 7, 5, 3]])
v10a = ((2 * A).T).det() + (A * A).det()
check("10(a) det A", A.det() == SOL_10a_detA, A.det(), SOL_10a_detA)
check("10(a) det((2A)^T)+det(A^2)", v10a == SOL_10a, v10a, SOL_10a)
M = sp.Matrix([[1, 3, 5, 2], [0, -1, 3, 4], [2, 1, 9, 6], [3, 2, 4, 8]])
b = sp.Matrix([1, -1, 0, 1])
Mw = M.copy()
Mw[:, 3] = b
sol = M.LUsolve(b)
check("10(b) D=160, D_w=-16", M.det() == 160 and Mw.det() == -16, (M.det(), Mw.det()), (160, -16))
check("10(b) w (Cramer and LU agree)", Mw.det() / M.det() == SOL_10b and sol[3] == SOL_10b, sol.T, SOL_10b)

# ---------------- report ----------------
w = max(len(rw[0]) for rw in ROWS)
for label, ok, mine, solv in ROWS:
    print(f"{'PASS' if ok else 'FAIL'}  {label:<{w}}  mine={mine}  sol={solv}")
nfail = sum(not rw[1] for rw in ROWS)
print(f"\n{len(ROWS)} checks, {len(ROWS) - nfail} PASS, {nfail} FAIL")
sys.exit(1 if nfail else 0)
