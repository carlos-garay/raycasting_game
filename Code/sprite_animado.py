import pygame as pg
from objeto_sprite import ObjetoSprite
from config import *
import os
from collections import deque


class SpriteAnimado(ObjetoSprite):
    """ Clase para manejar sprites animados que cambien entre otros posibles """
    def __init__(self, juego, ruta='../assets/sprites/animated_sprites/donkey_kong/0.png',
                 escala=0.9, shift=.10, tiempo_animacion=120):
        super().__init__(juego, ruta, escala, shift)
        self.tiempo_animacion = tiempo_animacion
        self.ruta = ruta.rsplit('/', 1)[0]
        self.imagenes = self.get_imagenes(self.ruta)
        # variables para revisar si hay que cambiar de imagen
        self.tiempo_previo_animacion = pg.time.get_ticks()
        self.trigger_animacion = False

    def actualizar(self, x, y):
        super().actualizar(x, y)
        self.revisar_tiempo_animacion()
        self.animar(self.imagenes)

    def animar(self, imagenes):
        """ Método para cambiar de sprite cuando sea tiempo """
        if self.trigger_animacion:
            imagenes.rotate(-1)
            self.imagen = imagenes[0]

    def revisar_tiempo_animacion(self):
        """ Método para revisar si ya es momento de cambiar de sprite para simular su movimiento"""
        self.trigger_animacion = False
        tiempo_ahora = pg.time.get_ticks()
        if tiempo_ahora - self.tiempo_previo_animacion > self.tiempo_animacion:
            self.tiempo_previo_animacion = tiempo_ahora
            self.trigger_animacion = True

    def get_imagenes(self, ruta):
        """ Método para obtener las imágenes para los sprites animados, accediendo a la ruta del SO y añadiendolos
         a la cola """
        imagenes = deque()
        for nombre in os.listdir(ruta):
            if os.path.isfile(os.path.join(ruta, nombre)):
                img = pg.image.load(ruta + '/' + nombre).convert_alpha()
                imagenes.append(img)
        return imagenes
