import math, os
D='/home/user/logocreator/forfar-eras'
TRI='540,120 790,470 290,470'
WEB='415,295 457,470 540,120 623,470 665,295'
def place(x,y,k,extra=''): return f'translate({x},{y}) {extra} scale({k}) translate(-540,-295)'
def star(cx,cy,ro,ri,n):
    pts=[]
    for i in range(2*n):
        r=ro if i%2==0 else ri; a=math.pi*i/n-math.pi/2
        pts.append(f'{cx+r*math.cos(a):.1f},{cy+r*math.sin(a):.1f}')
    return ' '.join(pts)
def page(fonts,body):
    return f'''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?{fonts}&display=block" rel="stylesheet">
<style>html,body{{margin:0;background:#000}}#stage{{width:1080px;height:1080px;overflow:hidden}}svg{{display:block}}</style></head>
<body><div id="stage"><svg viewBox="0 0 1080 1080" width="1080" height="1080">{body}</svg></div></body></html>'''

# ---------- 1970s ----------
arcs=''.join(f'<circle cx="540" cy="560" r="{r}" stroke="{c}"/>' for r,c in [(400,'#FFF4DC'),(364,'#C8F26B'),(328,'#8FDB4A'),(292,'#4CBF3A'),(256,'#25A03C')])
w70=lambda f,t: f'<text x="540" y="800" text-anchor="middle" font-family="Shrikhand" font-size="220" fill="{f}" transform="{t}">Forfar</text>'
s70=f'''<defs>
<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 .9 0 0 0 .10 0"/></filter>
<clipPath id="top"><rect width="1080" height="556"/></clipPath></defs>
<rect width="1080" height="1080" fill="#0D3A22"/>
<g clip-path="url(#top)" fill="none" stroke-width="34">{arcs}</g>
<g transform="{place(540,403,.9)}" stroke-linejoin="round" stroke-linecap="round">
 <polygon points="{TRI}" fill="#0D3A22" stroke="#FFF4DC" stroke-width="20"/>
 <polyline points="{WEB}" fill="none" stroke="#FFF4DC" stroke-width="13"/></g>
<rect x="120" y="552" width="840" height="10" rx="5" fill="#FFF4DC"/>
{w70('#1B7A3A','translate(24,20)')}{w70('#4CBF3A','translate(16,13)')}{w70('#C8F26B','translate(8,7)')}{w70('#FFF4DC','')}
<text x="540" y="905" text-anchor="middle" font-family="Righteous" font-size="46" letter-spacing="7" fill="#C8F26B">ROOF TRUSS COMPANY</text>
<text x="540" y="965" text-anchor="middle" font-family="Righteous" font-size="32" letter-spacing="4" fill="#FFF4DC">★ Est. 1993 ★</text>
<rect width="1080" height="1080" filter="url(#grain)"/>'''

