import math

# Parámetros ventana de juego
ANCHO = 1200
ALTO = 700
MITAD_ANCHO = 600
MITAD_ALTO = 350
FPS = 60

# Parámetros movimientos del jugador
POSICION_JUGADOR = 1.5, 5  # COORDENADAS DONDE APARECE EN EL MAPA
ANGULO_JUGADOR = 0
VELOCIDAD_JUGADOR = 0.004
VELOCIDAD_ROTACION_JUGADOR = 0.002

# Parámetros raycasting
FOV = math.pi / 3
MITAD_FOV = FOV / 2
NUM_RAYS = ANCHO // 2
MITAD_NUM_RAYS = NUM_RAYS // 2
ANGULO_DELTA = FOV / NUM_RAYS
MAX_DEPTH = 20

# La distancia en la que se localiza la pantalla proyectada para simular 3D
DISTANCIA_PANTALLA = MITAD_ANCHO / math.tan(MITAD_FOV)

# Los rayos no abarcan toda la pantalla, reducimos la escala para mejorar rendimiento
ESCALA = ANCHO // NUM_RAYS

