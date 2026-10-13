#!/usr/bin/env python3
"""Independent anchor values for stewart/exams 2024-midterm (Calculus II midterm, Fall 2024).

Every final answer is recomputed from the problem statement with sympy / mpmath and compared
with the constant written in solutions/2024-midterm.html (SOL_* below).
Coordinate-change / order-reversal problems are also checked with a test integrand
(1 + x + y^2 + z) to make sure the converted region is the original region.
Run: python3 -I stewart/exams/inventory/anchor-2024-midterm.py   (exit 0 = all PASS)
"""
import random
import sys

import mpmath as mp
import sympy as sp

mp.mp.dps = 20
x, y, z, t, r, th, ph, rho, lam = sp.symbols("x y z t r theta phi rho lambda", real=True)

ROWS = []


def check(label, ok, mine, sol):
    ROWS.append((label, bool(ok), str(mine), str(sol)))


def close(a, b, tol=1e-8):
    return abs(complex(a) - complex(b)) < tol


# ---------------- Solution constants (copied from solutions/2024-midterm.html) ----------------
SOL_1a = {(0, 0): ("saddle", 0), (1, 2): ("min", -3), (-4, -8): ("min", -128)}
SOL_1a_D = {(0, 0): -64, (1, 2): 80, (-4, -8): 320}
SOL_1b = (sp.Rational(1, 2), sp.Rational(3, 4))
SOL_2a = sp.log(2) / 3
SOL_2b = sp.Rational(1, 40)
SOL_3a = 0
SOL_3b_paths = {"y=x": 0, "y=2x": sp.Rational(-1, 17)}
SOL_4 = sp.sqrt(3) / 2
SOL_5a = 0
SOL_5b = 46
SOL_6 = 9 * sp.pi / 4 + 2
SOL_6_parts = (2 * sp.pi, 3 * sp.pi / 2, 5 * sp.pi / 4 - 2)   # D1, D2, D1∩D2
SOL_7 = -1
SOL_8 = 15 * sp.pi / 2
SOL_9 = sp.pi / 18 + 7 * sp.sqrt(3) / 36
SOL_9_first_sector = 7 * sp.sqrt(3) / 72
SOL_10 = sp.pi / 420

# ---------------- 1(a) critical points ----------------
f1 = x**4 + 4 * x**3 + 2 * y**2 - 8 * x * y
crit = sp.solve([sp.diff(f1, x), sp.diff(f1, y)], [x, y], dict=True)
crit = {(c[x], c[y]) for c in crit}
check("1(a) critical point set", crit == set(SOL_1a), sorted(crit), sorted(SOL_1a))
for (a0, b0), (kind, val) in SOL_1a.items():
    fxx = sp.diff(f1, x, 2).subs({x: a0, y: b0})
    D = (sp.diff(f1, x, 2) * sp.diff(f1, y, 2) - sp.diff(f1, x, y) ** 2).subs({x: a0, y: b0})
    mykind = "saddle" if D < 0 else ("min" if fxx > 0 else "max")
    fv = f1.subs({x: a0, y: b0})
    check(f"1(a) D at {(a0, b0)}", D == SOL_1a_D[(a0, b0)], D, SOL_1a_D[(a0, b0)])
    check(f"1(a) class/value at {(a0, b0)}", (mykind, fv) == (kind, val), (mykind, fv), (kind, val))

# ---------------- 1(b) implicit derivatives ----------------
F = x * z + y * sp.exp(x * y**2 - z) - 2 * z**2
pt = {x: 1, y: 1, z: 1}
check("1(b) (1,1,1) on surface", sp.simplify(F.subs(pt)) == 0, F.subs(pt), 0)
zx = sp.simplify((-sp.diff(F, x) / sp.diff(F, z)).subs(pt))
zy = sp.simplify((-sp.diff(F, y) / sp.diff(F, z)).subs(pt))
check("1(b) dz/dx, dz/dy", (zx, zy) == SOL_1b, (zx, zy), SOL_1b)

