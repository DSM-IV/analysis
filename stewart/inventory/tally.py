#!/usr/bin/env python3
"""Tally cards/examples per section from inventory/inv-*.md. Prints a table; --apply updates build_index.py SECTIONS + SOURCE-MAP.md."""
import re, glob, os, sys
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
rows={}
for f in sorted(glob.glob(os.path.join(HERE,'inv-*.md'))):
    sec=os.path.basename(f)[4:-3]
    s=open(f,encoding='utf-8').read()
    a=s.split('## A.')[1].split('## B.')[0] if '## A.' in s else ''
    b=s.split('## B.')[1].split('## C.')[0] if '## B.' in s else ''
    kinds={k:0 for k in ['note','def','thm','rem','fig']}
    for line in a.splitlines():
        m=re.match(r'\|\s*\d+\s*\|\s*(note|def|thm|rem|fig)\s*\|',line)
        if m: kinds[m.group(1)]+=1
    ex=len([l for l in b.splitlines() if re.match(r'\|\s*\d+[a-z]?\s*\|',l)])
    concept=sum(v for k,v in kinds.items() if k!='fig')
    rows[sec]=(kinds,concept,ex)
def key(x):
    a,b=x.split('.'); return (int(a),int(b))
print(f"{'sec':<7}{'note':>5}{'def':>5}{'thm':>5}{'rem':>5}{'fig':>5}{'concept':>9}{'ex':>5}")
tc=te=0
for sec in sorted(rows,key=key):
    k,c,e=rows[sec]; tc+=c; te+=e
    print(f"{sec:<7}{k['note']:>5}{k['def']:>5}{k['thm']:>5}{k['rem']:>5}{k['fig']:>5}{c:>9}{e:>5}")
print(f"{'TOTAL':<7}{'':>25}{tc:>9}{te:>5}  ({len(rows)} sections)")
if '--apply' in sys.argv:
    p=os.path.join(ROOT,'build_index.py'); s=open(p,encoding='utf-8').read()
    for sec,(k,c,e) in rows.items():
        f='s'+sec.replace('.','-')
        s=re.sub(r'\("%s","%s",("[^"]*"),("[^"]*"),(\d+),\d+,("[^"]*"),(None|\d+)\)'%(re.escape(f),re.escape(sec)),
                 lambda m: f'("{f}","{sec}",{m.group(1)},{m.group(2)},{m.group(3)},{e},{m.group(4)},{c})', s)
    open(p,'w',encoding='utf-8').write(s)
    p2=os.path.join(ROOT,'SOURCE-MAP.md'); t=open(p2,encoding='utf-8').read()
    for sec,(k,c,e) in rows.items():
        f='s'+sec.replace('.','-')+'.html'
        t=re.sub(r'\| %s \| %s \| ([^|]*)\| ([^|]*)\| \d+ \| [^|]*\| ([^|]*)\|'%(re.escape(sec),re.escape(f)),
                 lambda m: f"| {sec} | {f} | {m.group(1)}| {m.group(2)}| {e} | {c} (+fig {k['fig']}) | {m.group(3)}|", t)
    open(p2,'w',encoding='utf-8').write(t)
    print("applied to build_index.py and SOURCE-MAP.md")
