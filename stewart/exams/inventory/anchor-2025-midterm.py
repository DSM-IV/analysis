#!/usr/bin/env python3
"""Independent anchor values for stewart/exams 2025-midterm (Calculus II MATH 162, Midterm, Fall 2025).

Every final answer is recomputed from the problem statement with sympy / mpmath and compared
with the constant written in solutions/2025-midterm.html (SOL_* below).
Reordering / coordinate-change problems are also checked with test integrands.
Run: python3 -I stewart/exams/inventory/anchor-2025-midterm.py   (exit 0 = all PASS)
"""
import random
import sys

import mpmath as mp
import sympy as sp

mp.mp.dps = 20
x, y, z, s, t, r, th, ph, rho, lam, mu = sp.symbols("x y z s t r theta phi rho lambda mu", real=True)

ROWS = []


def check(label, ok, mine, sol):
    ROWS.append((label, bool(ok), str(mine), str(sol)))


def close(a, b, tol=1e-8):
    return abs(complex(a) - complex(b)) < tol


# ---------------- Solution constants (copied from solutions/2025-midterm.html) ----------------
SOL_1_m = 2 * sp.sqrt(3) - 2 * sp.pi / 9
SOL_1_Mx = 11 * sp.sqrt(3) / 5
SOL_1_sin5 = 49 * sp.sqrt(3) / 80
SOL_1_center = (0, 99 * sp.sqrt(3) / (10 * (9 * sp.sqrt(3) - sp.pi)))
SOL_2a_min = {(2, 1): -30}
SOL_2a_max = {(-2, -1): 30}
SOL_2a_saddles = {(0, sp.sqrt(5)), (0, -sp.sqrt(5))}
# 2(b): int_0^{pi/3} int_1^{2 sec th} + int_{pi/3}^{pi/2} int_1^4   f(r cos, r sin) r dr dth
SOL_3a = 0
SOL_3b_paths = (0, sp.Rational(1, 3))  # y=0 -> 0, x=1+y^2 -> 1/3  => DNE
SOL_4 = sp.Rational(1, 240)
SOL_5 = 2
SOL_6_point = (1, 1, 1)
SOL_6a = 19 * sp.sqrt(13) / 26
SOL_6b = sp.Rational(17, 20)
SOL_7_max, SOL_7_min = sp.exp(sp.Rational(9, 4)), 1
SOL_8_max, SOL_8_min = sp.Rational(5, 4), 1
SOL_9 = sp.pi * (sp.E**4 - 1)
# 10(a): int_0^{pi/2} int_{acot(sin th)}^{pi/2} int_0^2 rho^2 sin ph  drho dph dth   (primary, phi-limits depend on theta)
#        = int_{pi/4}^{pi/2} int_{asin(cot ph)}^{pi/2} int_0^2 rho^2 sin ph  drho dth dph   (alternative)
SOL_10b = 2 * sp.pi / 3

# ---------------- 1. lamina between r=2 sin th and r=1, density r ----------------
lo1, hi1 = sp.pi / 6, 5 * sp.pi / 6
m1 = sp.simplify(sp.integrate(sp.integrate(r * r, (r, 1, 2 * sp.sin(th))), (th, lo1, hi1)))
Mx1 = sp.simplify(sp.integrate(sp.integrate(r * sp.sin(th) * r * r, (r, 1, 2 * sp.sin(th))), (th, lo1, hi1)))
My1 = sp.simplify(sp.integrate(sp.integrate(r * sp.cos(th) * r * r, (r, 1, 2 * sp.sin(th))), (th, lo1, hi1)))
sin5 = sp.integrate(sp.sin(th) ** 5, (th, lo1, hi1))
check("1 intersection 2sin(th)=1 at pi/6, 5pi/6", set(sp.solve(sp.Eq(2 * sp.sin(th), 1), th)) == {sp.pi / 6, 5 * sp.pi / 6}, "pi/6,5pi/6", "pi/6,5pi/6")
check("1 mass m", sp.simplify(m1 - SOL_1_m) == 0, m1, SOL_1_m)
check("1 int sin^5", sp.simplify(sin5 - SOL_1_sin5) == 0, sp.nsimplify(sin5), SOL_1_sin5)
check("1 M_x", sp.simplify(Mx1 - SOL_1_Mx) == 0, Mx1, SOL_1_Mx)
check("1 M_y = 0", My1 == 0, My1, 0)
ybar = sp.simplify(Mx1 / m1)
check("1 center of mass", My1 == SOL_1_center[0] and sp.simplify(ybar - SOL_1_center[1]) == 0, f"(0, {sp.N(ybar, 8)})", f"(0, {sp.N(SOL_1_center[1], 8)})")


