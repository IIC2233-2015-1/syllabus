import simpy
import random


SIM_TIME = 500
C_CAJAS = 2
INTERVAL = 10
ATENCION = 15
PACIENCIA = [5, 10]
N_CLIENT = 100
NAMES = ["JUAN", "PATIWIS", "BELEN", "MARKIWIS", "KOKO", "JAIME"]


class Cola():

    def __init__(self, env, num):
        self.ncola = num
        self.cola = []
        self.env = env
        self.counter = simpy.Resource(env, capacity=1)
        self.tiempo = random.expovariate(1.0 / INTERVAL)

    def Agregar(self, cliente):
        self.cola.append(cliente)
        with self.counter.request() as req:
            result = yield req | self.env.timeout(int(cliente.paciencia))
            espera = self.env.now - cliente.llegada
            yield self.env.timeout(self.tiempo)
            print('{2}: {0} ha esperado {1} para ser atendido'.format(
                cliente.name, int(espera), int(self.env.now)))
            if req in result:
                yield self.env.timeout(int(random.expovariate(1 / ATENCION)))
                print('{1}: {0} ha salido de la {2}'.format(
                    cliente.name, int(self.env.now), self))
            else:
                print('{1}: {0} ha salido enojado de la {2}'.format(
                    cliente.name, int(self.env.now), self))
            self.cola.pop(0)

    def __repr__(self):
        return 'Caja {0}'.format(self.ncola)


class Banco():

    def __init__(self, env, ncajas):
        self.cajas = []
        self.env = env
        for i in range(ncajas):
            self.cajas.append(Cola(env, i))


class Cliente:

    def __init__(self, colas, env, i):
        self.env = env
        self.name = 'Cliente ' + str(i)
        self.llegada = env.now
        self.paciencia = random.uniform(PACIENCIA[0], PACIENCIA[1])
        print('{1}: {0} ha llegado al Banco'.format(self.name, self.llegada))
        self.env.process(self.ElegirCola(colas))

    def ElegirCola(self, colas):
        cola = min(colas, key=lambda x: len(x.cola))
        yield self.env.timeout(1)
        print('{2}: {0} ha entrado a {1}'.format(
            self.name, cola, self.env.now))
        self.env.process(cola.Agregar(self))


def costumer_generator(env, banco, intervalo):
    for i in range(N_CLIENT):
        yield env.timeout(int(random.expovariate(1.0 / INTERVAL)))
        c = Cliente(banco.cajas, env, i)


if __name__ == '__main__':
    print("Banco")
    env = simpy.Environment()
    banco = Banco(env, C_CAJAS)
    env.process(costumer_generator(env, banco, INTERVAL))

    env.run(until=SIM_TIME)
