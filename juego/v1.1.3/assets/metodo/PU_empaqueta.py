#!/usr/bin/env python3
"""PU_empaqueta.py · EL EMPAQUETADO COMO PROGRAMA (decisión de la dirección, 10-10-2026; nace en H S.17). De la carpeta de la build —el fichero
   de juego versionado más «assets/»— produce las DOS formas de distribución, y nada más que ellas:
     1 · el PAQUETE WEB: la carpeta tal cual, para servir por https (o para abrir en un ordenador descomprimida), en los dos
         zips de §0.2 cuando pesan más de lo que admite el canal: «…_parte1.zip» (fichero de juego + imagenes + metodo) y
         «…_parte2_audio.zip» (audio). Es el artefacto del proyecto: sobre él corre el banco.
     2 · la COPIA DE UN SOLO FICHERO: el mismo fichero de juego con las 143 piezas de «assets/» incrustadas en base64
         —las 137 imágenes y las 6 piezas de audio por el hueco `ART_EMBEBIDO` que `assetURL` lee, y las cuatro texturas
         de la hoja de estilo, que no pasan por `assetURL`, sustituidas en su `url()`—, para descargar y jugar en local
         sin carpeta al lado (H586). Lo de «assets/metodo/» no se incrusta: el registro de procedencia, el prompt maestro y
         este mismo programa, que el juego no carga; viajan con el paquete web.
         [14-11-2026 · G17 S.4-bis · H721, al lado y no encima: desde la v1.0.6 las piezas de audio son 7 y no 6 —entró el sello
         de las transiciones de época, `PU_epoca.mp3`—, y con ellas las piezas incrustadas son 144 y no 143.]
         [14-11-2026 · G17 S.4-ter, al lado y no encima: desde la v1.0.9 las imágenes son 159 y no 137 —entran los veintidós
         rostros de «assets/imagenes/rostros/», que el fichero de juego declara como familia—, y las piezas incrustadas son 166.]
   Lo que el programa afirma antes de escribir nada, y para con error si no se cumple: que la build trae un solo fichero
   de juego y su versión coincide con el nombre; que toda ruta «assets/…» que el fichero nombra existe en la carpeta y
   que toda pieza de la carpeta (salvo metodo) la nombra el fichero o vive en una de sus carpetas de familia; que la copia
   única no conserva ninguna ruta a «assets/» fuera de comentarios; y las huellas y pesos de lo que sale.
   DÓNDE VIVE (decisión de la dirección, 11-10-2026): en «assets/metodo/», al lado del registro de procedencia y del prompt
   maestro, para que viaje con el paquete y nadie tenga que custodiarlo aparte. Es método y no pieza: no lleva fila en el
   registro y no se incrusta en la copia. Se conserva además en el paquete de la sesión H S.17, con los dos instrumentos
   que comprueban lo que produce (h17_compara_copia.py y h17_sirve_paquete.py), que necesitan Chromium y no viajan aquí.
   Uso, desde cualquier sitio: python3 PU_empaqueta.py <carpeta_de_la_build> <carpeta_de_salida>"""
import sys, os, re, base64, hashlib, zipfile, json, mimetypes
src, out = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
juegos = [f for f in os.listdir(src) if f.endswith('.html')]
if len(juegos) != 1: raise SystemExit(f'la build tiene que traer UN fichero de juego y trae {len(juegos)}: {juegos}')
nombre = juegos[0]; m = re.match(r'Progressus_Universitas_v(\d+)_(\d+)_(\d+)\.html$', nombre)
if not m: raise SystemExit('el fichero de juego no lleva versión en su nombre: ' + nombre)
version = 'v%s.%s.%s' % m.groups(); base = nombre[:-5]
html = open(os.path.join(src, nombre), encoding='utf-8').read()
if ('const PROTO_VERSION = "%s";' % version) not in html: raise SystemExit('PROTO_VERSION no coincide con el nombre: ' + version)
assets = os.path.join(src, 'assets')
if not os.path.isdir(assets): raise SystemExit('falta assets/')
sobra = [f for f in os.listdir(src) if f not in (nombre, 'assets')]
if sobra: raise SystemExit('la raíz de la build trae más que el fichero de juego y assets/: ' + ', '.join(sobra))
piezas = sorted(os.path.relpath(os.path.join(d, f), src).replace(os.sep, '/') for d, _, fs in os.walk(assets) for f in fs)
MIME = {'.webp': 'image/webp', '.mp3': 'audio/mpeg', '.png': 'image/png', '.jpg': 'image/jpeg', '.svg': 'image/svg+xml'}
sha = lambda b: hashlib.sha256(b).hexdigest()

# ── 1 · las rutas que el fichero nombra, todas existentes ──
rutas = set(re.findall(r'"(assets/[^"\s]+\.(?:webp|mp3|png|jpg|svg))"', html)) | set(re.findall(r'url\("(assets/[^"]+)"\)', html))
faltan = [r for r in rutas if not os.path.exists(os.path.join(src, r))]
if faltan: raise SystemExit('el fichero nombra piezas que no están en assets/: ' + ', '.join(faltan))
familias = set(re.findall(r'"(assets/[^"\s]+/)"', html))   # «assets/imagenes/plaza/» y hermanas: sus ficheros se piden por nombre compuesto
incrustables = [p for p in piezas if not p.startswith('assets/metodo/')]
huerfanas = [p for p in incrustables if p not in rutas and not any(p.startswith(f) for f in familias)]
if huerfanas: raise SystemExit('piezas en assets/ que el fichero no nombra ni por ruta ni por familia: ' + ', '.join(huerfanas))

