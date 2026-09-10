#!/usr/bin/env python3
"""Independent recomputation of Stewart ET 9e §16.8 example answers (anchor values).
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

x, y, z, t, r, th = sp.symbols('x y z t r theta', real=True)

def curl(F, vars=(x, y, z)):
    Pf, Qf, Rf = F
    a, b, c = vars
    return sp.Matrix([sp.diff(Rf, b) - sp.diff(Qf, c),
                      sp.diff(Pf, c) - sp.diff(Rf, a),
                      sp.diff(Qf, a) - sp.diff(Pf, b)])

# ----------------------------------------------------------------------
@item("Ex 1: int_C F.dr, F = -y^2 i + x j + z^2 k, C = (y+z=2) cap (x^2+y^2=1), ccw from above")
def ex1():
    F = [-y**2, x, z**2]
    cF = curl(F)
    P("  curl F =", cF.T, "  -> (1+2y) k")
    # Surface: elliptical region in y+z=2, z = g(x,y) = 2 - y, upward, D = unit disk
    g = 2 - y
    Pc, Qc, Rc = [sp.simplify(c) for c in cF]
    integrand = sp.simplify(-Pc*g.diff(x) - Qc*g.diff(y) + Rc)
    P("  Eq 16.7.10 integrand =", integrand)
    pol = integrand.subs({x: r*sp.cos(th), y: r*sp.sin(th)})
    I = sp.integrate(sp.integrate(pol*r, (r, 0, 1)), (th, 0, 2*sp.pi))
    P("  surface integral =", sp.simplify(I), "  textbook pi =", sp.pi,
      "  match:", sp.simplify(I - sp.pi) == 0)
    # cross-check: direct line integral over the ellipse
    R = sp.Matrix([sp.cos(t), sp.sin(t), 2 - sp.sin(t)])
    Fon = sp.Matrix([-R[1]**2, R[0], R[2]**2])
    J = sp.integrate(sp.simplify(Fon.dot(R.diff(t))), (t, 0, 2*sp.pi))
    P("  direct line integral (independent 2nd method) =", sp.simplify(J))

# ----------------------------------------------------------------------
@item("Ex 2: iint_S curl F . dS, F = xz i + yz j + xy k, S = sphere r=2 inside cyl x^2+y^2=1, z>0")
def ex2():
    F = [x*z, y*z, x*y]
    cF = curl(F)
    P("  curl F =", cF.T, "  -> (x-y) i + (x-y) j")
    # boundary curve C: x^2+y^2=1, z = sqrt(3)
    P("  boundary: x^2+y^2=1 and x^2+y^2+z^2=4  ->  z^2 = 3, z = sqrt(3)")
    R = sp.Matrix([sp.cos(t), sp.sin(t), sp.sqrt(3)])
    Fon = sp.Matrix([R[0]*R[2], R[1]*R[2], R[0]*R[1]])
    dot = sp.simplify(Fon.dot(R.diff(t)))
    P("  F(r(t)) . r'(t) =", dot)
    I = sp.integrate(dot, (t, 0, 2*sp.pi))
    P("  Solution 1 (line integral) =", sp.simplify(I))
    # Solution 2: replace S by the flat disk S1 at z = sqrt(3), n = k
    P("  Solution 2: on S1 (z=sqrt3, n=k):  curl F . k =", sp.simplify(cF[2]), " -> integral 0")
    P("  textbook 0;  match:", sp.simplify(I) == 0)
    # Third check: direct surface integral over the spherical cap (parametric)
    ph = sp.Symbol('phi', positive=True)
    a = 2
    Rs = sp.Matrix([a*sp.sin(ph)*sp.cos(th), a*sp.sin(ph)*sp.sin(th), a*sp.cos(ph)])
    n = Rs.diff(ph).cross(Rs.diff(th))            # outward (upward on the cap)
    cFs = cF.subs({x: Rs[0], y: Rs[1], z: Rs[2]})
    integ = sp.simplify(cFs.dot(n))
    ph_max = sp.asin(sp.Rational(1, 2))           # sin phi = 1/2  (rho=2, cylinder radius 1)
    K = sp.integrate(sp.integrate(integ, (th, 0, 2*sp.pi)), (ph, 0, ph_max))
    P("  direct surface integral over the spherical cap (3rd method) =", sp.simplify(K))

# ----------------------------------------------------------------------
@item("Green's Theorem as the flat special case of Stokes (16.5.12)")
def flat():
    Pf, Qf = sp.Function('P')(x, y), sp.Function('Q')(x, y)
    cF = curl([Pf, Qf, 0])
    P("  curl(P i + Q j) . k =", sp.simplify(cF[2]), "  -> Q_x - P_y  (Green)")

# ----------------------------------------------------------------------
@item("Eq (4): circulation form of curl")
def eq4():
    P("  curl v(P0) . n(P0) = lim_{a->0} (1/(pi a^2)) int_{C_a} v . dr")
    P("  [Stewart prints 1/(pi a^2); the pdftotext extract loses the pi -- see ERRATA]")
    P("  since A(S_a) = pi a^2 and int_{C_a} v.dr ~ curl v(P0).n(P0) * pi a^2")

P("=" * 70); P("done")
