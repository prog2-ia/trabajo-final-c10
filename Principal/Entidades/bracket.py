#Clase abstracta bracket
from Principal.Entidades.fase import Fase
from abc import ABC,abstractmethod

class Bracket(ABC):
    def __init__(self,equipos:list):
        self._equipos=equipos
        self._fases: list[Fase] = []

    @abstractmethod
    def gen_bracket(self):
        pass

    def mostrar_bracket(self):
        for r in self._fases:
            r.mostrar_partidas() #Llamada a la clase fase

