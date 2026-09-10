#!/usr/bin/env python3
"""Independent recomputation of Stewart ET 9e §16.6 example answers (anchor values).

Each item runs under a 20 s SIGALRM timeout; every print is flushed.
Run:  python3 anchor-16.6.py
"""
import signal, sys, traceback
import sympy as sp

def P(*a):
    print(*a, flush=True)

class TO(Exception):
    pass

def _h(sig, frm):
    raise TO()

signal.signal(signal.SIGALRM, _h)

def item(name):
    def deco(fn):
        P("=" * 70)
        P(f"[{name}]")
        signal.alarm(20)
        try:
            fn()
        except TO:
            P("  !! TIMEOUT (20s)")
        except Exception:
            P("  !! ERROR")
            traceback.print_exc()
        finally:
            signal.alarm(0)
        return fn
    return deco

u, v, x, y, z, r, th, ph, a, t = sp.symbols('u v x y z r theta phi a t', real=True)

# ----------------------------------------------------------------------
@item("Ex 1: r(u,v) = <2cos u, v, 2 sin u>  ->  x^2+z^2 = 4 (cylinder about y-axis)")
def ex1():
    X, Y, Z = 2*sp.cos(u), v, 2*sp.sin(u)
    P("  x^2 + z^2 =", sp.simplify(X**2 + Z**2))
    P("  y = v unrestricted -> full circular cylinder, radius 2, axis = y-axis")

# ----------------------------------------------------------------------
@item("Ex 2: r(u,v) = <(2+sin v)cos u, (2+sin v)sin u, u + cos v>  grid curves")
def ex2():
    X = (2 + sp.sin(v))*sp.cos(u)
    Y = (2 + sp.sin(v))*sp.sin(u)
    Z = u + sp.cos(v)
    P("  x^2 + y^2 =", sp.simplify(X**2 + Y**2), " (= (2+sin v)^2, indep. of u)")
    P("  v = v0 fixed: radius const, z = u + const  ->  helix/spiral curve")
    P("  u = u0 fixed: z = u0 + cos v in [u0-1, u0+1], (x,y) direction fixed")
    P("    -> circle of radius (2+sin v) traced in the vertical plane theta=u0")

# ----------------------------------------------------------------------
@item("Ex 3: plane r(u,v) = r0 + u a + v b  (verify normal a x b)")
def ex3():
    a1, a2, a3, b1, b2, b3, x0, y0, z0 = sp.symbols('a1 a2 a3 b1 b2 b3 x0 y0 z0', real=True)
    A = sp.Matrix([a1, a2, a3]); B = sp.Matrix([b1, b2, b3]); R0 = sp.Matrix([x0, y0, z0])
    R = R0 + u*A + v*B
    P("  r(u,v) =", list(R.T))
    ru = R.diff(u); rv = R.diff(v)
    P("  r_u x r_v =", list(ru.cross(rv).T), " = a x b (constant) -> plane")

# ----------------------------------------------------------------------
@item("Ex 4: sphere x^2+y^2+z^2=a^2  ->  <a sin(phi)cos(th), a sin(phi)sin(th), a cos(phi)>")
def ex4():
    X = a*sp.sin(ph)*sp.cos(th); Y = a*sp.sin(ph)*sp.sin(th); Z = a*sp.cos(ph)
    P("  x^2+y^2+z^2 =", sp.simplify(X**2 + Y**2 + Z**2))
    P("  domain D = [0,pi] x [0,2pi]  (phi in [0,pi], theta in [0,2pi])")

# ----------------------------------------------------------------------
@item("Ex 5: cylinder x^2+y^2=4, 0<=z<=1  ->  <2cos th, 2 sin th, z>")
def ex5():
    X = 2*sp.cos(th); Y = 2*sp.sin(th)
    P("  x^2+y^2 =", sp.simplify(X**2 + Y**2))
    P("  domain: 0<=theta<=2pi, 0<=z<=1")

# ----------------------------------------------------------------------
@item("Ex 6: elliptic paraboloid z = x^2+2y^2  ->  r(x,y) = <x, y, x^2+2y^2>")
def ex6():
    P("  z - (x^2+2y^2) =", sp.simplify(x**2 + 2*y**2 - (x**2 + 2*y**2)))
    P("  r(x,y) = x i + y j + (x^2+2y^2) k")

# ----------------------------------------------------------------------
@item("Ex 7: cone z = 2 sqrt(x^2+y^2)  two parametrizations")
def ex7():
    # Sol 1
    P("  Sol1: r(x,y) = <x, y, 2 sqrt(x^2+y^2)>")
    # Sol 2
    X = r*sp.cos(th); Y = r*sp.sin(th); Z = 2*r
    chk = sp.simplify(Z**2 - 4*(X**2 + Y**2))
    P("  Sol2: r(r,th) = <r cos th, r sin th, 2r>;  z^2 - 4(x^2+y^2) =", chk)
    P("  (r >= 0, 0<=theta<=2pi);  part below z=1  ->  0 <= r <= 1/2")

