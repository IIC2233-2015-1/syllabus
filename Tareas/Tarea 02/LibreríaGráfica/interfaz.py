import sys
from PyQt4.QtGui import QGridLayout, QLabel, QFrame, QListWidgetItem
from PyQt4.QtGui import QSlider, QLCDNumber, QLineEdit, QListWidget
from PyQt4.QtCore import pyqtSignal, QObject
from PyQt4.QtGui import QColor, QApplication, QWidget, QPushButton


class Signal(QObject):
    sig = pyqtSignal(object)


class Consultas(QFrame):

    def __init__(self, func):
        super().__init__()
        self.consulta_actual = 0
        self.funciones = [f for f in func]
        self.initUI()

    def initUI(self):
        self.setFixedSize(830, 120)
        self.setStyleSheet(
            """
            QWidget{ background-color: #FFFFFF; border:0px; }
            QLineEdit{ border: 1px solid #000099;}
            QListWidget{ border: 1px solid #000099;}
            QPushButton{ border: 1px solid #000099;}
            QPushButton{background-color: #FFCC33; color: #000099; }
            QPushButton:pressed { background-color: #FFFF00; }
            """)

        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.grid.setSpacing(5)

        # Botones
        self.boton = QPushButton("¡Click y descubre!")
        self.atras = QPushButton("◄")
        self.adelante = QPushButton("►")

        # Conexiones
        self.boton.clicked.connect(self.clicked)
        self.atras.clicked.connect(self.retroceder)
        self.adelante.clicked.connect(self.avanzar)

        # Lista de consultas
        self.args = [("1.Cantidad de ubicaciones por región:",
                      "Ubicación", "Región"),
                     ("2.Regiones sin ubicaciones:", "Ubicaciones:",
                      "Región:"),
                     ("3.Ruta de ubicacion1 a ubicacion2",
                      "Ubicación 1:", "Ubicación 2:"),
                     ("4.Cantidad de un tipo de ubicación a una distancia",
                      "Ubicación", "Cantidad de sub-grillas:"),
                     ("5.Distancia hasta n ubicaciones de un tipo:",
                      "Ubicación", "Cantidad")]

        self.consulta(*self.args[self.consulta_actual])

    def consulta(self, titulo, label1, label2):
        label_consulta = QLabel(titulo)
        label1 = QLabel(label1)
        label2 = QLabel(label2)
        label3 = QLabel("Respuesta:")
        self.arg1 = QLineEdit()
        self.arg2 = QLineEdit()
        self.respuesta = QListWidget(self)

        self.limpiar_grid(self.grid)
        self.grid.addWidget(label_consulta, 0, 0)
        self.grid.addWidget(self.boton, 1, 0)
        self.grid.addWidget(self.atras, 2, 0)
        self.grid.addWidget(self.adelante, 3, 0)
        self.grid.addWidget(label1, 0, 1)
        self.grid.addWidget(self.arg1, 1, 1)
        self.grid.addWidget(label2, 2, 1)
        self.grid.addWidget(self.arg2, 3, 1)
        self.grid.addWidget(label3, 0, 3)
        self.grid.addWidget(self.respuesta, 1, 3, 3, 1)

    def clicked(self):

        try:
            tupla = (self.arg1.text(), self.arg2.text())
            valor1 = tupla[0].split(sep=",")
            valor2 = tupla[1].split(sep=",")
            tupla = (valor1, valor2)
            if tupla[0] and tupla[1]:
                lista = (self.funciones[self.consulta_actual])(tupla)
                self.respuesta.clear()
                if isinstance(lista, list):
                    for x in lista:
                        item = QListWidgetItem(str(x))
                        self.respuesta.addItem(item)
                else:
                    item = QListWidgetItem(str(lista))
                    self.respuesta.addItem(item)

        except:
            print("Ooops!")

    def avanzar(self):
        self.consulta_actual = (self.consulta_actual + 1) % 5
        self.consulta(*self.args[self.consulta_actual])

    def retroceder(self):
        valor = self.consulta_actual - 1
        self.consulta_actual = 4 if valor < 0 else valor
        self.consulta(*self.args[self.consulta_actual])

    def limpiar_grid(self, grid):
        for i in reversed(range(grid.count())):
            grid.itemAt(i).widget().setParent(None)


