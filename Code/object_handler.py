from objeto_sprite import *
from sprite_animado import *


class ObjectHandler:
    """ Clase que se encaraga de mostrar todos los sprites que tenemos """

    def __init__(self, juego):
        self.juego = juego
        self.lista_sprites = []
        self.ruta_sprites_estaticos = './assets/sprites/static_sprites/'
        self.ruta_sprites_animados = './assets/sprites/animated_sprites/'
        agregar_sprite = self.agregar_sprite

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
                                    escala=0.6, shift=.20))

        agregar_sprite(SpriteAnimado(juego, ruta=self.ruta_sprites_animados + 'donkey_kong/0.png', posicion=(12.5, 1.5),
                                     escala=0.9, shift=.10, tiempo_animacion=500))

    def actualizar(self):
        """ Método para actualizar los cambios a todos los sprites """
        [sprite.actualizar() for sprite in self.lista_sprites]

    def agregar_sprite(self, sprite):
        """ Método para agregar cada sprite a la lista """
        self.lista_sprites.append(sprite)
