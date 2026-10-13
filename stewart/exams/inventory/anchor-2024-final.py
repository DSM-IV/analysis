#!/usr/bin/env python3
"""Independent anchor values for stewart/exams 2024-final (Calculus II final, Fall 2024).

Every final answer is recomputed from the problem statement with sympy / mpmath and compared
with the constant written in solutions/2024-final.html (SOL_* below).
Orientation-sensitive problems (5, 6, 7, 10) are checked by computing the surface or line
integral DIRECTLY on the given surface with the stated orientation, not via the solution's
replacement surface.
Run: python3 -I stewart/exams/inventory/anchor-2024-final.py   (exit 0 = all PASS)
"""
import sys

import mpmath as mp
import sympy as sp

mp.mp.dps = 15
x, y, z, t, u, v, w = sp.symbols("x y z t u v w", real=True)
r, th, ph, rho = sp.symbols("r theta phi rho", nonnegative=True)

ROWS = []


def check(label, ok, mine, sol):
    ROWS.append((label, bool(ok), str(mine), str(sol)))


def close(a, b, tol=1e-7):
    return abs(complex(a) - complex(b)) < tol


def curl(Fv):
    P, Q, R = Fv
    return [sp.diff(R, y) - sp.diff(Q, z), sp.diff(P, z) - sp.diff(R, x), sp.diff(Q, x) - sp.diff(P, y)]


def div(Fv):
    return sp.diff(Fv[0], x) + sp.diff(Fv[1], y) + sp.diff(Fv[2], z)


# ---------------- Solution constants (copied from solutions/2024-final.html) ----------------
SOL_1a = -4 * sp.pi
SOL_1b = sp.Rational(9, 2)
SOL_2a = sp.Rational(29, 21)
SOL_2b = -sp.sin(1) - sp.cos(1)
SOL_3a = 5
SOL_3b = 2 * sp.sqrt(6)
SOL_4 = 3 * sp.pi / 2
SOL_4_L = sp.pi / 2                       # closing segment (2,2)->(-2,2)
SOL_5_area = sp.pi * (sp.sqrt(3) + sp.log(sp.sqrt(2) + sp.sqrt(3)) / sp.sqrt(2))
SOL_6 = 14 * sp.sqrt(2) * sp.pi
SOL_7 = 4 * sp.pi
SOL_7_up = -4 * sp.pi
SOL_8a = (u - v) / 2
SOL_8b = sp.pi / 42
SOL_9 = sp.Rational(13, 96)
SOL_9_dets = (18, 39)
SOL_10a = 0
SOL_10b = [1 / sp.sqrt(x**2 + y**2 + z**2)] * 3
SOL_10c = 0

# ---------------- 1(a) Green: direct line integral on the circle ----------------
P1, Q1 = y - sp.cos(y), x * sp.sin(y) + y
check("1(a) Q_x - P_y = -1", sp.simplify(sp.diff(Q1, x) - sp.diff(P1, y)) == -1,
      sp.simplify(sp.diff(Q1, x) - sp.diff(P1, y)), -1)
cx, cy = 3 + 2 * sp.cos(t), -4 + 2 * sp.sin(t)          # counterclockwise
integrand = (P1.subs({x: cx, y: cy}) * sp.diff(cx, t) + Q1.subs({x: cx, y: cy}) * sp.diff(cy, t))
f1 = sp.lambdify(t, integrand, "mpmath")
val1a = mp.quad(f1, [0, mp.pi / 2, mp.pi, 3 * mp.pi / 2, 2 * mp.pi])
check("1(a) line integral (direct)", close(val1a, sp.N(SOL_1a)), mp.nstr(val1a, 12), SOL_1a)

# ---------------- 1(b) pentagon area ----------------
V = [(0, 0), (2, 1), (1, 3), (0, 2), (-1, 2)]
shoe = sp.Rational(sum(V[i][0] * V[(i + 1) % 5][1] - V[(i + 1) % 5][0] * V[i][1] for i in range(5)), 2)
check("1(b) signed area (positive => CCW)", shoe == SOL_1b and shoe > 0, shoe, SOL_1b)


