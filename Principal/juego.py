#Trabajo eSports.py

#Clase videojuego
class Juego:
    def __init__(self, nombre: str, cod: int|str, desarrollador: str, tamanyo_equipo: int):
        self.nombre = nombre
        self._cod = cod #Atributo protegido
        self.desarrollador = desarrollador
        self.tamanyo_equipo = tamanyo_equipo

