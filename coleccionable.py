from abc import ABC, abstractmethod

import pygame as pg
from objeto_sprite import ObjetoSprite
from config import *
import os
from collections import deque


class Coleccionable(ABC):
    """ Clase abstracta para objetos que sean coleccionables por el jugador """
    def __init__(self, flyweight_coleccionable, posicion):
        self.x, self.y = posicion
        self.flyweight = flyweight_coleccionable
        self.bandera_activo = True

    @abstractmethod
    def actualizar_coleccionable(self):
        """ Método abstracto para actualizar el estado del coleccionable """
        pass

    @abstractmethod
    def logica_coleccionar(self):
        """ Método abstracto para manejar lo que sucede al recolectar el objeto """
        pass
