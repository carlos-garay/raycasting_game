from enum import Enum

from banana import Banana
from llave import Llave
from enemigo import *
from coleccionable import *


class ObjectHandler:
    """ Clase que se encaraga de crear todos los sprites que tenemos (Factory Concreta)"""
    class TiposColeccionables(Enum):
        """ Enumeración posibles tipos de coleccionables """
        BANANA = "banana"
        LLAVE = "llave"
        BANDERA = "bandera"

    def __init__(self, juego):
        self.juego = juego  # TODO que sea el raycasting solamente?
        self.lista_enemigos = []
        self.lista_coleccionables = []
        self.ruta_sprites_estaticos = '../assets/sprites/static_sprites/'
        self.ruta_sprites_animados = '../assets/sprites/animated_sprites/'
        agregar_coleccionable = self.agregar_coleccionable
        agregar_enemigo = self.agregar_enemigo
        self.posiciones_enemigos = {}  # Si queremos mas de un enemigo, para que no se empalmen

        # mapa de sprites TODO hacer un método para cargar sprites dependiendo del nivel en el que estamos
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(10.5, 3.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(10.5, 4.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(8.5, 1.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(7.5, 1.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(6.5, 1.5))

        agregar_coleccionable(self.TiposColeccionables.LLAVE, posicion=(7.5, 3.5))

        agregar_enemigo(
            Enemigo(juego, ruta='../assets/sprites/animated_sprites/donkey_kong/0.png', posicion=(12.5, 1.5),
                    escala=1.2, shift=0, tiempo_animacion=100, velocidad=0.002, tamanno=5))
        # agregar_enemigo(
        #     Enemigo(juego, ruta='../assets/sprites/animated_sprites/donkey_kong/0.png', posicion=(8.5, 2.5),
        #             escala=1.2, shift=0, tiempo_animacion=100, velocidad=0.002, tamanno=20))

    def actualizar(self):
        """ Método para actualizar los cambios a todos los sprites """
        self.posiciones_enemigos = {enemigo.posicion_mapa for enemigo in self.lista_enemigos if enemigo.vivo}
        [coleccionable.actualizar() for coleccionable in self.lista_coleccionables if
         coleccionable.bandera_activo is True]
        [enemigo.actualizar() for enemigo in self.lista_enemigos]

    def agregar_enemigo(self, enemigo):
        """ Método para agregar enemigos a la lista """
        self.lista_enemigos.append(enemigo)

    def agregar_coleccionable(self, tipo: TiposColeccionables, posicion=(10.5, 3.5)):
        """ Método para agregar un sprite coleccionable a la lista """
        sprite = Banana(self.juego)
        if tipo.value == "banana":
            sprite = Banana(self.juego, self.ruta_sprites_estaticos + 'banana.png', posicion, escala=0.3, shift=1.20)
        elif tipo.value == "llave":
            sprite = Llave(self.juego, self.ruta_sprites_estaticos + 'key.png', posicion, escala=0.4, shift=1.0)
        elif tipo.value == "bandera":
            pass

        self.lista_coleccionables.append(sprite)