def seg_inter(p1, p2, p3, p4):
    d = lambda a, b, c: (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return d(p1, p2, p3) * d(p1, p2, p4) < 0 and d(p3, p4, p1) * d(p3, p4, p2) < 0


simple = not any(seg_inter(V[i], V[(i + 1) % 5], V[j], V[(j + 1) % 5])
                 for i in range(5) for j in range(i + 2, 5) if not (i == 0 and j == 4))
check("1(b) polygon is simple", simple, simple, True)
# reflex vertex at (0,2): cross product of consecutive edges negative
e1 = (V[3][0] - V[2][0], V[3][1] - V[2][1]); e2 = (V[4][0] - V[3][0], V[4][1] - V[3][1])
check("1(b) non-convex at (0,2)", e1[0] * e2[1] - e1[1] * e2[0] < 0, e1[0] * e2[1] - e1[1] * e2[0], "<0")

# ---------------- 2 ----------------
rt = (t**3, -t**2, t)
F2 = (x + y**2, x * y, y + z)
sub2 = dict(zip((x, y, z), rt))
I2a = sp.integrate(sum(Fi.subs(sub2) * sp.diff(ri, t) for Fi, ri in zip(F2, rt)), (t, 0, 1))
check("2(a)", I2a == SOL_2a, I2a, SOL_2a)
G2 = (sp.sin(y), x * sp.cos(y) + sp.cos(z), -y * sp.sin(z))
g2 = sp.lambdify(t, sum(Gi.subs(sub2) * sp.diff(ri, t) for Gi, ri in zip(G2, rt)), "mpmath")
I2b = mp.quad(g2, [0, 1])
check("2(b) direct parametrization", close(I2b, sp.N(SOL_2b)), mp.nstr(I2b, 12), SOL_2b)
check("2(b) curl G = 0", all(sp.simplify(c) == 0 for c in curl(G2)), curl(G2), 0)

# ---------------- 3: two different test f with the given moments ----------------
for name, fexpr in (("2+6u", 2 + 6 * u), ("4-6u+12u^2", 4 - 6 * u + 12 * u**2)):
    ok_moments = (sp.integrate(fexpr, (u, 0, 1)) == 5 and sp.integrate(u * fexpr, (u, 0, 1)) == 3)
    check(f"3 test f={name} has moments 5,3", ok_moments, ok_moments, True)
    s = x + y - 2 * z
    fs = fexpr.subs(u, s)
    # (a) along a curved path (not the segment) from (1,3,2) to (2,5,3)
    pc = (1 + t, 3 + 2 * t + sp.sin(sp.pi * t), 2 + t**2)
    subc = dict(zip((x, y, z), pc))
    fa = sp.lambdify(t, (fs * sp.diff(pc[0], t) + fs * sp.diff(pc[1], t) - 2 * fs * sp.diff(pc[2], t)).subs(subc), "mpmath")
    Ia = mp.quad(fa, [0, 1])
    check(f"3(a) curved path, f={name}", close(Ia, SOL_3a), mp.nstr(Ia, 12), SOL_3a)
    # (b) segment, g = int_0^{s} f
    gexpr = sp.integrate(fexpr, (u, 0, s))
    ps = (1 + t, 3 + 2 * t, 2 + t)
    speed = sp.sqrt(sum(sp.diff(c, t)**2 for c in ps))
    Ib = sp.integrate(gexpr.subs(dict(zip((x, y, z), ps))) * speed, (t, 0, 1))
    check(f"3(b) segment, f={name}", sp.simplify(Ib - SOL_3b) == 0, Ib, SOL_3b)

# ---------------- 4: direct line integral along the parabola ----------------
P4 = (x - y) / (x**2 + y**2); Q4 = (x + y) / (x**2 + y**2)
check("4 Q_x = P_y", sp.simplify(sp.diff(Q4, x) - sp.diff(P4, y)) == 0, "Q_x-P_y", 0)
p4 = (t, 2 * t**2 - 6)
f4 = sp.lambdify(t, (P4.subs({x: p4[0], y: p4[1]}) * 1 + Q4.subs({x: p4[0], y: p4[1]}) * sp.diff(p4[1], t)), "mpmath")
I4 = mp.quad(f4, [-2, -mp.sqrt(3), 0, mp.sqrt(3), 2])
check("4 direct numeric", close(I4, sp.N(SOL_4)), mp.nstr(I4, 12), SOL_4)
IL = sp.integrate(P4.subs(y, 2), (x, 2, -2))
check("4 closing segment L", sp.simplify(IL - SOL_4_L) == 0, IL, SOL_4_L)

# ---------------- 5 ----------------
zz, tt = sp.symbols("z_p theta_p", real=True)
R5 = sp.Matrix([sp.sqrt(1 + zz**2) * sp.cos(tt), sp.sqrt(1 + zz**2) * sp.sin(tt), zz])
check("5(1) param lies on S", sp.simplify(R5[0]**2 + R5[1]**2 - R5[2]**2 - 1) == 0, "x^2+y^2-z^2-1", 0)
nS = sp.Matrix([-R5[0], -R5[1], R5[2]]) / sp.sqrt(R5[0]**2 + R5[1]**2 + R5[2]**2)
unit = sp.simplify(nS.dot(nS)) == 1
perp = sp.simplify(nS.dot(R5.diff(zz))) == 0 and sp.simplify(nS.dot(R5.diff(tt))) == 0
inward = sp.simplify(nS[0] * R5[0] + nS[1] * R5[1]) .subs({zz: sp.Rational(1, 3), tt: 1}) < 0
check("5(1) n unit", unit, unit, True)
check("5(1) n normal to S", perp, perp, True)
check("5(1) n points toward z-axis", inward, inward, True)
cr = R5.diff(zz).cross(R5.diff(tt))
check("5(1) r_z x r_theta = <-x,-y,z>", sp.simplify(cr - sp.Matrix([-R5[0], -R5[1], R5[2]])) == sp.zeros(3, 1), "cross", "<-x,-y,z>")
mag = sp.sqrt(sp.simplify(cr.dot(cr)))
A5 = 2 * mp.pi * mp.quad(sp.lambdify(zz, mag, "mpmath"), [0, 1])
check("5(2) area numeric", close(A5, sp.N(SOL_5_area)), mp.nstr(A5, 12), sp.N(SOL_5_area, 8))
# also via the cosh parametrization on 0<=u<=asinh(1)
A5b = 2 * mp.pi * mp.quad(lambda s: mp.cosh(s) * mp.sqrt(mp.cosh(2 * s)), [0, mp.asinh(1)])
check("5(2) area via cosh param", close(A5b, sp.N(SOL_5_area)), mp.nstr(A5b, 12), sp.N(SOL_5_area, 8))

# ---------------- 6: direct surface integral over the hemisphere y >= x, outward ----------------
h = sp.exp(x**2 - y**2)
F6 = [3 * z * h, 2 * z * h, 2 * x - 4 * y + sp.exp(z**2)]
C6 = curl(F6)
cf = sp.lambdify((x, y, z), C6, "mpmath")
e1 = mp.matrix([-1, 1, 0]) / mp.sqrt(2)   # pole of S (y-x maximal)
e2 = mp.matrix([1, 1, 0]) / mp.sqrt(2)
e3 = mp.matrix([0, 0, 1])


def integrand6(a, b):  # a = polar angle from e1 in [0, pi/2], b in [0, 2pi]
    p = 2 * (mp.cos(a) * e1 + mp.sin(a) * mp.cos(b) * e2 + mp.sin(a) * mp.sin(b) * e3)
    c = cf(p[0], p[1], p[2])
    nrm = p / 2                              # outward unit normal of the sphere
    return (c[0] * nrm[0] + c[1] * nrm[1] + c[2] * nrm[2]) * 4 * mp.sin(a)


chk_pt = 2 * (mp.cos(0.3) * e1 + mp.sin(0.3) * mp.cos(1.1) * e2 + mp.sin(0.3) * mp.sin(1.1) * e3)
check("6 parametrization covers y>=x side", chk_pt[1] - chk_pt[0] > 0, mp.nstr(chk_pt[1] - chk_pt[0], 5), ">0")
I6 = mp.quad(integrand6, [0, mp.pi / 4, mp.pi / 2], [0, mp.pi / 2, mp.pi, 3 * mp.pi / 2, 2 * mp.pi])
check("6 direct hemisphere integral (outward)", close(I6, sp.N(SOL_6), 1e-6), mp.nstr(I6, 12), SOL_6)
# boundary circle as in the solution, orientation check: n x T must point into S (toward e1)
rc = (sp.sqrt(2) * sp.sin(t), sp.sqrt(2) * sp.sin(t), 2 * sp.cos(t))
T0 = sp.Matrix([sp.diff(c, t) for c in rc]).subs(t, 0)
n0 = sp.Matrix([0, 0, 1])
left = n0.cross(T0)
check("6 boundary orientation (n x T toward S)", left.dot(sp.Matrix([-1, 1, 0])) > 0, list(left), "(-1,1,0) dir")
lf = sp.lambdify(t, sum(Fi.subs(dict(zip((x, y, z), rc))) * sp.diff(ri, t) for Fi, ri in zip(F6, rc)), "mpmath")
I6c = mp.quad(lf, [0, mp.pi / 2, mp.pi, 3 * mp.pi / 2, 2 * mp.pi])
check("6 Stokes line integral", close(I6c, sp.N(SOL_6)), mp.nstr(I6c, 12), SOL_6)

# ---------------- 7: direct flux through the paraboloid, downward ----------------
F7 = [-z**2 * sp.exp((x * y)**2) + sp.atan(x * z), z**2 * sp.exp((x * y)**2) - y * z / (1 + x**2 * z**2), -z + 1]
d7 = sp.simplify(div(F7))
check("7 div F = 2xyz^2(x-y)e^{x^2y^2} - 1",
      sp.simplify(d7 - (2 * x * y * z**2 * (x - y) * sp.exp(x**2 * y**2) - 1)) == 0, d7, "given")
pr = sp.Matrix([r * sp.cos(th), r * sp.sin(th), 4 - r**2])
nr = pr.diff(r).cross(pr.diff(th))          # check its k-component sign
k_sign = sp.simplify(nr[2])
down = -nr if sp.simplify(k_sign - r) == 0 else nr
check("7 chosen normal is downward", sp.simplify(down[2]) == -r, down[2], "-r")
F7p = sp.Matrix([c.subs({x: pr[0], y: pr[1], z: pr[2]}) for c in F7])
f7 = sp.lambdify((r, th), F7p.dot(down), "mpmath")
I7 = mp.quad(f7, [0, 1, 2], [0, mp.pi / 2, mp.pi, 3 * mp.pi / 2, 2 * mp.pi])
check("7 direct flux downward", close(I7, sp.N(SOL_7), 1e-6), mp.nstr(I7, 12), SOL_7)
check("7 upward flux = -downward", close(-I7, sp.N(SOL_7_up), 1e-6), mp.nstr(-I7, 12), SOL_7_up)

# ---------------- 8 ----------------
M = sp.Matrix([[1, 1, 1], [1, -1, 1], [1, 1, 2]])
My = M.copy(); My[:, 1] = sp.Matrix([u, v, w])
ycr = sp.simplify(My.det() / M.det())
check("8(a) Cramer y", sp.simplify(ycr - SOL_8a) == 0, ycr, SOL_8a)
sol = sp.solve([x + y + z - u, x - y + z - v, x + y + 2 * z - w], [x, y, z], dict=True)[0]
check("8(a) solve agrees", sp.simplify(sol[y] - SOL_8a) == 0, sol[y], SOL_8a)
J = sp.Matrix([sol[x], sol[y], sol[z]]).jacobian([u, v, w]).det()
check("8(b) |d(x,y,z)/d(u,v,w)| = 1/2", abs(J) == sp.Rational(1, 2), J, "±1/2")
integrand8 = (sol[y]**2 * (u**2 + v**2 + w**2) * abs(J)).subs(
    {u: rho * sp.sin(ph) * sp.cos(th), v: rho * sp.sin(ph) * sp.sin(th), w: rho * sp.cos(ph)}) * rho**2 * sp.sin(ph)
I8 = sp.simplify(sp.integrate(sp.expand(integrand8), (rho, 0, 1), (th, 0, 2 * sp.pi), (ph, 0, sp.pi / 2)))
check("8(b) integral", sp.simplify(I8 - SOL_8b) == 0, I8, SOL_8b)
# independent Cartesian-in-uvw evaluation (w first slice): numeric triple quad
g8 = sp.lambdify((u, v, w), sol[y]**2 * (u**2 + v**2 + w**2) * abs(J), "mpmath")
I8n = mp.quad(lambda ww: mp.quad(lambda vv: mp.quad(lambda uu: g8(uu, vv, ww),
              [-mp.sqrt(max(0, 1 - ww**2 - vv**2)), mp.sqrt(max(0, 1 - ww**2 - vv**2))]),
              [-mp.sqrt(1 - ww**2), mp.sqrt(1 - ww**2)]), [0, 1])
check("8(b) Cartesian numeric", close(I8n, sp.N(SOL_8b), 1e-6), mp.nstr(I8n, 12), SOL_8b)

# ---------------- 9 ----------------
A9 = sp.Matrix([[5, 3, -2, 6], [2, 1, -1, 1], [4, 2, 1, 5], [7, 3, 5, 3]])
B9 = sp.Matrix([[1, -2, 3, 1], [5, -9, 6, 3], [-1, 2, -6, -2], [2, 8, 6, 1]])
check("9 det A, det B", (A9.det(), B9.det()) == SOL_9_dets, (A9.det(), B9.det()), SOL_9_dets)
d9 = ((2 * A9).inv() * B9.T).det()
check("9 det((2A)^{-1} B^T)", d9 == SOL_9, d9, SOL_9)

# ---------------- 10 ----------------
rr = sp.sqrt(x**2 + y**2 + z**2)
F10 = [(z - y) / rr**3, (x - z) / rr**3, (y - x) / rr**3]
check("10 div F = 0 (off origin)", sp.simplify(div(F10)) == 0, sp.simplify(div(F10)), 0)
check("10 F . r = 0 (tangent to spheres => H_eps flux 0)",
      sp.simplify(F10[0] * x + F10[1] * y + F10[2] * z) == 0, "F.r", 0)
F10f = sp.lambdify((x, y, z), F10, "mpmath")


def side(zv, tv):
    f = F10f(mp.cos(tv), mp.sin(tv), zv)
    return f[0] * mp.cos(tv) + f[1] * mp.sin(tv)          # outward radial, dS = dz dtheta


def top(rv, tv):
    return F10f(rv * mp.cos(tv), rv * mp.sin(tv), 3)[2] * rv   # normal +k


tq = [0, mp.pi / 2, mp.pi, 3 * mp.pi / 2, 2 * mp.pi]
Iside = mp.quad(side, [0, 3], tq)
Itop = mp.quad(top, [0, 1], tq)
check("10(a) direct flux side + top", close(Iside + Itop, SOL_10a, 1e-9),
      mp.nstr(Iside, 6) + " + " + mp.nstr(Itop, 6), SOL_10a)
# excision pieces: annulus eps<=r<=1 at z=0 with -k
eps = mp.mpf("0.01")
Iann = mp.quad(lambda rv, tv: -F10f(rv * mp.cos(tv), rv * mp.sin(tv), 0)[2] * rv, [eps, 1], tq)
check("10(a) annulus flux = 0", close(Iann, 0, 1e-9), mp.nstr(Iann, 6), 0)
Gs = SOL_10b
cG = curl(Gs)
check("10(b) curl G = F", all(sp.simplify(a - b) == 0 for a, b in zip(cG, F10)), "curl G - F", 0)
# 10(c) induced orientation on bottom circle: at (1,0,0) outward n = i; T must satisfy n x T -> into S (+k)
Tc = sp.Matrix([0, 1, 0])  # counterclockwise from above at (1,0,0)
check("10(c) CCW (from above) is the induced orientation", sp.Matrix([1, 0, 0]).cross(Tc).dot(sp.Matrix([0, 0, 1])) > 0,
      list(sp.Matrix([1, 0, 0]).cross(Tc)), "+k")
cc = (sp.cos(t), sp.sin(t), sp.Integer(0))
Ic = sp.integrate(sum(Gi.subs(dict(zip((x, y, z), cc))) * sp.diff(ci, t) for Gi, ci in zip(Gs, cc)), (t, 0, 2 * sp.pi))
check("10(c) line integral of G", sp.simplify(Ic) == SOL_10c, Ic, SOL_10c)

# ---------------- report ----------------
w1 = max(len(rw[0]) for rw in ROWS)
for label, ok, mine, solv in ROWS:
    print(f"{'PASS' if ok else 'FAIL'}  {label:<{w1}}  mine={mine}  sol={solv}")
n_fail = sum(1 for rw in ROWS if not rw[1])
print(f"\n{len(ROWS)} checks, {len(ROWS) - n_fail} PASS, {n_fail} FAIL")
sys.exit(1 if n_fail else 0)
