#Clase abstracta bracket

from abc import ABC,abstractmethod

class Bracket(ABC):
    def __init__(self,equipos):
        self._equipos=equipos
        self._fases=[]

    @abstractmethod
    def gen_bracket(self):
        pass

    def mostrar_bracket(self):
        for r in self._fases:
            r.mostrar_partidos() #Llamada a la clase fase