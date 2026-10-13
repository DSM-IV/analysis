#!/usr/bin/env python3
"""Independent anchor values for stewart/exams 2022-midterm-b2 (Calculus II midterm, Fall 2022, block 2).

Every final answer is recomputed from the problem statement with sympy / mpmath and compared
with the constant written in solutions/2022-midterm-b2.html (SOL_* below).
Reordering / coordinate-change problems (7a, 8a, 8b) are checked by evaluating the original
and the rewritten integral for several test integrands.
Run: python3 -I stewart/exams/inventory/anchor-2022-midterm-b2.py   (exit 0 = all PASS)
"""
import math
import random
import sys

import mpmath as mp
import sympy as sp

mp.mp.dps = 20
x, y, z, s, t, r, th, ph, rho, h, u = sp.symbols("x y z s t r theta phi rho h u", real=True)

ROWS = []


def check(label, ok, mine, sol):
    ROWS.append((label, bool(ok), str(mine), str(sol)))


def close(a, b, tol=1e-9):
    return abs(complex(a) - complex(b)) < tol


def same(a, b):
    return sp.simplify(sp.nsimplify(a) - sp.nsimplify(b)) == 0


# ---------------- Solution constants (copied from solutions/2022-midterm-b2.html) ----------------
SOL_1a_paths = (0, sp.Rational(1, 2))          # y=0 -> 0, y=x -> 1/2  => DNE
SOL_1b = 0
SOL_2a_bound = "|f| <= |x| + 3|y|"
SOL_2b = (1, 0)                                 # f_x(0,0), f_xx(0,0)
SOL_3_grad = (sp.Rational(-2, 7), sp.Rational(4, 7))
SOL_3a = 2 * sp.sqrt(5) / 7
SOL_3b = sp.Rational(4, 5)
SOL_4a = (2, -6)                                # g_s(1,0), g_ss(1,0)
SOL_4b = 2 * y                                  # h(x,y)
SOL_5a = {(0, 1): ("min", -1), (2, 1): ("saddle", 4 * sp.exp(-2) - 1)}
SOL_5b = (sp.E - 1, -1)                         # absolute max, absolute min on the disk
SOL_6 = sp.pi / 8 - sp.log(2) / 4
SOL_7a = "int_{-pi/3}^{pi/3} int_1^2 f r dr dtheta"
SOL_7b = (135 * sp.sqrt(3) / (56 * sp.pi), 0)
SOL_9 = 10 * sp.pi / 3
SOL_10 = 175 * sp.pi / 96

# ---------------- 1(a) ----------------
f1a = (4 * x**3 + x * y) / (x**2 + y**2)
p0 = sp.limit(f1a.subs(y, 0), x, 0)
p1 = sp.limit(f1a.subs(y, x), x, 0)
m = sp.symbols("m", real=True)
pm = sp.simplify(sp.limit(f1a.subs(y, m * x), x, 0))
check("1(a) path y=0", p0 == SOL_1a_paths[0], p0, SOL_1a_paths[0])
check("1(a) path y=x", p1 == SOL_1a_paths[1], p1, SOL_1a_paths[1])
check("1(a) path y=mx gives m/(1+m^2) (DNE)", sp.simplify(pm - m / (1 + m**2)) == 0, pm, "m/(1+m^2)")

# ---------------- 1(b) ----------------
random.seed(7)
ok1b = True
for _ in range(20000):
    R = 10 ** random.uniform(-4, 0)
    a = random.uniform(0, 2 * math.pi)
    X, Y = R * math.cos(a), R * math.sin(a)
    q = X * X + Y * Y
    val = abs(X * X * Y / q * math.sin(1 / q))
    if val > abs(Y) * (1 + 1e-12):
        ok1b = False
check("1(b) |f| <= |y| (random samples) => limit 0", ok1b and SOL_1b == 0, "bound holds, limit 0", SOL_1b)

# ---------------- 2 ----------------
f2 = (x**3 + 3 * y**5) / (x**2 + x**2 * y**2 + y**4)
f2n = sp.lambdify((x, y), f2, "math")
ok2a = True
for _ in range(20000):
    R = 10 ** random.uniform(-5, 0)
    a = random.uniform(0, 2 * math.pi)
    X, Y = R * math.cos(a), R * math.sin(a)
    if abs(f2n(X, Y)) > (abs(X) + 3 * abs(Y)) * (1 + 1e-12):
        ok2a = False
