import math, random, os
D=os.path.dirname(os.path.abspath(__file__))
G=['#FFF3B0','#FFD84D','#F5B82E','#E0952A','#B8701E','#8A4F14']
CREAM='#FFF8E1'; BLK='#0A0805'; RED='#E03A2F'
HAMMER=('M540,108 a42,42 0 1 1 -0.1,0 z M540,135 a15,15 0 1 0 0.1,0 z M506,190 h68 v130 h-68 z '
 'M430,318 h220 q20,0 34,16 l110,160 q24,36 -6,70 q-20,22 -40,10 q-20,-12 -40,-4 q-60,24 -168,24 '
 'q-108,0 -168,-24 q-20,-8 -40,4 q-20,12 -40,-10 q-30,-34 -6,-70 l110,-160 q14,-16 34,-16 z')
AXE=('<g><rect x="-11" y="-262" width="22" height="545" rx="9"/>'
 '<path d="M6,-252 L60,-264 Q122,-240 142,-170 Q152,-110 128,-36 Q96,-70 60,-88 Q30,-100 6,-122 Z"/></g>')
def place(cx,cy,k,ox=540,oy=354): return f'translate({cx},{cy}) scale({k}) translate({-ox},{-oy})'
def bands(x,y,w,h,cols=G):
    wt=[.27,.2,.16,.13,.1,.08]; gp=[0,.012,.018,.024,.03,.036]; s=sum(wt)+sum(gp); out=''; cy=y
    for i,c in enumerate(cols):
        cy+=gp[i]/s*h; hh=wt[i]/s*h; out+=f'<rect x="{x}" y="{cy:.1f}" width="{w}" height="{hh+.5:.1f}" fill="{c}"/>'; cy+=hh
    return out
def chrome(id,y1,y2,hi='#FFFBE6',mid='#FFD84D',dark='#5A2F08',lo='#FFE08A'):
    return (f'<linearGradient id="{id}" gradientUnits="userSpaceOnUse" x1="0" y1="{y1}" x2="0" y2="{y2}">'
     f'<stop offset="0" stop-color="{hi}"/><stop offset=".45" stop-color="{mid}"/><stop offset=".5" stop-color="{dark}"/>'
     f'<stop offset=".56" stop-color="#B8701E"/><stop offset="1" stop-color="{lo}"/></linearGradient>')
def grid(y0,col='#E0952A',op=.55,bottom=1080):
    s=f'<g stroke="{col}" stroke-width="2" opacity="{op}">'
    for k in range(1,9):
        y=y0+(bottom-y0)*(k/8)**2; s+=f'<line x1="0" y1="{y:.1f}" x2="1080" y2="{y:.1f}"/>'
    for i in range(-12,13): s+=f'<line x1="{540+i*28}" y1="{y0}" x2="{540+i*170}" y2="{bottom}"/>'
    return s+'</g>'
def stars(n,seed,y1=0,y2=1080):
    r=random.Random(seed); return ''.join(f'<circle cx="{r.uniform(0,1080):.0f}" cy="{r.uniform(y1,y2):.0f}" r="{r.choice([1,1,1.5,2,2.5])}" fill="{CREAM}" opacity="{r.uniform(.3,.9):.2f}"/>' for _ in range(n))
def spark(x,y,s=40,c=CREAM):
    return f'<path d="M{x},{y-s} Q{x+s*.12},{y-s*.12} {x+s},{y} Q{x+s*.12},{y+s*.12} {x},{y+s} Q{x-s*.12},{y+s*.12} {x-s},{y} Q{x-s*.12},{y-s*.12} {x},{y-s} Z" fill="{c}"/>'
