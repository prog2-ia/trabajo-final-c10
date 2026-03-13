#Clase bracket eliminacion-> se divide en directa y doble

import bracket as b

class BracketEliminacion(b.Bracket):

    def __init__(self,equipos):
        super().__init__(equipos)
        self.fase_actual=0

    def avanzar_fase(self):
        self.fase_actual+=1
        