# Worked-example explanation QA — 2026-09-26

Coverage: all 181 existing textbook worked examples in 27 sections: 12.6,
14.1–14.8, 15.1–15.9, and 16.1–16.9. Each has a Korean and English
supplement inside its existing solution toggle (362 panels).

The additions explain intermediate calculations, assumptions, equality and
boundary cases, orientation, geometric checks, and alternative derivations.
They supplement the existing independently written solutions.

## Maintenance

Edit `../example-details.json` and run:

```sh
python3 stewart/build_example_details.py
python3 stewart/build_example_details.py --check
python3 stewart/example-checks/check_math.py
```

The builder uses only the standard library. It requires exactly one solution
panel per language for every example, validates source coverage and math
delimiters, inserts before any final QED, and preserves all markup outside
marked supplement blocks. The symbolic checks require SymPy.

## Verification

- All 27 pages match the canonical explanation data; a second build is unchanged.
- Removing the inserted blocks reproduces the prior pages from commit `b533244`
  byte for byte, with one intentional bilingual correction: example 15.1.8 says
  the integrand is **nonnegative**, since it is zero on two boundary edges.
- 42 exact SymPy checks pass for new derivatives, error expansions, extrema
  identities, reordered integrals, cross products, and curl/flux calculations.
  These check selected nontrivial calculations, not every prose statement.
- `verify_structure.py`: index and all 28 section pages pass.
- Existing exercise checks pass: 119 content files, 7,170 exercises, and 122
  exercise-site pages including links, anchors, and SVG XML.
- Chrome rendered all 1,466 added formulas across the 27 pages (19,848 formulas
  including existing material), with zero MathJax error nodes. All 362
  supplement panels were present; no document overflow at a 1,710 px viewport.
- Expanded Korean and English 14.7.3 solutions were visually checked. At a
  390 px viewport, the expanded 14.4.6 solution and the 16.3 page had no document
  overflow. Long new 14.4 and 16.3 calculations use display blocks and aligned
  rows; their updated MathJax checks also passed. Temporary viewport was reset.
