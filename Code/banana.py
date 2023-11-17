import pygame as pg

from tipo_coleccionable import TipoColeccionable
from objeto_sprite import ObjetoSprite
from config import *
from coleccionable import Coleccionable


class Banana(Coleccionable):
    """ Clase para definir funcionalidad de las bananas """
    def __init__(self, flyweight_coleccionable, posicion=(12.5, 1.5)):
        self.x, self.y = posicion
        self.flyweight: TipoColeccionable = flyweight_coleccionable
        # variable para determinar si ya fue recolectada
        self.bandera_activo = True

    def actualizar_coleccionable(self):
        """ Método para actualizar el estado del coleccionable """
        self.flyweight.get_sprite(self.x, self.y)
        self.logica_coleccionar()

    def logica_coleccionar(self):
        """ Recolactar el objeto solo cuando estamos encima de el y aumentar el contador de bananas  """

        ox, oy = self.flyweight.juego.jugador.posicion  # Coordenadas del jugador en el mapa
        distancia = math.sqrt(pow(ox - self.x, 2) + pow(oy - self.y, 2))

        # Cuando el jugador esta encima del coleccionable y aun no se obtiene, omitiendo el 0 cuando se estan cargando
        if distancia < self.flyweight.rango_coleccion and distancia != 0 and self.bandera_activo:
            self.bandera_activo = False
            self.flyweight.juego.sonido.banana.play()
            self.flyweight.juego.jugador.bananas += 1
            self.flyweight.juego.renderer_objetos.dibujar_bananas_jugador()
