from calc1_helpers import *
import copy
class AltBook(CalcBook):
 def add(self,*args,**kwargs):
  super().add(*args,**kwargs);self.E[args[0]]['id']=self.E[args[0]]['id'].replace('*','-alt')
 def save(self):
  ns=sorted(self.E);d={'section':self.section,'source':{'title':'Calculus','edition':9,'language':'en','printedPages':self.pages,'pdfPages':[p+37 for p in self.pages]},'scope':{'kind':'exercise','numbers':ns,'total':len(ns),'note':pair('대체 전개 절의 원문 대조 문제·해설·검산.','Source-checked exercises and solutions for the alternative development.')},'exercises':[self.E[n]for n in ns]};(ROOT/f's{self.section.replace(".","-").replace("*","-alt")}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
 def reuse(self,n,section,number,page):
  doc=json.loads((ROOT/f's{section.replace(".","-")}.json').read_text());e=copy.deepcopy(next(e for e in doc['exercises']if e['number']==number));e.update(id=f'stewart9-exercise-{self.section.replace("*","-alt")}-{n}',number=n,source={'printedPage':page,'pdfPage':page+37},conceptHref='../../calc1/index.html');self.E[n]=e
  if 'figure'in e:
   old=ROOT/e['figure']['src'].split('../exercise-content/')[1];name=f's{self.section.replace(".","-").replace("*","-alt")}-{n}.svg';new=ROOT/'assets'/name;svg=old.read_text().replace(f'{section}.{number}',f'{self.section}.{n}');new.write_text(svg);e['figure']['src']='../exercise-content/assets/'+name;e['figure']['alt']=pair(f'{self.section}.{n} 자체 그래프',f'Original graph for {self.section}.{n}')
  self.save()
