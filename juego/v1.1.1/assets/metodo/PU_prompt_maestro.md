# Progressus Universitas · El prompt maestro y las referencias

**Nace en H S.2 (H573).** Es uno de los tres ficheros de texto que §17 pone en lugar de la app
descartada. No es un artefacto del proyecto (§0.1: son tres y no hay un cuarto): es contenido de
`assets/`, y por eso viaja dentro del paquete y la dirección no custodia nada nuevo entre sesiones.

**Qué es.** El texto común a todas las piezas de la Fase H, para que la perspectiva, la luz, la
escala y la técnica no haya que volver a describirlas pieza a pieza — y para que, cuando una pieza
salga mal, se sepa qué se pidió exactamente. **Qué no es.** No dice DÓNDE va cada pieza: eso es el
banco de composición, que nace en H S.4 con la plaza base delante.

---

## 0 · Cómo se usa, y es lo único que hay que leer antes de pedir una pieza

1. Se copia el **bloque maestro** (§1) tal cual.
2. Se le añade el **bloque de familia** que toque (§3).
3. Se le añade el **encargo concreto** de la pieza.
4. Se pinta **dentro de la lámina** y se recorta por resta (§2) si la familia sale por ese método; si no —el logotipo de
   H S.3-bis, los ambientes de sala y las familias que se pintan fuera de la plaza—, la familia declara por cuál sale.
5. **Se anota la fila** en `PU_registro_de_procedencia.md` — con el prompt LITERAL, no resumido —
   antes de dar la pieza por buena. Sin fila, la pieza no entra (§13.5).

---

## 1 · El bloque maestro

> Ilustración pictórica de una ciudad universitaria europea de principios del siglo XVII (1600–1650).
> Estilo de pintura al óleo con empaste visible, pincelada suave y contornos no delineados; aspecto de
> lámina de juego de gestión histórica europeo, cálido y habitado, no fotorrealista y no caricaturesco.
> Paleta cálida y limitada: ámbar, terracota, ocres, maderas profundas, pergamino y dorados apagados;
> sin colores saturados modernos, sin neón, sin azules fríos dominantes.
> Luz de tarde baja y lateral, sombras largas y suaves, atmósfera con polvo en suspensión.
> Perspectiva de tres cuartos ligeramente elevada, línea de horizonte alta, punto de vista de quien
> mira la plaza desde un balcón bajo.
> Sin texto, sin letras, sin números, sin cartelas, sin firmas y sin marcas de agua.
> Sin personas en primer plano reconocibles; figuras solo como siluetas pequeñas de escala.
> Sin anacronismos: nada eléctrico, nada de cristal plano grande, nada de vehículos.

**Por qué cada línea está ahí, para que nadie la afloje sin saber lo que suelta.** La pincelada y el
óleo son §11 —«ilustrado y cálido, pictórico»—. La paleta es §11 literal. La luz baja es lo que da
volumen a un módulo recortado sobre un fondo que no es el suyo. La perspectiva alta es lo que permite
que dieciséis edificios convivan sin taparse. **La prohibición de texto no es estética: es
funcional** — el juego escribe los nombres en su propia placa (`plate()`), y una lámina con letras
pintadas diría dos veces lo mismo y en dos idiomas tipográficos distintos.

---

## 2 · El método de la resta [§11 · DECIDIDO en H S.1]

Cada pieza se pinta **dentro de la plaza**, sobre la lámina entera, en su sitio y a su escala, y se
recorta después **por resta contra la misma lámina sin ella**. Con eso la perspectiva, la luz, la
escala y la técnica dejan de ser un encargo que hay que describir y pasan a ser una **consecuencia**
de dónde se pintó la pieza.

Las cifras que lo decidieron, y son de repintado —cuánto de la lámina cambia fuera de la pieza que se
pedía—: **10,4 %** por el método de la resta, frente al **45,8 %** y al **93,6 %** de las otras dos
vías que se probaron. Un edificio de una sesión anterior salió con **0,2 %**, que es el suelo
práctico del método.