check("2(a) |f| <= |x|+3|y| (random samples)", ok2a, "bound holds", SOL_2a_bound)
lim2a = sp.limit(sp.simplify(f2.subs({x: r * sp.cos(th), y: r * sp.sin(th)}).subs(th, sp.pi / 7)), r, 0)
check("2(a) sample ray limit = 0 = f(0,0)", lim2a == 0, lim2a, 0)

fx00 = sp.limit((f2.subs({x: h, y: 0}) - 0) / h, h, 0)
fx_formula = sp.diff(f2, x)                     # valid off the origin
fx_on_axis = sp.simplify(fx_formula.subs(y, 0))  # f_x(h,0), h != 0
fxx00 = sp.limit((fx_on_axis.subs(x, h) - fx00) / h, h, 0)
check("2(b) f_x(0,0) by definition", fx00 == SOL_2b[0], fx00, SOL_2b[0])
check("2(b) f_x(h,0)=1 for h!=0 (quotient rule, y=0)", fx_on_axis == 1, fx_on_axis, 1)
check("2(b) f_xx(0,0) by definition", fxx00 == SOL_2b[1], fxx00, SOL_2b[1])
# numeric difference quotient of f along y=0 near h = 0.37 (independent of the formula)
hh, kk = 0.37, 1e-6
fxh_num = (f2n(hh + kk, 0.0) - f2n(hh - kk, 0.0)) / (2 * kk)
check("2(b) numeric f_x(0.37,0) = 1", close(fxh_num, 1, 1e-6), fxh_num, 1)

# ---------------- 3 ----------------
F3 = x**2 - 2 * y**3 + 3 * z**4 - 2 * x * y * z
pt = {x: 1, y: -1, z: 1}
check("3 f(1,-1,1) = 8", F3.subs(pt) == 8, F3.subs(pt), 8)
gx = -sp.diff(F3, x).subs(pt) / sp.diff(F3, z).subs(pt)
gy = -sp.diff(F3, y).subs(pt) / sp.diff(F3, z).subs(pt)
check("3 grad g(1,-1)", (gx, gy) == SOL_3_grad, (gx, gy), SOL_3_grad)
mag = sp.sqrt(gx**2 + gy**2)
check("3(a) max directional derivative |grad g|", sp.simplify(mag - SOL_3a) == 0, mag, SOL_3a)
L = 1 + gx * sp.Rational(3, 10) + gy * sp.Rational(-2, 10)
check("3(b) linear approximation g(1.3,-1.2)", L == SOL_3b, L, SOL_3b)
# implicit-function sanity: solve F3(x,y,z)=8 near z=1 by Newton at a nearby point and compare slopes
F3n = sp.lambdify((x, y, z), F3, "mpmath")
zz = mp.findroot(lambda Z: F3n(1 + mp.mpf("1e-6"), -1, Z) - 8, 1)
check("3 numeric g_x(1,-1) via Newton", close((zz - 1) / 1e-6, float(gx), 1e-4), mp.nstr((zz - 1) / 1e-6, 8), gx)

# ---------------- 4 ----------------
# Taylor polynomial of f at (0,1) carries all data needed for g_s, g_ss at (1,0)
fT = 2 * x + (y - 1) + sp.Rational(1, 2) * (-1) * x**2 + 3 * x * (y - 1) + sp.Rational(1, 2) * (-2) * (y - 1)**2
gT = fT.subs({x: t / s, y: s**2 + t**2})
gs10 = sp.diff(gT, s).subs({s: 1, t: 0})
gss10 = sp.diff(gT, s, 2).subs({s: 1, t: 0})
check("4(a) g_s(1,0)", gs10 == SOL_4a[0], gs10, SOL_4a[0])
check("4(a) g_ss(1,0)", gss10 == SOL_4a[1], gss10, SOL_4a[1])
ok4b = True
for ftest in (sp.exp(x) * sp.sin(y) + x**3 * y**2, sp.cos(x * y) + y**3 * x, sp.log(1 + y**2) * (x + 2)):
    g = ftest.subs({x: t / s, y: s**2 + t**2})
    lhs = s * sp.diff(g, s) + t * sp.diff(g, t)
    rhs = (SOL_4b * sp.diff(ftest, y)).subs({x: t / s, y: s**2 + t**2})
    for sv, tv in ((1.3, 0.4), (-0.7, 1.1), (2.0, -0.5)):
        if abs(float((lhs - rhs).subs({s: sv, t: tv}))) > 1e-10:
            ok4b = False
