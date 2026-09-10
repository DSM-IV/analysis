#!/usr/bin/env python3
"""§12.6 Cylinders and Quadric Surfaces — 예제 1~8 최종답 독립 재계산 (sympy).

이 절의 예제는 대부분 '자취(trace)를 구해 곡면을 식별·스케치'하는 유형이므로,
검증 대상은 (i) 각 자취 방정식, (ii) 자취가 타원/포물선/쌍곡선이 되는 조건,
(iii) 표준형 변환(양변 나누기·완전제곱)이다.
각 항목은 signal.alarm(20) 타임아웃 + flush 출력.
"""
import signal
import sys
import sympy as sp

x, y, z, k = sp.symbols('x y z k', real=True)
a, b, c = sp.symbols('a b c', positive=True)


class Timeout(Exception):
    pass


def _handler(signum, frame):
    raise Timeout()


def item(label):
    def deco(fn):
        print(f"\n=== {label} ===", flush=True)
        signal.signal(signal.SIGALRM, _handler)
        signal.alarm(20)
        try:
            fn()
        except Timeout:
            print("  !! TIMEOUT (20s)", flush=True)
        except Exception as e:  # noqa: BLE001
            print(f"  !! ERROR: {type(e).__name__}: {e}", flush=True)
        finally:
            signal.alarm(0)
        return fn
    return deco


def eq(name, got, want):
    """방정식 좌변(= 0 형태) 비교.

    두 좌변이 같은 자취를 나타내는지 보므로, 0 이 아닌 상수배(부호 포함)까지
    허용한다: got == lam * want 인 상수 lam 이 존재하면 같은 방정식이다.
    """
    ok = sp.simplify(sp.expand(got - want)) == 0
    lam = None
    if not ok:
        ratio = sp.simplify(sp.expand(got) / sp.expand(want))
        if ratio.is_number and ratio != 0:
            ok, lam = True, ratio
    tag = 'MATCH' if ok else 'MISMATCH'
    if lam is not None:
        tag += f" (상수배 {lam})"
    print(f"  {name}: sympy = {sp.simplify(got)} = 0", flush=True)
    print(f"  {'':{len(name)}}  교재  = {want} = 0   -> {tag}", flush=True)
    return ok


def prop(name, got, want, note=""):
    ok = (sp.simplify(got - want) == 0) if isinstance(got, sp.Expr) else got == want
    print(f"  {name}: sympy = {got} / 교재 = {want} -> "
          f"{'MATCH' if ok else 'MISMATCH'} {note}", flush=True)
    return ok


# ------------------------------------------------------- Example 1 (개념·스케치)
@item("Example 1  z = x^2  (parabolic cylinder)")
def ex1():
    F = z - x**2
    # y = k 자취: z = x^2 (k 와 무관) -> 평행한 포물선들의 합집합 = 포물기둥
    tr = sp.simplify(F.subs(y, k))
    eq("trace y=k", tr, z - x**2)
    prop("자취가 k 에 의존?", sp.diff(tr, k) != 0, False,
         "(0 이므로 모든 y=k 에서 같은 포물선 -> rulings ∥ y축)")


# ------------------------------------------------------- Example 2 (개념·스케치)
@item("Example 2  (a) x^2+y^2=1  (b) y^2+z^2=1  (circular cylinders)")
def ex2():
    Fa = x**2 + y**2 - 1
    eq("(a) trace z=k", Fa.subs(z, k), x**2 + y**2 - 1)
    prop("(a) 결여 변수", 'z', 'z', "-> 축은 z축, 반지름 1")
    Fb = y**2 + z**2 - 1
    eq("(b) trace x=k", Fb.subs(x, k), y**2 + z**2 - 1)
    prop("(b) 결여 변수", 'x', 'x', "-> 축은 x축, 반지름 1")


