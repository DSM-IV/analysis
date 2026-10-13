#!/usr/bin/env python3
"""Independent anchor values for stewart/exams 2025-final (Calculus II MATH 162, Final, Fall 2025).

Every final answer is recomputed from the problem statement with sympy / mpmath and compared
with the constant written in solutions/2025-final.html (SOL_* below).
Change-of-variables / Stokes / Divergence problems are cross-checked numerically
(original integral vs. transformed integral, surface integral vs. line integral, etc.).
Run: python3 -I stewart/exams/inventory/anchor-2025-final.py   (exit 0 = all PASS)
"""
import math
import sys

import mpmath as mp
import sympy as sp

mp.mp.dps = 20
x, y, z, t, u, v, r, th, ph, w = sp.symbols("x y z t u v r theta phi w", real=True)

ROWS = []


def check(label, ok, mine, sol):
    ROWS.append((label, bool(ok), str(mine), str(sol)))


def close(a, b, tol=1e-7):
    return abs(complex(a) - complex(b)) < tol


def same(a, b):
    return sp.simplify(sp.nsimplify(a) - sp.nsimplify(b)) == 0 or close(sp.N(a, 30), sp.N(b, 30), 1e-12)


# ---------------- Solution constants (copied from solutions/2025-final.html) ----------------
SOL_1a = 2
SOL_1b_ccw = -24 * sp.pi          # counterclockwise (positive) orientation
SOL_1b_cw = 24 * sp.pi            # clockwise
SOL_2a = (2 * sp.sqrt(2) - 1) / 3
SOL_2b = 2 * sp.pi
SOL_3 = sp.Rational(2, 3) * sp.log(2) * (sp.exp(4) - sp.E)
SOL_3_jac = sp.Rational(2, 3) / v           # d(x,y)/d(u,v) with u = xy, v = y/sqrt(x)
SOL_4 = -sp.pi / 4 - 3 * sp.sqrt(3)
SOL_5 = sp.pi - 12
SOL_5_angular = sp.pi
SOL_5_xdy = -12
SOL_6 = 32 * sp.pi / 5
SOL_7 = sp.Rational(8, 3)
SOL_8 = -3 * sp.sqrt(2) * sp.pi / 16
SOL_9 = 8 * sp.pi
SOL_10a = sp.Rational(-5, 4)
SOL_10b = -12
SOL_10c = 12


def line_int(F, rr, a, b):
    """int_a^b F(r(t)) . r'(t) dt, symbolic F in x,y,z and r(t) list."""
    sub = {x: rr[0], y: rr[1], z: rr[2]}
    integrand = sum(sp.sympify(F[i]).subs(sub) * sp.diff(sp.sympify(rr[i]), t) for i in range(3))
    return integrand


def num_line(F, rr, a, b):
    integrand = line_int(F, rr, a, b)
    f = sp.lambdify(t, integrand, "mpmath")
    return mp.quad(f, [a, b])


# ---------------- 1(a) ----------------
F1 = [y + z, x + z, x + y]
segs = [([0, 0, 0], [1, 0, 1]), ([1, 0, 1], [0, 1, 2])]
val1a = 0
for P0, P1 in segs:
    rr = [P0[i] + t * (P1[i] - P0[i]) for i in range(3)]
    val1a += sp.integrate(line_int(F1, rr, 0, 1), (t, 0, 1))
pot1 = x * y + y * z + z * x
grad_ok = all(sp.simplify(sp.diff(pot1, var) - F1[i]) == 0 for i, var in enumerate((x, y, z)))
check("1(a) potential xy+yz+zx", grad_ok, "grad = F", "f = xy+yz+zx")
check("1(a) segment-by-segment value", same(val1a, SOL_1a), val1a, SOL_1a)

