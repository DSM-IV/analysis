"""Small dependency-free vector renderer for original mathematical diagrams."""
import math, html
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ASSETS=ROOT/'exercise-content/assets'
ASSETS.mkdir(exist_ok=True)
def solid(filename,title,mapping,axes=(1,1,1),subtitle='',resolution=12):
    # mapping takes a unit-cube parameter triple to a point in the solid.
    pts=[mapping(i/8,j/8,k/8) for i in range(9) for j in range(9) for k in range(9)]
    def raw(p):
        x,y,z=p
        return (.78*y-.58*x,.32*x+.25*y-.95*z)
    projected=[raw(p) for p in pts]+[raw((0,0,0))]
    minx=min(p[0] for p in projected);maxx=max(p[0] for p in projected)
    miny=min(p[1] for p in projected);maxy=max(p[1] for p in projected)
    scale=min(420/max(maxx-minx,.1),300/max(maxy-miny,.1))
    def xy(p):
        q=raw(p);return (300+(q[0]-(minx+maxx)/2)*scale,240+(q[1]-(miny+maxy)/2)*scale)
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 470" role="img"><title>{html.escape(title)}</title><rect width="600" height="470" fill="#fbfcff"/><text x="28" y="34" fill="#17243b" font-family="sans-serif" font-size="19">{html.escape(title)}</text>']
    colors=['#86a9ed','#648bd5','#9ac7c0','#78a69f','#b2beeb','#899acb']
    faces=[]
    for axis in range(3):
        other=[j for j in range(3) if j!=axis]
        for side in (0,1):
            for i in range(resolution):
                for j in range(resolution):
                    p=[]
                    for di,dj in [(0,0),(1,0),(1,1),(0,1)]:
                        q=[0.,0.,0.];q[axis]=side;q[other[0]]=(i+di)/resolution;q[other[1]]=(j+dj)/resolution
                        p.append(mapping(*q))
                    depth=sum(sum(a) for a in p)/4
                    faces.append((depth,p,colors[axis*2+side]))
    for _,p,color in sorted(faces,key=lambda q:q[0]):
        coords=' '.join(f'{u:.2f},{v:.2f}' for u,v in map(xy,p))
        out.append(f'<polygon points="{coords}" fill="{color}" fill-opacity=".72" stroke="#536784" stroke-opacity=".18" stroke-width=".45"/>')
    origin=xy((0,0,0))
    for j,label in enumerate(('x','y','z')):
        p=[0,0,0];p[j]=axes[j];q=xy(p)
        out.append(f'<path d="M{origin[0]:.2f},{origin[1]:.2f}L{q[0]:.2f},{q[1]:.2f}" stroke="#24344e" stroke-width="1.6"/><text x="{q[0]+4:.2f}" y="{q[1]-4:.2f}" font-size="16" font-family="sans-serif">{label}</text>')
    out.append(f'<text x="28" y="438" fill="#3e526e" font-size="13" font-family="sans-serif">{html.escape(subtitle)}</text></svg>')
    (ASSETS/filename).write_text('\n'.join(out))

def attach(item,filename,alt,caption):
    item['figure']={'src':'../exercise-content/assets/'+filename,'alt':{'ko':alt[0],'en':alt[1]},'caption':{'ko':caption[0],'en':caption[1]}}

def points_plot(filename,title,points):
    extent=max(1,max(abs(q) for p in points for q in p))*1.2
    scale=140/extent
    def xy(p):
        x,y,z=p;return (300+scale*(.8*y-.6*x),240+scale*(.32*x+.25*y-z))
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 480" role="img"><title>{html.escape(title)}</title><rect width="600" height="480" fill="#fbfcff"/><text x="25" y="32" font-family="sans-serif" font-size="20">{html.escape(title)}</text>']
    for j,label in enumerate('xyz'):
        ends=[]
        for sign in (-1,1):
            p=[0,0,0];p[j]=sign*extent;ends.append(xy(p))
        q,v=ends
        out.append(f'<path d="M{q[0]},{q[1]}L{v[0]},{v[1]}" stroke="#556780"/><text x="{v[0]+4}" y="{v[1]-5}" font-family="sans-serif" font-size="16">{label}</text>')
    for label,p,color in zip('abcdef',points,['#285eaf','#b04055','#238070','#9444aa']):
        q=xy(p);b=xy((p[0],p[1],0));o=xy((0,0,0))
        out.append(f'<path d="M{o[0]},{o[1]}L{b[0]},{b[1]}L{q[0]},{q[1]}" stroke="{color}" stroke-dasharray="5 4" fill="none"/><circle cx="{q[0]}" cy="{q[1]}" r="5" fill="{color}"/><text x="{q[0]+9}" y="{q[1]-7}" fill="{color}" font-family="sans-serif" font-size="16">{label}</text>')
    for j,(label,p) in enumerate(zip('abcdef',points)):
        labeltext=label+': ('+', '.join(f'{q:.3g}' for q in p)+')'
        out.append(f'<text x="30" y="{428+j*21}" font-family="sans-serif" font-size="14">{labeltext}</text>')
    out.append('</svg>');(ASSETS/filename).write_text('\n'.join(out))

