# Eliminacion directa: si pierdes quedas eliminado

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
