from threading import Thread
from time import sleep


def funcion(n):
    i = 0
    while i < n:
        print(i)
        sleep(.5)
        i += 1

t1 = Thread(target=funcion, args=(10,))
t2 = Thread(target=funcion, args=(15,))

t1.daemon = True
t2.daemon = True

t1.start()
t1.join()

t2.start()