**El porcentaje de repintado va en el registro y no en el banco**, y el motivo está en §13.5: se mide
entre dos imágenes en producción y no hay build que sondear, de modo que una aserción sobre él
tendría que fiarse de un número tecleado.

**Las excepciones, declaradas — y en H S.7 dejan de ser una rareza:** el logotipo de H S.3-bis **no pasa por la resta**
—es una ilustración de pantalla de apertura y no hay lámina dentro de la que pintarlo— y **los dieciséis ambientes tampoco**,
porque un interior no se pinta dentro de la plaza ni se recorta contra ella. Con dieciocho piezas más fuera que dentro,
§13.5 recoge en H S.7 lo que ya era cierto: **la resta es UN método de la fase y no EL método**, y cada familia declara por
cuál sale. Lo que no cambia es el porqué: donde la resta se puede usar, se usa, porque es lo que convierte la perspectiva,
la luz y la escala en una consecuencia y no en un encargo escrito con palabras.

### 2.1 · El corte de fondo, que es el método de la marca [H S.3-bis · H579]

**Las piezas se entregan con el fondo CORTADO, no recortado, y con el LIENZO INTACTO.** Son dos cosas
distintas y las dos van medidas.

**Por qué cortado y no recortado.** La lámina traía reborde blanco dentro del fichero —medido sobre el
original de 1792 × 2400: **4,52 % de píxeles casi blancos**, y **27 px a la izquierda, 13 a la derecha,
35 arriba y 0 abajo** en el centro de cada cara—. **Recortar en rectángulo no valía**, porque las
esquinas del libro son redondeadas y comidas y el blanco habría quedado en las cuatro.

**La receta, exacta:** inundación desde los cuatro bordes con `lum>200 && sat<46` —donde `lum` es el
máximo de los tres canales y `sat` la diferencia entre el máximo y el mínimo—, **erosión de 2 px**
sobre la máscara opaca y **pluma gaussiana σ 0,8** sobre el alfa. Retira el **6,24 %**. Un primer corte
más suave (`lum>224 && sat<26`) **dejaba halo**, y no era sólo blanco: era la **sombra fría** que el
modelo pintó bajo el libro.

**Y el lienzo NO se recorta, y el motivo es medido:** recortar a la caja útil —(22, 28) → (1773, 2381),
o sea 1752 × 2354— **movería las tres regiones de la animación un 1,2 %**, y conservar el lienzo de
1792 × 2400 **cuesta 2.468 bytes** (789.492 frente a 787.024). Se conserva.

**El formato es WebP con alfa a q90**, y la cifra se eligió midiendo y no a ojo: PSNR sobre la banda de
la plaza con el recorte que usa la animación — q82 37,24 dB · q86 38,52 · **q90 40,50** · q94 42,97.

---

## 3 · Los bloques de familia

Uno por familia del inventario de §11. El de cada familia se escribió **en la sesión que la produjo y
no antes** (§16: «un criterio escrito sin la pieza delante es un deseo»). **Estado final de la Fase H (H S.17):** todas las familias están hechas; la tabla dice en qué sesión y en qué versión, y el registro de procedencia (191 filas) es la fuente de cada pieza. La última
columna dice la sesión que produjo cada familia.

