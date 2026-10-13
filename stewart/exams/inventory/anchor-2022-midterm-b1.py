#!/usr/bin/env python3
"""Independent anchor values for stewart/exams 2022-midterm-b1 (Calculus II midterm, Fall 2022, block 1).

Every final answer is recomputed from the problem statement with sympy / mpmath and compared
with the constant written in solutions/2022-midterm-b1.html (SOL_* below).
Run: python3 -I stewart/exams/inventory/anchor-2022-midterm-b1.py   (exit 0 = all PASS)
"""
import random
import sys

import mpmath as mp
import sympy as sp

mp.mp.dps = 30
x, y, z, t, r, th, ph, rho, lam = sp.symbols("x y z t r theta phi rho lambda", real=True)

ROWS = []


def check(label, ok, mine, sol):
    ROWS.append((label, bool(ok), str(mine), str(sol)))


def close(a, b, tol=1e-9):
    return abs(complex(a) - complex(b)) < tol


# ---------------- Solution constants (copied from solutions/2022-midterm-b1.html) ----------------
SOL_1a_paths = (1, 0)              # y=0 -> 1, y=-x -> 0  => DNE
SOL_1b = 0
SOL_2a = sp.Rational(3, 4) * (sp.E**4 - 1)
SOL_2b_inner = (sp.Rational(3, 2) * y - 1, 6)   # int_0^2 int_{3y/2-1}^6 f dx dy
SOL_3_fx, SOL_3_fy, SOL_3_f0 = 6, 2, 8
SOL_3c = sp.Rational(401, 50)
SOL_4_min = {(0, -2): -4}
SOL_4_saddles = {(-1, sp.Rational(-1, 2)), (3, sp.Rational(23, 2))}
SOL_5a = (2 * sp.sqrt(2), -sp.sqrt(2), 3 * sp.sqrt(2))
SOL_5b = (-6, -12, 6)
SOL_5c = sp.Rational(-35, 3)
SOL_6_max = 5 * sp.sqrt(5)
SOL_6_min = -sp.Rational(75, 8) - 5 * sp.sqrt(10) / 2
SOL_7a = sp.sqrt(2) / 2
SOL_7b = 1 + 2 * sp.sqrt(2)
SOL_8a = sp.Rational(11, 24)
SOL_8b = sp.Rational(27, 22)
SOL_9 = 25 * sp.pi / 6 - sp.Rational(32, 9)
SOL_10 = sp.pi * (2 - sp.sqrt(2)) / 2

# ---------------- 1(a) ----------------
f1a = (sp.sin(x) + sp.sin(y)) ** 2 / (x**2 + y**2)
p_y0 = sp.limit(f1a.subs(y, 0), x, 0)
p_yx = sp.limit(f1a.subs(y, x), x, 0)
p_ymx = sp.limit(f1a.subs(y, -x), x, 0)
check("1(a) path y=0", p_y0 == SOL_1a_paths[0], p_y0, SOL_1a_paths[0])
check("1(a) path y=-x", p_ymx == SOL_1a_paths[1], p_ymx, SOL_1a_paths[1])
check("1(a) DNE (y=x gives 2, too)", p_y0 != p_ymx and p_yx == 2, f"{p_y0},{p_ymx},{p_yx}", "DNE")

# ---------------- 1(b) ----------------
num = x**3 * y * z + x * y**3 * z - x * y * z**3
check("1(b) factorization xyz(x^2+y^2-z^2)", sp.expand(num - x * y * z * (x**2 + y**2 - z**2)) == 0, "0", "0")
f1b = num / (x**2 + y**2 + z**2)
random.seed(1)
bound_ok = True
for _ in range(20000):
    R = 10 ** random.uniform(-4, 0)
    v = [random.gauss(0, 1) for _ in range(3)]
    n = sum(c * c for c in v) ** 0.5
    px, py, pz = (R * c / n for c in v)
    val = abs((px**3 * py * pz + px * py**3 * pz - px * py * pz**3) / (px**2 + py**2 + pz**2))
    if val > R**3 * (1 + 1e-12):
        bound_ok = False