COMMON=f'''<filter id="blur" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="14"/></filter>
<filter id="blur6" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="6"/></filter>
<filter id="soft"><feGaussianBlur stdDeviation="1"/></filter>
<pattern id="slats" width="10" height="12" patternUnits="userSpaceOnUse"><rect width="10" height="8" fill="#fff"/></pattern>
<mask id="slatMask"><rect width="1080" height="1080" fill="url(#slats)"/></mask>
<path id="hammer" d="{HAMMER}" fill-rule="evenodd"/>'''
def page(fonts,defs,body,bg='#000'):
    return f'''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?{fonts}&display=block" rel="stylesheet">
<style>html,body{{margin:0;background:#000}}#stage{{position:relative;width:1080px;height:1080px;overflow:hidden;background:{bg}}}svg{{position:absolute;inset:0}}
#scan{{position:absolute;inset:0;background:repeating-linear-gradient(to bottom,rgba(0,0,0,.26) 0 2px,rgba(255,255,255,.02) 2px 4px)}}
#vig{{position:absolute;inset:0;background:radial-gradient(ellipse at center,transparent 55%,rgba(0,0,0,.75) 100%)}}</style></head>
<body><div id="stage"><svg viewBox="0 0 1080 1080" width="1080" height="1080"><defs>{COMMON}{defs}</defs>
<g filter="url(#soft)">{body}</g></svg><div id="scan"></div><div id="vig"></div></div></body></html>'''
DARK='radial-gradient(ellipse at 50% 40%,#17120a 0%,#070604 60%,#000 100%)'
P={}

# 01 Sunset shield + crossed axes
w01=lambda f,t='': f'<text x="540" y="790" text-anchor="middle" font-family="Archivo Black" font-size="140" fill="{f}" transform="skewX(-8) translate(111,0) {t}">VALHALLA</text>'
P['01-shield']=('family=Archivo+Black',
 chrome('ch',680,800)+'<clipPath id="sh"><circle cx="540" cy="360" r="225"/></clipPath>',
 grid(890)+
 f'<g fill="{CREAM}" stroke="{BLK}" stroke-width="8" transform="translate(540,400) rotate(-38) scale(-1.45,1.45)">{AXE}</g>'
 f'<g fill="{CREAM}" stroke="{BLK}" stroke-width="8" transform="translate(540,400) scale(-1,1) rotate(-38) scale(-1.45,1.45)">{AXE}</g>'
 f'<g opacity=".5" filter="url(#blur)"><circle cx="540" cy="360" r="225" fill="#F5B82E"/></g>'
 f'<g clip-path="url(#sh)">{bands(300,135,480,450)}</g>'
 f'<circle cx="540" cy="360" r="225" fill="none" stroke="{CREAM}" stroke-width="12"/>'
 f'<circle cx="540" cy="360" r="205" fill="none" stroke="{BLK}" stroke-width="5" stroke-dasharray="2 36"/>'
 f'<circle cx="540" cy="360" r="46" fill="{BLK}" stroke="{CREAM}" stroke-width="9"/><circle cx="540" cy="360" r="14" fill="{G[1]}"/>'
 f'<g mask="url(#slatMask)">{w01(G[4],"translate(0,40)")}{w01(G[2],"translate(0,20)")}</g>'
 f'<g opacity=".5" filter="url(#blur)">{w01(G[1])}</g>{w01("url(#ch)")}'
 f'<text x="540" y="870" text-anchor="middle" font-family="Archivo Black" font-size="50" letter-spacing="22" fill="{CREAM}">WLC</text>', DARK)

# 02 Neon sign: horned helm + script
helm=('M380,420 Q380,230 540,230 Q700,230 700,420 Z M366,410 h348 v40 h-348 z M528,450 h24 v90 h-24 z '
      'M392,330 Q300,300 296,170 Q330,262 404,284 M688,330 Q780,300 784,170 Q750,262 676,284')
neon=lambda col,w: f'<path d="{helm}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>'
scr=lambda f,extra='': f'<text x="540" y="760" text-anchor="middle" font-family="Yellowtail" font-size="230" fill="{f}" {extra} transform="rotate(-6 540 700)">Valhalla</text>'
P['02-neon']=('family=Yellowtail&family=Archivo+Black','',
 f'<rect width="1080" height="1080" fill="#0B0906"/>'
 +''.join(f'<rect x="{(i%2)*-60+j*120}" y="{i*48}" width="114" height="42" fill="#15100A"/>' for i in range(23) for j in range(10))+
 f'<g filter="url(#blur)" opacity=".9">{neon(G[2],22)}</g><g filter="url(#blur6)">{neon(G[1],12)}</g>{neon("#FFF6D0",5)}'
 f'<g filter="url(#blur)" opacity=".9">{scr(G[3])}</g><g filter="url(#blur6)">{scr(G[1])}</g>{scr("#FFF6D0")}'
 f'<g filter="url(#blur6)"><text x="540" y="920" text-anchor="middle" font-family="Archivo Black" font-size="90" letter-spacing="30" fill="none" stroke="{RED}" stroke-width="10">WLC</text></g>'
 f'<text x="555" y="920" text-anchor="middle" font-family="Archivo Black" font-size="90" letter-spacing="30" fill="none" stroke="#FFD6CF" stroke-width="3">WLC</text>','#0B0906')

