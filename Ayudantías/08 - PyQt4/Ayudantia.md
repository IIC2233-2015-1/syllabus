# Ayudantia 8 - PyQt4 & Qt Designer

Como ya vieron en el material del curso, ahora estamos trabajando sobre interfaces de usuario (UI por sus siglas en ingles), y estas las creamos con la ayuda de **PyQt4**. Hoy veremos algunos ejemplos con **PyQt4** e integraremos **Qt Designer** para facilitar el trabajo de crear interfaces.

## Ejercicios

###	Ejercicio 1

Cree una GUI en la que un usuario, pueda cargar el archivo de texto, *input.txt* y permita crear la imagen correspondiente con un click. Además, debe mostrar una barra de progreso. Una vez que se tenga la imagen, se debe mostrar en la interfaz.

## Bonus

Crear opciones para cambiar el color de la imagen (una vez generada, para lanzar el random), abrir un archivo determinado y guardar la imagen donde el usuario quiera (usar *File Dialog*)

### Ejercicio 2

Cree una GUI en la que pueda ingresar a un usuario con `nombre` y `rut` para el ingreso de ciertos dineros, esta ventana debe permitir cambiar de funcionalidad entre *abono* y *deuda*. (soy el peor ayudante) Los datos ingresados se deben registrar en un archivo para tener respaldo de ellos. Debe crear una funcionalidad extra que permita saber el saldo total de abonos, deudas y neto de un cliente en específico ingresando solo su rut.


####Widgets que usaremos
* 3 QRadioButton
* 3 QLabel
* 3 QLineEdit
* 2 QPushButton
* 1 Spacer
* 1 QHBoxLayout
* 1 QGridLayout
* 1 QPlainTextEdit