from tipo_coleccionable import *


class FabricaColeccionable:
    """ Clase fábrica de los objetos flyweights para coleccionables """
    tipos_coleccionable = {}

    @classmethod
    def get_tipo_coleccionable(cls, nombre, juego, ruta='assets/sprites/static_sprites/banana.png',
                               escala=0.9, shift=.10, rango_coleccion=0.5):
        """ Método para crear los objetos flyweight solo si no existe ya uno de ese tipo en el diccionario """

        if nombre not in cls.tipos_coleccionable:
            resultado = TipoColeccionable(juego, ruta, escala, shift, rango_coleccion)
            cls.tipos_coleccionable[nombre] = resultado
            return resultado
        else:
            return cls.tipos_coleccionable[nombre]

    @classmethod
    def limpiar_lista(cls):
        """ Método para crear los objetos flyweight solo si no existe ya uno de ese tipo en el diccionario """
        cls.tipos_coleccionable = {}