# 03 GTA-style stripe V
sv=''
for k,c in enumerate([G[0],G[1],G[2],G[3],G[4]]):
    a=690+29*k; b=a+26; sv+=f'<polygon points="{a},540 {b},540 {826+12*k},790 {814+12*k},790" fill="{c}"/>'
P['03-stripes']=('family=Archivo+Black','',
 f'<g opacity=".45" filter="url(#blur)"><text x="80" y="420" font-family="Archivo Black" font-size="158" fill="{CREAM}" letter-spacing="-4">VALHALLA</text></g>'
 f'<text x="80" y="420" font-family="Archivo Black" font-size="158" fill="{CREAM}" letter-spacing="-4">VALHALLA</text>'
 f'<text x="80" y="790" font-family="Archivo Black" font-size="268" fill="{CREAM}" letter-spacing="-10">WLC</text>'
 f'<g opacity=".6" filter="url(#blur6)">{sv}</g>{sv}'
 f'<polygon points="892,790 1020,540 982,540 878,744" fill="none" stroke="{CREAM}" stroke-width="7" stroke-linejoin="round"/>'
 f'<g filter="url(#blur6)">{spark(1018,540,46)}</g>{spark(1018,540,40)}'
 f'<text x="84" y="880" font-family="Archivo Black" font-size="34" letter-spacing="10" fill="{G[2]}">STRENGTH · HONOUR · IRON</text>', DARK)

# 04 Arcade pixel helmet
rows=["..H............H..",".HH............HH.",".HH....LGGG....HH.",".HHH.LLGGGGGG.HHH.","..HHLGGGGGGGGGHH..",
"...LGGGGGGGGGGD...","..GGGGGGGGGGGGDD..","..BBBBBBBBBBBBBB..","..BYBBBBBBBBBBYB..","..GG...GNNG...DD..","..GG...GNNG...DD..",
"..GG....NN....DD..","...G....NN....D..."]
cm={'H':G[0],'L':CREAM,'G':G[1],'D':G[3],'B':G[5],'Y':G[0],'N':G[2]}
px=22; x0=540-9*px; y0=150; pix=''
for r,row in enumerate(rows):
    for c,ch in enumerate(row):
        if ch!='.': pix+=f'<rect x="{x0+c*px}" y="{y0+r*px}" width="{px}" height="{px}" fill="{cm[ch]}"/>'
pg=('<linearGradient id="pg" gradientUnits="userSpaceOnUse" x1="0" y1="500" x2="0" y2="580">'
 +''.join(f'<stop offset="{i/5:.2f}" stop-color="{c}"/><stop offset="{(i+1)/5-.001:.3f}" stop-color="{c}"/>' for i,c in enumerate(G[:5]))+'</linearGradient>')
pt=lambda f,t='': f'<text x="540" y="580" text-anchor="middle" font-family="\'Press Start 2P\'" font-size="80" fill="{f}" transform="{t}">VALHALLA</text>'
P['04-arcade']=('family=Press+Start+2P',pg,
 stars(70,4)+
 f'<text x="60" y="70" font-family="\'Press Start 2P\'" font-size="24" fill="{RED}">1UP</text><text x="60" y="104" font-family="\'Press Start 2P\'" font-size="24" fill="{CREAM}">00000</text>'
 f'<text x="1020" y="70" text-anchor="end" font-family="\'Press Start 2P\'" font-size="24" fill="{RED}">HI-SCORE</text><text x="1020" y="104" text-anchor="end" font-family="\'Press Start 2P\'" font-size="24" fill="{CREAM}">1RM PR</text>'
 f'<g opacity=".45" filter="url(#blur)">{pix}</g>{pix}'
 f'{pt(G[5],"translate(8,8)")}{pt("url(#pg)")}'
 f'<text x="540" y="680" text-anchor="middle" font-family="\'Press Start 2P\'" font-size="56" letter-spacing="16" fill="{CREAM}">WLC</text>'
 f'<text x="540" y="840" text-anchor="middle" font-family="\'Press Start 2P\'" font-size="30" fill="{G[1]}">PRESS LIFT TO START</text>'
 f'<text x="540" y="930" text-anchor="middle" font-family="\'Press Start 2P\'" font-size="20" fill="{G[3]}">INSERT PROTEIN  CREDIT 01</text>','#050403')