| Familia | Piezas | Bloque de familia |
|---|---|---|
| Módulos construibles de la plaza | 12 | **HECHOS en H S.4 (v0.134.0)**, los doce con su sombra como pieza aparte (H S.7): cada uno se distingue de los demás a la vista por su silueta, no solo por su color; recortados de la lámina de la plaza | H S.4 |
| Edificios públicos | 4 | **HECHOS en H S.4 (v0.134.0)** · la Asamblea, la Lonja, la Taberna y el Colegio, recortados de la misma lámina, con la lámina de fondo de la plaza | H S.4 |
| Ambientes de sala | **16** | **HECHAS · son DIECISÉIS y no cuatro, y son 18 ficheros porque el Colegio usa tres tiras.** Se entra en las dieciséis salas —doce construibles y cuatro públicos—, no sólo en los cuatro públicos, de modo que «una por edificio público» contaba mal desde H S.1. El ambiente es un MARCO ENVOLVENTE de 120 px arriba, 120 abajo y 26 a los lados, y no una cabecera; es ADORNO y no estado, de modo que no retrata lo que el jugador acaba de decidir; y no puede contradecir al edificio de la plaza, que manda forma, material, altura y si está abierto o cerrado | H S.7 |
| Obra en curso | 1 | **HECHA en H S.4** · el andamio, **común a las doce**: no tiene rasgos de ningún edificio concreto | H S.4 |
| Retratos | **18** | **HECHAS · son DIECIOCHO y no seis** (§11): **seis personas por tres edades cada una, 38 · 60 · 76**, una edad por época del arco. Tondo de 512 con alfa, y el aro de color se dibuja en SVG por encima. El emblema se retira —a 46 px medía 8 px— y el nombre accesible pasa al **ordinal**, que es lo único que no describe a nadie (§2.6). §2.2 sigue mandando: el retrato está **desacoplado del tratamiento** y ninguna pieza puede volver a atarlos. Es la única pieza de la fase que **no es adorno sino ESTADO**: sigue a la época | H S.9 |
| Iconos de recurso | 8 | **HECHOS en H S.10 (v0.141.0)** · los materiales, el oro, los estudiantes, el aforo, el atractivo y el claustro, pintados y no en SVG, en dos tallas (26 px en la barra y 16 en el teléfono), normalizados por ÁREA y no por alto; viven **dentro** del fichero de juego | H S.10 |
| Iconos de puerta y de tarjeta | 4 | **HECHOS en H S.10** · el libro (Cuentas), la brújula (Tu visión), el Colegio (Estado) y el cofrecillo (Para tus adentros); dentro del fichero de juego, dos tallas | H S.10 |
| Marcas de tiempo y de mando | 8 | **HECHAS en H S.10-bis** · son OCHO y no seis: los cuatro mandos del reloj (Pausa, ×1, ×5, Próximo año) y los cuatro de la cabecera (Guardar, Sonido, Crónica, Guía), cada uno en su tono oscuro y su tono claro derivado; la hoja del año no lleva marca. Dentro del fichero de juego | H S.10-bis |
| Superficies | 4 | **HECHAS en H S.10-bis** · el papel sobre el que se juega, la fibra de la cédula, el reloj y la barra, el canto de pergamino quemado del panel de decisiones y el papel de su interior; cortadas de las láminas de la dirección sin generador. Son las únicas piezas que la hoja de estilo pide por `url()` y no por `assetURL` | H S.10-bis |
| Marca de ayuda | 1 | **HECHA en H S.12-bis** · el disco de lacre con la «i», en dos tallas, dentro del fichero de juego | H S.12-bis |
| Familias de sello | 3 | **HECHAS en H S.10** · lacre (decisión), mazo (obras disponibles) y campanilla (algo nuevo), dentro del cartel y a 30 px, más la campanilla de sala; el sello se estampa **al cometer una decisión, nunca como marca de coherencia** (§11, regla inviolable) | H S.10 |
| Lugares de fondo | 9 | **HECHOS en H S.8 (v0.138.0)** · son NUEVE y no catorce: tu mesa, el claustro, el patio, el umbral, el aula a media entrada, la calle, la comparecencia, el entierro y el renglón en blanco; de las 91 pantallas de decisión y de suceso sirven a 42; otras 9, las que ocurren en una sala pública, usan el ambiente de esa sala, y las 40 restantes, el de su propio edificio | H S.8 |
| La vida de la plaza | 27 | **HECHA en H S.12-quater (v0.150.0)** · la gente, los carros y la recua —24 cuerpos, cada uno con su sombra como pieza aparte— y la paloma en vuelo; con el árbol y las casas del frente, capas de la lámina recortadas en H S.4, son 27; se colocan con azar sembrado y algunas se mueven | H S.12-quater |
| Sonidos de evento | 11 | **HECHOS en H S.13 (v0.153.0)** · son ONCE y no nueve: los nueve de siempre, rehechos, y la frontera de época al cerrarse y al abrirse; siguen generados al vuelo, **sin un solo fichero**, con la regla del sonido de §11 delante | H S.13 |
| Música de fondo | 5 | **HECHAS en H S.14 (v0.154.0)** · cinco piezas instrumentales de unos tres minutos producidas por la dirección con Lyria 3 Pro, en `assets/audio/` (PU_fondo_1_pavana, _2_diferencias, _3_ricercar, _4_aire, _5_folia), que suenan en su orden y tras la quinta vuelve la primera, a 0,10 de volumen | H S.14 |
| Logotipo | **3** | **HECHAS** · son tres piezas y no una (§11): **lámina vertical** 1792 × 2400 → `assets/imagenes/` · **lockup horizontal** 1027 × 358 → **dentro** del fichero de juego, `data:` URI · **monograma de la tapa** 496 × 554 → `assets/imagenes/`, que sólo usa la animación | H S.3-bis |
| Icono del juego | 1 | **HECHA** · **se queda DENTRO del fichero de juego** y **es un RECORTE del logotipo, en PNG y no en SVG**: el redibujo en vector se justificaba para comprar legibilidad a tamaño pequeño y, medido, la perdía en los cinco tamaños probados, el de 16 px incluido | H S.3-bis |
| Sonido de entrada de la apertura | 1 | **HECHA en H S.14 (v0.154.0)** · «Gallarda del mediodía», 12,10 s, el corte K4 de una toma de Lyria 3 Pro, en `assets/audio/PU_entrada.mp3`; suena con el gesto de la portada en lugar del pase de página, y la duración de la animación vive en un solo sitio declarado (10.400 ms), de modo que la música termina con el fundido a negro | H S.14 |

