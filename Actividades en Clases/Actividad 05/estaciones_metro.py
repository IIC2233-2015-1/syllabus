from enum import Enum

__author__ = ['belen_saldias', 'patricio_lopez']


class Direccion(Enum):
    """
    Una enumeración es como "números con nombre"
    Se utiliza así: dir = Direccion.arriba
    """
    izquierda = 1
    arriba = 2
    derecha = 3
    abajo = 4


class Estacion:

    def __init__(self, numero):
        self.numero = numero
        self.direcciones = {Direccion.izquierda: None,
                            Direccion.arriba: None,
                            Direccion.derecha: None,
                            Direccion.abajo: None}

    @property
    def izquierda(self):
        return self.direcciones[Direccion.izquierda]

    @property
    def arriba(self):
        return self.direcciones[Direccion.arriba]

    @property
    def derecha(self):
        return self.direcciones[Direccion.derecha]

    @property
    def abajo(self):
        return self.direcciones[Direccion.abajo]

    def __repr__(self):
        return "Estacion {}".format(self.numero)


class MapaMetro:

    def __init__(self, numero_estaciones):
        self.estaciones = [Estacion(str(i)) for i in range(numero_estaciones)]

    def __unir_izquierda(self, tuplas_caminos):
        self.__unir_tuplas(tuplas_caminos, Direccion.izquierda)

    def __unir_arriba(self, tuplas_caminos):
        self.__unir_tuplas(tuplas_caminos, Direccion.arriba)

    def __unir_derecha(self, tuplas_caminos):
        self.__unir_tuplas(tuplas_caminos, Direccion.derecha)

    def __unir_abajo(self, tuplas_caminos):
        self.__unir_tuplas(tuplas_caminos, Direccion.abajo)

    def __unir_tuplas(self, tuplas, direccion):
        """ Dada una lista de tuplas, hacemos las conexiones """

        for i, (numero_origen, numero_destino) in enumerate(tuplas):
            estacion_origen = self.estaciones[numero_origen]
            estacion_destino = self.estaciones[numero_destino]
            estacion_origen.direcciones[direccion] = estacion_destino

    @property
    def primera_estacion(self):
        return self.estaciones[0]

    @property
    def ultima_estacion(self):
        return self.estaciones[-1]

    @classmethod
    def mapa_de_ejemplo(cls):
        """
        Este métodos estático nos permite instanciar
        un objeto del tipo "cls", en este caso del tipo 'MapaMetro'
        """

        ESTACIONES_EJEMPLO = 20

        mapa = cls(ESTACIONES_EJEMPLO)

        # Entregamos las tuplas que representan los caminos

        mapa.__unir_izquierda([(3, 2),
                               (6, 5),
                               (8, 7),
                               (11, 10),
                               (12, 11),
                               (13, 12),
                               (14, 13),
                               (17, 16),
                               (19, 18)])
        mapa.__unir_derecha([(0, 1),
                             (1, 2),
                             (3, 4),
                             (6, 7),
                             (8, 9),
                             (15, 16),
                             (17, 18)])
        mapa.__unir_arriba([(5, 0),
                            (6, 1),
                            (11, 6),
                            (16, 11),
                            (8, 3),
                            (13, 8),
                            (18, 13),
                            (9, 4),
                            (14, 9),
                            (19, 14)])
        mapa.__unir_abajo([(5, 10),
                           (10, 15),
                           (2, 7),
                           (7, 12),
                           (12, 17)])
        return mapa
