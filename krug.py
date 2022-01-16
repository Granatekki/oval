import sys

from random import randint as ran
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 500, 450)
        self.btn = QPushButton('draw', self)
        self.btn.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        col = ran(1, 50)
        for y in range(col):
            y = ran(1, 500)
            x = ran(1, 500)
            r = ran(1, 300)
            qp.setBrush(QColor(ran(0, 255), ran(0, 255), ran(0, 255)))
            #qp.setPen(QColor('yellow'))
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
