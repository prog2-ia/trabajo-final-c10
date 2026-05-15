# Archivo principal de ejecución

from Principal.torneo import Torneo
from Principal.equipo import Equipo
from Principal.jugador import Jugador
from Modos.battleroyale import BattleRoyale
from Modos.moba import Moba
from Modos.lucha import Lucha
from Modos.deportes import Deportes
from Modos.shooter import Shooter
from Eliminaciones.eliminaciondirecta import EliminacionDirecta
from Eliminaciones.dobleeliminacion import DobleEliminacion
from Eliminaciones.roundrobin import RoundRobin


def menu_juego():
    print("\nElija el género del juego para su torneo:")
    print("1.- Battle Royale")
    print("2.- Deportes")
    print("3.- Lucha")
    print("4.- MOBA")
    print("5.- Shooter")
    print("6.- Ver descripción de géneros")

    opciones = ['1', '2', '3', '4', '5']
    answ = input("Introduzca su opción: ")

    while answ not in opciones:
        if answ == '6':
            descrip_modos()
        else:
            print("Opción no válida.")
        answ = input("Introduzca su opción: ")

    if answ == '1':
        return BattleRoyale("Battle Royale Genérico", "BR01", "Varios", 4, 100, 30, ["Mapa1", "Mapa2"])
    elif answ == '2':
        return Deportes("Deportes Genérico", "D01", "Varios", 5)
    elif answ == '3':
        return Lucha("Lucha Genérico", "L01", "Varios", 1)
    elif answ == '4':
        return Moba("MOBA Genérico", "M01", "Varios", 5, 3, True, 40)
    elif answ == '5':
        return Shooter("Shooter Genérico", "S01", "Varios", 5)


def descrip_modos():
    print("\n----- DESCRIPCIÓN DE GÉNEROS eSPORTS -----\n")
    print("1.- Battle Royale")
    print("Muchos equipos compiten hasta que queda uno. Mapas grandes, zonas que se reducen.")
    print("Ejemplos: Fortnite, Apex Legends, PUBG.\n")
    print("2.- Deportes")
    print("Simulan competiciones deportivas reales. Pueden terminar en empate.")
    print("Ejemplos: EA Sports FC, NBA 2K, Rocket League.\n")
    print("3.- Lucha")
    print("Dos jugadores se enfrentan directamente. Gana quien reduzca la vida del rival.")
    print("Ejemplos: Street Fighter, Tekken, Mortal Kombat.\n")
    print("4.- MOBA")
    print("Dos equipos en un mapa con líneas. El objetivo es destruir la base enemiga.")
    print("Ejemplos: League of Legends, Dota 2, Smite.\n")
    print("5.- Shooter")
    print("Combate con armas de fuego. Requiere puntería y trabajo en equipo.")
    print("Ejemplos: Counter Strike, Valorant, Call of Duty.\n")


def menu_formato(formatos_validos: list) -> str:
    nombre_formato = {
        'eliminacion_directa': 'Eliminación Directa',
        'doble_eliminacion':   'Doble Eliminación',
        'round_robin':         'Round Robin (todos contra todos)'
    }

    print("\nFormatos disponibles para este género:")
    for i, f in enumerate(formatos_validos, 1):
        print(f"{i}.- {nombre_formato[f]}")

    opciones = [str(i) for i in range(1, len(formatos_validos) + 1)]
    answ = input("Elija el formato: ")
    while answ not in opciones:
        print("Opción no válida.")
        answ = input("Elija el formato: ")

    return formatos_validos[int(answ) - 1]


def crear_equipos(tamanyo_equipo: int) -> list:
    equipos = []
    num = int(input("\n¿Cuántos equipos participan? "))

    for i in range(num):
        nombre_eq = input(f"\nNombre del equipo {i + 1}: ")
        region = input("Región: ")
        jugadores = []
        print(f"  Introduce {tamanyo_equipo} jugador(es):")
        for j in range(tamanyo_equipo):
            nick = input(f"  Nick jugador {j + 1}: ")
            jugadores.append(Jugador(nick, nick, "", 18, "Desconocido"))
        eq = Equipo(nombre_eq, region, i + 1, jugadores)
        equipos.append(eq)

    return equipos


def crear_bracket(formato: str, equipos: list):
    if formato == 'eliminacion_directa':
        return EliminacionDirecta(equipos)
    elif formato == 'doble_eliminacion':
        return DobleEliminacion(equipos)
    elif formato == 'round_robin':
        return RoundRobin(equipos)

def nombre_ronda(num_fase: int, total_equipos: int, formato: str) -> str:
    # Devuelve el nombre legible de la ronda según la fase y el total de equipos
    if formato == 'round_robin':
        return f"Jornada {num_fase}"

    partidas_en_fase = total_equipos // (2 ** num_fase)
    nombres = {
        1:  "Final",
        2:  "Semifinal",
        4:  "Cuartos de Final",
        8:  "Round of 16",
        16: "Round of 32",
    }
    return nombres.get(partidas_en_fase, f"Ronda {num_fase}")


