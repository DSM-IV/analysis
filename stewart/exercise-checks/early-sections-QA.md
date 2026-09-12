# Stewart early-section content QA

Source: local *Calculus*, 9th edition, English PDF. Exercise pages were rendered with Poppler and visually compared before authoring. Statements and explanations are independently written in Korean and English.

| Content file | Main numbers | Printed pages | PDF pages |
|---|---:|---|---|
| s12-6.json | 1–55 | 919–921 | 956–958 |
| s12-7.json (Review Exercises) | 1–38 | 922–924 | 959–961 |
| s12-8.json (Problems Plus) | 1–8 | 925–926 | 962–963 |
| s14-1.json | 1–81 | 984–989 | 1021–1026 |
| s14-2.json | 1–59 | 998–999 | 1035–1036 |
| s14-3.json | 1–101 | 1007–1011 | 1044–1048 |

Total: 342 main exercises, all subparts addressed, 142 attached original SVGs. Existing §14.3 exercises 9–16 were preserved. The Chapter 12 True–False Quiz is a separately numbered book component and is not part of the assigned Review Exercises.

## Verification

`early-math-verify.py` passes 42 independent algebra, differentiation, path-limit, geometry, and numerical-quadrature checks, plus all 6 complete-numbering checks and 1,710 English-language separation checks. It also validates all six documents through the production schema and parses all 142 attached SVGs as XML. Machine-readable results are in `early-math-verification.json` (1,758 recorded assertions).

The mathematical checks include completed squares, partial derivatives and mixed derivatives, the inverse-radius Laplace equation, Gaussian diffusion, the §14.3.101 mixed-partial counterexample, line/plane geometry, the Problems Plus ruled hyperboloid, internal sphere tangency, friction thresholds, and numerical quadrature of the three-shadow solid.

Source visual QA also included printed 974 / PDF 1011 (wind-chill and production-data tables) and printed 978 / PDF 1015 (the terrain map). §14.1.81 includes all 24 original production-data rows, all 24 log-transformed rows, and calculated least-squares coefficients.

Chrome rendering was visually inspected for the composite §14.1.53 graph/contour SVG, §14.3.94 surface/trace/tangent SVG, and Chapter 12 Problems Plus 8 solid. The first inspection found an excessively narrow plotted window in §14.1.53; the final surface uses 0≤z≤4. §14.3.94 explicitly labels its vertical display scale z/4. Long graph titles wrap. Multisurface graphs distinguish later components by color.

## Source and interpretation notes

- §14.3.39: the printed real logarithm has a negative argument at the supplied point (1,2,2). The derivative is undefined as a real derivative. The solution explicitly distinguishes the formally differentiated/absolute-value variant that would yield 1/6; it does not silently change the printed problem.
- §14.3.19 and 48 retain the source parameter b, not Greek beta. Mixed derivative subscripts separate TeX tokens so `theta r` does not become an invalid command.
- The Chapter 12 Problems Plus 3 finite-parameter ruled family omits one limiting generator; its closure is the usual hyperboloid. This omission does not change enclosed volume.
- Problems Plus 7 gives the finite upper-force formula only in its physically valid angular range; otherwise there is no finite upper threshold.
- Problems Plus 8 distinguishes the infimum 0 for positive-volume solids from an actual zero-volume boundary set.
- Graph-only exercises do not uniquely determine an analytic function. Where a qualitative explanatory model is plotted (for example §14.1.38, 41–44 and §14.3.4–6, 69, 72, 74), the caption says it is an illustrative model rather than a recovered source formula. Numerical contour-map readings are explicitly approximate.

## Reproduction

Run with `/opt/homebrew/bin/python3` from the repository root, in this order:

1. `stewart/exercise-checks/s12-6-author.py`
2. `stewart/exercise-checks/s12-7-author.py`
3. `stewart/exercise-checks/s12-8-author.py`
4. `stewart/exercise-checks/s12-review-graphs.py`
5. `stewart/exercise-checks/s14-1-graphs.py` (executes its author script first)
6. `stewart/exercise-checks/s14-2-author.py`
7. `stewart/exercise-checks/s14-3-finish.py` (executes its author script, preserving existing 9–16)
8. `stewart/exercise-checks/s14-3-graphs.py`
9. `stewart/exercise-checks/early-math-verify.py`

`early_helpers.py` and `early_plots.py` provide deterministic wireframes, domain shading, and marching-triangle contours without plotting-library dependencies. Production manifest, builder, and indexes are owned by the coordinating agent and were not edited by this content agent.
