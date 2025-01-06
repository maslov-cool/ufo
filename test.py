import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class UfoControl(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('Управление НЛО')
        self.ufo = QLabel(self)
        self.pixmap = QPixmap('ufo.png')
        self.ufo.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        # Проверяем, какая клавиша была нажата
        if event.key() == Qt.Key.Key_Up:
            if self.ufo.y() - 10 < 0:
                self.ufo.move(self.ufo.x(), 250)
            else:
                self.ufo.move(self.ufo.x(), self.ufo.y() - 10)
        elif event.key() == Qt.Key.Key_Down:
            if self.ufo.y() + 10 > 250:
                self.ufo.move(self.ufo.x(), 0)
            else:
                self.ufo.move(self.ufo.x(), self.ufo.y() + 10)
        elif event.key() == Qt.Key.Key_Left:
            if self.ufo.x() - 10 < 0:
                self.ufo.move(250, self.ufo.y())
            else:
                self.ufo.move(self.ufo.x() - 10, self.ufo.y())
        elif event.key() == Qt.Key.Key_Right:
            if self.ufo.x() + 10 > 250:
                self.ufo.move(0, self.ufo.y())
            else:
                self.ufo.move(self.ufo.x() + 10, self.ufo.y())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = UfoControl()
    program.show()
    sys.exit(app.exec())
