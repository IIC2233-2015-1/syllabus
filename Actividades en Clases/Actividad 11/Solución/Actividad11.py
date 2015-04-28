from abc import ABCMeta, abstractmethod, abstractproperty
from math import pi, sqrt, cos, sin, asin

# Generador del bonus

def calcular_puntos(trasl, radius, angles):
    def generador(radius, angles):
        for k in angles:
            yield (radius * cos(k), radius * sin(k))

    points = list(generador(radius, angles))
    return list(map(lambda x: tuple([y + z for y, z in zip(x, trasl)]), points))

# Fin

class Figura(metaclass=ABCMeta):

    def __init__(self, center):
        self._center = center

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, value):
        self._center = value

    @abstractproperty
    def perimetro(self):
        pass

    @abstractproperty
    def area(self):
        pass

    @abstractmethod
    def crecer_area(self, veces):
        pass

    @abstractmethod
    def crecer_perimetro(self, cantidad):
        pass

    def trasladar(self, vector):
        self.center = tuple(map(lambda x, y: x + y, self.center, vector))

    def __repr__(self):
        return '{} - Perimetro: {:.2f}, Area: {:.2f}, Centro: {}'.format(type(self).__name__, self.perimetro, self.area, self.center)

    
    # Propiedades para el bonus (no es la única solución)

    @abstractproperty
    def dist_centro_vertice(self):
        pass

    @abstractproperty
    def angulos(self):
        pass

    @property
    def vertices(self):
        return calcular_puntos(self.center, self.dist_centro_vertice, self.angulos)

    # Fin

class Rectangulo(Figura):

    def __init__(self, a, b, center):
        super().__init__(center)
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value

    @property
    def perimetro(self):
        return 2 * (self._a + self._b)

    @property
    def area(self):
        return self._a * self._b

    def crecer_area(self, veces):
        self._a = self._a * sqrt(veces)
        self._b = self._b * sqrt(veces)

    def crecer_perimetro(self, cantidad):
        self._a = self._a + self._a * cantidad / (2 * (self._a + self._b))
        self._b = self._b + self._b * cantidad / (2 * (self._a + self._b))


    # Propiedades para el bonus (no es la única solución)

    @property
    def dist_centro_vertice(self):
        return sqrt(self.a**2 + self.b**2) / 2

    @property
    def angulos(self):
        angles = []
        angles.append(2 * asin(self.b / (2 * self.dist_centro_vertice)))
        angles.append(pi)
        angles.append(pi + 2 * asin(self.b / (2 * self.dist_centro_vertice)))
        angles.append(0)
        return angles

    # Fin


class TrianguloEquilatero(Figura):

    def __init__(self, l, center):
        super().__init__(center)
        self._l = l

    @property
    def l(self):
        return self._l

    @l.setter
    def l(self, value):
        self._l = value

    @property
    def perimetro(self):
        return 3 * self._l

    @property
    def area(self):
        return (self._l ** 2) * sqrt(3) / 4

    def crecer_area(self, veces):
        self._l = self._l * sqrt(veces)

    def crecer_perimetro(self, cantidad):
        self._l = self._l + cantidad / 3


    # Propiedades para el bonus (no es la única solución)

    @property
    def dist_centro_vertice(self):
        return self.l / sqrt(3)

    @property
    def angulos(self):
        angles = []
        angles.append(2 * pi / 3)
        angles.append(4 * pi / 3)
        angles.append(0)
        return angles

    # Fin


# Pequeña prueba. No obligatorio

if __name__ == '__main__':
    figuras = []
    figuras.append(TrianguloEquilatero(5, (0, 0)))
    figuras.append(Rectangulo(6, 8, (0, 0)))

    print(*figuras, sep = "\n")
    print("*" * 20)

    for i in figuras:
        i.crecer_perimetro(0)

    print(*figuras, sep = "\n")
    print("*" * 20)

    for i in figuras:
        i.crecer_area(1)

    print(*figuras, sep = "\n")
    print("*" * 20)

    print("Antes del traslado")
    for i in figuras:
        print(i.vertices)
    print("*" * 20)

    print("Después del traslado")
    for i in figuras:
        i.trasladar((2,-1))
        print(i.vertices)
    print("*" * 20)

    print(*figuras, sep = "\n")
    print("*" * 20)