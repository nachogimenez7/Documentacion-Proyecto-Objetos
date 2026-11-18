import random

from jugador import Jugador
from rol import Rol
from participacion import Participacion
from partida import Partida


# Creamos a los jugadores.
jugador1 = Jugador(1, "Lucas")
jugador2 = Jugador(2, "Federico")
jugador3 = Jugador(3, "César")
jugador4 = Jugador(4, "Matías")
jugador5 = Jugador(5, "Ramiro")
jugador6 = Jugador(6, "Juan")
jugador7 = Jugador(7, "Elías")
jugador8 = Jugador(8, "Walter")

# Preparamos los ocho roles y mezclamos su orden.
rolAldeano = Rol("Aldeano", "Pueblo")
roles = [rolAldeano, rolAldeano, rolAldeano,
         Rol("Médico", "Pueblo"), Rol("Detective", "Pueblo"),
         Rol("Asesino", "Traidores"), Rol("Mercenario", "Traidores"),
         Rol("Bufón", "Neutral")]
random.shuffle(roles)

# Asignamos a cada jugador un rol de la lista mezclada.
participacion1 = Participacion(jugador1, roles[0])
participacion2 = Participacion(jugador2, roles[1])
participacion3 = Participacion(jugador3, roles[2])
participacion4 = Participacion(jugador4, roles[3])
participacion5 = Participacion(jugador5, roles[4])
participacion6 = Participacion(jugador6, roles[5])
participacion7 = Participacion(jugador7, roles[6])
participacion8 = Participacion(jugador8, roles[7])

participaciones = [participacion1, participacion2, participacion3, participacion4,
                   participacion5, participacion6, participacion7, participacion8]

# Agregamos las participaciones y buscamos los roles para el ejemplo.
partida1 = Partida()
for participacion in participaciones:
    partida1.agregarParticipacion(participacion)
    nombreRol = participacion.obtenerRol().obtenerNombreRol()
    if nombreRol == "Asesino":
        asesino = participacion
    elif nombreRol == "Médico":
        medico = participacion
    elif nombreRol == "Aldeano":
        aldeano = participacion

print("PARTICIPANTES DE LA PARTIDA")
partida1.mostrarParticipantes()
print("\nAsesino:", asesino.obtenerJugador().obtenerNombre())
print("Médico:", medico.obtenerJugador().obtenerNombre())

# En esta demostración el Asesino y el Médico eligen al mismo Aldeano.
partida1.resolverNoche(aldeano, aldeano)

# Votos preparados: cinco para el Asesino y tres para un Aldeano.
votos = [asesino, asesino, asesino, asesino, asesino,
         aldeano, aldeano, aldeano]
partida1.resolverVotacion(votos)

if asesino.estaVivo():
    print(asesino.obtenerJugador().obtenerNombre(), "sigue en la partida.")
else:
    print(asesino.obtenerJugador().obtenerNombre(), "está eliminado.")
