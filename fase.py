#Fase del torneo)

class Fase:
    def __init__(self, numero):
        self.__numero = numero
        self.partidas = []

    def agregar_partida(self, partida):
        self.partidas.append(partida)

    #Ver si está completa la fase para poder avanzar en la siguiente
    def esta_completa(self):
        for p in self.partidas:
            if p.resultado is None:
                return False
        return True

    def mostrar_partidas(self):
        print(f"Fase {self.__numero}")
        for p in self.partidas:
            print(p)