# 05 VHS cover
vs=''.join(f'<rect x="-300" y="{560+i*56}" width="1700" height="44" fill="{c}"/>' for i,c in enumerate(G))
P['05-vhs']=('family=Archivo+Black','',
 f'<rect width="1080" height="1080" fill="#0A0805"/>'
 f'<g transform="rotate(-18 540 700)"><g opacity=".4" filter="url(#blur)">{vs}</g>{vs}</g>'
 f'<text x="70" y="250" font-family="Archivo Black" font-size="175" fill="{CREAM}" letter-spacing="-6" transform="skewX(-10) translate(44,0)">VALHALLA</text>'
 f'<rect x="80" y="290" width="920" height="10" fill="{RED}"/>'
 f'<text x="80" y="360" font-family="Archivo Black" font-size="40" letter-spacing="14" fill="{G[1]}">HEAVY DUTY · HIGH GRADE</text>'
 f'<g transform="{place(860,800,.6)}"><use href="#hammer" fill="{CREAM}" stroke="{BLK}" stroke-width="14" stroke-linejoin="round"/></g>'
 f'<rect x="80" y="880" width="330" height="120" fill="{CREAM}"/><text x="245" y="972" text-anchor="middle" font-family="Archivo Black" font-size="96" letter-spacing="6" fill="{BLK}">WLC</text>'
 f'<rect x="430" y="880" width="120" height="120" fill="none" stroke="{CREAM}" stroke-width="6"/><text x="490" y="934" text-anchor="middle" font-family="Archivo Black" font-size="30" fill="{CREAM}">HI-FI</text><text x="490" y="972" text-anchor="middle" font-family="Archivo Black" font-size="30" fill="{CREAM}">IRON</text>','#0A0805')

# 06 Aerobics: chrome block + script
cw=lambda f,t='': f'<text x="540" y="760" text-anchor="middle" font-family="Archivo Black" font-size="340" letter-spacing="-10" fill="{f}" transform="skewX(-10) translate(134,0) {t}">WLC</text>'
sc=lambda f,extra='': f'<text x="530" y="560" text-anchor="middle" font-family="Yellowtail" font-size="220" fill="{f}" {extra} transform="rotate(-8 540 520)">Valhalla</text>'
lasers=''.join(f'<rect x="0" y="{y}" width="1080" height="{h}" fill="{G[2]}" opacity="{o}"/>' for y,h,o in [(250,2,.35),(268,4,.5),(292,7,.6),(860,7,.6),(884,4,.5),(902,2,.35)])
P['06-script']=('family=Yellowtail&family=Archivo+Black',chrome('ch',525,760),
 stars(90,6)+lasers+
 f'<g mask="url(#slatMask)">{cw(G[4],"translate(0,44)")}{cw(G[2],"translate(0,22)")}</g>'
 f'<g opacity=".45" filter="url(#blur)">{cw(G[1])}</g>{cw("url(#ch)","stroke=\"#FFF8E1\" stroke-width=\"4\"")}'
 f'{sc(BLK,"stroke=\"#0A0805\" stroke-width=\"26\" stroke-linejoin=\"round\"")}<g filter="url(#blur6)">{sc(G[1])}</g>{sc(CREAM)}'
 f'{spark(250,640,34)}{spark(900,410,44)}{spark(830,800,22)}'
 f'<text x="540" y="990" text-anchor="middle" font-family="Archivo Black" font-size="34" letter-spacing="18" fill="{G[1]}">LIFT LIKE A LEGEND</text>', '#050403')

