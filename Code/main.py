"""
Proyecto final Diseño de Software
Equipo:
Carlos Eduardo Garay Olmos
Martín Santiago Herrera Soto
"""

import pygame as pg
from mapa import *
import sys
from jugador import *
from config import *
from raycasting import *
from render_objetos import *
from object_handler import *


class Juego:
    """ Clase con las configuraciones y funciones principales para que corra el juego """
    def __init__(self):
        """ Inicializamos el framerate y el tamaño de la pantalla """
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))
        self.clock = pg.time.Clock()
        self.tiempo_delta = 1
        self.nueva_partida()

    def nueva_partida(self) -> None:
        """ Método para mandar llamar a la creación del mapa inicial """
        self.mapa = Mapa(self)
        self.jugador = Jugador(self)
        self.renderer_objetos = RendererObjetos(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)

    def refrescar_pantalla(self) -> None:
        """ Actualizar la pantalla del juego, incluye información de FPS """
        self.jugador.actualizar()
        self.raycasting.actualizar()
        self.object_handler.actualizar()
        pg.display.flip()
        self.tiempo_delta = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')
        
    def dibujar(self) -> None:
        """ Dibujamos los gráficos en pantalla """
        self.renderer_objetos.dibujar()
        # self.mapa.dibujar()
        # self.jugador.dibujar()

    def revisar_eventos(self) -> None:
        """ Revisar los eventos del teclado para ejecutar una respectiva función """
        for evento in pg.event.get():
            if evento.type == pg.QUIT or (evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
        
    def run(self) -> None:
        """ Método principal del juego donde se mantiene corriendo """
        while True:
            self.revisar_eventos()
            self.refrescar_pantalla()
            self.dibujar()


if __name__ == '__main__':
    juego = Juego()
    juego.run()
