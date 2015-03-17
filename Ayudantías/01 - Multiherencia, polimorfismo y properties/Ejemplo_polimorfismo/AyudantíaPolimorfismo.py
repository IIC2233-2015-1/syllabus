__author__ = 'Vicente'
class Objeto:

    def __init__(self, peso, volumen, **kwargs):
        self.peso = peso
        self.volumen = volumen

    def descripcion(self):
        print("{} {}".format(self.peso, self.volumen))

class Calculadora(Objeto):

    def __init__(self, marca, modelo, **kwargs):
        super().__init__(**kwargs)
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        super().descripcion()
        print("{} {}".format(self.marca, self.modelo))
    def sumar(self, a, b):
        print(a+b)
class Agenda(Objeto):

    def __init__(self, agno, **kwargs):
        super().__init__(**kwargs)
        self.agno = agno

    def descripcion(self):
        super().descripcion()
        print("Agenda del año {}".format(self.agno))

class Celular(Calculadora, Agenda):
    def __init__(self):
        super().__init__(agno=("2015"),
                         peso="1.0 kg",
                         volumen="0.1 L",
                         marca="Pear",
                         modelo="yoFono 6g plus")

    def descripcion(self):
        super().descripcion()
        print("El mejor telefono del mundo mundial")
    def bend(self):
        print("Ups! You unlocked and special feature")

if __name__ == '__main__':
    celu = Celular()
    celu.descripcion()
    print (Celular.__mro__)#Muestra el orden de las clases a buscar en el polimorfismo