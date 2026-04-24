from Principal import juego as j


#

class Moba(j.Juego):
    def __init__(self, nombre, cod, desarrollador, tamanyo_equipo, num_lineas: int, tiene_jungla: bool, duracion: int):
        super().__init__(nombre, cod, desarrollador, tamanyo_equipo) # Heredamos los atributos del padre
        # Atributos específicos de un MOBA
        self.num_lineas = num_lineas
        self.tiene_jungla = tiene_jungla  # Boolea
        self.duracion = duracion # Tiempo estimado por partida