# ---------------- 2(a) original order, numerically ----------------
orig2a = mp.quad(lambda yy: mp.quad(lambda xx: 1 / (xx**3 + 1), [mp.sqrt(yy), 1]), [0, 1])
check("2(a) original order numeric", close(orig2a, sp.N(SOL_2a, 20)), mp.nstr(orig2a, 12), SOL_2a)
# region check with test function: int_0^1 int_sqrt(y)^1 h dx dy  vs  int_0^1 int_0^{x^2} h dy dx
h2 = lambda xx, yy: 1 + xx + yy**2
A = mp.quad(lambda yy: mp.quad(lambda xx: h2(xx, yy), [mp.sqrt(yy), 1]), [0, 1])
B = mp.quad(lambda xx: mp.quad(lambda yy: h2(xx, yy), [0, xx**2]), [0, 1])
check("2(a) reversed region (test fn)", close(A, B), mp.nstr(A, 12), mp.nstr(B, 12))
# the inner antiderivative IS elementary (partial fractions) -- the solution must not claim otherwise
anti = sp.integrate(1 / (x**3 + 1), x)
check("2(a) 1/(x^3+1) has elementary antiderivative", not anti.has(sp.Integral), anti, "elementary")

# ---------------- 2(b) triple integral ----------------
# E: between cylinders y=x^2 (below) and y=x (above) for 0<=x<=1, and 0<=z<=y
I2b = sp.integrate(x * y, (z, 0, y), (y, x**2, x), (x, 0, 1))
check("2(b) iiint xy dV", I2b == SOL_2b, I2b, SOL_2b)
# brute-force numeric with indicator over the bounding box [0,1]x[0,1]x[0,1]
num2b = mp.quad(lambda xx: mp.quad(lambda yy: xx * yy * yy, [xx**2, xx]), [0, 1])
check("2(b) numeric", close(num2b, sp.N(SOL_2b)), mp.nstr(num2b, 12), SOL_2b)

# ---------------- 3(a) ----------------
f3a = (x - x * sp.cos(y)) / (x**2 + y**2)
vals = []
random.seed(1)
for _ in range(200):
    rr = 10 ** random.uniform(-6, -2)
    a0 = random.uniform(0, 2 * 3.14159)
    xx, yy = rr * mp.cos(a0), rr * mp.sin(a0)
    v = (xx - xx * mp.cos(yy)) / (xx**2 + yy**2)
    vals.append(abs(v) / rr)          # |f| / r should stay bounded (<= 1/2)
check("3(a) |f| <= r/2 near 0 (so limit 0)", max(vals) <= 0.5 + 1e-12, mp.nstr(max(vals), 6), SOL_3a)
check("3(a) bound 1-cos y <= y^2/2", sp.limit((1 - sp.cos(y)) / y**2, y, 0) == sp.Rational(1, 2), "1/2", "ok")

# ---------------- 3(b) DNE ----------------
f3b = (x * sp.sin(y) - y * sp.sin(x)) / (x**4 + y**4)
L1 = sp.limit(f3b.subs(y, x), x, 0)
L2 = sp.limit(f3b.subs(y, 2 * x), x, 0)
check("3(b) path y=x", L1 == SOL_3b_paths["y=x"], L1, SOL_3b_paths["y=x"])
check("3(b) path y=2x", L2 == SOL_3b_paths["y=2x"], L2, SOL_3b_paths["y=2x"])
k = sp.symbols("k", real=True)
Lk = sp.simplify(sp.limit(f3b.subs(y, k * x), x, 0))
check("3(b) general y=kx -> k(1-k^2)/(6(1+k^4))", sp.simplify(Lk - k * (1 - k**2) / (6 * (1 + k**4))) == 0, Lk, "DNE")

# ---------------- 4 Lagrange ----------------
a, b, c = sp.symbols("a b c", positive=True)
sols4 = sp.solve([b * c - 2 * lam * a, a * c - 2 * lam * b, a * b - 2 * lam * c, a**2 + b**2 + c**2 - 1],
                 [a, b, c, lam], dict=True)
Vs = {sp.nsimplify(1 / (6 * s[a] * s[b] * s[c])) for s in sols4}
check("4 Lagrange candidates", Vs == {SOL_4}, Vs, SOL_4)
random.seed(4)
best = 1e9
for _ in range(20000):
    u = [abs(random.gauss(0, 1)) + 1e-12 for _ in range(3)]
    n = sum(q * q for q in u) ** 0.5
    best = min(best, 1 / (6 * (u[0] / n) * (u[1] / n) * (u[2] / n)))
check("4 random search min V >= sqrt3/2", best >= float(SOL_4) - 1e-9 and best < float(SOL_4) + 0.05,
      round(best, 6), sp.N(SOL_4, 8))
# tetrahedron volume formula check: integrate directly for a=b=c=1/sqrt3
a0 = 1 / sp.sqrt(3)
Vdir = sp.integrate(1, (z, 0, (1 - a0 * x - a0 * y) / a0), (y, 0, (1 - a0 * x) / a0), (x, 0, 1 / a0))
check("4 direct volume at a=b=c=1/sqrt3", sp.simplify(Vdir - SOL_4) == 0, sp.simplify(Vdir), SOL_4)

