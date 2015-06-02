from collections import deque
from random import uniform

__author__ = 'Javiera'


class Paradero:
    def __init__(self):
        self.cola = deque()


class Bus:
    def __init__(self, max_pasajeros):
        self.max_pasajeros = max_pasajeros

    def subir_pasajeros(self, paradero):
        num_pasajeros = min(self.max_pasajeros, len(paradero.cola))
        print("Se suben {} pasajeros".format(str(num_pasajeros)))
        self.pasajeros = deque(paradero.cola.popleft() for i in range(num_pasajeros))


class Pasajero():
    pass


class Simulacion:
    def __init__(self, tiempo_maximo):
        self.tiempo_maximo_sim = tiempo_maximo
        self.tiempo_simulacion = 0
        self.tiempo_prox_pasajero = uniform(0.5, 1)
        self.tiempo_prox_bus = uniform(15, 20)
        self.paradero = Paradero()
        self.bus = Bus(30)


    def bus_primero(self):
        print("Llega bus en tiempo: {}".format(str(self.tiempo_simulacion)))
        self.bus.subir_pasajeros(self.paradero)
        self.tiempo_prox_bus = self.tiempo_simulacion + uniform(15, 20)

    def pasajero_primero(self):
        print("Llega pasajero en tiempo: {}".format(str(self.tiempo_simulacion)))
        self.paradero.cola.append(Pasajero())
        self.tiempo_prox_pasajero = self.tiempo_simulacion + uniform(0.5, 1)

    def run(self):

        while self.tiempo_simulacion < self.tiempo_maximo_sim:
            primer_evento = min(self.tiempo_prox_pasajero, self.tiempo_prox_bus)
            self.tiempo_simulacion = primer_evento

            if primer_evento == self.tiempo_prox_pasajero:
                self.pasajero_primero()
            else:
                self.bus_primero()


if __name__ == '__main__':
    s = Simulacion(100)
    s.run()