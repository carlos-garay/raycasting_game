"""
Proyecto final Diseño de Software
Equipo:
Carlos Eduardo Garay Olmos
Martín Santiago Herrera Soto
"""

import pygame as pg

from memento import Memento
from mapa import *
import sys
from jugador import *
from config import *
from raycasting import *
from render_objetos import *
from object_handler import *
from sonido import *
from pathfinding import *
from fabrica_coleccionable import *
from checkpoint import *


class Juego:
    """ Clase con las configuraciones y funciones principales para que corra el juego """
    def __init__(self):
        """ Inicializamos el framerate y el tamaño de la pantalla """
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))
        self.clock = pg.time.Clock()
        self.tiempo_delta = 1
        self.mapa = Mapa(self)
        self.renderer_objetos = RendererObjetos(self)
        self.raycasting = RayCasting(self)
        self.sonido = Sonido(self)
        self.pathfinding = PathFinding(self)
        self.jugador = Jugador(self)
        self.object_handler = ObjectHandler(self)
        self.checkpoint = Checkpoint(self)
        FabricaColeccionable.limpiar_lista()
        self.sonido.poner_musica()

    def nueva_partida(self) -> None:
        """ Método para mandar llamar a la creación del mapa inicial """
        self.mapa = Mapa(self)
        self.renderer_objetos = RendererObjetos(self)
        self.raycasting = RayCasting(self)
        self.sonido = Sonido(self)
        self.pathfinding = PathFinding(self)
        self.jugador = Jugador(self)
        self.object_handler = ObjectHandler(self)
        FabricaColeccionable.limpiar_lista()
        self.checkpoint = Checkpoint(self)

    def reiniciar_nivel(self):
        """ Método para reiniciar el nivel si el jugador es atrapado """
        self.mapa = Mapa(self)
        self.raycasting = RayCasting(self)
        self.sonido = Sonido(self)
        self.object_handler = ObjectHandler(self)
        self.jugador.x, self.jugador.y = POSICION_JUGADOR
        self.jugador.angulo = ANGULO_JUGADOR
        self.jugador.bananas = 0
        self.jugador.llave = False
        FabricaColeccionable.limpiar_lista()

    def guardar_estado(self):
        """ Método para para crear un Memento del estado del juego para los checkpoints """
        return Memento(self.jugador.x, self.jugador.y, self.jugador.bananas, self.jugador.llave, self.object_handler.lista_coleccionables)

    def cargar_estado(self, memento):
        """ Método para para cargar el estado de un checkpoint guardado como Memento """
        jugador_x, jugador_y, jugador_bananas, jugador_llave, lista_coleccionables_flag = memento.obtener_estado()
        self.object_handler.cambiar_estado_colecionables(lista_coleccionables_flag)
        self.jugador.x, self.jugador.y = jugador_x, jugador_y
        self.jugador.angulo = ANGULO_JUGADOR
        self.jugador.bananas = jugador_bananas
        self.jugador.llave = jugador_llave
        self.object_handler.lista_enemigos[0].x = POSICION_ENEMIGO_1[0]
        self.object_handler.lista_enemigos[0].y = POSICION_ENEMIGO_1[1]
        self.object_handler.lista_enemigos[1].x = POSICION_ENEMIGO_2[0]
        self.object_handler.lista_enemigos[1].y = POSICION_ENEMIGO_2[1]
        if jugador_llave:
            # Cambiamos la textura de la puerta a que no tenga candado
            posicion_puerta = self.mapa.posicion_puerta
            self.mapa.mapa_mundo[posicion_puerta] = 4
        else:
            # Sino, ponemos la textura de la puerta con candado
            posicion_puerta = self.mapa.posicion_puerta
            self.mapa.mapa_mundo[posicion_puerta] = 3
        FabricaColeccionable.limpiar_lista()

    def refrescar_pantalla(self) -> None:
        """ Actualizar la pantalla del juego, incluye información de FPS """
        self.jugador.actualizar()
        self.raycasting.actualizar()
        self.object_handler.actualizar()
        pg.display.flip()
        self.tiempo_delta = self.clock.tick(FPS)
        # pg.display.set_caption(f'{self.clock.get_fps():.1f}')
        pg.display.set_caption('DK Maze')
        
    def dibujar(self) -> None:
        """ Dibujamos los gráficos en pantalla """
        self.renderer_objetos.dibujar()

        # self.pantalla.fill('black')
        # self.mapa.dibujar()
        # self.jugador.dibujar()

    def revisar_salir(self) -> None:
        """ Revisar los eventos del teclado para saber si se debe cerrar la aplicacion """
        for evento in pg.event.get():
            if evento.type == pg.QUIT or (evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self) -> None:
        """ Método principal del juego donde se mantiene corriendo """
        while True:
            self.revisar_salir()
            self.refrescar_pantalla()
            self.dibujar()


if __name__ == '__main__':
    juego = Juego()
    juego.run()
