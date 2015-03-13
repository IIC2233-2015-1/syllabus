class Bodega:

    def __init__(self):
        self.objetos = []

    def agregar(self, objeto):
        self.objetos.append(objeto)

    def mostrar_descripciones(self):
        for obj in self.objetos:
            obj.descripcion()
            print("-" * 20)


# Para poder recorrer todos los __mro__ necesito llegar a una clase que
# "pare" este recorrido (que no sea object, sino se cae)

class Objeto:

    def __init__(self, peso, volumen, **kwargs):
        self.peso = peso
        self.volumen = volumen

    def descripcion(self):
        print("{} {}".format(self.peso, self.volumen))


# Categorías

class Electronicos(Objeto):

    def __init__(self, voltaje, consumo, **kwargs):
        super().__init__(**kwargs)
        self.voltaje = voltaje
        self.consumo = consumo

    def descripcion(self):
        super().descripcion()
        print("{} {}".format(self.voltaje, self.consumo))


class Comestibles(Objeto):

    def __init__(self, calorias, **kwargs):
        super().__init__(**kwargs)
        self.calorias = calorias

    def descripcion(self):
        super().descripcion()
        print(self.calorias)


class Vestibles(Objeto):

    def __init__(self, talla, material, **kwargs):
        super().__init__(**kwargs)
        self.talla = talla
        self.material = material

    def descripcion(self):
        super().descripcion()
        print("{} {}".format(self.talla, self.material))


class DeLujo(Objeto):

    def __init__(self, costo, **kwargs):
        super().__init__(**kwargs)
        self.costo = costo

    def descripcion(self):
        super().descripcion()
        print(self.costo)


class Ilicitos(Objeto):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def descripcion(self):
        super().descripcion()
        print("ALERTA")


class Domesticos(Objeto):

    def __init__(self, resena, **kwargs):
        super().__init__(**kwargs)
        self.resena = resena

    def descripcion(self):
        super().descripcion()
        print(self.resena)


class ObrasDeArte(Objeto):

    def __init__(self, nombre, autor, ano, **kwargs):
        super().__init__(**kwargs)
        self.nombre = nombre
        self.autor = autor
        self.ano = ano

    def descripcion(self):
        super().descripcion()
        print("{} {} {}".format(self.nombre, self.autor, self.ano))


# Objetos categorizados

class MonaLisaRobada(ObrasDeArte, Ilicitos):

    def __init__(self):
        super().__init__(nombre="Mona Lisa",
                         autor="Da Vinci",
                         ano="1495",
                         volumen="200 cc",
                         peso="3 kg")

    def descripcion(self):
        super().descripcion()


class AbrigoPiel(Vestibles, Ilicitos):

    def __init__(self):
        super().__init__(talla="42",
                         material="Cuero de animal en peligro",
                         volumen="200 cc",
                         peso="1 kg")

    def descripcion(self):
        super().descripcion()


class JarronChino(ObrasDeArte, Domesticos, DeLujo):

    def __init__(self):
        super().__init__(nombre="Jarro de Yao Ming",
                         autor="Doctor Ming",
                         ano="963 d.C",
                         resena="Un valioso jarro de la antigua China",
                         costo="CLP$ 10.000.000",
                         volumen="5L",
                         peso="10 kg")

    def descripcion(self):
        super().descripcion()


class AppleWatchDorado(DeLujo, Vestibles, Electronicos):

    def __init__(self):
        super().__init__(costo="US$ 10000",
                         talla="Cualquiera",
                         material="oro",
                         voltaje="3.7 V",
                         consumo="0.1 Wh",
                         volumen="50 cc",
                         peso="30 gr")

    def descripcion(self):
        super().descripcion()


class PapasFritas(Comestibles):

    def __init__(self):
        super().__init__(calorias="300 cal",
                         volumen="50 L",
                         peso="50 kg")

    def descripcion(self):
        super().descripcion()


class Refrigerador(Electronicos, Domesticos):

    def __init__(self):
        super().__init__(resena="Inventado por el hombre "
                         "para uno de sus grandes problemas",
                         voltaje="220 V",
                         consumo="0.1 Wh",
                         volumen="400L",
                         peso="100 kg")

    def descripcion(self):
        super().descripcion()


if __name__ == '__main__':
    bodega = Bodega()
    mona_lisa = MonaLisaRobada()
    bodega.agregar(mona_lisa)
    abrigo = AbrigoPiel()
    bodega.agregar(abrigo)
    jarron = JarronChino()
    bodega.agregar(jarron)
    apple_watch = AppleWatchDorado()
    bodega.agregar(apple_watch)
    papas = PapasFritas()
    bodega.agregar(papas)
    refri = Refrigerador()
    bodega.agregar(refri)
    bodega.mostrar_descripciones()
