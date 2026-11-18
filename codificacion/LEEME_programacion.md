# Simulación de una ronda de Traidores

Esta demostración académica crea ocho participantes, muestra las elecciones preparadas del Asesino y el Médico, y resuelve una votación. Busca mostrar clases, objetos, atributos, métodos y relaciones.

## Ejecutar

Abrí una terminal en esta carpeta y ejecutá:

```bash
python3 main.py
```

En Windows también puede funcionar `py main.py` o `python main.py`, según cómo esté instalado Python. Se requiere Python 3.9 o posterior y no hacen falta bibliotecas adicionales.

## Archivos

- `jugador.py`: identidad del jugador.
- `rol.py`: nombre del rol y equipo.
- `participacion.py`: relaciona jugador y rol y guarda si está vivo.
- `partida.py`: guarda participaciones y resuelve la noche y la votación del ejemplo.
- `main.py`: crea los objetos y prepara las decisiones de la ronda.
- `GUIA_PARA_EXPONER.md`: explicación de cada archivo y sugerencias para la presentación.
- `EXPLICACION_LINEA_POR_LINEA.md`: explicación detallada del código, agrupando instrucciones repetidas.

Los roles se sortean al iniciar; las elecciones y votos están preparados; se muestran los roles solo para explicar el ejemplo. No se implementan todas las habilidades, la victoria final, la validación completa de acciones ni el desempate. `Guia_para_programar_una_partida.md` conserva una propuesta anterior de 12 participantes; la demostración actual usa ocho.