# 07 Heavy metal
rays=''.join(f'<polygon points="540,470 {540+900*math.cos(math.radians(a-2.2)):.0f},{470+900*math.sin(math.radians(a-2.2)):.0f} {540+900*math.cos(math.radians(a+2.2)):.0f},{470+900*math.sin(math.radians(a+2.2)):.0f}" fill="{G[4]}" opacity=".35"/>' for a in range(0,360,12))
mt=lambda f,extra='',t='': f'<text x="540" y="560" text-anchor="middle" font-family="Metal Mania" font-size="210" fill="{f}" {extra} transform="{t}">VALHALLA</text>'
bolt=lambda x,y,s: f'<polygon points="{x},{y} {x+30*s},{y} {x+8*s},{y+60} {x+34*s},{y+60} {x-14*s},{y+150} {x+2*s},{y+80} {x-22*s},{y+80}" fill="{CREAM}"/>'
P['07-metal']=('family=Metal+Mania',chrome('ch',400,560),
 rays+f'<circle cx="540" cy="470" r="300" fill="url(#fadeC)"/>'
 f'<g fill="{G[1]}" stroke="{BLK}" stroke-width="10" transform="translate(540,470) rotate(-40) scale(-1.15,1.15)">{AXE}</g>'
 f'<g fill="{G[1]}" stroke="{BLK}" stroke-width="10" transform="translate(540,470) scale(-1,1) rotate(-40) scale(-1.15,1.15)">{AXE}</g>'
 f'{mt(BLK,"stroke=\"#0A0805\" stroke-width=\"30\" stroke-linejoin=\"round\"")}'
 f'<g opacity=".5" filter="url(#blur)">{mt(G[1])}</g>{mt("url(#ch)","stroke=\"#FFF8E1\" stroke-width=\"3\"")}'
 f'<g filter="url(#blur6)">{bolt(110,400,1)}{bolt(970,400,-1)}</g>{bolt(110,400,1)}{bolt(970,400,-1)}'
 f'<g filter="url(#blur6)"><text x="540" y="760" text-anchor="middle" font-family="Metal Mania" font-size="140" fill="{RED}">WLC</text></g>'
 f'<text x="540" y="760" text-anchor="middle" font-family="Metal Mania" font-size="140" fill="{RED}" stroke="#FFD6CF" stroke-width="2">WLC</text>'
 f'<text x="540" y="880" text-anchor="middle" font-family="Metal Mania" font-size="54" letter-spacing="6" fill="{G[1]}">~ Forged in Iron ~</text>', '#050403')
P['07-metal']=(P['07-metal'][0],P['07-metal'][1]+'<radialGradient id="fadeC"><stop offset="0" stop-color="#000" stop-opacity=".0"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>',P['07-metal'][2],P['07-metal'][3])

# 08 Circular badge (globe-style)
globe=''.join(f'<ellipse cx="540" cy="540" rx="{rx}" ry="250" fill="none"/>' for rx in [250,190,120,45])+''.join(f'<line x1="{540-math.sqrt(max(0,250**2-(y-540)**2)):.0f}" y1="{y}" x2="{540+math.sqrt(max(0,250**2-(y-540)**2)):.0f}" y2="{y}"/>' for y in range(320,780,55))
ring='VALHALLA · WLC · STRENGTH · HONOUR · VALHALLA · WLC · STRENGTH · HONOUR · '
bw=lambda f,extra='': f'<text x="540" y="590" text-anchor="middle" font-family="Archivo Black" font-size="132" letter-spacing="-3" fill="{f}" {extra}>VALHALLA</text>'
P['08-badge']=('family=Archivo+Black','<path id="circ" d="M540,540 m-345,0 a345,345 0 1,1 690,0 a345,345 0 1,1 -690,0"/>',
 f'<g opacity=".45" filter="url(#blur)"><circle cx="540" cy="540" r="420" fill="{G[2]}"/></g>'
 f'<circle cx="540" cy="540" r="420" fill="{G[2]}"/><circle cx="540" cy="540" r="300" fill="none" stroke="{BLK}" stroke-width="6"/>'
 f'<circle cx="540" cy="540" r="408" fill="none" stroke="{BLK}" stroke-width="4"/>'
 f'<text font-family="Archivo Black" font-size="40" letter-spacing="3.2" fill="{BLK}"><textPath href="#circ">{ring}</textPath></text>'
 f'<g stroke="{G[5]}" stroke-width="5">{globe}</g>'
 f'<g transform="{place(540,350,.3)}"><use href="#hammer" fill="{BLK}"/></g>'
 f'{bw(BLK,"stroke=\"#0A0805\" stroke-width=\"22\" stroke-linejoin=\"round\"")}{bw(G[0])}'
 f'<text x="540" y="690" text-anchor="middle" font-family="Archivo Black" font-size="60" letter-spacing="20" fill="{BLK}">WLC</text>', DARK)

