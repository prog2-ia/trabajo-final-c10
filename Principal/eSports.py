#Trabajo eSports.py
#Archivo para ejecutar

#importamos los errores que vienen del archivo errores.py
from errores import OpcionInvalidaError, EntradaVaciaError
#blablabla
def descrip_modos():
    print("\n DESCRIPCIÓN DE GÉNEROS eSPORTS\n")

    print("1.- Battle Royale")
    print("En los Battle Royale una gran cantidad de jugadores compiten entre sí")
    print("hasta que solamente queda uno o un equipo con vida. Suelen incluir")
    print("mapas muy grandes, zonas que se reducen con el tiempo y partidas largas.")
    print("Ejemplos conocidos: Fortnite, Apex Legends, PUBG.\n")

    print("2.- Deportes")
    print("Los juegos de deportes buscan simular competiciones deportivas reales")
    print("como fútbol, baloncesto, automovilismo o tenis. Normalmente enfrentan")
    print("a dos jugadores o equipos en partidos con reglas similares al deporte real.")
    print("Ejemplos conocidos: FIFA/EA Sports FC, NBA 2K, Rocket League.\n")

    print("3.- Lucha")
    print("Los juegos de lucha enfrentan a dos jugadores en combates")
    print("directos donde gana quien reduzca primero la vida del rival.")
    print("Se basan mucho en reflejos, combos y precisión.")
    print("Ejemplos conocidos: Street Fighter, Tekken, Mortal Kombat.\n")

    print("4.- MOBA")
    print("Los MOBA enfrentan a dos equipos en mapas divididos por líneas.")
    print("Cada jugador controla un personaje con habilidades únicas y el objetivo")
    print("principal suele ser destruir la base enemiga.")
    print("Ejemplos conocidos: League of Legends, Dota 2, Smite.\n")

    print("5.- Shooter")
    print("Los shooters son juegos centrados en el combate con armas de fuego.")
    print("Pueden jugarse en primera persona o tercera persona y suelen requerir")
    print("buena puntería, reflejos rápidos y trabajo en equipo.")
    print("Ejemplos conocidos: Counter Strike, Valorant, Call of Duty.\n")


def menu_modo():
    #diccionario de modos llamado mapping
    mapping = {'1': 'BR', '2': 'D', '3': 'L', '4': 'M', '5': 'S'}

    while True:
        try:
            print("Elija el género que desea para su torneo: ")
            print(f"1.- Battle Royale \n2.- Deportes \n3.- Lucha \n4.- Moba \n5.- Shooter")
            print("6.- Ver descripciones detalladas")

            answ = input('Introduzca su opción: ')

            # 1. Primero vemos si no se ha introducido nada
            if not answ:
                raise EntradaVaciaError() #Error de entrada vacía

            # 2. Si la opción es el número 6, vemos las descripciones
            if answ == '6':
                descrip_modos()
                continue  # Reinicia el bucle para volver a preguntar

            # 3. Validar si la opción no está en nuestro diccionario de modos
            if answ not in mapping:
                raise OpcionInvalidaError(answ)

        except EntradaVaciaError as e:
            print(f"\nERROR: {e}\n")
        except OpcionInvalidaError as e:
            print(f"\nERROR: {e} Por favor, elija un número del 1 al 6.\n")
        except Exception as e:
            print(f"\nERROR: Ha ocurrido un error inesperado: {e}\n")

        else:
            # Si no hay errores, guardamos el modo y salimos del bucle
            modo_elegido = mapping[answ]
            print(f"\n>>> Has elegido {modo_elegido}.\n")
            return modo_elegido


if __name__ == "__main__":
    modo = menu_modo()
    print(f"Torneo de {modo}")
