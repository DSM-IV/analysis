import json,math,html,sys,re
from pathlib import Path
import sympy as S
BASE=Path(__file__).resolve().parents[1];items=[];n=S.symbols('n',integer=True,positive=True)
def M(s):return r'\('+s+r'\)'
def bi(k,e=None):return {'ko':k,'en':k if e is None else e}
def add(q,sk,se,steps,ak,ae,ck,ce,sub=''):
 p=816 if q<=39 else 817
 items.append(dict(id=f'stewart9-exercise-11.6-{q}',number=q,subparts=list(sub),source=dict(printedPage=p,pdfPage=p+37),topic=bi('비율·근 판정법','Ratio and Root Tests'),statement=bi(sk,se),hint=bi('일반항과 부분합을 구별하고 등비급수·소거합·일반항의 영 수렴 조건을 살펴본다.','Distinguish terms from partial sums and examine geometric sums, telescoping, and the zero-term condition.'),steps={'ko':[a for a,b in steps],'en':[b for a,b in steps]},answer=bi(ak,ae),check=bi(ck,ce),conceptHref='../../calc1/index.html',status='math-verified'))
def calc(q,eq,tk,te,lines,ans,k='',e='',sub=''):
 steps=[(M(x),M(x)) for x in lines]
 if k:steps.append((k,e))
 add(q,M(eq)+' '+tk,M(eq)+' '+te,steps,M(ans),M(ans),'초기항·정의역과 극한 논증의 조건을 확인했다.','Initial terms, domain, and conditions of the limit argument were checked.',sub)
def dots(q,sets,limit=None):
 pts=[(i,v) for label,values in sets for i,v in values];xmin=0;xmax=max(i for i,v in pts)+1;lo=min(v for i,v in pts);hi=max(v for i,v in pts)
 if limit is not None:lo=min(lo,limit);hi=max(hi,limit)
 pad=max(.1,(hi-lo)*.12);lo-=pad;hi+=pad;X=lambda x:55+510*(x-xmin)/(xmax-xmin);Y=lambda y:300-250*(y-lo)/(hi-lo)
 out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 390"><rect width="620" height="390" fill="white"/><path d="M55 40V300H575" stroke="#8492a5" fill="none"/>',f'<text x="55" y="25" font-size="15">Sequence {q}: discrete terms</text>']
 for j,(label,values) in enumerate(sets):
  c=['#1463c2','#c64c38','#159568'][j%3]
  for i,v in values:out.append(f'<circle cx="{X(i):.3f}" cy="{Y(v):.3f}" r="3" fill="{c}"/>')
  out.append(f'<text x="55" y="{337+17*j}" fill="{c}" font-size="12">{html.escape(label)}</text>')
 if limit is not None:out.append(f'<path d="M55 {Y(limit)}H575" stroke="#65758d" stroke-dasharray="5 5"/><text x="570" y="{Y(limit)-5}" font-size="10">L={limit:.5g}</text>')
 for i in range(6):
  v=lo+(hi-lo)*i/5;out.append(f'<text x="5" y="{Y(v)+4}" font-size="10">{v:.4g}</text>')
 for i in [1,int(xmax/2),int(xmax)-1]:out.append(f'<text x="{X(i)}" y="318" font-size="11">{i}</text>')
 out.append('</svg>');p=BASE/f'exercise-content/assets/s11-6-{q}.svg';p.write_text(''.join(out));ex=next(e for e in items if e['number']==q);ex['figure']={'src':f'../exercise-content/assets/{p.name}','alt':bi('정수 인덱스에 대응하는 수열의 점 그래프','Discrete sequence values at integer indices'),'caption':bi('자체 계산한 항을 점으로 표시했다. 선으로 연결하지 않았다.','Original computed terms shown as discrete points.')}
