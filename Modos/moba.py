from Principal.juego import Juego

class Moba(Juego):
    def __init__(self, nombre, cod, desarrollador, tamanyo_equipo, num_lineas: int, tiene_jungla: bool, duracion: int):
        super().__init__(nombre, cod, desarrollador, tamanyo_equipo)
        self.num_lineas = num_lineas
        self.tiene_jungla = tiene_jungla
        self.duracion = duracion

    def formatos_validos(self) -> list:
        return ['eliminacion_directa', 'doble_eliminacion']

    def permite_empate(self) -> bool:
        return False