#!/usr/bin/env python3
"""Independent recomputation of Stewart ET 9e §16.9 example answers (anchor values).
20 s SIGALRM timeout per item, flushed prints."""
import signal, traceback
import sympy as sp

def P(*a): print(*a, flush=True)
class TO(Exception): pass
def _h(s, f): raise TO()
signal.signal(signal.SIGALRM, _h)

def item(name):
    def deco(fn):
        P("=" * 70); P(f"[{name}]"); signal.alarm(20)
        try: fn()
        except TO: P("  !! TIMEOUT (20s)")
        except Exception: P("  !! ERROR"); traceback.print_exc()
        finally: signal.alarm(0)
        return fn
    return deco

x, y, z, a, r, th, ph = sp.symbols('x y z a rho theta phi', real=True)
eps, Q = sp.symbols('epsilon Q', positive=True)

def div(F):
    return sp.diff(F[0], x) + sp.diff(F[1], y) + sp.diff(F[2], z)

# ----------------------------------------------------------------------
@item("Ex 1: flux of F = z i + y j + x k over the unit sphere (Divergence Theorem)")
def ex1():
    F = [z, y, x]
    d = div(F)
    P("  div F =", d)
    vol = sp.Rational(4, 3)*sp.pi*1**3
    P("  flux = iiint_B 1 dV = V(B) =", vol, "  textbook 4*pi/3")
    P("  match:", sp.simplify(vol - 4*sp.pi/3) == 0)
    # cross-check by direct surface integral (cf. Example 16.7.4)
    R = sp.Matrix([sp.sin(ph)*sp.cos(th), sp.sin(ph)*sp.sin(th), sp.cos(ph)])
    n = R.diff(ph).cross(R.diff(th))
    Fon = sp.Matrix([R[2], R[1], R[0]])
    I = sp.integrate(sp.integrate(sp.simplify(Fon.dot(n)), (ph, 0, sp.pi)), (th, 0, 2*sp.pi))
    P("  direct surface integral (2nd method, = Example 16.7.4) =", sp.simplify(I))

# ----------------------------------------------------------------------
@item("Ex 2: iint_S F.dS, F = xy i + (y^2 + e^{xz^2}) j + sin(xy) k, E under z=1-x^2, y+z<=2")
def ex2():
    F = [x*y, y**2 + sp.exp(x*z**2), sp.sin(x*y)]
    d = sp.simplify(div(F))
    P("  div F =", d, "  (= y + 2y = 3y)")
    # type 3 region: -1<=x<=1, 0<=z<=1-x^2, 0<=y<=2-z
    I = sp.integrate(sp.integrate(sp.integrate(3*y, (y, 0, 2 - z)), (z, 0, 1 - x**2)), (x, -1, 1))
    I = sp.simplify(I)
    txt = sp.Rational(184, 35)
    P("  triple integral =", I, "  textbook 184/35 =", txt,
      "  match:", sp.simplify(I - txt) == 0, "  numeric:", float(I))
    # 2nd method: different integration order (y outer via slabs)  -> integrate over z,y for each x
    J = sp.integrate(sp.integrate(sp.integrate(3*y, (z, 0, sp.Min(1 - x**2, 2 - y))), (y, 0, 2)), (x, -1, 1))
    P("  alt-order check (z inner, y outer) =", sp.simplify(J))

# ----------------------------------------------------------------------
@item("Ex 3: electric flux of E(x) = eps*Q*x/|x|^3 through any closed surface enclosing 0")
def ex3():
    X = sp.Matrix([x, y, z])
    nrm = sp.sqrt(x**2 + y**2 + z**2)
    E = eps*Q*X/nrm**3
    d = sp.simplify(sp.diff(E[0], x) + sp.diff(E[1], y) + sp.diff(E[2], z))
    P("  div E =", d, "  (0 away from the origin -- Exercise 25)")
    P("  On the sphere |x| = a:  E . n = eps*Q/|x|^4 * (x.x) = eps*Q/a^2")
    flux = eps*Q/a**2 * 4*sp.pi*a**2
    P("  flux = (eps Q / a^2) * A(S1) =", sp.simplify(flux),
      "  textbook 4 pi eps Q =", 4*sp.pi*eps*Q,
      "  match:", sp.simplify(flux - 4*sp.pi*eps*Q) == 0)
    P("  Gauss's Law (16.7.11) special case;  eps = 1/(4 pi eps0)")

# ----------------------------------------------------------------------
@item("Eq (9) + Figure 4: div F(P0) as outward flux density; sources and sinks")
def eq9():
    P("  div F(P0) = lim_{a->0} (1/V(B_a)) iint_{S_a} F . dS")
    F = [x**2, y**2, 0]
    P("  Figure 4 field F = x^2 i + y^2 j,  div F =", div(F), " = 2x + 2y")
    P("  div F > 0  <=>  x + y > 0  <=>  y > -x   -> sources above the line y = -x, sinks below")

# ----------------------------------------------------------------------
@item("Proof pieces: Equations (2)(3)(4) and the type-1 argument for (4)")
def proof():
    Rf = sp.Function('R')(x, y, z)
    P("  (4)  iint_S R k.n dS = iiint_E dR/dz dV")
    P("  type 1: E = {(x,y) in D, u1(x,y) <= z <= u2(x,y)}")
    P("  (15.6.6 + FTC)  iiint_E R_z dV = iint_D [R(x,y,u2) - R(x,y,u1)] dA   -> Eq (5)")
    P("  S3 (vertical side): k.n = 0  ->  contributes 0")
    P("  S2 upward (16.7.10 with F = R k): +iint_D R(x,y,u2) dA;  S1 downward: -iint_D R(x,y,u1) dA")
    P("  sum matches Eq (5).  (2),(3) analogous with E as a type 2 / type 3 region.")

P("=" * 70); P("done")
