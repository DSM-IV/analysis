#!/usr/bin/env python3
"""Regenerate the original SVG graphs for §§16.6–16.7 in their final form."""
import runpy
from pathlib import Path
for filename in ('s16-6-graphs.py','s16-6-tangent-graphs.py','s16-7-graphs.py'):
    runpy.run_path(str(Path(__file__).with_name(filename)),run_name='__main__')
