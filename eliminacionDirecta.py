#Eliminacion directa(si pierdes te eliminas)

import bracketEliminacion as b

class EliminacionDirecta(b.BracketEliminacion):

    def generar_bracket(self):
        equipos=self.equipos.copy()
        fase=Fase(1)

        for i in range(0,len(equipos),2 ):
            partido = Partida( equipos[i],equipos[i+1])
            fase.partidos.append(partido)

    self.fases.append(fase)