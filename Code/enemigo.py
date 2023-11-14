from sprite_animado import *
from random import randint, random, choice


class Enemigo(SpriteAnimado):
    """ Clase para crear los enemigos """
    def __init__(self, juego, ruta='../assets/sprites/animated_sprites/donkey_kong/0.png', posicion=(12.5, 1.5),
                 escala=1, shift=0.1, tiempo_animacion=100, velocidad=0.038, tamanno=20):
        super().__init__(juego, ruta, posicion, escala, shift, tiempo_animacion)
        self.velocidad = velocidad
        self.tamanno = tamanno
        self.vivo = True
        self.valor_raycast = False
        self.trigger_busqueda_jugador = True

    @property
    def posicion_mapa(self):
        return int(self.x), int(self.y)

    def actualizar(self):
        """ Método para actualizar el estado del enemigo """
        self.revisar_tiempo_animacion()
        self.get_sprite()
        self.logica_enemigo()
        # self.draw_ray_cast()

    def revisar_colision_pared(self, dx, dy):
        """ Revisa si el enemigo intenta entrar a una coordenada donde tenemos una pared para impedírselo"""
        if (int(self.x + dx * self.tamanno), int(self.y)) not in self.juego.mapa.mapa_mundo1:
            self.x += dx
        if (int(self.x), int(self.y + dy * self.tamanno)) not in self.juego.mapa.mapa_mundo1:
            self.y += dy

    def movimiento(self):
        """ Método para determinar la forma en la que se mueve el enemigo"""
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
            if self.raycast_enemigo_jugador():
                self.trigger_busqueda_jugador = True
                self.movimiento()
            elif self.trigger_busqueda_jugador:
                self.movimiento()


    def raycast_enemigo_jugador(self):  # TODO Se puede separar mas en una posterior refactorización
        """ Función para determinar si el enemigo puede ver al jugador """
        if self.juego.jugador.posicion_mapa == self.posicion_mapa:  # Si esta en el mismo cuadrante, se pueden ver
            return True

        dist_vertical_pared, dist_horizontal_pared = 0, 0
        dist_vertical_jugador, dist_horizontal_jugador = 0, 0

        ox, oy = self.juego.jugador.posicion  # Coordenadas del jugador en el mapa
        x_mapa, y_mapa = self.juego.jugador.posicion_mapa  # Coordenadas del cuadro del mapa en el que se encuentra

        angulo_ray = self.theta

        sin_a = math.sin(angulo_ray)
        cos_a = math.cos(angulo_ray)

        # Determinamos la coordenada de intersección con las líneas verticales
        if cos_a > 0:
            x_vert, dx = (x_mapa + 1, 1)
        else:
            # Cuando el coseno es negativo necesitamos quitar un valor muy pequeño para evitar conflictos
            # al revisar al cuadro de la izquierda
            x_vert, dx = (x_mapa - 1e-6, -1)

        distancia_vert = (x_vert - ox) / cos_a  # Distancia desde el jugador hasta la primera intersección vertical
        y_vert = oy + distancia_vert * sin_a

        delta_distancia = dx / cos_a  # Distancia entre intersecciones verticales siguientes
        dy = delta_distancia * sin_a

        for i in range(MAX_DEPTH):
            tile_vertical = int(x_vert), int(y_vert)
            # revisamos el paso del rayo hasta llegar a la maxima profundidad o toparse con una pared
            if tile_vertical == self.posicion_mapa:
                dist_vertical_jugador = distancia_vert
                break

            if tile_vertical in self.juego.mapa.mapa_mundo1:
                dist_vertical_pared = distancia_vert
                break
            # sino continuamos añadiendo la distancia segun los tiles que vamos pasando
            x_vert += dx
            y_vert += dy
            distancia_vert += delta_distancia

        # Determinamos la coordenada de intersección con las líneas horizontales
        if sin_a > 0:
            y_hor, dy = (y_mapa + 1, 1)
        else:
            y_hor, dy = (y_mapa - 1e-6, -1)

        distancia_hor = (y_hor - oy) / sin_a
        x_hor = ox + distancia_hor * cos_a

        delta_distancia = dy / sin_a
        dx = delta_distancia * cos_a

        for i in range(MAX_DEPTH):
            tile_horizontal = int(x_hor), int(y_hor)
            if tile_horizontal == self.posicion_mapa:
                dist_horizontal_jugador = distancia_hor
                break
            if tile_horizontal in self.juego.mapa.mapa_mundo1:
                dist_horizontal_pared = distancia_hor
                break

            x_hor += dx
            y_hor += dy
            distancia_hor += delta_distancia

        # Determinamos si es posible que el enemigo pueda ver al jugador

        dist_jugador = max(dist_vertical_jugador, dist_horizontal_jugador)
        dist_pared = max(dist_vertical_pared, dist_horizontal_pared)

        if 0 < dist_jugador < dist_pared or not dist_pared:
            return True
        return False

    def draw_ray_cast(self):
        """ Método para probar que funciona el rayo del enemigo al jugador"""
        pg.draw.circle(self.juego.pantalla, 'red', (TILE_SIZE * self.x, TILE_SIZE * self.y), 15)
        if self.raycast_enemigo_jugador():
            pg.draw.line(self.juego.pantalla, 'orange', (TILE_SIZE * self.juego.jugador.x,
                         TILE_SIZE * self.juego.jugador.y), (TILE_SIZE * self.x, TILE_SIZE * self.y), 2)