# Cartesian numeric cross-check (independent of the polar set-up)
def ylo(xx):
    q = mp.sqrt(1 - xx**2)
    return max(q, 1 - q)


def cart(fn):
    a = mp.sqrt(3) / 2
    tot = 0
    for (p, q) in ((-1, -a), (-a, 0), (0, a), (a, 1)):
        tot += mp.quad(lambda xx: mp.quad(lambda yy: fn(xx, yy) * mp.sqrt(xx**2 + yy**2), [ylo(xx), 1 + mp.sqrt(1 - xx**2)]), [p, q])
    return tot


mN = cart(lambda a, b: 1)
MxN = cart(lambda a, b: b)
check("1 Cartesian numeric ybar", close(MxN / mN, sp.N(SOL_1_center[1], 20), 1e-7), mp.nstr(MxN / mN, 12), sp.N(SOL_1_center[1], 12))

# ---------------- 2(a). f = x^3+3xy^2-15x+y^3-15y ----------------
f2 = x**3 + 3 * x * y**2 - 15 * x + y**3 - 15 * y
crit = sp.solve([sp.diff(f2, x), sp.diff(f2, y)], [x, y], dict=True)
Dfun = sp.diff(f2, x, 2) * sp.diff(f2, y, 2) - sp.diff(f2, x, y) ** 2
mins, maxs, sads = {}, {}, set()
for c in crit:
    D = Dfun.subs(c)
    fxx = sp.diff(f2, x, 2).subs(c)
    pt = (c[x], c[y])
    if D > 0 and fxx > 0:
        mins[pt] = f2.subs(c)
    elif D > 0 and fxx < 0:
        maxs[pt] = f2.subs(c)
    elif D < 0:
        sads.add(pt)
check("2(a) number of critical points", len(crit) == 4, len(crit), 4)
check("2(a) local min", mins == SOL_2a_min, mins, SOL_2a_min)
check("2(a) local max", maxs == SOL_2a_max, maxs, SOL_2a_max)
check("2(a) saddle points", sads == SOL_2a_saddles, sads, SOL_2a_saddles)
check("2(a) D at (0,sqrt5) = -180, at (2,1) = 180", Dfun.subs({x: 0, y: sp.sqrt(5)}) == -180 and Dfun.subs({x: 2, y: 1}) == 180, "-180,180", "-180,180")


# ---------------- 2(b). Cartesian sum vs polar (test integrands) ----------------
def orig2b(g):
    a = mp.quad(lambda yy: mp.quad(lambda xx: g(xx, yy), [mp.sqrt(1 - yy**2), 2]), [0, 1])
    b = mp.quad(lambda yy: mp.quad(lambda xx: g(xx, yy), [0, 2]), [1, 2 * mp.sqrt(3)])
    c = mp.quad(lambda yy: mp.quad(lambda xx: g(xx, yy), [0, mp.sqrt(16 - yy**2)]), [2 * mp.sqrt(3), 4])
    return a + b + c


def polar2b(g):
    a = mp.quad(lambda T: mp.quad(lambda R: g(R * mp.cos(T), R * mp.sin(T)) * R, [1, 2 / mp.cos(T)]), [0, mp.pi / 3])
    b = mp.quad(lambda T: mp.quad(lambda R: g(R * mp.cos(T), R * mp.sin(T)) * R, [1, 4]), [mp.pi / 3, mp.pi / 2])
    return a + b


for name, g in (("1+x+y^2", lambda a, b: 1 + a + b**2), ("x^3+3xy^2-15x+y^3-15y", lambda a, b: a**3 + 3 * a * b**2 - 15 * a + b**3 - 15 * b), ("e^(x/3) y", lambda a, b: mp.e ** (a / 3) * b)):
    o, p = orig2b(g), polar2b(g)
    check(f"2(b) polar = Cartesian, f={name}", close(o, p, 1e-9), mp.nstr(o, 12), mp.nstr(p, 12))

