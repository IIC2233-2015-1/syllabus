__author__ = 'ivania'
from arbol import Arbol, crear_arbol
import operator
# medida
miedo = {}


def get_miedo(arbol):
    global miedo
    if type(arbol.nombre) is str:
        mov_pocmon = arbol.nombre
        for fantasma, mov_fantasma in arbol.ancestros.items():
            if check_direction_sense(mov_pocmon, mov_fantasma):
                if fantasma.nombre in miedo.keys():
                    miedo[fantasma.nombre] += 1
                else:
                    miedo[fantasma.nombre] = 1
    else:
        for hijo in arbol.hijos:
            if arbol.hijos[hijo] is not None:
                get_miedo(arbol.hijos[hijo])


def check_direction_sense(pocmon, fantasma):
    d1 = ['r', 'u']
    d2 = ['d', 'l']
    if (pocmon in d1 and fantasma in d1) or (pocmon in d2 and fantasma in d2):
        return pocmon != fantasma
    else:
        return False


datos = [('r', 'l', 'd', 'd', 'l', 'r', 'u', 'd', 'd', 'l', 'l', 'v'),
         ('r', 'l', 'u', 'd', 'l', 'r', 'r', 'u', 'r', 'l', 'u', 'v'),
         ('u', 'r', 'r', 'd', 'r', 'l', 'd', 'u', 'l', 'u', 'r', 'v'),
         ('l', 'r', 'd', 'd', 'd', 'u', 'l', 'r', 'u', 'u', 'd', 'm'),
         ('d', 'r', 'r', 'l', 'r', 'r', 'd', 'u', 'l', 'r', 'r', 'v'),
         ('d', 'r', 'r', 'l', 'r', 'r', 'd', 'u', 'l', 'r', 'r', 'v'),
         ('u', 'r', 'd', 'd', 'r', 'u', 'd', 'r', 'l', 'u', 'l', 'v'),
         ('r', 'r', 'd', 'u', 'd', 'u', 'u', 'u', 'r', 'd', 'l', 'v'),
         ('r', 'r', 'r', 'u', 'l', 'r', 'd', 'r', 'r', 'r', 'r', 'm'),
         ('u', 'd', 'd', 'd', 'l', 'r', 'r', 'u', 'u', 'd', 'd', 'm'),
         ('d', 'r', 'l', 'd', 'r', 'r', 'u', 'd', 'u', 'u', 'd', 'm'),
         ('d', 'd', 'd', 'r', 'r', 'u', 'u', 'l', 'l', 'l', 'd', 'v'),
         ('r', 'r', 'd', 'd', 'd', 'd', 'l', 'l', 'l', 'u', 'l', 'v'),
         ('u', 'd', 'l', 'u', 'u', 'd', 'u', 'r', 'u', 'l', 'u', 'm'),
         ('l', 'u', 'd', 'l', 'd', 'd', 'd', 'u', 'u', 'r', 'l', 'm'),
         ('d', 'r', 'r', 'l', 'r', 'd', 'u', 'l', 'd', 'l', 'd', 'v'),
         ('r', 'r', 'l', 'r', 'u', 'u', 'l', 'u', 'u', 'l', 'l', 'm'),
         ('r', 'r', 'l', 'r', 'u', 'u', 'l', 'u', 'u', 'l', 'l', 'm'),
         ('r', 'r', 'l', 'r', 'u', 'u', 'l', 'u', 'u', 'l', 'l', 'v')]

datos_agrupados = {}

for d in datos:
    if d[:len(d) - 1] not in datos_agrupados:
        datos_agrupados[d[:len(d) - 1]] = [0, 0]
    if d[-1] == 'm':
        datos_agrupados[d[:len(d) - 1]][0] += 1
    else:
        datos_agrupados[d[:len(d) - 1]][1] += 1

outcomes = {}

def get_outcome(arbol):
    if type(arbol.nombre) is str:
        mov_pocmon = arbol.nombre
        subconjunto = [k for k in datos_agrupados]
        # encontrar las entradas que tienen ese mov para ese fantasma
        subconjunto = get_entradas(subconjunto, mov_pocmon, arbol.ancestros.items())
        outcome = [0, 0]
        # sumar los outcomes para todos los fantasmas
        for entrada in subconjunto:
            outcome[0] += datos_agrupados[entrada][0]
            outcome[1] += datos_agrupados[entrada][1]
        outcomes[arbol] = outcome

    else:
        for hijo in arbol.hijos:
            if arbol.hijos[hijo] is not None:
                get_outcome(arbol.hijos[hijo])

def get_entradas(subconjunto, mov_pocmon, fantasmas):
    sub_subconjunto = []
    for fantasma, mov_fantasma in fantasmas:
        for entrada in subconjunto:
            if entrada[-1] == mov_pocmon and entrada[fantasma.nombre] == mov_fantasma:
                sub_subconjunto.append(entrada)
    return sub_subconjunto



for k, v in datos_agrupados.items():
    print(k, v)


results = []
fantasma_root = Arbol(0)
crear_arbol(fantasma_root, 4)

fantasma_root.print(0)
get_miedo(fantasma_root)
print(miedo)
r = dict(sorted(miedo.items(), key=operator.itemgetter(1)))
print(r)

get_outcome(fantasma_root)
print(outcomes)