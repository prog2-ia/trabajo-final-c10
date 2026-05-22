# Archivo principal de ejecución

from Principal.Entidades.torneo import Torneo
from Principal.Entidades.equipo import Equipo
from Principal.Entidades.jugador import Jugador
from Modos.battleroyale import BattleRoyale
from Modos.moba import Moba
from Modos.lucha import Lucha
from Modos.deportes import Deportes
from Modos.shooter import Shooter
from Eliminaciones.eliminaciondirecta import EliminacionDirecta
from Eliminaciones.dobleeliminacion import DobleEliminacion
from Eliminaciones.roundrobin import RoundRobin
from Principal.Datos.generador_aleatorio import GeneradorAleatorio
from Principal.Entidades.fase import Fase
from Principal.Entidades.partida import Partida

from Principal.Errores.errores import OpcionInvalidaError
from Principal.Errores.errores import EquiposInsuficientesError
from Principal.Errores.errores import EquiposImpares
from Principal.Errores.errores import NombreVacioError
from Principal.Errores.errores import PuntuacionNegativaError
from Principal.Errores.errores import EmpateNoPermitidoError
from Principal.Errores.errores import IndiceImparError
from Principal.Errores.errores import BracketTipoError
from Principal.Errores.errores import FaseFinInvalidaError
from Principal.Errores.manejo_errores import registrar_error

MIN_EQUIPOS_FORMATO = {'eliminacion_directa': 2, 'doble_eliminacion': 4, 'round_robin': 2}


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
            try:
                raise OpcionInvalidaError(f"'{answ}' no es una opción válida. Elija un número del 1 al 5.")
            except OpcionInvalidaError as e:
                registrar_error(e)
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
        try:
            raise OpcionInvalidaError(f"'{answ}' no es una opción válida. Elija un número del 1 al {len(formatos_validos)}.")
        except OpcionInvalidaError as e:
            registrar_error(e)
        answ = input("Elija el formato: ")

    return formatos_validos[int(answ) - 1]


def crear_equipos(tamanyo_equipo: int, formato: str) -> list:

    # Controlar que el número de equipos sea un entero y no texto
    while True:
        try:
            num = int(input("\n¿Cuántos equipos participan? "))
        except ValueError as e:
            registrar_error(e)
            continue

        # Controlar número de equipos insuficiente para el formato
        try:
            if num < MIN_EQUIPOS_FORMATO.get(formato, 2):
                raise EquiposInsuficientesError(
                    f"El formato '{formato}' requiere al menos {MIN_EQUIPOS_FORMATO.get(formato, 2)} equipos. Se introdujeron {num}.")
        except EquiposInsuficientesError as e:
            registrar_error(e)
            continue

        # Controlar número de equipos impar en eliminación directa
        try:
            if formato == 'eliminacion_directa' and num % 2 != 0:
                raise EquiposImpares(
                    f"La eliminación directa requiere un número par de equipos. Se introdujeron {num}.")
        except EquiposImpares as e:
            registrar_error(e)
            continue

        break

    print("\n¿Cómo quieres crear los equipos?")
    print("1.- Introducirlos manualmente")
    print("2.- Generarlos aleatoriamente")

    # Controlar opción inválida en el menú de creación de equipos
    opcion = input("Elige una opción: ").strip()
    while opcion not in ['1', '2']:
        try:
            raise OpcionInvalidaError(f"'{opcion}' no es una opción válida. Introduzca 1 o 2.")
        except OpcionInvalidaError as e:
            registrar_error(e)
        opcion = input("Elige una opción: ").strip()

    if opcion == '1':
        # Introducción manual
        equipos = []
        for i in range(num):
            nombre_eq = input(f"\nNombre del equipo {i + 1}: ")
            region = input("Región: ")
            jugadores = []
            print(f"  Introduce {tamanyo_equipo} jugador(es):")
            for j in range(tamanyo_equipo):
                nick = input(f"  Nick jugador {j + 1}: ")
                jugadores.append(Jugador(nick, nick, "", 18, "Desconocido"))
            equipos.append(Equipo(nombre_eq, region, i + 1, jugadores))
        return equipos

    else:
        # Generación aleatoria
        generador = GeneradorAleatorio(num, tamanyo_equipo)
        equipos = generador.generar()
        print("\nEquipos generados:")
        for eq in equipos:
            print(f"  {eq.nombre} ({eq.region})")
            for j in eq.juegos:
                print(f"    - {j.nick}")
        return equipos


