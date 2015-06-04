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
    Tienen que programar este método
    """

    def run(self):
        while self.hp > 0 and self.vivo is True:
            time.sleep(8)
            if self.vivo is True:  # Puedee haber muerto mientras esperaba
                self.atacar()
        print("Termino la simulacion")

    """
    Les damos este método
    """

    def atacado(self, guerrero):
        self.hp -= guerrero.ataque
        if self.hp <= 0:
            self.vivo = False
            print("El Godzilla MURIO!!")
        else:
            print(
                "El Godzilla ha sido atacado! El guerrero le ha hecho " + str(
                    guerrero.ataque) + " de dano" +
                ". HP Godzilla " + str(self.hp))
            guerrero.atacado(int(guerrero.ataque / 4))

    """
    Tienen que programar este método
    """

    def atacar(self):
        for i in lista_guerreros:
            if i.vivo is True:
                i.atacado(3)


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
    Tienen que programar este método

    """

    def run(self):
        while self.hp > 0 and Godzilla.vivo is True:
            time.sleep(self.velocidad)
            if Godzilla.vivo is True:  # Puede haber muerto mientras esperaba
                Godzilla.atacado(self)

    """
    Les damos este método
    """

    def atacado(self, ataque):
        self.hp -= ataque
        print("El guerrero" + str(self.ID) +
              " ha sido danado!! HP " + str(self.hp))
        if self.hp <= 0:
            self.vivo = False
            print("El guerrero" + str(self.ID) + " ha muerto :( !!!")

    """
    Les damos este método
    """

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
    num_guerreros = 20  # int(input("Cuantos Guerreros tendra la simulacion?"))
    lista_guerreros = []
    Godzilla = Godzilla(1000)
    Godzilla.start()
    for i in range(num_guerreros):
        guerrero = Guerrero(Godzilla, random.randint(4, 20), 60, 30)
        guerrero.setDaemon(True)
        guerrero.start()
        lista_guerreros.append(guerrero)
