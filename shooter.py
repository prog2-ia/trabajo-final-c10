#Subclase shooter con herencia de juego
import juego as j
class Shooter(j.Juego):
    def __init__(self, nombre, cod, desarrollador, tamaño_equipo, rondas, dur_rondas, mapas):
        super().__init__(nombre, cod, desarrollador, tamaño_equipo) #Heredamos del padre
        self.rondas = rondas
        self.dur_rondas = dur_rondas
        self.mapas = mapas