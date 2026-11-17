from jugador import Jugador
from rol import Rol


class Participacion:

    def __init__(self, jugador: Jugador, rol: Rol):
        self.__jugador: Jugador = jugador
        self.__rol: Rol = rol
        self.__vivo: bool = True

    def obtenerJugador(self) -> Jugador:
        return self.__jugador

    def obtenerRol(self) -> Rol:
        return self.__rol

    def estaVivo(self) -> bool:
        return self.__vivo

    def eliminar(self):
        self.__vivo = False