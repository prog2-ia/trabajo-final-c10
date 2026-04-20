Sistema de Gestión de Torneos eSports
Un ecosistema en Python diseñado para gestionar equipos, jugadores y diversas modalidades de torneos (Brackets) para diferentes géneros de videojuegos competitivos. 

· Características Principales
    Jerarquía de Videojuegos: Soporte específico para múltiples géneros como MOBA, Shooter, Battle Royale, Lucha y Deportes. 
    Gestión de Competidores: Sistema de perfiles para jugadores con cálculo automático de Winrate y estatus competitivo.
    Sistemas de Torneo (Brackets):
    Eliminación Directa: Formato clásico donde el perdedor queda fuera.
    Doble Eliminación: Incluye un cuadro de perdedores (repesca) para dar una segunda oportunidad.
    Round Robin: Formato de "todos contra todos" con tabla de clasificación por puntos.

· Estructura del Proyecto
    El proyecto sigue un modelo de Programación Orientada a Objetos (POO) con herencia y clases abstractas:

· Núcleo de Juegos
    La clase base Juego es extendida por clases especializadas que añaden atributos propios de cada género:
    Shooter: Control de rondas y mapas.
    Moba: Gestión de líneas, jungla y duración.
    BattleRoyale: Número de jugadores y mapas.
    Deportes/Lucha: Atributos técnicos como duración de partida o perspectiva (2D/3D).

· Sistema de Competición
    El motor de torneos se organiza en una jerarquía lógica:
    Bracket (Abstracta): Define la estructura base para cualquier torneo.
    Fase: Contenedor de partidas que verifica si se puede avanzar a la siguiente etapa.
    Partida: Gestiona el enfrentamiento entre dos equipos y su resultado.
    Resultado: Lógica interna para determinar ganadores basándose en puntos.

· Entidades
    Equipo: Agrupación de jugadores con ranking y región.
    Jugador: Registro de estadísticas individuales y cálculo de nivel (Favorito vs Don Nadie).

· Instalación y Uso
  Requisitos: Tener instalado Python 3.x.
    Ejecución: El punto de entrada principal es el archivo eSports.py.
    Bash
    python eSports.py
· Detalles Técnicos
    Encapsulamiento: Uso de atributos privados (e.g., __puntos en Resultado) y protegidos para asegurar la integridad de los datos.
    Abstracción: Implementación de ABC en la clase Bracket para obligar a definir el método gen_bracket en cada tipo de torneo.
    Validaciones: El sistema verifica si todas las partidas de una fase han terminado antes de permitir el avance del torneo.


(README temporal).
