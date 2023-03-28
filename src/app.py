# importing libraries
# import PyQt6.

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *  
import sys

from basic_math import math
 
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        # setting title
        self.setWindowTitle("Calculator")
        # fixed window size
        self.setFixedSize(QSize(400, 420))
        # global button styling
        self.setStyleSheet("QPushButton{height: 53px; width: 53px; border-radius: 26px; border: 1px solid black}")
        # setting geometry
        self.setGeometry(100, 100, 600, 400)
        # calling method
        self.UiComponents()
        # showing all the widgets
        self.show()
 
    # method for widgets
    def UiComponents(self):
        basicFrame = QtWidgets
        # # creating a push button
        # button = QPushButton("Math", self)
        # # setting geometry of button
        # button.setGeometry(16, 133, 53, 53)
        # button.shadow = QTabWidget.QGra
        # button.setGraphicsEffect(shadow)
        # # adding action to a button
        # button.clicked.connect(self.action)
 
    # action method
    def action(self):
        op = math.BasicMath(1)
        print(op.add(2))


class Button(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)


# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())