check("4(b) s g_s + t g_t = 2y f_y (3 test f's)", ok4b, "identity holds", SOL_4b)

# ---------------- 5(a) ----------------
f5 = x**2 * sp.exp(-x) + y**2 - 2 * y
crit = sp.solve([sp.diff(f5, x), sp.diff(f5, y)], [x, y], dict=True)
found = {}
for c in crit:
    H = sp.hessian(f5, (x, y)).subs(c)
    Dv = sp.simplify(H.det())
    kind = "saddle" if Dv < 0 else ("min" if H[0, 0] > 0 else "max")
    found[(c[x], c[y])] = (kind, sp.simplify(f5.subs(c)))
ok5a = set(found) == set(SOL_5a) and all(found[k][0] == SOL_5a[k][0] and sp.simplify(found[k][1] - SOL_5a[k][1]) == 0 for k in found)
check("5(a) critical points + classification", ok5a, found, SOL_5a)

# ---------------- 5(b) ----------------
f5n = sp.lambdify((x, y), f5, "math")
bvals = [f5n(math.cos(a), 1 + math.sin(a)) for a in (2 * math.pi * k / 200000 for k in range(200000))]
ivals = []
N = 400
for i in range(N + 1):
    for j in range(N + 1):
        X, Y = -1 + 2 * i / N, 2 * j / N
        if X * X + (Y - 1)**2 <= 1:
            ivals.append(f5n(X, Y))
vmax, vmin = max(bvals + ivals), min(bvals + ivals)
check("5(b) absolute max (dense sampling)", close(vmax, float(SOL_5b[0]), 1e-6), vmax, SOL_5b[0])
check("5(b) absolute min (dense sampling)", close(vmin, float(SOL_5b[1]), 1e-6), vmin, SOL_5b[1])
# psi(x) = (2-x)e^{-x}: psi' = (x-3)e^{-x} < 0 on [-1,1], psi(0)=2 -> unique root of psi=2 is 0
psi = (2 - x) * sp.exp(-x)
dpsi = sp.simplify(sp.diff(psi, x) - (x - 3) * sp.exp(-x))
sign_ok = all(((2 - X) * math.exp(-X) - 2) * (-X) >= -1e-15 for X in (-1 + 2 * k / 100000 for k in range(100001)))
check("5(b) psi' = (x-3)e^{-x}, psi=2 only at x=0 on [-1,1]", dpsi == 0 and sign_ok and psi.subs(x, 0) == 2, "unique root 0", "x=0")
# Lagrange points on the circle <=> zeros of the tangential derivative
#   T(a) = grad f . <-sin a, cos a>  at (cos a, 1 + sin a)   (grad g != 0 on the circle).
# (Newton on the 3x3 Lagrange system is useless here: its Jacobian is singular at (0,0),(0,2).)
# T has a double zero at a = pi/2, 3pi/2, so locate local minima of |T| on a grid and refine.
fxn = sp.lambdify((x, y), sp.diff(f5, x), "mpmath")
fyn = sp.lambdify((x, y), sp.diff(f5, y), "mpmath")
T = lambda a: -mp.sin(a) * fxn(mp.cos(a), 1 + mp.sin(a)) + mp.cos(a) * fyn(mp.cos(a), 1 + mp.sin(a))
NG = 7200
grid = [2 * mp.pi * k / NG for k in range(NG)]
absT = [abs(T(a)) for a in grid]
sols = set()
for k in range(NG):
    if absT[k] <= absT[k - 1] and absT[k] <= absT[(k + 1) % NG]:
        try:
            a0 = mp.findroot(T, grid[k], tol=1e-24)
        except Exception:
            continue
        if abs(T(a0)) < 1e-10:
            sols.add((round(float(mp.cos(a0)), 6) + 0.0, round(float(1 + mp.sin(a0)), 6) + 0.0))
