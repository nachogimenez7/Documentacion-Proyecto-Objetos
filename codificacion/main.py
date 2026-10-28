from jugador import Jugador
from rol import Rol
from participacion import Participacion
from partida import Partida


def crear_partida_ejemplo():
    # Los roles son fijos para poder seguir el ejemplo paso a paso.
    roles = [
        ("Aldeana", "Pueblo"), ("Aldeana", "Pueblo"),
        ("Aldeana", "Pueblo"), ("Aldeana", "Pueblo"),
        ("Aldeana", "Pueblo"), ("Detective", "Pueblo"),
        ("Médico", "Pueblo"), ("Alcalde", "Pueblo"),
        ("Asesino", "Traidores"), ("Espía", "Traidores"),
        ("Mercenario", "Traidores"), ("Bufón", "Neutral"),
    ]
    participaciones = []
    numero = 1

    for nombre_rol, equipo in roles:
        jugador = Jugador(numero, "Jugador " + str(numero))
        rol = Rol(nombre_rol, equipo)
        participacion = Participacion(jugador, rol)
        participaciones.append(participacion)
        numero = numero + 1

    return Partida(participaciones)


def main():
    partida = crear_partida_ejemplo()
    print("TRAIDORES - Ejemplo inicial de 12 jugadores")
    print("Los roles se muestran para explicar el ejemplo; en el juego son secretos.\n")

    for participacion in partida.participaciones:
        print(participacion.jugador.obtenerNombre(), "-", participacion.rol.nombre,
              "-", participacion.rol.obtenerEquipo())

    ganador = partida.comprobarVictoria()
    if ganador == None:
        print("\nTodavía no hay ganador.")
    else:
        print("\nGanador:", ganador)
    print("Esta primera etapa todavía no juega rondas ni procesa votaciones.")


if __name__ == "__main__":
    main()
