__author__ = 'ivania'
from collections import deque
from random import gauss, randint, triangular
from enum import Enum


class Menu(Enum):
    plato_fondo = 1
    plato_mas_jugo = 2
    plato_mas_postre_y_jugo = 3

    def tiempo_preparacion(self):
        if self == Menu(1):
            return 5
        elif self == Menu(2):
            return 7
        else:
            return 9


class Habilidad(Enum):
    principiante = 1
    intermedia = 2
    avanzada = 3

    def tiempo_atencion(self):
        if self== Habilidad.principiante: # es igual que hacer Habilidad(1)
            return 3
        elif self == Habilidad.intermedia:
            return 2
        else:
            return 1


class Caja:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        self.cliente_actual = None
        self.tiempo_atención = 0

    def ocupada(self):
        return self.cliente_actual is not None

    def atender_cliente(self, cliente):
        self.cliente_actual = cliente
        self.tiempo_atención = cliente.cantidad_productos * self.habilidad.tiempo_atencion() \
                               + cliente.Menu.tiempo_preparacion()

    def __repr__(self):
        return 'Caja habilidad: {0}' \
               '\n\tCliente actual: {1}' \
               '\n\tTiempo de atención: {2}'.format(self.habilidad.name, self.cliente_actual.id, self.tiempo_atención)


class Cliente:
    low = 2
    high = 25
    mode = 10
    def __init__(self, _id, tiempo_llegada, cantidad_productos=1):
        self.id = _id
        self.cantidad_productos = cantidad_productos
        self.Menu = Menu(randint(1, 3))

        self.tiempo_maximo_espera = int(triangular(Cliente.low, Cliente.high, Cliente.mode))
        self.tiempo_llegada = tiempo_llegada  # Momento en que llega
        self.tiempo_salida = 0  # Momento en que sale
        self.tiempo_atencion = 0  # Momento en que lo atienden

    def tiempo_espera(self, tiempo_actual):
        if self.tiempo_salida == 0:  # No ha sido atendido
            return tiempo_actual - self.tiempo_llegada
        elif self.tiempo_atencion == 0:  # Se fue antes de ser atendido
            return self.tiempo_salida - self.tiempo_llegada
        else:  # Fue atendido
            return self.tiempo_atencion - self.tiempo_llegada

    def aburrido(self, tiempo_actual):
        if self.tiempo_espera(tiempo_actual) > self.tiempo_maximo_espera:
            return True
        else:
            return False

    def __repr__(self):
        return 'Cliente {0}' \
               '\n\tCantidad de productos: {1} ' \
               '\n\tTiempo de espera máximo: {2}' \
               '\n\tTiempo de espera: {3}' \
               '\n\tMenu: {4}'.format(self.id, self.cantidad_productos, self.tiempo_maximo_espera,
                                               self.tiempo_espera(TIEMPO_ACTUAL), self.Menu.name)


class RestoUniversitario:
    avg = 2
    std_dev = 1
    def __init__(self, habilidad):
        self.caja = Caja(Habilidad(habilidad))
        self.llegada_proximo_cliente = 0 # Momento en que llega el próximo cliente
        self.termina_cliente_actual = 0 # Momento en que termina el cliente actual

        self.clientes_id = 0

        self.clientes = deque()
        self.clientes_atendidos = []
        self.clientes_no_atendidos = []
        global TIEMPO_ACTUAL

    def calcular_llegada_prox_cliente(self):
        self.llegada_proximo_cliente = TIEMPO_ACTUAL + int(gauss(resto.avg, resto.std_dev))

    def get_clientes_id(self):
        self.clientes_id += 1
        return self.clientes_id

    def aburrido(self):
        global TIEMPO_ACTUAL
        if self.tiempo_espera(TIEMPO_ACTUAL) > self.tiempo_maximo_espera:
            return True
        else:
            return False

    def run(self, tiempo_max_simulacion):

        global TIEMPO_ACTUAL
        while True:
            '''actualizamos el tiempo de simulación'''
            if (not self.caja.ocupada()) \
                    or (self.caja.ocupada() and self.llegada_proximo_cliente < self.termina_cliente_actual):
                TIEMPO_ACTUAL = self.llegada_proximo_cliente
            else:
                TIEMPO_ACTUAL = self.termina_cliente_actual
            ''' Chequea que el tiempo de simulación no supere el tiempo máximo de simulación'''
            if TIEMPO_ACTUAL > tiempo_max_simulacion: break

            print('[SIMULACION] tiempo: {0} min'.format(TIEMPO_ACTUAL))

            ''' Revisamos los eventos de la simulación'''

            ''' 0. Clientes se aburren (o se han aburrido de esperar de esperar '''
            clientes_aburridos = list(filter((lambda x: x.aburrido(TIEMPO_ACTUAL)), self.clientes))
            if len(clientes_aburridos) > 0:
                print("[Clientes aburridos]", end=' ')
                for cliente_aburrido in clientes_aburridos:
                    self.clientes.remove(cliente_aburrido)
                    print(cliente_aburrido.id, end=' ')
                    cliente_aburrido.tiempo_salida = TIEMPO_ACTUAL
                print('\n', end='')
            self.clientes_no_atendidos.extend(clientes_aburridos)

            ''' 1. llegan más clientes. Esto ocurre ssi el tiempo de simulación corresponde al de la llegada de un cliente '''
            if TIEMPO_ACTUAL == self.llegada_proximo_cliente:
                self.clientes.append(Cliente(self.get_clientes_id(),TIEMPO_ACTUAL))
                self.calcular_llegada_prox_cliente()
                print('[LLEGADA]Llega {0} en tiempo simulación: {1} min.'.format(self.clientes[-1].id, TIEMPO_ACTUAL))
                print(self.clientes[-1])
            else:
                ''' 2. Terminamos de atender a un cliente '''
                cliente = self.caja.cliente_actual
                cliente.tiempo_salida = self.termina_cliente_actual  # Hay que actualizar los parámetros del cliente
                self.caja.cliente_actual = None
                self.clientes_atendidos.append(cliente)
                print('[SALIDA]Termina cliente:')
                print(cliente)
            ''' 3. Si la caja está vacía atendemos '''
            if not self.caja.ocupada():
                if len(self.clientes) > 0:
                    cliente = self.clientes.popleft()  # Obtenemos el cliente
                    self.caja.atender_cliente(cliente)  # Lo atienden!
                    cliente.tiempo_atencion = TIEMPO_ACTUAL
                    self.termina_cliente_actual = TIEMPO_ACTUAL + self.caja.tiempo_atención  # La simulación necesita saber cuando va a terminar
                    print('[ATENCIÓN]')
                    print(self.caja)



TIEMPO_ACTUAL = 0

resto = RestoUniversitario(Habilidad.avanzada)
resto.run(100)

print("ATENDIDOS")
for c in resto.clientes_atendidos:
    print(c.id, end=' ')
    print("tiempo de espera " + str(c.tiempo_espera(TIEMPO_ACTUAL)))

print("EN COLA")
for c in resto.clientes:
    print(c.id, end=' ')
    print("tiempo de espera " + str(c.tiempo_espera(TIEMPO_ACTUAL)))

print("NO ATENDIDOS")
for c in resto.clientes_no_atendidos:
    print(c.id, end=' ')
    print("tiempo de espera " + str(c.tiempo_espera(TIEMPO_ACTUAL)))






