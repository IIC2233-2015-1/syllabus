## Solución

> Son 3 formas con leves cambios, abajo solo se muestra una.


```python
def mi_dec(f):
	def interno(*args, **kwargs):
		print("Los argumentos son {0} {1}\n".format(*args,**kwargs))
		return f(*args,**kwargs)
	return interno

@mi_dec
def f_1(x,y=1):
	return x*y

def f_2(x, y):
	return (x+1)**y

print(f_1(6,7))
print(f_2(2,2))
```

### Puntaje: 

* 3 puntos por print totalmente correcto
* 0 puntos si él print hace cosas de más (i.e: imprimir lo que corresponde más otra línea)
* 1.5 puntos en el print con decorator si usa bien el decorator pero el valor retornado por f_1 / f_2 está malo.
* -0.2 por errores de sintaxis
* -0.2 por no poner el salto de línea del print (\n)