# ---------------- 3(a) ----------------
f3a = x**3 * sp.sin(y) ** 2 / (x**2 + y**2) ** 2
random.seed(1)
worst = 0.0
for _ in range(4000):
    R = 10 ** random.uniform(-6, 0)
    T = random.uniform(0, 2 * 3.141592653589793)
    a, b = R * mp.cos(T), R * mp.sin(T)
    worst = max(worst, abs(a**3 * mp.sin(b) ** 2 / (a**2 + b**2) ** 2) / R)
check("3(a) |f| <= r on 4000 random points", worst <= 1, f"max|f|/r={mp.nstr(worst, 6)}", "<=1")
paths3a = [sp.limit(f3a.subs(y, k * x), x, 0) for k in (0, 1, -2, 5)] + [sp.limit(f3a.subs(x, y**2), y, 0)]
check("3(a) limit 0", all(v == 0 for v in paths3a) and SOL_3a == 0, paths3a, SOL_3a)

# ---------------- 3(b) ----------------
num3 = sp.sin(x * y**2) * sp.cos(y**2) - sp.cos(x * y**2) * sp.sin(y**2)
check("3(b) numerator = sin((x-1)y^2)", sp.simplify(sp.expand_trig(num3 - sp.sin((x - 1) * y**2))) == 0, "identity", "identity")
den3 = (x - 1) ** 2 + 2 * y**4
f3b = num3 / den3
L1 = sp.limit(f3b.subs(y, 0), x, 1)
L2 = sp.limit(f3b.subs(x, 1 + y**2), y, 0)
L3 = sp.limit(f3b.subs(x, 1 + 2 * y**2), y, 0)
check("3(b) path y=0", L1 == SOL_3b_paths[0], L1, SOL_3b_paths[0])
check("3(b) path x=1+y^2", L2 == SOL_3b_paths[1], L2, SOL_3b_paths[1])
check("3(b) DNE (x=1+2y^2 gives 1/3 too; x=1+k y^2 -> k/(k^2+2))", L1 != L2 and L3 == sp.Rational(1, 3), f"{L1},{L2},{L3}", "DNE")

# ---------------- 4. iiint_E 2xy dV ----------------
c4 = sp.cos(2 * th)
I4 = sp.integrate(sp.integrate(sp.integrate(r**2 * sp.sin(2 * th) * r, (z, r**4, r**2 * c4)), (r, 0, sp.sqrt(c4))), (th, 0, sp.pi / 4))
I4 = sp.simplify(I4)
check("4 cylindrical (sympy)", I4 == SOL_4, I4, SOL_4)


# Cartesian numeric: for fixed y, x^2 in [u-, u+] with u^2+(2y^2-1)u+y^4+y^2<=0, y<=1/(2 sqrt 2)
def x_range(yy):
    disc = mp.sqrt(max(1 - 8 * yy**2, 0))
    um, up = ((1 - 2 * yy**2) - disc) / 2, ((1 - 2 * yy**2) + disc) / 2
    return mp.sqrt(max(um, 0)), mp.sqrt(up)


def inner4(yy):
    a, b = x_range(yy)
    return mp.quad(lambda xx: 2 * xx * yy * ((xx**2 - yy**2) - (xx**2 + yy**2) ** 2), [a, b])


I4N = mp.quad(inner4, [0, 1 / (2 * mp.sqrt(2))])
check("4 Cartesian numeric", close(I4N, sp.N(SOL_4, 20), 1e-9), mp.nstr(I4N, 12), sp.N(SOL_4, 12))

