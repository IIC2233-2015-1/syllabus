#!/usr/bin/env

from wordcloud import WordCloud
from PyQt4 import QtGui, QtCore
from sys import exit

"""
Este es el 'frontend', que se refiere a la interfaz usuaria,
la que recoge los argumentos del usuario y que muestra los
resultados o output que correspondan.
"""


class Interfaz(QtGui.QMainWindow):

    def __init__(self):
        super(Interfaz, self).__init__()
        self.initUI()

    def initUI(self):
        """ Este es el codigo que les interesa """

        # Configuración básica para una ventana
        self.resize(200, 600)
        self.setWindowTitle('Generador WordCloud')

        # Barra progreso (al generar nube)
        self.BarraPgenerarNube = QtGui.QProgressBar(self)
        self.BarraPgenerarNube.move(40, 75)
        self.BarraPgenerarNube.resize(150, 25)

        # Boton para cargar nube
        self.BcargarNube = QtGui.QPushButton('Generar nube', self)
        self.BcargarNube.move(50, 150)
        self.BcargarNube.clicked.connect(self.GenerarImagen)

        # Boton para guardar imagen
        self.BGuardar = QtGui.QPushButton('Guardar', self)
        self.BGuardar.move(50, 225)
        self.BGuardar.clicked.connect(self.GuardarImagen)

        # Boton para abrir la imagen
        self.BAbrir = QtGui.QPushButton('Abrir', self)
        self.BAbrir.move(50, 300)
        self.BAbrir.clicked.connect(self.MostrarImagen)

        # Sección para colocar imágen
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(0, 450, 200, 100)


        # Muestra la ventana
        self.show()

    def palabraGenerada(self):

        # Recibe el evento de PalabraColocada
        self.BarraPgenerarNube.setValue(self.BarraPgenerarNube.value() + 1)

    def MostrarImagen(self):

        myPixmap = QtGui.QPixmap('imagen.bmp')
        myScaledPixmap = myPixmap.scaled(self.label.size())
        self.label.setPixmap(myScaledPixmap)

    def GenerarImagen(self):

        # Generar imagen
        archivo_input = fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                                                                  '/home')
        self.A = WordCloud(archivo=archivo_input)
        self.A.configurar_output()

        # Conectamos el evento a nuestro receptor
        self.A.PalabraColocada.connect(self.palabraGenerada)

        # Seteamos la barra para que avance bien
        self.BarraPgenerarNube.setMaximum(len(self.A.palabras) - 1)

        # Ahora empezamos a acomodar las palabras
        self.A.acomodar_palabras()

        # Avisar término
        QtGui.QMessageBox.about(
            self, "Imagen generada", "La imagen se termino de construir")

    def GuardarImagen(self):

        # Guardamos la imagen como archivo
        archivo_input = fname = QtGui.QFileDialog.getSaveFileName(self, 'Open file',
                                                                  '/home')
        if  ".bmp" not in archivo_input:
            archivo_input += ".bmp"
        self.A.to_file(nombre=archivo_input)

if __name__ == '__main__':
    # Esto va siempre también
    app=QtGui.QApplication([])
    interfaz=Interfaz()
    exit(app.exec_())
