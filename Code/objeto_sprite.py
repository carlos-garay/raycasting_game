import pygame as pg
from config import *

class ObjetoSprite:
    """ Clase para crear los sprites que tiene el juego"""

    def __init__(self, juego, ruta='../assets/sprites/static_sprites/banana.png', posicion=(10.5, 3.5),
                 escala=0.3, shift=1.20):
        self.juego = juego
        self.jugador = juego.jugador
        self.x, self.y = posicion
        self.imagen = pg.image.load(ruta).convert_alpha()
        self.ANCHO_IMAGEN = self.imagen.get_width()
        self.MITAD_ANCHO_IMAGEN = self.imagen.get_width() // 2
        self.RATIO_IMAGEN = self.ANCHO_IMAGEN / self.imagen.get_height()
        self.dx, self.dy, self.theta, self.pantalla_x, self.dist, self.dist_norm = 0, 0, 0, 0, 1, 1
        self.mitad_ancho_sprite = 0
        self.ESCALA_SPRITE = escala
        self.SHIFT_ALTURA_SPRITE = shift

    def get_proyeccion_sprite(self):
        """ Método para ajustar el tamaño de la proyección de la imagen segun su aspect ratio y a la altura
        que queremos """
        proyeccion = DISTANCIA_PANTALLA / self.dist_norm * self.ESCALA_SPRITE
        proyeccion_ancho, proyeccion_alto = proyeccion * self.RATIO_IMAGEN, proyeccion

        imagen = pg.transform.scale(self.imagen, (proyeccion_ancho, proyeccion_alto))

        self.mitad_ancho_sprite = proyeccion_ancho // 2
        shift_altura = proyeccion_alto * self.SHIFT_ALTURA_SPRITE
        posicion = self.pantalla_x - self.mitad_ancho_sprite, MITAD_ALTO - proyeccion_alto // 2 + shift_altura

        self.juego.raycasting.objetos_a_renderizar.append((self.dist_norm, imagen, posicion))

    def get_sprite(self):
        """ Método para obtener el sprite dependendiendo del ángulo desde el que lo ve el jugado r"""
        dx = self.x - self.jugador.x
        dy = self.y - self.jugador.y
        self.dx, self.dy = dx, dy
        # Calculamos el ángulo del jugador con la razón de las diferencias en coordenadas entre éste y el sprite
        self.theta = math.atan2(dy, dx)
        delta = self.theta - self.jugador.angulo
        if (dx > 0 and self.jugador.angulo > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau
        delta_rays = delta / ANGULO_DELTA
        self.pantalla_x = (MITAD_NUM_RAYS + delta_rays) * ESCALA

        # Calculamos el tamaño del sprite segun el tamaño de la proyección
        self.dist = math.hypot(dx, dy)
        self.dist_norm = self.dist * math.cos(delta)

        # Cuidamos el problema del rendimiento Si el sprite se ve más grande que la pantalla
        # TODO posible refactorización para claridad.
        if -self.MITAD_ANCHO_IMAGEN < self.pantalla_x < (ANCHO + self.MITAD_ANCHO_IMAGEN) and self.dist_norm > 0.5:
            self.get_proyeccion_sprite()

    def actualizar(self):
        """ Método para actualizar el estado del sprite"""
        self.get_sprite()


