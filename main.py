from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton

app = QApplication([])

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.show()

mw = MainWindow()
mw.setWindowTitle('test Rufye')















app.exec()
