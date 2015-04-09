__author__ = 'mabucchi'


# La idea de esta actividad es poder escribir clases tal como
# si fuesen formularios. Esto implica forzar el tipado de los atributos

# e.g

# class Prueba(metaclass=Meta):
#     attr1 = int
#     attr2 = str

# esto forzaría a attr1 a ser int y a attr2 a ser str


# INICIO SOLUCION #

def create_property(name, _type):
    '''Crea un property para un atributo con nombre 'name' y que
    fuerza el tipo del atributo a '_type'.'''

    def getter(self):
        '''Retorna el atributo del objeto o None si es que no existe'''
        return self.__dict__.get(name)

    def setter(self, val):
        '''Solo permite setear el valor si es que es del tipo correcto'''
        if isinstance(val, _type):
            self.__dict__[name] = val
        else:
            print('ERROR: Se esperaba un valor de tipo {}'.format(_type))

    return property(getter, setter)


class Meta(type):

    def __new__(cls, clsname, bases, clsdict):

        # Recorre el diccionario de la clase buscando los atributos que
        # tienen asociados un tipo
        for key, val in clsdict.items():

            if isinstance(val, type):
                # cambia el contenido de ese atributo a un property
                clsdict[key] = create_property(key, val)

        return super().__new__(cls, clsname, bases, clsdict)


class Person(metaclass=Meta):
    name = str
    age = int


class Company(metaclass=Meta):
    name = str
    stock_value = float
    employees = list


# FIN SOLUCION #

c = Company()
c.name = 'Apple'
c.stock_value = 125.78
c.employees = ['Tim Cook', 'Kevin Lynch']

print(c.name, c.stock_value, c.employees, sep=', ')

p = Person()
p.name = 'Karim'
p.age = 'hola'
# Esto debiese imprimir 'ERROR'

print(p.name, p.age, sep=', ')


# CÓDIGO ADICIONAL!! #
print('\n------------------\nPARTE DOS\n')

# Acá se logra lo mismo que arriba y además se
# implementa la funcionalidad de poder instanciar la clase con los
# argumentos necesarios desde un principio
# Esto es lo deseable en la realidad

# eg:
# p = Person('Marco', 20)


from collections import OrderedDict


class MetaOpt(type):

    @classmethod
    def __prepare__(metacls, name, bases):
        '''Construye la clase sobre un OrderedDict en vez de un
        diccionario común'''
        return OrderedDict()

    def __new__(cls, clsname, bases, clsdict):

        # Guarda los nombres de atributos para poder construir la función
        # '__call__'
        attributes = list()

        for key, val in clsdict.items():
            if isinstance(val, type):
                attributes.append(key)
                clsdict[key] = create_property(key, val)

        # Guarda los nombres de los atributos en la clase
        cls._attributes = attributes

        return super().__new__(cls, clsname, bases, dict(clsdict))

    def __call__(cls, *args, **kwargs):
        # llama al '__call__' de type para crear el nuevo objeto
        obj = super().__call__()

        # Asocia los 'args' a los nombres de los atributos de la clase
        for key, value in zip(cls._attributes, args):
                # setea el valor de los atributos en el objeto creado
            setattr(obj, key, value)
        return obj


# La idea es poder escribir las clases de la siguiente forma y que
# esto establezca el tipo de las variables


class Person(metaclass=MetaOpt):
    name = str
    age = int
    gender = str
    friends = tuple


p1 = Person('Marco', 20, 'male', ('Belen', 'Pato', 'Jaime', 'Rodrigo'))

print(p1.name, p1.age, p1.gender, p1.friends, sep='\n')
