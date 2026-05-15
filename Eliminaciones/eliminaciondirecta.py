#Eliminacion directa(si pierdes te eliminas)

from Eliminaciones.bracketeliminacion import BracketEliminacion
from Principal.fase import Fase
from Principal.partida import Partida

class EliminacionDirecta(BracketEliminacion):
    def gen_bracket(self):
        equipos = self._equipos.copy()
        fase = Fase(1)

        for i in range(0, len(equipos), 2):
            partido = Partida(equipos[i], equipos[i + 1])
            fase.partidas.append(partido)

        self._fases.append(fase)

    def siguiente_fase(self):
        fase_actual = self._fases[-1]
        ganadores = []
        for partida in fase_actual.partidas:
            if partida.resultado is None:
                continue
            ganador = partida.resultado.ganador()
            if ganador == 1:
                ganadores.append(partida.equipo1)
            else:
                ganadores.append(partida.equipo2)

        nueva_fase = Fase(fase_actual.numero + 1)
        for i in range(0, len(ganadores), 2):
            if i + 1 < len(ganadores):
                nueva_fase.partidas.append(Partida(ganadores[i], ganadores[i + 1]))

        self._fases.append(nueva_fase)