check("1(b) |f| <= R^3 (random samples)", bound_ok, "bound holds", "R^3")
sph = f1b.subs({x: rho * sp.sin(ph) * sp.cos(th), y: rho * sp.sin(ph) * sp.sin(th), z: rho * sp.cos(ph)})
lim1b = sp.limit(sp.simplify(sph), rho, 0)
check("1(b) limit", lim1b == SOL_1b, lim1b, SOL_1b)

# ---------------- 2(a) ----------------
orig2a = mp.quad(lambda X: mp.quad(lambda Y: mp.e ** (Y**2), [X / 2, 2 * X]), [0, 1]) + \
    mp.quad(lambda X: mp.quad(lambda Y: mp.e ** (Y**2), [X / 2, 2]), [1, 4])
rev2a = sp.integrate(sp.integrate(sp.exp(y**2), (x, y / 2, 2 * y)), (y, 0, 2))
check("2(a) reversed symbolic", sp.simplify(rev2a - SOL_2a) == 0, sp.simplify(rev2a), SOL_2a)
check("2(a) original numeric", close(orig2a, sp.N(SOL_2a, 30), 1e-15), mp.nstr(orig2a, 15), sp.N(SOL_2a, 15))

# ---------------- 2(b) ----------------
for name, ftest in [("1+x+y^2", lambda X, Y: 1 + X + Y**2), ("x*y+exp(y)", lambda X, Y: X * Y + mp.e**Y)]:
    orig = mp.quad(lambda X: mp.quad(lambda Y: ftest(X, Y), [0, 2 * (X + 1) / 3]), [-1, 0]) \
        + mp.quad(lambda X: mp.quad(lambda Y: ftest(X, Y), [0, 2 * (X + 1) / 3]), [0, 2]) \
        + mp.quad(lambda X: mp.quad(lambda Y: ftest(X, Y), [0, mp.sqrt(6 - X)]), [2, 6]) \
        + mp.quad(lambda X: mp.quad(lambda Y: ftest(X, Y), [mp.sqrt(6 - X), 2]), [2, 6])
    rev = mp.quad(lambda Y: mp.quad(lambda X: ftest(X, Y), [mp.mpf(3) / 2 * Y - 1, 6]), [0, 2])
    check(f"2(b) reversed order, f={name}", close(orig, rev, 1e-12), mp.nstr(orig, 15), mp.nstr(rev, 15))

# ---------------- 3 ----------------
R_, S_, T_ = sp.symbols("R S T")
g = R_**2 + 2 * S_**2 - T_**2
f3 = g.subs({R_: x**2 * y, S_: sp.exp(x * y + 1) - 3, T_: 3 * x * y**2 - 2})
pt = {x: 1, y: -1}
fx3 = sp.simplify(sp.diff(f3, x).subs(pt))
fy3 = sp.simplify(sp.diff(f3, y).subs(pt))
f03 = sp.simplify(f3.subs(pt))
check("3(a) f_x(1,-1)", fx3 == SOL_3_fx, fx3, SOL_3_fx)
check("3(a) f_y(1,-1)", fy3 == SOL_3_fy, fy3, SOL_3_fy)
check("3(b) f(1,-1)", f03 == SOL_3_f0, f03, SOL_3_f0)
L3 = f03 + fx3 * (x - 1) + fy3 * (y + 1)
est = L3.subs({x: sp.Rational(101, 100), y: sp.Rational(-102, 100)})
check("3(c) L(1.01,-1.02)", est == SOL_3c, est, SOL_3c)
true3c = sp.N(f3.subs({x: sp.Rational(101, 100), y: sp.Rational(-102, 100)}), 10)
check("3(c) sanity: true value near estimate", abs(true3c - 8.02) < 0.05, true3c, "~8.02")