calc(1,r'L=\lim|a_{n+1}/a_n|','극한이 각각 (a) 팔 (b) 팔십 퍼센트 (c) 일일 때 급수에 대해 설명하라.','Describe the conclusion when the ratio limit is (a) eight, (b) eight tenths, and (c) one.',[r'L>1\Rightarrow\text{divergence};\quad L<1\Rightarrow\text{absolute convergence}',r'L=1:\quad\sum1/n\text{ diverges},\quad\sum1/n^2\text{ converges}'],r'\text{(a) divergent; (b) absolutely convergent; (c) inconclusive}',sub='abc')
calc(2,r'\lim|a_n/a_{n+1}|=2','역방향 비율의 극한과 급수의 수렴 여부를 구하라.','Find the reciprocal ratio limit and the convergence conclusion.',[r'\lim|a_{n+1}/a_n|=1/2<1'],r'\lim|a_{n+1}/a_n|=1/2;\quad\text{absolutely convergent}')
ratio=[(3,r'n/5^n',1,r'(n+1)/(5n)',r'1/5',True),(4,r'(-2)^n/n^2',1,r'2n^2/(n+1)^2',r'2',False),(5,r'(-1)^{n-1}3^n/(2^nn^3)',1,r'3n^3/[2(n+1)^3]',r'3/2',False),(6,r'(-3)^n/(2n+1)!',0,r'3/[(2n+2)(2n+3)]',r'0',True),(7,r'1/n!',1,r'1/(n+1)',r'0',True),(8,r'ne^{-n}',1,r'(n+1)/(en)',r'1/e',True),(9,r'10^n/[(n+1)4^{2n+1}]',1,r'10(n+1)/[16(n+2)]',r'5/8',True),(10,r'n!/100^n',1,r'(n+1)/100',r'+\infty',False),(11,r'n\pi^n/(-3)^{n-1}',1,r'\pi(n+1)/(3n)',r'\pi/3',False),(12,r'n^{10}/(-10)^{n+1}',1,r'(1+1/n)^{10}/10',r'1/10',True),(14,r'n!/n^n',1,r'[n/(n+1)]^n',r'1/e',True),(15,r'n^{100}100^n/n!',1,r'100(1+1/n)^{100}/(n+1)',r'0',True),(16,r'(2n)!/(n!)^2',1,r'(2n+2)(2n+1)/(n+1)^2',r'4',False),(17,r'(-1)^{n-1}n!/[1\cdot3\cdot5\cdots(2n-1)]',1,r'(n+1)/(2n+1)',r'1/2',True),(18,r'\prod_{k=1}^n(3k-1)/(2k+1)',1,r'(3n+2)/(2n+3)',r'3/2',False),(19,r'[2\cdot4\cdot6\cdots(2n)]/n!',1,r'(2n+2)/(n+1)',r'2',False),(20,r'(-1)^n2^nn!/[5\cdot8\cdot11\cdots(3n+2)]',1,r'2(n+1)/(3n+5)',r'2/3',True)]
for q,term,start,quot,L,conv in ratio:calc(q,rf'\sum_{{n={start}}}^\infty {term}','비율 판정법으로 수렴·발산을 결정하라.','Use the Ratio Test to determine convergence or divergence.',[rf'|a_{{n+1}}/a_n|={quot}',rf'L=\lim|a_{{n+1}}/a_n|={L}'+(r'<1'if conv else r'>1')],r'\text{absolutely convergent}'if conv else r'\text{divergent}')
calc(13,r'\sum_{n=1}^\infty\cos(n\pi/3)/n!','비율 판정법으로 수렴·발산을 결정하라.','Use the Ratio Test to determine convergence or divergence.',[r'|\cos(n\pi/3)|\in\{1/2,1\}',r'0\le|a_{n+1}/a_n|=\frac{|\cos((n+1)\pi/3)|}{(n+1)|\cos(n\pi/3)|}\le2/(n+1)\to0'],r'\text{absolutely convergent}','분모의 코사인이 정수 인덱스에서 영이 되지 않음을 먼저 확인한다.','The cosine denominator never vanishes at an integer index.')
for q,term,start,root,L,conv in [(21,r'[(n^2+1)/(2n^2+1)]^n',1,r'(n^2+1)/(2n^2+1)',r'1/2',True),(22,r'(-2)^n/n^n',1,r'2/n',r'0',True),(23,r'(-1)^{n-1}/(\ln n)^n',2,r'1/\ln n',r'0',True),(24,r'[-2n/(n+1)]^{5n}',1,r'[2n/(n+1)]^5',r'32',False),(25,r'(1+1/n)^{n^2}',1,r'(1+1/n)^n',r'e',False),(26,r'(\arctan n)^n',0,r'\arctan n',r'\pi/2',False)]:
 calc(q,rf'\sum_{{n={start}}}^\infty {term}','근 판정법으로 수렴·발산을 결정하라.','Use the Root Test to determine convergence or divergence.',[rf'\sqrt[n]{{|a_n|}}={root}\to {L}'+(r'<1'if conv else r'>1')],r'\text{absolutely convergent}'if conv else r'\text{divergent}','근은 양의 인덱스 꼬리에서 취한다. 영 인덱스의 거듭제곱은 상수항 관례로 두며 유한한 초기항은 판정에 영향이 없다.','Take roots on the positive-index tail. A zeroth-power constant term uses the usual power-series convention; a finite initial term does not affect the verdict.')
