import pygame as pg
from tipo_coleccionable import TipoColeccionable
from objeto_sprite import ObjetoSprite
from config import *
from coleccionable import Coleccionable


class Llave(Coleccionable):
    """ Clase para manejar el objeto llave para abrir la puerta al siguiente nivel """

    def __init__(self, flyweight_coleccionable, posicion=(12.5, 1.5)):
        self.x, self.y = posicion
        self.flyweight_coleccionable: TipoColeccionable = flyweight_coleccionable
        # variable para determinar si ya fue recolectada
        self.bandera_activo = True

    def actualizar_coleccionable(self):
        """ Método para actualizar el estado del coleccionable """
        self.flyweight_coleccionable.get_sprite(self.x, self.y)
        self.logica_coleccionar()

    def logica_coleccionar(self):
        """ Recolectar el objeto y quitar el candado de la puerta """

        ox, oy = self.flyweight_coleccionable.juego.jugador.posicion  # Coordenadas del jugador en el mapa
        distancia = math.sqrt(pow(ox - self.x, 2) + pow(oy - self.y, 2))

        # Cuando el jugador esta encima del coleccionable y aun no se obtiene, omitiendo el 0 cuando se estan cargando
        if distancia < self.flyweight_coleccionable.rango_coleccion and distancia != 0 and self.bandera_activo:
            self.bandera_activo = False
            self.flyweight_coleccionable.juego.sonido.llave.play()
            self.flyweight_coleccionable.juego.jugador.llave = True

            # SUBSTITUTE ALGORITHM
            # Cambiamos la textura de la puerta a que no tenga candado
            posicion_puerta = self.flyweight_coleccionable.juego.mapa.posicion_puerta
            self.flyweight_coleccionable.juego.mapa.mapa_mundo[posicion_puerta] = 4

            # # Buscamos la posición de la puerta y cambiamos su textura a que no tenga candado
            # for llave in self.flyweight_coleccionable.juego.mapa.mapa_mundo:
            #     # 3 representa textura puerta cerrada
            #     if self.flyweight_coleccionable.juego.mapa.mapa_mundo[llave] == 3:
            #         # 4 representa textura puerta abierta
            #         self.flyweight_coleccionable.juego.mapa.mapa_mundo[llave] = 4
            #         break
