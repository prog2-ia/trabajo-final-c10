#Clase equipo eSports
class Equipo:
    #Atributos de clase:
    cont_equipos = 0  # Contador para ver cuantos equipos tenemos
    def __init__(self, nombre, region, ranking, juegos):
        self.nombre = nombre
        self.region = region
        self.ranking = ranking
        self.juegos = juegos #VA A SER UNA LISTA
        #Para el contador de equipos
        type(self).cont_equipos +=1
        self.codigo_equipo = type(self).cont_equipos
