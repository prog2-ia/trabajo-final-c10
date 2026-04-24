#Clase equipo eSports
class Equipo:
    #Atributos de clase:
    cont_equipos: int = 0  # Contador para ver cuantos equipos tenemos
    def __init__(self, nombre: str, region: str, ranking: int, juegos: list):
        self.nombre = nombre
        self.region = region
        self.__ranking = ranking #No se debe cambiar sin control
        self.juegos = juegos #VA A SER UNA LISTA
        #Para el contador de equipos
        type(self).cont_equipos +=1
        self._codigo_equipo: int = type(self).cont_equipos #Atributo protegido

    def muestra(self):
        print(self.__ranking)
        print(self.region)
