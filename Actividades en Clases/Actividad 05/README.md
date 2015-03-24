# Actividad 5
> Estructura de Datos 2

### Descripción

Todas las estructuras de datos con las que has trabajado hasta ahora son lineales, sin embargo, a veces es necesario trabajar con más dimensiones, como con un grafo para recorrer un laberinto o simplemente un árbol para tomar decisiones o hacer búsquedas en profundidad.

En esta actividad se te entrega una estructura de datos que modela un mapa de un servicio de Metro, donde **cada estación puede tener hasta 4 estaciones adyacentes**:
* Derecha
* Izquierda
* Arriba
* Abajo

A continuación te mostramos un ejemplo de un mapa. Puedes notar que, por ejemplo, la `estación 1` está conectada con la `estación 2`, pero no viceversa. 

También podemos ver que es posible llegar desde la `estación 0` a la `estación 11` pero no es posible ir desde la `estación 0` hasta la `estación 19`.

![grafo1](https://raw.githubusercontent.com/IIC2233-2015-1/Ayudantes/master/Actividades%20en%20Clases/Clase%2005%20-%20Estaciones%20de%20metro/Enunciado/grafo.jpg?token=AHOFOMs1dsJKWPs0zGiTDFdinKx1NO0vks5VGhs4wA%3D%3D "Grafo")

### Requerimientos

* Obtén los archivos `main.py` y `estaciones_metro.py` que están en esta misma carpeta.
* Pon estos archivos en tu repositorio privado en la carpeta donde les corresponse (`Actividad_05`)
* **Debes modificar el archivo ``main.py`` (y solamente este archivo) y completar el método `camino(...)`**
	* Este método recibe dos estaciones de metro
	* Retorna **`False`** si **no es posible llegar desde el origen hasta el final** respetando los caminos.
	* Retorna **`True`** si **existe un camino entre el origin y el destino**. Además **imprime** el recorrido que hace.
* Puedes crear métodos, clases y/o lo que estimes conveniente en el `main.py` o en otros archivos (asegúrate de importarlos). Solo preocúpate de no modificar la firma del método `camino(...)`.
* Debes cambiar el nombre del `main.py`, si trabajas en grupo debes llamarlo: `AC5_numAlumno1_numAlumno2.py` y ambos deben subirlo a sus repositorios. En caso de trabajar solo, lo debes nombrer como: `AC5_numAlumno.py`.


### Entrega

* No debes modificar el archivo `estaciones_metro.py`.
* Asegúrate de subir a tu repositorio los archivos `main.py` (renombrado según las instrucciones de arriba) y `estaciones_metro.py`. 

### Recomendaciones

**Lee completo el código base** que te pasamos para que entiendas la lógica del programa. Todo lo que pueda resultar extraño está comentado, recuerda que puedes preguntarle a los ayudantes si no entiendes algo.

Aunque la actividad **se revisará con otro input**, puedes trabajar con la representación del mapa que ves en la imagen. Para usarlo, se genera así: 

```python
mapa = MapaMetro.mapa_de_ejemplo()
```

Esto ya está programado en al final del `main.py`.

