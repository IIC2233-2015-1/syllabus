import sys
from PyQt4 import QtGui


class Gato(QtGui.QWidget):

    def __init__(self):
        super(Gato, self).__init__()
        self.initUI()

    def initUI(self):
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
        self.turno = 'X'
        self.button_dict = {}
        self.rep = [[], [], []]
        self.jugadas = 0
        self.terminado = False
        for i in range(3):
            for j in range(3):
                button = QtGui.QPushButton(' ')
                button.setFixedSize(50, 50)
                grid.addWidget(button, i, j)
                self.button_dict[button] = (i, j)
                self.rep[i].append(0)
                button.clicked.connect(self.buttonClicked)

        self.label = QtGui.QLabel('Turno  de jugador %s' % self.turno)
        grid.addWidget(self.label, 4, 0, 1, 4)
        self.setWindowTitle('Gato')
        self.show()

    def buttonClicked(self):
        if not self.terminado:
            sender = self.sender()
            pos = self.button_dict[sender]
            val = self.rep[pos[0]][pos[1]]
            ant = self.turno
            if val == 0:
                self.jugadas += 1
                if self.turno == 'X':
                    sender.setText('X')
                    self.turno = 'O'
                    self.rep[pos[0]][pos[1]] = 1
                else:
                    sender.setText('O')
                    self.turno = 'X'
                    self.rep[pos[0]][pos[1]] = -1

                self.label.setText('Turno  de jugador %s' % self.turno)

                if self.check_winner(ant):
                    self.label.setText('Gano jugador %s' % ant)
                    self.terminado = True

                elif self.jugadas == 9:
                    self.label.setText('Empate')
                    self.terminado = True

    def check_winner(self, turno):
        jug = 1 if turno == 'X' else -1
        rep = self.rep
        transp = list(zip(*rep))

        # filas y columnas
        for i in range(3):
            if len(set(rep[i])) == 1 and rep[i][0] == jug:
                return True
            if len(set(transp[i])) == 1 and transp[i][0] == jug:
                return True

        # diagonales
        diag1 = [rep[i][i] for i in range(3)]
        diag2 = [rep[i][2 - i] for i in range(3)]

        if diag1[0] == jug and len(set(diag1)) == 1:
            return True

        if diag2[0] == jug and len(set(diag2)) == 1:
            return True


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Gato()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