class Navegador(QFrame):

    def __init__(self, lcd):
        super().__init__()
        self.signal = Signal()
        self.initUI(lcd)

    def initUI(self, lcd):
        self.setStyleSheet(
            """
            QWidget{ background-color: #FFFFFF; border:1px solid #000099; }
            QPushButton{background-color: #FFCC33; color: #000099; }
            QPushButton:pressed { background-color: #FFFF00; }
            """)
        self.setFixedSize(220, 220)

        grid = QGridLayout()
        self.setLayout(grid)

        arrow_up = QPushButton("▲")
        arrow_left = QPushButton("◄")
        arrow_right = QPushButton("►")
        arrow_down = QPushButton("▼")

        arrow_up.clicked.connect(self.clicked)
        arrow_left.clicked.connect(self.clicked)
        arrow_right.clicked.connect(self.clicked)
        arrow_down.clicked.connect(self.clicked)

        elementos = [None, arrow_up, None, arrow_left,
                     lcd, arrow_right, None, arrow_down, None]

        coords = [(i, j) for i in range(3) for j in range(3)]

        for coords, element in zip(coords, elementos):
            if not element:
                continue
            grid.addWidget(element, *coords)

    def clicked(self):
        sender = self.sender()
        direccion = sender.text()
        tupla = (0, 0)
        if direccion == "▲":
            tupla = (0, 1)
        elif direccion == "◄":
            tupla = (-1, 0)
        elif direccion == "►":
            tupla = (1, 0)
        elif direccion == "▼":
            tupla = (0, -1)
        self.signal.sig.emit(tupla)

    def connect(self, func):
        self.signal.sig.connect(func)


class Mapa(QFrame):

    def __init__(self, mapa_inicial, func_zoom, func_move):
        super().__init__()
        self.__good_map = mapa_inicial
        self.__mapa = mapa_inicial
        self.__func_zoom = func_zoom
        self.__func_move = func_move
        self.initUI()

    def initUI(self):
        self.setStyleSheet(
            """
            QWidget{background-color: #000000;border: 0px}
            QLabel{background-color: #FFAA33;
            qproperty-alignment: AlignCenter; 
            font-size: 11px;}
            """)

        self.setFixedSize(560, 560)

        self.__mapa_grid = QGridLayout()
        self.__mapa_grid.setSpacing(1)
        self.setLayout(self.__mapa_grid)
        self.imprimir_mapa()

    def zooming(self):
        sender = self.sender()
        valor = sender.value()
        self.__mapa = self.__func_zoom(valor)
        sender.setToolTip(str(valor))
        self.imprimir_mapa()

    def moving(self, valor):
        self.__mapa = self.__func_move(valor)
        self.imprimir_mapa()

    def imprimir_mapa(self):
        mapa = self.__mapa
        self.limpiar_grid(self.__mapa_grid)
        try:
            size = str(int(36/len(mapa)*3))
            for y in range(len(mapa)):
                for x in range(len(mapa[y])):
                    position = (y, x)
                    label = QLabel(str(mapa[y][x]))
                    style = "QLabel{font-size: "+size+"px;}"
                    label.setStyleSheet(style)
                    self.__mapa_grid.addWidget(label, *position)

        except:
            print("Ooops...")

    def limpiar_grid(self, grid):
        """
        http://stackoverflow.com/questions/4528347/clear-all-widgets-in-a-layout-in-pyqt
        """
        for i in reversed(range(grid.count())):
            grid.itemAt(i).widget().setParent(None)


class MainWindow(QWidget):

    def __init__(self, func_zoom, func_move, mapa_inicial, funcs):
        super().__init__()
        self.__func_zoom = func_zoom
        self.__func_move = func_move
        self.__mapa = mapa_inicial
        self.__funcs = funcs

        self.initUI()

    def initUI(self):
        self.setStyleSheet(
            """
            QWidget{ background-color: #FFCC33;
            border:1px solid #000099; }
            """
        )
        self.setFixedSize(850, 700)
        self.setWindowTitle('Tarea 2')

        # Elementos de la ventana
        lcd = QLCDNumber()
        self.mapa = Mapa(self.__mapa, self.__func_zoom, self.__func_move)
        self.barra_zoom = QSlider()
        self.navegador = Navegador(lcd)
        self.consultas = Consultas(self.__funcs)

        # Colores
        palette = lcd.palette()
        palette.setColor(palette.Light, QColor(255, 204, 51))
        lcd.setPalette(palette)

        # Conexiones
        self.barra_zoom.valueChanged.connect(self.mapa.zooming)
        self.barra_zoom.valueChanged.connect(lcd.display)

        self.navegador.connect(self.mapa.moving)

        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        # Agregar elementos.
        self.grid.addWidget(self.mapa, 0, 0, 2, 3)
        self.grid.addWidget(self.barra_zoom, 0, 4, 1, 1)
        self.grid.addWidget(self.navegador, 1, 3, 1, 3)
        self.grid.addWidget(self.consultas, 2, 0)

        self.setLayout(self.grid)
        self.show()


class Interfaz:

    def __init__(self, func_zoom, func_move, mapa_inicial, funcs):
        """
        Interfaz grafica de la Tarea 2.
        func_zoom: funcion encargada de hacer zoom sobre el mapa
        func_move: funcion encargada de navegar por el mapa
        mapa_inicial: primera vision del mapa

        """
        self.func_zoom = func_zoom
        self.func_move = func_move
        self.mapa_inicial = mapa_inicial
        self.funcs = funcs

    def run(self):
        app = QApplication(sys.argv)
        window = MainWindow(
            self.func_zoom, self.func_move, self.mapa_inicial, self.funcs)
        sys.exit(app.exec_())
