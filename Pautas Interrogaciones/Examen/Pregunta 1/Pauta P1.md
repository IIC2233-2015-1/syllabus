Pregunta 1 - Examen IIC2233
=========================== 

- **a) (3 pts.)** ¿Para qué sirve sobre-escribir el método \_\_**call**\_\_ en una clase que hereda de _type_?

- **b) (3 pts.)** ¿Cuál es la diferencia entre un iterador y un generador?

- **c) (4 pts.)** Muestre un ejemplo que ilustre la diferencia entre herencia y composición en modelamiento OOP.

- **d) (5 pts.)** Usando la función _reduce_, en una línea de código transforme una lista de dígitos `L` en el número resultante de "juntar" los dígitos de la lista, ejemplo: `[2, 4, 6, 1] -> 2461`.

- **e) (3 pts.)** ¿Qué diferencia práctica existe entre realizar llamadas a un servidor usando los métodos `GET` y `POST`?

- **f) (7 pts.)** Implemente un decorador que controle el acceso a la función decorada de tal forma de que no pueda vovler a ser ejecutada mientras ya esté siendo ejecutada.

- **g) (5 pts.)** Dado el siguiente código (ver enunciado), escriba lo que debería salir como output.

```
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
```

Soluciones
=========================== 

- **a)** De los apuntes (**04 MetaClases**): 

    El método `__call__` se llama cada vez que la "ya creada" clase es "llamada" para instanciar un nuevo objeto. Por lo tanto, implementar el método `__call__` en una clase, (...) hace que las instancias sean "llamables", es decir, que se comporten como una función, donde `instancia()` llamaría al método `__call__` implementado.

- **b)** De los apuntes (**03 Python Functions**): 

    **Iterador:** Un iterador es un objeto que itera sobre un iterable, es el objeto retornado por el método iter(), además contiene el método next() que nos va retornando el siguiente elemento.

    **Generador:** Los generadores son **un caso especial** de los iteradores. Los generadores nos permiten iterar sobre secuencias de datos sin la necesidad de almacenarlos en alguna estructura de datos, evitando el uso innecesario de memoria. Una vez que terminamos de iterar sobre un generador, el generador desaparece.

- **c)** De los apuntes (**01 OOP**): 

    **Herencia:** Cuando un objeto pertenece a una clase en particular, si esta clase es a su vez una sub-clase de otra clase más general, la herencia nos permite "heredar" los datos y comportamiento de la clase "madre" (superclase), de tal manera de no tener que volver a definir esos datos y comportamiento en la subclase. 
    **Ej:** La clase *furgón escolar* es una subclase de la clase *vehículo*, por lo tanto sabemos que la clase *furgón escolar* va a heredar los datos (campos) y comportamiento (métodos) de *vehículo* (como ruedas, motor, etc.) y no es necesario volver a definirlos en la subclase *furgón escolar*.

    **Composicion:** La composición es un tipo de relación dependiente en dónde un objeto más complejo es conformado por objetos más pequeños. Este caso se da cuando un objeto tiene como atributo a algun objeto de otra clase. En esta situación, la frase “Tiene un” (o "contiene"), debe tener sentido.
    **Ej:** La **moto** *tiene* **ruedas**. La **sala** *tiene* **mesas**. En ambos casos podemos definir por ejemplo `moto.ruedas = [rueda(1), rueda(2)]`, para asignar objetos de otras clases como atributos de otra.

- **d)** Basado en los apuntes (**03 Python Functions**). 

    ```
    >>> from functools import reduce
	>>> L = [2, 4, 6, 1]
	>>> reduce(lambda x, y: 10*x + y, L)
	2461
    ```

- **e)** Basado en los apuntes (**13 WebService**): 

    | **VERBO HTTP** | **Acción** |  
	| -------------- | ------------------------------- |
	| POST | Crea un recurso. |
	| GET  | Recupera una representación de un recurso sin cambiar nada en el servidor. |

- **f)** De los apuntes (**03 Python Functions**): 

    ```
    import threading


    def decorator_f(f):
        def f2():
            lock.acquire()
            try:
                return f()
            finally:
                lock.release()
        return f2


    @decorator_f
    def f():
        for j in range(7):
            print(j)

    if __name__ == "__main__":
        lock = threading.Lock()
        num_threads = 10
        t = []
        for i in range(num_threads):
            my_thread = threading.Thread(target=f)  # , args = (i,)
            t.append(my_thread)
        for th in t:
            th.start()
    ```

- **g)**  Output:

    ```
    0
    [4, 1, 2, 3, 4]
    0
    hola mundo
    ```
