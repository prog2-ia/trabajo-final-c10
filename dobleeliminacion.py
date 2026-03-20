#Doble eliminación(si te eliminas hay 'repesca')

import bracketeliminacion as b
import fase as f
import partida as p

class DobleEliminacion(b.BracketEliminacion):
    #Atributos
    def __init__(self, equipos):
        super().__init__(equipos)
        self._bracket_ganadores = []
        self._bracket_perdedores = []

    def generar_bracket(self):
        equipos = self._equipos.copy()
        fase_g = f.Fase(1)

        #Inicia la primera fase
        for i in range(0, len(equipos), 2):
            partida = p.Partida(equipos[i], equipos[i + 1])
            fase_g.partidas.append(partida)

        self._bracket_ganadores.append(fase_g)

    def procesar_fase(self):
        fase_actual = self._bracket_ganadores[-1]
        nueva_fase_g = f.Fase(fase_actual.numero + 1)
        nueva_fase_p = f.Fase(fase_actual.numero)

        for partida in fase_actual.partidas:
            ganador = partida.resultado.ganador() #Saca el resultado de la partida

            if ganador == 1:
                ganador_eq = partida.equipo1
                perdedor_eq = partida.equipo2
            else:
                ganador_eq = partida.equipo2
                perdedor_eq = partida.equipo1

            # Ganador sigue en winners
            nueva_fase_g.partidas.append(p.Partida(ganador_eq, None))

            # Perdedor baja a losers
            nueva_fase_p.partidas.append(p.Partida(perdedor_eq, None))

        self._bracket_ganadores.append(nueva_fase_g)
        self._bracket_perdedores.append(nueva_fase_p)

