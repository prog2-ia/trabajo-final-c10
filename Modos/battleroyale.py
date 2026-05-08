from Principal.juego import Juego

class BattleRoyale(Juego):
    def __init__(self, nombre, cod, desarrollador, tamanyo_equipo, num_jugadores: int, tiempo_partida: int, mapas: list):
        super().__init__(nombre, cod, desarrollador, tamanyo_equipo)
        self.num_jugadores = num_jugadores
        self.tiempo_partida = tiempo_partida
        self.mapas = mapas

    def formatos_validos(self) -> list:
        return ['round_robin']  # Muchos equipos, todos se enfrentan

    def permite_empate(self) -> bool:
        return False