# Ejercicio Simulación

Simule sin el uso de `Simpy` un paradero. Considere que:
* Llegan pasajeros con tiempo entre llegadas uniforme(0.5, 1) minutos.
* Llegan microbuses con tiempo entre llegadas uniforme(15, 20) minutos. 
* La capacidad máxima del bus es de 30 personas. 
* Los pasajeros suben instantáneamente al bus (partida inmediata).

Además indique:
* Eventos
* Variables

## Solución

### Eventos:

* Llegada bus.
* Llegada pasajero.

### Variables

* Tiempo simulación.
* Tiempo próximo pasajero.
* Tiempo próximo bus.

### Simulación
En `Simulacion.py`.

# Ejercicio Threads

## Ejercicio 1

**Dado el siguiente código:**
``` python
def thread1():
    while seguir:
        print("Thread 1")


def thread2():
    global seguir
    while seguir:
        print("Thread 2")
        seguir = False


def thread3():
    while seguir:
        print("Thread 3")


seguir = True
t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)
t3 = threading.Thread(target=thread3)
t1.start()
t2.start()
t1.join()
t3.start()
```

**¿Cuáles de las siguientes salidas es posible?**
* a. 
```
Thread 1
Thread 1
Thread 2
Thread 1
```
* b. 
```
Thread 1
Thread 2
Thread 1
Thread 1
Thread 2
```
* c. 
```
Thread 1
Thread 1
Thread 3
Thread 1
Thread 1
Thread 2
```

* d. Ninguna de las anteriores

### Respuesta correcta
**a.** es correcta. No es posible que entre a `thread3`, por lo que **c.** es incorrecta. No puede entrar dos veces a `thread2`, por lo que **b.** es incorrecta.

## Ejercicio 2
**Dado el siguiente código:**
``` python
def thread1():
    while True:
        global t2, t1start
        t1start = True
        print("Thread 1")
        t2.join()


def thread2():
    global seguir, t1, seguir
    while seguir:
        if t1start:
            t1.join()
            seguir = False
            print("Thread 2")


seguir = True
t1start = False
t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)
t2.start()
t1.start()
t2.join()
print("Main thread")
```
**¿Cuál es la salida?**

* a.
```
Thread 1
```

* b.
```
Thread 1
Thread 2
```

* c. 
```
Thread 1
Thread 2
Main thread
```
* d. Ninguna de las anteriores.

### Respuesta correcta 
**a.**

## Ejercicio 3

**Respecto al ejercicio anterior**: ¿alguna vez termina de correr el programa? Si la respuesta es no: ¿por qué no lo hace?


