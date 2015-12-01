import threading
from time import sleep
from random import randint, random

__author__ = 'figarrido'

iden = 1


def catalogo():
    global iden
    a = 0
    mismo = iden
    print('Usuario-{} comenzo el proceso'.format(mismo))
    iden += 1
    while a < 5:
        print('Soy el usuario-{} usando el catalogo'.format(mismo))
        sleep(random() * randint(1, 3))
        a += 1
    print('Usuario-{} termino el proceso'.format(mismo))


class Vigilante:

    def __init__(self, C):
        self.C = C
        self.procesos = 0
        self.lock = threading.Lock()

    def vigilar(self):
        self.procesos += 1

        if self.procesos < self.C:
            catalogo()
        else:
            self.lock.acquire()
            catalogo()

        if self.lock.locked():
            self.lock.release()

        self.procesos -= 1


v = Vigilante(3)
threads = []
for _ in range(15):
    t = threading.Thread(target=v.vigilar, daemon=True)
    t.start()
    threads.append(t)
while True:
    if not any([i.isAlive() for i in threads]):
        break
