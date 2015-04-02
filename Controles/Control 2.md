## Solución

> Eran 3 formas, se presenta la principal solución para cada una de ellas.

```python
L = ["a","b","c","d","e"]

d = {L[i]:i for i in range(len(L))}
print(d)

s = set(k for k in d)
print(s)

L = [d[k] for k in d]
print(L)
```

### Puntaje:
* Todo bueno: 7.0
* Malo: 1.0
* Errores de sintaxis mínimas: intermedio
