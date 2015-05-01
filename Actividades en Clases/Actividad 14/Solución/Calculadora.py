import enum
from math import e, pi

__author__ = 'Ivania Donoso'


# Debes tener Python3 para usar Enumeraciones.
class Operaciones(enum.Enum):
    suma = ('+', 'plus')
    resta = ('-', 'minus')
    multiplicacion = ('*', 'times')
    division = ('/', 'divided')
    modulo = ('%', 'module')

    def encontrar_operacion(operacion_str):
        for operacion in Operaciones:
            if operacion.value[0] == operacion_str:
                return operacion

    def is_operacion(value):
        for operacion in Operaciones:
            if operacion.value[0] == value:
                return True
        return False


def index_generator(n):
    for i in range(n):
        yield i


class Calculadora:

    def __init__(self, letras_especiales):
        self.letras_especiales = letras_especiales

    def encontrar_operaciones(self, declaracion):
        operaciones = []
        operandos = []
        last = 0
        for i in range(len(declaracion)):
            if Operaciones.is_operacion(declaracion[i]):
                operandos.append(declaracion[last:i])
                operaciones.append(declaracion[i])
                last = i + 1
        if last != len(declaracion):
            operandos.append(declaracion[last:])
        return operaciones, operandos

    def leer_operaciones(self, declaracion):
        declaracion = declaracion.replace(' ', '')
        operaciones, operandos = self.encontrar_operaciones(declaracion)
        index_operandos = index_generator(len(operandos))
        operador1 = self.valor_en_numeros(
            operandos[next(index_operandos)], declaracion)
        for operacion_actual in operaciones:
            try:
                operador2 = self.valor_en_numeros(
                    operandos[next(index_operandos)], declaracion)
            except StopIteration:
                print('[ERROR] {0}'.format(StopIteration.__name__))
                print('Falta un operador en {0}'.format(declaracion))
            else:
                operacion = Operaciones.encontrar_operacion(operacion_actual)
                resultado = self.realizar_operacion(
                    operador1, operador2, operacion, declaracion)
                operador1 = resultado

    def realizar_operacion(self, operador1, operador2, operacion, declaracion):
        try:
            if operacion is Operaciones.suma:
                resultado = operador1 + operador2
            elif operacion is Operaciones.resta:
                resultado = operador1 - operador2
            elif operacion is Operaciones.multiplicacion:
                resultado = operador1 * operador2
            elif operacion is Operaciones.division:
                try:
                    resultado = operador1 / operador2
                except ZeroDivisionError:
                    print('[ERROR] {0}'.format(ZeroDivisionError.__name__))
                    resultado = 'infinito'
            else:
                resultado = operador1 % operador2
            print('{0} {1} {2} es igual a {3}'.format(
                operador1, operacion.value[1], operador2, resultado))
            return resultado
        except:
            print('No se ha realizado la operacion {0}'.format(declaracion))

    def valor_en_numeros(self, numero_letra, declaracion):

        if numero_letra.isdigit():
            return int(numero_letra)

        elif numero_letra.isalpha():
            try:
                v = self.letras_especiales[numero_letra]
            except KeyError:
                print('[ERROR] {0}'.format(KeyError.__name__))
                print(('\'{0}\' no tiene valores asignados.'
                       'Debe agregarla antes de usarla.').format(
                    numero_letra))
            else:
                return v

        elif Calculadora.isfloat(numero_letra):
            return float(numero_letra)

        else:
            print(('[ERROR] La sintaxis de \'{0}\' es incorrecta. '
                   'Lea el manual para mas informacion.').format(declaracion))

    def isfloat(s):
        try:
            float(s)
            return True
        except ValueError:
            print('[ERROR] {0}'.format(ValueError.__name__))
            print('\'{0}\' no puede castearse a float'.format(s))
            return False

    def agregar_letra(self, letra, valor):
        try:
            v = self.letras_especiales[letra]
        except KeyError:
            self.letras_especiales[letra] = valor
        else:
            print('[ERROR] {0}'.format(KeyError.__name__))
            print(('La letra \'{0}\' no sera agregada. '
                   'Ya existe dentro de la calculadora.').format(letra))


# NO PUEDE MODIFICAR ESTO.
letras_especiales = {'g': 9.81, 'e': e, 'pi': pi}
calculadora = Calculadora(letras_especiales)
operaciones_testeadas = ['3+5', 'g*3', 'pi*4', '76 /2 + 35 / 5']
calculadora.agregar_letra('g', 5757)
print('')
operaciones_por_testear = ['1/0', 'a+2', 'g+0', '88/2+0+', '1=2', '8.953 + 1']
for operaciones in operaciones_por_testear:
    calculadora.leer_operaciones(operaciones)
    print('')
