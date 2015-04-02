# Preguntas:
> Son 2 preguntas por control, 3 puntos cada pregunta completamente correcta.

### Forma 1
1. **Explique en qué consiste el problema del diamante**

 * Este problema surge cuándo dos clases heredan de otra tercera y, además una cuarta clase tiene cómo padre a las dos últimas. 

 * La primera clase padre es llamada A y las clases B y C heredan de ella, a su vez la clase D tiene cómo padres a B y C. En está situación, si una instancia de la clase D llama a un método de la clase A, ¿lo heredará desde la clase B o desde la clase C?

 * Cada lenguaje de programación utiliza un algoritmo para tomar está decisión. En el caso particular de Python, se toma cómo referencia que todas las clases descienden de la clase padre object. Además, se crea una lista de clases que se buscan de derecha a izquierda y de abajo a arriba, posteriormente se eliminan todas las apariciones de una clase repetida menos la última. 

2. **¿Es posible usar una lista como key en un diccionario? Justifique**

 * No, porque no es un tipo *hasheable*

### Forma 2

3. Explique la diferencia entre Overriding y Overloading

 * *Overloading* = sobrecarga de métodos -> varias definiciones del método para tomar distintos parámetros. Puede ser dentro de la misma clase. (No existe en python)
 * *Overriding* = sobre escritura -> declaración de un nuevo método. Se realiza en clases hijas.

4. ¿Cuál es la diferencia entre los métodos "extend" y "append" para listas?
 
 * `Append`: agrega un elemento al final de la colección.
 * `Extend`: Agrega todos los elementos de una colección al final de la colección.
 

### Forma 3

5. ¿Cuál es la diferencia entre polimorfismo y duck typing?

 * El **polimorfismo** es más estructurado y se sostiene en las firmas de clases que presenten asociaciones de herencia. 
 * El **Duck-typing** ocurre al existir coincidencia de las firmas de métodos o atributos. 

6. ¿Qué es un `defaultdict` y para qué puede servir?

 * El `defaultdict` funciona como un diccionario, solo que al momento de construirlo **recibe una función que se usará en caso de que se le pida algún valor a través de una llave que no exista dentro de este**. Sirve principalmente para evitar excepciones al momento de pedir una value y para entregarnos valores por defecto.
