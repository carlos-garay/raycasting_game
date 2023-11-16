import pygame as pg
from objeto_sprite import ObjetoSprite
from config import *
from coleccionable import Coleccionable


class Llave(ObjetoSprite, Coleccionable):
    """ Clase para manejar el objeto llave para abrir la puerta al siguiente nivel """

    def __init__(self, juego, ruta='../assets/sprites/static_sprites/key.png', posicion=(12.5, 1.5),
                 escala=0.9, shift=.10, rango_coleccion=0.5):
        super().__init__(juego, ruta, posicion, escala, shift)
        self.ruta = ruta.rsplit('/', 1)[0]
        # variable para determinar si ya fue recolectada
        self.bandera_activo = True
        self.rango_coleccion = rango_coleccion

    def actualizar(self):
        """ Método para actualizar el estado del coleccionable """
        self.get_sprite()
        self.logica_coleccionar()

    def logica_coleccionar(self):
        """ Recolectar el objeto y quitar el candado de la puerta """

        ox, oy = self.juego.jugador.posicion  # Coordenadas del jugador en el mapa
        distancia = math.sqrt(pow(ox - self.x, 2) + pow(oy - self.y, 2))

        # Cuando el jugador esta encima del coleccionable y aun no se obtiene, omitiendo el 0 cuando se estan cargando
        if distancia < 0.6 and distancia != 0 and self.bandera_activo:
            self.bandera_activo = False
            self.juego.jugador.llave = True

            # Buscamos la posición de la puerta y cambiamos su textura a que no tenga candado
            for llave in self.juego.mapa.mapa_mundo:
                if self.juego.mapa.mapa_mundo[llave] == 3:
                    self.juego.mapa.mapa_mundo[llave] = 4
                    break