# ---------- 1990s ----------
w90=lambda f,t: f'<text x="0" y="0" text-anchor="middle" font-family="Bungee" font-size="182" fill="{f}" stroke="#111" stroke-width="9" paint-order="stroke" stroke-linejoin="round" transform="{t}">FORFAR</text>'
s90=f'''<defs><pattern id="dots" width="26" height="26" patternUnits="userSpaceOnUse"><circle cx="6" cy="6" r="4.5" fill="#111"/></pattern></defs>
<rect width="1080" height="1080" fill="#F4F4EC"/>
<!-- memphis confetti -->
<path d="M70,150 q30,-45 60,0 t60,0 t60,0 t60,0" fill="none" stroke="#22B24C" stroke-width="12" stroke-linecap="round"/>
<rect x="800" y="820" width="220" height="200" fill="url(#dots)"/>
<path d="M80,990 l30,-32 l30,32 l30,-32 l30,32 l30,-32 l30,32" fill="none" stroke="#111" stroke-width="10" stroke-linejoin="round"/>
<path d="M880,960 a90,90 0 0 1 180,0 z" fill="#8FDB4A" stroke="#111" stroke-width="6"/>
<polygon points="120,420 170,500 70,500" fill="none" stroke="#22B24C" stroke-width="9" transform="rotate(18 120 470)"/>
<circle cx="980" cy="440" r="26" fill="none" stroke="#111" stroke-width="8"/>
<rect x="60" y="640" width="70" height="18" fill="#22B24C" stroke="#111" stroke-width="5" transform="rotate(-30 95 649)"/>
<rect x="940" y="620" width="90" height="18" fill="#C8F26B" stroke="#111" stroke-width="5" transform="rotate(40 985 629)"/>
<!-- icon -->
<g transform="{place(540,330,.82,'rotate(-5)')}" stroke-linejoin="round" stroke-linecap="round">
 <polygon points="{TRI}" fill="#111" transform="translate(18,18)"/>
 <polygon points="{TRI}" fill="none" stroke="#111" stroke-width="34"/>
 <polygon points="{TRI}" fill="#22B24C" stroke="#fff" stroke-width="13"/>
 <polyline points="{WEB}" fill="none" stroke="#fff" stroke-width="13"/>
 <polygon points="{TRI}" fill="none" stroke="#fff" stroke-width="5" transform="translate(540,295) scale(.86) translate(-540,-295)" opacity="0"/></g>
<!-- starburst -->
<g transform="rotate(12 875 225)"><polygon points="{star(875,225,108,80,16)}" fill="#C8F26B" stroke="#111" stroke-width="6" stroke-linejoin="round"/>
<text x="875" y="212" text-anchor="middle" font-family="Bungee" font-size="30" fill="#111">SINCE</text>
<text x="875" y="262" text-anchor="middle" font-family="Bungee" font-size="52" fill="#111">'93</text></g>
<!-- wordmark -->
<g transform="translate(540,720) skewX(-10)">{w90('#0B4D2A','translate(14,14)')}{w90('#22B24C','')}</g>
<g transform="rotate(-3 540 800)"><rect x="235" y="760" width="610" height="84" fill="#111"/>
<text x="540" y="818" text-anchor="middle" font-family="Bungee" font-size="46" letter-spacing="4" fill="#fff">ROOF TRUSS CO.</text></g>'''

