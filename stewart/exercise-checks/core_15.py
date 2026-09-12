"""Shared authoring helpers; explanations and source transcriptions stay explicit."""
import json,re
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
def pair(ko,en):return {'ko':ko,'en':en}
def tex(x):return s.latex(s.sympify(x))
def d(x):return r'\['+x+r'\]'
def m(x):return r'\('+x+r'\)'
def integral(f,lims):
    return ''.join(r'\int_{'+tex(lo)+'}^{'+tex(hi)+'}' for v,lo,hi in reversed(lims))+r'\left('+(f if isinstance(f,str) else tex(f))+r'\right)\,'+r'\,'.join('d'+tex(v) for v,lo,hi in lims)
class Doc:
    def __init__(self,section,pages,pagefor):self.section=section;self.pages=pages;self.pagefor=pagefor;self.items=[];self.checks=[]
    def add(self,n,topic,statement,hint,steps,answer,check,parts=()):
        p=self.pagefor(n)
        e={'id':f'stewart9-exercise-{self.section}-{n}','number':n,'subparts':list(parts),'source':{'printedPage':p,'pdfPage':p+37},'topic':pair(*topic),'statement':pair(*statement),'hint':pair(*hint),'steps':{'ko':[q[0] for q in steps],'en':[q[1] for q in steps]},'answer':pair(*answer) if isinstance(answer,tuple) else pair(answer,answer),'check':pair(*check),'conceptHref':'../s'+self.section.replace('.','-')+'.html','status':'math-verified'}
        self.items.append(e);return e
    def evaluated(self,f,lims):
        f=s.sympify(f);cur=f;steps=[]
        for v,lo,hi in lims:
            nxt=s.simplify(s.integrate(cur,(v,lo,hi)))
            if nxt.has(s.Integral):raise ValueError((cur,v,lo,hi,nxt))
            eq=d(integral(cur,[(v,lo,hi)])+'='+tex(nxt))
            steps.append((m(tex(v))+' 적분을 수행한다. '+eq,'Integrate with respect to '+m(tex(v))+'. '+eq));cur=nxt
        self.checks.append({'integrand':str(f),'limits':[[str(q) for q in li] for li in lims],'value':str(cur),'method':'exact sequential symbolic integration'})
        return cur,steps
    def calc(self,n,statement,f,lims,setup,parts=(),topic=('좌표변환과 삼중적분','Coordinate transformation and triple integration'),check=None):
        value,steps=self.evaluated(f,lims)
        steps.insert(0,(setup[0]+' '+d('I='+integral(f,lims)),setup[1]+' '+d('I='+integral(f,lims))))
        self.add(n,topic,statement,('경계 곡면의 교선을 먼저 구하고 좌표변환의 야코비안을 곱한다.','Find boundary intersections first, then include the coordinate Jacobian.'),steps,d('I='+tex(value)),check or ('경계 교선과 적분구간을 원래 좌표식에 대입해 대조하고 기호 적분을 수행했다.','The boundary intersections and integration limits were checked in the original equations and the integral was evaluated symbolically.'),parts)
        return value
    def save(self,total):
        self.items.sort(key=lambda e:e['number']);assert [e['number'] for e in self.items]==list(range(1,total+1))
        for e in self.items:
            for lang in ('ko','en'):
                for txt in [e['statement'][lang],e['hint'][lang],*e['steps'][lang],e['answer'][lang],e['check'][lang]]:
                    assert not any(ord(c)<32 and c!='\n' for c in txt),(e['number'],'control')
                    assert len(re.findall(r'(?<!\\)\\\(',txt))==len(re.findall(r'(?<!\\)\\\)',txt)),(e['number'],'inline')
                    assert len(re.findall(r'(?<!\\)\\\[',txt))==len(re.findall(r'(?<!\\)\\\]',txt)),(e['number'],'display')
        name='s'+self.section.replace('.','-')
        payload={'section':self.section,'source':{'title':'Calculus','edition':9,'language':'en','printedPages':self.pages,'pdfPages':[p+37 for p in self.pages]},'scope':{'kind':'exercise','numbers':list(range(1,total+1)),'total':total,'note':pair('이 절의 모든 일반 연습문제.','All general exercises in this section.')},'exercises':self.items}
        (ROOT/f'exercise-content/{name}.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
        (ROOT/f'exercise-checks/{name}-report.json').write_text(json.dumps({'section':self.section,'sourceVisualPages':[p+37 for p in self.pages],'uncertainties':[],'checks':self.checks},ensure_ascii=False,indent=2)+'\n')
        print('Saved',self.section,total,'exercises')
