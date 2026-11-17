# Traidores: explicación del código línea por línea

Esta guía corresponde a la demostración de ocho participantes. Las líneas vacías solo ayudan a ordenar el código. Las líneas que comienzan con `#` son comentarios para las personas: Python no las ejecuta.

## Antes de empezar: algunas palabras de Python

- `class`: define una clase, el molde para crear objetos.
- `def`: define un método o función.
- `__init__`: constructor; se ejecuta al crear un objeto.
- `self`: representa al objeto que está usando el método. Python lo proporciona al llamar al método sobre ese objeto.
- `=`: asigna un valor. `==`: compara dos valores.
- `return`: devuelve un valor a quien llamó el método.
- `True` y `False`: valores booleanos, verdadero y falso. `None`: ausencia de valor.
- `int`, `str` y `bool`: anotaciones que indican entero, texto y booleano. Ayudan a leer el código, pero Python no las obliga por sí solo.
- La sangría, los espacios al principio de una línea, indica qué instrucciones están dentro de una clase, método, `if` o `for`.
- `__nombre`: el doble guion bajo al inicio indica un atributo tratado como privado; Python cambia internamente su nombre. No es una barrera de seguridad absoluta.

## 1. jugador.py

```python
class Jugador:
```
Declara el molde `Jugador`. Cada objeto creado con esta clase representa a una persona.

```python
def __init__(self, id: int, nombre: str):
```
Declara el constructor. Recibe un identificador entero y un nombre de texto. Por ejemplo, `Jugador(1, "Lucas")` crea el jugador Lucas.

```python
self.__id: int = id
self.__nombre: str = nombre
```
Guarda los valores recibidos en dos atributos privados del objeto. En la primera línea, el `id` de la derecha es el valor recibido; `self.__id` es dónde lo guardamos.

```python
def obtenerId(self) -> int:
    return self.__id
```
Define un método para consultar el identificador. `-> int` indica que esperamos que devuelva un entero; `return` devuelve el valor.

```python
def obtenerNombre(self) -> str:
    return self.__nombre
```
Hace lo mismo para el nombre y devuelve un texto. El jugador no guarda aquí su rol ni si está vivo: esos datos se relacionan con una partida concreta mediante `Participacion`.

## 2. rol.py

```python
class Rol:
```
Define el molde de un rol, por ejemplo Médico o Asesino.

```python
def __init__(self, nombre: str, equipo: str):
    self.__nombre: str = nombre
    self.__equipo: str = equipo
```
Recibe y guarda el nombre del rol y su equipo. En `Rol("Médico", "Pueblo")`, el nombre es Médico y el equipo es Pueblo.

```python
def obtenerNombreRol(self) -> str:
    return self.__nombre

def obtenerEquipoRol(self) -> str:
    return self.__equipo
```
Estos métodos permiten consultar los dos atributos. `obtenerNombreRol()` devuelve el nombre del rol, no el del jugador. Los nombres distintos ayudan a no confundirlo con `Jugador.obtenerNombre()`.

## 3. participacion.py

```python
from jugador import Jugador
from rol import Rol
```
Importa las clases desde sus archivos para poder utilizarlas en este archivo.

```python
class Participacion:
```
Define el molde que relaciona un jugador con su rol en una partida y registra si está vivo.

```python
def __init__(self, jugador: Jugador, rol: Rol):
```
El constructor recibe un objeto `Jugador` y un objeto `Rol`. `Jugador` y `Rol` son clases; `jugador` y `rol` son los nombres de los parámetros que reciben los objetos.

```python
self.__jugador: Jugador = jugador
self.__rol: Rol = rol
self.__vivo: bool = True
```
Guarda el jugador y el rol completos, no solo sus nombres. También crea el estado `__vivo` como verdadero: el participante comienza vivo.

```python
def obtenerJugador(self) -> Jugador:
    return self.__jugador
```
Devuelve el objeto Jugador asociado. Con ese objeto podemos llamar, por ejemplo, a `obtenerNombre()`.

```python
def obtenerRol(self) -> Rol:
    return self.__rol
```
Devuelve el objeto Rol asociado. No devuelve directamente el texto «Médico»: devuelve el objeto que guarda ese dato.

