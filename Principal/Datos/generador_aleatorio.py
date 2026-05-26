import pickle
import random
import os
from Principal.Entidades.equipo import Equipo
from Principal.Entidades.jugador import Jugador
from Principal.Errores.errores import JugadoresInsuficientesError, EquiposInsuficientesError
from Principal.Errores.manejo_errores import registrar_error

BASE_DIR = os.path.dirname(__file__)


class GeneradorAleatorio:
    def __init__(self, num_equipos: int, tamanyo_equipo: int):
        self.__num_equipos = num_equipos
        self.__tamanyo_equipo = tamanyo_equipo
        self.__jugadores_disponibles: list[Jugador] = []
        self.__equipos_disponibles: list[tuple[str, str]] = []
        self.__equipos_generados: list[Equipo] = []

        self.__cargar_datos()

    def __cargar_datos(self):
        # Cargamos la base de datos de jugadores desde el fichero binario
        with open(os.path.join(BASE_DIR, 'jugadores.pickle'), 'rb') as f:
            jugadores_raw = pickle.load(f)

        # Cargamos la base de datos de equipos desde el fichero binario
        with open(os.path.join(BASE_DIR, 'equipos.pickle'), 'rb') as f:
            equipos_raw = pickle.load(f)

        # Mezclamos aleatoriamente ambas listas para mayor variedad
        random.shuffle(jugadores_raw)
        random.shuffle(equipos_raw)

        # Convertimos los datos en objetos Jugador
        for nick, nombre, apellidos, edad, pais in jugadores_raw:
            self.__jugadores_disponibles.append(
                Jugador(nick, nombre, apellidos, edad, pais)
            )

        self.__equipos_disponibles = equipos_raw

    def generar(self) -> list:
        jugadores_necesarios = self.__num_equipos * self.__tamanyo_equipo

        # Controlar que haya suficientes jugadores en el fichero para cubrir todos los equipos
        # Controlar que haya suficientes equipos en el fichero
        try:
            if len(self.__jugadores_disponibles) < jugadores_necesarios:
                raise JugadoresInsuficientesError(
                    f"Se necesitan {jugadores_necesarios} jugadores pero solo hay "
                    f"{len(self.__jugadores_disponibles)} en la base de datos."
                )
            if len(self.__equipos_disponibles) < self.__num_equipos:
                raise EquiposInsuficientesError(
                    f"Se necesitan {self.__num_equipos} equipos pero solo hay "
                    f"{len(self.__equipos_disponibles)} en la base de datos."
                )
        except (JugadoresInsuficientesError, EquiposInsuficientesError) as e:
            registrar_error(e)
            return []

        # Seleccionamos aleatoriamente los equipos necesarios sin repetir
        equipos_seleccionados = random.sample(self.__equipos_disponibles, self.__num_equipos)

        for i, (nombre_eq, region) in enumerate(equipos_seleccionados):
            # Cogemos los jugadores necesarios sin repetir — los eliminamos de disponibles
            jugadores_equipo = self.__jugadores_disponibles[:self.__tamanyo_equipo]
            self.__jugadores_disponibles = self.__jugadores_disponibles[self.__tamanyo_equipo:]

            equipo = Equipo(nombre_eq, region, i + 1, jugadores_equipo)
            self.__equipos_generados.append(equipo)

        return self.__equipos_generados