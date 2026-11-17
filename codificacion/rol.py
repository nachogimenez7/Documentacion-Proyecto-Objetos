class Rol:

    def __init__(self, nombre: str, equipo: str):
        self.__nombre: str = nombre
        self.__equipo: str = equipo

    def obtenerNombreRol(self) -> str:
        return self.__nombre

    def obtenerEquipoRol(self) -> str:
        return self.__equipo