# ── 2 · la copia de un solo fichero: se arma y se comprueba en memoria, antes de escribir nada ──
emb = {}
for p in incrustables:
    ext = os.path.splitext(p)[1].lower(); mime = MIME.get(ext) or mimetypes.guess_type(p)[0]
    if not mime: raise SystemExit('sin tipo MIME para ' + p)
    emb[p] = 'data:%s;base64,%s' % (mime, base64.b64encode(open(os.path.join(src, p), 'rb').read()).decode('ascii'))
ancla = 'const ART_EMBEBIDO = {};'
if html.count(ancla) != 1: raise SystemExit('el hueco ART_EMBEBIDO no aparece una sola vez')
unico = html.replace(ancla, 'const ART_EMBEBIDO = ' + json.dumps(emb, ensure_ascii=False, separators=(',', ':')) + ';')
texturas = re.findall(r'url\("(assets/[^"]+)"\)', unico)
for t in texturas: unico = unico.replace('url("%s")' % t, 'url("%s")' % emb[t])
# lo que queda de «assets/» en la copia fuera de comentarios tiene que ser una constante de familia o una clave del hueco:
# nunca una petición. Se mira sobre el texto SIN comentarios de bloque ni de línea.
sin_comentarios = re.sub(r'/\*.*?\*/', '', unico, flags=re.S); sin_comentarios = re.sub(r'^\s*//.*$', '', sin_comentarios, flags=re.M)
sin_comentarios = re.sub(r'<!--.*?-->', '', sin_comentarios, flags=re.S)
vivas = [x for x in re.findall(r'assets/[A-Za-z0-9_./-]*', sin_comentarios) if not x.endswith('/')]   # las que acaban en «/» son las constantes de familia
vivas = sorted(set(x for x in vivas if x not in emb))   # las claves del hueco siguen escritas en su literal, y es correcto: assetURL las resuelve
# H S.17 · la sesión lo corrige al lado de lo que la cabecera promete: esta comprobación PARA, y para ANTES de escribir nada.
# En la forma de la preparación sólo se imprimía, después de haber escrito ya los dos zips, y sólo miraba rutas entre comillas dobles.
if vivas: raise SystemExit('la copia de un solo fichero conservaría ' + str(len(vivas)) + ' rutas a «assets/» sin resolver fuera de comentarios, y no se escribe nada: ' + ', '.join(vivas[:8]))

# ── 3 · ahora sí se escribe: el paquete web en los dos zips de §0.2, y la copia ──
os.makedirs(out, exist_ok=True)
def zipea(nombre_zip, filtro):
    """Los zips son REPRODUCIBLES: mismo contenido, misma huella. Las entradas van en orden fijo y con una fecha fija, porque
       un zip hecho con las fechas del disco cambia de huella cada vez que se copia la carpeta, y entonces «byte a byte» no
       significaría nada."""
    ruta = os.path.join(out, nombre_zip)
    entradas = sorted(r for r in [nombre] + piezas if filtro(r))
    with zipfile.ZipFile(ruta, 'w') as z:
        for rel in entradas:
            zi = zipfile.ZipInfo(rel, date_time=(2026, 1, 1, 0, 0, 0)); zi.compress_type = zipfile.ZIP_DEFLATED; zi.external_attr = 0o644 << 16
            z.writestr(zi, open(os.path.join(src, rel), 'rb').read())
    return ruta
p1 = zipea(base + '_parte1.zip', lambda r: not r.startswith('assets/audio/'))
p2 = zipea(base + '_parte2_audio.zip', lambda r: r.startswith('assets/audio/'))

nombre_unico = base + "_completo.html"
open(os.path.join(out, nombre_unico), 'w', encoding='utf-8').write(unico)

# ── 4 · lo que sale, con sus huellas y pesos ──
def peso(p): return os.path.getsize(p)
fam = {}
for p in piezas:
    k = p.split('/')[1]; fam[k] = fam.get(k, 0) + peso(os.path.join(src, p))
informe = {
  'version': version, 'programa': {'nombre': os.path.basename(__file__), 'sha256': sha(open(os.path.abspath(__file__), 'rb').read())}, 'fichero_de_juego': {'nombre': nombre, 'bytes': peso(os.path.join(src, nombre)), 'sha256': sha(open(os.path.join(src, nombre), 'rb').read())},
  'familias_en_disco_bytes': fam, 'ficheros_en_assets': len(piezas), 'incrustadas': len(incrustables), 'texturas_sustituidas': texturas,
  'paquete_web': {os.path.basename(p): {'bytes': peso(p), 'sha256': sha(open(p, 'rb').read())} for p in (p1, p2)},
  'copia_unica': {'nombre': nombre_unico, 'bytes': peso(os.path.join(out, nombre_unico)), 'sha256': sha(unico.encode('utf-8')), 'rutas_a_assets_sin_resolver': vivas},
}
open(os.path.join(out, 'INFORME_empaquetado_%s.json' % version), 'w', encoding='utf-8').write(json.dumps(informe, ensure_ascii=False, indent=1))
MiB = lambda b: '%.2f MiB' % (b / 1048576)
print('build', version, '·', len(piezas), 'ficheros en assets/ ·', 'código', MiB(informe['fichero_de_juego']['bytes']), '· imagenes', MiB(fam.get('imagenes', 0)), '· audio', MiB(fam.get('audio', 0)), '· metodo', MiB(fam.get('metodo', 0)))
for k, v in informe['paquete_web'].items(): print('  ', k, MiB(v['bytes']), v['sha256'][:16])
print('  ', nombre_unico, MiB(informe['copia_unica']['bytes']), informe['copia_unica']['sha256'][:16], '·', len(incrustables), 'ficheros incrustados ·', len(texturas), 'texturas sustituidas ·', len(vivas), 'rutas a «assets/» sin resolver')
if vivas: print('     ', '\n      '.join(l.strip()[:120] for l in vivas[:8]))
