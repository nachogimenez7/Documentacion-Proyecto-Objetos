class Participacion:
    """Estado de un jugador dentro de una partida."""

    def __init__(self, jugador, rol):
        self.jugador = jugador
        self.rol = rol
        self.vivo = True
        self.restringido = False
        self.identidad_revelada = False
        self.victoria_individual = False

    def estaVivo(self):
        return self.vivo

    def eliminar(self):
        self.vivo = False

    def puedeVotar(self):
        return self.vivo and not self.restringido