# ---------- 2000s ----------
t00=lambda f,extra='': f'<text x="540" y="640" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="215" letter-spacing="-8" fill="{f}" {extra}>forfar</text>'
s00=f'''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#D9EADC"/></linearGradient>
<pattern id="pin" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="7" height="14" fill="#fff" opacity=".35"/></pattern>
<linearGradient id="icon" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8BE36A"/><stop offset="1" stop-color="#16803A"/></linearGradient>
<linearGradient id="gloss" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".75"/><stop offset="1" stop-color="#fff" stop-opacity=".08"/></linearGradient>
<linearGradient id="tg" gradientUnits="userSpaceOnUse" x1="0" y1="480" x2="0" y2="645"><stop offset="0" stop-color="#7EDC5A"/><stop offset="1" stop-color="#138036"/></linearGradient>
<linearGradient id="tgloss" gradientUnits="userSpaceOnUse" x1="0" y1="480" x2="0" y2="645"><stop offset="0" stop-color="#fff" stop-opacity=".7"/><stop offset=".48" stop-color="#fff" stop-opacity=".15"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/></linearGradient>
<linearGradient id="fade" gradientUnits="userSpaceOnUse" x1="0" y1="645" x2="0" y2="760"><stop offset="0" stop-color="#fff" stop-opacity=".38"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<mask id="refl"><rect y="640" width="1080" height="200" fill="url(#fade)"/></mask>
<clipPath id="rr"><rect x="390" y="110" width="300" height="300" rx="72"/></clipPath>
<filter id="ds" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#0B4D2A" flood-opacity=".35"/></filter>
<filter id="ts"><feDropShadow dx="0" dy="3" stdDeviation="3" flood-color="#0B4D2A" flood-opacity=".35"/></filter></defs>
<rect width="1080" height="1080" fill="url(#bg)"/><rect width="1080" height="1080" fill="url(#pin)"/>
<g filter="url(#ds)"><rect x="390" y="110" width="300" height="300" rx="72" fill="url(#icon)" stroke="#11702F" stroke-width="3"/></g>
<rect x="397" y="117" width="286" height="286" rx="66" fill="none" stroke="#fff" stroke-opacity=".45" stroke-width="3"/>
<g transform="{place(540,272,.5)}" stroke="#fff" fill="none" stroke-linejoin="round" stroke-linecap="round" filter="url(#ts)">
 <polygon points="{TRI}" stroke-width="26"/><polyline points="{WEB}" stroke-width="18"/></g>
<g clip-path="url(#rr)"><ellipse cx="540" cy="150" rx="250" ry="140" fill="url(#gloss)"/></g>
<g filter="url(#ts)">{t00('url(#tg)','stroke="#fff" stroke-width="6" paint-order="stroke"')}</g>{t00('url(#tgloss)')}
<g mask="url(#refl)"><g transform="translate(0,1290) scale(1,-1)">{t00('#138036')}</g></g>
<text x="540" y="820" text-anchor="middle" font-family="Nunito" font-weight="800" font-size="60" fill="#3F5246">roof truss co.</text>
<text x="540" y="880" text-anchor="middle" font-family="Nunito" font-weight="700" font-size="30" fill="#6B8072" letter-spacing="2">quality roof trusses since 1993</text>
<g transform="rotate(14 880 210)"><polygon points="{star(880,210,100,84,20)}" fill="url(#icon)" stroke="#11702F" stroke-width="2"/>
<polygon points="{star(880,210,100,84,20)}" fill="url(#gloss)" opacity=".5" clip-path="inset(0 0 50% 0)"/>
<text x="880" y="200" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="30" fill="#fff">est.</text>
<text x="880" y="240" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="42" fill="#fff">1993!</text></g>'''

# ---------- 2010s ----------
r=180; c=540; cy=330; o=r/math.sqrt(2)
sh=f'{c+o:.0f},{cy-o:.0f} {c+o+1000:.0f},{cy-o+1000:.0f} {c-o+1000:.0f},{cy+o+1000:.0f} {c-o:.0f},{cy+o:.0f}'
s10=f'''<rect width="1080" height="1080" fill="#1E9E4A"/>
<polygon points="{sh}" fill="#178A3E"/>
<circle cx="{c}" cy="{cy}" r="{r}" fill="#fff"/>
<g transform="{place(540,342,.55)}" stroke="#1E9E4A" fill="none" stroke-linejoin="round" stroke-linecap="round">
 <polygon points="{TRI}" stroke-width="26"/><polyline points="{WEB}" stroke-width="18"/></g>
<text x="552" y="705" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="150" letter-spacing="24" fill="#fff">FORFAR</text>
<rect x="420" y="752" width="240" height="4" fill="#fff" opacity=".7"/>
<text x="547" y="822" text-anchor="middle" font-family="Montserrat" font-weight="500" font-size="40" letter-spacing="14" fill="#fff">ROOF TRUSS CO.</text>
<text x="545" y="878" text-anchor="middle" font-family="Montserrat" font-weight="600" font-size="26" letter-spacing="10" fill="#CFF5D8">EST. 1993</text>'''

pages={'1970s':('family=Shrikhand&family=Righteous',s70),'1990s':('family=Bungee',s90),
 '2000s':('family=Nunito:wght@700;800;900',s00),'2010s':('family=Montserrat:wght@500;600;800',s10)}
for k,(f,b) in pages.items(): open(f'{D}/{k}.html','w').write(page(f,b))
