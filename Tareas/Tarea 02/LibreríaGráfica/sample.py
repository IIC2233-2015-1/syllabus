from interfaz import Interfaz


class Sample:

    def __init__(self):
        self.lista = [[0 for y in range(32)] for x in range(36)]

    def func_alumno1(self, num):
        valor = 32 - num if num < 32 else 2
        self.lista = [[0 for y in range(valor)] for x in range(valor)]

        return self.lista

    def func_alumno2(self, tupla):
        return self.lista

    def consulta1(self, tupla):
        return ["Respuesta1", "Respuesta2", tupla]

    def consulta5(self, tupla):
        return 1


if __name__ == '__main__':
    sample = Sample()
    funciones = [sample.consulta1, sample.consulta1,
                 sample.consulta1, sample.consulta5, sample.consulta5]
    interfaz = Interfaz(
        sample.func_alumno1, sample.func_alumno2, sample.lista, funciones)
    interfaz.run()
