"""Check last and following source pages for a continuation beyond each inventory.
Requires a user-supplied pdftotext -layout extraction; source text is never saved here.
This is a numbering tripwire, not a replacement for visual source review.
"""
from pathlib import Path
import json,re,argparse
p=argparse.ArgumentParser();p.add_argument('--text',required=True);args=p.parse_args();pages=Path(args.text).read_text().split('\f');R=Path(__file__).resolve().parents[1];rows={}
for f in (R/'exercise-checks').glob('calc1-ch*-inventory.json'):
 for row in json.loads(f.read_text())['sections']:rows[row['section']]={'section':row['section'],'count':row.get('total',row.get('exerciseCount')),'lastPdfPage':max(row['pdfPages'])}
for row in json.loads((R/'exercise-content/manifest.json').read_text())['sections']:
 if row['section']not in rows:
  doc=json.loads((R/'exercise-content'/('s'+row['section'].replace('.','-').replace('*','-alt')+'.json')).read_text());rows[row['section']]={'section':row['section'],'count':row['total'],'lastPdfPage':max(doc['source']['pdfPages'])}
hits=[]
for row in rows.values():
 for pg in[row['lastPdfPage'],row['lastPdfPage']+1]:
  if re.search(r'(?<!\d)'+str(row['count']+1)+r'\.\s',pages[pg-1]):hits.append({'section':row['section'],'candidateNextNumber':row['count']+1,'pdfPage':pg})
report={'sectionsChecked':len(rows),'method':'Search last and following PDF page for the next main exercise number; visually review all hits.','correctedBoundaries':{'10.2':85,'12.2':52,'13.1':62,'13.3':78,'15.6':59,'16.5':41},'unresolvedCandidates':hits};(R/'exercise-checks/boundary-inventory-audit.json').write_text(json.dumps(report,indent=2)+'\n');print(report);assert not hits,'Review continuation candidates before claiming full scope.'