# 09 Longship synthwave
ship=(f'<path d="M300,548 L780,548 Q768,606 540,610 Q312,606 300,548 Z" fill="{BLK}"/>'
 f'<path d="M770,552 Q812,540 812,492 Q812,448 846,440 Q864,446 852,458 Q828,464 828,500 Q828,560 772,566 Z" fill="{BLK}"/>'
 f'<path d="M310,552 Q268,540 268,500 Q268,466 248,458 Q240,468 252,476 Q254,506 256,516 Q264,560 308,566 Z" fill="{BLK}"/>'
 f'<rect x="535" y="300" width="10" height="250" fill="{BLK}"/><rect x="420" y="316" width="240" height="8" fill="{BLK}"/>'
 '<clipPath id="sail"><path d="M424,322 L656,322 Q676,420 650,512 L430,512 Q404,420 424,322 Z"/></clipPath>'
 f'<g clip-path="url(#sail)">'+''.join(f'<rect x="{400+i*40}" y="300" width="40" height="230" fill="{[CREAM,RED][i%2]}"/>' for i in range(7))+'</g>'
 f'<path d="M424,322 L656,322 Q676,420 650,512 L430,512 Q404,420 424,322 Z" fill="none" stroke="{BLK}" stroke-width="7"/>'
 +''.join(f'<circle cx="{x}" cy="560" r="15" fill="{G[1]}" stroke="{BLK}" stroke-width="5"/>' for x in range(350,740,40)))
P['09-longship']=('family=Monoton',
 f'<clipPath id="sunc"><circle cx="540" cy="420" r="270"/></clipPath><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000"/><stop offset="1" stop-color="#2A1A06"/></linearGradient>',
 f'<rect width="1080" height="610" fill="url(#sky)"/>'+stars(60,9,0,300)+
 f'<g opacity=".55" filter="url(#blur)"><circle cx="540" cy="420" r="270" fill="{G[2]}"/></g>'
 f'<g clip-path="url(#sunc)">{bands(260,150,560,460)}</g>'
 f'<rect x="0" y="606" width="1080" height="474" fill="#0A0805"/>{grid(606,G[3],.6)}'
 f'{ship}<rect x="0" y="604" width="1080" height="4" fill="{G[1]}"/>'
 f'<rect x="0" y="700" width="1080" height="380" fill="url(#fadeB)"/>'
 f'<g filter="url(#blur6)"><text x="540" y="835" text-anchor="middle" font-family="Monoton" font-size="118" fill="{G[1]}">VALHALLA</text></g>'
 f'<text x="540" y="835" text-anchor="middle" font-family="Monoton" font-size="118" fill="{CREAM}">VALHALLA</text>'
 f'<text x="540" y="960" text-anchor="middle" font-family="Monoton" font-size="84" letter-spacing="20" fill="{G[2]}">WLC</text>','#000')
P['09-longship']=(P['09-longship'][0],P['09-longship'][1]+'<linearGradient id="fadeB" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity="0"/><stop offset=".3" stop-color="#000" stop-opacity=".7"/><stop offset="1" stop-color="#000" stop-opacity=".85"/></linearGradient>',P['09-longship'][2],P['09-longship'][3])

# 10 Block V (TV-ident style)
V=["X...X","X...X","XX.XX",".XXX.","..X.."]
bc=[[G[3],G[2],G[1],G[2],G[3]],[G[4],G[2],G[0],G[2],G[4]],[G[3],G[1],G[0],G[1],G[3]],[G[4],G[2],G[1],G[2],G[4]],[G[4],G[3],G[2],G[3],G[4]]]
blk=''
for r,row in enumerate(V):
    for c,ch in enumerate(row):
        if ch=='X': blk+=f'<rect x="{298+c*98}" y="{110+r*98}" width="88" height="88" rx="16" fill="{bc[r][c]}"/>'
P['10-blocks']=('family=Montserrat:wght@500;800','',
 f'<g opacity=".5" filter="url(#blur)">{blk}</g>{blk}'
 f'<g opacity=".4" filter="url(#blur)"><text x="540" y="760" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="170" letter-spacing="-6" fill="{CREAM}">Valhalla</text></g>'
 f'<text x="540" y="760" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="170" letter-spacing="-6" fill="{CREAM}">Valhalla</text>'
 f'<text x="540" y="830" text-anchor="middle" font-family="Montserrat" font-weight="500" font-size="44" letter-spacing="2" fill="{CREAM}">Train like a Viking</text>'
 f'<text x="540" y="930" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="56" letter-spacing="26" fill="{G[1]}">WLC</text>', DARK)

for k,(f,d,b,bg) in P.items(): open(f'{D}/{k}.html','w').write(page(f,d,b,bg))
print(len(P))
