#!/usr/bin/env python3
"""Independent anchor values for stewart/exams 2022-final-b1 (Calculus II MATH 162, Final, Fall 2022, Block 1).

Every final answer is recomputed from the problem statement with sympy / mpmath and compared
with the constant written in solutions/2022-final-b1.html (SOL_* below).
Stokes / Divergence problems are cross-checked by computing the other side directly
(e.g. the curved surface integral numerically, the line integral arc by arc).
Run: python3 -I stewart/exams/inventory/anchor-2022-final-b1.py   (exit 0 = all PASS)
"""
import sys

import mpmath as mp
import sympy as sp

mp.mp.dps = 20
x, y, z, t, r, th, ph = sp.symbols("x y z t r theta phi", real=True)
pi = sp.pi
ROWS = []


def check(label, ok, mine, sol):
    ROWS.append((label, bool(ok), str(mine), str(sol)))


def close(a, b, tol=1e-7):
    return abs(complex(a) - complex(b)) < tol


def same(a, b):
    return sp.simplify(sp.sympify(a) - sp.sympify(b)) == 0 or close(sp.N(a, 30), sp.N(b, 30), 1e-12)


# ---------------- Solution constants (copied from solutions/2022-final-b1.html) ----------------
SOL_1 = (0, sp.Rational(5, 4))
SOL_1_m = 2 * pi
SOL_1_Mx = 5 * pi / 2
SOL_2 = 0
SOL_3 = -pi
SOL_3_C2 = -pi
SOL_4 = 8 * pi / 5
SOL_5a = (2 + pi) * sp.E / 8 + pi / 4
SOL_5b = sp.sqrt(5) * (8 + 3 * pi**2) / 48
SOL_6 = 68 * pi / 15
SOL_6_div = 8 * pi / 15
SOL_6_disk = -4 * pi
SOL_7a = 4 * pi * (3 * sp.sqrt(3) + 1) / 3
SOL_7b = 8 * pi - 16
SOL_8 = sp.Rational(-2, 3)
SOL_8_arcs = (0, sp.Rational(-4, 3), sp.Rational(2, 3))
SOL_9 = 2 * pi
SOL_10_detA = None  # -a (symbolic, checked below)
SOL_10_x2 = 1
SOL_10_B = 128   # times k
SOL_10_C = 12
SOL_10_D = -2


def curl(F):
    P, Q, R = F
    return [sp.diff(R, y) - sp.diff(Q, z), sp.diff(P, z) - sp.diff(R, x), sp.diff(Q, x) - sp.diff(P, y)]


def div(F):
    return sp.diff(F[0], x) + sp.diff(F[1], y) + sp.diff(F[2], z)


def line_integrand(F, rr):
    sub = {x: rr[0], y: rr[1], z: rr[2]}
    return sum(sp.sympify(F[i]).subs(sub) * sp.diff(sp.sympify(rr[i]), t) for i in range(3))


def nquad_t(expr, a, b):
    f = sp.lambdify(t, expr, "mpmath")
    return mp.quad(f, [a, b])


# ---------------- 1. center of mass, ellipse x^2+4(y-1)^2=4, density y ----------------
xmax = 2 * sp.sqrt(1 - (y - 1) ** 2)
m = sp.integrate(sp.integrate(y, (x, -xmax, xmax)), (y, 0, 2))
Mx = sp.integrate(sp.integrate(y * y, (x, -xmax, xmax)), (y, 0, 2))
My = sp.integrate(sp.integrate(x * y, (x, -xmax, xmax)), (y, 0, 2))
cm = (sp.simplify(My / m), sp.simplify(Mx / m))
check("1 mass m", same(m, SOL_1_m), m, SOL_1_m)
check("1 moment M_x", same(Mx, SOL_1_Mx), Mx, SOL_1_Mx)
check("1 center of mass", same(cm[0], SOL_1[0]) and same(cm[1], SOL_1[1]), cm, SOL_1)

# ---------------- 2. closed space curve ----------------
F2 = [x - sp.sin(x), y**2 + sp.exp(y), x + z]
r2 = [(1 + sp.sin(20 * t)) * sp.cos(t), (1 + sp.sin(20 * t)) * sp.sin(t), sp.cos(20 * t)]
closed = all(sp.simplify(c.subs(t, 0) - c.subs(t, 2 * pi)) == 0 for c in r2)
f2 = sp.lambdify(t, line_integrand(F2, r2), "mpmath")
I2 = mp.quad(f2, mp.linspace(0, 2 * mp.pi, 81))
check("2 curve closed", closed, closed, True)
check("2 line integral (numeric)", close(I2, SOL_2, 1e-9), mp.nstr(I2, 12), SOL_2)
check("2 curl F = <0,-1,0>", curl(F2) == [0, -1, 0], curl(F2), "<0,-1,0>")

