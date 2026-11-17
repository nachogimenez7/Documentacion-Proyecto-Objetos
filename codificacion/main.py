from jugador import Jugador
from rol import Rol
from participacion import Participacion
from partida import Partida


# Creamos a los jugadores
jugador1 = Jugador(1, "Lucas")
jugador2 = Jugador(2, "Federico")
jugador3 = Jugador(3, "César")
jugador4 = Jugador(4, "Matías")
jugador5 = Jugador(5, "Ramiro")
jugador6 = Jugador(6, "Juan")
jugador7 = Jugador(7, "Elías")
jugador8 = Jugador(8, "Walter")


# Creamos los roles
rolAldeano = Rol("Aldeano", "Pueblo")
rolMedico = Rol("Médico", "Pueblo")
rolDetective = Rol("Detective", "Pueblo")
rolAsesino = Rol("Asesino", "Traidores")
rolMercenario = Rol("Mercenario", "Traidores")
rolBufon = Rol("Bufón", "Neutral")


# Unimos cada jugador con su rol
participacion1 = Participacion(jugador1, rolAldeano)
participacion2 = Participacion(jugador2, rolAldeano)
participacion3 = Participacion(jugador3, rolAldeano)
participacion4 = Participacion(jugador4, rolMedico)
participacion5 = Participacion(jugador5, rolDetective)
participacion6 = Participacion(jugador6, rolAsesino)
participacion7 = Participacion(jugador7, rolMercenario)
participacion8 = Participacion(jugador8, rolBufon)


# Creamos la partida y agregamos las participaciones
partida1 = Partida()

partida1.agregarParticipacion(participacion1)
partida1.agregarParticipacion(participacion2)
partida1.agregarParticipacion(participacion3)
partida1.agregarParticipacion(participacion4)
partida1.agregarParticipacion(participacion5)
partida1.agregarParticipacion(participacion6)
partida1.agregarParticipacion(participacion7)
partida1.agregarParticipacion(participacion8)


print("PARTICIPANTES DE LA PARTIDA")
partida1.mostrarParticipantes()

# El Asesino y el Médico eligen a Lucas.
partida1.resolverNoche(participacion1, participacion1)

# Los votos están preparados: cinco para Juan y tres para Federico.
votos = [participacion6, participacion6, participacion6,
         participacion6, participacion6, participacion2,
         participacion2, participacion2]
partida1.resolverVotacion(votos)
