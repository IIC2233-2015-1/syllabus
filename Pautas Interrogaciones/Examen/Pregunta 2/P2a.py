__author__ = 'figarrido'


def _promedio(datos):
    return sum(datos) / len(datos)


def _varianza(datos):
    prom = _promedio(datos)
    suma = 0
    for i in datos:
        suma += (i - prom)**2
    return suma / len(datos)


class Estrella:

    def __init__(self, clase, RA, DEC, id, observaciones=[]):
        self.clase = clase
        self.RA = RA
        self.DEC = DEC
        self.id = id
        self.observaciones = observaciones

    def get_brillos(self):
        return [i.brillo for i in self.observaciones]

    @property
    def promedio(self):
        brillos = self.get_brillos()
        return _promedio(brillos)

    @property
    def varianza(self):
        brillos = self.get_brillos()
        return _varianza(brillos)

    def agregar_observacion(self, observacion):
        self.observaciones.append(observacion)


class Observacion(object):

    def __init__(self, brillo, tiempo, error):
        self.brillo = brillo
        self.tiempo = tiempo
        self.error = error


class Field:

    def __init__(self, estrellas=[]):
        self.estrellas = estrellas

    def agregar_estrella(self, estrella):
        self.estrella.append(estrella)


class Cielo:

    def __init__(self, fields=[]):
        self.fields = fields

    def agregar_field(self, field):
        self.fields.append(field)