```python
def estaVivo(self) -> bool:
    return self.__vivo
```
Devuelve `True` o `False`, según el estado de esta participación.

```python
def eliminar(self):
    self.__vivo = False
```
Cambia el estado a falso. El jugador y su participación siguen existiendo como objetos; lo que cambia es que quedó eliminado de la partida.

## 4. partida.py

```python
from participacion import Participacion
```
Importa la clase con la que va a trabajar la partida.

```python
class Partida:
    def __init__(self):
        self.__participaciones: list[Participacion] = []
```
Declara la clase y su constructor. Al crear una Partida se prepara una lista privada de participaciones. `[]` quiere decir que empieza vacía; `list[Participacion]` describe qué clase de objetos se espera guardar.

### Agregar y mostrar participantes

```python
def agregarParticipacion(self, participacion: Participacion):
    self.__participaciones.append(participacion)
```
Recibe una participación y la agrega a la lista. `append()` añade un elemento al final.

```python
def mostrarParticipantes(self):
    for participacion in self.__participaciones:
```
Define un método y recorre la lista. En cada vuelta, `participacion` es uno de los objetos guardados.

```python
jugador = participacion.obtenerJugador()
rol = participacion.obtenerRol()
```
Pide a esa participación sus dos objetos relacionados y los guarda en variables locales, para utilizarlos dentro del método.

```python
print(jugador.obtenerNombre(), "-", rol.obtenerNombreRol())
```
Muestra el nombre del jugador y el nombre de su rol. Se llama a los métodos de los objetos correspondientes. Por ejemplo: `Lucas - Aldeano`.

### Resolver la noche

```python
def resolverNoche(self, victima: Participacion, protegido: Participacion):
```
Recibe dos participaciones ya elegidas: la víctima del Asesino y la persona protegida por el Médico. No recibe a los actores que hicieron esas elecciones ni verifica sus roles; es un ejemplo preparado.

```python
nombreVictima = victima.obtenerJugador().obtenerNombre()
nombreProtegido = protegido.obtenerJugador().obtenerNombre()
```
Para cada participación, primero obtiene el objeto Jugador y después su nombre. Guarda los textos en variables para poder mostrarlos.

```python
print("\nNOCHE")
print("El Asesino eligió a", nombreVictima)
print("El Médico protegió a", nombreProtegido)
```
Muestra un título y las elecciones. `\n` agrega un salto de línea antes del título.

```python
if victima == protegido:
    print(nombreVictima, "sigue con vida.")
```
Pregunta si las dos variables hacen referencia a la misma participación. Si es así, la protección evita que llamemos a `eliminar()`.

```python
else:
    victima.eliminar()
    print(nombreVictima, "fue eliminado.")
```
Si son participaciones distintas, llama al método `eliminar()` de la víctima y muestra el resultado.

### Resolver la votación

```python
def resolverVotacion(self, votos: list[Participacion]):
    print("\nVOTACIÓN")
```
Recibe una lista cuyos elementos son las participaciones votadas y muestra el título. La lista está preparada en `main.py`: no registra quién emitió cada voto.

```python
mayorCantidad = 0
masVotado = None
empate = False
```
Prepara las variables para recorrer la votación: por ahora la mayor cantidad es cero, no hay un más votado y no se detectó empate.

```python
for participante in self.__participaciones:
    cantidad = votos.count(participante)
```
Recorre cada participación de la partida. `count(participante)` cuenta cuántas veces aparece ese objeto en la lista de votos. Esa cantidad es la cantidad de votos que recibió.

```python
if cantidad > mayorCantidad:
    mayorCantidad = cantidad
    masVotado = participante
    empate = False
```
Si el participante actual supera el máximo anterior, se guardan la nueva cantidad y la participación. También se vuelve a poner `empate` en falso: ahora existe un nuevo máximo.

```python
elif cantidad > 0 and cantidad == mayorCantidad:
    empate = True
```
`elif` significa «si no se cumplió la condición anterior, comprobar esta otra». Si alguien tiene la misma cantidad máxima y al menos un voto, se detecta empate. `and` exige que se cumplan las dos condiciones.

