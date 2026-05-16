# 🎮 Gestor de Torneos eSports

Sistema de gestión de torneos competitivos desarrollado en Python como proyecto universitario de **Programación Orientada a Objetos**. Permite organizar torneos completos para distintos géneros de videojuegos, con soporte para múltiples formatos de bracket y generación automática de equipos.

---

## 📋 Características

- 🕹️ **5 géneros de videojuego** — Battle Royale, MOBA, Shooter, Lucha y Deportes, cada uno con sus propias reglas y formatos válidos
- 🏆 **3 formatos de torneo** — Eliminación Directa, Doble Eliminación y Round Robin
- 👥 **Creación de equipos** manual o aleatoria desde una base de datos de jugadores y equipos reales de eSports
- 📊 **Seguimiento en tiempo real** del torneo con nombres de ronda automáticos (Final, Semifinal, Round of 16...)
- 🔒 **Arquitectura OO completa** — herencia, clases abstractas, encapsulación y composición

---

## 🗂️ Estructura del Proyecto

```
trabajo-final-c10/
│
├── Principal/
│   ├── eSports.py              # Punto de entrada y bucle principal
│   ├── torneo.py               # Clase Torneo (composición central)
│   ├── juego.py                # Clase abstracta Juego
│   ├── bracket.py              # Clase abstracta Bracket
│   ├── fase.py                 # Fases del torneo
│   ├── partida.py              # Enfrentamiento entre dos equipos
│   ├── resultado.py            # Lógica de puntos y ganador
│   ├── equipo.py               # Clase Equipo
│   ├── jugador.py              # Clase Jugador con winrate
│   ├── generador_aleatorio.py  # Generación aleatoria desde ficheros .pickle
│   ├── crear_ficheros.py       # Script de inicialización de la base de datos
│   ├── jugadores.pickle        # Base de datos de jugadores eSports
│   ├── equipos.pickle          # Base de datos de equipos eSports
│   ├── errores.py              # Excepciones personalizadas
│   └── manejo_errores.py       # Manejador centralizado de errores
│
├── Modos/
│   ├── battleroyale.py
│   ├── moba.py
│   ├── shooter.py
│   ├── lucha.py
│   └── deportes.py
│
└── Eliminaciones/
    ├── bracketeliminacion.py
    ├── eliminaciondirecta.py
    ├── dobleeliminacion.py
    └── roundrobin.py
```

---

## ⚙️ Instalación

**Requisitos:** Python 3.10 o superior

```bash
# 1. Clona el repositorio
git clone https://github.com/jorgesancere/trabajo-final-c10.git
cd trabajo-final-c10

# 2. (Solo la primera vez) Genera los ficheros de la base de datos
python Principal/crear_ficheros.py

# 3. Ejecuta el programa
python Principal/eSports.py
```

> Los ficheros `jugadores.pickle` y `equipos.pickle` ya están incluidos en el repositorio, por lo que el paso 2 solo es necesario si los eliminas o quieres regenerarlos.

---

## 🚀 Flujo de uso

```
1. Elige el género del juego
        ↓
2. Elige el formato de torneo (según los que admite ese género)
        ↓
3. Indica cuántos equipos participan
        ↓
4. Crea los equipos manualmente o genéralos de forma aleatoria
        ↓
5. El torneo arranca — se muestran los enfrentamientos ronda a ronda
        ↓
6. Introduce los resultados de cada partida
        ↓
7. Al final de cada partida puedes consultar el estado del torneo
        ↓
8. El torneo termina mostrando el campeón o la clasificación final
```

---

## 🧱 Conceptos de POO aplicados

| Concepto | Dónde se aplica |
|---|---|
| **Herencia** | `Moba`, `Shooter`... heredan de `Juego`; `EliminacionDirecta`... heredan de `Bracket` |
| **Clases abstractas** | `Juego` y `Bracket` usan `ABC` con métodos abstractos |
| **Encapsulación** | Atributos `__privados` y `_protegidos` con `@property` |
| **Composición** | `Torneo` contiene un `Juego` y un `Bracket` |
| **Polimorfismo** | Cada subclase de `Juego` devuelve sus propios `formatos_validos()` |
| **Modularización** | Código dividido en 3 carpetas y más de 15 archivos |

---

## 👨‍💻 Autores

- **Jorge Sánchez Cerezo** — [@jorgesancere](https://github.com/jorgesancere)
- **Javier Rifé Sánchez** — [@javierrs007-web](https://github.com/javierrs007-web)

*Proyecto de Programación II — Grado en Ingeniería en Inteligencia Artificial, Universidad de Alicante*
```