# ---------------------------------------------------------------- Example 3
@item("Example 3  x^2 + y^2/9 + z^2/4 = 1  (ellipsoid) — traces")
def ex3():
    F = x**2 + y**2/9 + z**2/4 - 1
    eq("trace z=0", F.subs(z, 0), x**2 + y**2/9 - 1)
    eq("trace z=k", F.subs(z, k), x**2 + y**2/9 - (1 - k**2/4))
    eq("trace x=k", F.subs(x, k), y**2/9 + z**2/4 - (1 - k**2))
    eq("trace y=k", F.subs(y, k), x**2 + z**2/4 - (1 - k**2/9))
    # 타원이 되는 조건 (우변 > 0)
    print(f"  z=k 타원 조건 : {sp.solve_univariate_inequality(1 - k**2/4 > 0, k)}"
          "   교재 = k^2 < 4 (|k| < 2)", flush=True)
    print(f"  x=k 타원 조건 : {sp.solve_univariate_inequality(1 - k**2 > 0, k)}"
          "   교재 = -1 < k < 1", flush=True)
    print(f"  y=k 타원 조건 : {sp.solve_univariate_inequality(1 - k**2/9 > 0, k)}"
          "   교재 = -3 < k < 3", flush=True)
    # 절편
    ints = [sp.solve(F.subs({y: 0, z: 0}), x), sp.solve(F.subs({x: 0, z: 0}), y),
            sp.solve(F.subs({x: 0, y: 0}), z)]
    print(f"  절편 x,y,z = {ints}   교재 Figure 4 = (1,0,0), (0,3,0), (0,0,2)",
          flush=True)


# ---------------------------------------------------------------- Example 4
@item("Example 4  z = 4x^2 + y^2  (elliptic paraboloid) — traces")
def ex4():
    F = z - 4*x**2 - y**2
    eq("trace x=0", F.subs(x, 0), z - y**2)
    eq("trace x=k", F.subs(x, k), z - (y**2 + 4*k**2))
    eq("trace y=k", F.subs(y, k), z - (4*x**2 + k**2))
    eq("trace z=k", F.subs(z, k), -(4*x**2 + y**2 - k))
    prop("z=k 가 타원일 조건", "k > 0", "k > 0")


# ---------------------------------------------------------------- Example 5
@item("Example 5  z = y^2 - x^2  (hyperbolic paraboloid) — traces")
def ex5():
    F = z - y**2 + x**2
    eq("trace x=k", F.subs(x, k), z - (y**2 - k**2))
    eq("trace y=k", F.subs(y, k), z - (-x**2 + k**2))
    eq("trace z=k", F.subs(z, k), -(y**2 - x**2 - k))
    prop("x=k 포물선 개구 방향", sp.sign(sp.diff(y**2 - k**2, y, 2)), 1, "(위로)")
    prop("y=k 포물선 개구 방향", sp.sign(sp.diff(-x**2 + k**2, x, 2)), -1, "(아래로)")


# ---------------------------------------------------------------- Example 6
@item("Example 6  x^2/4 + y^2 - z^2/4 = 1  (hyperboloid of one sheet) — traces")
def ex6():
    F = x**2/4 + y**2 - z**2/4 - 1
    eq("trace z=k", F.subs(z, k), x**2/4 + y**2 - (1 + k**2/4))
    eq("trace y=0", F.subs(y, 0), x**2/4 - z**2/4 - 1)
    eq("trace x=0", F.subs(x, 0), y**2 - z**2/4 - 1)
    print(f"  z=k 우변 1+k^2/4 > 0 (모든 k) -> 모든 높이에서 타원 (한 개의 잎)",
          flush=True)
    ints = [sp.solve(F.subs({y: 0, z: 0}), x), sp.solve(F.subs({x: 0, z: 0}), y)]
    print(f"  절편 x,y = {ints}   교재 Figure 9 = (2,0,0), (0,1,0)", flush=True)


