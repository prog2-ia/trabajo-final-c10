#Vamos a crear la clase jugador en la que le vamos a meter el nick y otros datos:

class Jugador:
    #Atributos de clase:
    cont_jug = 0 #Contador para ver cuantos jugadores tenemos
    #Atributos de instancia
    def __init__(self, nick, nombre, apellidos, edad, pais):
        self.nick = nick
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.pais = pais
        self.__victorias = 0
        self.__derrotas = 0
        type(self).cont_jug +=1
        self._codigo_jug = type(self).cont_jug
        self.__estatus = 'Don Nadie'

    #Metodo winrate(proporción victorias-derrotas)
    def winrate(self):
        if self.__derrotas==0:    #Evitamos dividir entre 0
            return 100
        else:
            return (self.__victorias/(self.__derrotas + self.__victorias))*100

    #Muestra el winrate
    def ficha_competitiva(self):
        wr=self.winrate()
        #Queremos que el WR influya en las probabilidades de ganar de cada equipo
        if wr>70:
            self.__estatus='favorito'
        else:
            self.__estatus='Don Nadie'

        #Print de la ficha competitiva
        print(f'EL jugador {self.nick}, con un winrate del {wr}% se le considera un {self.__estatus}')