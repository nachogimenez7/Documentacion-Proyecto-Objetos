# Guía para explicar la demostración de Traidores

## 1. Cómo empezar la presentación

«Mi proyecto se basa en Traidores, un juego de deducción social. Para mostrar el paradigma de objetos preparé una demostración de una ronda en Python. Creo ocho participantes, sorteo sus roles, represento una elección nocturna del Asesino y del Médico y cuento una votación. Las decisiones están preparadas en el código».

La demostración es parcial: no es toda la aplicación móvil ni una partida completa. No implementa las habilidades del Detective, el Mercenario y el Bufón, condiciones de victoria, entrada interactiva ni un desempate. Los roles se muestran en pantalla para la explicación, aunque en el juego son secretos.

## 2. Cómo ejecutar

Abrir una terminal en la carpeta `codificacion` y ejecutar:

```bash
python3 main.py
```

En Windows puede utilizarse `py main.py` o `python main.py`, según la instalación. Se necesita Python 3.9 o posterior; no hay bibliotecas adicionales. En VS Code también se puede abrir `main.py` y usar el botón para ejecutar Python.

El resultado presenta a los ocho participantes con roles sorteados. El Asesino y el Médico eligen al mismo Aldeano, que sobrevive. Luego el Asesino recibe cinco votos frente a tres para ese Aldeano y es expulsado. Los nombres cambian en cada ejecución.

## 3. ¿Qué es programar con objetos?

Una **clase** es un modelo que define qué datos y comportamientos tendrán sus objetos. Un **objeto** es una instancia concreta creada a partir de una clase. Por ejemplo, `Jugador` es la clase y `jugador1 = Jugador(1, "Lucas")` crea un objeto.

Los **atributos** son los datos que guarda el objeto, como `__nombre` en Jugador. Los **métodos** son operaciones definidas en la clase, como `obtenerNombre()` o `eliminar()`. `__init__` es el constructor: se ejecuta al crear el objeto y establece sus datos iniciales. `self` representa el objeto que recibe la llamada.

Los nombres con doble guion bajo, como `__nombre`, representan atributos privados por convención y Python modifica internamente sus nombres. Los consultamos mediante métodos. Esto ayuda a explicar la encapsulación, aunque no es una barrera de seguridad absoluta.

Las clases colaboran: `Partida` reúne objetos `Participacion`; cada participación conoce a un `Jugador` y a un `Rol`. Es una relación entre objetos. Esta implementación no incluye herencia ni polimorfismo: no es necesario afirmar que los utiliza.

## 4. Qué decir de cada archivo

### `jugador.py`

«La clase Jugador representa la identidad de una persona. Guarda un identificador y un nombre. Sus métodos `obtenerId()` y `obtenerNombre()` permiten consultar esos datos».

El rol y el estado vivo no están aquí porque pueden cambiar entre partidas. Están asociados a la participación.

### `rol.py`

«La clase Rol guarda el nombre del rol y el equipo. Tiene métodos para consultarlos. Por ejemplo, `Rol("Médico", "Pueblo")` crea un objeto que representa ese rol».

En el ejemplo, los tres Aldeanos comparten el mismo objeto Rol, porque describe el mismo tipo de rol; cada jugador tiene una participación distinta y por eso su estado es independiente.

### `participacion.py`

«Una Participacion relaciona un jugador con su rol en una partida. También guarda si está vivo. El constructor recibe los objetos Jugador y Rol y comienza con `__vivo = True`».

`obtenerJugador()` y `obtenerRol()` devuelven esos objetos; `estaVivo()` consulta el estado y `eliminar()` lo cambia a `False`. `Jugador` y `Rol` son tipos de objetos, no textos: por eso se importan las clases.

### `partida.py`

«Partida guarda una lista de participaciones y coordina la demostración».

- `agregarParticipacion()` recibe una participación y la agrega a la lista con `append()`.
- `mostrarParticipantes()` usa `for` para recorrer la lista y pedir a cada participación su jugador y su rol.
- `resolverNoche(victima, protegido)` muestra las elecciones preparadas. Si son la misma participación, evita la eliminación; si son distintas, llama a `eliminar()` sobre la víctima.
- `resolverVotacion(votos)` recorre las participaciones. Para cada una, `votos.count(participante)` cuenta sus apariciones en la lista. Guarda la mayor cantidad, detecta empates y, si hay un único más votado, lo elimina. Si no hay votos o hay empate, muestra el mensaje correspondiente; no implementa una segunda votación.

Las elecciones y los votos se proporcionan preparados. El programa no valida quién hizo cada acción o voto ni si todos los objetivos son válidos: es una demostración acotada.

### `main.py`

«Es el punto de inicio del ejemplo. Importa las clases, crea los jugadores y roles, mezcla la lista de roles con `random.shuffle(roles)`, relaciona cada jugador con un rol mediante una participación y agrega las ocho participaciones a la partida. Después llama a los métodos que muestran la noche y la votación».

En la lista `votos`, cada elemento es el candidato elegido: el Asesino aparece cinco veces y el Aldeano elegido tres. La lista no registra la identidad de cada votante.

## 5. Orden sugerido para mostrar el código

1. Ejecutar `main.py` y explicar qué se ve en pantalla.
2. Mostrar `jugador.py` y `rol.py` como modelos simples con atributos y métodos.
3. Mostrar `participacion.py` y explicar cómo une un jugador con un rol y mantiene su estado para esa partida.
4. Mostrar `partida.py`: la lista, la comparación de la noche y el conteo con `count()`.
5. Volver a `main.py` y señalar dónde se crean los objetos y se los relaciona.
6. Aclarar el alcance de la demostración y que el resto de las reglas queda fuera de esta versión.

## 6. Preguntas posibles

**¿Por qué separar Jugador y Participacion?** El jugador mantiene su identidad; la participación guarda su rol y estado en una partida concreta. La misma persona podría tener otro rol en otra partida.

**¿Cómo se evita la muerte?** La partida compara las dos participaciones elegidas. Si son la misma, no llama a `eliminar()`.

**¿Cómo se sabe quién fue el más votado?** Se cuenta cuántas veces aparece cada participación en la lista `votos` y se conserva la mayor cantidad. Si hay empate se informa, sin resolverlo.

**¿Es un juego completo?** No. Las decisiones están preparadas, solo se muestra una ronda y varias habilidades quedan sin implementar. La aplicación Android es otro alcance.