# ---------------- 5. chain rule, second order ----------------
X, Y = t / s, s / t
fx, fy, fxx, fxy, fyy = sp.symbols("f_x f_y f_xx f_xy f_yy")
F = sp.Function("F")
zst = F(X, Y)
expr5 = s**2 * sp.diff(zst, s, 2) - t**2 * sp.diff(zst, t, 2)
expr5 = sp.simplify(expr5.doit())
# evaluate with concrete polynomials having f_x(1,1)=2, f_y(1,1)=1 and random second/third derivatives
ok5, vals5 = True, []
random.seed(5)
for _ in range(5):
    a, b, c, d, e = (sp.Rational(random.randint(-9, 9), random.randint(1, 5)) for _ in range(5))
    fpoly = 2 * x + y + a * (x - 1) ** 2 + b * (x - 1) * (y - 1) + c * (y - 1) ** 2 + d * (x - 1) ** 3 + e * x * y**3
    fpoly = fpoly - (sp.diff(fpoly, x).subs({x: 1, y: 1}) - 2) * x - (sp.diff(fpoly, y).subs({x: 1, y: 1}) - 1) * y
    zz = fpoly.subs({x: X, y: Y})
    v = (s**2 * sp.diff(zz, s, 2) - t**2 * sp.diff(zz, t, 2)).subs({s: 2, t: 2})
    vals5.append(sp.simplify(v))
    ok5 &= sp.simplify(v - SOL_5) == 0
check("5 value with 5 random test f (f_x=2, f_y=1 at (1,1))", ok5, vals5, SOL_5)
# general identity: s^2 z_ss - t^2 z_tt = 2x f_x - 2y f_y
g5 = sp.Function("g")
zz = g5(t / s, s / t)
lhs = s**2 * sp.diff(zz, s, 2) - t**2 * sp.diff(zz, t, 2)
u1, u2 = sp.symbols("u1 u2")
gx = sp.Subs(sp.Derivative(g5(u1, u2), u1), (u1, u2), (t / s, s / t))
gy = sp.Subs(sp.Derivative(g5(u1, u2), u2), (u1, u2), (t / s, s / t))
diff5 = sp.simplify((lhs - (2 * (t / s) * gx - 2 * (s / t) * gy)).doit())
check("5 identity s^2 z_ss - t^2 z_tt = 2x f_x - 2y f_y", diff5 == 0, diff5, 0)

# ---------------- 6. implicit z, tangent plane 2x+5y-2z=5 ----------------
z0 = sp.solve(sp.Eq(2 * 1 + 5 * 1 - 2 * z, 5), z)[0]
check("6 tangent point", (1, 1, z0) == SOL_6_point, (1, 1, z0), SOL_6_point)
# z_x = -F_x/F_z with grad F parallel to <2,5,-2>
zx, zy = sp.Rational(-2, -2), sp.Rational(-5, -2)
u6 = sp.Matrix([2, 3]) / sp.sqrt(13)
Du = sp.simplify(zx * u6[0] + zy * u6[1])
check("6(a) directional derivative", sp.simplify(Du - SOL_6a) == 0, Du, SOL_6a)
L6 = z0 + zx * sp.Rational(1, 10) + zy * sp.Rational(-1, 10)
check("6(b) linear approximation z(1.1,0.9)", L6 == SOL_6b, L6, SOL_6b)

# ---------------- 7. f = e^{(x-1/2)^2+y^2} on cardioid r <= 1+cos th ----------------
g7 = (x - sp.Rational(1, 2)) ** 2 + y**2
cp7 = sp.solve([sp.diff(sp.exp(g7), x), sp.diff(sp.exp(g7), y)], [x, y], dict=True)
check("7 interior critical point (1/2,0) only, inside D", cp7 == [{x: sp.Rational(1, 2), y: 0}] and sp.Rational(1, 4) <= sp.sqrt(sp.Rational(1, 4)) + sp.Rational(1, 2), cp7, "(1/2,0)")
gb = sp.simplify(g7.subs({x: (1 + sp.cos(th)) * sp.cos(th), y: (1 + sp.cos(th)) * sp.sin(th)}))
check("7 boundary g = 5/4 + cos th", sp.simplify(gb - (sp.Rational(5, 4) + sp.cos(th))) == 0, gb, "5/4+cos th")
# brute-force grid over D
import math

best_max, best_min = -1.0, 1e9
N7 = 400
for i in range(N7 + 1):
    T = -math.pi + 2 * math.pi * i / N7
    Rmax = 1 + math.cos(T)
    for j in range(N7 + 1):
        R = Rmax * j / N7
        a, b = R * math.cos(T), R * math.sin(T)
        val = math.exp((a - 0.5) ** 2 + b**2)
        best_max, best_min = max(best_max, val), min(best_min, val)
