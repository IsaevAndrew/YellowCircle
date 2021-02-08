import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QInputDialog
from random import randrange

class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.update()


    def draw_circle(self, qp):
        qp.setBrush(QColor("yellow"))
        for i in range(1, 15):
            x = randrange(150)
            qp.drawEllipse(randrange(200), randrange(200), x, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())