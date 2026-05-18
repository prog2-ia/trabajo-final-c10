from Principal.Entidades.juego import Juego

class Lucha(Juego):
    def __init__(self, nombre, cod, desarrollador, tamanyo_equipo):
        super().__init__(nombre, cod, desarrollador, tamanyo_equipo)

    def formatos_validos(self) -> list:
        return ['eliminacion_directa', 'doble_eliminacion']

    def permite_empate(self) -> bool:
        return False