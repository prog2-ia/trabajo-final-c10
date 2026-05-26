# Gestor de Torneos eSports

Sistema de gestión de torneos competitivos desarrollado en Python. Permite organizar torneos completos para distintos géneros de videojuegos, con soporte para múltiples formatos de bracket, generación automática de equipos y exportación del resumen del torneo a fichero de texto.

---

## Características

- **5 géneros de videojuego**: Battle Royale, MOBA, Shooter, Lucha y Deportes, cada uno con sus propias reglas y formatos válidos
- **3 formatos de torneo**: Eliminación Directa, Doble Eliminación y Round Robin
- **Creación de equipos** manual o aleatoria desde una base de datos de jugadores y equipos reales de eSports
- **Seguimiento en tiempo real** del torneo con nombres de ronda automáticos (Final, Semifinal, Round of 16...)
- **Exportación a fichero txt**: opción de guardar un resumen completo del torneo al terminar
- **Control de errores** centralizado con excepciones personalizadas para entradas inválidas

---

## Estructura del Proyecto

```
trabajo-final-c10/
│
├── main.py                     # Punto de entrada: ejecutable principal
│
├── Modos/                      # Subgéneros de videojuego
│   ├── battleroyale.py
│   ├── moba.py
│   ├── shooter.py
│   ├── lucha.py
│   └── deportes.py
│
├── Eliminaciones/              # Formatos de bracket
│   ├── bracketeliminacion.py
│   ├── eliminaciondirecta.py
│   ├── dobleeliminacion.py
│   └── roundrobin.py
│
└── Principal/
    │
    ├── Entidades/              # Clases del dominio del torneo
    │   ├── juego.py
    │   ├── jugador.py
    │   ├── equipo.py
    │   ├── torneo.py
    │   ├── bracket.py
    │   ├── fase.py
    │   ├── partida.py
    │   └── resultado.py
    │
    ├── Errores/                # Excepciones personalizadas y manejador
    │   ├── errores.py
    │   └── manejo_errores.py
    │
    └── Datos/                  # Base de datos, generación aleatoria y exportación
        ├── generador_aleatorio.py
        ├── generador_txt.py
        ├── crear_ficheros.py
        ├── jugadores.pickle
        ├── equipos.pickle
        └── Resumenes/          # Carpeta generada automáticamente con los ficheros txt
```

---

## Instalación

**Requisitos:** Python 3.10 o superior

```bash
# 1. Clona el repositorio
git clone https://github.com/jorgesancere/trabajo-final-c10.git
cd trabajo-final-c10

# 2. (Solo la primera vez) Genera los ficheros de la base de datos
python Principal/Datos/crear_ficheros.py

# 3. Ejecuta el programa
python main.py
```

> Los ficheros `jugadores.pickle` y `equipos.pickle` ya están incluidos en el repositorio, por lo que el paso 2 solo es necesario si los eliminas o quieres regenerarlos.

---
### Ejecutable Linux

Si no tienes Python instalado, puedes ejecutar directamente el binario incluido en la raíz del repositorio:

```bash
./main
```

## Flujo de uso

```
1. Elige el género del juego
        ↓
2. Elige el formato de torneo (según los que admite ese género)
        ↓
3. Indica cuántos equipos participan
        ↓
4. Crea los equipos manualmente o genéralos de forma aleatoria
        ↓
5. Elige si exportar el torneo a txt.
        ↓
6. El torneo arranca: se muestran los enfrentamientos ronda a ronda
        ↓
7. Introduce los resultados de cada partida
        ↓
8. Al final de cada partida puedes consultar el estado del torneo
        ↓
9. El torneo termina mostrando el campeón o la clasificación final
```
## Autores

- **Jorge Sánchez Cerezo** — [@jorgesancere](https://github.com/jorgesancere)
- **Javier Rifé Sánchez** — [@javierrife](https://github.com/javierrife)

*Proyecto de Programación II — Grado en Ingeniería en Inteligencia Artificial, Universidad de Alicante*