# ---------------- 5 homogeneous function ----------------
fF = sp.Function("f")
g5 = x**3 * fF(y / x, z / x)
expr5 = sp.simplify(x * sp.diff(g5, x) + y * sp.diff(g5, y) + z * sp.diff(g5, z) - 3 * g5)
check("5(a) xg_x+yg_y+zg_z-3g", expr5 == SOL_5a, expr5, SOL_5a)
# 5(b): linear approximation with unknown f_u=p, f_v=q at (1,2), f(1,2)=5
p, q = sp.symbols("p q")
u_, v_ = sp.symbols("u v")
fl = 5 + p * (u_ - 1) + q * (v_ - 2)                     # any f with these first-order data
g5b = x**3 * fl.subs({u_: y / x, v_: z / x})
P0 = {x: 2, y: 2, z: 4}
L5 = g5b.subs(P0) + sum(sp.diff(g5b, s).subs(P0) * d for s, d in
                        ((x, sp.Rational(1, 10)), (y, sp.Rational(1, 10)), (z, sp.Rational(2, 10))))
L5 = sp.simplify(L5)
check("5(b) linear approx (independent of f_u,f_v)", L5 == SOL_5b, L5, SOL_5b)

# ---------------- 6 union of disks ----------------
I_D1 = sp.integrate(r**3, (r, 0, sp.sqrt(2)), (th, 0, 2 * sp.pi))
I_D2 = sp.integrate(r**3, (r, 0, 2 * sp.cos(th)), (th, -sp.pi / 2, sp.pi / 2))
I_cap = (sp.integrate(r**3, (r, 0, sp.sqrt(2)), (th, -sp.pi / 4, sp.pi / 4))
         + 2 * sp.integrate(r**3, (r, 0, 2 * sp.cos(th)), (th, sp.pi / 4, sp.pi / 2)))
I6 = sp.simplify(I_D1 + I_D2 - I_cap)
check("6 inclusion-exclusion", sp.simplify(I6 - SOL_6) == 0, I6, SOL_6)
check("6 parts D1,D2,cap", all(sp.simplify(m - s) == 0 for m, s in zip((I_D1, I_D2, I_cap), SOL_6_parts)),
      (I_D1, I_D2, sp.simplify(I_cap)), SOL_6_parts)


def Y6(xx):
    ys = [0]
    if xx * xx <= 2:
        ys.append(mp.sqrt(2 - xx * xx))
    if 0 <= xx <= 2:
        ys.append(mp.sqrt(max(0, 1 - (xx - 1) ** 2)))
    return max(ys)


num6 = mp.quad(lambda xx: 2 * (xx * xx * Y6(xx) + Y6(xx) ** 3 / 3), [-mp.sqrt(2), 0, 1, mp.sqrt(2), 2])
check("6 Cartesian numeric", close(num6, sp.N(SOL_6, 20), 1e-7), mp.nstr(num6, 12), sp.N(SOL_6, 12))
# solution's polar split, with test function 1 + x + y^2
hp = lambda rr, tt: (1 + rr * mp.cos(tt) + (rr * mp.sin(tt)) ** 2) * rr
split6 = (mp.quad(lambda tt: mp.quad(lambda rr: hp(rr, tt), [0, 2 * mp.cos(tt)]), [-mp.pi / 4, mp.pi / 4])
          + mp.quad(lambda tt: mp.quad(lambda rr: hp(rr, tt), [0, mp.sqrt(2)]), [mp.pi / 4, 7 * mp.pi / 4]))
cart6 = mp.quad(lambda xx: mp.quad(lambda yy: 1 + xx + yy * yy, [-Y6(xx), Y6(xx)]), [-mp.sqrt(2), 0, 1, mp.sqrt(2), 2])
check("6 polar split region (test fn)", close(split6, cart6, 1e-7), mp.nstr(split6, 12), mp.nstr(cart6, 12))

