from Principal.juego import Juego

class Deportes(Juego):
    def __init__(self, nombre, cod, desarrollador, tamanyo_equipo):
        super().__init__(nombre, cod, desarrollador, tamanyo_equipo)

    def formatos_validos(self) -> list:
        return ['eliminacion_directa', 'round_robin']

    def permite_empate(self) -> bool:
        return True  # En deportes puede haber empate (fútbol, etc.)