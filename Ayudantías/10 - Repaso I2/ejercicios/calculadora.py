__author__ = 'ivania'


class CalculadoraMisteriosa():
    def __init__(self, iniciador):
        self.iniciador = iniciador

    def op_misteriosa_1(self, numero):
        resultado = 1
        for i in range(1, numero):
            resultado *= self.iniciador
            # print(resultado)
        return resultado

    def op_misteriosa_2(self, numero):
        resultado = 1
        for i in range(1, self.iniciador):
            resultado %= numero
            resultado += i
            # print(resultado)
        return resultado


if __name__ == "__main__":
    calculadora = CalculadoraMisteriosa(8)
    for j in [1, 3, 6, 7, 8]:
        print("Num {}".format(j))
        print("Op1 = {}".format(calculadora.op_misteriosa_1(j)))
        print("Op2 = {}".format(calculadora.op_misteriosa_2(j)))


