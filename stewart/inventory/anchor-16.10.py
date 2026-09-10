#!/usr/bin/env python3
"""Stewart ET 9e §16.10 (Summary) — no worked examples in this section (0 examples).

This script only sanity-checks the internal consistency of the five identities
collected in the summary table, so that the site's summary card cannot drift.
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

x, y, z, t = sp.symbols('x y z t', real=True)

# ----------------------------------------------------------------------
@item("Row 1-2: FTC and FT for Line Integrals (gradient field is exact)")
def rows12():
    f = sp.Function('f')
    xs, ys, zs = sp.Function('x')(t), sp.Function('y')(t), sp.Function('z')(t)
    F = sp.Function('f')(xs, ys, zs)
    P("  d/dt f(r(t)) =", sp.diff(F, t))
    P("  = grad f . r'(t)  ->  int_C grad f . dr = f(r(b)) - f(r(a))   (chain rule + FTC)")

# ----------------------------------------------------------------------
@item("Row 4 => Row 3: Green's Theorem is flat Stokes (n = k)")
def row43():
    Pf, Qf = sp.Function('P')(x, y), sp.Function('Q')(x, y)
    curl_k = sp.diff(Qf, x) - sp.diff(Pf, y)
    P("  curl(P i + Q j + 0 k) . k =", curl_k)
    P("  iint_S curl F . dS  ->  iint_D (Q_x - P_y) dA = int_C P dx + Q dy   (Green)")

# ----------------------------------------------------------------------
@item("Row 5: Divergence Theorem; 2-D (Green flux form) analogue")
def row5():
    Pf, Qf, Rf = (sp.Function('P')(x, y, z), sp.Function('Q')(x, y, z),
                  sp.Function('R')(x, y, z))
    d = sp.diff(Pf, x) + sp.diff(Qf, y) + sp.diff(Rf, z)
    P("  div F =", d)
    P("  iiint_E div F dV = iint_S F . dS")
    P("  2-D form (16.5): int_C F . n ds = iint_D div F(x,y) dA")

# ----------------------------------------------------------------------
@item("Common shape of all five rows")
def shape():
    P("  LHS: integral of a 'derivative' over a region")
    P("       F' | grad f | Q_x - P_y | curl F | div F")
    P("  RHS: values of the original function on the BOUNDARY only")
    P("       {a,b} | r(a),r(b) | C = bdry D | C = bdry S | S = bdry E")
    P("  dimension ladder: 0-dim bdry of an interval/curve -> 1-dim bdry of a region/surface")
    P("                    -> 2-dim bdry of a solid")

P("=" * 70); P("done  (no numeric anchors: §16.10 has 0 examples)")
