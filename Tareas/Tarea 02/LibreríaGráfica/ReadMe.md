##Características de la interfaz:

* __Botones de navegación__: son 4, cada uno entrega un valor diferente al ser 
presionado:
	..*Arriba: (0, 1)
	..*Abajo: (0,-1)
	..*Izquierda: (-1, 0)
	..*Derecha: (1, 0)
* __Barra de zoom__: retorna un valor del 0 al 99, el valor actual se indica entre los
botones de navegación.
* __Mapa__: grilla donde están los elementos actuales.
* __Barra de consultas__: puedes cambiar de consulta presionando las flechas.
Para aquellas consultas que requieran más de un elemento,
sepárelos con una "," y sin espacios. Se toma el supuesto de que las consultas toman los argumentos de la siguiente forma:
	..*consulta1: (Ubicación, región)
	..*consulta2: (Ubicaciones, región) [Siendo ubicaciones una lista]
	..*consulta3: (ubicacion1, ubicacion2)
	..*consulta4: (ubicación, cantidad de sub-grillas)
	..*consulta5: (ubicación, cantidad)
* Las dimensiones son fijas, no se pueden modificar.



##Cómo usar:

* Para usar la interfaz se toma la clase "Interfaz" del módulo "interfaz". Esta clase
recibe como parámetros la función de zoom, la función de navegación, el mapa inicial,
y una lista de funciones que corresponden a las consultas. Estas funciones deben ser entregadas
por el orden que están en el enunciado.