# ---------------- 3. three semicircles (3,0)->(-3,0) ----------------
F3 = [-y / (x**2 + y**2), x / (x**2 + y**2), 0]
# C1: upper semicircle centre (2,0) from (3,0) to (1,0): angle s 0 -> pi (counterclockwise about (2,0))
C1 = [2 + sp.cos(t), sp.sin(t), 0]
# C2: lower unit semicircle from (1,0) through (0,-1) to (-1,0): angle 0 -> -pi
C2 = [sp.cos(-t), sp.sin(-t), 0]
# C3: upper semicircle centre (-2,0) from (-1,0) to (-3,0): angle 0 -> pi about (-2,0)
C3 = [-2 + sp.cos(t), sp.sin(t), 0]
assert [c.subs(t, 0) for c in C1[:2]] == [3, 0] and [c.subs(t, pi) for c in C1[:2]] == [1, 0]
assert [c.subs(t, 0) for c in C2[:2]] == [1, 0] and [sp.simplify(c.subs(t, pi)) for c in C2[:2]] == [-1, 0]
assert [sp.simplify(c.subs(t, pi / 2)) for c in C2[:2]] == [0, -1]
assert [c.subs(t, 0) for c in C3[:2]] == [-1, 0] and [c.subs(t, pi) for c in C3[:2]] == [-3, 0]
parts = [sp.N(nquad_t(sp.simplify(line_integrand(F3, C)), 0, mp.pi)) for C in (C1, C2, C3)]
I3 = sum(parts)
check("3 C1 = 0", close(parts[0], 0), parts[0], 0)
check("3 C2 = -pi", close(parts[1], sp.N(SOL_3_C2)), parts[1], SOL_3_C2)
check("3 C3 = 0", close(parts[2], 0), parts[2], 0)
check("3 total", close(I3, sp.N(SOL_3)), I3, SOL_3)

# ---------------- 4. maximal outward flux ----------------
F4 = [x - x**3, y - y**3, z - z**3]
d4 = sp.factor(div(F4))
check("4 div F = 3(1-x^2-y^2-z^2)", sp.expand(d4 - 3 * (1 - x**2 - y**2 - z**2)) == 0, d4, "3(1-|x|^2)")
rho, R = sp.symbols("rho R", positive=True)
ball = sp.integrate(3 * (1 - rho**2) * rho**2 * sp.sin(ph), (rho, 0, R), (th, 0, 2 * pi), (ph, 0, pi))
crit = sp.solve(sp.diff(ball, R), R)
best = ball.subs(R, 1)
check("4 ball family max at R=1", crit == [1], crit, [1])
check("4 max flux (unit ball)", same(best, SOL_4), best, SOL_4)
# compare with other solids: cube [-1,1]^3, half ball, ball of radius 0.9 -> all smaller
g = 3 * (1 - x**2 - y**2 - z**2)
cube = sp.integrate(g, (x, -1, 1), (y, -1, 1), (z, -1, 1))
check("4 cube [-1,1]^3 smaller", cube < best, cube, best)
# Monte-Carlo-free sanity: unit ball minus a cap is smaller (integrand >=0 inside)
cap = sp.integrate(3 * (1 - rho**2) * rho**2 * sp.sin(ph), (rho, 0, 1), (th, 0, 2 * pi), (ph, 0, pi / 4))
check("4 removing a cap lowers flux", best - cap < best, best - cap, best)

