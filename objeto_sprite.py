from abc import ABC

import pygame as pg
from config import *


class ObjetoSprite(ABC):
    """ Clase para crear los sprites que tiene el juego"""
    def __init__(self, juego, ruta='assets/sprites/static_sprites/banana.png',
                 escala=0.3, shift=1.20):
        self.juego = juego
        self.jugador = juego.jugador
        self.imagen = pg.image.load(ruta).convert_alpha()
        self.ancho_imagen = self.imagen.get_width()
        self.mitad_ancho_imagen = self.imagen.get_width() // 2
        self.ratio_imagen = self.ancho_imagen / self.imagen.get_height()
        self.dx, self.dy, self.theta, self.pantalla_x, self.dist, self.dist_norm = 0, 0, 0, 0, 1, 1
        self.mitad_ancho_sprite = 0
        self.escala_sprite = escala
        self.shift_altura_sprite = shift

    def get_proyeccion_sprite(self):
        """ Método para ajustar el tamaño de la proyección de la imagen segun su aspect ratio y a la altura
        que queremos """
        proyeccion = DISTANCIA_PANTALLA / self.dist_norm * self.escala_sprite
        proyeccion_ancho, proyeccion_alto = proyeccion * self.ratio_imagen, proyeccion

        imagen = pg.transform.scale(self.imagen, (proyeccion_ancho, proyeccion_alto))

        self.mitad_ancho_sprite = proyeccion_ancho // 2
        shift_altura = proyeccion_alto * self.shift_altura_sprite
        posicion = self.pantalla_x - self.mitad_ancho_sprite, MITAD_ALTO - proyeccion_alto // 2 + shift_altura

        self.juego.raycasting.objetos_a_renderizar.append((self.dist_norm, imagen, posicion))

    def get_sprite(self, x, y):
        """ Método para obtener el sprite dependendiendo del ángulo desde el que lo ve el jugado r"""
        dx = x - self.jugador.x
        dy = y - self.jugador.y
        self.dx, self.dy = dx, dy
        # Calculamos el ángulo del jugador con la razón de las diferencias en coordenadas entre éste y el sprite
        self.theta = math.atan2(dy, dx)
        delta = self.theta - self.jugador.angulo
        if (dx > 0 and self.jugador.angulo > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau

        # Encontramos la posición en x del sprite en la ventana
        delta_rays = delta / ANGULO_DELTA
        self.pantalla_x = (MITAD_NUM_RAYS + delta_rays) * ESCALA

        # Calculamos el tamaño del sprite segun el tamaño de la proyección
        self.dist = math.hypot(dx, dy)
        self.dist_norm = self.dist * math.cos(delta)  # Eliminar efecto de cámara convexa

        # Cuidamos el problema del rendimiento solo calculando la proyección si está dentro de la visión del jugador
        # Refactor extract variable
        sprite_visible_por_jugador = -self.mitad_ancho_imagen < self.pantalla_x < (ANCHO + self.mitad_ancho_imagen)
        sprite_lejano_a_jugador = self.dist_norm > 0.5
        if sprite_visible_por_jugador and sprite_lejano_a_jugador:
            self.get_proyeccion_sprite()

        # if -self.mitad_ancho_imagen < self.pantalla_x < (ANCHO + self.mitad_ancho_imagen) and self.dist_norm > 0.5:
        #     self.get_proyeccion_sprite()

    def actualizar(self, x, y):
        """ Método para actualizar el estado del sprite"""
        self.get_sprite(x, y)