```python
if masVotado is None:
    print("No hubo votos.")
```
Si no se encontró a nadie con votos, se informa. `is None` comprueba que siga sin haber una participación seleccionada.

```python
elif empate:
    print("Hubo un empate; no se resuelve en este ejemplo.")
```
Si hay empate por el primer lugar, se informa. Esta versión no implementa una nueva votación.

```python
else:
    masVotado.eliminar()
    print(masVotado.obtenerJugador().obtenerNombre(),
          "fue expulsado con", mayorCantidad, "votos.")
```
Si hubo un único más votado, se elimina esa participación y se muestran su nombre y cantidad de votos. El `print` ocupa dos líneas por comodidad, pero es una sola instrucción.

### Ejemplo del conteo actual

La lista preparada tiene cinco referencias a la participación de Juan y tres a la de Federico. Al recorrer a Federico, `count()` devuelve 3; al recorrer a Juan, devuelve 5. Como 5 es mayor que 3, Juan pasa a ser el más votado y se lo expulsa.

## 5. main.py

```python
from jugador import Jugador
from rol import Rol
from participacion import Participacion
from partida import Partida
```
Importa las cuatro clases desde sus archivos. `main.py` prepara la demostración y llama a los métodos.

```python
jugador1 = Jugador(1, "Lucas")
```
Crea un objeto de la clase Jugador con identificador 1 y nombre Lucas. Las siguientes siete líneas hacen lo mismo para Federico, César, Matías, Ramiro, Juan, Elías y Walter, con sus propios números.

```python
rolAldeano = Rol("Aldeano", "Pueblo")
```
Crea un objeto de la clase Rol. Las siguientes líneas crean los roles Médico, Detective, Asesino, Mercenario y Bufón con sus equipos.

```python
participacion1 = Participacion(jugador1, rolAldeano)
```
Crea una participación que relaciona a Lucas con el rol Aldeano. Las demás líneas relacionan cada jugador con su rol. Lucas, Federico y César comparten `rolAldeano`, pero tienen participaciones distintas y por eso el estado vivo de cada uno es independiente.

```python
partida1 = Partida()
```
Crea un objeto Partida. Su constructor comienza con la lista de participaciones vacía.

```python
partida1.agregarParticipacion(participacion1)
```
Le pide a `partida1` que agregue esa participación. Las siete líneas siguientes agregan las demás.

```python
print("PARTICIPANTES DE LA PARTIDA")
partida1.mostrarParticipantes()
```
Muestra el título y llama al método que recorre y presenta la lista. Los roles se muestran para la demostración; en el juego real son secretos.

```python
partida1.resolverNoche(participacion1, participacion1)
```
Llama al método de la partida y le pasa las dos elecciones preparadas. Ambas son Lucas, así que la protección funciona. El programa muestra que el Asesino y el Médico eligieron a Lucas; no pregunta a los usuarios ni verifica la identidad de quienes eligen.

```python
votos = [participacion6, participacion6, participacion6,
         participacion6, participacion6, participacion2,
         participacion2, participacion2]
```
Crea una lista de ocho votos preparados: `participacion6` es Juan y aparece cinco veces; `participacion2` es Federico y aparece tres. Cada elemento indica un candidato votado, no quién votó.

```python
partida1.resolverVotacion(votos)
```
Entrega la lista al método que cuenta los votos y expulsa al único más votado: Juan.

## 6. Cómo explicarlo de corrido

«Primero tengo las clases Jugador y Rol, que representan la identidad y el rol. Después Participacion relaciona ambos objetos y guarda si el jugador está vivo. Partida tiene una lista de participaciones y métodos para recorrerla, resolver la noche y contar una votación. En main creo los objetos, los relaciono y preparo una ronda de ejemplo».

Para ejecutar, desde la carpeta `codificacion`, escribir `python3 main.py`. En Windows puede ser `py main.py` o `python main.py`, según la instalación.

La demostración no es una partida completa: no valida todas las acciones y votos, no implementa la segunda votación en empates, las habilidades del Detective, el Mercenario y el Bufón ni las condiciones de victoria final. No hay herencia ni polimorfismo implementados en este código.
