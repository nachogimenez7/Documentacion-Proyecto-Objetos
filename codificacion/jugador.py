class Jugador:
    def __init__(self, id: int, nombre: str):
        self.__id: int = id
        self.__nombre: str = nombre

    def obtenerId(self) -> int:
        return self.__id

    def obtenerNombre(self) -> str:
        return self.__nombre