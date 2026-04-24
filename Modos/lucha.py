from Principal import juego as j


#
class Lucha(j.Juego):
    def __init__(self, nombre, cod, desarrollador, tamanyo_equipo, num_luchadores: int, perspectiva: str):
        super().__init__(nombre, cod, desarrollador, tamanyo_equipo)
        self.num_luchadores = num_luchadores # Cantidad de luchadores seleccionables
        self.perspectiva = perspectiva       # "2D", "3D"# , "2.5D"
