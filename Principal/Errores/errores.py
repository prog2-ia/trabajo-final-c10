#errores.py
#Aquí tenemos todos los errores posibles, no se importa de ningun sitio

# #manejo_errores.py se encarga de resolverlos


#En primer lugar, creamos una clase TorneoError, y a partir de ahi, todas las subclases de todos los errores.
class TorneoError(Exception):
    '''La clase base de errores'''
    pass
class OpcionInvalidaError(TorneoError):
    """Se lanza cuando el usuario elige una opción inexistente en los menús."""
    #Numero fuera del rango...
    pass

class EquiposInsuficientesError(TorneoError):
    """Se lanza cuando el número de equipos no alcanza el mínimo del formato."""
    #si num equipos menor del requerido, ERROR
    pass

class RegistroJugadorError(TorneoError):
    """Errores relacionados con la creación o validación de jugadores."""
    pass

class EquiposImpares(TorneoError):
    """Se lanza cuando se requieren equipos pares y el número es impar."""
    pass

class TamanoEquipoError(TorneoError):
    """Se lanza cuando el tamaño del equipo no coincide con el que impone el juego."""
    pass

class NombreVacioError(TorneoError):
    """Se lanza cuando el nombre del torneo está vacío."""
    pass

class PuntuacionNegativaError(TorneoError):
    """Se lanza cuando se introduce una puntuación negativa."""
    pass

class EmpateNoPermitidoError(TorneoError):
    """Se lanza cuando hay empate en un juego que no lo permite."""
    pass

class IndiceImparError(TorneoError):
    """Se lanza cuando el número de ganadores es impar al generar la siguiente fase."""
    pass

class BracketTipoError(TorneoError):
    """Se lanza cuando el bracket no es RoundRobin al llamar a actualizar_tabla."""
    pass

class FaseFinInvalidaError(TorneoError):
    """Se lanza cuando la última fase no tiene exactamente una partida con resultado."""
    pass

class JugadoresInsuficientesError(TorneoError):
    """Se lanza cuando no hay suficientes jugadores en el fichero para cubrir todos los equipos."""
    pass