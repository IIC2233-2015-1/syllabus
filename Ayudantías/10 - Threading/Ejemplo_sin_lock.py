from threading import Thread
from time import sleep
from random import random
import threading


productos = 0
t = 1


def agrega(name, to):
    global productos, t
    while True:
        # with lock:
        print('sumando...')
        sleep(1)
        productos += 1
        print(name, 'time: ', t, 'number: ', productos)

        t += 1
        sleep(random())


def quita(name, to):
    global productos, t
    while True:
        # with lock:
        if productos > 0:
            print('restando...')
            sleep(1)
            productos -= 1
            print(name, 'time: ', t, 'number: ', productos)

            t += 1
        sleep(random())

a = Thread(target=agrega, args=('Thread 1', 1))
a.daemon = True

b = Thread(target=quita, args=('Thread 2', 2))
b.daemon = True

print('___Started___')
print(threading.activeCount())
a.start()
b.start()
sleep(15)
print('Total', productos)
print(threading.activeCount())
print('___Finished___')
