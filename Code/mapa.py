import pygame as pg

# Los valores como False son espacioes en blanco y los números paredes
o = False

mapa_1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, o, o, o, o, o, o, o, o, o, o, o, o, o, 1],
    [1, o, o, 1, 1, 1, 1, o, o, o, 1, 1, o, o, 1],
    [1, o, o, o, o, o, 1, o, o, o, o, 1, 1, o, 1],
    [1, o, o, o, o, o, 1, o, o, o, o, o, 1, o, 1],
    [1, o, o, 1, 1, 1, 1, o, o, o, o, o, o, o, 1],
    [1, o, o, o, o, o, o, o, o, o, o, o, o, o, 1],
    [1, o, o, 1, o, o, o, 1, o, o, o, o, o, o, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

class Mapa:
    def __init__(self, juego):
        self.juego = juego
        self.mapa_1 = mapa_1
        self.mapa_mundo1 = {}
        self.obtener_mapa()

    def obtener_mapa(self):
        """ Método donde solo guardamos las coordenadas de las paredes (datos numericos) al diccionario del mapa """
        for j, fila in enumerate(self.mapa_1):  # enumerate nos regresa como tupla el (índice, valor)
            for i, valor in enumerate(fila):
                if valor:
                    self.mapa_mundo1[(i, j)] = valor

    def dibujar(self):
        """ Método para test que aparezca el mapa"""

        [pg.draw.rect(self.juego.pantalla, 'darkgray', (pos[0] * 70, pos[1] * 70, 70, 70), 2)
         for pos in self.mapa_mundo1]
