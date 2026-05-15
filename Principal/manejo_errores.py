#En este archivo, vamos a pillar los errores y vamos a intentar ver que hacemos  con ellos
from errores import OpcionInvalidaError
from errores import EquiposInsuficientesError
from errores import TorneoError


def registrar_error(error):
    """
    Recibe la excepción y muestra el mensaje adecuado por pantalla.
    """
    if isinstance(error, OpcionInvalidaError):
        print(f"OPCIÓN NO VÁLIDA: {error}")

    elif isinstance(error, EquiposInsuficientesError):
        print(f"ERROR EN EQUIPOS: {error}")

    elif isinstance(error, ValueError):
        print("ERROR DE FORMATO: Se esperaba un número y se recibió texto.")

    elif isinstance(error, TorneoError):
        # Captura cualquier otro error que herede de TorneoError pero no tenga mensaje específico
        print(f"ERROR DEL SISTEMA: {error}")

    else:
        # Para errores inesperados de Python (ZeroDivision, etc.)
        print(f"ERROR INESPERADO: {error}")
