#Preguntas de Conceptos
#####1. Los threads de un proceso comparten:
I. Recursos abiertos por el proceso.
    II. Stack de instrucciones.
    III. Valor de los registros en la CPU (i.e. contexto de la CPU).
	(a) Sólo I.
    (b) Sólo III.
    (c) Sólo I y II.
	(d) Sólo I y III
#####2. Respecto a serialización, señale cuál de las siguientes afirmaciones es verdadera:
(a) Al modificar el objeto producto de una deserialización se modifica el objeto original, puesto que tienen la misma referencia.
(b) La serialización es posible realizarla sobre archivos binarios y de texto plano.
(c) Todas las clases son serializables por defecto
(d) Ninguna de los anteriores.
#####3. Los archivos de texto traen metadata que indica el encoding de estos.
#####4. Con respecto a Serialización indique:
I. Al serializar, el output obtenido es una copia de el/los objetos serializados.
II. Al des-serializar debo indicar a que clase pertenece la instancia des-serializada
III. Puedo crear mis propias formas de serializar una clase.
(a) Sólo I es correcta.
(b) Sólo II es correcta.
(c) I y III son correctas.
(d) I, II y III son correctas.
#####5. Un archivo de texto también es un archivo binario, puesto que tiene un header de tamaño variable que indica como leerlo.
#####6. Un objeto obtenido a partir de un proceso de deserialización posee la misma dirección de memoria que el original.
##Respuestas: 
|Pregunta|Respuesta|
|:-------|:--------|
|1|a|
|2|b|
|3|Verdadero|
|4|c|
|5|Falso: El archivo de texto plano no tiene metadata.|
|6|Falso: Es una copia|