check("7 absolute max (grid)", close(best_max, sp.N(SOL_7_max, 20), 1e-6), mp.nstr(best_max, 10), sp.N(SOL_7_max, 10))
check("7 absolute min (grid, includes (1/2,0))", close(best_min, SOL_7_min, 1e-6), mp.nstr(best_min, 10), SOL_7_min)

# ---------------- 8. Lagrange with two constraints ----------------
f8 = x**2 + y**2 + z**2
g8 = x**2 + y**2 + z**4 - 1
h8 = y - x
eqs = [sp.diff(f8, v) - lam * sp.diff(g8, v) - mu * sp.diff(h8, v) for v in (x, y, z)] + [g8, h8]
sols8 = sp.solve(eqs, [x, y, z, lam, mu], dict=True)
vals8 = sorted({sp.nsimplify(f8.subs(c)) for c in sols8})
check("8 Lagrange candidate values", vals8 == [1, sp.Rational(5, 4)], f"{len(sols8)} pts, values {vals8}", "1, 5/4")
check("8 max / min", max(vals8) == SOL_8_max and min(vals8) == SOL_8_min, f"{max(vals8)}/{min(vals8)}", f"{SOL_8_max}/{SOL_8_min}")
# parametric check: f = 1 + w - w^2, w = z^2 in [0,1]
w = sp.symbols("w")
hw = 1 + w - w**2
check("8 reduction f=1+z^2-z^4 extrema", sp.Max(*[hw.subs(w, v) for v in (0, sp.Rational(1, 2), 1)]) == SOL_8_max, "5/4 at z^2=1/2", SOL_8_max)

# ---------------- 9. sum of two triple integrals ----------------
def orig9(G):
    a = mp.quad(lambda yy: mp.quad(lambda xx: mp.quad(lambda zz: G(xx, yy, zz), [2 * xx, 2]), [0, 1 - yy / 2]), [0, 2])
    b = mp.quad(lambda xx: mp.quad(lambda yy: mp.quad(lambda zz: G(xx, yy, zz), [2 * xx, 2]), [2 - 2 * xx, 2]), [0, 1])
    return a + b


def reord9(G):  # 0<=y<=2, 0<=z<=2, 0<=x<=z/2
    return mp.quad(lambda yy: mp.quad(lambda zz: mp.quad(lambda xx: G(xx, yy, zz), [0, zz / 2]), [0, 2]), [0, 2])


mp.mp.dps = 10
G9 = lambda a, b, c: 32 * mp.e ** (c**2) / (b**2 + 4)
v9 = orig9(G9)
check("9 original integral numeric", close(v9, sp.N(SOL_9, 20), 1e-5), mp.nstr(v9, 12), sp.N(SOL_9, 12))
for name, G in (("1+x+y^2+z", lambda a, b, c: 1 + a + b**2 + c),):
    o, p = orig9(G), reord9(G)
    check(f"9 reordered region = original, G={name}", close(o, p, 1e-7), mp.nstr(o, 12), mp.nstr(p, 12))
I9 = sp.integrate(sp.integrate(sp.integrate(32 * sp.exp(z**2) / (y**2 + 4), (x, 0, z / 2)), (z, 0, 2)), (y, 0, 2))
check("9 exact (sympy, dx dz dy)", sp.simplify(I9 - SOL_9) == 0, sp.simplify(I9), SOL_9)

# ---------------- 10. cylindrical -> spherical ----------------
mp.mp.dps = 10


def cyl10(G):
    def Rb(T):
        return 2 / mp.sqrt(mp.cos(T) ** 2 + 2 * mp.sin(T) ** 2)

    a = mp.quad(lambda T: mp.quad(lambda R: mp.quad(lambda Z: G(R * mp.cos(T), R * mp.sin(T), Z) * R, [0, R * mp.sin(T)]), [0, Rb(T)]), [0, mp.pi / 2])
    b = mp.quad(lambda T: mp.quad(lambda R: mp.quad(lambda Z: G(R * mp.cos(T), R * mp.sin(T), Z) * R, [0, mp.sqrt(4 - R**2)]), [Rb(T), 2]), [0, mp.pi / 2])
    return a + b


