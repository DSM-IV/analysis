# 선형대수학 2 기준값 (GROUND-TRUTH)

sympy 정확산술로 산출 (스크립트: scratchpad/gt_la2.py 재생성 가능). 풀이 에이전트 anchor용 — 불일치 시 직접 재계산으로 판정하고 보고할 것.
기저 순서: 다항식은 표준순서기저 {1, x, x^2, …}, M_{2x2}는 {E11, E12, E21, E22}. 고유벡터 기저는 유일하지 않음(스칼라배·선택 자유).

```
L2 Example 1: A v1 = [-2, 2]  A v2 = [15, 20]

=== L2 Example 1 A=(1 3;4 2) ===
A = [[1, 3], [4, 2]]
char poly det(A - tI) = (t - 5)*(t + 2)   expanded: t**2 - 3*t - 10
eigenvalues (mult): {5: 1, -2: 1}
  lambda=5: mult 1, dim E = 1, basis of E: [[3/4, 1]]
  lambda=-2: mult 1, dim E = 1, basis of E: [[-1, 1]]
diagonalizable over R : True
Q = [[-1, 3], [1, 4]]  D = [[-2, 0], [0, 5]]  check Q^-1 A Q == D: True

Reflection about y=2x, std matrix: [[-3/5, 4/5], [4/5, 3/5]]  R(1,2)= [1, 2]  R(2,-1)= [-2, 1]  R(-2,1)= [2, -1]

=== 5.1 #3(b) ===
A = [[0, -2, -3], [-1, 1, -1], [2, 2, 5]]
char poly det(A - tI) = -(t - 3)*(t - 2)*(t - 1)   expanded: -t**3 + 6*t**2 - 11*t + 6
eigenvalues (mult): {3: 1, 2: 1, 1: 1}
  lambda=3: mult 1, dim E = 1, basis of E: [[-1, 0, 1]]
  lambda=2: mult 1, dim E = 1, basis of E: [[-1, 1, 0]]
  lambda=1: mult 1, dim E = 1, basis of E: [[-1, -1, 1]]
diagonalizable over R : True
Q = [[-1, -1, -1], [-1, 1, 0], [1, 0, 1]]  D = [[1, 0, 0], [0, 2, 0], [0, 0, 3]]  check Q^-1 A Q == D: True

=== 5.1 #3(d) ===
A = [[2, 0, -1], [4, 1, -4], [2, 0, -1]]
char poly det(A - tI) = -t*(t - 1)**2   expanded: -t**3 + 2*t**2 - t
eigenvalues (mult): {1: 2, 0: 1}
  lambda=1: mult 2, dim E = 2, basis of E: [[0, 1, 0], [1, 0, 1]]
  lambda=0: mult 1, dim E = 1, basis of E: [[1/2, 2, 1]]
diagonalizable over R : True
Q = [[1, 0, 1], [4, 1, 0], [2, 0, 1]]  D = [[0, 0, 0], [0, 1, 0], [0, 0, 1]]  check Q^-1 A Q == D: True

5.1 #4(e) [T]_beta, beta={1,x,x^2}: [[1, 3, 9], [1, 3, 4], [0, 0, 2]]

=== 5.1 #4(e) ===
A = [[1, 3, 9], [1, 3, 4], [0, 0, 2]]
char poly det(A - tI) = -t*(t - 4)*(t - 2)   expanded: -t**3 + 6*t**2 - 8*t
eigenvalues (mult): {2: 1, 4: 1, 0: 1}
  lambda=2: mult 1, dim E = 1, basis of E: [[-3/4, -13/4, 1]]
  lambda=4: mult 1, dim E = 1, basis of E: [[1, 1, 0]]
  lambda=0: mult 1, dim E = 1, basis of E: [[-3, 1, 0]]
diagonalizable over R : True
Q = [[-3, -3, 1], [1, -13, 1], [0, 4, 0]]  D = [[0, 0, 0], [0, 2, 0], [0, 0, 4]]  check Q^-1 A Q == D: True
  lambda=2: eigen-polynomial x**2 - 13*x/4 - 3/4
  lambda=4: eigen-polynomial x + 1
  lambda=0: eigen-polynomial x - 3

5.1 #4(g) [T]_beta, beta={1,x,x^2,x^3}: [[-1, -2, -2, -8], [0, 1, 0, 6], [0, 0, 2, 0], [0, 0, 0, 3]]

=== 5.1 #4(g) ===
A = [[-1, -2, -2, -8], [0, 1, 0, 6], [0, 0, 2, 0], [0, 0, 0, 3]]
char poly det(A - tI) = (t - 3)*(t - 2)*(t - 1)*(t + 1)   expanded: t**4 - 5*t**3 + 5*t**2 + 5*t - 6
eigenvalues (mult): {3: 1, 1: 1, 2: 1, -1: 1}
  lambda=3: mult 1, dim E = 1, basis of E: [[-7/2, 3, 0, 1]]
  lambda=1: mult 1, dim E = 1, basis of E: [[-1, 1, 0, 0]]
  lambda=2: mult 1, dim E = 1, basis of E: [[-2/3, 0, 1, 0]]
  lambda=-1: mult 1, dim E = 1, basis of E: [[1, 0, 0, 0]]
diagonalizable over R : True
Q = [[1, -1, -2, -7], [0, 1, 0, 6], [0, 0, 3, 0], [0, 0, 0, 2]]  D = [[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 2, 0], [0, 0, 0, 3]]  check Q^-1 A Q == D: True
  lambda=3: eigen-polynomial x**3 + 3*x - 7/2
  lambda=1: eigen-polynomial x - 1
  lambda=2: eigen-polynomial x**2 - 2/3
  lambda=-1: eigen-polynomial 1

5.1 #4(j) [T]_beta, beta={E11,E12,E21,E22}: [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]

=== 5.1 #4(j) ===
A = [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]
char poly det(A - tI) = (t - 5)*(t - 1)**2*(t + 1)   expanded: t**4 - 6*t**3 + 4*t**2 + 6*t - 5
eigenvalues (mult): {5: 1, 1: 2, -1: 1}
  lambda=5: mult 1, dim E = 1, basis of E: [[1, 0, 0, 1]]
  lambda=1: mult 2, dim E = 2, basis of E: [[0, 1, 1, 0], [-1, 0, 0, 1]]
  lambda=-1: mult 1, dim E = 1, basis of E: [[0, -1, 1, 0]]
diagonalizable over R : True
Q = [[0, 0, -1, 1], [-1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1]]  D = [[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 5]]  check Q^-1 A Q == D: True
  lambda=5: eigen-matrix [[1, 0], [0, 1]]
  lambda=1: eigen-matrix [[0, 1], [1, 0]]
  lambda=1: eigen-matrix [[-1, 0], [0, 1]]
  lambda=-1: eigen-matrix [[0, -1], [1, 0]]

5.1 #17(c) [T]_beta transpose operator: [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]

=== 5.1 #17(c) ===
A = [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]
char poly det(A - tI) = (t - 1)**3*(t + 1)   expanded: t**4 - 2*t**3 + 2*t - 1
eigenvalues (mult): {1: 3, -1: 1}
  lambda=1: mult 3, dim E = 3, basis of E: [[1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1]]
  lambda=-1: mult 1, dim E = 1, basis of E: [[0, -1, 1, 0]]
diagonalizable over R : True
Q = [[0, 1, 0, 0], [-1, 0, 1, 0], [1, 0, 1, 0], [0, 0, 0, 1]]  D = [[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]  check Q^-1 A Q == D: True

=== 5.2 #2(a) ===
A = [[1, 2], [0, 1]]
char poly det(A - tI) = (t - 1)**2   expanded: t**2 - 2*t + 1
eigenvalues (mult): {1: 2}
  lambda=1: mult 2, dim E = 1, basis of E: [[1, 0]]
diagonalizable over R : False

=== 5.2 #2(d) ===
A = [[7, -4, 0], [8, -5, 0], [6, -6, 3]]
char poly det(A - tI) = -(t - 3)**2*(t + 1)   expanded: -t**3 + 5*t**2 - 3*t - 9
eigenvalues (mult): {3: 2, -1: 1}
  lambda=3: mult 2, dim E = 2, basis of E: [[1, 1, 0], [0, 0, 1]]
  lambda=-1: mult 1, dim E = 1, basis of E: [[2/3, 4/3, 1]]
diagonalizable over R : True
Q = [[2, 1, 0], [4, 1, 0], [3, 0, 1]]  D = [[-1, 0, 0], [0, 3, 0], [0, 0, 3]]  check Q^-1 A Q == D: True

=== 5.2 #2(e) ===
A = [[0, 0, 1], [1, 0, -1], [0, 1, 1]]
char poly det(A - tI) = -(t - 1)*(t**2 + 1)   expanded: -t**3 + t**2 - t + 1
eigenvalues (mult): {1: 1, -I: 1, I: 1}
  lambda=1: mult 1, dim E = 1, basis of E: [[1, 0, 1]]
  lambda=-I: mult 1, dim E = 1, basis of E: [[I, -1 - I, 1]]
  lambda=I: mult 1, dim E = 1, basis of E: [[-I, -1 + I, 1]]
diagonalizable over R : False

5.2 #3(a) [T]_beta: [[0, 1, 2, 0], [0, 0, 2, 6], [0, 0, 0, 3], [0, 0, 0, 0]]

=== 5.2 #3(a) ===
A = [[0, 1, 2, 0], [0, 0, 2, 6], [0, 0, 0, 3], [0, 0, 0, 0]]
char poly det(A - tI) = t**4   expanded: t**4
eigenvalues (mult): {0: 4}
  lambda=0: mult 4, dim E = 1, basis of E: [[1, 0, 0, 0]]
diagonalizable over R : False

5.2 #3(d) [T]_beta: [[1, 0, 0], [1, 1, 1], [1, 1, 1]]

=== 5.2 #3(d) ===
A = [[1, 0, 0], [1, 1, 1], [1, 1, 1]]
char poly det(A - tI) = -t*(t - 2)*(t - 1)   expanded: -t**3 + 3*t**2 - 2*t
eigenvalues (mult): {1: 1, 2: 1, 0: 1}
  lambda=1: mult 1, dim E = 1, basis of E: [[-1, 1, 1]]
  lambda=2: mult 1, dim E = 1, basis of E: [[0, 1, 1]]
  lambda=0: mult 1, dim E = 1, basis of E: [[0, -1, 1]]
diagonalizable over R : True
Q = [[0, -1, 0], [-1, 1, 1], [1, 1, 1]]  D = [[0, 0, 0], [0, 1, 0], [0, 0, 2]]  check Q^-1 A Q == D: True
  lambda=1: eigen-polynomial x**2 + x - 1
  lambda=2: eigen-polynomial x**2 + x
  lambda=0: eigen-polynomial x**2 - x

=== 5.2 #3(e) ===
A = [[1, I], [I, 1]]
char poly det(A - tI) = t**2 - 2*t + 2   expanded: t**2 - 2*t + 2
eigenvalues (mult): {1 - I: 1, 1 + I: 1}
  lambda=1 - I: mult 1, dim E = 1, basis of E: [[-1, 1]]
  lambda=1 + I: mult 1, dim E = 1, basis of E: [[1, 1]]
diagonalizable over C : True
Q = [[-1, 1], [1, 1]]  D = [[1 - I, 0], [0, 1 + I]]  check Q^-1 A Q == D: True

=== 5.2 #7 ===
A = [[1, 4], [2, 3]]
char poly det(A - tI) = (t - 5)*(t + 1)   expanded: t**2 - 4*t - 5
eigenvalues (mult): {5: 1, -1: 1}
  lambda=5: mult 1, dim E = 1, basis of E: [[1, 1]]
  lambda=-1: mult 1, dim E = 1, basis of E: [[-2, 1]]
diagonalizable over R : True
Q = [[-2, 1], [1, 1]]  D = [[-1, 0], [0, 5]]  check Q^-1 A Q == D: True
A^n = [[2*(-1)**n/3 + 5**n/3, -2*(-1)**n/3 + 2*5**n/3], [-(-1)**n/3 + 5**n/3, (-1)**n/3 + 2*5**n/3]]
check n=1..4: True
with Q=(1 -2;1 1): Q^-1 A Q = [[5, 0], [0, -1]]

5.1 #1(j): P A P = [[1, 1], [1, 4]]  eig A: [[3/2 - sqrt(13)/2, 1]] [[3/2 + sqrt(13)/2, 1]]
5.1 #1(f): eigenvalues of diag(1,-1): {1: 1, -1: 1}
5.1 #1(c): char poly of (0 -1;1 0): t**2 + 1
```

