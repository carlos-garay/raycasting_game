import pygame as pg
from config import *

# Los valores como False son espacioes en blanco y los números paredes
o = False

mapa_1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, o, o, 1, 1, o, o, o, o, o, o, o, o, o, 1],
    [1, o, o, o, o, o, o, o, o, o, 1, 1, 1, o, 1],
    [1, o, o, o, o, o, o, o, o, o, o, o, 1, o, 1],
    [1, o, o, 2, 2, o, o, o, o, o, o, o, 1, o, 1],
    [1, o, o, 2, 2, o, o, o, 1, 1, o, o, 1, o, 1],
    [1, o, o, o, o, o, o, o, o, 1, 1, 1, 1, o, 1],
    [1, o, o, 1, 1, o, o, 1, o, o, o, o, o, o, 3],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


class Mapa:
    """ Clase para guardar y mostrar el mapa del nivel"""
    def __init__(self, juego):
        self.juego = juego
        self.mapa = mapa_1
        self.mapa_mundo = {}
        self.posicion_puerta = (14, 8)
        self.obtener_mapa()

    def obtener_mapa(self):
        """ Método donde solo guardamos las coordenadas de las paredes (datos numericos) al diccionario del mapa """
        for j, fila in enumerate(self.mapa):  # enumerate nos regresa como tupla el (índice, valor)
            for i, valor in enumerate(fila):
                if valor:
                    self.mapa_mundo[(i, j)] = valor

    def dibujar(self):
        """ Método para test que aparezca el mapa"""

        [pg.draw.rect(self.juego.pantalla, 'darkgray', (pos[0] * TILE_SIZE, pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE), 2)
         for pos in self.mapa_mundo]