# ---------------- 1(b) ----------------
P1b = x**3 * sp.sin(x) + y**3
Q1b = sp.exp(y) * sp.cos(y) - x**3
rr = [2 * sp.cos(t), 2 * sp.sin(t), 0]
num1b = num_line([P1b, Q1b, 0], rr, 0, 2 * mp.pi)
green1b = sp.integrate(sp.integrate((sp.diff(Q1b, x) - sp.diff(P1b, y)).subs({x: r * sp.cos(th), y: r * sp.sin(th)}) * r, (r, 0, 2)), (th, 0, 2 * sp.pi))
check("1(b) ccw: direct parametrization", close(num1b, sp.N(SOL_1b_ccw)), sp.N(num1b, 12), SOL_1b_ccw)
check("1(b) ccw: Green", same(green1b, SOL_1b_ccw), green1b, SOL_1b_ccw)
check("1(b) cw = -(ccw)", same(-green1b, SOL_1b_cw), -green1b, SOL_1b_cw)

# ---------------- 2(a) ----------------
R2 = sp.Matrix([u * sp.cos(v), u * sp.sin(v), v])
n2 = R2.diff(u).cross(R2.diff(v))
mag2 = sp.sqrt(sp.simplify(n2.dot(n2)))
check("2(a) |r_u x r_v| = sqrt(1+u^2)", sp.simplify(mag2 - sp.sqrt(1 + u**2)) == 0, mag2, "sqrt(1+u^2)")
val2a = sp.integrate(sp.integrate(u * sp.cos(v) * sp.sqrt(1 + u**2), (u, 0, 1)), (v, 0, sp.pi / 2))
check("2(a) iint x dS", same(val2a, SOL_2a), sp.simplify(val2a), SOL_2a)

# ---------------- 2(b) ----------------
F2 = [y**2 + 2 * x, x**3 - 2 * y * z, z**2 - y]
div2 = sp.simplify(sum(sp.diff(F2[i], var) for i, var in enumerate((x, y, z))))
check("2(b) div F = 2", div2 == 2, div2, 2)
vol2 = sp.integrate(sp.integrate((r * sp.sin(th) + 1) * r, (r, 0, 1)), (th, 0, 2 * sp.pi))
check("2(b) volume = pi", same(vol2, sp.pi), vol2, "pi")
# direct flux through the three faces (outward) as an independent check
# side: r(th,z) = (cos th, sin th, z), 0<=z<=sin th + 1, outward n = (cos th, sin th, 0)
sub_side = {x: sp.cos(th), y: sp.sin(th)}
side = sp.integrate(sp.integrate((F2[0] * sp.cos(th) + F2[1] * sp.sin(th)).subs(sub_side), (z, 0, sp.sin(th) + 1)), (th, 0, 2 * sp.pi))
# bottom z=0, outward n = -k : -(z^2 - y) at z=0 = y
bottom = sp.integrate(sp.integrate((-(F2[2])).subs({z: 0, x: r * sp.cos(th), y: r * sp.sin(th)}) * r, (r, 0, 1)), (th, 0, 2 * sp.pi))
# top z = y+1, upward normal (-g_x, -g_y, 1) = (0, -1, 1)
top_int = (-F2[1] + F2[2]).subs(z, y + 1)
top = sp.integrate(sp.integrate(top_int.subs({x: r * sp.cos(th), y: r * sp.sin(th)}) * r, (r, 0, 1)), (th, 0, 2 * sp.pi))
flux2 = sp.simplify(side + bottom + top)
check("2(b) flux by Divergence Thm", same(div2 * vol2, SOL_2b), div2 * vol2, SOL_2b)
check("2(b) flux by direct faces", same(flux2, SOL_2b), flux2, SOL_2b)