expect = {(1.0, 1.0), (-1.0, 1.0), (0.0, 0.0), (0.0, 2.0)}
check("5(b) Lagrange points on circle = {(+-1,1),(0,0),(0,2)}", sols == expect, sorted(sols), sorted(expect))

# ---------------- 6 ----------------
V6orig = mp.quad(lambda X: mp.quad(lambda Y: mp.cos(Y) * mp.atan(mp.cos(Y)**2), [mp.asin(X), mp.pi / 2]), [0, 1])
V6rev = sp.integrate(sp.integrate(sp.cos(y) * sp.atan(sp.cos(y)**2), (x, 0, sp.sin(y))), (y, 0, sp.pi / 2))
check("6 volume (original order, numeric)", close(V6orig, float(SOL_6), 1e-12), mp.nstr(V6orig, 15), sp.N(SOL_6, 15))
check("6 volume (reversed, numeric value of sympy result)", close(sp.N(V6rev, 20), float(SOL_6), 1e-12), sp.N(V6rev, 15), SOL_6)

# ---------------- 7(a) ----------------
def sum7(F):
    a = mp.quad(lambda X: mp.quad(lambda Y: F(X, Y), [-mp.sqrt(3) * X, -mp.sqrt(1 - X**2)]), [0.5, 1])
    b = mp.quad(lambda X: mp.quad(lambda Y: F(X, Y), [mp.sqrt(1 - X**2), mp.sqrt(3) * X]), [0.5, 1])
    c = mp.quad(lambda X: mp.quad(lambda Y: F(X, Y), [-mp.sqrt(4 - X**2), mp.sqrt(4 - X**2)]), [1, 2])
    return a + b + c


def polar7(F):
    return mp.quad(lambda T: mp.quad(lambda R: F(R * mp.cos(T), R * mp.sin(T)) * R, [1, 2]), [-mp.pi / 3, mp.pi / 3])


ok7a = True
vals7 = []
for F in (lambda X, Y: 1 + X + Y**2, lambda X, Y: mp.exp(X) * mp.cos(Y) + X * Y**3 + Y, lambda X, Y: 1):
    A, B = sum7(F), polar7(F)
    vals7.append((mp.nstr(A, 12), mp.nstr(B, 12)))
    ok7a = ok7a and close(A, B, 1e-10)
check("7(a) Cartesian sum = polar (3 test f's)", ok7a, vals7, SOL_7a)

# ---------------- 7(b) ----------------
m7 = sp.integrate(r * r, (r, 1, 2), (th, -sp.pi / 3, sp.pi / 3))
My7 = sp.integrate(r * sp.cos(th) * r * r, (r, 1, 2), (th, -sp.pi / 3, sp.pi / 3))
Mx7 = sp.integrate(r * sp.sin(th) * r * r, (r, 1, 2), (th, -sp.pi / 3, sp.pi / 3))
xb, yb = sp.simplify(My7 / m7), sp.simplify(Mx7 / m7)
check("7(b) mass 14pi/9", sp.simplify(m7 - 14 * sp.pi / 9) == 0, m7, "14*pi/9")
check("7(b) center of mass", sp.simplify(xb - SOL_7b[0]) == 0 and yb == SOL_7b[1], (xb, yb), SOL_7b)
# Cartesian cross-check of the mass and M_y using the three original pieces
m7c = sum7(lambda X, Y: mp.sqrt(X**2 + Y**2))
My7c = sum7(lambda X, Y: X * mp.sqrt(X**2 + Y**2))
check("7(b) x-bar from Cartesian pieces", close(My7c / m7c, float(SOL_7b[0]), 1e-10), mp.nstr(My7c / m7c, 12), sp.N(SOL_7b[0], 12))

# ---------------- 8(a) ----------------
# inner integrals done exactly by sympy, outer two numerically


