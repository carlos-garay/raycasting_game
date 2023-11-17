import math

# Parámetros ventana de juego
ANCHO = 1400
ALTO = 800
MITAD_ANCHO = ANCHO // 2
MITAD_ALTO = ALTO // 2
FPS = 60
TILE_SIZE = 70

# Parámetros movimientos del jugador
POSICION_JUGADOR = 1.5, 1.5  # COORDENADAS DONDE APARECE EN EL MAPA
ANGULO_JUGADOR = 0
VELOCIDAD_JUGADOR = 0.004
VELOCIDAD_ROTACION_JUGADOR = 0.003
ESCALA_TAMANNO_JUGADOR = 60

# Parámetros enemigo
POSICION_ENEMIGO_1 = 19.5, 1.5
POSICION_ENEMIGO_2 = 25.5, 20.5

# Parametros colores
COLOR_TECHO = (207, 194, 99)
COLOR_PISO = (156, 102, 61)

# Parámetros raycasting
FOV = math.pi / 2
MITAD_FOV = FOV / 2
NUM_RAYS = ANCHO // 2
MITAD_NUM_RAYS = NUM_RAYS // 2
ANGULO_DELTA = FOV / NUM_RAYS
MAX_DEPTH = 20

# La distancia en la que se localiza la pantalla proyectada para simular 3D
DISTANCIA_PANTALLA = MITAD_ANCHO / math.tan(MITAD_FOV)

# Los rayos no abarcan toda la pantalla, reducimos la escala para mejorar rendimiento
ESCALA = ANCHO // NUM_RAYS

TAMANNO_TEXTURA = 256
MITAD_TAMANNO_TEXTURA = TAMANNO_TEXTURA // 2

_ = False  # Los valores numéricos representan paredes, el número indica la textura a cargar
MAPA = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, 5, _, _, _, _, _, _, 5, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, _, _, _, _, _, _, _, 2, _, _, 5, _, 5, 5, 5, 5, 5, 5, _, _, _, _, 1, 1, 1, 1, _, 1, 1, 1],
    [1, 1, _, _, _, 2, _, 2, _, _, 2, _, _, _, _, 5, 5, 1, 1, 1, 1, _, 1, 1, _, 1, _, _, _, _, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, 1, _, _, 1, _, _, _, _, 1, 1, 1],
    [1, _, _, _, _, 2, _, 2, _, _, _, _, _, 1, _, 1, _, 1, _, _, _, _, 1, _, _, 1, _, _, _, _, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, 1, 1, _, _, 1, _, 1, 1, 1, _, _, 1, 1, 1, _, 1, 1, 1, _, 1, _, _, _, 1],
    [1, _, _, 1, _, 1, 1, _, _, 1, 1, _, _, 1, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, 1, _, 1],
    [1, _, _, 1, _, 1, 1, _, _, 1, 1, _, _, 1, _, 1, 1, 1, _, _, _, _, _, _, 1, 1, 1, _, _, _, 1, _, 1],
    [1, _, _, 1, _, 1, 1, _, _, 1, 1, _, _, 1, _, _, _, _, _, _, _, _, _, _, 1, _, 1, 1, 1, 1, 1, _, 1],
    [1, _, _, 1, _, 1, 1, _, _, 1, 1, 1, _, 1, 1, 1, _, 1, _, _, 1, _, 1, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, 1, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1, _, 1, _, _, _, 2, _, _, _, _, _, 1],
    [1, _, _, 1, 1, _, 1, 1, 1, 1, _, 1, _, _, _, 1, 1, 1, _, _, 1, _, _, _, _, _, 2, _, 1, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1, 1, _, _, _, _, _, _, _, 1, _, _, 1, _, _, _, _, _, 2, _, 1, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, _, _, 1, 1, 1, 1, 1, _, _, _, _, 1, _, _, 1, 1, 1, _, _, _, 2, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, _, _, _, _, _, _, _, _, _, 1, 1, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1, 1, _, _, _, _, _, 1, _, _, _, 1, 1, _, 1, _, 5, _, 5, _, _, 1, 1, _, 1],
    [1, _, _, _, _, _, _, _, 1, 1, _, _, _, 2, _, 1, _, _, _, 1, 1, _, 1, _, 5, _, 5, _, _, 1, _, _, 1],
    [1, _, _, _, 1, 1, 1, 1, 1, 1, _, _, _, 2, _, 1, _, 1, _, 1, _, _, _, _, 5, _, 5, _, _, 1, _, _, 1],
    [1, _, _, _, 1, 1, 1, 1, 1, 1, _, 2, 2, 2, _, 1, _, 1, _, 1, _, _, 1, _, 5, _, 5, _, 1, 1, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, 1, _, 5, _, 5, _, _, _, _, _, 3],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 1, 1, 1, 1, 1, 1],
]
