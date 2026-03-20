#Round Robin(Todos contra todos)

from bracket import Bracket
import fase as f
import partida as p


class RoundRobin(Bracket):
    #Atirbutos
    def __init__(self, equipos):
        super().__init__(equipos)
        self.__tabla = {}  # equipo -> puntos

    def generar_bracket(self):
        equipos = self._equipos.copy()

        # Inicializamos la tabla
        for eq in equipos:
            self.__tabla[eq] = 0
        num_fase = 1

        # Todos contra todos
        for i in range(len(equipos)):
            for j in range(i + 1, len(equipos)):
                fase = f.Fase(num_fase)
                partida = p.Partida(equipos[i], equipos[j])
                fase.partidas.append(partida)
                self._fases.append(fase)
                num_fase += 1

    def actualizar_tabla(self):
        for fase in self._fases:
            for partida in fase.partidas:
                if partida.resultado is None:
                    continue
                ganador = partida.resultado.ganador()
                #Asignación de puntos en la tabla
                if ganador == 1:
                    self.__tabla[partida.equipo1] += 3
                elif ganador == 2:
                    self.__tabla[partida.equipo2] += 3
                else:
                    # empate
                    self.__tabla[partida.equipo1] += 1
                    self.__tabla[partida.equipo2] += 1

    def mostrar_clasificacion(self):
        # Ordenamos por puntos
        clasificacion = sorted(self.__tabla.items(), key=lambda x: x[1], reverse=True)

        print("CLASIFICACIÓN:")
        for eq, puntos in clasificacion:
            print(eq.nombre, "-", puntos, "puntos")