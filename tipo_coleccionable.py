import pygame as pg
from objeto_sprite import ObjetoSprite


class TipoColeccionable(ObjetoSprite):
    """ Clase para definir funcionalidad de las bananas """
    def __init__(self, juego, ruta='assets/sprites/static_sprites/banana.png',
                 escala=0.9, shift=.10, rango_coleccion=0.5):
        super().__init__(juego, ruta, escala, shift)
        # variable para determinar si ya fue recolectada
        self.rango_coleccion = rango_coleccion

    def actualizar(self, x, y):
        """ Método para actualizar el estado visible del coleccionable """
        self.get_sprite(x, y)