def crear_bracket(formato: str, equipos: list):
    if formato == 'eliminacion_directa':
        return EliminacionDirecta(equipos)
    elif formato == 'doble_eliminacion':
        return DobleEliminacion(equipos)
    elif formato == 'round_robin':
        return RoundRobin(equipos)


def nombre_ronda(fase_actual, formato: str) -> str:
    # Devuelve el nombre legible de la ronda según las partidas reales de la fase
    if formato == 'round_robin':
        return f"Jornada {fase_actual.numero}"

    num_partidas = len(fase_actual.partidas)
    nombres = {
        1:  "Final",
        2:  "Semifinal",
        4:  "Cuartos de Final",
        8:  "Round of 16",
        16: "Round of 32",
    }
    return nombres.get(num_partidas, f"Ronda {fase_actual.numero}")


def mostrar_enfrentamiento(partida, fase_actual, formato: str):
    # Muestra un enfrentamiento con el nombre de la ronda
    ronda = nombre_ronda(fase_actual, formato)
    print(f"\n  [{ronda}] {partida.equipo1.nombre} vs {partida.equipo2.nombre}")


def pedir_resultado(partida, juego):
    print(f"  Introduce el resultado:")

    # Controlar que la entrada sea un número entero y no texto
    while True:
        try:
            puntos1 = int(input(f"    Puntos {partida.equipo1.nombre}: "))
            if puntos1 < 0:
                raise PuntuacionNegativaError(f"La puntuación no puede ser negativa ({puntos1}).")
            break
        except (ValueError, PuntuacionNegativaError) as e:
            registrar_error(e)

    # Controlar que la entrada sea un número entero y no texto
    while True:
        try:
            puntos2 = int(input(f"    Puntos {partida.equipo2.nombre}: "))
            if puntos2 < 0:
                raise PuntuacionNegativaError(f"La puntuación no puede ser negativa ({puntos2}).")
            break
        except (ValueError, PuntuacionNegativaError) as e:
            registrar_error(e)

    # Controlar empate si el juego no lo permite
    while puntos1 == puntos2 and not juego.permite_empate():
        try:
            raise EmpateNoPermitidoError(f"El juego '{juego.nombre}' no permite empates. Introduce un resultado sin empate.")
        except EmpateNoPermitidoError as e:
            registrar_error(e)
        while True:
            try:
                puntos1 = int(input(f"    Puntos {partida.equipo1.nombre}: "))
                break
            except ValueError as e:
                registrar_error(e)
        while True:
            try:
                puntos2 = int(input(f"    Puntos {partida.equipo2.nombre}: "))
                break
            except ValueError as e:
                registrar_error(e)

    partida.registrar_resultado(puntos1, puntos2)
    ganador = partida.ganador()

    if ganador is None:
        print("  Empate registrado.")
    else:
        print(f"  Ganador: {ganador.nombre}")


# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────

