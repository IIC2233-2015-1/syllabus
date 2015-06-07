import threading
import time
import random

__author__ = ['Bastian', 'Jm']


class MegaGodzilla(threading.Thread):
    lockgod = threading.Lock()

    def __init__(self, hp):
        super().__init__()
        self.hp = hp
        self.grito = False

    @property
    def vivo(self):
        if self.hp > 0:
            return True
        return False

    ###
    # Tienen que programar este método
    ###

    def run(self):
        while self.hp > 0 and self.vivo:
            tiempoataque = random.randint(3, 6)
            time.sleep(tiempoataque)
            if self.vivo:
                tipoataque = random.randint(0, 1)
                if tipoataque == 0 or self.grito:
                    # Puede haber muerto mientras esperaba
                    self.atacar(3)
                elif tipoataque == 1 and not self.grito:
                    self.grito = True
                    print("MEGA-GODZILLA: 1 , 2 ,3 MOMIA ES!!!")
                    self.cambiarestado()
                    self.atacar(6)

        print("Termino la simulacion")

    ###
    # Les damos este método
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
    # Tienen que programar estos métodos
    ###

    def cambiarestado(self, estado=False):
        for i in lista_soldados:
            if i.vivo:
                i.estado = estado
        if estado:
            self.grito = False

    def atacar(self, dano):
        for i in lista_soldados:
            if i.vivo:
                i.atacado(dano)


class Soldado(threading.Thread):
    locksold = threading.Lock()
    lockataque = threading.Lock()

    def __init__(self, MegaGodzilla, velocidad, hp, ataque):
        super().__init__()
        self.MegaGodzilla = MegaGodzilla
        self.velocidad = velocidad
        self.hp = hp
        self.estado = True
        self.ID = next(Soldado.get_i)
        self.ataque = ataque
        self.duracionataque = random.randint(1, 3)

    @property
    def vivo(self):
        if self.hp > 0:
            return True
        return False

    ###
    # Tienen que programar este método
    ###

    def run(self):
        while self.hp > 0 and MegaGodzilla.vivo:
            time.sleep(self.velocidad)
            Soldado.locksold.acquire()
            if not self.estado:
                time.sleep(10)
                print("WII NOS PODEMOS MOVER DE NUEVO")
                MegaGodzilla.cambiarestado(estado=True)
            if MegaGodzilla.vivo:
                Soldado.lockataque.acquire()
                MegaGodzilla.atacado(self)
                time.sleep(self.duracionataque)
                Soldado.lockataque.release()
            Soldado.locksold.release()

    ###
    # Les damos este método
    ###

    def atacado(self, ataque):
        self.hp -= ataque
        print("El soldado" + str(self.ID) +
              " ha sido danado!!  HP " + str(self.hp))
        if not self.vivo:
            print("El soldado" + str(self.ID) + " ha muerto :( !!!")

    ###
    # Les damos este método
    ###

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
    num_soldados = 20  # int(input("Cuantos Guerreros tendra la simulacion?"))
    lista_soldados = []
    MegaGodzilla = MegaGodzilla(1000)
    MegaGodzilla.start()
    for i in range(num_soldados):
        soldado = Soldado(MegaGodzilla, random.randint(4, 19), 60, 30)
        soldado.setDaemon(True)
        soldado.start()
        lista_soldados.append(soldado)
