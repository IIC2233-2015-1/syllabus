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

    """Esta clase controla el 'frontend', para facilitar
    la recepción de inputs y la muestra de outputs"""

    def __init__(self):
        # Siempre es conveniente hacer eso
        super(Interfaz, self).__init__()
        self.initUI()

    def initUI(self):
        """Este método lo llenan ustedes"""

        self.show()

if __name__ == '__main__':
        # Esto va siempre también
    app = QtGui.QApplication([])
    interfaz = Interfaz()
    exit(app.exec_())
