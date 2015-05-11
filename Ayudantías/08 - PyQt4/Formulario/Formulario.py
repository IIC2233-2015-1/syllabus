from PyQt4 import QtGui, uic
from os import listdir

form_classes = uic.loadUiType("Ventana.ui")

ARCHIVOS = listdir('.')
DATOS = ['NAME', 'RUT', 'VALOR']
INFO = """%s
Abonos: $%d
Deudas: $%d
Neto:   $%d"""


class Formulario(form_classes[0], form_classes[1]):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.__ingresa_info = True
        self.rbtn_Abono.clicked.connect(self.rbtn_Abono_clicked)
        self.rbtn_Deuda.clicked.connect(self.rbtn_Deuda_clicked)
        self.rbtn_Info.clicked.connect(self.rbtn_Info_clicked)
        self.pbtn_Ingreso.clicked.connect(self.pbtn_Ingreso_clicked)
        self.__abrir_archivo("Abono_Usuarios.txt")

    def rbtn_Abono_clicked(self):
        self.__limpiar(True)
        self.__ingresa_info = True
        self.archivo.close()
        self.__abrir_archivo("Abono_Usuarios.txt")

    def rbtn_Deuda_clicked(self):
        self.__limpiar(True)
        self.__ingresa_info = True
        self.archivo.close()
        self.__abrir_archivo("Deuda_Usuarios.txt")

    def rbtn_Info_clicked(self):
        self.__limpiar(False)
        self.__ingresa_info = False

    def pbtn_Ingreso_clicked(self):
        nombre = self.line_Nombre.text()
        rut = self.line_Rut.text()
        valor = self.line_Valor.text()
        if self.__ingresa_info:
            if nombre == "" and rut == "" and valor == "":
                QtGui.QMessageBox.question(self, "Alerta", "Falta un campo",
                                           QtGui.QMessageBox.Accepted)
                return

            self.archivo.write('\n' + '\t\t'.join([nombre, rut, valor]))
            self.__limpiar(True)
            self.archivo.close()

        else:
            if rut == "":
                QtGui.QMessageBox.question(self, "Alerta", "Falta un campo",
                                           QtGui.QMessageBox.Accepted)
                return

            with open("Abono_Usuarios.txt", 'r') as a_u:
                nombre, abono = self.__suma_valores(rut, a_u)
            with open("Deuda_Usuarios.txt", 'r') as d_u:
                nombre, deuda = self.__suma_valores(rut, d_u)

            self.plain_Info.setPlainText(INFO %
                                         (nombre, abono, deuda, abono - deuda))

    def __suma_valores(self, rut, archivo):
        suma = 0
        nombre = ""
        lineas = archivo.readlines()
        tuplas = list(map(lambda x: tuple(x.split('\t\t')), lineas[1:]))
        for tupla in tuplas:
            if tupla[1] == rut:
                nombre = tupla[0]
                suma += int(tupla[2])
        return nombre, suma

    def __abrir_archivo(self, nombre_archivo):
        if nombre_archivo in ARCHIVOS:
            self.archivo = open(nombre_archivo, 'a')
        else:
            self.archivo = open(nombre_archivo, 'w')
            self.archivo.write('\t\t'.join(DATOS))

    def __limpiar(self, booleano):
        self.line_Nombre.clear()
        self.line_Rut.clear()
        self.line_Valor.clear()
        self.plain_Info.clear()
        self.label_Valor.setEnabled(booleano)
        self.line_Valor.setEnabled(booleano)
        self.label_Nombre.setEnabled(booleano)
        self.line_Nombre.setEnabled(booleano)
        self.plain_Info.setDisabled(booleano)
        if booleano:
            self.pbtn_Ingreso.setText('Ingresar')
        else:
            self.pbtn_Ingreso.setText('Solicitar')


app = QtGui.QApplication([])
form = Formulario()
form.show()
app.exec_()