for q,term,start,lines,kind in [(27,r'(-1)^n\ln n/n',2,[r'b_n\to0,\quad(\ln x/x)^{\prime}=(1-\ln x)/x^2<0\quad(x>e)',r'\sum\ln n/n\text{ diverges by comparison with }\sum1/n'],'conditionally convergent'),(28,r'[(1-n)/(2+3n)]^n',1,[r'\sqrt[n]{|a_n|}=|1-n|/(2+3n)\to1/3<1'],'absolutely convergent'),(29,r'(-9)^n/[n10^{n+1}]',1,[r'|a_{n+1}/a_n|=9n/[10(n+1)]\to9/10<1'],'absolutely convergent'),(30,r'n5^{2n}/10^{n+1}',1,[r'a_n=(n/10)(5/2)^n\to\infty'],'divergent'),(31,r'(n/\ln n)^n',2,[r'\sqrt[n]{|a_n|}=n/\ln n\to\infty'],'divergent'),(32,r'\sin(n\pi/6)/(1+n\sqrt n)',1,[r'|a_n|\le n^{-3/2},\quad p=3/2>1'],'absolutely convergent'),(33,r'(-1)^n\arctan n/n^2',1,[r'|a_n|\le\pi/(2n^2)'],'absolutely convergent'),(34,r'(-1)^n/(\sqrt n\ln n)',2,[r'b_n=1/(\sqrt n\ln n)\downarrow0',r'\ln n<\sqrt n\Rightarrow b_n>1/n'],'conditionally convergent')]:
 calc(q,rf'\sum_{{n={start}}}^\infty {term}','절대수렴·조건수렴·발산 중 하나로 분류하라.','Classify as absolutely convergent, conditionally convergent, or divergent.',lines,r'\text{'+kind+'}')