# ---------------- 3 ----------------
# u = xy in [1,4], v = y/sqrt(x) in [1,2]  =>  x = (u/v)^(2/3), y = u^(1/3) v^(2/3)
u, v = sp.symbols("u v", positive=True)
SOL_3_jac = sp.Rational(2, 3) / v
xs = (u / v) ** sp.Rational(2, 3)
ys = u ** sp.Rational(1, 3) * v ** sp.Rational(2, 3)
check("3 inverse map: xy = u", sp.simplify(xs * ys - u) == 0, sp.simplify(xs * ys), "u")
check("3 inverse map: y/sqrt(x) = v", sp.simplify(sp.powsimp(ys / sp.sqrt(xs), force=True) - v) == 0, "v", "v")
J3 = sp.simplify(sp.Matrix([[sp.diff(xs, u), sp.diff(xs, v)], [sp.diff(ys, u), sp.diff(ys, v)]]).det())
check("3 d(x,y)/d(u,v) = 2/(3v)", sp.simplify(J3 - SOL_3_jac) == 0, J3, SOL_3_jac)
Jf = sp.Matrix([[sp.diff(x * y, x), sp.diff(x * y, y)], [sp.diff(y / sp.sqrt(x), x), sp.diff(y / sp.sqrt(x), y)]]).det()
check("3 d(u,v)/d(x,y) = 3y/(2 sqrt x) = 3v/2", sp.simplify(Jf - sp.Rational(3, 2) * y / sp.sqrt(x)) == 0, sp.simplify(Jf), "3y/(2sqrt x)")
val3 = sp.integrate(sp.integrate(sp.exp(u) * sp.Rational(2, 3) / v, (u, 1, 4)), (v, 1, 2))
check("3 transformed integral", same(val3, SOL_3), sp.simplify(val3), SOL_3)
# original integral in xy: region between y=sqrt x, y=2sqrt x, y=1/x, y=4/x.  Use y as outer variable:
# for fixed y, x ranges over max(y^2/4, 1/y) <= x <= min(y^2, 4/y)
def inner3(yy, g):
    lo = max(yy**2 / 4, 1 / yy)
    hi = min(yy**2, 4 / yy)
    if hi <= lo:
        return mp.mpf(0)
    return mp.quad(lambda xx: g(xx, yy), [lo, hi])


# corner y-values: (u,v)=(1,1)->1, (1,2)->2^(2/3), (4,1)->4^(1/3), (4,2)->2^(4/3)
ybreaks = sorted(set([1.0, 2 ** (2 / 3), 4 ** (1 / 3), 2 ** (4 / 3)]))
orig3 = mp.quad(lambda yy: inner3(yy, lambda xx, Y: mp.exp(xx * Y)), ybreaks)
check("3 original xy-integral (numeric) = transformed", close(orig3, sp.N(SOL_3), 1e-6), mp.nstr(orig3, 12), sp.N(SOL_3, 12))
# test integrand 1 + x + y^2 : original vs transformed
g = lambda xx, Y: 1 + xx + Y**2
orig3t = mp.quad(lambda yy: inner3(yy, g), ybreaks)
gt = sp.lambdify((u, v), (1 + xs + ys**2) * sp.Rational(2, 3) / v, "mpmath")
tr3t = mp.quad(gt, [1, 4], [1, 2])
check("3 test integrand 1+x+y^2: xy vs uv", close(orig3t, tr3t, 1e-6), mp.nstr(orig3t, 12), mp.nstr(tr3t, 12))

# ---------------- 4 ----------------
F4 = [y / (1 + x**2 * y**2), x / (1 + x**2 * y**2) + z * sp.sec(y * z / 3) ** 2, y * sp.sec(y * z / 3) ** 2]
f4 = sp.atan(x * y) + 3 * sp.tan(y * z / 3)
grad4 = all(sp.simplify(sp.diff(f4, var) - F4[i]) == 0 for i, var in enumerate((x, y, z)))
check("4 potential atan(xy)+3tan(yz/3)", grad4, "grad f = F", "f")
rr4 = [t / 3 * sp.cos(sp.pi * t / 3), t / 3 * sp.sin(sp.pi * t / 6), sp.pi * sp.cos(sp.pi * t)]
A4 = [c.subs(t, 0) for c in rr4]
B4 = [sp.simplify(c.subs(t, 3)) for c in rr4]
check("4 endpoints (0,0,pi) -> (-1,1,-pi)", A4 == [0, 0, sp.pi] and B4 == [-1, 1, -sp.pi], (A4, B4), "(0,0,pi),(-1,1,-pi)")
fts = f4.subs({x: B4[0], y: B4[1], z: B4[2]}) - f4.subs({x: A4[0], y: A4[1], z: A4[2]})
check("4 f(B) - f(A)", same(fts, SOL_4), sp.simplify(fts), SOL_4)
num4 = num_line(F4, rr4, 0, 3)
check("4 direct numeric line integral", close(num4, sp.N(SOL_4), 1e-8), mp.nstr(num4, 12), sp.N(SOL_4, 12))
# domain: |yz/3| along C stays below pi/2
yz3 = sp.lambdify(t, (rr4[1] * rr4[2] / 3), "math")
mx4 = max(abs(yz3(k * 3 / 20000)) for k in range(20001))
check("4 max |yz/3| on C < pi/2 (tan defined)", mx4 < math.pi / 2, round(mx4, 6), "< 1.5708 (bound pi/3=1.0472)")

