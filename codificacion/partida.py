from participacion import Participacion


class Partida:

    def __init__(self):
        self.__participaciones: list[Participacion] = []

    def agregarParticipacion(self, participacion: Participacion):
        self.__participaciones.append(participacion)

    def mostrarParticipantes(self):
        for participacion in self.__participaciones:
            jugador = participacion.obtenerJugador()
            rol = participacion.obtenerRol()
            print(jugador.obtenerNombre(), "-", rol.obtenerNombreRol())

    def resolverNoche(self, victima: Participacion, protegido: Participacion):
        nombreVictima = victima.obtenerJugador().obtenerNombre()
        nombreProtegido = protegido.obtenerJugador().obtenerNombre()

        print("\nNOCHE")
        print("El Asesino eligió a", nombreVictima)
        print("El Médico protegió a", nombreProtegido)

        if victima == protegido:
            print(nombreVictima, "sigue con vida.")
        else:
            victima.eliminar()
            print(nombreVictima, "fue eliminado.")

    def resolverVotacion(self, votos: list[Participacion]):
        print("\nVOTACIÓN")
        mayorCantidad = 0
        masVotado = None
        empate = False

        for participante in self.__participaciones:
            cantidad = votos.count(participante)
            if cantidad > mayorCantidad:
                mayorCantidad = cantidad
                masVotado = participante
                empate = False
            elif cantidad > 0 and cantidad == mayorCantidad:
                empate = True

        if masVotado is None:
            print("No hubo votos.")
        elif empate:
            print("Hubo un empate; no se resuelve en este ejemplo.")
        else:
            masVotado.eliminar()
            print(masVotado.obtenerJugador().obtenerNombre(),
                  "fue expulsado con", mayorCantidad, "votos.")