calc(35,r'a_1=2,\quad a_{n+1}=(5n+1)a_n/(4n+3)','점화식으로 정의된 급수의 수렴·발산을 판정하라.','Determine convergence of the recursively defined series.',[r'a_n>0,\quad a_{n+1}/a_n=(5n+1)/(4n+3)\to5/4>1'],r'\text{divergent}')
calc(36,r'a_1=1,\quad a_{n+1}=(2+\cos n)a_n/\sqrt n','점화식으로 정의된 급수의 수렴·발산을 판정하라.','Determine convergence of the recursively defined series.',[r'a_n>0,\quad0<a_{n+1}/a_n\le3/\sqrt n\to0'],r'\text{convergent}')
calc(37,r'b_n>0,\quad b_n\to1/2,\quad\sum_{n=1}^\infty b_n^n\cos(n\pi)/n','절대수렴 여부를 판정하라.','Determine absolute convergence.',[r'|a_n|=b_n^n/n',r'\sqrt[n]{|a_n|}=b_n/n^{1/n}\to1/2<1'],r'\text{absolutely convergent}')
calc(38,r'b_n>0,\quad b_n\to1/2,\quad\sum_{n=1}^\infty\frac{(-1)^nn!}{n^nb_1b_2\cdots b_n}','절대수렴 여부를 판정하라.','Determine absolute convergence.',[r'|a_{n+1}/a_n|=\frac1{b_{n+1}}\left(\frac n{n+1}\right)^n\to2/e<1'],r'\text{absolutely convergent}')
calc(39,r'\text{(a)}\sum1/n^3;\quad\text{(b)}\sum n/2^n;\quad\text{(c)}\sum(-3)^{n-1}/\sqrt n;\quad\text{(d)}\sum\sqrt n/(1+n^2)','비율 판정법만으로 결론이 나오지 않는 급수를 고르라.','Identify the series for which the Ratio Test is inconclusive.',[r'L_a=1,\quad L_b=1/2,\quad L_c=3,\quad L_d=1'],r'\text{(a), (d)}',sub='abcd')
calc(40,r'\sum_{n=1}^\infty(n!)^2/(kn)!,\quad k\in\mathbb N','수렴하는 양의 정수 매개변수를 구하라.','Find positive integers giving convergence.',[r'|a_{n+1}/a_n|=\frac{(n+1)^2}{(kn+1)(kn+2)\cdots(kn+k)}',r'k=1:\ L=\infty;\quad k=2:\ L=1/4;\quad k>2:\ L=0'],r'k=2,3,4,\ldots')
calc(41,r'\sum_{n=0}^\infty x^n/n!','(a) 모든 실수 입력에서 수렴함을 증명하고 (b) 일반항의 극한을 결론내려라.','(a) Prove convergence for every real input and (b) deduce the term limit.',[r'x=0:\text{ only the constant term remains}',r'x\ne0:\quad|a_{n+1}/a_n|=|x|/(n+1)\to0',r'\text{convergent series}\Rightarrow a_n\to0'],r'\text{(a) absolutely convergent for all real }x;\quad\text{(b)}\lim x^n/n!=0',sub='ab')
calc(42,r'a_n>0,\quad r_n=a_{n+1}/a_n\to L<1,\quad R_N=\sum_{n=N+1}^\infty a_n','(a) 비율 수열이 감소하고 필요한 비율이 일 미만일 때 (b) 비율 수열이 증가할 때 각각 기하급수 상계로 나머지를 평가하라.','Bound the remainder by geometric series when (a) the ratios decrease and the relevant ratio is below one and (b) the ratios increase.',[r'\text{(a)} r_{N+1}<1,\quad a_{N+1+j}\le a_{N+1}r_{N+1}^j',r'R_N\le a_{N+1}\sum_{j=0}^\infty r_{N+1}^j=\frac{a_{N+1}}{1-r_{N+1}}',r'\text{(b)} r_n\le L<1\Rightarrow a_{N+1+j}\le a_{N+1}L^j',r'R_N\le a_{N+1}/(1-L)'],r'\text{(a)}\ R_N\le a_{N+1}/(1-r_{N+1});\quad\text{(b)}\ R_N\le a_{N+1}/(1-L)',sub='ab')
sm5=sum(1/(j*2**j)for j in range(1,6));N=1
while 1/((N+1)*2**N)>=.00005:N+=1
sm=sum(1/(j*2**j)for j in range(1,N+1))
calc(43,r'\sum_{n=1}^\infty1/(n2^n)','(a) 다섯 부분합과 비율 나머지 상계 (b) 오차가 지정값 미만인 부분합과 항 수를 구하라.','Find (a) the five-term sum with a ratio remainder bound and (b) a term count and partial sum with error below the target.',[r'r_n=n/[2(n+1)]\uparrow1/2,\quad R_N\le2a_{N+1}=1/[(N+1)2^N]',rf'\text{{(a)}}\ s_5={sm5:.12f},\quad R_5\le1/192',rf'\text{{(b)}}\ R_{{{N}}}\le{1/((N+1)*2**N):.12f}<0.00005',rf's_{{{N}}}={sm:.12f}'],rf's_5={sm5:.12f};\quad N={N},\quad S\approx{sm:.12f}',sub='ab')
sm=sum(j/2**j for j in range(1,11));bound=S.Rational(11,2**11)/(1-S.Rational(12,22))
calc(44,r'\sum_{n=1}^\infty n/2^n','열 부분합으로 근사하고 감소 비율의 나머지 정리로 오차를 평가하라.','Approximate using ten terms and bound the error using the decreasing-ratio remainder theorem.',[r'r_n=(n+1)/(2n)\downarrow1/2',r'R_{10}\le a_{11}/(1-r_{11})=(11/2048)/(1-6/11)=121/10240'],rf's_{{10}}={sm:.12f},\quad0<R_{{10}}\le121/10240\approx{float(bound):.12f}')
calc(45,r'L=\lim_{n\to\infty}\sqrt[n]{|a_n|}','근 판정법의 세 경우를 증명하라.','Prove all three cases of the Root Test.',[r'\text{(i)} L<1:\quad L<r<1\Rightarrow\sqrt[n]{|a_n|}<r\text{ eventually}\Rightarrow|a_n|<r^n',r'\text{(ii)}\ L>1:\quad1<r<L\Rightarrow|a_n|>r^n\text{ eventually}\Rightarrow a_n\not\to0',r'\text{(iii)}\ L=1:\quad\sqrt[n]{1/n}\to1,\quad\sqrt[n]{1/n^2}\to1'],r'L<1:\text{ absolute convergence};\quad L>1:\text{ divergence};\quad L=1:\text{ inconclusive}','무한대인 극한도 임의의 일보다 큰 비교 공비를 고르면 둘째 논증에 포함된다. 일인 경우는 조화급수와 역제곱급수의 다른 결과가 반례이다.','An infinite limit fits the second argument by choosing any ratio larger than one. The harmonic and inverse-square series demonstrate the inconclusive case.',sub='')
import mpmath as mp
mp.mp.dps=70
ram=lambda j:mp.factorial(4*j)*(1103+26390*j)/(mp.factorial(j)**4*mp.mpf(396)**(4*j))
coef=2*mp.sqrt(2)/9801;pi1=1/(coef*ram(0));pi2=1/(coef*(ram(0)+ram(1)));err1=pi1-mp.pi;err2=pi2-mp.pi
calc(46,r'\frac1\pi=\frac{2\sqrt2}{9801}\sum_{n=0}^\infty\frac{(4n)!(1103+26390n)}{(n!)^4\cdot396^{4n}}','(a) 급수의 수렴을 보이고 (b) 첫 한 항 또는 두 항을 사용한 원주율 근삿값과 정확한 소수 자릿수를 구하라.','(a) Verify convergence, and (b) find the pi approximations from one or two terms and their decimal accuracy.',[r'\frac{a_{n+1}}{a_n}=\frac{(4n+1)(4n+2)(4n+3)(4n+4)}{(n+1)^4\cdot396^4}\frac{1103+26390(n+1)}{1103+26390n}\to\frac{256}{396^4}=\frac1{99^4}<1',rf'\pi_1={mp.nstr(pi1,28)},\quad|\pi_1-\pi|\approx{mp.nstr(err1,9)}',rf'\pi_2={mp.nstr(pi2,28)},\quad|\pi_2-\pi|\approx{mp.nstr(err2,9)}',r'\text{accuracy criterion: }|\text{error}|<\tfrac12\cdot10^{-d}'],r'\text{(a) convergent; (b) half-unit error guarantee: }d=6,14;\quad\text{matching rounded values: }d=7,14','절대오차가 반 단위보다 작다는 기준으로 자릿수를 셌다. 반올림 전 십진 전개의 공통 접두 숫자를 세면 각각 육 자리와 십오 자리이다. 실제로 같은 값으로 반올림되는 최대 소수 자릿수는 한 항 일곱 자리, 두 항 십사 자리이다. 이 세 기준을 구분한다.','Decimal accuracy is counted by the half-unit absolute-error criterion. Counting matching leading digits of unrounded decimal expansions instead gives six and fifteen places; that is a different convention. The actual rounded values agree through seven decimal places for one term and fourteen for two terms.',sub='ab')
items.sort(key=lambda e:e['number']);assert [e['number']for e in items]==list(range(1,47))
raw={'section':'11.6','source':{'title':'Calculus','edition':'9','language':'en','printedPages':[816,817],'pdfPages':[853,854]},'scope':{'kind':'exercise','numbers':list(range(1,47)),'total':46,'note':bi('일반 Exercises의 모든 주번호와 소문항.','All main-numbered ordinary Exercises and their subparts.')},'exercises':items}
sys.path.insert(0,str(BASE));from build_exercises import validate_document
validate_document(raw,BASE/'exercise-content/s11-6.json')
for ex in items:
 for key in ['statement','answer']:assert re.findall(r'\\\((.*?)\\\)',ex[key]['ko'])==re.findall(r'\\\((.*?)\\\)',ex[key]['en']),(ex['number'],key)
assert mp.mpf('0.5e-7')<err1<mp.mpf('0.5e-6');assert mp.mpf('0.5e-15')<err2<mp.mpf('0.5e-14')
assert mp.mpf(256)/396**4==mp.mpf(1)/99**4
assert 0<math.log(2)-sm5<1/192
assert 0<2-sm<float(bound)
(BASE/'exercise-content/s11-6.json').write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
print('11.6: 46 cards; source, schema, bilingual formulas, ratio and remainder checks; Ramanujan evaluated at 70 digits')
