# Doble eliminacion: un equipo necesita perder dos veces para quedar eliminado

from Eliminaciones.bracketeliminacion import BracketEliminacion
from Principal.Entidades.fase import Fase
from Principal.Entidades.partida import Partida


class DobleEliminacion(BracketEliminacion):
    def __init__(self, equipos):
        super().__init__(equipos)
        self._bracket_ganadores = []   # fases del bracket superior
        self._bracket_perdedores = []  # fases del bracket inferior

    def gen_bracket(self):
        # Generamos la primera fase del bracket de ganadores
        equipos = self._equipos.copy()
        fase_g = Fase(1)

        for i in range(0, len(equipos), 2):
            partida = Partida(equipos[i], equipos[i + 1])
            fase_g.partidas.append(partida)

        self._bracket_ganadores.append(fase_g)
        self._fases.append(fase_g)

    def procesar_fase(self):
        # Recoge los resultados de la última fase del bracket de ganadores,
        # manda a los ganadores a la siguiente fase del bracket de ganadores,
        # y a los perdedores al bracket de perdedores.

        fase_g_actual = self._bracket_ganadores[-1]
        ganadores = []
        nuevos_perdedores = []

        for partida in fase_g_actual.partidas:
            ganador = partida.ganador()
            if ganador == partida.equipo1:
                ganadores.append(partida.equipo1)
                nuevos_perdedores.append(partida.equipo2)
            else:
                ganadores.append(partida.equipo2)
                nuevos_perdedores.append(partida.equipo1)

        # Procesamos también el bracket de perdedores si ya tiene fases
        supervivientes_perdedores = []
        if self._bracket_perdedores:
            fase_p_actual = self._bracket_perdedores[-1]
            for partida in fase_p_actual.partidas:
                # El que gana aqui sigue vivo, el que pierde queda eliminado
                ganador = partida.ganador()
                if ganador == partida.equipo1:
                    supervivientes_perdedores.append(partida.equipo1)
                else:
                    supervivientes_perdedores.append(partida.equipo2)

        # Comprobamos si estamos en la gran final
        # (1 ganador en bracket de ganadores + 1 superviviente en bracket de perdedores)
        if len(ganadores) == 1 and len(supervivientes_perdedores) == 1:
            gran_final = Fase(fase_g_actual.numero + 1)
            gran_final.partidas.append(Partida(ganadores[0], supervivientes_perdedores[0]))
            self._fases.append(gran_final)
            return

        # Generamos la siguiente fase del bracket de ganadores
        if len(ganadores) > 1:
            nueva_fase_g = Fase(fase_g_actual.numero + 1)
            for i in range(0, len(ganadores), 2):
                if i + 1 < len(ganadores):
                    nueva_fase_g.partidas.append(Partida(ganadores[i], ganadores[i + 1]))
            self._bracket_ganadores.append(nueva_fase_g)
            self._fases.append(nueva_fase_g)

        # Generamos la siguiente fase del bracket de perdedores
        # mezclando supervivientes anteriores con los nuevos perdedores del bracket de ganadores
        todos_perdedores = supervivientes_perdedores + nuevos_perdedores
        if len(todos_perdedores) > 1:
            nueva_fase_p = Fase(len(self._bracket_perdedores) + 1)
            for i in range(0, len(todos_perdedores), 2):
                if i + 1 < len(todos_perdedores):
                    nueva_fase_p.partidas.append(Partida(todos_perdedores[i], todos_perdedores[i + 1]))
            self._bracket_perdedores.append(nueva_fase_p)
            self._fases.append(nueva_fase_p)

