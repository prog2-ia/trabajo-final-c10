from Principal.Entidades.juego import Juego
from Principal.Entidades.bracket import Bracket

class Torneo:
    def __init__(self, nombre: str, juego: Juego, bracket: Bracket):
        self.nombre = nombre
        self._juego = juego
        self._bracket = bracket

    @property
    def juego(self):
        return self._juego

    @property
    def bracket(self):
        return self._bracket

    def iniciar(self):
        self._bracket.gen_bracket()

    def mostrar_estado(self):
        print(f"\n===== TORNEO: {self.nombre} =====")
        print(f"Juego: {self._juego}")
        print(f"Formato: {type(self._bracket).__name__}")
        print()
        self._bracket.mostrar_bracket()