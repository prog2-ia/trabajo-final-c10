from abc import ABC, abstractmethod

class Juego(ABC):
    def __init__(self, nombre: str, cod: int | str, desarrollador: str, tamanyo_equipo: int):
        self.nombre = nombre
        self._cod = cod
        self.desarrollador = desarrollador
        self.tamanyo_equipo = tamanyo_equipo

    @abstractmethod
    def formatos_validos(self) -> list:
        #Devuelve los formatos de bracket válidos para este género.
        pass

    @abstractmethod
    def permite_empate(self) -> bool:
        #Indica si el género permite empates en una partida.
        pass

    def __str__(self):
        return f"{self.nombre} ({type(self).__name__}) - Equipo: {self.tamanyo_equipo} jugadores"