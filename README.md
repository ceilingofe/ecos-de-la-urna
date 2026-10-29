# Ecos de la urna

Una historia interactiva sobre quién vota en México, hecha con los **Conteos Censales de Participación Ciudadana (CCPC) 2009–2024 del INE**. Proyecto para el hackatón *Hackea la participación* del INE, Reto 3: Storytelling con datos.

Entras con tu año de nacimiento, tu estado y tu sexo. Papelito, un ajolote que es funcionario de casilla, te acompaña durante un domingo de elección en tu barrio: cuánta gente de tu edad votó, la fila por edad con sus lugares vacíos, el salón donde la mitad decide por todos, quince años de listas nominales, a dónde va el presupuesto que aprueba la Cámara y, al final, tu propia boleta para 2027.

- **La historia:** `index.html`
- **El tablero didáctico "Ecos en datos":** `datos.html`

## Cómo verlo

Es un sitio estático: no necesita servidor propio ni compilación. Para probarlo en tu computadora:

```
python3 -m http.server 8000
```

y abre `http://localhost:8000`. Abrir el archivo directo con doble clic no carga las voces, porque el navegador bloquea los audios locales.

## Qué hay aquí

| Ruta | Qué es |
|---|---|
| `index.html` | Ecos de la urna: escenas 3D con Three.js r128, música sintetizada en el navegador, subtítulos, voz de Papelito, versión en texto, panel de accesibilidad y capa en maya. Al final graba tu reel vertical "Tu eco". |
| `datos.html` | Tablero con la curva por edad, seis elecciones, mujeres y hombres, mosaico de estados, secciones urbanas, mixtas y rurales, simulador de participación joven, presupuesto 2026 y glosario. |
| `voz/` | Clips MP3 de la voz de Papelito y de los personajes de las boletas. |
| `herramientas/agg.py` | Agrega los CSV de los CCPC por estado, municipio, tipo de sección, sexo y edad. Uso: `python3 agg.py 2024 datos_procesados/agg_2024.csv` con los ZIP de datos abiertos en `datos/`. |
| `herramientas/tablero-prep.py` | Calcula, a partir de esos agregados, las cifras que usan la historia y el tablero. |

## Datos

- Conteos Censales de Participación Ciudadana 2009, 2012, 2015, 2018, 2021 y 2024, datos abiertos del INE (DECEyEC). Participación = votantes / (votantes + no votantes).
- Presupuesto de Egresos de la Federación 2026 y notas del CEFP de la Cámara de Diputados para la escena del gasto.
- Los ZIP originales no se incluyen por su tamaño; se descargan del portal de datos abiertos del INE.

## Créditos

- Voz de Papelito y voces de los personajes generadas con IA (ElevenLabs).
- Three.js r128 (licencia MIT), servido desde cdnjs. Fuentes de Google Fonts: Bungee, Atkinson Hyperlegible, Caveat, Permanent Marker, DM Serif Display y Fredoka.
- Las personas, razones y barrios de la historia son ilustrativos; las cifras vienen de los datos del INE.
