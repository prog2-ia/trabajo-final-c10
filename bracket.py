#Clase abstracta bracket

from abc import ABC,abstractmethod

class Bracket(ABC):
    def __init__(self,equipos,fases=4):
        self.equipos=equipos
        self.fases=fases

    @abstractmethod
    def gen_bracket(self):
        pass

    def mostrar_bracket(self):
        for r in self.rondas:
            r.mostrar_partidos() #Llamada a la clase fases
