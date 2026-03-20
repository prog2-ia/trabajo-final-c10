#Eliminacion directa(si pierdes te eliminas)

import bracketeliminacion as b
import fase as f
import partida as p

class EliminacionDirecta(b.BracketEliminacion):
    def generar_bracket(self):
        equipos=self._equipos.copy()
        num_fase=1
        fase=f.Fase(1)

        for i in range(0,len(equipos),2 ):
            partido = p.Partida( equipos[i],equipos[i+1])
            fase.partidas.append(partido)

        self._fases.append(fase)

    #Avanzar el torneo
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
        # Crear nueva fase
        nueva_fase = f.Fase(fase_actual.numero + 1)

        for i in range(0, len(ganadores), 2):
            if i+1 < len(ganadores):
                nueva_partida = p.Partida(ganadores[i], ganadores[i+1])
                nueva_fase.partidas.append(nueva_partida)

        self.fases.append(nueva_fase)