def outer2(expr_inner, v_out, v_mid, mid_lo, mid_hi, out_lo, out_hi, out_pts=None):
    fi = sp.lambdify((v_out, v_mid), expr_inner, "mpmath")
    flo = sp.lambdify(v_out, mid_lo, "mpmath")
    fhi = sp.lambdify(v_out, mid_hi, "mpmath")
    pts = out_pts if out_pts else [out_lo, out_hi]
    return mp.quad(lambda O: mp.quad(lambda M: fi(O, M), [flo(O), fhi(O)]), pts)


tests8a = [1 + x + y**2 + z, x**2 * sp.exp(y) + z**3 + x * y * z + y, sp.cos(x + y) + z * y**2]
ok8a = True
vals8a = []
for g in tests8a:
    # original: dx dz dy  (x inner, z middle, y outer)
    gin = sp.integrate(g, (x, -sp.sqrt(1 - z), sp.sqrt(1 - z)))
    orig = outer2(gin, y, z, sp.Integer(0) * y, 1 - sp.sqrt(1 - (y - 1)**2), 0, 1)
    # rewritten: dz dy dx, two pieces
    g1 = sp.integrate(g, (z, 0, 1 - x**2))
    g2 = sp.integrate(g, (z, 0, 1 - sp.sqrt(1 - (y - 1)**2)))
    p1 = outer2(g1, x, y, sp.Integer(0) * x, 1 - sp.sqrt(1 - x**4), -1, 1, [-1, 0, 1])
    p2 = outer2(g2, x, y, 1 - sp.sqrt(1 - x**4), sp.Integer(1) + 0 * x, -1, 1, [-1, 0, 1])
    vals8a.append((mp.nstr(orig, 12), mp.nstr(p1 + p2, 12)))
    ok8a = ok8a and close(orig, p1 + p2, 1e-9)
check("8(a) original = rewritten dz dy dx (3 test f's)", ok8a, vals8a, "equal")
# a single-piece answer (top = 1-x^2 only) would be wrong:
gw = sp.integrate(sp.Integer(1), (z, 0, 1 - x**2))
wrong = outer2(gw, x, y, sp.Integer(0) * x, sp.Integer(1) + 0 * x, -1, 1)
gin1 = sp.integrate(sp.Integer(1), (x, -sp.sqrt(1 - z), sp.sqrt(1 - z)))
vol8a = outer2(gin1, y, z, sp.Integer(0) * y, 1 - sp.sqrt(1 - (y - 1)**2), 0, 1)
check("8(a) naive single top surface differs (volume)", not close(wrong, vol8a, 1e-6), mp.nstr(wrong, 10), mp.nstr(vol8a, 10))

# ---------------- 8(b) ----------------
X_ = rho * sp.sin(ph) * sp.cos(th)
Y_ = rho * sp.sin(ph) * sp.sin(th)
Z_ = rho * sp.cos(ph)
tests8b = [1 + x + y**2 + z, (x + 1)**2 * y + z**2 + x * z, sp.Integer(1), y**3 * z + x**2]
ok8b = True
vals8b = []
for g in tests8b:
    # original cylindrical: dz dr dtheta
    gc = sp.integrate(g.subs({x: r * sp.cos(th), y: r * sp.sin(th)}) * r,
                      (z, sp.sqrt(2 * r * sp.sin(th) - r**2), sp.sqrt(4 - r**2)))
    orig = outer2(gc, th, r, sp.Integer(0) * th, 2 * sp.sin(th), 0, sp.pi, [0, mp.pi / 2, mp.pi])
    # spherical answer: d rho d phi d theta, alpha(theta) = min(theta, pi - theta)
    G = g.subs({x: X_, y: Y_, z: Z_}) * rho**2 * sp.sin(ph)
    lo = 2 * sp.sin(ph) * sp.sin(th)
    Ga = sp.lambdify((th, ph), sp.integrate(G, (rho, lo, 2)), "mpmath")
    Gb = sp.lambdify((th, ph), sp.integrate(G, (rho, lo, 2 * sp.sin(th) / sp.sin(ph))), "mpmath")

    def sph(T):
        al = min(T, mp.pi - T)
        return mp.quad(lambda P: Ga(T, P), [0, al]) + mp.quad(lambda P: Gb(T, P), [al, mp.pi / 2])

    spv = mp.quad(sph, [0, mp.pi / 2, mp.pi])
    vals8b.append((mp.nstr(orig, 12), mp.nstr(spv, 12)))
    ok8b = ok8b and close(orig, spv, 1e-9)
