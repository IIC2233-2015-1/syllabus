## Solución Control 5

###1. Explique para qué sirvem los métodos `setUp` y `tearDown` de unittest
####`setUp`
El método `setUp` nos permite declarar y asignar valores a las variables que serán usadas para los tests. Sirve para manejar de forma rápida el input de cada test ya que se preocupa de volver a setear o inicializar las variables antes de entrar a un test nuevo.
####`tearDown`
Este método define las acciones a seguir luego de que se han realizado **Todos** los test. Se usa para limpiar el ambiente del programa después de la ejecución de todos los tests. 

####Puntaje
* 1.5 puntos por cada uno

###2. ¿Es una mala práctica de programación manejar una excepción usando `except:` (a secas) después de un `try:`? Justifique su respuesta
Sí, porque no permite conocer cuál es el tipo de error que ocurrió y por lo mismo no permite manejarlos de forma personalizada (todos los errores siguen el mismo tratamiento)

####Puntaje
* 1 punto por respuesta 
* 2 puntos por justificación
