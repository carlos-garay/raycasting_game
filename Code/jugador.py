
import pygame as pg
import math
from config import *


class Jugador:
    """ Clase del jugador con su posición y atributos de movimiento"""
    def __init__(self, juego):
        self.juego = juego
        self.x, self.y = POSICION_JUGADOR
        self.angulo = ANGULO_JUGADOR
        self.bananas = 0
        self.vidas = 3
        self.llave = False
        self.rel = 0

    def movimiento(self):
        """ Utilizando el ángulo que tiene el jugador y la tecla de movimiento que presiones podemos calcular
            los incrementos en x y en y que debe tener para determinar su velocidad normalizada """
        sin_a = math.sin(self.angulo)
        cos_a = math.cos(self.angulo)
        dx = 0
        dy = 0

        # Para que la velocidad no se vea repercutida por el framerate, obtenemos el tiempo delta
        # (tiempo que ha transcurrido desde el último frame)
        velocidad = VELOCIDAD_JUGADOR * self.juego.tiempo_delta
        sin_velocidad = velocidad * sin_a
        cos_velocidad = velocidad * cos_a

        keys = pg.key.get_pressed()
        # Segun la dirección de las teclas y el ángulo son los incrementos
        if keys[pg.K_w]:
            dx += cos_velocidad
            dy += sin_velocidad
        if keys[pg.K_s]:
            dx += -cos_velocidad
            dy += -sin_velocidad
        if keys[pg.K_a]:
            dx += sin_velocidad
            dy += -cos_velocidad
        if keys[pg.K_d]:
            dx += -sin_velocidad
            dy += cos_velocidad

        self.revisar_colision_pared(dx, dy)
        self.revisar_condicion_ganar()

        if keys[pg.K_LEFT]:
            self.angulo -= VELOCIDAD_ROTACION_JUGADOR * self.juego.tiempo_delta
        if keys[pg.K_RIGHT]:
            self.angulo += VELOCIDAD_ROTACION_JUGADOR * self.juego.tiempo_delta
        self.angulo %= math.tau  # Tau es una constante = 2pi, para que el ángulo esté dentro de 2pi radianes

    def revisar_colision_pared(self, dx, dy):
        """ Revisa si el jugador intenta entrar a una coordenada donde tenemos una pared para impedírselo"""
        escala = ESCALA_TAMANNO_JUGADOR / self.juego.tiempo_delta
        if (int(self.x + dx * escala), int(self.y)) not in self.juego.mapa.mapa_mundo:
            self.x += dx
        if (int(self.x), int(self.y + dy * escala)) not in self.juego.mapa.mapa_mundo:
            self.y += dy
        if abs(dx) > 0.5 or abs(dy) > 0.5:
            self.x, self.y = POSICION_JUGADOR

    def dibujar(self):
        """ Método para dibujar al jugador y la línea donde apunta su dirección para prueba que funciona"""
        pg.draw.line(self.juego.pantalla, 'yellow', (self.x * TILE_SIZE, self.y * TILE_SIZE),
                     (self.x * TILE_SIZE + ANCHO * math.cos(self.angulo),
                      self.y * TILE_SIZE + ANCHO * math.sin(self.angulo)), 2)
        pg.draw.circle(self.juego.pantalla, 'green', (self.x * TILE_SIZE, self.y * TILE_SIZE), 15)

    def actualizar(self):
        """ Método para llamar a la función de movimiento cada cierto tiempo"""
        self.movimiento()

    def revisar_condicion_ganar(self) -> None:
        """ Revisar si el jugador llegó a la puerta con las llaves para llamar las condiciones de ganar """
        door_x, door_y = self.juego.mapa.posicion_puerta
        if int(self.y) == door_y and self.x > door_x - 0.25 and self.llave:
            self.juego.renderer_objetos.ganar()
            pg.display.flip()
            pg.time.delay(2000)
            self.juego.nueva_partida()
            pg.time.delay(300)

    @property
    def posicion(self):
        """ propiedad para regresar la posición en la que está el jugador"""
        return self.x, self.y

    @property
    def posicion_mapa(self):
        """ propiedad para regresar las coordenadas en int de la posición en el mapa en la que está el jugador"""
        return int(self.x), int(self.y)