# ---------------- 5 ----------------
P5 = y / (x**2 + y**2)
Q5 = x * (x**2 + y**2 - 1) / (x**2 + y**2)
pts = [(-1, 0), (-2, 2), (-2, 4), (-1, 3), (0, 4), (1, 3), (2, 4), (2, 2), (1, 0)]
tot5 = mp.mpf(0)
xdy = 0
ang = mp.mpf(0)
for (a1, b1), (a2, b2) in zip(pts[:-1], pts[1:]):
    rr = [a1 + t * (a2 - a1), b1 + t * (b2 - b1), 0]
    tot5 += num_line([P5, Q5, 0], rr, 0, 1)
    xdy += sp.integrate(line_int([0, x, 0], rr, 0, 1), (t, 0, 1))
    ang += num_line([y / (x**2 + y**2), -x / (x**2 + y**2), 0], rr, 0, 1)
check("5 Q_x - P_y != 0 (not conservative)", sp.simplify(sp.diff(Q5, x) - sp.diff(P5, y)) != 0, sp.simplify(sp.diff(Q5, x) - sp.diff(P5, y)), "nonzero")
check("5 split: F = <y,-x>/r^2 + <0,x>", sp.simplify(Q5 - (-x / (x**2 + y**2) + x)) == 0, "ok", "ok")
check("5 angular part = pi", close(ang, sp.N(SOL_5_angular)), mp.nstr(ang, 12), SOL_5_angular)
check("5 int x dy = -12", xdy == SOL_5_xdy, xdy, SOL_5_xdy)
check("5 total (numeric, segment by segment)", close(tot5, sp.N(SOL_5)), mp.nstr(tot5, 12), SOL_5)
# shoelace area of closed polygon E..M,E
poly = pts + [pts[0]]
area = sp.Rational(1, 2) * sum(poly[i][0] * poly[i + 1][1] - poly[i + 1][0] * poly[i][1] for i in range(len(pts)))
check("5 polygon signed area (E..M then M->E) = -12 (clockwise)", area == -12, area, -12)

# ---------------- 6 ----------------
rho6 = 1 - sp.cos(ph)
R6 = sp.Matrix([rho6 * sp.sin(ph) * sp.cos(th), rho6 * sp.sin(ph) * sp.sin(th), rho6 * sp.cos(ph)])
n6 = R6.diff(ph).cross(R6.diff(th))
mag6sq = sp.simplify(sp.expand(n6.dot(n6)))
target6 = 2 * (1 - sp.cos(ph)) ** 3 * sp.sin(ph) ** 2
check("6 |r_phi x r_theta|^2 = 2(1-cos)^3 sin^2", sp.simplify(mag6sq - target6) == 0, "2(1-cos phi)^3 sin^2 phi", "")
val6 = 2 * sp.pi * sp.sqrt(2) * sp.integrate(w ** sp.Rational(3, 2), (w, 0, 2))
check("6 surface area", same(val6, SOL_6), sp.simplify(val6), SOL_6)
f6 = sp.lambdify((ph, th), sp.sqrt(mag6sq), "mpmath")
num6 = mp.quad(f6, [0, mp.pi], [0, 2 * mp.pi])
check("6 numeric |r_phi x r_theta| integral", close(num6, sp.N(SOL_6), 1e-8), mp.nstr(num6, 12), sp.N(SOL_6, 12))

