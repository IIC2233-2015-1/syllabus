from datetime import date
from functools import reduce
__author__ = "jecastro1"
path = "jugadores.txt"


def leer_archivo():
    def splitter(line):
        return tuple(line.split(";"))

    def transform_to_int(foo):
        return tuple(map(int, foo))

    splitted = list(map(splitter, [line for line in open(path)]))
    tuplas = map(lambda foo: foo[0:5] + transform_to_int(foo[5:11]), splitted)
    return list(tuplas)


def se_llama_como_yo(lista):
    mi_nombre = ("Jaime", "Castro", "Retamal")

    def algun_dato_igual(tupla):
        return any(map(lambda foo1, foo2: foo1 == foo2, tupla, mi_nombre))

    return list(filter(algun_dato_igual, lista))


def chilenos_zurdos(lista):
    pais_pie = ("Chile", "izquierdo")
    return list(filter(lambda foo: foo[3:5] == pais_pie, lista))


def edades(lista):
    ano = date.today().year
    return list(map(lambda foo: foo[0:2] + (ano - foo[7],), lista))


def sub_17(lista):
    tuplas_edad = edades(lista)
    return list(filter(lambda foo: foo[2] <= 17, tuplas_edad))


def goleador(lista):
    def mayor_goleador(foo1, foo2):
        return foo1 if foo1[8] > foo2[8] else foo2

    return reduce(mayor_goleador, lista)


def mayor_riesgo_obesidad(lista):
    def imc(tupla):
        return (tupla[3] / (tupla[2] / 100) ** 2,)

    def max_imc(foo1, foo2):
        return foo1 if foo1[4] > foo2[4] else foo2

    # Vemos los chilenos
    seleccion = list(filter(lambda foo: foo[3] == 'Chile', lista))
    # Ocupamos solo ciertos campos
    proyeccion = list(map(lambda foo: foo[0:2] + foo[9:11], seleccion))
    # Añadimos los IMC
    tuplas_imc = list(map(lambda foo: foo + imc(foo), proyeccion))
    # Reducimos
    return reduce(max_imc, tuplas_imc)
    # Debería salir Suazo. Si no pusieramos la condición de Chileno
    # saldría Ronaldo


def print_consulta(func, lista):
    result = func(lista)

    print(func.__name__.title())
    print("-" * len(func.__name__))

    if type(result) is list:
        print(*result, sep='\n')
    else:
        print(result)

    print("")

if __name__ == '__main__':
    tuplas = leer_archivo()
    print_consulta(se_llama_como_yo, tuplas)
    print_consulta(chilenos_zurdos, tuplas)
    print_consulta(edades, tuplas)
    print_consulta(sub_17, tuplas)
    print_consulta(goleador, tuplas)
    print_consulta(mayor_riesgo_obesidad, tuplas)