# ---------------- 4 ----------------
f4 = 6 * x**3 - 3 * x**2 * y + sp.Rational(15, 2) * x**2 + y**2 + 4 * y
crit = sp.solve([sp.diff(f4, x), sp.diff(f4, y)], [x, y], dict=True)
H = sp.hessian(f4, (x, y))
mins, maxs, sads = {}, {}, set()
for c in crit:
    D = H.det().subs(c)
    fxx = H[0, 0].subs(c)
    p = (c[x], c[y])
    if D > 0 and fxx > 0:
        mins[p] = f4.subs(c)
    elif D > 0 and fxx < 0:
        maxs[p] = f4.subs(c)
    elif D < 0:
        sads.add(p)
check("4 number of critical points", len(crit) == 3, len(crit), 3)
check("4 local min", mins == SOL_4_min, mins, SOL_4_min)
check("4 no local max", maxs == {}, maxs, "none")
check("4 saddle points", sads == SOL_4_saddles, sads, SOL_4_saddles)
Dvals = {(c[x], c[y]): (H[0, 0].subs(c), H.det().subs(c)) for c in crit}
check("4 (f_xx, D) table", Dvals == {(0, -2): (27, 54), (-1, sp.Rational(-1, 2)): (-18, -72),
                                      (3, sp.Rational(23, 2)): (54, -216)}, Dvals, "27/54, -18/-72, 54/-216")

# ---------------- 5 ----------------
v = sp.Matrix([2, -1, 3])
gf = 2 * sp.sqrt(7) * v / v.norm()
check("5(a) grad f", all(sp.simplify(a - b) == 0 for a, b in zip(gf, SOL_5a)), list(gf), SOL_5a)
k = sp.symbols("k")
gg = k * sp.Matrix([1, 2, -1])
u = sp.Matrix([2, -1, 2]) / 3
ksol = sp.solve(sp.Eq(gg.dot(u), 4), k)[0]
gg = gg.subs(k, ksol)
check("5(b) grad g", tuple(gg) == SOL_5b, list(gg), SOL_5b)
gh = sp.sqrt(2) * gf + sp.Rational(1, 2) * gg
w = sp.Matrix([-1, 2, -2])
D5 = sp.simplify(gh.dot(w / w.norm()))
check("5(c) D_v h", D5 == SOL_5c, D5, SOL_5c)

# ---------------- 6 ----------------
f6 = x**3 + y**3 - sp.Rational(3, 2) * x**2 * y**2
g6 = x**2 + y**2 - 5
sols6 = sp.solve([sp.diff(f6, x) - lam * sp.diff(g6, x), sp.diff(f6, y) - lam * sp.diff(g6, y), g6], [x, y, lam], dict=True)
vals6 = [sp.nsimplify(sp.simplify(f6.subs(s))) for s in sols6]
mx6, mn6 = max(vals6, key=lambda q: float(q)), min(vals6, key=lambda q: float(q))
check("6 number of Lagrange points", len(sols6) == 8, len(sols6), 8)
check("6 max", sp.simplify(mx6 - SOL_6_max) == 0, mx6, SOL_6_max)
check("6 min", sp.simplify(mn6 - SOL_6_min) == 0, mn6, SOL_6_min)
dense = [float(f6.subs({x: mp.sqrt(5) * mp.cos(a), y: mp.sqrt(5) * mp.sin(a)})) for a in mp.linspace(0, 2 * mp.pi, 20001)]
check("6 dense parametric max/min", abs(max(dense) - float(SOL_6_max)) < 1e-6 and abs(min(dense) - float(SOL_6_min)) < 1e-6,
      f"{max(dense):.8f},{min(dense):.8f}", f"{float(SOL_6_max):.8f},{float(SOL_6_min):.8f}")