# ---------------- 7 ----------------
F7 = [sp.log(1 + y**2) - x * sp.sech(2 * z), y - 2 * sp.atan(x), sp.atan(sp.tanh(z))]
div7 = sum(sp.diff(F7[i], var) for i, var in enumerate((x, y, z)))
div7n = sp.lambdify(z, div7, "mpmath")
check("7 div F = 1", all(close(div7n(zz), 1, 1e-15) for zz in (0, 0.3, 0.77, 1.0, 2.5)), "1 (numeric)", 1)
check("7 div F = 1 (symbolic)", sp.simplify((div7 - 1).rewrite(sp.exp)) == 0, sp.simplify((div7).rewrite(sp.exp)), 1)
vol7 = sp.integrate(4 * (1 - z**2), (z, 0, 1))
check("7 volume (squares 4(1-z^2))", vol7 == SOL_7, vol7, SOL_7)
# numeric: z <= sqrt(1 - max(x^2, y^2)); 8 congruent pieces with 0 <= y <= x <= 1
vol7b = 8 * mp.quad(lambda xx: mp.quad(lambda yy: mp.sqrt(1 - max(xx * xx, yy * yy)), [0, xx]), [0, 1])
check("7 volume (numeric, z<=sqrt(1-max(x^2,y^2)))", close(vol7b, 8 / 3, 1e-6), mp.nstr(vol7b, 10), SOL_7)

# ---------------- 8 ----------------
F8 = [z * sp.exp(x) * sp.sin(y) + y * z, z * sp.exp(x) * sp.cos(y) + x * y**2, sp.exp(x) * sp.sin(y) + x * y]
rr8 = [sp.cos(t) / sp.sqrt(2), sp.sin(t), 1 - sp.cos(t) ** 2 / 2]
on8 = sp.simplify(rr8[2] - (rr8[0] ** 2 + rr8[1] ** 2)) == 0 and sp.simplify(rr8[2] - (1 - rr8[0] ** 2)) == 0
check("8(1) r(t) on both surfaces", on8, "ok", "x=cos t/sqrt2, y=sin t, z=1-cos^2 t/2")
# orientation: d/dt of polar angle of (x,y) at t=0 positive -> counterclockwise
ccw8 = sp.simplify((rr8[0] * sp.diff(rr8[1], t) - rr8[1] * sp.diff(rr8[0], t)).subs(t, 0)) > 0
check("8(1) t increasing is counterclockwise (from above)", bool(ccw8), "x y' - y x' > 0", "")
G8 = [y * z, x * y**2, x * y]
gpart = sp.integrate(sp.expand(line_int(G8, rr8, 0, 2 * sp.pi)), (t, 0, 2 * sp.pi))
check("8(2) non-gradient part = -3 sqrt2 pi/16", same(gpart, SOL_8), sp.simplify(gpart), SOL_8)
check("8(2) z e^x sin y is potential of the rest", all(sp.simplify(sp.diff(z * sp.exp(x) * sp.sin(y), var) - (F8[i] - G8[i])) == 0 for i, var in enumerate((x, y, z))), "ok", "")
num8 = num_line(F8, rr8, 0, 2 * mp.pi)
check("8(2) full numeric line integral", close(num8, sp.N(SOL_8), 1e-8), mp.nstr(num8, 12), sp.N(SOL_8, 12))
# Stokes cross-check: S = part of z = 1 - x^2 over 2x^2+y^2<=1, upward normal (2x, 0, 1)
curl8 = [sp.diff(G8[2], y) - sp.diff(G8[1], z), sp.diff(G8[0], z) - sp.diff(G8[2], x), sp.diff(G8[1], x) - sp.diff(G8[0], y)]
integrand8 = (curl8[0] * 2 * x + curl8[2]).subs(z, 1 - x**2)
st8 = sp.integrate(sp.integrate(integrand8, (y, -sp.sqrt(1 - 2 * x**2), sp.sqrt(1 - 2 * x**2))), (x, -1 / sp.sqrt(2), 1 / sp.sqrt(2)))
check("8(2) Stokes on z=1-x^2 (upward)", same(st8, SOL_8), sp.simplify(st8), SOL_8)

