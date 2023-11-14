from sprite_animado import *
from enemigo import *


class ObjectHandler:
    """ Clase que se encaraga de mostrar todos los sprites que tenemos """

    def __init__(self, juego):
        self.juego = juego
        self.lista_sprites = []
        self.lista_enemigos = []
        self.ruta_sprites_estaticos = './assets/sprites/static_sprites/'
        self.ruta_sprites_animados = './assets/sprites/animated_sprites/'
        agregar_sprite = self.agregar_sprite
        agregar_enemigo = self.agregar_enemigo
        self.posiciones_enemigos = {}  # Si queremos mas de un enemigo, para que no se empalmen

        # mapa de sprites
        agregar_sprite(ObjetoSprite(juego, ruta=self.ruta_sprites_estaticos + 'banana.png', posicion=(10.5, 3.5),
                                    escala=0.3, shift=1.20))
        agregar_sprite(ObjetoSprite(juego, ruta=self.ruta_sprites_estaticos + 'banana.png', posicion=(10.5, 4.5),
                                    escala=0.3, shift=1.20))
        agregar_sprite(ObjetoSprite(juego, ruta=self.ruta_sprites_estaticos + 'banana.png', posicion=(8.5, 1.5),
                                    escala=0.3, shift=1.20))
        agregar_sprite(ObjetoSprite(juego, ruta=self.ruta_sprites_estaticos + 'banana.png', posicion=(7.5, 1.5),
                                    escala=0.3, shift=1.20))
        agregar_sprite(ObjetoSprite(juego, ruta=self.ruta_sprites_estaticos + 'banana.png', posicion=(6.5, 1.5),
                                    escala=0.3, shift=1.20))

        agregar_sprite(ObjetoSprite(juego, ruta=self.ruta_sprites_estaticos + 'balloon.png', posicion=(6.5, 4.5),
                                    escala=1.1, shift=0))

        agregar_enemigo(
            Enemigo(juego, ruta='./assets/sprites/animated_sprites/donkey_kong/0.png', posicion=(12.5, 1.5),
                    escala=1.2, shift=0, tiempo_animacion=100, velocidad=0.002, tamanno=20))
        agregar_enemigo(
            Enemigo(juego, ruta='./assets/sprites/animated_sprites/donkey_kong/0.png', posicion=(8.5, 2.5),
                    escala=1.2, shift=0, tiempo_animacion=100, velocidad=0.002, tamanno=20))

    def actualizar(self):
        """ Método para actualizar los cambios a todos los sprites """
        self.posiciones_enemigos = {enemigo.posicion_mapa for enemigo in self.lista_enemigos if enemigo.vivo}
        [sprite.actualizar() for sprite in self.lista_sprites]
        [enemigo.actualizar() for enemigo in self.lista_enemigos]

    def agregar_enemigo(self, enemigo):
        """ Método para agregar enemigos a la lista """
        self.lista_enemigos.append(enemigo)

    def agregar_sprite(self, sprite):
        """ Método para agregar cada sprite a la lista """
        self.lista_sprites.append(sprite)
