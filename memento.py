
class Memento:
    """ Clase memento para guardar el estado del juego cuando tomas un checkpoint """
    def __init__(self, jugador_x, jugador_y, jugador_bananas, jugador_llave, lista_coleccionables):
        self._jugador_x = jugador_x
        self._jugador_y = jugador_y
        self._jugador_bananas = jugador_bananas
        self._jugador_llave = jugador_llave
        self._lista_coleccionables_flags = [coleccionable.bandera_activo for coleccionable in lista_coleccionables]

    def obtener_estado(self):
        """ Método para regresar el estado del memento que tenemos guardado"""
        return self._jugador_x, self._jugador_y, self._jugador_bananas, self._jugador_llave, self._lista_coleccionables_flags
