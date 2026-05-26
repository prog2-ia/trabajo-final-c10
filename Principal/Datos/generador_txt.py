import os

BASE_DIR = os.path.dirname(__file__)
CARPETA_RESUMENES = os.path.join(BASE_DIR, 'Resumenes')


class GeneradorTxt:
    def __init__(self, nombre_torneo: str, juego, formato: str):
        # Creamos la carpeta Resumenes si no existe
        if not os.path.exists(CARPETA_RESUMENES):
            os.makedirs(CARPETA_RESUMENES)

        # El nombre del fichero será el nombre del torneo sin espacios
        nombre_fichero = nombre_torneo.replace(' ', '_') + '.txt'
        self.__ruta = os.path.join(CARPETA_RESUMENES, nombre_fichero)

        # Escribimos la cabecera del torneo
        self.__escribir_cabecera(nombre_torneo, juego, formato)

    def __escribir_cabecera(self, nombre_torneo: str, juego, formato: str):
        nombres_formato = {'eliminacion_directa': 'Eliminación Directa','doble_eliminacion': 'Doble Eliminación','round_robin': 'Round Robin'}
        with open(self.__ruta, 'a', encoding='utf-8') as writer:
            writer.write('=' * 45 + '\n')
            writer.write(f'TORNEO: {nombre_torneo}\n')
            writer.write(f'Juego: {juego.nombre} ({type(juego).__name__})\n')
            writer.write(f'Formato: {nombres_formato.get(formato, formato)}\n')
            writer.write('=' * 45 + '\n\n')

    def escribir_equipos(self, equipos: list):
        # Escribe la lista de equipos y jugadores al inicio del resumen
        with open(self.__ruta, 'a', encoding='utf-8') as writer:
            writer.write('--- EQUIPOS PARTICIPANTES ---\n')
            for eq in equipos:
                writer.write(f'  {eq.nombre} ({eq.region})\n')
                for j in eq.juegos:
                    writer.write(f'    - {j.nick}\n')
            writer.write('\n')

    def escribir_nueva_ronda(self, nombre_ronda: str):
        # Escribe el encabezado de una nueva ronda
        with open(self.__ruta, 'a', encoding='utf-8') as writer:
            writer.write('=' * 45 + '\n')
            writer.write(f'  {nombre_ronda}\n')
            writer.write('=' * 45 + '\n')

    def escribir_resultado_partida(self, partida, nombre_ronda: str):
        # Escribe el resultado de una partida
        with open(self.__ruta, 'a', encoding='utf-8') as writer:
            writer.write(f'  [{nombre_ronda}] {partida.equipo1.nombre} vs {partida.equipo2.nombre}')
            if partida.resultado:
                ganador = partida.ganador()
                writer.write(f' -> {partida.resultado}')
                if ganador:
                    writer.write(f' | Ganador: {ganador.nombre}')
                else:
                    writer.write(' | Empate')
            writer.write('\n')

    def escribir_campeon(self, campeon):
        # Escribe el campeón al final del resumen
        with open(self.__ruta, 'a', encoding='utf-8') as writer:
            writer.write('\n' + '=' * 45 + '\n')
            writer.write(f'  CAMPEÓN: {campeon.nombre}\n')
            writer.write('=' * 45 + '\n')

    def escribir_clasificacion_rr(self, bracket):
        with open(self.__ruta, 'a', encoding='utf-8') as writer:
            writer.write('\n--- CLASIFICACIÓN FINAL ---\n')
            clasificacion = bracket.get_clasificacion()
            for i, (equipo, puntos) in enumerate(clasificacion, 1):
                writer.write(f'  {i}. {equipo.nombre} — {puntos} puntos\n')