=== Lecture 3 (9/8) 추가분 — python Fraction 검산 ===
```
L3 Example 4: A=(1 3;4 2): det(A-tI)= t^2-3t-10 = (t+2)(t-5); eigenvalues -2, 5
  A-tI correct = ((1-t, 3),(4, 2-t)); A+2I = ((3,3),(4,4)) -> x+y=0 -> v1=(1,-1); A-5I = ((-4,3),(4,-3)) -> 4x-3y=0 -> v2=(3,4)
  A v1 = [-2, 2]  A v2 = [15, 20] ; Q=(1 3;-1 4), D=diag(-2,5); det Q = 7
L3 Example 6: A=(1 1;4 1): (1-t)^2-4 = t^2-2t-3 = (t-3)(t+1); A(1,2)= [3, 6]  A(1,-2)= [-1, 2] ; Q=(1 1;2 -2), D=diag(3,-1), det Q = -4
L3 Example 5/7: [T]_B=(1 1 0;0 2 2;0 0 3), T(f)=f+(x+1)f' on P2(R): T(1)=1, T(x)=2x+1, T(x^2)=3x^2+2x; eigenvalues 1,2,3
  [T]_B [1, 0, 0] = [1, 0, 0] = 1*[1, 0, 0]
  [T]_B [1, 1, 0] = [2, 2, 0] = 2*[1, 1, 0]
  [T]_B [1, 2, 1] = [3, 6, 3] = 3*[1, 2, 1]
  Q=(1 1 1;0 1 2;0 0 1) (columns = eigenvectors), [T]_gamma = diag(1,2,3) with gamma={1, x+1, x^2+2x+1}
L3 Example B: [T_theta] = (cos -sin; sin cos): det(.. - tI) = t^2 - 2cos(theta) t + 1, discriminant 4cos^2(theta)-4 < 0 for 0<theta<pi -> no real eigenvalues
L3 Theorem 5.3: deg det(A-tI)=n, leading coeff (-1)^n (Leibniz: only identity permutation gives degree n; others degree <= n-2)
```
