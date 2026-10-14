# TRAIDORES: guía para programar una partida

**Ignacio Giménez · 14 de octubre de 2026 · Borrador de trabajo**

## Objetivo

Representar en Python el funcionamiento de una partida de 12 participantes, para explicar clases, atributos, métodos y relaciones. El alumno desarrollará el código paso a paso, siguiendo el estilo del parcial de simuladores.

La primera versión mostrará resultados en la consola. Las decisiones de los participantes estarán preparadas en `main.py`. Cuentas, salas online, chat, conexión a Firebase y decisiones de IA quedan fuera de esta primera versión.

## Participantes y roles

Composición recomendada para 12 jugadores en Feudo de Hierro:

| Rol | Cantidad | Función |
|---|---:|---|
| Aldeana | 5 | Debatir y votar. |
| Detective | 1 | Investigar; el Espía aparece como inocente. |
| Médico | 1 | Proteger de la eliminación nocturna. Puede protegerse y repetir objetivo en noches consecutivas. |
| Alcalde | 1 | Revelarse durante el debate; desde entonces su voto vale doble y decide los empates. |
| Asesino | 1 | Elegir una víctima de noche. |
| Espía | 1 | Elegir una víctima junto al Asesino y engañar la investigación. |
| Mercenario | 1 | Impedir hablar y votar durante el día siguiente. No puede elegirse a sí mismo ni repetir objetivo en noches consecutivas; puede elegir compañeros Traidores. |
| Bufón | 1 | Ganar individualmente si lo expulsan por votación. |

Total: **8 del Pueblo, 3 Traidores y 1 Neutral**.

## Recorrido de la partida

1. Crear participantes y asignar roles.
2. Registrar las acciones de la noche. Si Asesino y Espía eligen víctimas distintas, sortear entre ambas; la protección del Médico puede evitar la muerte de la víctima elegida.
3. Resolver la noche y comprobar si hay ganador.
4. Pasar al debate; el Alcalde puede revelar su identidad.
5. Registrar votos y resolver la expulsión. Sin Alcalde revelado, repetir la votación solo entre los empatados; si empatan nuevamente, no expulsar a nadie. Con Alcalde revelado, él elige entre los empatados, aunque sean más de dos.
6. Comprobar la victoria y, si la partida continúa, comenzar otra ronda. El efecto del Mercenario corresponde únicamente al día afectado.

Solo los participantes vivos realizan acciones y votan; el afectado por el Mercenario tampoco vota ese día. Cada voto se registra una vez por votación, permitiendo un nuevo voto en el desempate.

## Victoria

- **Pueblo:** gana si no quedan Asesinos ni Espías vivos, aunque quede el Mercenario.
- **Traidores:** si todavía queda un Asesino o Espía, ganan al igualar o superar el número de participantes vivos del Pueblo. El Mercenario cuenta como Traidor; el Bufón no pertenece a ninguno de esos bandos.
- **Bufón:** obtiene su victoria individual si es expulsado por votación. La partida continúa y su victoria se conserva aparte del resultado final. Morir de noche no le da la victoria.

Comprobar primero la ausencia de Asesinos y Espías; después, la superioridad numérica de los Traidores.

## Clases iniciales propuestas

| Archivo | Atributos principales | Métodos para empezar |
|---|---|---|
| `jugador.py` | Identificador y nombre. | `obtenerNombre()` |
| `rol.py` | Nombre y equipo. | `obtenerEquipo()` |
| `participacion.py` | Jugador, rol, estado vivo, restricción del día, identidad revelada y victoria individual. | `estaVivo()`, `eliminar()`, `puedeVotar()` |
| `partida.py` | Participaciones, ronda, fase, acciones, votos y ganador. | `iniciar()`, `resolverNoche()`, `resolverVotacion()`, `comprobarVictoria()` |
| `main.py` | Crea los objetos y prepara las decisiones del ejemplo. | Llama a los métodos y muestra lo ocurrido. |

Jugador representa a la persona; Participacion guarda lo que le ocurre dentro de esta partida. Los atributos y métodos se ampliarán al incorporar cada habilidad.

## Por dónde arrancar

1. Crear Jugador y Rol; comprobar que muestran correctamente sus datos.
2. Crear Participacion; comprobar que alguien puede pasar de vivo a eliminado.
3. Crear Partida con las 12 participaciones; mostrar la composición y comprobar las condiciones de victoria.
4. Incorporar votación, empate y voto del Alcalde.
5. Incorporar las habilidades nocturnas y la victoria individual del Bufón.
6. Unir las fases en un ejemplo que avance hasta el final.

**Primera ronda de ejemplo:** el Detective investiga al Espía y obtiene una respuesta de inocencia; Asesino y Espía eligen a la misma Aldeana; el Médico protege a esa Aldeana y evita su muerte; el Mercenario afecta a otra Aldeana, que no vota ese día. En la votación se expulsa al Bufón: gana individualmente, pero la partida continúa.

Antes de resolver la noche, falta acordar el orden exacto de las habilidades y qué ocurre con la acción de un participante que muere esa misma noche. También falta definir los objetivos permitidos del voto, incluido si se puede votar a uno mismo. Estos detalles no impiden empezar por las primeras tres etapas.

Fuente de la composición y habilidades: https://www.traidores.me/. Reglas de ataque, protección, Mercenario, desempates y victoria del Bufón aclaradas por el autor del juego en este chat.
