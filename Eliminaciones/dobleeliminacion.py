#Doble eliminación(si te eliminas hay 'repesca')

from Eliminaciones.bracketeliminacion import BracketEliminacion
from Principal.fase import Fase
from Principal.partida import Partida

class DobleEliminacion(BracketEliminacion):
    def __init__(self, equipos):
        super().__init__(equipos)
        self._bracket_ganadores = []
        self._bracket_perdedores = []

    def gen_bracket(self):
        equipos = self._equipos.copy()
        fase_g = Fase(1)

        for i in range(0, len(equipos), 2):
            partida = Partida(equipos[i], equipos[i + 1])
            fase_g.partidas.append(partida)

        self._bracket_ganadores.append(fase_g)
        self._fases.append(fase_g)

    def procesar_fase(self):
        fase_actual = self._bracket_ganadores[-1]
        nueva_fase_g = Fase(fase_actual.numero + 1)
        nueva_fase_p = Fase(fase_actual.numero)

        for partida in fase_actual.partidas:
            ganador = partida.resultado.ganador()
            if ganador == 1:
                ganador_eq = partida.equipo1
                perdedor_eq = partida.equipo2
            else:
                ganador_eq = partida.equipo2
                perdedor_eq = partida.equipo1

            nueva_fase_g.partidas.append(Partida(ganador_eq, None))
            nueva_fase_p.partidas.append(Partida(perdedor_eq, None))

        self._bracket_ganadores.append(nueva_fase_g)
        self._bracket_perdedores.append(nueva_fase_p)
        self._fases.append(nueva_fase_g)


