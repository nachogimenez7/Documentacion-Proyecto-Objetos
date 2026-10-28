class Jugador:
    """Identidad del jugador, independiente de una partida concreta."""

    def __init__(self, identificador, nombre):
        self.identificador = identificador
        self.nombre = nombre

    def obtenerNombre(self):
        return self.nombre