---

## 4 · Las referencias

**Cómo se usa una referencia, y es la mitad que importa.** Se usa para fijar **luz, materia y
encuadre**, nunca para reproducir una obra. Una pieza que se reconozca como una obra existente no
entra, y el motivo no es de gusto: la licencia BY-NC-ND de §11 solo se sostiene sobre obra propia o
sobre obra cuya licencia la permita (§4.1).

| Referencia | Para qué sirve |
|---|---|
| Ciudad portuaria del norte de Europa, s. XVII, en pintura de género | la escala de la plaza y cómo se apilan los tejados |
| Interiores de gremio y de lonja pintados con luz de ventana alta | los dieciséis ambientes de sala |
| Retrato de tres cuartos con fondo neutro y luz lateral | los dieciocho retratos —seis personas, tres edades— |
| Grabado y sello de cera de cancillería | las tres familias de sello y la identidad de registro/ledger |
| Ilustración de juego de gestión histórica europeo | el registro general: cálido, habitado, legible a tamaño de módulo |

### 4.1 · La regla de abastecimiento [§11 · DECIDIDO en H S.1]

**Ninguna pieza entra en `assets/` si su licencia no permite lo que el juego promete.**

- **SIRVEN:** dominio público y **CC0**, siempre · **CC BY**, con atribución obligatoria en los
  créditos · **CC BY-NC** y **CC BY-NC-ND**, sin más.
- **NO SIRVE**, y el motivo es de aritmética y no de gusto: cualquier **Share-Alike** —CC BY-SA,
  CC BY-NC-SA— y cualquier **GPL**. Obligan a licenciar la obra derivada con la misma licencia, y esa
  obligación es incompatible con el ND. Una sola pieza Share-Alike dentro del paquete le quitaría al
  juego entero el ND. No es una preferencia entre dos licencias buenas: es que las dos no caben
  juntas, y **la que se va es la pieza**.

### 4.2 · Las herramientas

