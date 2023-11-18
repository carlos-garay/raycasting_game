
class Checkpoint:
    """ Clase caretaker del memento que se encarga de controlar los estados del checkpoint """
    def __init__(self, juego):
        self.memento = None
        self.juego = juego  # Nuestro originator

    def crear_checkpoint(self):
        """ Guarda en la variable el estado del juego cuando se tome la bandera del chekpoint """
        self.memento = self.juego.guardar_estado()

    def cargar_checkpoint(self):
        """ Método para cargar el estado que se tiene guardado de vuelta al juego """
        if self.memento is None:
            self.juego.reiniciar_nivel()
            return

        self.juego.cargar_estado(self.memento)


