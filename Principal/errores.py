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