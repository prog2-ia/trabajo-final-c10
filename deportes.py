import juego as j
#
class Deporte(j.Juego):
    def __init__(self, nombre, cod, desarrollador, tamanyo_equipo, tipo_deporte, duracion_partida):
        super().__init__(nombre, cod, desarrollador, tamanyo_equipo)
        self.tipo_deporte = tipo_deporte   # Ej: "Fútbol", "Automovilismo", "Baloncesto"
        self.duracion_partida = duracion_partida