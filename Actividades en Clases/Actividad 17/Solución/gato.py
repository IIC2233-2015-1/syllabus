#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        grid = QtGui.QGridLayout()
        self.setLayout(grid)
        self.turno = 'X'

        for i in range(3):
            for j in range(3):
                button = QtGui.QPushButton(' ')
                button.setFixedSize(50, 50)
                grid.addWidget(button, i, j)
                button.clicked.connect(self.buttonClicked)

        self.label = QtGui.QLabel('Turno  de jugador %s' % self.turno)
        grid.addWidget(self.label, 4, 0, 1, 4)
        self.setWindowTitle('Gato')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        if sender.text() == ' ':
            if self.turno == 'X':
                sender.setText(' X ')
                self.turno = 'O'
                self.label.setText('Turno  de jugador %s' % self.turno)

            else:
                sender.setText(' O ')
                self.turno = 'X'
                self.label.setText('Turno  de jugador %s' % self.turno)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
