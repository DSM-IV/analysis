#!/usr/bin/env python3
"""Independent recomputation of Stewart ET 9e §16.7 example answers (anchor values).
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

x, y, z, u, v, r, th, ph, a, K, C = sp.symbols('x y z u v r theta phi a K C', real=True)

# ----------------------------------------------------------------------
@item("Ex 1:  iint_S x^2 dS,  S = unit sphere")
def ex1():
    R = sp.Matrix([sp.sin(ph)*sp.cos(th), sp.sin(ph)*sp.sin(th), sp.cos(ph)])
    n = R.diff(ph).cross(R.diff(th))
    mag = sp.simplify(sp.sqrt(sum(c**2 for c in n)))
    P("  |r_phi x r_theta| =", mag, "  (= sin phi on [0,pi])")
    f = R[0]**2
    I = sp.integrate(sp.integrate(f*sp.sin(ph), (ph, 0, sp.pi)), (th, 0, 2*sp.pi))
    P("  integral =", sp.simplify(I), " textbook 4*pi/3 =", 4*sp.pi/3,
      " match:", sp.simplify(I - 4*sp.pi/3) == 0)

# ----------------------------------------------------------------------
@item("Ex 2:  iint_S y dS,  S: z = x + y^2, 0<=x<=1, 0<=y<=2")
def ex2():
    g = x + y**2
    dS = sp.sqrt(1 + g.diff(x)**2 + g.diff(y)**2)
    P("  dS factor =", sp.simplify(dS))
    I = sp.integrate(sp.integrate(y*dS, (y, 0, 2)), (x, 0, 1))
    I = sp.simplify(sp.radsimp(I))
    txt = 13*sp.sqrt(2)/3
    P("  integral =", I, " textbook 13 sqrt2/3 =", txt,
      " match:", sp.simplify(I - txt) == 0, " numeric:", float(I), float(txt))

# ----------------------------------------------------------------------
@item("Ex 3:  iint_S z dS,  S = cylinder side x^2+y^2=1 + bottom disk (z=0) + top z=1+x")
def ex3():
    # S1: side, r(th,z) = (cos th, sin th, z), 0<=z<=1+cos th
    Rs = sp.Matrix([sp.cos(th), sp.sin(th), z])
    n = Rs.diff(th).cross(Rs.diff(z))
    mag = sp.simplify(sp.sqrt(sum(c**2 for c in n)))
    P("  side |r_th x r_z| =", mag)
    I1 = sp.integrate(sp.integrate(z*1, (z, 0, 1 + sp.cos(th))), (th, 0, 2*sp.pi))
    I1 = sp.simplify(I1)
    P("  S1 =", I1, " (textbook 3*pi/2)")
    # S2: z = 0
    P("  S2 = 0  (z = 0 on the bottom disk)")
    # S3: z = 1+x over unit disk, dS = sqrt(2) dA
    I3 = sp.integrate(sp.integrate((1 + r*sp.cos(th))*sp.sqrt(2)*r, (r, 0, 1)), (th, 0, 2*sp.pi))
    I3 = sp.simplify(I3)
    P("  S3 =", I3, " (textbook sqrt2 * pi)")
    tot = sp.simplify(I1 + 0 + I3)
    txt = (sp.Rational(3, 2) + sp.sqrt(2))*sp.pi
    P("  total =", tot, " textbook (3/2 + sqrt2) pi =", txt,
      " match:", sp.simplify(tot - txt) == 0, " numeric:", float(tot))

# ----------------------------------------------------------------------
@item("Eq (5)(6) orientation; sphere outward normal n = r/a")
def orient():
    R = sp.Matrix([a*sp.sin(ph)*sp.cos(th), a*sp.sin(ph)*sp.sin(th), a*sp.cos(ph)])
    n = R.diff(ph).cross(R.diff(th))
    P("  r_phi x r_theta =", sp.simplify(n).T)
    P("  = a^2 sin^2(phi) cos(th) i + a^2 sin^2(phi) sin(th) j + a^2 sin(phi)cos(phi) k")
    nn = sp.simplify(n / (a**2*sp.sin(ph)))
    P("  n = (r_phi x r_th)/|..| =", nn.T, " = r(phi,th)/a  -> outward")

# ----------------------------------------------------------------------
@item("Ex 4:  flux of F = z i + y j + x k across unit sphere (outward)")
def ex4():
    R = sp.Matrix([sp.sin(ph)*sp.cos(th), sp.sin(ph)*sp.sin(th), sp.cos(ph)])
    F = sp.Matrix([R[2], R[1], R[0]])          # F = <z, y, x> on the sphere
    n = R.diff(ph).cross(R.diff(th))
    integ = sp.simplify(F.dot(n))
    P("  F . (r_phi x r_th) =", sp.expand_trig(sp.simplify(integ)))
    I = sp.integrate(sp.integrate(integ, (ph, 0, sp.pi)), (th, 0, 2*sp.pi))
    I = sp.simplify(I)
    txt = 4*sp.pi/3
    P("  flux =", I, " textbook 4*pi/3 =", txt, " match:", sp.simplify(I - txt) == 0)
    P("  Gauss law (11): Q = eps0 * flux = (4/3) pi eps0")

# ----------------------------------------------------------------------
@item("Ex 5:  iint_S F.dS, F = y i + x j + z k, S = bdry of E under z = 1-x^2-y^2, z>=0")
def ex5():
    g = 1 - x**2 - y**2
    Pc, Qc, Rc = y, x, g                       # R = z = g on S1
    # Eq (10): upward orientation
    integrand = -Pc*g.diff(x) - Qc*g.diff(y) + Rc
    P("  Eq(10) integrand =", sp.expand(integrand), " (= 1 + 4xy - x^2 - y^2)")
    pol = integrand.subs({x: r*sp.cos(th), y: r*sp.sin(th)})
    I1 = sp.integrate(sp.integrate(sp.simplify(pol)*r, (r, 0, 1)), (th, 0, 2*sp.pi))
    I1 = sp.simplify(I1)
    P("  S1 (upward) =", I1, " (textbook pi/2)")
    P("  S2 (disk z=0, downward n = -k): F.n = -z = 0  ->  0")
    tot = sp.simplify(I1)
    P("  total =", tot, " textbook pi/2 =", sp.pi/2,
      " match:", sp.simplify(tot - sp.pi/2) == 0)

# ----------------------------------------------------------------------
@item("Ex 6:  heat flow across sphere of radius a, u = C(x^2+y^2+z^2)")
def ex6():
    uf = C*(x**2 + y**2 + z**2)
    grad = sp.Matrix([uf.diff(x), uf.diff(y), uf.diff(z)])
    F = -K*grad
    P("  F = -K grad u =", F.T)
    n = sp.Matrix([x, y, z])/a
    Fn = sp.simplify(F.dot(n))
    P("  F . n =", Fn, "  on x^2+y^2+z^2=a^2  ->", sp.simplify(Fn.subs(x**2 + y**2 + z**2, a**2)))
    Fn_on_S = -2*K*C*a
    A = 4*sp.pi*a**2
    P("  flux = (F.n) * A(S) =", sp.simplify(Fn_on_S*A),
      " textbook -8 K C pi a^3 =", -8*K*C*sp.pi*a**3,
      " match:", sp.simplify(Fn_on_S*A + 8*K*C*sp.pi*a**3) == 0)

P("=" * 70); P("done")