def sphere_cylinder(filename):
    def xy(x,y,z):return (300+150*(.8*y-.6*x),240+150*(.32*x+.25*y-z))
    out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 500" role="img"><title>Sphere and offset cylinder, a = 1</title><rect width="600" height="500" fill="#fbfcff"/><text x="25" y="32" font-family="sans-serif" font-size="20">15.7 / 28 · Sphere and offset cylinder (a = 1)</text>']
    def line(points,color,width=1):
        path=' '.join(('M' if i==0 else 'L')+f'{q[0]:.2f},{q[1]:.2f}' for i,p in enumerate(points) for q in [xy(*p)])
        out.append(f'<path d="{path}" fill="none" stroke="{color}" stroke-width="{width}"/>')
    for j in range(1,12):
        phi=math.pi*j/12
        line([(math.sin(phi)*math.cos(2*math.pi*i/96),math.sin(phi)*math.sin(2*math.pi*i/96),math.cos(phi)) for i in range(97)],'#789fc2')
    for j in range(16):
        theta=2*math.pi*j/16
        line([(math.sin(math.pi*i/64)*math.cos(theta),math.sin(math.pi*i/64)*math.sin(theta),math.cos(math.pi*i/64)) for i in range(65)],'#789fc2')
    for z in (-1.15,1.15):line([(.5+.5*math.cos(2*math.pi*i/96),.5*math.sin(2*math.pi*i/96),z) for i in range(97)],'#bd6f30',1.6)
    for j in range(12):
        q=2*math.pi*j/12;line([(.5+.5*math.cos(q),.5*math.sin(q),z) for z in (-1.15,1.15)],'#bd6f30',1.2)
    for j,label in enumerate('xyz'):
        p=[0,0,0];p[j]=1.3;line([(0,0,0),p],'#24344e',1.4);q=xy(*p)
        out.append(f'<text x="{q[0]+3}" y="{q[1]-3}" font-family="sans-serif" font-size="15">{label}</text>')
    out.extend(['<text x="25" y="459" fill="#456f95" font-family="sans-serif" font-size="14">Sphere: x² + y² + z² = 1</text>','<text x="25" y="481" fill="#9c5921" font-family="sans-serif" font-size="14">Cylinder: (x - 1/2)² + y² = 1/4; shown for -1.15 ≤ z ≤ 1.15</text>','</svg>'])
    (ASSETS/filename).write_text('\n'.join(out))

def section156(items):
    specs={
      9:('Parabolic cylinder and plane',lambda a,b,c:(a,b*(2-c*(1-a*a)),c*(1-a*a)),(1.15,2.1,1.1),'z = 1 - x²; y + z = 2; first octant'),
      10:('A wedge under a parabolic cylinder',lambda a,b,c:(a*2*b,2*b,c*(4-4*b*b)),(2.2,2.2,4.2),'0 ≤ x ≤ y; 0 ≤ z ≤ 4 - y²'),
      11:('Plane above a parabolic base',lambda a,b,c:(2*a,b*4*a*a,c*(2-2*a)),(2.2,4.2,2.2),'0 ≤ y ≤ x²; 0 ≤ z ≤ 2 - x'),
      12:('Symmetric solid with three roofs',lambda a,b,c:((2*a-1)*(4-4*c),(2*b-1)*math.sqrt(max(0,4-4*c)),4*c),(4.3,2.2,4.3),'z - 4 ≤ x ≤ 4 - z; y² ≤ 4 - z; z ≥ 0'),
      31:('Rectangular pyramid',lambda a,b,c:(a*(1-c),2*b*(1-c),c),(1.15,2.2,1.2),'Base: (0,0,0), (1,0,0), (1,2,0), (0,2,0); apex: (0,0,1)'),
      32:('Curved wedge',lambda a,b,c:(a*(4-4*b*b),2*b,c*(2-2*b)),(4.2,2.2,2.2),'x + y² ≤ 4; y + z ≤ 2; x, y, z ≥ 0'),
      37:('Changing order: curved triangular solid',lambda a,b,c:(a*b*b,b,c*(1-b)),(1.15,1.15,1.15),'0 ≤ x ≤ y²; 0 ≤ z ≤ 1 - y'),
      38:('Changing order: two independent roofs',lambda a,b,c:(a,b*(1-a),c*(1-a*a)),(1.15,1.15,1.15),'0 ≤ y ≤ 1 - x; 0 ≤ z ≤ 1 - x²')}
    for n,(title,fn,axes,subtitle) in specs.items():
        filename=f's15-6-{n}.svg';solid(filename,f'15.6 / {n} · {title}',fn,axes,subtitle)
        attach(next(i for i in items if i['number']==n),filename,
               ('해설의 경계 부등식으로 직접 그린 입체와 좌표축', 'Original solid diagram generated from the boundary inequalities, with coordinate axes'),
               (subtitle,subtitle))