check("8(b) cylindrical = spherical d rho d phi d theta (4 test f's)", ok8b, vals8b, "equal")

# ---------------- 9 ----------------
integrand9 = (1 + r * sp.cos(th) + r * sp.sin(th)) * r
I9 = sp.integrate(integrand9, (z, 0, 3 - r**2), (r, 0, 1), (th, 0, 2 * sp.pi)) + \
    sp.integrate(integrand9, (z, sp.sqrt(r**2 - 1), 3 - r**2), (r, 1, sp.sqrt(2)), (th, 0, 2 * sp.pi))
check("9 cylindrical (full integrand incl. x,y)", sp.simplify(I9 - SOL_9) == 0, sp.simplify(I9), SOL_9)
V9z = sp.integrate(sp.pi * (1 + z**2), (z, 0, 1)) + sp.integrate(sp.pi * (3 - z), (z, 1, 3))
check("9 volume by z-slices", sp.simplify(V9z - SOL_9) == 0, V9z, SOL_9)
# Monte Carlo sanity check of the full integrand in Cartesian coordinates (seeded)
random.seed(11)
NMC, acc = 400000, 0.0
for _ in range(NMC):
    X, Y, Z = random.uniform(-math.sqrt(3), math.sqrt(3)), random.uniform(-math.sqrt(3), math.sqrt(3)), random.uniform(0, 3)
    q = X * X + Y * Y
    if q - Z * Z <= 1 and Z <= 3 - q:
        acc += 1 + X + Y
mc9 = acc / NMC * (2 * math.sqrt(3))**2 * 3
check("9 Monte Carlo (Cartesian, 4e5 pts, tol 2%)", abs(mc9 - float(SOL_9)) < 0.02 * float(SOL_9), round(mc9, 4), sp.N(SOL_9, 8))

# ---------------- 10 ----------------
V10 = sp.integrate(rho**2 * sp.sin(ph), (rho, 0, 1 + sp.cos(ph)), (th, 0, 2 * sp.pi), (ph, 0, sp.pi / 3))
check("10 spherical symbolic", sp.simplify(V10 - SOL_10) == 0, sp.simplify(V10), SOL_10)


# independent cylindrical check: for each r, z from the cone z=r/sqrt3 up to the surface (bisection)
def ztop(R):
    hfun = lambda Z: R * R + Z * Z - mp.sqrt(R * R + Z * Z) - Z
    a, b = R / mp.sqrt(3), mp.mpf(3)
    if hfun(a) > 0:
        return a
    for _ in range(80):
        c = (a + b) / 2
        if hfun(c) <= 0:
            a = c
        else:
            b = c
    return a


rmax = mp.mpf(3) / 2 * mp.sin(mp.pi / 3)
V10c = 2 * mp.pi * mp.quad(lambda R: R * (ztop(R) - R / mp.sqrt(3)), [0, rmax])
check("10 cylindrical shells (bisection)", close(V10c, float(SOL_10), 1e-8), mp.nstr(V10c, 12), sp.N(SOL_10, 12))
check("10 surface max r = 3sqrt3/4 at phi=pi/3", close(max((1 + math.cos(p)) * math.sin(p) for p in (k * math.pi / 200000 for k in range(200001))), float(rmax), 1e-9),
      mp.nstr(rmax, 10), "r-extent")

# ---------------- report ----------------
w0 = max(len(rw[0]) for rw in ROWS)
print(f"{'check'.ljust(w0)}  result  mine | solution")
for label, ok, mine, sol in ROWS:
    print(f"{label.ljust(w0)}  {'PASS' if ok else 'FAIL'}    {mine} | {sol}")
nf = sum(1 for rw in ROWS if not rw[1])
print(f"\n{len(ROWS)} checks, {len(ROWS) - nf} PASS, {nf} FAIL")
sys.exit(1 if nf else 0)
