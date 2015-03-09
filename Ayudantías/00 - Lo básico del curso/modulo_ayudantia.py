__author__ = "jecastro1"

variable_misteriosa = 0
print("Este es el peor módulo de la vida, pero les va a servir para entender")


def acerca_de():
    print("Este es un módulo programado por",
          __author__, "para la ayudantía 0")


class ObjetoCualquiera:

    objects_created = 0

    def __init__(self, saved):
        self.saved = saved
        objects_created = objects_created + 1

    def get_saved(self):
        return self.saved
