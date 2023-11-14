import pygame as pg
import math
from config import *


class RayCasting:
    """ Clase que maneja la apariencia delos gráficos en 3D por raycasting"""
    def __init__(self, juego):
        self.juego = juego
        self.resultado_raycasting = []
        self.objetos_a_renderizar = []
        self.texturas = self.juego.renderer_objetos.textura_pared

    def obtener_objetos_a_renderizar(self):
        """ Obtener los parámetros de los resultados de raycasting y por cada uno tomar el rectángulo recortado
        de la textura segun sea appropiado """
        self.objetos_a_renderizar = []
        for ray, valores in enumerate(self.resultado_raycasting):
            distancia, altura_proyeccion, textura, offset = valores

            # Para evitar un error en el rendimiento por como se escala la textura, restringir que el tamaño del
            # segmento rectangular de la imagen no exceda el de la pantalla
            if altura_proyeccion < ALTO:
                columna_pared = self.texturas[textura].subsurface(
                    offset * (TAMANNO_TEXTURA - ESCALA), 0, ESCALA, TAMANNO_TEXTURA
                )

                # Escalamos la superficie al tamaño de la proyección que ve el jugador
                columna_pared = pg.transform.scale(columna_pared, (ESCALA, altura_proyeccion))

                # La posición de la pared depende del número de rayo que la este dibujando
                posicion_pared = (ray * ESCALA, MITAD_ALTO - altura_proyeccion // 2)

            else:
                altura_textura = TAMANNO_TEXTURA * ALTO / altura_proyeccion
                columna_pared = self.texturas[textura].subsurface(
                    offset * (TAMANNO_TEXTURA - ESCALA), MITAD_TAMANNO_TEXTURA - altura_textura // 2,
                    ESCALA, altura_textura
                )
                columna_pared = pg.transform.scale(columna_pared, (ESCALA, ALTO))
                posicion_pared = (ray * ESCALA, 0)

            self.objetos_a_renderizar.append((distancia, columna_pared, posicion_pared))

    def raycast(self):  # TODO Se puede separar mas en una posterior refactorización
        """ Función para calcular las distancias de cada uno de los rayos a una pared """
        self.resultado_raycasting = []
        ox, oy = self.juego.jugador.posicion  # Coordenadas del jugador en el mapa
        x_mapa, y_mapa = self.juego.jugador.posicion_mapa  # Coordenadas del cuadro del mapa en el que se encuentra
        textura_vert = 1
        textura_hor = 1

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
                    textura_vert = self.juego.mapa.mapa_mundo1[tile_vertical]
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
                    textura_hor = self.juego.mapa.mapa_mundo1[tile_horizontal]
                    break

                x_hor += dx
                y_hor += dy
                distancia_hor += delta_distancia

            # Tendremos punto de intersección con x y con y, elegimos el más chico pues significa
            # que es la primer pared encontrada, también se calcula el offset de las texturas en las paredes
            if distancia_vert < distancia_hor:
                distancia = distancia_vert
                textura = textura_vert
                y_vert %= 1
                offset = y_vert if cos_a > 0 else (1 - y_vert)
            else:
                distancia = distancia_hor
                textura = textura_hor
                x_hor %= 1
                offset = (1 - x_hor) if sin_a > 0 else x_hor

            # para eliminar el efecto convexo
            distancia *= math.cos(self.juego.jugador.angulo - angulo_ray)

            # proyección
            altura_proyeccion = DISTANCIA_PANTALLA / (distancia + 0.0001)  # Evitar division por 0

            # # dibujar paredes, acorde al número de rayo para calcular su altura proyectada
            # color = [255 / (1 + distancia ** 5 * 0.00002)] * 3
            # pg.draw.rect(self.juego.pantalla, color,
            #              (ray * ESCALA, MITAD_ALTO - altura_proyeccion // 2, ESCALA, altura_proyeccion))

            # resultado de raycasting
            self.resultado_raycasting.append((distancia, altura_proyeccion, textura, offset))

            angulo_ray += ANGULO_DELTA

    def actualizar(self):
        """ Método para mandar llamar a la función de calcular los rays"""
        self.raycast()
        self.obtener_objetos_a_renderizar()
