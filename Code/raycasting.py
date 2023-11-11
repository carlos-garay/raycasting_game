import pygame as pg
import math
from config import *


class RayCasting:
    """ Clase que maneja la apariencia delos gráficos en 3D por raycasting"""
    def __init__(self, juego):
        self.juego = juego

    def ray_cast(self):  # TODO Se puede separar mas en una posterior refactorización
        """ Función para calcular las distancias de cada uno de los rayos para el siguiente """
        ox, oy = self.juego.jugador.posicion  # Coordenadas del jugador en el mapa
        x_mapa, y_mapa = self.juego.jugador.posicion_mapa  # Coordenadas del cuadro del mapa en el que se encuentra

        # Se agrega el pequeño valor para evitar errores de división entre 0 en el cálculo del rayo
        angulo_ray = self.juego.jugador.angulo - MITAD_FOV + 0.0001
        for ray in range(NUM_RAYS):  # Calculamos los ángulos de cada rayo
            sin_a = math.sin(angulo_ray)
            cos_a = math.cos(angulo_ray)

            # Determinamos la coordenada de intersección con las líneas verticales
            if cos_a > 0:
                x_vert, dx = (x_mapa + 1, 1)
            else:
                # Cuando el coseno es negativo necesitamos quitar un valor muy pequeño para evitar conflictos
                # al revisar al cuadro de la izquierda
                x_vert, dx = (x_mapa - 1e-6, -1)

            distancia_vert = (x_vert - ox) / cos_a  # Distancia desde el jugador hasta la primera intersección vertical
            y_vert = oy + distancia_vert * sin_a

            delta_distancia = dx / cos_a  # Distancia entre intersecciones verticales siguientes
            dy = delta_distancia * sin_a

            for i in range(MAX_DEPTH):
                tile_vertical = int(x_vert), int(y_vert)
                # revisamos el paso del rayo hasta llegar a la maxima profundidad o toparse con una pared
                if tile_vertical in self.juego.mapa.mapa_mundo1:
                    break
                # sino continuamos añadiendo la distancia segun los tiles que vamos pasando
                x_vert += dx
                y_vert += dy
                distancia_vert += delta_distancia

            # Determinamos la coordenada de intersección con las líneas horizontales
            if sin_a > 0:
                y_hor, dy = (y_mapa + 1, 1)
            else:
                y_hor, dy = (y_mapa - 1e-6, -1)
            distancia_hor = (y_hor - oy) / sin_a
            x_hor = ox + distancia_hor * cos_a

            delta_distancia = dy / sin_a
            dx = delta_distancia * cos_a

            for i in range(MAX_DEPTH):
                tile_horizontal = int(x_hor), int(y_hor)
                if tile_horizontal in self.juego.mapa.mapa_mundo1:
                    break

                x_hor += dx
                y_hor += dy
                distancia_hor += delta_distancia

            # Tendremos punto de intersección con x y con y, elegimos el más chico pues significa
            # que es la primer pared encontrada
            if distancia_vert < distancia_hor:
                distancia = distancia_vert
            else:
                distancia = distancia_hor

            # para eliminar el efecto convexo
            distancia *= math.cos(self.juego.jugador.angulo - angulo_ray)

            # proyección
            altura_proyeccion = DISTANCIA_PANTALLA / (distancia + 0.0001)  # Evitar division por 0

            # dibujar paredes, acorde al número de rayo para calcular su altura proyectada
            color = [255 / (1 + distancia ** 5 * 0.00002)] * 3
            pg.draw.rect(self.juego.pantalla, color,
                         (ray * ESCALA, MITAD_ALTO - altura_proyeccion // 2, ESCALA, altura_proyeccion))

            angulo_ray += ANGULO_DELTA

    def actualizar(self):
        """ Método para mandar llamar a la función de calcular los rays"""
        self.ray_cast()
