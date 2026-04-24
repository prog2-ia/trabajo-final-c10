# Clase bracket eliminacion-> se divide en directa y doble

from Principal import bracket as b


class BracketEliminacion(b.Bracket):
    def __init__(self,equipos):
        super().__init__(equipos)
        self._fase_actual:int = 0

    def avanzar_fase(self):
        self._fase_actual += 1

