#En este archivo, vamos a pillar los errores y vamos a intentar ver que hacemos  con ellos
from Principal.errores import OpcionInvalidaError
from Principal.errores import EquiposInsuficientesError
from Principal.errores import TorneoError
from Principal.errores import EquiposImpares
from Principal.errores import TamanoEquipoError
from Principal.errores import NombreVacioError
from Principal.errores import PuntuacionNegativaError
from Principal.errores import EmpateNoPermitidoError
from Principal.errores import IndiceImparError
from Principal.errores import BracketTipoError
from Principal.errores import FaseFinInvalidaError
from Principal.errores import JugadoresInsuficientesError


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

    elif isinstance(error, TamanoEquipoError):
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
