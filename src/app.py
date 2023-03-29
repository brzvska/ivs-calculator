# importing libraries
# import PyQt6.

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *  

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
        # self.UiComponents()
        # showing all the widgets
        self.show()
        
    def render_ui(self):
        button = Button()
 
    # method for widgets
    def UiComponents(self):
        basicFrame = QtWidgets
        # creating a push button
        button = QPushButton("Math", self)
        # setting geometry of button
        button.setGeometry(16, 133, 53, 53)
        button.shadow = QTabWidget.QGra
        # adding action to a button
        button.clicked.connect(self.action)
 
    # action method
    def action(self):
        op = math.BasicMath(1)
        print(op.add(2))


class Button(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)        
        self.set_up()
        
    def set_up(self):
        font = QFont
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.setFont(font)
        
    # set the position of particular button     
    def set_button_position(self, x, y, b_height, b_width):
        self.setGeometry(x, y, b_height, b_width)     
        

# subclass of class Button for digit button
class digitButton(Button):
    def __init__(self, name):
        self.name = name
        self.setStyleSheet("background-color: #9893DA; border-style: none; border-radius: 26px; color: #F2F6F5")
        
# subclass of class Button for math operation button        
class mathOperationButton(Button):
    def __init__(self, name):
        self.name = name
        self.setStyleSheet("border-style: none; border-radius: 26px; background-color: #72727E; color: #242224;")
           
            
# subclass of class Button for functional button        
class functionButton(Button):
    def __init__(self, name):
        self.name = name
        self.setStyleSheet("border-style: none; border-radius: 26px; background-color: #797A9E; color: #F2F6F5;")

# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
window.show()

# start the app
sys.exit(App.exec())
