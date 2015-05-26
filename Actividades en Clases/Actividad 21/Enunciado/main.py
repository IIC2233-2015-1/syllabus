#!/usr/bin/env python
#-*- coding:utf-8 -*-

from PyQt4 import QtCore, QtGui
import datetime
import pickle
import os

# Usted debe:
# Escribir la clase Cliente
# Completar el método 'serializarCliente' de la clase 'VentanaCajero'
# Completar el método 'generarArchivo' de la clase 'VentanaAdmin'
# Completar el método 'on_pushButton_clicked' de la clase 'Input'


class VentanaCajero(QtGui.QDialog):

    def __init__(self, parent=None, username=""):
        super(VentanaCajero, self).__init__(parent)

        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)

        self.clienteLabel = QtGui.QLabel("Nombre cliente", self)
        self.clienteText = QtGui.QLineEdit(self)
        self.idLabel = QtGui.QLabel("RUT", self)
        self.idText = QtGui.QLineEdit(self)
        self.gastadoLabel = QtGui.QLabel("Gastado", self)
        self.gastadoText = QtGui.QLineEdit(self)

        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.addWidget(self.clienteLabel)
        self.verticalLayout.addWidget(self.clienteText)
        self.verticalLayout.addWidget(self.idLabel)
        self.verticalLayout.addWidget(self.idText)
        self.verticalLayout.addWidget(self.gastadoLabel)
        self.verticalLayout.addWidget(self.gastadoText)
        self.verticalLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self.serializarCliente)
        self.buttonBox.rejected.connect(self.close)

    def serializarCliente(self):
        #####

        # Completar

        #####

        self.clienteText.setText("")
        self.idText.setText("")
        self.gastadoText.setText("")


class VentanaAdmin(QtGui.QDialog):

    def __init__(self, parent=None):
        super(VentanaAdmin, self).__init__(parent)

        self.archivoButton = QtGui.QPushButton("TOP-LIST")
        self.archivoButton.clicked.connect(self.generarArchivo)

        self.cancelButton = QtGui.QPushButton("Cancel")
        self.cancelButton.clicked.connect(self.close)

        self.horizontalLayout = QtGui.QVBoxLayout(self)
        self.horizontalLayout.addWidget(self.archivoButton)
        self.horizontalLayout.addWidget(self.cancelButton)

    def generarArchivo(self):

        #####

        # Completar

        #####
        pass


class Input(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Input, self).__init__(parent)

        self.userNameText = QtGui.QLineEdit(self)

        self.pushButtonWindow = QtGui.QPushButton(self)
        self.pushButtonWindow.setText("Iniciar Sesión")
        self.pushButtonWindow.clicked.connect(self.on_pushButton_clicked)

        self.layout = QtGui.QHBoxLayout(self)
        self.layout.addWidget(self.userNameText)
        self.layout.addWidget(self.pushButtonWindow)

    @QtCore.pyqtSlot()
    def on_pushButton_clicked(self):
        #####

        # Completar

        #####
        pass


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('Log-in WM')

    main = Input()
    main.show()

    sys.exit(app.exec_())