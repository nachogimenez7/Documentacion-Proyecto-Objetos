# Primera etapa de la codificación

Este ejemplo en Python crea los 12 participantes con roles fijos y comprueba si hay un equipo ganador. Sirve para estudiar las clases y sus relaciones; todavía no juega una partida completa.

## Ejecutar

Abrí una terminal en esta carpeta y escribí:

```text
python main.py
```

Se probó con Python 3.11 y no necesita bibliotecas adicionales. Los roles se muestran en pantalla solo para explicar el ejemplo: en una partida real son secretos.

## Cómo está organizado

- `jugador.py`: guarda la identidad del jugador.
- `rol.py`: guarda el nombre del rol y su equipo.
- `participacion.py`: une jugador y rol y registra su estado durante la partida.
- `partida.py`: reúne las participaciones y comprueba las victorias de Pueblo y Traidores.
- `main.py`: crea los doce participantes y muestra la situación inicial.

Para seguir, leer `Guia_para_programar_una_partida.md`: el próximo paso es implementar la votación y sus desempates. Las acciones nocturnas, la victoria individual del Bufón y el desarrollo completo quedan para etapas posteriores. Antes de cerrar esas reglas hay que definir los puntos pendientes que indica la guía.

## ¿Qué significa el paradigma de objetos?

Es una forma de organizar un programa mediante objetos que representan elementos del problema. Cada objeto reúne **datos** (atributos) y **acciones** (métodos). Una clase es el modelo con el que se crean los objetos; cada objeto creado es una instancia de esa clase.

Por ejemplo, `Jugador` es una clase. `Jugador(1, "Ana")` crea un objeto con un identificador y un nombre. Su método `obtenerNombre()` permite consultar ese nombre. `Rol` es otra clase: sus objetos guardan el nombre y el equipo del rol.

En el juego, una `Participacion` relaciona un objeto `Jugador` con un objeto `Rol` y guarda lo que le ocurre en esa partida, como estar vivo. Una `Partida` reúne varias participaciones y puede ejecutar `comprobarVictoria()`. Así, los objetos colaboran para resolver una tarea.

En este borrador se ven clases, objetos, atributos, métodos y relaciones entre objetos. No hace falta afirmar que ya hay herencia o polimorfismo: todavía no aparecen en esta implementación. `self` representa el objeto que está usando el método y `__init__` establece sus datos iniciales al crearlo.

## Comprobación sencilla

Al ejecutar `python main.py` deben aparecer doce participantes: ocho del Pueblo, tres Traidores y un Bufón neutral. Al comienzo debe indicar que todavía no hay ganador. Para explorar el código, seguí cómo `main.py` crea los objetos y cómo `Partida` consulta el estado de cada participación.