# ---------------- 7 ----------------
m = sp.symbols("m", positive=True)
x0, y0, z0, mu = sp.symbols("x0 y0 z0 mu")
F7 = x**2 + y**2 / 2 + z**2 / 2
gradF = sp.Matrix([sp.diff(F7, s) for s in (x, y, z)]).subs({x: x0, y: y0, z: z0})
eqs = list(gradF - mu * sp.Matrix([1, 1, m])) + [F7.subs({x: x0, y: y0, z: z0}) - 1, x0 + y0 + m * z0 - 2]
s7 = sp.solve(eqs, [x0, y0, z0, mu, m], dict=True)
ms = sorted({sp.simplify(s[m]) for s in s7})
check("7(a) m (positive)", ms == [SOL_7a], ms, SOL_7a)
# cross-check: plane n.x = d tangent to x^T A x = 1  <=>  d^2 = n^T A^{-1} n
check("7(a) support-function check", sp.simplify(1 + 2 + 2 * SOL_7a**2 - 4) == 0, "1+2+2m^2=4", "m^2=1/2")
kk = sp.symbols("kk")
G7 = x**2 + y**2 + kk - z
gradG = sp.Matrix([2 * x0, 2 * y0, -1])
s7b = sp.solve(list(gradG - mu * sp.Matrix([1, 1, SOL_7a])) + [z0 - x0**2 - y0**2 - kk, x0 + y0 + SOL_7a * z0 - 2],
               [x0, y0, z0, mu, kk], dict=True)
k7 = sp.simplify(s7b[0][kk])
check("7(b) k", sp.simplify(k7 - SOL_7b) == 0, k7, SOL_7b)
# sanity: plane and paraboloid meet in exactly one point (discriminant zero)
inter = sp.expand(sp.sqrt(2) * (2 - x - y) - (x**2 + y**2 + k7))   # plane z minus paraboloid z
crit7 = sp.solve([sp.diff(inter, x), sp.diff(inter, y)], [x, y], dict=True)[0]
gapmax = sp.simplify(inter.subs(crit7))
check("7(b) max of (plane - paraboloid) = 0 (touch at one point)", gapmax == 0, f"{gapmax} at {crit7}", "0")

# ---------------- 8 ----------------
M8 = sp.integrate(sp.integrate(r * sp.sin(th) * r, (r, 1, 2 * sp.cos(th))), (th, 0, sp.pi / 3))
My8 = sp.integrate(sp.integrate(r * sp.cos(th) * r * sp.sin(th) * r, (r, 1, 2 * sp.cos(th))), (th, 0, sp.pi / 3))
xbar = sp.simplify(My8 / M8)
check("8(a) mass (polar)", sp.simplify(M8 - SOL_8a) == 0, sp.simplify(M8), SOL_8a)
check("8(b) x-bar (polar)", sp.simplify(xbar - SOL_8b) == 0, xbar, SOL_8b)
# Cartesian numeric: x in [1/2, 2], y between sqrt(max(0,1-x^2)) and sqrt(2x-x^2)
def ylo(X):
    return mp.sqrt(1 - X**2) if X < 1 else mp.mpf(0)
M8n = mp.quad(lambda X: mp.quad(lambda Y: Y, [ylo(X), mp.sqrt(2 * X - X**2)]), [0.5, 1, 2])
My8n = mp.quad(lambda X: mp.quad(lambda Y: X * Y, [ylo(X), mp.sqrt(2 * X - X**2)]), [0.5, 1, 2])
check("8(a) mass (Cartesian numeric)", close(M8n, float(SOL_8a), 1e-12), mp.nstr(M8n, 15), sp.N(SOL_8a, 15))
check("8(b) x-bar (Cartesian numeric)", close(My8n / M8n, float(SOL_8b), 1e-12), mp.nstr(My8n / M8n, 15), sp.N(SOL_8b, 15))

# ---------------- 9 ----------------
# base disk x^2+(y-1)^2<=1, height = (x^2+y^2) - (-sqrt(4-x^2-y^2))
V9n = mp.quad(lambda X: mp.quad(lambda Y: X**2 + Y**2 + mp.sqrt(max(0, 4 - X**2 - Y**2)),
                                [1 - mp.sqrt(1 - X**2), 1 + mp.sqrt(1 - X**2)]), [-1, 0, 1])