# ---------------- 7 second directional derivative ----------------
# concrete f with f(0,0)=3, D_u f=3sqrt2, D_u^2 f=3 (u=(1,1)/sqrt2), and a generic symbolic check
f7 = 3 + 3 * (x + y) + sp.Rational(3, 4) * (x + y) ** 2 + 7 * (x - y) ** 2
along = lambda e: e.subs({x: t / sp.sqrt(2), y: t / sp.sqrt(2)})
assert sp.simplify(along(f7).subs(t, 0)) == 3
assert sp.simplify(sp.diff(along(f7), t).subs(t, 0) - 3 * sp.sqrt(2)) == 0
assert sp.simplify(sp.diff(along(f7), t, 2).subs(t, 0)) == 3
D2g = sp.simplify(sp.diff(along(sp.log(f7)), t, 2).subs(t, 0))
check("7 D_u^2 g (concrete f)", D2g == SOL_7, D2g, SOL_7)
F0, F1, F2 = sp.symbols("F0 F1 F2")
hgen = sp.Function("h")(t)
formula = sp.diff(sp.log(hgen), t, 2).subs({sp.Derivative(hgen, (t, 2)): F2}).subs(
    {sp.Derivative(hgen, t): F1}).subs(hgen, F0)
check("7 general formula (F0F2-F1^2)/F0^2", sp.simplify(formula - (F0 * F2 - F1**2) / F0**2) == 0, formula, "ok")

# ---------------- 8 cylindrical -> spherical ----------------
cyl8 = (sp.integrate(z * r, (z, 1, 2), (r, 0, sp.sqrt(3)), (th, 0, 2 * sp.pi))
        + sp.integrate(z * r, (z, r / sp.sqrt(3), 2), (r, sp.sqrt(3), 2 * sp.sqrt(3)), (th, 0, 2 * sp.pi))
        - sp.integrate(z * r, (z, 1, 2), (r, 0, 1), (th, 0, 2 * sp.pi))
        - sp.integrate(z * r, (z, r, 2), (r, 1, 2), (th, 0, 2 * sp.pi)))
cyl8 = sp.simplify(cyl8)
check("8 original cylindrical value", sp.simplify(cyl8 - SOL_8) == 0, cyl8, SOL_8)
sph8 = sp.integrate(rho * sp.cos(ph) * rho**2 * sp.sin(ph), (rho, 1 / sp.cos(ph), 2 / sp.cos(ph)),
                    (th, 0, 2 * sp.pi), (ph, sp.pi / 4, sp.pi / 3))
check("8 spherical value", sp.simplify(sph8 - SOL_8) == 0, sp.simplify(sph8), SOL_8)


# region check with test function H = 1 + x + y^2 + z (theta-dependent, so the full 3-D region is tested)
def H(xx, yy, zz):
    return 1 + xx + yy * yy + zz


def cyl_piece(rlo, rhi, zlo, zhi):
    return mp.quad(lambda tt: mp.quad(lambda rr: mp.quad(
        lambda zz: H(rr * mp.cos(tt), rr * mp.sin(tt), zz) * rr, [zlo(rr), zhi(rr)]), [rlo, rhi]), [0, 2 * mp.pi])


mp.mp.dps = 12
one, two = (lambda rr: 1), (lambda rr: 2)
cyl_test = (cyl_piece(0, mp.sqrt(3), one, two) + cyl_piece(mp.sqrt(3), 2 * mp.sqrt(3), lambda rr: rr / mp.sqrt(3), two)
            - cyl_piece(0, 1, one, two) - cyl_piece(1, 2, lambda rr: rr, two))
sph_test = mp.quad(lambda pp: mp.quad(lambda tt: mp.quad(
    lambda RR: H(RR * mp.sin(pp) * mp.cos(tt), RR * mp.sin(pp) * mp.sin(tt), RR * mp.cos(pp)) * RR**2 * mp.sin(pp),
    [1 / mp.cos(pp), 2 / mp.cos(pp)]), [0, 2 * mp.pi]), [mp.pi / 4, mp.pi / 3])
check("8 region identification (test fn)", close(cyl_test, sph_test, 1e-6), mp.nstr(cyl_test, 10), mp.nstr(sph_test, 10))
mp.mp.dps = 20

# ---------------- 9 volume above paraboloid in the unit box ----------------
R0 = 2 / sp.sqrt(3)
cart9 = sp.integrate(1 - sp.Rational(3, 4) * (x**2 + y**2), (y, 0, 1), (x, 0, sp.sqrt(R0**2 - 1)))
cart9 += sp.integrate(1 - sp.Rational(3, 4) * (x**2 + y**2), (y, 0, sp.sqrt(R0**2 - x**2)), (x, sp.sqrt(R0**2 - 1), 1))
cart9 = sp.simplify(cart9)
check("9 Cartesian exact", sp.simplify(cart9 - SOL_9) == 0 or close(sp.N(cart9, 20), sp.N(SOL_9, 20)),
      sp.N(cart9, 12), SOL_9)
