# Buduje index.html z src.html: znak Wylinki (oficjalny fragment), logo SVG, symbole przysłony, karty teledysków.
import html
s=open('src.html',encoding='utf-8').read()
s=s.replace('{{BADGE_STYLE}}',open('badge_style.part',encoding='utf-8').read().replace('<style>','').replace('</style>',''))
s=s.replace('{{BADGE_LINK}}',open('badge_link.part',encoding='utf-8').read())
d,g=open('parts/logo_paths.txt',encoding='utf-8').read().split('\n')
logo=f'<svg viewBox="0 0 400 80" aria-hidden="true" focusable="false"><path fill="currentColor" fill-rule="evenodd" d="{d}"/><path fill="#c49a66" fill-rule="evenodd" d="{g}"/></svg>'
s=s.replace('{{LOGO}}',logo)
s=s.replace('{{IRIS}}',open('parts/iris_symbols.txt',encoding='utf-8').read())
F=[l.split('|') for l in open('parts/filmy.txt',encoding='utf-8').read().strip().split('\n')]
out=[]
for k,(i,para,miejsce) in enumerate(F):
    lazy='' if k<0 else ' loading="lazy"'
    out.append(f'''      <figure class="film"><div class="ekran"><button type="button" data-yt="{i}" aria-label="Odtwórz teledysk: {html.escape(para)}"><img src="img/t-{i}-480.webp" srcset="img/t-{i}-480.webp 480w, img/t-{i}-800.webp 800w" sizes="(min-width:2300px) 18vw, (min-width:1700px) 22vw, (min-width:1100px) 30vw, (min-width:640px) 46vw, 86vw" width="800" height="450"{lazy} decoding="async" alt="Kadr z teledysku: {html.escape(para)}"><span class="przeslona" aria-hidden="true"><svg><use href="#irp"/></svg><i></i></span></button></div><figcaption><b>{html.escape(para)}</b><span>{html.escape(miejsce)}</span></figcaption></figure>''')
s=s.replace('{{FILMY}}','\n'.join(out))
open('index.html','w',encoding='utf-8').write(s)
print('ok',len(s))
