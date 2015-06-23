## Solución Control 9

### 1. ¿Qué tipo de problemas sería útil implementar la solución de Web-Services?

Cuando se requiere gran capacidad de procesamiento o uso de sistemas muy especializados que no serían capaces de ejecutarse en la máquina local. 

Por ejemplo, los reconocimientos de voces que usa Apple, Google y Microsoft se hacen en sus servidores y los clientes (celulares) consumen ese servicio a través de una API (que puede ser privada o no).

Otro caso podría ser cuando se requiere el uso de recursos comunes en tiempo real. Por ejemplo, una *web app* como Facebook.

### 2. Suponga que tiene que hacer consultas al recurso `el_tiempo` a la web `http://www.meteochile.cl/aplicaciones` con la `ciudad` como parámetro. Usando la librería `requests`, escríba el código para hacerlo.


```python
import requests

# Opción 1:
parameters = {'ciudad' : 'San Felipe'}
response = requests.get(url='http://www.meteochile.cl/aplicaciones/el_tiempo', params=parameters)

# Opción 2:
parameters = {'recurso': 'el_tiempo', 'ciudad' : 'San Felipe'}
response = requests.get(url='http://www.meteochile.cl/aplicaciones', params=parameters)

# Opción 3:
response = requests.get(url='http://www.meteochile.cl/aplicaciones/el_tiempo?ciudad=SanFelipe)

# Opción 4:
response = requests.get(url='http://www.meteochile.cl/aplicaciones?recurso=el_tiempo&ciudad=SanFelipe)
```
