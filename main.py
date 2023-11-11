from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt

app = QApplication([])

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.init_ui()
        self.connects()
    def set_appear(self):
        self.show()
        self.setWindowTitle('test Rufye')
    def init_ui(self):
        label = QLabel('Добро пожаловать!')
        vline = QVBoxLayout()
        vline.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        label2 = QLabel('...')
        vline.addWidget(label2, alignment=Qt.AlignmentFlag.AlignCenter)
        button =  QPushButton('Далее')
        vline.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(vline)

    def connects(self):
        pass

mw = MainWindow()
















app.exec()
