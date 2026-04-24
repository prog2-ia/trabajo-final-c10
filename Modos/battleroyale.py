#Clase BattelRoyale
#
from Principal import juego as j


class BattleRoyale(j.Juego):
    def __init__(self, nombre, cod, desarrollador, tamanyo_equipo, num_jugadores: int, tiempo_partida: int, mapas: list):
        super().__init__(nombre, cod, desarrollador, tamanyo_equipo) #Heredamos del padre
        self.num_jugadores = num_jugadores
        self.tiempo_partida = tiempo_partida
        self.mapas = mapas
