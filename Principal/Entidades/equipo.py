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
        print(f"Ranking: {self.__ranking} | Región: {self.region}")

    def __str__(self):
        return f"{self.nombre} (Ranking: {self.__ranking} | Región: {self.region})"

    def __eq__(self, otro):
        # Dos equipos son iguales si tienen el mismo nombre
        if not isinstance(otro, Equipo):
            return False
        return self.nombre == otro.nombre

    def __hash__(self):
        return hash(self.nombre)

    def __lt__(self, otro):
        # Permite ordenar equipos por ranking (menor ranking = mejor posición)
        return self.__ranking < otro.__ranking