# ---------------- 5. conservative field; scalar line integral ----------------
F5 = [sp.exp(z) / (1 + x**2) ** 2, sp.sin(y) ** 2, sp.Rational(1, 2) * (x / (x**2 + 1) + sp.atan(x)) * sp.exp(z)]
c5 = [sp.simplify(c) for c in curl(F5)]
check("5(1) curl F = 0", c5 == [0, 0, 0], c5, [0, 0, 0])
# independent potential: integrate P in x, fix y-, z-parts
fpot = sp.integrate(F5[0], x)
fpot = fpot + sp.integrate(sp.simplify(F5[1] - sp.diff(fpot, y)), y)
fpot = fpot + sp.integrate(sp.simplify(F5[2] - sp.diff(fpot, z)), z)
grad_ok = all(sp.simplify(sp.diff(fpot, v) - F5[i]) == 0 for i, v in enumerate((x, y, z)))
val5 = sp.simplify(fpot.subs({x: 1, y: pi / 2, z: 1}) - fpot.subs({x: 0, y: 0, z: 0}))
check("5(1) potential reproduces F", grad_ok, grad_ok, True)
check("5(1) FTLI value", same(val5, SOL_5a), sp.N(val5, 12), sp.N(SOL_5a, 12))
# along a non-straight path for good measure: r(t) = (t, pi/2 t^2, t^3)
I5n = nquad_t(line_integrand(F5, [t, pi / 2 * t**2, t**3]), 0, 1)
check("5(1) numeric along (t, pi t^2/2, t^3)", close(I5n, sp.N(SOL_5a)), mp.nstr(I5n, 12), sp.N(SOL_5a, 12))
r5 = [sp.cos(2 * t), sp.sin(2 * t), t]
speed = sp.sqrt(sum(sp.diff(c, t) ** 2 for c in r5))
I5b = sp.integrate(sp.simplify((x * y**2 + 2 * z).subs({x: r5[0], y: r5[1], z: r5[2]}) * sp.simplify(speed)), (t, 0, pi / 4))
check("5(2) scalar line integral", same(I5b, SOL_5b), sp.N(I5b, 12), sp.N(SOL_5b, 12))

# ---------------- 6. flux through upper half-ellipsoid x^2+y^2+4z^2=4, upward ----------------
F6 = [x * z**2, sp.exp(y) - x**3, y**2 - z * sp.exp(y)]
r6 = [2 * sp.sin(ph) * sp.cos(th), 2 * sp.sin(ph) * sp.sin(th), sp.cos(ph)]
n6 = sp.Matrix([sp.diff(c, ph) for c in r6]).cross(sp.Matrix([sp.diff(c, th) for c in r6]))
# upward check at the top-ish point phi=pi/4, theta=0
up = sp.N(n6[2].subs({ph: pi / 4, th: 0})) > 0
integ6 = sum(sp.sympify(F6[i]).subs({x: r6[0], y: r6[1], z: r6[2]}) * n6[i] for i in range(3))
f6 = sp.lambdify((ph, th), integ6, "mpmath")
I6 = mp.quad(lambda a, b: f6(a, b), [0, mp.pi / 2], [0, mp.pi, 2 * mp.pi])
check("6 r_phi x r_theta points upward", up, up, True)
check("6 direct surface integral", close(I6, sp.N(SOL_6), 1e-8), mp.nstr(I6, 12), sp.N(SOL_6, 12))
divE = sp.integrate(z**2 * pi * (4 - 4 * z**2), (z, 0, 1))
disk = -sp.integrate(sp.integrate((r * sp.sin(th)) ** 2 * r, (r, 0, 2)), (th, 0, 2 * pi))
check("6 triple integral", same(divE, SOL_6_div), divE, SOL_6_div)
check("6 bottom disk (down)", same(disk, SOL_6_disk), disk, SOL_6_disk)

# ---------------- 7. sphere of radius 2 ----------------
rs = [2 * sp.sin(ph) * sp.cos(th), 2 * sp.sin(ph) * sp.sin(th), 2 * sp.cos(ph)]
ns = sp.Matrix([sp.diff(c, ph) for c in rs]).cross(sp.Matrix([sp.diff(c, th) for c in rs]))
dS = sp.simplify(sp.sqrt(sp.simplify(ns.dot(ns))))  # 4 sin(phi) on 0<phi<pi
f7 = sp.lambdify((ph, th), (rs[0] ** 3 + rs[2] ** 2) * 4 * sp.sin(ph), "mpmath")
I7a = mp.quad(f7, [mp.pi / 6, 2 * mp.pi / 3], [0, mp.pi, 2 * mp.pi])
check("7(1) |r_phi x r_theta| = 4 sin phi", sp.simplify(dS - 4 * sp.Abs(sp.sin(ph))) == 0, dS, "4 sin(phi)")
check("7(1) z-range <-> phi in [pi/6, 2pi/3]",
      same(2 * sp.cos(pi / 6), sp.sqrt(3)) and same(2 * sp.cos(2 * pi / 3), -1), "ok", "ok")
