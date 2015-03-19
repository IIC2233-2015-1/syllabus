__author__ = 'patricio_lopez'


class Paquete:
    paquetes_id = 0

    def __init__(self):
        Paquete.paquetes_id += 1
        self.id = Paquete.paquetes_id
        self.botellas = []

    def agregar_botella(self, botella):
        self.botellas.append(botella)

    def agregar_botellas(self, botellas):
        self.botellas.extend(botellas)

    def ver_contenido(self):
        print("----------------------")
        print("Paquete #{}".format(self.id))
        for botella in self.botellas:
            print(botella)