brute9 = mp.quad(lambda xx: mp.quad(lambda yy: max(0, 1 - 0.75 * (xx * xx + yy * yy)), [0, 0.5, 1]), [0, 0.5, 1])
check("9 brute max(0,height) numeric", close(brute9, sp.N(SOL_9, 20), 1e-6), mp.nstr(brute9, 10), sp.N(SOL_9, 10))
inner = lambda R: R**2 / 2 - 3 * R**4 / 16
first9 = sp.integrate(inner(1 / sp.cos(th)), (th, 0, sp.pi / 6))
check("9 first sector", sp.simplify(first9 - SOL_9_first_sector) == 0, sp.simplify(first9), SOL_9_first_sector)
# three angular pieces vs Cartesian with test function 1 + x + y^2 (not symmetric in x<->y)
h9 = lambda xx, yy: 1 + xx + yy * yy
pol9 = (mp.quad(lambda tt: mp.quad(lambda rr: h9(rr * mp.cos(tt), rr * mp.sin(tt)) * rr, [0, 1 / mp.cos(tt)]), [0, mp.pi / 6])
        + mp.quad(lambda tt: mp.quad(lambda rr: h9(rr * mp.cos(tt), rr * mp.sin(tt)) * rr, [0, 2 / mp.sqrt(3)]), [mp.pi / 6, mp.pi / 3])
        + mp.quad(lambda tt: mp.quad(lambda rr: h9(rr * mp.cos(tt), rr * mp.sin(tt)) * rr, [0, 1 / mp.sin(tt)]), [mp.pi / 3, mp.pi / 2]))
c9 = mp.sqrt(mp.mpf(4) / 3 - 1)
car9 = (mp.quad(lambda xx: mp.quad(lambda yy: h9(xx, yy), [0, 1]), [0, c9])
        + mp.quad(lambda xx: mp.quad(lambda yy: h9(xx, yy), [0, mp.sqrt(mp.mpf(4) / 3 - xx * xx)]), [c9, 1]))
check("9 three angular pieces (test fn)", close(pol9, car9, 1e-8), mp.nstr(pol9, 12), mp.nstr(car9, 12))
check("9 whole-square value 1/2 (common mistake)",
      sp.integrate(1 - sp.Rational(3, 4) * (x**2 + y**2), (x, 0, 1), (y, 0, 1)) == sp.Rational(1, 2), "1/2", "1/2")

# ---------------- 10 quartic surface ----------------
I10 = sp.integrate(rho * sp.cos(ph) * rho**2 * sp.sin(ph), (rho, 0, sp.cos(ph) * sp.sin(ph) ** 2),
                   (th, 0, 2 * sp.pi), (ph, 0, sp.pi / 2))
check("10 spherical exact", sp.simplify(I10 - SOL_10) == 0, sp.simplify(I10), SOL_10)


# independent cylindrical numeric: region (r^2+z^2)^2 <= z r^2 ; for each r find z-interval via polyroots
def zint(rr):
    roots = mp.polyroots([1, 0, 2 * rr**2, -rr**2, rr**4], maxsteps=200, extraprec=60)
    re_ = sorted(mp.re(w) for w in roots if abs(mp.im(w)) < mp.mpf(10) ** -12 and mp.re(w) > 0)
    return (re_[0], re_[-1]) if len(re_) >= 2 else None


# r_max: max of rho sin(phi) = cos(phi) sin^3(phi)  -> at tan^2(phi)=3
rmax = mp.cos(mp.pi / 3) * mp.sin(mp.pi / 3) ** 3


def integrand10(rr):
    zi = zint(rr)
    if zi is None:
        return mp.mpf(0)
    return 2 * mp.pi * rr * (zi[1] ** 2 - zi[0] ** 2) / 2


mp.mp.dps = 25
cyl10 = mp.quad(integrand10, [mp.mpf(10) ** -8, rmax * 0.5, rmax * 0.9, rmax * 0.99, rmax])
check("10 cylindrical numeric", close(cyl10, sp.N(SOL_10, 25), 1e-6), mp.nstr(cyl10, 10), sp.N(SOL_10, 10))

# ---------------- report ----------------
w = max(len(rw[0]) for rw in ROWS)
nfail = 0
for label, ok, mine, sol in ROWS:
    nfail += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {label.ljust(w)}  mine={mine[:60]}  sol={sol[:60]}")
print(f"\n{len(ROWS)} checks, {len(ROWS) - nfail} PASS, {nfail} FAIL")
sys.exit(1 if nfail else 0)
