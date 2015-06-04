__author__ = ['Bastian','Jm']
import threading
import time
import random


class MegaGodzilla(threading.Thread):

    ###
    # Tienen que completar la clase (piensen en los locks necesarios)
    ###

    def __init__(self, hp):
        super().__init__()
        self.hp = hp

    @property
    def vivo(self):
        if self.hp > 0:
            return True
        return False

    ###
    # Tienen que programar el método run
    ###

    def atacado(self, soldado):
        self.hp -= soldado.ataque
        if not self.vivo:
            print("MegaGodzilla ha muerto!!")
        else:
            print(
                "Mega-Godzilla ha sido atacado! El soldado le ha hecho " + str(
                    soldado.ataque) + " de dano" +
                ". HP Godzilla " + str(self.hp))
            soldado.atacado(int(soldado.ataque / 4))

    ###
    # Programar método atacar
    ###


class Soldado(threading.Thread):

    ###
    # Tienen que completar la clase (piensen en los locks necesarios)
    ###

    def __init__(self, MegaGodzilla, velocidad, hp, ataque):
        super().__init__()
        self.MegaGodzilla = MegaGodzilla
        self.velocidad = velocidad
        self.hp = hp
        self.ID = next(Soldado.get_i)
        self.ataque = ataque

    @property
    def vivo(self):
        if self.hp > 0:
            return True
        return False

    ###
    # Tienen que programar el método run
    ###

    def atacado(self, ataque):
        self.hp -= ataque
        print("El soldado" + str(self.ID) +
              " ha sido danado!!  HP " + str(self.hp))
        if not self.vivo:
            print("El soldado" + str(self.ID) + " ha muerto :( !!!")

    def id_():
        i = 0
        while True:
            yield i
            i += 1

    get_i = id_()


if __name__ == "__main__":
    print("Comenzo la Simulacion!")

    ###
    # Tienen que programar el main completo
    ###