inner = sp.integrate((r**2 + sp.sqrt(4 - r**2)) * r, (r, 0, 2 * sp.sin(th)))
V9s = sp.integrate(inner.subs(sp.sqrt(4 - 4 * sp.sin(th)**2), 2 * sp.cos(th)), (th, 0, sp.pi / 2)) + \
    sp.integrate(inner.subs(sp.sqrt(4 - 4 * sp.sin(th)**2), -2 * sp.cos(th)), (th, sp.pi / 2, sp.pi))
V9s = sp.simplify(V9s)
check("9 volume (polar, |cos| split)", sp.simplify(V9s - SOL_9) == 0, V9s, SOL_9)
check("9 volume (Cartesian numeric)", close(V9n, float(SOL_9), 1e-10), mp.nstr(V9n, 15), sp.N(SOL_9, 15))
wrong9 = sp.integrate(sp.Rational(8, 3) * (1 - sp.cos(th)**3) + 4 * sp.sin(th)**4, (th, 0, sp.pi))
check("9 dropping |cos| gives a different value", sp.simplify(wrong9 - SOL_9) != 0, wrong9, "!= answer")

# ---------------- 10 ----------------
def zint(s, a, b):
    # int_a^b sqrt(s+z^2) dz
    def F(Z):
        if s == 0:
            return Z * abs(Z) / 2
        return Z / 2 * mp.sqrt(s + Z**2) + s / 2 * mp.asinh(Z / mp.sqrt(s))
    return F(b) - F(a)

def g10(X, Y):
    s = X**2 + Y**2
    return zint(s, mp.sqrt(s), mp.sqrt(max(0, 4 - s)))

I10n = mp.quad(lambda X: mp.quad(lambda Y: g10(X, Y), [0, X]), [0, 1]) + \
    mp.quad(lambda X: mp.quad(lambda Y: g10(X, Y), [0, mp.sqrt(max(0, 2 - X**2))]), [1, mp.sqrt(2)])
I10s = sp.integrate(rho * rho**2 * sp.sin(ph), (rho, 0, 2), (th, 0, sp.pi / 4), (ph, 0, sp.pi / 4))
check("10 spherical symbolic", sp.simplify(I10s - SOL_10) == 0, sp.simplify(I10s), SOL_10)
check("10 original Cartesian numeric", close(I10n, float(SOL_10), 1e-10), mp.nstr(I10n, 15), sp.N(SOL_10, 15))
# region check with a test function: volume of the solid both ways
V10c = mp.quad(lambda X: mp.quad(lambda Y: mp.sqrt(max(0, 4 - X**2 - Y**2)) - mp.sqrt(X**2 + Y**2), [0, X]), [0, 1]) + \
    mp.quad(lambda X: mp.quad(lambda Y: mp.sqrt(max(0, 4 - X**2 - Y**2)) - mp.sqrt(X**2 + Y**2), [0, mp.sqrt(max(0, 2 - X**2))]), [1, mp.sqrt(2)])
V10s = sp.integrate(rho**2 * sp.sin(ph), (rho, 0, 2), (th, 0, sp.pi / 4), (ph, 0, sp.pi / 4))
check("10 region: volume Cartesian = spherical", close(V10c, float(V10s), 1e-10), mp.nstr(V10c, 15), sp.N(V10s, 15))

# ---------------- report ----------------
w0 = max(len(rw[0]) for rw in ROWS)
print(f"{'check'.ljust(w0)}  result  mine | solution")
for label, ok, mine, sol in ROWS:
    print(f"{label.ljust(w0)}  {'PASS' if ok else 'FAIL'}    {mine} | {sol}")
nf = sum(1 for rw in ROWS if not rw[1])
print(f"\n{len(ROWS)} checks, {len(ROWS) - nf} PASS, {nf} FAIL")
sys.exit(1 if nf else 0)
