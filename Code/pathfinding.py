from collections import deque
from object_handler import *


class PathFinding:
    """ Clase para definir un algoritmo de búsqueda para el enemigo principal """
    def __init__(self, juego):
        self.juego = juego
        self.mapa = juego.mapa.mapa_1
        # El enemigo se puede mover en 8 direcciones
        self.direcciones = [-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, -1], [1, 1], [-1, 1]
        self.grafo = {}
        self.visitados = {}
        self.get_grafo()

    def get_ruta(self, inicio, objetivo):

        """ Obtener el siguiente paso necesario para llegar al jugador en la ruta calculada"""
        self.visitados = self.algoritmo_bfs(inicio, objetivo, self.grafo)
        ruta = [objetivo]
        paso = self.visitados.get(objetivo, inicio)

        while paso and paso != inicio:
            ruta.append(paso)
            paso = self.visitados[paso]
        return ruta[-1]

    def algoritmo_bfs(self, inicio, objetivo, grafo):
        """ Implementación del algoritmo de búsqueda por amplitud para que el enemigo encuentre al jugador """
        queue = deque([inicio])
        visitados = {inicio: None}

        while queue:
            nodo_actual = queue.popleft()
            if nodo_actual == objetivo:
                break
            nodos_siguientes = grafo[nodo_actual]

            for nodo_siguiente in nodos_siguientes:
                if nodo_siguiente not in visitados and nodo_siguiente not in self.juego.object_handler.posiciones_enemigos:
                    queue.append(nodo_siguiente)
                    visitados[nodo_siguiente] = nodo_actual
        return visitados

    def get_nodos_siguientes(self, x, y):
        """ Método para obtener la lista de tiles adyacentes, nuestros nodos vecinos en BFS"""
        return [(x + dx, y + dy) for dx, dy in self.direcciones if (x + dx, y + dy) not in self.juego.mapa.mapa_mundo1]

    def get_grafo(self):
        """  Método para obtener el diccionario del grafo segun los vecinos de cada nodo.  """
        for y, fila in enumerate(self.mapa):
            for x, col in enumerate(fila):
                if not col:
                    self.grafo[(x, y)] = self.grafo.get((x, y), []) + self.get_nodos_siguientes(x, y)
