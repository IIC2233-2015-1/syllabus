def f1(_input):
        if type(_input) in [int, float, bool, str]:
            _input = 2
        else:
            _input[0] = _input[-1]
        return True


def f2(_input):
    print(_input)


class A:

    def __init__(self, a=0):
        self.atributo = a

    def __str__(self):
        return "{}".format(self.atributo)

if __name__ == "__main__":
    a = 0
    f1(a)
    f2(a)

    b = [0, 1, 2, 3, 4]
    f1(b)
    f2(b)

    c = A()
    f1(c.atributo)
    f2(c)

    d = "hola mundo"
    f1(d)
    f2(d)