check("7(1) surface integral (with x^3)", close(I7a, sp.N(SOL_7a), 1e-9), mp.nstr(I7a, 12), sp.N(SOL_7a, 12))
# 7(2): both caps; on the sphere, x^2+y^2 < 2y  <=>  4 sin^2(phi) < 4 sin(phi) sin(theta) <=> sin(phi) < sin(theta)
# area = int_0^pi int_{phi: sin phi < sin theta} 4 sin(phi) dphi dtheta
#      = int_0^pi [ int_0^theta + int_{pi-theta}^pi ] 4 sin phi dphi dtheta   (theta in (0, pi/2]; symmetric)
A_half = sp.integrate(sp.integrate(4 * sp.sin(ph), (ph, 0, th)), (th, 0, pi / 2)) * 2  # upper cap, theta in (0,pi)
A_total = 2 * A_half
check("7(2) area (both caps)", same(A_total, SOL_7b), A_total, SOL_7b)
# numeric cross-check via the graph formula over D: r <= 2 sin(theta)
Ag = mp.quad(lambda T: mp.quad(lambda R_: 2 * R_ / mp.sqrt(4 - R_**2), [0, 2 * mp.sin(T)]), [0, mp.pi / 2, mp.pi])
check("7(2) graph formula upper cap", close(Ag, sp.N(SOL_7b / 2), 1e-7), mp.nstr(Ag, 12), sp.N(SOL_7b / 2, 12))

# ---------------- 8. octant of x^2+y^2/4+z^2=1, ccw from above ----------------
F8 = [y * z + 2 * x * z, y * z + z**2 / 2, y * x + y * z]
cF8 = curl(F8)
check("8 curl F = <x-y, 2x, -z>", [sp.expand(a - b) for a, b in zip(cF8, [x - y, 2 * x, -z])] == [0, 0, 0], cF8, "<x-y,2x,-z>")
arcs = [
    [sp.cos(t), 2 * sp.sin(t), sp.Integer(0)],  # (1,0,0)->(0,2,0) in z=0
    [sp.Integer(0), 2 * sp.cos(t), sp.sin(t)],  # (0,2,0)->(0,0,1) in x=0
    [sp.sin(t), sp.Integer(0), sp.cos(t)],      # (0,0,1)->(1,0,0) in y=0
]
arc_vals = [sp.integrate(sp.expand(line_integrand(F8, a)), (t, 0, pi / 2)) for a in arcs]
for k_, (av, sv) in enumerate(zip(arc_vals, SOL_8_arcs), 1):
    check(f"8 arc C{k_}", same(av, sv), av, sv)
I8line = sum(arc_vals)
# orientation: projection of the loop onto the xy-plane has positive signed area (ccw from above)
area_xy = sum(sp.integrate(sp.Rational(1, 2) * (a[0] * sp.diff(a[1], t) - a[1] * sp.diff(a[0], t)), (t, 0, pi / 2)) for a in arcs)
check("8 loop is ccw seen from above", sp.N(area_xy) > 0, area_xy, ">0")
# direct surface integral of curl F over the curved piece with the outward (upward) normal
r8 = [sp.sin(ph) * sp.cos(th), 2 * sp.sin(ph) * sp.sin(th), sp.cos(ph)]
n8 = sp.Matrix([sp.diff(c, ph) for c in r8]).cross(sp.Matrix([sp.diff(c, th) for c in r8]))
outward = sp.N(n8.dot(sp.Matrix(r8)).subs({ph: pi / 3, th: pi / 5})) > 0
integ8 = sum(sp.sympify(cF8[i]).subs({x: r8[0], y: r8[1], z: r8[2]}) * n8[i] for i in range(3))
f8 = sp.lambdify((ph, th), integ8, "mpmath")
I8surf = mp.quad(f8, [0, mp.pi / 2], [0, mp.pi / 2])
check("8 r_phi x r_theta outward", outward, outward, True)
check("8 line integral (3 arcs)", same(I8line, SOL_8), I8line, SOL_8)
check("8 curved-surface flux of curl F", close(I8surf, sp.N(SOL_8), 1e-9), mp.nstr(I8surf, 12), SOL_8)

