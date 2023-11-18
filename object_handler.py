from enum import Enum

from banana import Banana
from llave import Llave
from enemigo import *
from coleccionable import *
from fabrica_coleccionable import *
from bandera import *


class ObjectHandler:
    """ Clase que se encaraga de crear todos los sprites que tenemos (Factory Concreta)"""
    class TiposColeccionables(Enum):
        """ Enumeración posibles tipos de coleccionables """
        BANANA = "banana"
        LLAVE = "llave"
        BANDERA = "bandera"

    def __init__(self, juego):
        self.juego = juego
        self.lista_enemigos = []
        self.lista_coleccionables = []
        self.ruta_sprites_estaticos = 'assets/sprites/static_sprites/'
        self.ruta_sprites_animados = 'assets/sprites/animated_sprites/'
        agregar_coleccionable = self.agregar_coleccionable
        agregar_enemigo = self.agregar_enemigo
        self.posiciones_enemigos = {}  # Si queremos mas de un enemigo, para que no se empalmen

        # BANANAS
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(4.5, 8.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(4.5, 10.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(2.5, 17.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(2.5, 19.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(5.5, 20.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(6.5, 4.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(7.5, 14.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(7.5, 16.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(8.5, 20.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(9.5, 1.5))

        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(9.5, 4.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(11.5, 16.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(11.5, 17.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(11.5, 20.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(12.5, 1.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(12.5, 4.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(12.5, 8.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(12.5, 12.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(14.5, 7.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(14.5, 20.5))

        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(16.5, 5.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(16.5, 11.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(16.5, 13.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(16.5, 14.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(17.5, 20.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(19.5, 12.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(19.5, 14.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(19.5, 20.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(20.5, 19.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(22.5, 12.5))

        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(22.5, 13.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(23.5, 19.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(23.5, 20.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(24.5, 12.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(24.5, 14.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(25.5, 1.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(27.5, 6.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(27.5, 7.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(27.5, 12.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(27.5, 13.5))

        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(27.5, 20.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(28.5, 8.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(29.5, 6.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(29.5, 7.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(30.5, 11.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(30.5, 14.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(31.5, 1.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(31.5, 6.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(31.5, 9.5))
        agregar_coleccionable(self.TiposColeccionables.BANANA, posicion=(31.5, 16.5))

        # LLAVE
        agregar_coleccionable(self.TiposColeccionables.LLAVE, posicion=(27.5, 4.5))

        # BANDERAS
        agregar_coleccionable(self.TiposColeccionables.BANDERA, posicion=(18.5, 9.5))
        agregar_coleccionable(self.TiposColeccionables.BANDERA, posicion=(26.5, 4.5))

        # ENEMIGOS
        agregar_enemigo(
            Enemigo(juego, ruta='assets/sprites/animated_sprites/donkey_kong/0.png', posicion=(19.5, 1.5),
                    escala=1.2, shift=0, tiempo_animacion=100, velocidad=0.002, tamanno=10))
        agregar_enemigo(
            Enemigo(juego, ruta='assets/sprites/animated_sprites/donkey_kong/0.png', posicion=(25.5, 20.5),
                    escala=1.2, shift=0, tiempo_animacion=100, velocidad=0.002, tamanno=10))

    def actualizar(self):
        """ Método para actualizar los cambios a todos los sprites """
        self.posiciones_enemigos = {enemigo.posicion_mapa for enemigo in self.lista_enemigos if enemigo.vivo}
        [coleccionable.actualizar_coleccionable() for coleccionable in self.lista_coleccionables if
         coleccionable.bandera_activo is True]
        [enemigo.actualizar_enemigo() for enemigo in self.lista_enemigos]

    def agregar_enemigo(self, enemigo):
        """ Método para agregar enemigos a la lista """
        self.lista_enemigos.append(enemigo)

    def agregar_coleccionable(self, tipo: TiposColeccionables, posicion=(10.5, 3.5)):
        """ Método para agregar un sprite coleccionable a la lista """
        sprite = Banana(self.juego)
        if tipo.value == "banana":
            coleccionable_flyweight = FabricaColeccionable.get_tipo_coleccionable(tipo.value, self.juego,
                self.ruta_sprites_estaticos + 'banana.png', escala=0.3, shift=1.20, rango_coleccion=0.5)
            sprite = Banana(coleccionable_flyweight, posicion)
        elif tipo.value == "llave":
            coleccionable_flyweight = FabricaColeccionable.get_tipo_coleccionable(tipo.value, self.juego,
                self.ruta_sprites_estaticos + 'key.png', escala=0.4, shift=1.0, rango_coleccion=0.5)
            sprite = Llave(coleccionable_flyweight, posicion)
        elif tipo.value == "bandera":
            coleccionable_flyweight = FabricaColeccionable.get_tipo_coleccionable(tipo.value, self.juego,
                self.ruta_sprites_estaticos + 'flag.png', escala=1, shift=0.15, rango_coleccion=0.75)
            sprite = Bandera(coleccionable_flyweight, posicion)

        self.lista_coleccionables.append(sprite)

    def cambiar_estado_colecionables(self, lista_coleccionables_flag):
        """ Método para recuperar el estado de cuáles objetos coleccionables ya se habían recogido """
        for i in range(0, len(self.lista_coleccionables)):
            self.lista_coleccionables[i].bandera_activo = lista_coleccionables_flag[i]
