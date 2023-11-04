from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

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
        vline =
    def connects(self):
        pass

mw = MainWindow()
















app.exec()
