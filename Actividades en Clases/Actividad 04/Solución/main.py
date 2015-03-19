from collections import deque
from collections import defaultdict
from paquete import Paquete
from botella import Botella

__author__ = 'patricio_lopez'


class Maquina:

    def procesar(self, linea_produccion_entrante):
        print("----------------------")
        print("La maquina {} comienza a trabajar.".format(
            self.__class__.__name__))


class Botellizamodulador(Maquina):

    def __init__(self):
        self.botellas_a_producir = 0

    def procesar(self, linea_produccion_entrante=None):
        super().procesar(linea_produccion_entrante)

        # Creamos la cola
        linea_produccion = deque()

        # Super simple :)
        while len(linea_produccion) != self.botellas_a_producir:
            if len(linea_produccion) == 0:
                linea_produccion.append(Botella())  # Botella normal
            elif len(linea_produccion) % 5 == 0:
                botella_anterior = linea_produccion[-1]
                linea_produccion.append(
                    Botella(litros=botella_anterior.litros * 3))
            elif len(linea_produccion) % 6 == 0:
                botella_anterior = linea_produccion[-1]
                botella_ante_anterior = linea_produccion[-2]
                linea_produccion.append(
                    Botella(litros=(botella_anterior.litros / 2 +
                                    botella_ante_anterior.litros * 4)))
            else:
                linea_produccion.append(Botella())  # Botella normal
        return linea_produccion


class LowFAT32(Maquina):

    def __init__(self):
        self.botellas_desechadas = []

    def desechar_botella(self, botella):
        self.botellas_desechadas.append(botella)

    def imprimir_botellas_desechadas(self):
        print("Se desecharon {} botellas".format(
            len(self.botellas_desechadas)))

    def procesar(self, linea_produccion_entrante):
        super().procesar(linea_produccion_entrante)

        # Creamos la cola
        linea_produccion = deque()

        # Super simple :)
        while len(linea_produccion_entrante) != 0:
            botella = linea_produccion_entrante.popleft()
            if len(linea_produccion) == 0:
                linea_produccion.append(botella)
            elif linea_produccion[-1].litros <= botella.litros:
                linea_produccion.append(botella)
            elif linea_produccion[0].litros >= botella.litros:
                linea_produccion.appendleft(botella)
            else:
                self.desechar_botella(botella)

        # Imprimimos
        self.imprimir_botellas_desechadas()
        return linea_produccion


class HashSoda9001(Maquina):

    def procesar(self, linea_produccion_entrante):
        super().procesar(linea_produccion_entrante)

        # Tenemos dos maneras de usar un Diccionario
        # Por defecto usaremos el defaultdict,
        # Sin embargo puedes cambiar esto a False
        # Para usar el dict normal.
        usar_default_dic = True

        if usar_default_dic:
            # Opción 1: Usar defaultdict (mejor)

            # Función que se llamará en ausencia de una pila
            # para una determinada key (litros)
            def crea_pilas():
                return []

            # Creamos el defaultdict con la función de recién
            pilas = defaultdict(crea_pilas)

            # Iteramos.
            while len(linea_produccion_entrante) != 0:
                botella = linea_produccion_entrante.popleft()
                pila = pilas[botella.litros]
                pila.append(botella)
            return pilas
        else:
            # Opción 2: Usar defaultdict
            pilas = dict()

            # Iteramos.
            while len(linea_produccion_entrante) != 0:
                botella = linea_produccion_entrante.popleft()

                # Tenemos que crear manualmente la pila.
                if botella.litros not in pilas:
                    pilas[botella.litros] = []

                pila = pilas[botella.litros]
                pila.append(botella)
            return pilas


class PackageManager(Maquina):

    def procesar(self, linea_produccion_entrante):
        paquetes = deque()
        for pila in linea_produccion_entrante.values():
            paquete = Paquete()
            paquete.agregar_botellas(pila)
            paquetes.append(paquete)
        return paquetes


class Fabrica:

    def __init__(self):
        self.botellizamodulador = Botellizamodulador()
        self.lowFAT32 = LowFAT32()
        self.hashSoda9001 = HashSoda9001()
        self.packageManager = PackageManager()

    def producir(self, numero_botellas):
        self.botellizamodulador.botellas_a_producir = numero_botellas
        producto = None
        for maquina in [self.botellizamodulador,
                        self.lowFAT32,
                        self.hashSoda9001,
                        self.packageManager]:
            producto = maquina.procesar(producto)
        return producto


if __name__ == "__main__":

    numero_botellas = 423

    fabrica = Fabrica()
    output = fabrica.producir(numero_botellas)
    print("----------------------")
    print("Para {} botellas, se producen {} paquetes".format(
        numero_botellas, len(output)))
    for paquete in output:
        paquete.ver_contenido()
    print("----------------------")
