__author__ = 'patricio_lopez'


class Botella:

    def __init__(self, litros=1):
        self.litros = litros

    @property
    def etiqueta(self):
        return "DCC-Cola"

    def beber(self):
        print("Deliciosa bebida {}".format(self.etiqueta))

    def __str__(self):
        return "{} de {} litros.".format(self.etiqueta, self.litros)