# ---------------- 9. Stokes on plane x-2z=3 inside y^2+z^2=1, normal toward +x ----------------
F9 = [2 * z, x * y, z + 2 * y]
cF9 = curl(F9)
Y, Z = sp.symbols("Y Z", real=True)
r9 = sp.Matrix([3 + 2 * Z, Y, Z])
n9 = r9.diff(Y).cross(r9.diff(Z))
check("9 normal has +x component", n9[0] > 0, list(n9), "<1,0,-2>")
integ9 = sum(sp.sympify(cF9[i]).subs({x: r9[0], y: r9[1], z: r9[2]}) * n9[i] for i in range(3))
S9 = sp.integrate(sp.integrate(sp.expand(integ9.subs({Y: r * sp.cos(th), Z: r * sp.sin(th)}) * r), (r, 0, 1)), (th, 0, 2 * pi))
# boundary: (Y,Z) ccw in the parameter plane (compatible with r_Y x r_Z)
c9 = [3 + 2 * sp.sin(t), sp.cos(t), sp.sin(t)]
L9 = sp.integrate(sp.expand(line_integrand(F9, c9)), (t, 0, 2 * pi))
check("9 surface side", same(S9, SOL_9), S9, SOL_9)
check("9 line side", same(L9, SOL_9), L9, SOL_9)
# orientation sanity: right-hand rule -- (r'(0) x (inward direction toward centre)) . n > 0
tan0 = sp.Matrix([sp.diff(c, t) for c in c9]).subs(t, 0)
inward0 = (sp.Matrix([3, 0, 0]) - sp.Matrix(c9).subs(t, 0))
check("9 boundary orientation matches +x normal", tan0.cross(inward0).dot(n9) > 0, tan0.cross(inward0).dot(n9), ">0")

# ---------------- 10. Cramer's rule and determinant identities ----------------
a, b, c, k = sp.symbols("a b c k")
A = sp.Matrix([[1, b, 1, 1], [a, 0, 0, a], [2, 1, c, 2 - c], [3, 0, 1, 2]])
dvec = sp.Matrix([1, 0, 1, 0])
detA = sp.factor(A.det())
A2 = A.copy()
A2[:, 1] = dvec
detA2 = sp.factor(A2.det())
x2 = sp.simplify(detA2 / detA)
sol10 = sp.solve(list(A * sp.Matrix(sp.symbols("x1:5")) - dvec), sp.symbols("x1:5"), dict=True)
check("10(1) det A = -a", sp.simplify(detA + a) == 0, detA, "-a")
check("10(1) det A_2 = -a", sp.simplify(detA2 + a) == 0, detA2, "-a")
check("10(1) x2 by Cramer (a != 0)", same(x2, SOL_10_x2), x2, SOL_10_x2)
check("10(1) x2 by solve", len(sol10) == 1 and same(sol10[0][sp.Symbol("x2")], SOL_10_x2), sol10, "x2=1")
al, be, ga, X, Yy, Zz = sp.symbols("alpha beta gamma X Y Z")
M = sp.Matrix([[a, b, c], [al, be, ga], [X, Yy, Zz]])
kk = M.det()
B = 2 * sp.Matrix([[1, 2, 3], [0, 1, 2], [0, 0, -2]]) * sp.Matrix([[0, 0, 1], [0, 2, 3], [4, 5, 6]]) * M
Cm = sp.Matrix([[6 * X, 3 * Yy, 3 * Zz], [-4 * al, -2 * be, -2 * ga], [2 * a, b, c]])
Dm = sp.Matrix([[al + X, a, 2 * X], [be + Yy, b, 2 * Yy], [ga + Zz, c, 2 * Zz]])
check("10(2)a det B = 128k", sp.expand(B.det() - SOL_10_B * kk) == 0, sp.factor(B.det() / kk), SOL_10_B)
check("10(2)b det C = 12k", sp.expand(Cm.det() - SOL_10_C * kk) == 0, sp.factor(Cm.det() / kk), SOL_10_C)
check("10(2)c det D = -2k", sp.expand(Dm.det() - SOL_10_D * kk) == 0, sp.factor(Dm.det() / kk), SOL_10_D)

# ---------------- report ----------------
w = max(len(r_[0]) for r_ in ROWS)
for label, ok, mine, sol in ROWS:
    print(f"{'PASS' if ok else 'FAIL'}  {label:<{w}}  anchor={mine[:60]}  solution={sol[:40]}")
n_fail = sum(1 for r_ in ROWS if not r_[1])
print(f"\n{len(ROWS)} checks, {len(ROWS) - n_fail} PASS, {n_fail} FAIL")
sys.exit(1 if n_fail else 0)
