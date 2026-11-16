# Progressus Universitas

**Un juego sobre el arte de decidir con criterio.**

Funda una universidad en 1600, ordena tus cinco criterios y gestiónala durante medio siglo. Al final el juego no te dice si lo hiciste bien: te dice si tus decisiones fueron coherentes con lo que declaraste.

Progressus Universitas es un juego serio gratuito para estudiantes universitarios, pensado para trabajar el juicio evaluativo. Se juega en el navegador, sin instalar nada y sin cuentas. No guarda nada en el navegador ni envía nada a ningún servidor: lo único que existe de tu partida es lo que tú descargas al final.

- **Jugar:** https://progressus-universitas.es (dirección oficial). Este repositorio es el respaldo público del juego y se sirve con GitHub Pages.
- **Vídeo de presentación (57 s):** https://www.youtube.com/watch?v=lHGK2Rl5tpo
- **Guía del juego** (para quien juega y para docentes) y **Documento de diseño** (por qué el juego es así y cómo se hizo): en la sección «Documentación» de la web.

## Qué hay en este repositorio

El paquete web del juego, tal cual se sirve en progressus-universitas.es, con una «release» por versión publicada. Cada release declara la huella SHA-256 del fichero del juego y de la copia de un solo fichero, para que quien lo descargue pueda comprobar que lo que juega es lo que se publicó.

```
index.html                  la web
juego/vX.Y.Z/               el juego de esa versión, con sus piezas en assets/
descargas/                  la copia de un solo fichero, para jugar sin conexión
```

Hasta que la web esté terminada, `index.html` es una portada mínima que lleva al juego, y `descargas/` llega con la primera release.

El registro de procedencia de las piezas generadas con inteligencia artificial viaja dentro del paquete, en `juego/vX.Y.Z/assets/metodo/`.

## Cómo citar

Gómez Ruiz, M. Á. (2026). *Progressus Universitas* (Versión 1.1.2) [Videojuego]. https://progressus-universitas.es

El fichero `CITATION.cff` lleva la cita en formato legible por máquina. GitHub la muestra en «Cite this repository». El DOI de Zenodo se añadirá aquí cuando exista.

## Autoría y licencia

Idea y dirección: Miguel Ángel Gómez Ruiz, Universidad de Cádiz, Grupo de Investigación EVALfor. Programación, interfaz, arte y textos: Claude (Anthropic), en coautoría con la dirección. Ilustración generada con Gemini «Nano Banana» (Google) y, en parte de las salas, con DALL·E 3 (OpenAI), sobre encargos de la dirección y de Claude, con ampliación de imagen con Upscale.media. Música producida por la dirección con Lyria 3 Pro (Google).

Licencia: [Creative Commons Reconocimiento-NoComercial-SinObraDerivada 4.0 Internacional](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.es) (CC BY-NC-ND 4.0). Puedes copiarlo y compartirlo tal cual, citando la autoría, sin uso comercial y sin obras derivadas. Las incidencias de este repositorio están abiertas para avisar de errores. Las bifurcaciones que GitHub permite no cambian la licencia.

---

*Progressus Universitas is a free serious game in Spanish for university students, designed to exercise evaluative judgement: declare your criteria, run a university from 1600 to 1650 and read, at the end, how coherent your decisions were with what you declared. Play at https://progressus-universitas.es.*
