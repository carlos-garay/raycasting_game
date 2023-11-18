import pygame as pg


class Sonido:
    """ Clase para manejar los sonidos del juego """
    def __init__(self, juego):
        self.juego = juego
        pg.mixer.init()
        self.ruta = 'assets/sound/'
        self.banana = pg.mixer.Sound(self.ruta + 'Banana.mp3')
        self.bandera = pg.mixer.Sound(self.ruta + 'Checkpoint.mp3')
        self.llave = pg.mixer.Sound(self.ruta + 'Key.mp3')
        self.golpe_dk = pg.mixer.Sound(self.ruta + 'DK_yell.mp3')
        self.game_over = pg.mixer.Sound(self.ruta + 'game_over.mp3')
        self.ganar = pg.mixer.Sound(self.ruta + 'win.mp3')

    def poner_musica(self):
        """ Método para mandar llamar a la música """
        pg.mixer.music.load(self.ruta + 'music_jungle.mp3')
        pg.mixer.music.play(-1)



