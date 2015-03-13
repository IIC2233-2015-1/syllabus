__author__ = 'karimpichara'


class Biblioteca():

    def __init__(self):
        # diccionario que contiene los estantes, el key es el tópico, ya que
        # hay sólo un estante por tópico
        self.lista_estantes = {}

    # crea un nuevo estante y lo agrega
    def agregar_estante(self, topico_estante):
        if topico_estante not in self.lista_estantes.keys():
            E = Estante(topico_estante)
            self.lista_estantes.update({E.topico: E})
        else:
            print("Tópico ya existe..")

    def __repr__(self):
        return "\n".join([str(e) for e in self.lista_estantes.values()])

    def agregar_libro(self, libro):
        if libro.topico in self.lista_estantes.keys():
            self.lista_estantes[libro.topico].agregar_libro(libro)

    def ordenar_libros(self, topico, criterio):
        if topico in self.lista_estantes.keys():
            self.lista_estantes[topico].ordenar_libros(criterio)


class Estante():
    last_id = 0

    def __init__(self, topico):
        self.topico = topico
        Estante.last_id += 1
        self._id = Estante.last_id
        self.lista_libros = []
        # diccionario para guardar el número de ejemplares ya calculados, el
        # key es titulo + autor, el value es una lista con los ids de los
        # libros iguales
        self.num_ejemplares = {}

    def agregar_libro(self, libro):
        self.lista_libros.append(libro)
        # ya teníamos ejemplares de este libro
        if libro.titulo + libro.autor in self.num_ejemplares.keys():
            self.num_ejemplares[libro.titulo + libro.autor].append(libro._id)
        else:
            # agrego el nuevo libro con su primer id en la lista de ids
            # existentes (vacia en este caso)
            self.num_ejemplares.update(
                {libro.titulo + libro.autor: [libro._id]})

    def __repr__(self):
        out = ""
        # voy leyendo los primeros ids de los ejemplares de los libros (para no
        # imprimir mas de una vez el mismo libro)
        ids_para_imprimir = [list(self.num_ejemplares.values())[i][
            0] for i in range(len(self.num_ejemplares))]
        for l in self.lista_libros:
            if l._id in ids_para_imprimir:
                out += "\n".join([str(l) + ", Ejemplares: {}".format(
                    str(len(self.num_ejemplares[l.titulo + l.autor])))]) + "\n"

        return out

    def ordenar_libros(self, criterio):
        self.lista_libros.sort(key=criterio)

    def numero_ejemplares(self, titulo, autor=None):
        try:  # coming soon
            return self.num_ejemplares[titulo + autor]
        except:
            print("Libro no existe en nuestra base de datos...")


class Libro():
    last_id = 0

    def __init__(self, titulo, autor, topico, pags):
        self.titulo = titulo
        self.autor = autor
        self.topico = topico
        self.paginas = pags
        Libro.last_id += 1
        self._id = Libro.last_id

    # aquí seteamos la forma en que dos libros se comparan iguales
    def __eq__(self, other):
        # exijo que ambos libros no tengan autor para comparar sólo por título
        if not self.autor and not other.autor:
            return self.titulo == other.titulo
        else:
            return self.titulo == other.titulo and self.autor == other.autor

    def __repr__(self):
        return ("Título: {}, Autor: {}, "
                "Tópico: {}, Páginas: {}").format(self.titulo,
                                         self.autor,
                                         self.topico,
                                         self.paginas)


if __name__ == '__main__':
    l1 = Libro("Viaje al corazón del hambre", "Xavier Aldekoa", "Drama", 84)
    l2 = Libro("Fantasmas", "Joe Hill", "Drama", 520)
    l3 = Libro("Cry Wolf", "Patricia Briggs", "Drama", 210)
    l4 = Libro("Fantasmas", "Joe Hill", "Drama", 520)
    l5 = Libro("Fantasmas", "Joe Hill", "Drama", 520)

    l6 = Libro("Burn, Witch, Burn!", "Javier Martín Lalanda", "Horror", 122)
    l7 = Libro("Salem's Lot", "Stephen King", "Horror", 311)
    l8 = Libro("The Turn of the Screw", "Henry James", "Horror", 93)
    l9 = Libro("Salem's Lot", "Stephen King", "Horror", 311)


    lista_libros = [l1, l2, l3, l4, l5, l6, l7, l8, l9]

    B1 = Biblioteca()
    B1.agregar_estante("Drama")
    B1.agregar_estante("Horror")
    for i in range(len(lista_libros)):
        B1.agregar_libro(lista_libros[i])

    print(B1)
    B1.ordenar_libros("Drama", lambda x: x.paginas)
    B1.ordenar_libros("Horror", lambda x: x.paginas)
    print(B1)
