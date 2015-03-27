from math import sin, cos, exp
from matplotlib import pyplot as plt
import numpy as np
import itertools

__author__ = "karimpichara, carlossantander"


tipos_energias = ["solar", "eolica", "nuclear"]

TIEMPO = 1440  # Minutos de un día


def calcular_energia(tipo):

    def solar(t):
        t = t % TIEMPO
        if t < 360 or t >= 1080:
            return 1
        if t < 720:
            return cos(t)**2
        if t < 1080:
            return t / 360

    def eolica(t):
        t = t % TIEMPO
        if t < 720:
            return sin(t) / 3 + sin(3 * t) / 3 + 1 / 2
        return 1

    def nuclear(t):
        return 22 * exp(-0.05*t)

    # aquí retorno la función dependiendo del tipo que me pidan
    return locals()[tipo]


def integrar(T, n, tipo):
    func = calcular_energia(tipo)  # aquí obtenemos la función a utilizar
    t = 0.0
    integral = 0
    while (t < T + 1):
        integral += func(t) * 1 / n
        yield integral
        t += 1 / n


def tiempo_n(T, n):
    t = 0
    while t < T + 1:
        yield t
        t += 1 / n


if __name__ == '__main__':
    delta_t = TIEMPO / 3
    n = 10

    nomb = {tipo: [calcular_energia(tipo), integrar(
        TIEMPO, n, tipo)] for tipo in tipos_energias}

    energias = []

    t = []
    integ = {}
    for c in nomb:
        integ.update({c: []})
    T = tiempo_n(TIEMPO, n)
    while next(T) <= TIEMPO:
        t.append(next(T))
        for c in nomb:
            aux = next(nomb[c][1])
            integ.update({c: integ[c] + [aux]})

    base_colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    colors = itertools.cycle(base_colors)
    for c in nomb:
        plt.scatter(
            t, integ[c], c=next(colors), s=15, cmap=plt.cm.cool, edgecolors='None', label = c)

    plt.grid(True)
    plt.legend(loc='best', shadow=True, fontsize='small')
    plt.show()
