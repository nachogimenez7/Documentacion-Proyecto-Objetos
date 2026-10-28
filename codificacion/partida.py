class Partida:
    """Reúne las participaciones y comprueba el resultado de la partida."""

    def __init__(self, participaciones):
        self.participaciones = participaciones
        self.ronda = 1
        self.fase = "Preparación"
        self.ganador = None

    def comprobarVictoria(self):
        pueblo_vivo = 0
        traidores_vivos = 0
        atacantes_vivos = 0

        for participacion in self.participaciones:
            if participacion.estaVivo():
                if participacion.rol.equipo == "Pueblo":
                    pueblo_vivo = pueblo_vivo + 1
                elif participacion.rol.equipo == "Traidores":
                    traidores_vivos = traidores_vivos + 1

                if participacion.rol.nombre == "Asesino" or participacion.rol.nombre == "Espía":
                    atacantes_vivos = atacantes_vivos + 1

        # Primero se revisa si el Pueblo ganó, aunque quede el Mercenario.
        if atacantes_vivos == 0:
            self.ganador = "Pueblo"
        elif traidores_vivos >= pueblo_vivo:
            self.ganador = "Traidores"
        else:
            self.ganador = None
        return self.ganador
