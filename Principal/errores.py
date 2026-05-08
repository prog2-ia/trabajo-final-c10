#Aqui se manejarán todos los errores del trabajo.

#-----------ERRORES QUE VAN A eSPORTS------------
#ERROR1. Opcion inválida
class OpcionInvalidaError(Exception):
    #Excepción lanzada cuando el usuario elige una opción fuera del menú (1-6).
    def __init__(self, valor):
        self.valor = valor
        super().__init__(f"La opción '{valor}' no es válida.")
#ERROR2. Entrada vacía
class EntradaVaciaError(Exception):
    #Excepción lanzada si el usuario pulsa Enter sin escribir nada.
    def __init__(self):
        super().__init__("No has introducido ningún valor.")
#---------------------------------------------------

#meteremos más...
