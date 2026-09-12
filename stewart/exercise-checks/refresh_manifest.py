"""Refresh ordinary-Exercise coverage from reviewed counts and saved content."""
from pathlib import Path
import ast,json
R=Path(__file__).resolve().parents[1];C=R/'exercise-content'
counts={'12.6':55,'14.1':81,'14.2':59,'14.3':101,'14.4':54,'14.5':60,'14.6':77,'14.7':62,'14.8':63,'15.1':58,'15.2':82,'15.3':51,'15.4':35,'15.5':26,'15.6':59,'15.7':33,'15.8':51,'15.9':31,'16.1':40,'16.2':54,'16.3':42,'16.4':35,'16.5':41,'16.6':64,'16.7':49,'16.8':24,'16.9':34}
assert len(counts)==27 and sum(counts.values())==1421
# Newly authored raw files are not approval. Preserve only additional ordinary
# sections explicitly approved in the existing manifest by the coordinator.
manifest_path=C/'manifest.json'
if manifest_path.exists():
 for row in json.loads(manifest_path.read_text())['sections']:
  if row.get('kind','exercise')=='exercise' and row['section'] not in counts:
   assert isinstance(row.get('total'),int) and row['total']>0,row
   counts[row['section']]=row['total']
titles={row["section"]:row["title"] for row in json.loads(manifest_path.read_text())["sections"] if "title" in row} if manifest_path.exists() else {}
for node in ast.parse((R/'build_index.py').read_text()).body:
 if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='SECTIONS'for t in node.targets):
  for row in ast.literal_eval(node.value):titles[row[1]]={'ko':row[2],'en':row[3]}
rows=[]
for sec,total in sorted(counts.items(),key=lambda v:tuple(int(x.rstrip('*')) for x in v[0].split('.'))+('*' in v[0],)):
 p=C/f's{sec.replace(".","-").replace("*", "-alt")}.json';doc=json.loads(p.read_text())if p.exists()else{};nums=[e['number']for e in doc.get('exercises',[])]
 kind='exercise'
 if doc and doc.get('kind',doc.get('scope',{}).get('kind','exercise'))!='exercise':
  raise ValueError(f'{sec}: expected ordinary exercise content')
 title=titles.get(sec,{'ko':sec.split('.')[0]+'장','en':'Chapter '+sec.split('.')[0]})
 rows.append({'section':sec,'kind':kind,'title':title,'total':total,'expectedNumbers':list(range(1,total+1)),'completedNumbers':nums})
(C/'manifest.json').write_text(json.dumps({'sections':rows},ensure_ascii=False,indent=2)+'\n')
print('Saved:',sum(len(r['completedNumbers'])for r in rows),'/',sum(counts.values()),'currently inventoried exercises')