# ----------------------------------------------------------------------
@item("Ex 8: revolve y = sin x, 0<=x<=2pi, about x-axis")
def ex8():
    X = x; Y = sp.sin(x)*sp.cos(th); Z = sp.sin(x)*sp.sin(th)
    P("  y^2+z^2 =", sp.simplify(Y**2 + Z**2), " ( = sin^2 x ) OK")
    P("  x=x, y=sin x cos th, z=sin x sin th; 0<=x<=2pi, 0<=th<=2pi")

# ----------------------------------------------------------------------
@item("Ex 9: tangent plane to x=u^2, y=v^2, z=u+2v at (1,1,3)")
def ex9():
    R = sp.Matrix([u**2, v**2, u + 2*v])
    ru = R.diff(u); rv = R.diff(v)
    P("  r_u =", list(ru.T), "  r_v =", list(rv.T))
    n = ru.cross(rv)
    P("  r_u x r_v =", list(n.T))
    n0 = n.subs({u: 1, v: 1})
    P("  at (u,v)=(1,1):  n =", list(n0.T))
    X, Y, Z = sp.symbols('X Y Z')
    plane = sp.expand(n0.dot(sp.Matrix([X - 1, Y - 1, Z - 3])))
    P("  plane:", sp.Eq(plane, 0), "  -> normalized:", sp.Eq(sp.simplify(plane/-2), 0))
    P("  i.e.  x + 2y - 2z + 3 = 0")

# ----------------------------------------------------------------------
@item("Ex 10: surface area of sphere of radius a")
def ex10():
    R = sp.Matrix([a*sp.sin(ph)*sp.cos(th), a*sp.sin(ph)*sp.sin(th), a*sp.cos(ph)])
    rp = R.diff(ph); rt = R.diff(th)
    n = rp.cross(rt)
    mag = sp.simplify(sp.sqrt(sum(c**2 for c in n)))
    P("  |r_phi x r_theta| =", mag, " (= a^2 sin phi for a>0, 0<=phi<=pi)")
    mag2 = a**2*sp.sin(ph)          # a>0
    A = sp.integrate(sp.integrate(mag2, (ph, 0, sp.pi)), (th, 0, 2*sp.pi))
    P("  A =", sp.simplify(A))

# ----------------------------------------------------------------------
@item("Ex 11: area of z = x^2+y^2 below z = 9")
def ex11():
    f = x**2 + y**2
    integrand = sp.sqrt(1 + f.diff(x)**2 + f.diff(y)**2)
    P("  integrand =", sp.simplify(integrand), " -> sqrt(1+4(x^2+y^2))")
    # polar
    A = sp.integrate(sp.integrate(sp.sqrt(1 + 4*r**2)*r, (r, 0, 3)), (th, 0, 2*sp.pi))
    A = sp.simplify(A)
    P("  A =", A, " = ", sp.nsimplify(A))
    txt = sp.pi/6*(37*sp.sqrt(37) - 1)
    P("  textbook  pi/6 (37 sqrt37 - 1) =", txt)
    P("  match:", sp.simplify(A - txt) == 0, "  numeric:", float(A), float(txt))

# ----------------------------------------------------------------------
@item("Eq (7)(8)(9) check:  r_x x r_y for z=f(x,y)")
def eq789():
    f = sp.Function('f')(x, y)
    R = sp.Matrix([x, y, f])
    rx = R.diff(x); ry = R.diff(y)
    n = rx.cross(ry)
    P("  r_x x r_y =", list(n.T), " = <-f_x, -f_y, 1>")
    P("  |r_x x r_y| = sqrt(f_x^2+f_y^2+1)  -> Eq (8)")
    P("  A(S) = int int_D sqrt(1+(dz/dx)^2+(dz/dy)^2) dA  -> Eq (9)")

# ----------------------------------------------------------------------
@item("Consistency: Def 6 reduces to the single-variable surface-of-revolution formula (8.2.4)")
def rev():
    F = sp.Function('f')(x)
    R = sp.Matrix([x, F*sp.cos(th), F*sp.sin(th)])
    rx = R.diff(x); rt = R.diff(th)
    n = rx.cross(rt)
    mag = sp.simplify(sum(c**2 for c in n))
    P("  |r_x x r_th|^2 =", sp.simplify(sp.factor(mag)))
    P("  = f(x)^2 (1 + f'(x)^2)  ->  |..| = f(x) sqrt(1+f'(x)^2)  (f>=0)")
    P("  A = int_0^{2pi} int_a^b f sqrt(1+f'^2) dx dth = 2 pi int_a^b f sqrt(1+f'^2) dx")

P("=" * 70)
P("done")
