from sprite_animado import *
from enemigo import *
from coleccionable import *


class ObjectHandler:
    """ Clase que se encaraga de mostrar todos los sprites que tenemos """

    def __init__(self, juego):
        self.juego = juego
        self.lista_enemigos = []
        self.lista_coleccionables = []
        self.ruta_sprites_estaticos = '../assets/sprites/static_sprites/'
        self.ruta_sprites_animados = '../assets/sprites/animated_sprites/'
        agregar_coleccionable = self.agregar_coleccionable
        agregar_enemigo = self.agregar_enemigo
        self.posiciones_enemigos = {}  # Si queremos mas de un enemigo, para que no se empalmen

        # mapa de sprites
        agregar_coleccionable(Coleccionable(juego, ruta=self.ruta_sprites_estaticos + 'banana.png', posicion=(10.5, 3.5),
                                            escala=0.3, shift=1.20))
        agregar_coleccionable(Coleccionable(juego, ruta=self.ruta_sprites_estaticos + 'banana.png', posicion=(10.5, 4.5),
                                            escala=0.3, shift=1.20))
        agregar_coleccionable(Coleccionable(juego, ruta=self.ruta_sprites_estaticos + 'banana.png', posicion=(8.5, 1.5),
                                            escala=0.3, shift=1.20))
        agregar_coleccionable(Coleccionable(juego, ruta=self.ruta_sprites_estaticos + 'banana.png', posicion=(7.5, 1.5),
                                            escala=0.3, shift=1.20))
        agregar_coleccionable(Coleccionable(juego, ruta=self.ruta_sprites_estaticos + 'banana.png', posicion=(6.5, 1.5),
                                            escala=0.3, shift=1.20))
        # agregar_coleccionable(Coleccionable(juego, ruta=self.ruta_sprites_estaticos + 'balloon.png', posicion=(6.5, 4.5),
        #                                     escala=1.1, shift=0))

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

    def agregar_coleccionable(self, sprite):
        """ Método para agregar un sprite coleccionable a la lista """
        self.lista_coleccionables.append(sprite)