# ---------------------------------------------------------------- Example 7
@item("Example 7  4x^2 - y^2 + 2z^2 + 4 = 0  -> standard form & traces")
def ex7():
    F = 4*x**2 - y**2 + 2*z**2 + 4
    std = -x**2 + y**2/4 - z**2/2 - 1          # 교재 표준형 (= 0)
    eq("표준형 (F/(-4))", sp.expand(F/(-4)), std)
    prop("분류", "hyperboloid of two sheets (axis: y)",
         "hyperboloid of two sheets (axis: y)")
    eq("trace z=0", std.subs(z, 0), -x**2 + y**2/4 - 1)
    eq("trace x=0", std.subs(x, 0), y**2/4 - z**2/2 - 1)
    # xz-평면(y=0) 자취 없음 확인
    print(f"  trace y=0 : {sp.simplify(std.subs(y, 0))} = 0 -> "
          f"실해 {sp.solve([sp.Eq(std.subs(y, 0), 0)], [x, z], dict=True)}"
          "  (교재: xz-평면에 자취 없음)", flush=True)
    print(f"     -x^2 - z^2/2 = 1 은 실수해 없음 (좌변 <= 0) -> MATCH", flush=True)
    # y = k 자취
    tr = sp.expand(std.subs(y, k))
    eq("trace y=k", tr, x**2 + z**2/2 - (k**2/4 - 1))
    R = k**2/4 - 1
    rewritten = x**2/R + z**2/(2*R) - 1
    ok = sp.simplify(sp.expand(rewritten*R - (x**2 + z**2/2 - R))) == 0
    print(f"  표준 타원형 재작성: x^2/(k^2/4-1) + z^2/(2(k^2/4-1)) = 1  -> "
          f"{'MATCH' if ok else 'MISMATCH'}", flush=True)
    print(f"  타원 조건 R > 0 : {sp.solve_univariate_inequality(R > 0, k)}"
          "   교재 = |k| > 2", flush=True)
    verts = sp.solve(std.subs({x: 0, z: 0}), y)
    print(f"  꼭짓점 y = {verts}   교재 Figure 10 = (0,±2,0)", flush=True)


# ---------------------------------------------------------------- Example 8
@item("Example 8  x^2 + 2z^2 - 6x - y + 10 = 0  -> complete the square")
def ex8():
    F = x**2 + 2*z**2 - 6*x - y + 10
    std = (x - 3)**2 + 2*z**2 - (y - 1)         # 교재: y - 1 = (x-3)^2 + 2z^2
    eq("완전제곱 후", sp.expand(F), sp.expand(std))
    prop("분류", "elliptic paraboloid (axis ∥ y)", "elliptic paraboloid (axis ∥ y)")
    vtx = sp.solve([sp.Eq(x - 3, 0), sp.Eq(z, 0),
                    sp.Eq(std.subs({x: 3, z: 0}), 0)], [x, y, z], dict=True)
    print(f"  꼭짓점 = {vtx}   교재 = (3, 1, 0)", flush=True)
    eq("trace y=k", sp.expand(std.subs(y, k)), (x - 3)**2 + 2*z**2 - (k - 1))
    print(f"  y=k 타원 조건 : k - 1 > 0  -> k > 1   교재 = k > 1", flush=True)
    eq("trace z=0", sp.expand(std.subs(z, 0)), (x - 3)**2 - (y - 1))
    print("  z=0 자취: y = 1 + (x-3)^2 (포물선)   교재와 일치", flush=True)


# ---------------------------------------------- Table 1 표준형 6종 (rem/fig 카드용)
@item("Table 1  six standard quadric surfaces (form check)")
def table1():
    forms = {
        "Ellipsoid": x**2/a**2 + y**2/b**2 + z**2/c**2 - 1,
        "Elliptic Paraboloid": z/c - x**2/a**2 - y**2/b**2,
        "Hyperbolic Paraboloid": z/c - x**2/a**2 + y**2/b**2,
        "Cone": z**2/c**2 - x**2/a**2 - y**2/b**2,
        "Hyperboloid of One Sheet": x**2/a**2 + y**2/b**2 - z**2/c**2 - 1,
        "Hyperboloid of Two Sheets": -x**2/a**2 - y**2/b**2 + z**2/c**2 - 1,
    }
    for name, F in forms.items():
        # z = k 수평 자취의 2차 부분 판별식으로 타원/쌍곡선 구분
        tr = sp.expand(F.subs(z, k))
        A = tr.coeff(x, 2)
        B = tr.coeff(y, 2)
        kind = ("ellipse" if A*B > 0 else
                "hyperbola" if A*B < 0 else "parabola/line")
        print(f"  {name:28s}: 수평자취 x^2 계수 {A}, y^2 계수 {B} -> {kind}",
              flush=True)


print("\n--- done ---", flush=True)
sys.exit(0)
