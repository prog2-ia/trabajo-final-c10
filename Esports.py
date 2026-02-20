#Trabajo eSports.py
#Vamos a crear la clase jugador en la que le vamos a meter el nick y otros datos:

class Jugador:
    #Atributos de instancia
    def __init__(self, nick, nombre, apellidos, edad, pais):
        self.nick = nick
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.pais = pais
        self.victorias = 0
        self.derrotas = 0

    #Metodo winrate(proporción victorias-derrotas)
    def winrate(self):
        if self.derrotas==0:    #Evitamos dividir entre 0
            return 100
        else:
            return (self.victorias/self.derrotas)*100

    #Muestra el winrate
    def ficha_competitiva(self):
        wr=self.winrate()
        if wr>70:
            self.estatus='favorito'
        else:
            self.estatus='Don Nadie'

        #Print de la ficha competitiva
        print(f'EL jugador {self.nick}, con un winrate del {wr}% se le considera un {self.estatus}')