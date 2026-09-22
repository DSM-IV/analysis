"""Economic and biological integral models, with unit conversions."""
from early_helpers import Book
from pathlib import Path
import sympy as s,mpmath as mp,json,re
mp.mp.dps=45;x=s.symbols('x',positive=True);R=s.Rational;b=Book('8.4',[628,629,630]);records=[]
def m(v):return r'\('+v+r'\)'
def F(v):return(m(v),m(v))
def tx(v):return s.latex(s.simplify(v))
def add(n,k,e,steps,ans,parts=''):
 b.add(n,628 if n<=3 else 629 if n<=18 else 630,('경제학과 생물학에의 응용','Applications to Economics and Biology'),(k,e),steps,(ans,ans),list(parts),check=('적분 구간과 단위를 확인한다. 수량이 천 단위이면 달러 환산에1000을 곱하고,초당 유량은60을 곱해 분당 유량으로 바꾼다.','Check bounds and units.Multiply thousand-unit quantities by1000 for dollars; multiply flow per second by60 for flow per minute.'));b.E[n]['conceptHref']='../../calc1/index.html'
def integ(f,a,c):
 v=s.integrate(f,(x,a,c));records.append({'integrand':str(f),'bounds':[str(a),str(c)],'value':str(v)});return v
f=R('.82')-R('.00003')*x+R('.000000003')*x*x;v=18000+integ(f,0,4000)
add(1,'C′(x)=.82−.00003x+.000000003x² 달러/갤런,C(0)=$18000이다. 첫4000갤런 생산비를 구하라.','Given C′(x)=.82−.00003x+.000000003x² dollars/gallon and C(0)=$18000,find the cost of the first4000gallons.',[F(r'C(4000)=18000+\int_0^{4000}(.82-.00003x+.000000003x^2)dx'),F(r'C(4000)=18000+3280-240+64=21104')],m(r'\$21104'))
v=integ(48-R('.0012')*x,5000,10000)
add(2,'한계수익48−.0012x 달러/단위에서 판매량5000→10000의 수익 증가를 구하라.','With marginal revenue48−.0012x dollars/unit,find the revenue increase from5000to10000units.',[F(r'\Delta R=\int_{5000}^{10000}(48-.0012x)dx=[48x-.0006x^2]_{5000}^{10000}')],m(r'\$'+tx(v)))
v1=100+integ(R('.6')+R('.008')*x,0,50);v2=integ(R('.6')+R('.008')*x,50,100)
add(3,'구리 한계추출비 .6+.008x는 천달러/톤이며 초기비용$100000이다. 첫50톤과 다음50톤의 비용을 구하라.','Copper marginal extraction cost .6+.008x is in thousands of dollars/ton, with startup$100000.Find costs for the first50tons and next50tons.',[F(r'C(50)=100+\int_0^{50}(.6+.008x)dx=140\quad\text{thousand dollars}'),F(r'C(100)-C(50)=\int_{50}^{100}(.6+.008x)dx=60\quad\text{thousand dollars}')],m(r'\$140000;\quad\$60000'))
surplus={4:(2000-46*s.sqrt(x),400,1,'소비자','consumer'),5:(870*s.exp(-R('.03')*x),45,1000,'소비자','consumer'),6:(6-x/3500,11200,1,'소비자','consumer'),7:(25-x/30,300,1,'소비자','consumer'),9:(3+R('.01')*x*x,10,1,'생산자','producer'),10:(125+R('.002')*x*x,500,1,'생산자','producer')}
for n,(f,q,scale,k,e)in surplus.items():
 price=f.subs(x,q);cs=n<=7;v=scale*integ(f-price if cs else price-f,0,q)
 desc={4:('수요p=2000−46√x,판매량400','Demand p=2000−46√x,sales400'),5:('수요p=870e^(−.03x),x는천개,판매45000개','Demand p=870e^(−.03x),x in thousands,sales45000'),6:('수요p=6−x/3500,가격$2.80','Demand p=6−x/3500,price$2.80'),7:('가격$18에210개 판매하고 $1 인하마다30개 증가하는 선형수요에서 가격$15','Linear demand sells210 at$18 and30more per$1 decrease; price$15'),9:('공급p=3+.01x²,판매량10','Supply p=3+.01x²,sales10'),10:('공급p=125+.002x²,가격$625','Supply p=125+.002x²,price$625')}[n]
 steps=[F('p(x)='+tx(f)+r',\quad X='+str(q)+r',\quad P='+tx(price))]
 if n==7:steps.insert(0,F(r'x=210+30(18-p)\Longrightarrow p=25-x/30'))
 steps +=[F(('CS'if cs else'PS')+'='+str(scale)+r'\int_0^{'+str(q)+r'}\left('+tx(f-price if cs else price-f)+r'\right)dx='+tx(v)),('곡선과 수평 가격선 사이의 넓이를0부터 판매량까지 취한다.','Take the area between the curve and horizontal price line from0to the sales quantity.')]
 add(n,desc[0]+'에서 '+k+'잉여를 구하라.','Find '+e+' surplus for '+desc[1]+'.',steps,m(r'\$'+f'{float(v):.2f}'))
