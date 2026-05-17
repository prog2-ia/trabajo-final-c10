#Fase del torneo)

class Fase:
    def __init__(self, numero: int):
        self.__numero = numero
        self.partidas: list = []

    @property
    def numero(self):
        return self.__numero

    def agregar_partida(self, partida):
        self.partidas.append(partida)

    def esta_completa(self):
        for p in self.partidas:
            if p.resultado is None:
                return False
        return True

    def mostrar_partidas(self):
        print(f"--- Fase {self.__numero} ---")
        for p in self.partidas:
            print(" ", p)

    def __len__(self):
        # Devuelve el número de partidas de la fase
        return len(self.partidas)

