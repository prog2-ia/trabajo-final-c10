#En este archivo, vamos a pillar los errores y vamos a intentar ver que hacemos  con ellos
from errores import OpcionInvalidaError
from errores import EquiposInsuficientesError
from errores import TorneoError
from errores import (EquiposImpares, TamanioEquipoError, NombreVacioError, PuntuacionNegativaError,
                     EmpateNoPermitidoError, IndiceImparError, BracketTipoError,
                     FaseFinInvalidaError, JugadoresInsuficientesError)


def registrar_error(error):
    """
    Recibe la excepción y muestra el mensaje adecuado por pantalla.
    """
    if isinstance(error, OpcionInvalidaError):
        print(f"OPCIÓN NO VÁLIDA: {error}")

    elif isinstance(error, EquiposInsuficientesError):
        print(f"ERROR EN EQUIPOS: {error}")

    elif isinstance(error, EquiposImpares):
        print(f"ERROR EN EQUIPOS: {error}")

    elif isinstance(error, TamanioEquipoError):
        print(f"ERROR EN EQUIPOS: {error}")

    elif isinstance(error, NombreVacioError):
        print(f"ERROR: {error}")

    elif isinstance(error, PuntuacionNegativaError):
        print(f"ERROR EN PUNTUACIÓN: {error}")

    elif isinstance(error, EmpateNoPermitidoError):
        print(f"ERROR EN RESULTADO: {error}")

    elif isinstance(error, IndiceImparError):
        print(f"ERROR EN FASE: {error}")

    elif isinstance(error, BracketTipoError):
        print(f"ERROR EN BRACKET: {error}")

    elif isinstance(error, FaseFinInvalidaError):
        print(f"ERROR EN FASE FINAL: {error}")

    elif isinstance(error, JugadoresInsuficientesError):
        print(f"ERROR EN JUGADORES: {error}")

    elif isinstance(error, ValueError):
        print("ERROR DE FORMATO: Se esperaba un número y se recibió texto.")

    elif isinstance(error, TorneoError):
        # Captura cualquier otro error que herede de TorneoError pero no tenga mensaje específico
        print(f"ERROR DEL SISTEMA: {error}")

    else:
        # Para errores inesperados de Python (ZeroDivision, etc.)
        print(f"ERROR INESPERADO: {error}")
