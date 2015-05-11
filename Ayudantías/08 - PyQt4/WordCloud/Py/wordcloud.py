#!/usr/bin/env

#  Mucho del código ha sido obtenido de:
#  https://github.com/amueller/word_cloud
#  Se simplificó, adaptó y comentó el código
# para facilitar su comprensión

# Agilizar el formateo del texto
from re import UNICODE, compile, sub
# Agilziar el conteo de las palabras
from collections import Counter
# Moverse a la carpeta con fonts
from sys import platform, stdin, argv
# Random
from random import Random
# Numpy
from numpy import zeros, array, log, uint32, asarray, cumsum, newaxis
# PIL
from PIL import Image, ImageDraw, ImageFont
# Un poquito de ayuda extra
from query_integral_image import query_integral_image
# PyQt
from PyQt4 import QtGui, QtCore

"""
Este es el 'backend' de la aplicación, es toda la parte lógica,
la parte que hace el trabajo pesado en una aplicación.
"""

# Esto ya lo verán
PATRON = compile('[\W_]+', UNICODE)

# Algo para acomodarse a los OS
if platform == 'win32':  # Windows
    FONT_PATH = r'C:\Windows\Fonts\consola.ttf'
elif platform == 'darwin':  # MacOS
    FONT_PATH = r'\Library\Fonts\DroidSansMono.ttf'
else:  # Linux
    FONT_PATH = os.environ.get(
        "FONT_PATH", "/usr/share/fonts/truetype/droid/DroidSansMono.ttf")

# Un random global
R = Random()


def color_random(word=None, font_size=None, position=None,
                 orientation=None):
    """Esta función genera los colores para cada palabra. Podemos
    usar los distintos argumentos de arriba para asignar los colores.
    Por ejemplo, asignar colores más oscuros para las palabras más largas,
    o asignar un color para las palabras verticales y otro para las
    horizontales"""
    return "hsl(%d, 80%%, 50%%)" % R.randint(0, 255)


