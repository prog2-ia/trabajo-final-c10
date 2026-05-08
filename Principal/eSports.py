#Trabajo eSports.py
#Archivo para ejecutar


if __name__ == "__main__":
    def menu_modo():

        # Print del menú
        print("Elija el género que desea para su torneo: ")
        print("1.- Battle Royale")
        print("2.- Deportes")
        print("3.- Lucha")
        print("4.- Moba")
        print("5.- Shooter")
        print("6.- *En caso de no saber identificar el género del juego para su torneo, aquí tiene las descripciones*")

        answ = input('Introduzca su opción: ')

        # Validación
        while answ not in ['1', '2', '3', '4', '5']:

            if answ == '6':
                descrip_modos()
            else:
                print('Opción no válida.')

            answ = input('Introduzca su opción: ')

        # Guardamos el modo
        if answ == '1':
            modo = 'BR'
        elif answ == '2':
            modo = 'D'
        elif answ == '3':
            modo = 'L'
        elif answ == '4':
            modo = 'M'
        elif answ == '5':
            modo = 'S'

        return modo

    def descrip_modos():
        print("\n----- DESCRIPCIÓN DE GÉNEROS eSPORTS -----\n")

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
        print("Los juegos de lucha enfrentan normalmente a dos jugadores en combates")
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