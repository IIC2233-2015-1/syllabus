
# Ayudantía I/O - Bytes

## Ejercicio 1:

Pasar una imagen a un arreglo de bytes. Completar el siguiente método:

```python
def file_to_bytes(path):
    pass
```


## Ejercicio 2:

Crear un método que tome un arreglo de bytes en *little endian* y calcule el número en decimal:

```python
def to_int(databytes):
    pass

print(to_int(b'\x09'))  # 0xFF = (16^1)*0 + (16^0)*9 = 9
print(to_int(b'\xFF'))  # 0xFF = (16^1)*15 + (16^0)*15 = 255
print(to_int(b'\xFF\x01'))  # ?
```


## Ejercicio 3:

Haga un método que extraiga la siguiente metadata de un archivo `.bmp` en números decimales:

* Ancho
* Alto
* Tamaño
* Inicio de la data de la imagen en sí

> Puede conseguir la arquitectura del formato aquí: http://es.wikipedia.org/wiki/Windows_bitmap

```python
def metadata(PATH):
    data = file_to_bytes(PATH)

    metadata = {}
    metadata['Tamano'] = 0
    metadata['Ancho'] = 0
    metadata['Alto'] = 0
    metadata['Inicio'] = 0

    return metadata
```


## Ejercicio 4:

Cree un método que reciba el *ancho* actual de la imagen en pixeles y retorne el *padding* de la imagen.
Recuerde que un pixel son **3 bytes**.

```python
def get_padding(pixel_width):
    pass
```


## Ejercicio 5

Cree un método que remueva **todos los tonos verdes**. Este debe recibir una ruta con la imagen original y otra ruta con la ruta de salida.

```python
def remove_red(source, output):
    pass
```
