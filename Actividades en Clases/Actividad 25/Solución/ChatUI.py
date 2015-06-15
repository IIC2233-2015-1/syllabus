#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
import threading


class Example(QtGui.QWidget):

    def __init__(self, chat, nombre, senal):
        super(Example, self).__init__()

        self.chat = chat
        self.senal = senal

        self.nombre = nombre
        self.initUI()


    def initUI(self):
        self.senal.connect(self.setPhoto)
        self.dimension = 400

        button = QtGui.QPushButton('Subir Foto')
        button.setFixedSize(150, 50)
        button.clicked.connect(self.buttonClicked)

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(button)

        self.label = QtGui.QLabel(' ')
        self.label.setFixedSize(self.dimension,self.dimension)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.setAutoFillBackground(True)
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(QtCore.QRectF(self.rect()).topLeft(),QtCore.QRectF(self.rect()).topRight())
        gradient.setColorAt(0,	QtCore.Qt.green)
        gradient.setColorAt(0.5,	QtCore.Qt.darkGreen)
        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(gradient))
        self.setPalette(palette)

        self.setGeometry(0, 0, self.dimension, self.dimension)
        self.centerOnScreen()
        self.setWindowTitle(self.nombre)
        self.show()


    def buttonClicked(self):
        self.chat.path = QtGui.QFileDialog.getOpenFileName(self)
        if not self.chat.path =='':
            self.chat.pressed = True

    def centerOnScreen (self):
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - self.dimension/2,
                  (resolution.height() / 2) - self.dimension/2)

    def setPhoto(self):
        self.myPixmap = QtGui.QPixmap(self.chat.get_path())
        self.label.setPixmap(self.myPixmap)
        self.label.setScaledContents(True)


class Chat(QtCore.QObject):

    senal = QtCore.pyqtSignal()

    def __init__(self, nombre):
        super(Chat, self).__init__()
        self.path = ""
        self.nombre = nombre
        self.pressed = False

    def inicializar_interfaz(self):
        self.run()

    def run(self):
        app = QtGui.QApplication(sys.argv)
        self.ex = Example(self, self.nombre, self.senal)
        sys.exit(app.exec_())

    def get_path(self):
        return self.path

    def update_image(self, path):
        self.path = path
        self.senal.emit()

    def subir_pressed(self):
        if self.pressed:
            self.pressed = False
            return True
        return False




