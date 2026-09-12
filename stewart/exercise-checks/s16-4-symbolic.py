import sympy as s
x,y,t,r=s.symbols('x y t r',real=True)
vals={1:s.integrate((2*x*y-2*y),(y,0,4),(x,0,5)),3:s.integrate(2*x*y**3-x,(y,0,2*x),(x,0,1)),4:s.integrate(y-2*x*x*y,(y,x*x,1),(x,0,1)),6:s.integrate(-y/x**2-1/y,(y,1,4),(x,1,2)),7:s.integrate(-2*x*x*y,(y,0,3*x),(x,0,1)),8:s.integrate(2*x-2*y,(x,0,2*y),(y,0,1)),14:s.integrate(2*x+2*y,(x,y*y,4),(y,0,2)),15:-s.integrate(y,(x,0,2-y/2),(y,0,4)),16:s.integrate(-2*x+2*y,(y,0,s.cos(x)),(x,-s.pi/2,s.pi/2)),18:s.integrate((1-x)/(1+x*x),(x,0,1)),19:s.integrate(x**4*s.cos(x)**5,(x,-s.pi/2,s.pi/2)),20:6*s.integrate(r**11,(r,0,1))*2**8*s.integrate(s.cos(t)**2*s.sin(t)**8,(t,0,2*s.pi)),21:s.integrate(y*y-x,(y,0,1-x),(x,0,1))}
for n,v in vals.items():print(n,s.simplify(v))
print('24',s.integrate(s.expand_trig((5*s.cos(t)-s.cos(5*t))*(5*s.cos(t)-5*s.cos(5*t))-(5*s.sin(t)-s.sin(5*t))*(-5*s.sin(t)+5*s.sin(5*t))),(t,0,2*s.pi))/2)