# ---------------- 9 ----------------
F9 = [x**2 * sp.sin(z), y**2, x * y + x**2 * sp.cos(z)]
curl9 = [sp.diff(F9[2], y) - sp.diff(F9[1], z), sp.diff(F9[0], z) - sp.diff(F9[2], x), sp.diff(F9[1], x) - sp.diff(F9[0], y)]
# (a) on the paraboloid itself, downward normal (2x, 2y, -1)
par = (curl9[0] * 2 * x + curl9[1] * 2 * y - curl9[2]).subs(z, x**2 + y**2)
parf = sp.lambdify((r, th), par.subs({x: -1 + r * sp.cos(th), y: r * sp.sin(th)}) * r, "mpmath")
num9a = mp.quad(parf, [0, 2], [0, 2 * mp.pi])
check("9 flux of curl on paraboloid (downward, numeric)", close(num9a, sp.N(SOL_9), 1e-8), mp.nstr(num9a, 12), SOL_9)
# (b) flat disk in z = 3 - 2x, downward normal (-2, 0, -1)
flat = (curl9[0] * (-2) + curl9[2] * (-1)).subs(z, 3 - 2 * x)
flat_v = sp.integrate(sp.integrate((flat.subs({x: -1 + r * sp.cos(th), y: r * sp.sin(th)}) * r), (r, 0, 2)), (th, 0, 2 * sp.pi))
check("9 flux of curl on flat disk (downward)", same(flat_v, SOL_9), sp.simplify(flat_v), SOL_9)
# (c) line integral: boundary clockwise from above
rr9 = [-1 + 2 * sp.cos(t), -2 * sp.sin(t), 3 - 2 * (-1 + 2 * sp.cos(t))]
num9c = num_line(F9, rr9, 0, 2 * mp.pi)
check("9 line integral, clockwise boundary", close(num9c, sp.N(SOL_9), 1e-8), mp.nstr(num9c, 12), SOL_9)

# ---------------- 10 ----------------
Mx = sp.Matrix([[1, -1, 0, 1], [3, 0, -1, 1], [0, 3, -5, -7], [-4, 1, 1, -1]])
bv = sp.Matrix([2, 1, 5, 2])
My = Mx.copy()
My[:, 1] = bv
y10 = sp.Rational(My.det(), Mx.det())
sol10 = Mx.LUsolve(bv)

check("10(a) det(A) and det(A_y)", Mx.det() != 0, (Mx.det(), My.det()), "")
check("10(a) y value", y10 == SOL_10a, y10, SOL_10a)
check("10(a) y by Cramer = y from solve", y10 == sol10[1], y10, sol10[1])
a, b, c, al, be, ga, X, Y, Z = sp.symbols("a b c alpha beta gamma X Y Z")
A10 = sp.Matrix([[a, b, c], [al, be, ga], [X, Y, Z]])
B10 = sp.Matrix([[2 * al, 2 * be, 2 * ga], [-X + 5 * a, -Y + 5 * b, -Z + 5 * c], [a - 3 * al, b - 3 * be, c - 3 * ga]])
check("10(b) det B = -2 det A", sp.expand(B10.det() + 2 * A10.det()) == 0, sp.factor(B10.det()), "-2 det A")
detA = sp.Rational(24, 8)
v10b = (-1) ** 3 * (-2 * detA) ** 2 / detA
check("10(b) det(-B^T A^{-1} B)", v10b == SOL_10b, v10b, SOL_10b)
# numeric instance
An = sp.Matrix([[1, 2, 0], [0, 1, 1], [1, 1, 2]])   # det = 3
Bn = B10.subs({a: An[0, 0], b: An[0, 1], c: An[0, 2], al: An[1, 0], be: An[1, 1], ga: An[1, 2], X: An[2, 0], Y: An[2, 1], Z: An[2, 2]})
check("10(b) numeric instance (det A = 3)", (2 * An).T.det() == 24 and (-Bn.T * An.inv() * Bn).det() == SOL_10b, (-Bn.T * An.inv() * Bn).det(), SOL_10b)
A10c = sp.Matrix([[2, 0], [1, 2], [5, -1]])
B10c = sp.Matrix([[2, -1, 4], [0, 3, 1]])
C10c = sp.Matrix([[2, 1, -6], [0, -1, 2], [5, 3, 7]])
D10 = A10c * B10c - C10c.T
check("10(c) D_33", D10[2, 2] == SOL_10c, D10[2, 2], SOL_10c)

# ---------------- report ----------------
w0 = max(len(rw[0]) for rw in ROWS)
nfail = 0
for label, ok, mine, sol in ROWS:
    print(f"{'PASS' if ok else 'FAIL'}  {label:<{w0}}  mine={mine}  sol={sol}")
    nfail += (not ok)
print(f"\n{len(ROWS)} checks, {len(ROWS) - nfail} PASS, {nfail} FAIL")
sys.exit(1 if nfail else 0)