if __name__ == "__main__":
    print("===== GENERADOR DE TORNEOS eSPORTS =====")

    # Controlar opción de menú inválida (no numérica o fuera de rango)
    juego = menu_juego()
    print(f"\nJuego seleccionado: {juego}")

    # Controlar opción de formato inválida
    formato = menu_formato(juego.formatos_validos())

    # Controlar que el número de equipos sea un entero y suficiente para el formato
    # Controlar que el número de equipos sea par en eliminación directa
    equipos = crear_equipos(juego.tamanyo_equipo, formato)

    bracket = crear_bracket(formato, equipos)

    # Controlar nombre vacío
    while True:
        nombre_torneo = input("\nNombre del torneo: ").strip()
        try:
            if not nombre_torneo:
                raise NombreVacioError("El nombre del torneo no puede estar vacío.")
            break
        except NombreVacioError as e:
            registrar_error(e)
    torneo = Torneo(nombre_torneo, juego, bracket)

    torneo.iniciar()
    torneo.mostrar_estado()

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

            if formato == 'doble_eliminacion':
                # Si la última fase es la gran final y está completa, el torneo termina
                if fase_actual.esta_completa() and len(fase_actual.partidas) == 1:
                    torneo_activo = False
                    continue

                # Comprobamos si todas las fases activas están completas antes de procesar
                fases_incompletas = [f for f in torneo.bracket._fases if not f.esta_completa()]
                if fases_incompletas:
                    fase_actual = fases_incompletas[0]
                    partidas_pendientes = [p for p in fase_actual.partidas if p.resultado is None]
                    partida = partidas_pendientes[0]
                    mostrar_enfrentamiento(partida, fase_actual, formato)
                    pedir_resultado(partida, juego)
                    ver_estado = input("\n  ¿Ver estado del torneo? (s/n): ").strip().lower()
                    if ver_estado == 's':
                        torneo.mostrar_estado()
                    continue

                # Todas las fases completas — procesamos la siguiente
                torneo.bracket.procesar_fase()

                nueva_fase = torneo.bracket._fases[-1]
                if len(nueva_fase.partidas) == 1:
                    print(f"\n{'=' * 45}")
                    print(f"  GRAN FINAL")
                    print(f"{'=' * 45}")
                else:
                    print(f"\n{'=' * 45}")
                    print(f"  NUEVA RONDA: {nombre_ronda(nueva_fase, formato)}")
                    print(f"{'=' * 45}")
                continue

                # Todas las fases activas están completas — procesamos la siguiente
                torneo.bracket.procesar_fase()

                # Comprobamos si la última fase generada es la gran final (1 sola partida)
                nueva_fase = torneo.bracket._fases[-1]
                if len(nueva_fase.partidas) == 1 and nueva_fase.partidas[0].equipo1 and nueva_fase.partidas[0].equipo2:
                    print(f"\n{'=' * 45}")
                    print(f"  GRAN FINAL")
                    print(f"{'=' * 45}")
                else:
                    print(f"\n{'=' * 45}")
                    print(f"  NUEVA RONDA: {nombre_ronda(nueva_fase, formato)}")
                    print(f"{'=' * 45}")
                continue

            ganadores = [p.ganador() for p in fase_actual.partidas]

            # Si solo queda un ganador el torneo ha terminado
            if len(ganadores) == 1:
                if formato == 'doble_eliminacion':
                    # En doble eliminación hay que procesar la gran final primero
                    torneo.bracket.procesar_fase()
                    nueva_fase = torneo.bracket._fases[-1]
                    print(f"\n{'=' * 45}")
                    print(f"  GRAN FINAL")
                    print(f"{'=' * 45}")
                else:
                    torneo_activo = False
                continue

            # Generamos la siguiente fase con los ganadores
            nueva_fase = Fase(fase_actual.numero + 1)
            for i in range(0, len(ganadores), 2):
                # Controlar índice impar (número de ganadores impar)
                try:
                    if i + 1 >= len(ganadores):
                        raise IndiceImparError(
                            f"Número de ganadores impar ({len(ganadores)}). No se puede emparejar el equipo '{ganadores[i].nombre}'.")
                    nueva_fase.partidas.append(Partida(ganadores[i], ganadores[i + 1]))
                except IndiceImparError as e:
                    registrar_error(e)

            torneo.bracket._fases.append(nueva_fase)
            print(f"\n{'='*45}")
            print(f"  NUEVA RONDA: {nombre_ronda(nueva_fase, formato)}")
            print(f"{'='*45}")
            continue

        # Jugamos la siguiente partida pendiente
        partida = partidas_pendientes[0]
        mostrar_enfrentamiento(partida, fase_actual, formato)

        # Controlar puntuaciones negativas
        # Controlar empate si el juego no permite_empate()
        pedir_resultado(partida, juego)

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
        # Controlar que bracket sea instancia de RoundRobin antes de llamar a actualizar_tabla
        try:
            if not isinstance(torneo.bracket, RoundRobin):
                raise BracketTipoError(
                    f"Se esperaba RoundRobin pero se encontró {type(torneo.bracket).__name__}.")
            torneo.bracket.actualizar_tabla()
            torneo.bracket.mostrar_clasificacion()
        except BracketTipoError as e:
            registrar_error(e)
    else:
        # En eliminación directa y doble eliminación hay un único ganador al final
        ultima_fase = torneo.bracket._fases[-1]
        # Controlar que la última fase tenga exactamente una partida con resultado
        try:
            if len(ultima_fase.partidas) != 1 or ultima_fase.partidas[0].resultado is None:
                raise FaseFinInvalidaError(
                    f"La fase final debería tener exactamente 1 partida con resultado.")
            campeon = ultima_fase.partidas[0].ganador()
            print(f"\n  CAMPEÓN: {campeon.nombre}")
        except FaseFinInvalidaError as e:
            registrar_error(e)

    print(f"{'='*45}\n")
