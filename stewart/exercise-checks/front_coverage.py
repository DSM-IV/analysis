"""Report the full source inventory separately from the publishing ledger."""
from pathlib import Path
import json,argparse
R=Path(__file__).resolve().parents[1];parser=argparse.ArgumentParser();parser.add_argument('--require-complete',action='store_true');args=parser.parse_args();rows={}
for p in sorted((R/'exercise-checks').glob('calc1-ch*-inventory.json')):
 for row in json.loads(p.read_text())['sections']:
  n=row.get('total',row.get('exerciseCount'));rows[row['section']]={'section':row['section'],'total':n,'title':row['title'],'pdfPages':row['pdfPages']}
ledger=json.loads((R/'exercise-content/manifest.json').read_text())['sections']
for row in ledger:
 if row.get('kind','exercise')!='exercise':continue
 if row['section'] not in rows:rows[row['section']]={'section':row['section'],'total':row['total'],'title':row['title']}
 for_expected=rows[row['section']]['total'];assert for_expected==row['total'],row
 rows[row['section']]['approved']=len(row['completedNumbers'])
for row in rows.values():row.setdefault('approved',0)
sort=lambda r:tuple(int(x.rstrip('*'))for x in r['section'].split('.'))+('*'in r['section'],)
rows=sorted(rows.values(),key=sort);total=sum(r['total']for r in rows);published=sum(r['approved']for r in rows)
assert len(rows)==119 and total==7170,(len(rows),total)
report={'targetSections':len(rows),'targetExercises':total,'approvedExercises':published,'remainingExercises':total-published,'scope':'General Exercises1–16, including6.2*–6.4* alternative sections; excludes Review,Problems Plus,projects.','sections':rows}
(R/'exercise-checks/full-exercise-coverage.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(f'Full source scope: {published}/{total} approved for publication; {total-published} remain in {len(rows)} total sections')
if args.require_complete:assert all(r['approved']==r['total']for r in rows),'The full requested exercise inventory is not complete.'
