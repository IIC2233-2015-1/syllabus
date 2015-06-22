import sys
from PyQt4 import QtGui, QtCore
import P5_I2a

__author__ = 'Javiera'


class Correo(QtGui.QWidget):

    def __init__(self):
        super(Correo, self).__init__()
        self.initUI()

    def initUI(self):
        self.button = QtGui.QPushButton('Ingresar')
        self.button.clicked.connect(self.buttonClicked)

        self.email_text = QtGui.QLineEdit()

        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.button)
        self.vbox.addWidget(self.email_text)

        self.setLayout(self.vbox)

        self.setGeometry(0, 0, 200, 200)
        self.centerOnScreen()
        self.show()

    def buttonClicked(self):
        email = self.email_text.text()
        if P5_I2a.func_verificadora(email):
            pass
            # Hacer lo que correspomde
        else:
            QtGui.QMessageBox.question(
                None,
                'ERROR',
                'Dirección de correo inválida',
                QtGui.QMessageBox.Ok
            )

    def centerOnScreen(self):
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - 10,
                  (resolution.height() / 2) - 10)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    interfaz = Correo()
    sys.exit(app.exec_())
