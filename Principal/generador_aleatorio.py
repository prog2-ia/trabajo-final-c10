#Archivo para leer ficheros binarios como base de datos de jugadores y equipos. Asigna equipos aleatoriamente.
import pickle
import random
from Principal.equipo import Equipo
from Principal.jugador import Jugador


class GeneradorAleatorio:
    def __init__(self, num_equipos: int, tamanyo_equipo: int):
        self.__num_equipos = num_equipos
        self.__tamanyo_equipo = tamanyo_equipo
        self.__jugadores_disponibles = []
        self.__equipos_disponibles = []
        self.__equipos_generados = []

        self.__cargar_datos()


    def __cargar_datos(self):   #Metodo privado para que no se pueda cargar datos desde otro lado
        # Cargamos la base de datos de jugadores
        with open('jugadores.pickle', 'rb') as f:
            jugadores_raw = pickle.load(f)

        # Cargamos la base de datos de equipos
        with open('equipos.pickle', 'rb') as f:
            equipos_raw = pickle.load(f)

        # Mezclamos aleatoriamente ambas listas para mayor variedad
        random.shuffle(jugadores_raw)
        random.shuffle(equipos_raw)

        # Convertimos los datos en objetos Jugador
        for nick, nombre, apellidos, edad, pais in jugadores_raw:
            self.__jugadores_disponibles.append(
                Jugador(nick, nombre, apellidos, edad, pais)
            )

        # Guardamos los equipos como tuplas (nombre, region)
        self.__equipos_disponibles = equipos_raw

    def generar(self) -> list:
        equipos_seleccionados = random.sample(self.__equipos_disponibles, self.__num_equipos)

        for i, (nombre_eq, region) in enumerate(equipos_seleccionados):
            # Cogemos los jugadores necesarios sin repetir. Los eliminamos de disponibles
            jugadores_equipo = self.__jugadores_disponibles[:self.__tamanyo_equipo]
            self.__jugadores_disponibles = self.__jugadores_disponibles[self.__tamanyo_equipo:]

            equipo = Equipo(nombre_eq, region, i + 1, jugadores_equipo)
            self.__equipos_generados.append(equipo)

        return self.__equipos_generados