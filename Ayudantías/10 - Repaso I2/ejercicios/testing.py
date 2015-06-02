__author__ = 'ivania'
import calculadora as cal
import py.test


class TestCalculadora:
    def setup_class(cls):
        cls.calculadora = cal.CalculadoraMisteriosa(8)
        cls.lista = [(1, 1, 7), (3, 64, 8), (6, 32768, 11), (7, 262144, 8), (8, 2097152, 13)]

    def test_op_1(self):
        for tupla in self.lista:
            a = self.calculadora.op_misteriosa_1(tupla[0])
            assert a == tupla[1]

    def test_op2_(self):
        for tupla in self.lista:
            a = self.calculadora.op_misteriosa_2(tupla[0])
            assert a == tupla[2]