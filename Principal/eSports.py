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

'''
Error de elegir opcion mal
'''
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

'''
Error de verificar tamaño equipos
'''
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


# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────

if __name__ == "__main__":
    print("===== GENERADOR DE TORNEOS eSPORTS =====")

    # 1. Elegir género → instancia el objeto Juego concreto
    juego = menu_juego()
    print(f"\nJuego seleccionado: {juego}")

    # 2. El juego expone sus formatos válidos → el usuario elige entre ellos
    formato = menu_formato(juego.formatos_validos())

    # 3. Crear equipos respetando el tamaño que impone el juego
    equipos = crear_equipos(juego.tamanyo_equipo)

    # 4. Instanciar el bracket según el formato elegido
    bracket = crear_bracket(formato, equipos)

    # 5. Nombrar y crear el torneo (composición: Torneo tiene un Juego y un Bracket)
    nombre_torneo = input("\nNombre del torneo: ")
    torneo = Torneo(nombre_torneo, juego, bracket)

    # 6. Iniciar: el bracket genera las fases y partidas iniciales
    torneo.iniciar()

    # 7. Mostrar el estado inicial del torneo
    torneo.mostrar_estado()