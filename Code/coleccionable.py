from abc import ABC, abstractmethod

import pygame as pg
from objeto_sprite import ObjetoSprite
from config import *
import os
from collections import deque


class Coleccionable(ABC):
    """ Interfaz para objetos que sean coleccionables por el jugador """

    @abstractmethod
    def actualizar_coleccionable(self):
        """ Método abstracto para actualizar el estado del coleccionable """
        pass

    @abstractmethod
    def logica_coleccionar(self):
        """ Método abstracto para manejar lo que sucede al recolectar el objeto """
        pass