**Ceden derechos también en gratuito:** Gemini y Nano Banana («Google won't claim ownership») ·
DALL·E 3 dentro de ChatGPT («you own all Input and Output»).
**No sirven en gratuito, y sí al pagar:** Leonardo.ai, Suno, Stable Audio.

**Y la regla que sale de ahí, que es lo que hace útil la lista en vez de dejarla en un inventario que
caduca:** los asistentes generales de los laboratorios grandes conceden los derechos también en
gratuito —su negocio está en otro sitio—, y las plataformas creativas especializadas los retienen
precisamente en gratuito y los sueltan al pagar, porque ahí el derecho ES el producto. Una sesión que
evalúe una herramienta que hoy no está en esta lista **empieza por preguntarse de cuál de las dos
familias es**, y luego lee sus condiciones para confirmarlo o desmentirlo.

**Lo autoalojado está descartado POR MEDICIÓN y no por prejuicio** (§11): FLUX Schnell sobre una
Radeon RX 580 de 8 GB con backend Vulkan tarda unos catorce minutos por imagen de 1024 × 1024. Si el
hardware cambia, la medición cambia con él y el descarte se reabre.

**LAS CONDICIONES DE UNA HERRAMIENTA SE MIRAN ANTES DE SUBIR NADA** [regla nueva · H S.3-bis · H579].
La regla de abastecimiento se escribió pensando en GENERADORES, y **cubre igual a cualquier servicio
por el que pase un asset, aunque sólo lo procese**. **El caso que la estrena, con su medición y su
conclusión: Upscale.media.** Su cláusula 9.1 concede al servicio *«una licencia libre de derechos, mundial, no
exclusiva, sublicenciable y transferible»* sobre lo que se sube, y su cláusula 7.4 **prohíbe al usuario el uso
comercial de la salida**. **Lo segundo no estorba, y el motivo va escrito:** el juego se publica
**BY-NC-ND**, o sea sin uso comercial por nadie, de modo que la restricción y la licencia dicen lo
mismo. **Y consta que la imagen ya estaba subida cuando se miraron las condiciones**, que es
exactamente el defecto que la regla viene a impedir.

**Design NO entra en esta lista**, y consta por qué: es una herramienta de Claude, integrada, sin
términos propios. Lo decidió la dirección.

**TODO ENCARGO DE UNA PIEZA SE ENTREGA EN UN FICHERO, NUNCA SÓLO EN EL CUERPO DEL MENSAJE**
[regla nueva · H S.3-bis · H579, y la decide la dirección al leer la parada de la tanda 1]. El registro
exige el prompt LITERAL; **un prompt que sólo vive en la conversación es un prompt que la conversación
se lleva**, y entonces la fila no se puede escribir. El caso que la funda: el encargo del lockup
horizontal se entregó en el cuerpo de un mensaje, la conversación se compactó y se perdió, mientras que
los encargos C1, C2 y C3 —que estaban en fichero— sobrevivieron intactos y coinciden palabra por
palabra con los pasos 4, 5 y 6 de la cadena. Lo recuperó la dirección de su chat, que era el único
sitio donde seguía vivo.

### 4.3 · La marca de agua

Las piezas **que se usan enteras** —la plaza de fondo, las escenas de sala, los fondos de decisión y
**el logotipo**— son las únicas donde la chispa de Gemini importa. Sus dos salidas: **AI Ultra**, que
la quita, o **DALL·E 3**.

**LA COMPROBACIÓN SE RETIRA, y no porque se haya contestado** [H S.3-bis · H579, y la retira la
dirección]. Sigue **sin medirse** si DALL·E 3 deja marca visible, y escribir lo contrario sería el
verde sin control que §13.3 prohíbe. **Se retira porque la herramienta por la que pregunta no se ha
usado y no se prevé usar:** el logotipo y su emblema salieron de **Gemini (Nano Banana 2)** y el
monograma de la tapa de **Design**, de modo que la producción no pasó por ninguna de las dos ramas que
la pregunta contemplaba. **Y la puerta queda abierta con esas palabras:** si alguna vez se produce una
pieza con DALL·E 3, la comprobación vuelve a §16 con dueña.

**Lo que SÍ está medido, y es lo único que se puede escribir:**

> De las **17 generaciones de Gemini (Nano Banana 2)** que conserva la dirección, miradas **una a una
> en su esquina**, **ninguna trae marca visible**.

**Eso dice algo de Gemini y nada de DALL·E 3.** Y **no dice nada en absoluto de SynthID**, que es
imperceptible por diseño y no se puede medir mirando: si alguna vez importa, hará falta un detector y
no un ojo.

---

## 5 · El presupuesto de peso [§11 · estimación, no muro]

Código ≤ **2 MB** · imágenes ≤ **10 MB** · audio ≤ **25 MB** · paquete ≤ **40 MB**.

Esa línea es la de partida y se queda escrita tal cual, porque el banco la compara con la de §11 y las dos tienen que ser una sola. Los techos que la dirección movió después están en §11 con su forma —«EL TECHO DE ‹familia› SE MUEVE»—: el de imágenes de 10 a 25 MB (12-09-2026) y el de paquete de 40 a 45 MB (4-10-2026). Y desde H S.17 la **copia de un solo fichero** tiene techo propio en §11, **60 MiB**, con su cifra medida al nacer (54,42 MiB sobre la v0.156.0): no es una familia del paquete, es la forma de distribución que se deriva de él.

Es estimación a propósito: un muro obligaría a tirar una pieza buena por cien kilobytes. Lo que se
quiere de esta cifra es que **nadie llegue a la sesión de cierre con un paquete de trescientos megas
sin haberlo visto venir**. Por eso el banco afirma que **cada familia cabe en el suyo** y no el techo
total: un desbordamiento tiene que decir DÓNDE está mientras todavía es barato moverlo.

### El listón se mueve, y lo que el banco vigila es que moverlo sea una decisión [H S.3 · H576]

**No se sacrifica vistosidad por el peso en ningún caso** —decisión de la dirección, con sus
palabras—: los cuarenta megas son una aproximación y no una atadura, y si hay que subirlos para darle
calidad al juego, se suben.

**Lo que eso NO significa: que el rojo desaparezca.** El rojo no es el muro, es el aviso barato que el
párrafo de arriba pide. La secuencia es **rojo → parada → la dirección mueve el techo en §11 con su
cifra vieja, su cifra nueva y su motivo → verde**, y todo dentro de la misma sesión. Ninguna sesión
cierra en rojo por esto.

**Y las cuatro cifras de arriba son una COPIA.** Quien las decide es §11, y desde H576 el banco las
lee de allí en vez de tenerlas tecleadas dentro. Si las dos listas dejan de decir lo mismo, lo dice
`documento.el_presupuesto_de_peso_dice_lo_mismo_en_sus_dos_copias`: dos sitios donde vive una cifra es
lo que §13.1 llama un sitio donde pudrirse, y por eso la pareja lleva vigilante.

**Cómo se mueve un techo, y la forma es la que el banco lee:** un párrafo de §11 que empiece por
«EL TECHO DE ‹familia› SE MUEVE» y diga «de N MB a M MB», con su marca `[DECIDIDO` y su motivo
detrás. **Sin las dos cosas no mueve nada** — un techo movido sin decisión declarada y sin motivo
escrito es exactamente la deriva contra la que se escribe.

**Cómo sabe el banco de qué familia es un fichero, y va escrito porque no es una columna del
registro:** por su sitio dentro de `assets/`. `assets/imagenes/…` → imágenes · `assets/audio/…` →
audio · el fichero de juego → código · `assets/metodo/…` → método, que no es un asset. Las dos
primeras carpetas existen desde H S.3-bis (imágenes) y H S.14 (audio), y `assets/` tiene 146 ficheros: 137 de imágenes, 6 de audio y los tres de método —el registro de procedencia,
este prompt maestro y, desde H S.17, el programa de empaquetado `PU_empaqueta.py`, que produce las dos formas de
distribución y no se incrusta en la copia de un solo fichero—.

---

## 6 · Lo que ninguna de estas líneas puede decidir

**El juicio estético lo firma la dirección mirando** (§13.5), exactamente como §0.2 hace con la
prosa: la regla de G S.1 dice que la prosa se valida leyéndola y no por haber pasado el banco, y una
pieza de arte tiene el mismo flanco y con menos remedio.