demand=lambda z:800000*mp.exp(-z/5000)/(z+20000);q8=mp.findroot(lambda z:demand(z)-16,3500);cs8=mp.quad(lambda z:demand(z)-16,[0,q8])
add(8,'수요p=800000e^(−x/5000)/(x+20000),가격$16에서 판매량과 소비자잉여를 근사하라.','For demand p=800000e^(−x/5000)/(x+20000) and price$16,estimate sales and consumer surplus.',[F(r'p(X)=16\Longrightarrow X\approx'+f'{float(q8):.6f}'),('수요는 x≥0에서 엄격히 감소하므로 교점이 유일하다.','Demand decreases strictly on x≥0, so the crossing is unique.'),F(r'CS=\int_0^X\left({800000e^{-x/5000}\over x+20000}-16\right)dx\approx'+f'{float(cs8):.6f}')],m(r'X\approx'+f'{float(q8):.2f}'+r',\quad CS\approx\$'+f'{float(cs8):.2f}'))
supply=lambda z:mp.sqrt(30+mp.mpf('.01')*z*mp.exp(mp.mpf('.001')*z));q11=mp.findroot(lambda z:supply(z)-30,3300);ps11=mp.quad(lambda z:30-supply(z),[0,q11])
add(11,'공급p=√(30+.01xe^(.001x)),가격$30에서 생산자잉여를 근사하라.','For supply p=√(30+.01xe^(.001x)) and price$30,estimate producer surplus.',[F(r'30+.01Xe^{.001X}=900\Longrightarrow X\approx'+f'{float(q11):.6f}'),('공급함수는 x≥0에서 증가하므로 이 교점이 유일하다.','Supply increases on x≥0, giving a unique crossing.'),F(r'PS=\int_0^X[30-\sqrt{30+.01xe^{.001x}}]dx\approx'+f'{float(ps11):.6f}')],m(r'PS\approx\$'+f'{float(ps11):.2f}'))
add(12,'수요p=50−x/20,공급p=20+x/10에서 (a)균형 수량·가격,(b)소비자·생산자 잉여를 구하고 그림으로 설명하라.','For demand p=50−x/20 and supply p=20+x/10,find(a)equilibrium quantity/price and(b)consumer/producer surplus; illustrate.',[F(r'50-X/20=20+X/10\Longrightarrow X=200,P=40'),F(r'CS=\int_0^{200}(50-x/20-40)dx=1000'),F(r'PS=\int_0^{200}(40-20-x/10)dx=2000')],m(r'(a)\ X=200,P=40;\quad(b)\ CS=1000,PS=2000\text{ dollars}'),'ab')
add(13,'x가 천 단위이고 수요228.4−18x,공급27x+57.4이다. (a)균형 수량,(b)최대 총잉여를 구하라.','With x in thousands,demand228.4−18x and supply27x+57.4,find(a)equilibrium quantity and(b)maximum total surplus.',[F(r'171=45X\Longrightarrow X=3.8\quad\text{thousand}'),F(r'TS=1000\int_0^{3.8}(171-45x)dx=324900'),('총잉여의 도함수는 수요−공급이며 균형점에서 양→음으로 바뀐다.','The total-surplus derivative is demand minus supply, changing positive-to-negative at equilibrium.')],m(r'(a)\ 3800\text{ units};\quad(b)\$324900'),'ab')
q14=s.log(12)/R('.34');v14=1000*integ(312*s.exp(-R('.14')*x)-26*s.exp(R('.2')*x),0,q14)
add(14,'x가 천 단위이고 수요312e^(−.14x),공급26e^(.2x)이다. 최대 총잉여를 구하라.','With x in thousands,demand312e^(−.14x) and supply26e^(.2x),find maximum total surplus.',[F(r'312e^{-.14X}=26e^{.2X}\Longrightarrow X=\ln12/.34'),F(r'TS=1000\int_0^X(312e^{-.14x}-26e^{.2x})dx'),F(r'TS\approx'+f'{float(v14):.2f}')],m(r'\$'+f'{float(v14):.2f}'))
v=integ(s.sqrt(x),4,8)
add(15,'순투자흐름√t 백만달러/년일 때4년부터8년까지 자본 증가를 구하라.','Net investment flow is√t million dollars/year.Find capital formation from year4to8.',[F(r'\Delta K=\int_4^8\sqrt t\,dt=\tfrac23(8^{3/2}-4^{3/2})')],m(tx(v)+r'\text{ million dollars}'))
v=integ(9000*s.sqrt(1+2*x),0,4)
add(16,'수익흐름9000√(1+2t) 달러/년의 첫4년 총수익을 구하라.','Find total revenue over the first4years for flow9000√(1+2t) dollars/year.',[F(r'R=\int_0^49000\sqrt{1+2t}\,dt=[3000(1+2t)^{3/2}]_0^4')],m(r'\$'+tx(v)))
pv=integ(8000*s.exp(-R('.022')*x),0,6);fv=s.exp(R('.372'))*pv
add(17,'수입흐름8000e^(.04t) 달러/년을 연6.2% 연속복리로 투자한다.6년 후 미래가치를 구하라.','Invest income flow8000e^(.04t) dollars/year at6.2% continuous interest.Find its future value after6years.',[F(r'FV=\int_0^68000e^{.04t}e^{.062(6-t)}dt'),F(r'FV={8000\over.022}e^{.372}(1-e^{-.132})')],m(r'FV\approx\$'+f'{float(fv):.2f}'))
add(18,'17번 수입흐름의 현재가치를 구하라.','Find the present value of the income stream in17.',[F(r'PV=\int_0^68000e^{.04t}e^{-.062t}dt={8000\over.022}(1-e^{-.132})'),F(r'FV=e^{.062(6)}PV')],m(r'PV\approx\$'+f'{float(pv):.2f}'))
add(19,'소득 a≤x≤b에서 인구밀도가Ax^(−k),A>0,k>1이다. 평균소득을 구하라.','On income interval a≤x≤b, population density is Ax^(−k),A>0,k>1.Find mean income.',[F(r'N={A\over1-k}(b^{1-k}-a^{1-k}),\quad0<a<b'),F(r'k\ne2:\quad\bar x={1-k\over2-k}{b^{2-k}-a^{2-k}\over b^{1-k}-a^{1-k}}'),F(r'k=2:\quad\bar x={\ln(b/a)\over1/a-1/b}={ab\ln(b/a)\over b-a}')],m(r'\bar x=\frac{1-k}{2-k}\frac{b^{2-k}-a^{2-k}}{b^{1-k}-a^{1-k}}\ (k\ne2);\quad\frac{ab\ln(b/a)}{b-a}\ (k=2)'))
v=integ(2200+10*s.exp(R('.8')*x),5,9)
add(20,'모기 개체 증가율2200+10e^(.8t) 마리/주에서5주부터9주까지 증가량을 구하라.','Find population increase from week5to9 for growth rate2200+10e^(.8t) mosquitoes/week.',[F(r'\Delta N=\int_5^9(2200+10e^{.8t})dt=8800+12.5(e^{7.2}-e^4)')],m(r'\Delta N\approx'+str(round(float(v)))))
flow=s.pi*4000*R('.008')**4/(8*R('.027')*2)
add(21,'Poiseuille 법칙에서 η=.027,R=.008cm,l=2cm,P=4000dyn/cm²일 때 유량을 구하라.','Use Poiseuille’s law with η=.027,R=.008cm,l=2cm,P=4000dyn/cm² to find flow.',[F(r'Q={\pi PR^4\over8\eta l}={\pi(4000)(.008)^4\over8(.027)(2)}')],m(r'Q\approx'+f'{float(flow):.9f}'+r'\mathrm{cm^3/s}'))
add(22,'같은 유량에서 동맥 반지름과 압력의 비 P/P₀=(R₀/R)⁴을 보이고 반지름이3/4로 줄면 압력이3배보다 커짐을 보이라.','At fixed flow,show P/P₀=(R₀/R)⁴ and that reducing radius to3/4 increases pressure more than threefold.',[F(r'{\pi PR^4\over8\eta l}={\pi P_0R_0^4\over8\eta l}\Longrightarrow P/P_0=(R_0/R)^4'),F(r'R=3R_0/4\Longrightarrow P/P_0=(4/3)^4=256/81>3')],m(r'P/P_0=(R_0/R)^4;\quad256/81\approx3.1605'))
area23=integ(20*x*s.exp(-R('.6')*x),0,10);q23=6/area23
add(23,'염료6mg 주입 후 c(t)=20te^(−.6t)mg/L,0≤t≤10초이다. 심박출량을 계산하라.','After6mg dye,c(t)=20te^(−.6t)mg/L on0≤t≤10seconds.Find cardiac output.',[F(r'Q={6\over\int_0^{10}20te^{-.6t}dt}'),F(r'\int_0^{10}20te^{-.6t}dt={500\over9}(1-7e^{-6})')],m(r'Q\approx'+f'{float(q23):.6f}'+r'\mathrm{L/s}='+f'{float(q23*60):.4f}'+r'\mathrm{L/min}'))
def sim(vals,step):return R(step)/3*sum((1 if i in[0,len(vals)-1]else 4 if i%2 else 2)*R(str(v))for i,v in enumerate(vals))
v24=sim([0,4.1,8.9,8.5,6.7,4.3,2.5,1.2,.2],2);q24=R('5.5')/v24
add(24,'염료5.5mg 주입 후 t=0,2,…,16초의 농도는[0,4.1,8.9,8.5,6.7,4.3,2.5,1.2,.2]mg/L이다. Simpson 법칙으로 심박출량을 추정하라.','After5.5mg dye,concentrations at t=0,2,…,16seconds are[0,4.1,8.9,8.5,6.7,4.3,2.5,1.2,.2]mg/L.Use Simpson’s rule for cardiac output.',[F(r'\int_0^{16}c(t)dt\approx\tfrac23[c_0+4c_1+2c_2+\cdots+4c_7+c_8]='+tx(v24)),F(r'Q\approx5.5/'+tx(v24))],m(r'Q\approx'+f'{float(q24):.6f}'+r'\mathrm{L/s}='+f'{float(q24*60):.4f}'+r'\mathrm{L/min}'))
ys25=[0,6,7.4,6.7,5.4,4.1,3,2.2,1.5];v25=sim(ys25,2);q25=7/v25
add(25,'염료7mg 주입 후 주어진0~16초 농도 그래프에서 Simpson 법칙으로 심박출량을 추정하라.','Use Simpson’s rule on the supplied0–16second concentration graph after7mg dye to estimate cardiac output.',[('2초 간격으로 농도를 약[0,6,7.4,6.7,5.4,4.1,3,2.2,1.5]mg/L로 읽는다. 그래프 근사값이며 결과도 이에 따른 추정이다.','Read approximate concentrations[0,6,7.4,6.7,5.4,4.1,3,2.2,1.5]mg/L at2second intervals.The result is a graphical estimate.'),F(r'\int_0^{16}c(t)dt\approx S_8='+tx(v25)),F(r'Q\approx7/S_8')],m(r'Q\approx'+f'{float(q25*60):.2f}'+r'\mathrm{L/min}'))
assert sorted(b.E)==list(range(1,26))
def norm(v):
 if isinstance(v,str):
  chunks=re.split(r'(\\\(.*?\\\)|\\\[.*?\\\])',v,flags=re.S);return ''.join(z if i%2 else z.replace('<',r'\(\lt\)')for i,z in enumerate(chunks))
 if isinstance(v,list):return[norm(z)for z in v]
 if isinstance(v,dict):return{k:norm(z)for k,z in v.items()}
 return v
b.E=norm(b.E);b.save();Path(__file__).with_name('s8-4-report.json').write_text(json.dumps({'section':'8.4','exercises':25,'exactIntegrals':records,'numerical':{'8quantity':str(q8),'8surplus':str(cs8),'11quantity':str(q11),'11surplus':str(ps11)}},ensure_ascii=False,indent=2)+'\n');print('8.4 authored25')
