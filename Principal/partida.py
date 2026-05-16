#Partida del torneo
from Principal.resultado import Resultado

class Partida:
    def __init__(self, equipo1, equipo2):
        self._equipo1 = equipo1
        self._equipo2 = equipo2
        self._resultado = None

    @property
    def equipo1(self):
        return self._equipo1

    @property
    def equipo2(self):
        return self._equipo2

    @property
    def resultado(self):
        return self._resultado

    def registrar_resultado(self, puntos1: int, puntos2: int):
        self._resultado = Resultado(puntos1, puntos2)

    def ganador(self):
        if self._resultado is None:
            return None
        g = self._resultado.ganador()
        if g == 1:
            return self._equipo1
        elif g == 2:
            return self._equipo2
        else:
            return None

    def __str__(self):
        if self._resultado:
            return f"{self._equipo1.nombre} vs {self._equipo2.nombre} -> {self._resultado}"
        else:
            return f"{self._equipo1.nombre} vs {self._equipo2.nombre} (sin jugar)"