def mostrar_enfrentamiento(partida, num_fase: int, total_equipos: int, formato: str):
    # Muestra un enfrentamiento con el nombre de la ronda
    ronda = nombre_ronda(num_fase, total_equipos, formato)
    print(f"\n  [{ronda}] {partida.equipo1.nombre} vs {partida.equipo2.nombre}")


def pedir_resultado(partida):
    print(f"  Introduce el resultado:")

    """ Controlar que la entrada sea un número entero y no texto """
    puntos1 = int(input(f"    Puntos {partida.equipo1.nombre}: "))

    """ Controlar que la entrada sea un número entero y no texto """
    puntos2 = int(input(f"    Puntos {partida.equipo2.nombre}: "))

    """ Controlar empate si el juego no lo permite """
    partida.registrar_resultado(puntos1, puntos2)
    ganador = partida.ganador()
    print(f"  Ganador: {ganador.nombre}")


# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────

if __name__ == "__main__":
    print("===== GENERADOR DE TORNEOS eSPORTS =====")

    """ Controlar opción de menú inválida (no numérica o fuera de rango) """
    juego = menu_juego()
    print(f"\nJuego seleccionado: {juego}")

    """ Controlar opción de formato inválida """
    formato = menu_formato(juego.formatos_validos())

    """ Controlar que el número de equipos sea un entero y suficiente para el formato """
    """ Controlar que el número de equipos sea par en eliminación directa """
    equipos = crear_equipos(juego.tamanyo_equipo)

    """ Controlar que el tamaño del equipo coincida con el que impone el juego """
    bracket = crear_bracket(formato, equipos)

    """ Controlar nombre vacío """
    nombre_torneo = input("\nNombre del torneo: ")
    torneo = Torneo(nombre_torneo, juego, bracket)

    torneo.iniciar()
    torneo.mostrar_estado()

    total_equipos = len(equipos)

    # ─────────────────────────────────────────
    # BUCLE PRINCIPAL DE EJECUCIÓN DEL TORNEO
    # ─────────────────────────────────────────

    torneo_activo = True

    while torneo_activo:

        fase_actual = torneo.bracket._fases[-1]

        # Filtramos las partidas que aún no tienen resultado
        partidas_pendientes = [p for p in fase_actual.partidas if p.resultado is None]

        if not partidas_pendientes:
            # Fase completada — intentamos generar la siguiente

            if formato == 'round_robin':
                # En round robin no hay fases siguientes, el torneo termina
                torneo_activo = False
                continue

            ganadores = [p.ganador() for p in fase_actual.partidas]

            # Si solo queda un ganador el torneo ha terminado
            if len(ganadores) == 1:
                torneo_activo = False
                continue

            # Generamos la siguiente fase con los ganadores
            from Principal.fase import Fase
            from Principal.partida import Partida

            nueva_fase = Fase(fase_actual.numero + 1)
            for i in range(0, len(ganadores), 2):
                """ Controlar índice impar (número de ganadores impar) """
                if i + 1 < len(ganadores):
                    nueva_fase.partidas.append(Partida(ganadores[i], ganadores[i + 1]))

            torneo.bracket._fases.append(nueva_fase)
            print(f"\n{'='*45}")
            print(f"  NUEVA RONDA: {nombre_ronda(nueva_fase.numero, total_equipos, formato)}")
            print(f"{'='*45}")
            continue

        # Jugamos la siguiente partida pendiente
        partida = partidas_pendientes[0]
        mostrar_enfrentamiento(partida, fase_actual.numero, total_equipos, formato)

        """ Controlar puntuaciones negativas """
        """ Controlar empate si el juego no permite_empate() """
        pedir_resultado(partida)

        # Tras cada partida preguntamos si quiere ver el estado del torneo
        ver_estado = input("\n  ¿Ver estado del torneo? (s/n): ").strip().lower()
        if ver_estado == 's':
            torneo.mostrar_estado()

    # ─────────────────────────────────────────
    # FIN DEL TORNEO
    # ─────────────────────────────────────────

    print(f"\n{'='*45}")
    print("         TORNEO FINALIZADO")
    print(f"{'='*45}")

    if formato == 'round_robin':
        # En round robin mostramos la clasificación final
        """ Controlar que bracket sea instancia de RoundRobin antes de llamar a actualizar_tabla """
        torneo.bracket.actualizar_tabla()
        torneo.bracket.mostrar_clasificacion()
    else:
        # En eliminación directa hay un único ganador al final
        ultima_fase = torneo.bracket._fases[-1]
        """ Controlar que la última fase tenga exactamente una partida con resultado """
        campeon = ultima_fase.partidas[0].ganador()
        print(f"\n  CAMPEÓN: {campeon.nombre}")

    print(f"{'='*45}\n")