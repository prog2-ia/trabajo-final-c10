#Resultado de la partida
class Resultado:
    #Atributos
    def __init__(self, puntos1, puntos2):
        self.__puntos1 = puntos1
        self.__puntos2 = puntos2

    #Comprobar quien ha ganado o si han empatado
    def ganador(self):
        if self.__puntos1 > self.__puntos2:
            return 1
        elif self.__puntos2 > self.__puntos1:
            return 2
        else:
            return 0

    #Print del resultado
    def __str__(self):
        return f"{self.__puntos1} - {self.__puntos2}"