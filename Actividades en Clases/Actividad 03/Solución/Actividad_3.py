#Polimorfismo + properties
__author__ = ('bcsaldias', 'mabucchi')


class Espacio:

    def __init__(self, ancho, largo, max_p):
        self._ancho = ancho
        self._alto = 2
        self._largo = largo
        self._max_personas = max_p
        self._personas_dentro = 0

    @property
    def area(self):
        return self._ancho * self._largo

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __add__(self, other):
        print("imposible unir espacios")


class EspacioConAsientos(Espacio):

    def __init__(self, asientos, *args, **kwargs):
        super(EspacioConAsientos, self).__init__(*args, **kwargs)
        self.asientos = asientos
        self.asientos_disponibles = asientos

    def __add__(self, other):
        if not (type(self) is type(other)):
            print("Imposible unir espacios")
            return

        n_ancho = self._ancho + other._ancho
        n_largo = self._largo + other._largo
        n_max_personas = self._max_personas + other._max_personas
        n_asientos = self.asientos + other.asientos

        obj = type(self)(n_asientos, n_ancho, n_largo, n_max_personas)
        template = '{} ancho: {}, largo: {}, alto: {}, max_personas: {}, asientos: {}'

        for op, espacio in [(' ', self), ('+', other), ('=', obj)]:
            print(template.format(op, espacio._ancho, espacio._largo,
                                  espacio._alto, espacio._max_personas, espacio.asientos))
        return obj

    def __lt__(self, other):
        if isinstance(other, EspacioConAsientos):
            return self.asientos < other.asientos
        return self.area < other.area

    def __gt__(self, other):
        if isinstance(other, EspacioConAsientos):
            return self.asientos > other.asientos
        return self.area > other.area


class SalaDeClases(EspacioConAsientos):

    def __init__(self, *args, **kwargs):
        print("Sala de clases creada")
        super(SalaDeClases, self).__init__(*args, **kwargs)


class SalaDeReuniones(EspacioConAsientos):

    def __init__(self, *args, **kwargs):
        print("Sala de reuniones creada")
        super(SalaDeReuniones, self).__init__(*args, **kwargs)


class Subterraneo(Espacio):

    def __init__(self, *args, **kwargs):
        print("Subterraneo creado")
        super(Subterraneo, self).__init__(*args, **kwargs)


class Persona:

    def __init__(self, nombre):
        self._nombre = nombre

    def entrar_a_sala(self, sala):
        print('{} entra a la sala {}/{} {}/{}'.format(self._nombre,
                                                      sala.asientos_disponibles,
                                                      sala.asientos,
                                                      sala._personas_dentro,
                                                      sala._max_personas))


class Alumno(Persona):

    def entrar_a_sala(self, sala):
        if sala._personas_dentro < sala._max_personas:
            if isinstance(sala, EspacioConAsientos) and sala.asientos_disponibles > 0:
                sala.asientos_disponibles -= 1
                sala._personas_dentro += 1
                super(Alumno, self).entrar_a_sala(sala)
            elif not isinstance(sala, EspacioConAsientos):
                sala._personas_dentro += 1
                print(self._nombre, "entra a la sala")
        else:
            print(self._nombre, "NO entra a la sala")


class Profesor(Persona):

    def entrar_a_sala(self, sala):
        if sala._personas_dentro < sala._max_personas:
            if isinstance(sala, SalaDeReuniones) and sala.asientos_disponibles > 0:
                sala.asientos_disponibles -= 1
            sala._personas_dentro += 1
            super(Profesor, self).entrar_a_sala(sala)
        else:
            print(self._nombre, "NO entra a la sala")