class WordCloud(QtGui.QWidget):

    """Esta clase está encargada de generar la imágen de la
    nube de palabras. Contiene tanto la parte lógica como las
    definiciones del output (archivo .jpg o .png)"""

    def __init__(self, archivo="input.txt"):
        super(WordCloud, self).__init__()
        #  Aquí tomamos el archivo, todas sus palabras
        # y obtenemos su frecuencia
        with open(archivo) as f:
            lines = f.readlines()
        text = ' '.join(lines)
        text = text.lower()
        text = str(PATRON.sub(' ', text))
        self.text = text.split()
        # cloud es el tipo: <class 'list'>
        self.palabras = []
        cloud = Counter(self.text).most_common()
        max_freq = cloud[0][1]
        self.num_palabras = 0
        for word, freq in cloud:
            self.palabras.append((word, float(freq / max_freq)))
            self.num_palabras += 1

    def configurar_output(self, width=400, height=200, margin=5, scale=1,
                          color_func=color_random, max_words=200, background='black',
                          max_font_size=200, horizontales=0.9):
        """Se definen los atributos principales para generar la imágen"""
        self.font_path = FONT_PATH
        self.R = Random()
        self.width = width
        self.height = height
        self.margin = margin
        self.scale = scale
        self.color_func = color_func
        self.max_words = max_words
        self.background = background
        self.max_font_size = max_font_size
        self.horizontales = 0.9
        self.imagen_generada = False
        return self

    def acomodar_palabras(self):
        """El 'trabajo pesado' de distribuir las palabras
        de forma que encajen en la imágen a generar"""

        altura, largo = self.height, self.width
        integral = zeros((altura, largo), dtype=uint32)

        # Creación de imágen
        imagen = Image.new("L", (largo, altura))
        dibujo = ImageDraw.Draw(imagen)
        img_arreglo = asarray(imagen)
        tamaños, posiciones, orientaciones, colores = [], [], [], []

        font_actual = self.max_font_size

        # Inicio de dibujado
        for palabra, freq in self.palabras:

            # Hay que encontrar una posición para todas las palabras
            while True:

                # font_actual = min(self.max_font_size, int(100 * log(freq + 100)))
                fuente = ImageFont.truetype(self.font_path, font_actual)

                # Vemos si va horizontal o vertical y dibujamos
                if self.R.random() < self.horizontales:
                    orientacion = None
                else:
                    orientacion = Image.ROTATE_90
                font_transpuesta = ImageFont.TransposedFont(fuente,
                                                            orientation=orientacion)
                dibujo.setfont(font_transpuesta)
                tamaño_resultante = dibujo.textsize(palabra)

                # Buscamos posibles lugares
                resultado = query_integral_image(integral, tamaño_resultante[1] + self.margin,
                                                 tamaño_resultante[0] + self.margin, self.R)

                # Si el resultado es posible o no podemos escribir más
                if resultado is not None or font_actual == 0:
                    break

                # Si no hay espacio, achicamos la fuente
                font_actual -= 1

            x, y = array(resultado) + self.margin // 2

            # Dibujar el resultado
            dibujo.text((y, x), palabra, fill="white")
            posiciones.append((x, y))
            orientaciones.append(orientacion)
            tamaños.append(font_actual)
            colores.append(self.color_func(palabra, font_size=font_actual,
                                           position=(x, y),
                                           orientation=orientacion))

            # Recalcular imágen
            img_arreglo = asarray(imagen)
            integral_parcial = cumsum(
                cumsum(img_arreglo[x:, y:], axis=1), axis=0)

            # Pegar parte calculada a la imágen acumulada
            if x > 0:
                if y > 0:
                    integral_parcial += (integral[x - 1, y:]
                                         - integral[x - 1, y - 1])
                else:
                    integral_parcial += integral[x - 1, y:]
            if y > 0:
                integral_parcial += integral[x:, y - 1][:, newaxis]

            integral[x:, y:] = integral_parcial

        self.distribucion = list(
            zip(self.palabras, tamaños, posiciones, orientaciones, colores))
        self.imagen_generada = True

    def to_image(self):
        """La distribución generada se traspasa a imágen. Habrá
        un error si la imágen no se ha generado"""

        altura, largo = self.height, self.width

        imagen = Image.new("RGB", (largo * self.scale, altura * self.scale),
                           self.background)
        dibujo = ImageDraw.Draw(imagen)
        for (palabra, freq), font_actual, posicion, orientacion, color in self.distribucion:
            fuente = ImageFont.truetype(
                self.font_path, font_actual * self.scale)
            font_transpuesta = ImageFont.TransposedFont(fuente,
                                                        orientation=orientacion)
            dibujo.setfont(font_transpuesta)
            posicion = (posicion[1] * self.scale, posicion[0] * self.scale)
            dibujo.text(posicion, palabra, fill=color)
        return imagen

    def to_file(self, nombre="imagen"):
        """Guarda la imágen en un archivo. Deben preguntar donde guardarla"""
        imagen = self.to_image()
        imagen.save(nombre + ".bmp")

    def cambiar_colores(self, funcion_colores=color_random):
        """Cambia los colores de la imágen. Habrá un error si la 
        imágen no se ha generado"""
        # Pueden agregar nuevas funciones si les interesa aportar
        self.distribucion = [(word_freq, font_size, position, orientation,
                              funcion_colores(word=word_freq[0], font_size=font_size,
                                              position=position, orientation=orientation))
                             for palabra, fuente, posicion, orientacion, color in self.stribucionlayout_]

    def __array__(self):
        """Convierte el objeto a un arreglo"""
        return array(self.to_image())


def Demo():
    """Función que ejecuta un ejemplo"""
    A = WordCloud()
    A.configurar_output()
    A.acomodar_palabras()
    print("Palabras listas, desplegando imágen...\n")

    import matplotlib.pyplot as plt
    plt.imshow(I)
    plt.axis("off")
    plt.show()
    print("Imágen desplegada")

if __name__ == '__main__':
    # Si está corriendo en una terminal
    if stdin.isatty():
        args = argv
        print("\n'-h' o 'help': Documentación del módulo" +
              "\n'-d o 'demo': Ejemplo de output (requiere archivo input.txt)\n")

        if len(args) != 2:
            raise Exception("Se debe ingresar solo 1 comando\n")

        if "-h" == args[1] or "help" == args[1]:
            import wordcloud
            help(wordcloud)
        elif "-d" or "demo" in args:
            print("Cargando demostración...\n" +
                  "(Esto puede tomar cerca de 1 minuto...)\n")
            Demo()
