import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *  

from basic_math import math


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(QSize(400, 420))
        self.setStyleSheet("QPushButton{height: 53px; width: 53px; border-radius: 26px; border: 1px solid black}")
        self.setGeometry(100, 100, 600, 400)
        self.ui_components()
        self.show()

    def ui_components(self):

        # Digit buttons
        NineButton = DigitButton("9", self)
        NineButton.setGeometry(262, 183, 53, 53)

        EightButton = DigitButton("8", self)
        EightButton.setGeometry(199, 183, 53, 53)

        SevenButton = DigitButton("7", self)
        SevenButton.setGeometry(136, 183, 53, 53)

        SixButton = DigitButton("6", self)
        SixButton.setGeometry(262, 240, 53, 53)

        FiveButton = DigitButton("5", self)
        FiveButton.setGeometry(199, 240, 53, 53)

        FourButton = DigitButton("4", self)
        FourButton.setGeometry(136, 240, 53, 53)

        ThreeButton = DigitButton("3", self)
        ThreeButton.setGeometry(262, 297, 53, 53)

        TwoButton = DigitButton("2", self)
        TwoButton.setGeometry(199, 297, 53, 53)

        OneButton = DigitButton("1", self)
        OneButton.setGeometry(136, 297, 53, 53)

        NullButton = DigitButton("0", self)
        NullButton.setGeometry(199, 354, 53, 53)


        # Math operation buttons
        MulButton = MathOperationButton("*", self)
        MulButton.setGeometry(325, 240, 53, 53)

        PlusButton = MathOperationButton("+", self)
        PlusButton.setGeometry(325, 297, 53, 53)

        MinusButton = MathOperationButton("-", self)
        MinusButton.setGeometry(325, 354, 53, 53)

        DivisionButton = MathOperationButton("/", self)
        DivisionButton.setGeometry(325, 183, 53, 53)

        GreaterButton = MathOperationButton(">", self)
        GreaterButton.setGeometry(73, 354, 53, 53)

        LessButton = MathOperationButton("<", self)
        LessButton.setGeometry(10, 354, 53, 53)

        BinaryButton = MathOperationButton("BIN", self)
        BinaryButton.setGeometry(10, 240, 53, 53)

        ProcentButton = MathOperationButton("%", self)
        ProcentButton.setGeometry(73, 240, 53, 53)

        EqualButton = MathOperationButton("=", self)
        EqualButton.setGeometry(262, 354, 53, 53)

        LeftParButton = MathOperationButton("(", self)
        LeftParButton.setGeometry(10, 183, 53, 53)

        PiButton = MathOperationButton("π", self)
        PiButton.setGeometry(10, 297, 53, 53)

        CommaButton = MathOperationButton(",", self)
        CommaButton.setGeometry(136, 354, 53, 53)

        RightParButton = MathOperationButton(")", self)
        RightParButton.setGeometry(73, 183, 53, 53)

        ExponentButton = MathOperationButton("e", self)
        ExponentButton.setGeometry(73, 297, 53, 53)

        # Functional buttons:
        DeleteButton = FunctionButton("←", self)
        DeleteButton.setGeometry(73, 126, 53, 53)

        ClearButton = FunctionButton("C", self)
        ClearButton.setGeometry(10, 126, 53, 53)

        FuncSwitchButton = FunctionButton("f", self)
        FuncSwitchButton.setGeometry(325, 126, 53, 53)



    # # action method
    # def action(self):
    #     op = math.BasicMath(1)
    #     print(op.add(2))


class Button(QPushButton):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.name = name
        self.setFont(QFont('Cascadia Mono', 18))
        

# subclass of class Button for digit button
class DigitButton(Button):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.setStyleSheet(" border-style: none; border-radius: 26px; background-color: #9893DA; color: #F2F6F5;")


# subclass of class Button for math operation button        
class MathOperationButton(Button):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.setStyleSheet("border-style: none; border-radius: 26px; background-color: #72727E; color: #242224;")
           
            
# subclass of class Button for functional button        
class FunctionButton(Button):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.setStyleSheet("border-style: none; border-radius: 26px; background-color: #797A9E; color: #F2F6F5;")


# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
window.show()

# start the app
sys.exit(App.exec())