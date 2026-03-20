#Partida del torneo

import resultado as r


class Partida:
    #Atirbutos
    def __init__(self, equipo1, equipo2):
        self._equipo1 = equipo1
        self._equipo2 = equipo2
        self.__resultado = None

    def registrar_resultado(self, puntos1, puntos2):
        self.resultado = r.Resultado(puntos1, puntos2)

    #Ver quien es el ganador de la partida
    def ganador(self):
        if self.resultado is None:
            return None
        g = self.resultado.ganador()
        if g == 1:
            return self.equipo1
        elif g == 2:
            return self.equipo2
        else:
            return None

    #Print quien juega contra quien
    def __str__(self):
        if self.resultado:
            return f"{self._equipo1.nombre} vs {self._equipo2.nombre} -> {self.resultado}"
        else:
            return f"{self._equipo1.nombre} vs {self._equipo2.nombre} (sin jugar)"