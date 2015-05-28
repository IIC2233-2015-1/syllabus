import threading
import time
import random

__author__ = 'Jm'


class Godzilla(threading.Thread):

    def __init__(self, hp):
        super().__init__()
        self.hp = hp
        self.vivo = True

    """
    Tienen que programar método run
    """

    def atacado(self, guerrero):
        self.hp -= guerrero.ataque
        if self.hp <= 0:
            self.vivo = False
            print("El Godzilla MURIO!!")
            self.terminate()
        else:
            print(
                "El Godzilla ha sido atacado! El " + guerrero.tipo +
                " le ha hecho " + str(guerrero.ataque) + " de dano" +
                ". HP Godzilla " + str(self.hp))
            guerrero.atacado(int(guerrero.ataque / 4))

    """
    Programar método atacar (el pasivo de Godzilla)
    """


class Guerrero(threading.Thread):

    def __init__(self, Godzilla, velocidad, hp, ataque):
        super().__init__()
        self.vivo = True
        self.Godzilla = Godzilla
        self.velocidad = velocidad
        self.hp = hp
        self.ID = next(Guerrero.get_i)
        self.ataque = ataque

    """
    Programar este método run

    """

    def atacado(self, ataque):
        self.hp -= ataque
        print("El guerrero" + str(self.ID) +
              " ha sido danado!! HP " + str(self.hp))
        if self.hp <= 0:
            self.vivo = False
            print("El guerrero" + str(self.ID) + " ha muerto :( !!!")

    def id_():
        i = 0
        while True:
            yield i
            i += 1

    get_i = id_()


if __name__ == "__main__":
    print("Comenzo la Simulacion!")

    """
    Tienen que programar el main completo
    """
