import pygame as pg
from config import *


class RendererObjetos:
    """ Clase para manejar los objetos y texturas del juego """
    def __init__(self, juego):
        self.juego = juego
        self.pantalla = juego.pantalla
        self.textura_pared = self.cargar_texturas_pared()

        # Digitos para mostrar el total de bananas recolectadas y las vidas
        self.tamanno_digitos = 60
        self.imagenes_digitos = [self.get_textura(f'../assets/sprites/static_sprites/numbers/{i}.png',
                                                  [self.tamanno_digitos] * 2) for i in range(0, 12)]
        self.digitos = dict(zip(map(str, range(0, 12)), self.imagenes_digitos))

    def dibujar(self):
        """ Llamar al método para dibujar los objetos en la lista a renderizar """
        # dibujar el piso
        pg.draw.rect(self.pantalla, COLOR_PISO, (0, MITAD_ALTO, ANCHO, ALTO))

        # dibujar el techo
        pg.draw.rect(self.pantalla, COLOR_TECHO, (0, 0, ANCHO, MITAD_ALTO))

        self.render_objetos_juego()
        self.dibujar_bananas_jugador()
        self.dibujar_vidas_jugador()

    def dibujar_bananas_jugador(self):
        """ Método para mostrar la cantidad de bananas que el jugador ha recolectado en la partida utilizando las
        imágenes para esto"""
        bananas = str(self.juego.jugador.bananas)
        for i, char in enumerate(bananas):
            self.pantalla.blit(self.digitos[char], (i * self.tamanno_digitos + 5, 10))
        self.pantalla.blit(self.digitos['10'], ((i + 1) * self.tamanno_digitos + 5, 10))

    def dibujar_vidas_jugador(self):
        """ Método para mostrar la cantidad de bananas que el jugador ha recolectado en la partida utilizando las
        imágenes para esto"""
        vidas = str(self.juego.jugador.vidas)
        for i, char in enumerate(vidas):
            self.pantalla.blit(self.digitos[char], (ANCHO - (2 * self.tamanno_digitos) - 5, 10))
        self.pantalla.blit(self.digitos['11'], (ANCHO - self.tamanno_digitos - 5, 10))

    def render_objetos_juego(self):
        """ Acceder a la lista de los objetos que se tienen que renderizar y dibujarlos"""
        # Ordenamos la lista para que los sprites detras de paredes no aparezcan por encima
        lista_objetos = sorted(self.juego.raycasting.objetos_a_renderizar, key=lambda t: t[0], reverse=True)
        for distancia, imagen, posicion in lista_objetos:
            self.pantalla.blit(imagen, posicion)

    @staticmethod
    def get_textura(ruta, res=(TAMANNO_TEXTURA, TAMANNO_TEXTURA)):
        """ Método para obtener las texturas guardadas como parte de nuestros assets"""
        textura = pg.image.load(ruta).convert_alpha()
        return pg.transform.scale(textura, res)

    def cargar_texturas_pared(self):
        """ Método para cargar las texturas de las paredes, con un mapa con un número de textura como llave (mismo que
         en el arreglo de mapa representa que la pared lleva esa textura) y la imagen obtenida de assets como valor """
        return{
            1: self.get_textura('../assets/textures/backroom_wall.png'),
            2: self.get_textura('../assets/textures/backroom_wall2.png')
        }
