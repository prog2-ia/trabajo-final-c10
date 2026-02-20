#Trabajo eSports.py
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
        self.victorias = 0
        self.derrotas = 0
        type(self).cont_jug +=1
        self.codigo_jug = type(self).cont_jug

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

#Clase videojuego
class Juego:
    def __init__(self, nombre, cod, genero):
        self.nombre = nombre
        self.cod = cod
        self.genero = genero


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