def sph_phi_outer(G):  # SOL answer order: phi in [pi/4,pi/2], theta in [asin(cot phi), pi/2], rho in [0,2]
    def cart(P, T, Rr):
        return Rr * mp.sin(P) * mp.cos(T), Rr * mp.sin(P) * mp.sin(T), Rr * mp.cos(P)

    return mp.quad(lambda P: mp.quad(lambda T: mp.quad(lambda Rr: G(*cart(P, T, Rr)) * Rr**2 * mp.sin(P), [0, 2]), [mp.asin(mp.cot(P)), mp.pi / 2]), [mp.pi / 4, mp.pi / 2])


def sph_theta_outer(G):  # theta in [0,pi/2], phi in [acot(sin theta), pi/2]
    def cart(P, T, Rr):
        return Rr * mp.sin(P) * mp.cos(T), Rr * mp.sin(P) * mp.sin(T), Rr * mp.cos(P)

    return mp.quad(lambda T: mp.quad(lambda P: mp.quad(lambda Rr: G(*cart(P, T, Rr)) * Rr**2 * mp.sin(P), [0, 2]), [mp.acot(mp.sin(T)), mp.pi / 2]), [0, mp.pi / 2])


one = lambda a, b, c: 1
vc = cyl10(one)
check("10(b) value (cylindrical numeric)", close(vc, sp.N(SOL_10b, 20), 1e-6), mp.nstr(vc, 12), sp.N(SOL_10b, 12))
s2v = sph_theta_outer(one)
check("10(a) volume: spherical (theta outer, drho dphi dtheta) = cylindrical", close(vc, s2v, 1e-6), mp.nstr(vc, 10), mp.nstr(s2v, 10))
Gt = lambda a, b, c: 1 + a + b**2 + c
c1, s1, s2 = cyl10(Gt), sph_phi_outer(Gt), sph_theta_outer(Gt)
check("10(a) spherical (theta outer, drho dphi dtheta) = cylindrical, G=1+x+y^2+z", close(c1, s2, 1e-6), mp.nstr(c1, 10), mp.nstr(s2, 10))
check("10(a) spherical (phi outer, drho dtheta dphi) = cylindrical, G=1+x+y^2+z", close(c1, s1, 1e-6), mp.nstr(c1, 10), mp.nstr(s1, 10))
I10 = sp.integrate(sp.Rational(8, 3) * sp.sin(ph) * sp.acos(sp.cot(ph)), (ph, sp.pi / 4, sp.pi / 2))
check("10(b) (8/3) int sin(phi) acos(cot phi) dphi", close(sp.N(I10, 20), sp.N(SOL_10b, 20), 1e-10), sp.N(I10, 12), SOL_10b)
# solution route (theta outer): cos(acot(sin th)) = sin th / sqrt(1+sin^2 th); u = cos th
cosacot = sp.cos(sp.acot(sp.sin(th))) - sp.sin(th) / sp.sqrt(1 + sp.sin(th) ** 2)
check("10(b) cos(acot(sin th)) = sin th/sqrt(1+sin^2 th) on (0,pi/2)", all(abs(sp.N(cosacot.subs(th, v))) < 1e-12 for v in (0.1, 0.7, 1.2, 1.5)), "identity", "identity")
inner10 = sp.integrate(1 / sp.sqrt(2 - w**2), (w, 0, 1))
check("10(b) int_0^1 du/sqrt(2-u^2) = pi/4", sp.simplify(inner10 - sp.pi / 4) == 0, inner10, "pi/4")
check("10(b) (8/3)(pi/4) = SOL", sp.Rational(8, 3) * inner10 == SOL_10b, sp.Rational(8, 3) * inner10, SOL_10b)

# ---------------- report ----------------
w1 = max(len(rw[0]) for rw in ROWS)
for label, ok, mine, sol in ROWS:
    print(f"{'PASS' if ok else 'FAIL'}  {label.ljust(w1)}  mine={mine}  sol={sol}")
n_fail = sum(1 for rw in ROWS if not rw[1])
print(f"\n{len(ROWS)} checks, {len(ROWS) - n_fail} PASS, {n_fail} FAIL")
sys.exit(1 if n_fail else 0)
