
# Ayudantía I/O - Bytes

## Ejercicio 1:

Pasar una imagen a un arreglo de bytes. Completar el siguiente método:

```python
def file_to_bytes(path):
    with open(path, 'rb') as file:
        return bytearray(file.read())
```


## Ejercicio 2:

Crear un método que tome un arreglo de bytes en *little endian* y calcule el número en decimal:

```python
def to_int(databytes):
    size = len(databytes)
    return sum(databytes[i] << (i * 8) for i in range(size))

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
    metadata['Tamano'] = to_int(data[2:6])
    metadata['Ancho'] = to_int(data[18:22])
    metadata['Alto'] = to_int(data[22:26])
    metadata['Inicio'] = to_int(data[10:14])

    return metadata
```


## Ejercicio 4:

Cree un método que reciba el *ancho* actual de la imagen en pixeles y retorne el *padding* de la imagen.
Recuerde que un pixel son **3 bytes**.

```python
def get_padding(pixel_width):
    res = (pixel_width * 3) % 4
    if res == 0:
        return 0
    return 4 - res
```


## Ejercicio 5

Cree un método que remueva **todos los tonos verdes**. Este debe recibir una ruta con la imagen original y otra ruta con la ruta de salida.

```python
def remove_red(source, output):
    pass
```
