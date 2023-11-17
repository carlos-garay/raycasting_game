from sprite_animado import *
import math
import sys


class Enemigo(SpriteAnimado):
    """ Clase para crear los enemigos """
    def __init__(self, juego, ruta='../assets/sprites/animated_sprites/donkey_kong/0.png', posicion=(12.5, 1.5),
                 escala=1, shift=0.1, tiempo_animacion=100, velocidad=0.038, tamanno=20):
        super().__init__(juego, ruta, escala, shift, tiempo_animacion)
        self.x, self.y = posicion
        self.velocidad = velocidad
        self.tamanno = tamanno
        self.vivo = True
        self.valor_raycast = False
        self.trigger_busqueda_jugador = True

    @property
    def posicion_mapa(self):
        """ Método para regresar como tupla la posición en el mapa que tiene el enemigo"""
        return int(self.x), int(self.y)

    def actualizar_enemigo(self):
        """ Método para actualizar el estado del enemigo """
        self.revisar_tiempo_animacion()
        self.get_sprite(self.x, self.y)
        self.logica_enemigo()
        # self.draw_ray_cast()

    def revisar_colision_pared(self, dx, dy):
        """ Revisa si el enemigo intenta entrar a una coordenada donde tenemos una pared para impedírselo"""
        if (int(self.x + dx * self.tamanno), int(self.y)) not in self.juego.mapa.mapa_mundo:
            self.x += dx
        if (int(self.x), int(self.y + dy * self.tamanno)) not in self.juego.mapa.mapa_mundo:
            self.y += dy

    def movimiento(self):
        """ Método para determinar la forma en la que se mueve el enemigo"""
        # Si el enemigo esta en el mismo tile que el jugador, su destino ahora es el jugador en sí
        if int(self.x) == int(self.juego.jugador.x) and int(self.y) == int(self.juego.jugador.y):
            posicion_siguiente = (self.juego.jugador.x, self.juego.jugador.y)
            x_siguiente, y_siguiente = posicion_siguiente

        # Sino, obten como posicion siguiente el tile siguiente en la ruta del bfs
        else:
            posicion_siguiente = self.juego.pathfinding.get_ruta(self.posicion_mapa, self.juego.jugador.posicion_mapa)
            x_siguiente, y_siguiente = posicion_siguiente
        # pg.draw.rect(self.juego.pantalla, 'blue', (TILE_SIZE * x_siguiente, TILE_SIZE * y_siguiente,
        #                                            TILE_SIZE, TILE_SIZE))

        if posicion_siguiente not in self.juego.object_handler.posiciones_enemigos:
            angulo = math.atan2(y_siguiente + 0.5 - self.y, x_siguiente + 0.5 - self.x)
            dx = math.cos(angulo) * self.velocidad * self.juego.tiempo_delta
            dy = math.sin(angulo) * self.velocidad * self.juego.tiempo_delta
            self.revisar_colision_pared(dx, dy)

    def logica_enemigo(self):
        """" Método para determinar la forma en la que funciona el enemigo """
        if self.vivo:
            self.animar(self.imagenes)
            self.movimiento()
            self.revisar_ataque_jugador()

    def revisar_ataque_jugador(self):
        """ Método para revisar si el enemigo entró en contacto con el jugador, le quita una vida y revisa si se
            reinicia el nivel o se termina el juego si no quedan más vidas"""

        ox, oy = self.juego.jugador.posicion  # Coordenadas del jugador en el mapa

        distancia = math.sqrt(pow(ox - self.x, 2) + pow(oy - self.y, 2))

        # Cuando el enemigo esta muy cerca del jugador, omitiendo cuando es 0 antes de que se termine de cargar
        if distancia < 0.6 and distancia != 0:

            self.juego.jugador.vidas -= 1
            if self.juego.jugador.vidas < 0:
                self.juego.renderer_objetos.game_over()
                pg.display.flip()
                pg.time.delay(2000)
                self.juego.nueva_partida()
            else:
                self.juego.renderer_objetos.dibujar_vidas_jugador()
                self.juego.checkpoint.cargar_checkpoint()
