from random import randint, choice
from MetaClases import *

__author__ = 'figarrido'


NOMBRES = ['Karim', 'Christian', 'Belen', 'Patricio', 'Jaime',
           'Marco', 'Rodrigo', 'Felipe', 'Antonio', 'Ian']

TAREAS = ['Hacer el papeleo', 'Depositar los sueldos',
          'Descansar', 'Comer', 'Tomar cafe',
          'Organizar la reunion', 'Agregar datos al sistema',
          'Jugar con las sillas', 'Revisar CV\'s',
          'Marcar entrada']


class Empresa(metaclass=MetaEmpresa):

    def __init__(self, boss):
        self.boss = boss
        self.empleados = {}


class Persona(metaclass=MetaPersona):

    def __init__(self, nombre, edad, **kwargs):
        super().__init__(**kwargs)
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return '{} is {} years old'.format(self.nombre, self.edad)


class Empleado(Persona):

    id_actual = 0

    def __init__(self, sueldo, **kwargs):
        super().__init__(**kwargs)
        self.sueldo = sueldo
        self.id_empleado = Empleado.id_actual
        Empleado.id_actual += 1
        self.tareas_realizadas = []

    def __str__(self):
        return super().__str__() + '\nID: {} - Sueldo: {}'.format(self.id_empleado, self.sueldo) + '\n'


class Jefe(Empleado):

    def __init__(self, **kwargs):
        self.password = 'Tu jefecito lindo'
        super().__init__(**kwargs)

if __name__ == '__main__':

    System = Empresa(Jefe(nombre='Pedro', edad=30, sueldo=1000000))

    """
    Agrega 10 empleados en la empresa
    """
    for _ in range(10):
        System.nuevo_empleado(Empleado(nombre=NOMBRES[_], edad=randint(20, 40),
                                       sueldo=randint(500000, 800000)))
    """
    Muestra a los empleados
    """
    for ID in System.empleados:
        print(System.empleados[ID])

    """
    Elige al azar al empleado del mes
    """
    empleado_del_mes = System.empleados[choice(list(System.empleados))]

    System.subir_sueldo(empleado_del_mes.id_empleado, 'Tu jefecito lindo')

    print('El empleado del mes es: {} y su sueldo quedo en ${}\n'.format(
        empleado_del_mes.nombre, empleado_del_mes.sueldo))

    """
    A cada empleado le asigna una tarea
    """
    for ID in System.empleados:
        System.empleados[ID](choice(TAREAS))

    print(Empresa(empresa=System))
