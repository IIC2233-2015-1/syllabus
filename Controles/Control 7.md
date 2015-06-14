## Solución

# 1. En la actividad anterior no controlamos el acceso a un recurso requerido por los threads. Explique en palabras en qué parte de la actividad esto eventualmente ocasionaría problemas y como podría solucionarlos.

* Al atacar al godzilla, un guerrero podría pensar que está vivo cuando ya murió y un así atacarlo. Y puede haber colisión también al intentar modificar algún recurso compartido, como es el hp del godzila. Se soluciona tomando con un lock al gozdilla cuando lo ataco.
* Hasta 3 puntos por explicación, había que aterrizarlo al ejemplo particular y más que nombrar que se compartía al godzilla, mencionar por qué era un problema haciendo referencia por ejemplo a la vida y que se podía estar atacando aun cuando estaba muerto. (1 pto nombrar locks en la solución)

# 2. ¿Es posible implementar el patrón productor-consumdor en un deque tradicional (directamente desde la librería collections). Justifique su respuesta.

* No, un deque es solo una estructura de datos y no está diseñada para ser usada en concurrencia con threads. Hay que hacerle override a sus métodos con un lock.
* 1 punto por decir que no
* 2 puntos por explicación correcta si dijo que no. 
Hasta un punto si dijo que si ya que no entendió la pregunta.
