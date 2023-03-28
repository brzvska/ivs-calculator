from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Calculator")
        
        self.setFixedSize(QSize(390, 420))

class Frame(QFrame):
    def __init__(self):
        super().__init()
        
        self.setStyleSheet("background-color: #F2F6F5;")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()