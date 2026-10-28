class Rol:
    """Rol asignado a un participante y equipo al que pertenece."""

    def __init__(self, nombre, equipo):
        self.nombre = nombre
        self.equipo = equipo

    def obtenerEquipo(self):
        return self.equipo
