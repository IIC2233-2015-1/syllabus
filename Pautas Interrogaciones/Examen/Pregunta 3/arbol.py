__author__ = 'ivania', 'belén'

import random


class Arbol:
    def __init__(self, f=None, l=None, r=None, d=None, u=None, ancestros={}):
        self.nombre = f
        self.hijos = {'l': l, 'r': r, 'd': d, 'u': u}
        self.ancestros = ancestros

    def agregar_rama(self, rama, hijo):
        self.hijos[rama] = hijo

    def get_ancestros(self):
        result = []
        for a in self.ancestros:
            result.append(a.nombre)
        return result

    def __repr__(self):
        return "{0}".format(self.nombre)

    def print(self, num):
        print(" " * num + "fantasma {0} {1}".format(self.nombre, self.ancestros))
        for hijo in self.hijos:
            if self.hijos[hijo] is not None:
                print(" " * num + "{0}: ".format(hijo))
                self.hijos[hijo].print(num + 1)


def crear_arbol(fantasma, num_hijos):
    moves = ['l', 'r', 'd', 'u']
    key = random.choice(moves)
    moves.remove(key)
    elegibles = seleccionar_elegibles(fantasma.get_ancestros())
    if fantasma.nombre in elegibles:
        elegibles.remove(fantasma.nombre)
    for i in range(4):
        if len(elegibles) > 0 and num_hijos > 0:
            f = Arbol(random.choice(elegibles), ancestros=fantasma.ancestros.copy())
            f.ancestros.update({fantasma: key})
            fantasma.hijos[key] = f
            if num_hijos - 1 >= 0:
                crear_arbol(f, num_hijos - 1)
        else:
            fantasma.nombre = random.choice(['l', 'r', 'd', 'u'])
        key = random.choice(moves)


def seleccionar_elegibles(ancestros):
    return list((set(fantasmas) - set(ancestros)))

fantasmas = [i for i in range(10)]

