import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtQuick
from PyQt5 import QtCore
from PyQt5.Qt import Qt

from basic_math import math


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # purple line
        self.line = QLineEdit(self)
        self.line.setReadOnly(True)
        self.line.move(0, 0)
        self.line.resize(400, 28)
        self.line.setStyleSheet("QLineEdit {background-color: #9893DA; border-style: none; "
                                "color: #72727E; font: 22px;}")

        # background frame
        self.back = QLineEdit(self)
        self.back.setReadOnly(True)
        self.back.move(0, 120)
        self.back.resize(400, 300)
        self.back.setStyleSheet("QLineEdit {background-color: #D9D9D9;" "border-style: none;"
                                "border-top-left-radius: 20px; border-top-right-radius: 20px;}")

        # input field
        self.textbox = QLineEdit(self)
        self.textbox.setReadOnly(True)
        self.textbox.move(12, 40)
        self.textbox.resize(376, 68)
        self.textbox.setStyleSheet("QLineEdit { background-color: #D9D9D9; border-style: none; border-radius: 20px; }")

        # setting window parameters
        self.setWindowTitle("Calculator")
        self.setFixedSize(QSize(400, 420))
        self.setGeometry(100, 100, 600, 400)

        self.label = QLabel(self)
        self.label.setGeometry(20, 50, 350, 45)
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont('Cascadia Mono', 40))
        self.label.setStyleSheet("letter-spacing: 2px; color: #72727E;")

        # filling with buttons
        self.ui_components()
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            self.action_button(1)
        elif event.key() == Qt.Key_2:
            self.action_button(2)
        elif event.key() == Qt.Key_3:
            self.action_button(3)
        elif event.key() == Qt.Key_4:
            self.action_button(4)
        elif event.key() == Qt.Key_5:
            self.action_button(5)
        elif event.key() == Qt.Key_6:
            self.action_button(6)
        elif event.key() == Qt.Key_7:
            self.action_button(7)
        elif event.key() == Qt.Key_8:
            self.action_button(8)
        elif event.key() == Qt.Key_9:
            self.action_button(9)
        elif event.key() == Qt.Key_0:
            self.action_button(0)
        elif event.key() == Qt.Key_Minus:
            self.action_button("minus")
        elif event.key() == Qt.Key_Plus:
            self.action_button("plus")
        elif event.key() == Qt.Key_multiply:
            self.action_button("mul")
        elif event.key() == Qt.Key_division:
            self.action_button("div")
        elif event.key() == Qt.Key_Slash:
            self.action_button("div")
        elif event.key() == Qt.Key_ParenLeft:
            self.action_button("left_par")
        elif event.key() == Qt.Key_ParenRight:
            self.action_button("right_par")
        elif event.key() == Qt.Key_Period:
            self.action_button("point")
        elif event.key() == Qt.Key_Delete:
            self.action_del()
        elif event.key() == Qt.Key_Percent:
            self.action_percent()
        elif event.key() == Qt.Key_Equal:
            self.action_equal()

    def ui_components(self):

        # digit buttons:
        nine_button = DigitButton("9", self)
        nine_button.setGeometry(262, 183, 53, 53)

        eight_button = DigitButton("8", self)
        eight_button.setGeometry(199, 183, 53, 53)

        seven_button = DigitButton("7", self)
        seven_button.setGeometry(136, 183, 53, 53)

        six_button = DigitButton("6", self)
        six_button.setGeometry(262, 240, 53, 53)

        five_button = DigitButton("5", self)
        five_button.setGeometry(199, 240, 53, 53)

        four_button = DigitButton("4", self)
        four_button.setGeometry(136, 240, 53, 53)

        three_button = DigitButton("3", self)
        three_button.setGeometry(262, 297, 53, 53)

        two_button = DigitButton("2", self)
        two_button.setGeometry(199, 297, 53, 53)

        one_button = DigitButton("1", self)
        one_button.setGeometry(136, 297, 53, 53)

        null_button = DigitButton("0", self)
        null_button.setGeometry(199, 354, 53, 53)

        # math operation buttons:
        mul_button = MathOperationButton("×", self)
        mul_button.setGeometry(325, 240, 53, 53)

        plus_button = MathOperationButton("+", self)
        plus_button.setGeometry(325, 297, 53, 53)

        minus_button = MathOperationButton("-", self)
        minus_button.setGeometry(325, 354, 53, 53)

        division_button = MathOperationButton("÷", self)
        division_button.setGeometry(325, 183, 53, 53)

        greater_button = MathOperationButton(">", self)
        greater_button.setGeometry(73, 354, 53, 53)

        less_button = MathOperationButton("<", self)
        less_button.setGeometry(10, 354, 53, 53)

        binary_button = MathOperationButton("BIN", self)
        binary_button.setGeometry(10, 240, 53, 53)

        percent_button = MathOperationButton("%", self)
        percent_button.setGeometry(73, 240, 53, 53)

        equal_button = MathOperationButton("=", self)
        equal_button.setGeometry(262, 354, 53, 53)

        left_par_button = MathOperationButton("(", self)
        left_par_button.setGeometry(10, 183, 53, 53)

        pi_button = MathOperationButton("π", self)
        pi_button.setGeometry(10, 297, 53, 53)

        point_button = MathOperationButton(".", self)
        point_button.setGeometry(136, 354, 53, 53)

        right_par_button = MathOperationButton(")", self)
        right_par_button.setGeometry(73, 183, 53, 53)

        exponent_button = MathOperationButton("e", self)
        exponent_button.setGeometry(73, 297, 53, 53)

        # functional buttons:
        delete_button = FunctionButton("←", self)
        delete_button.setGeometry(73, 126, 53, 53)

        clear_button = FunctionButton("C", self)
        clear_button.setGeometry(10, 126, 53, 53)

        func_switch_button = FunctionButton("f", self)
        func_switch_button.setGeometry(325, 126, 53, 53)

        # mouse manipulating with buttons
        null_button.clicked.connect(lambda: self.action_button(0))
        one_button.clicked.connect(lambda: self.action_button(1))
        two_button.clicked.connect(lambda: self.action_button(2))
        three_button.clicked.connect(lambda: self.action_button(3))
        four_button.clicked.connect(lambda: self.action_button(4))
        five_button.clicked.connect(lambda: self.action_button(5))
        six_button.clicked.connect(lambda: self.action_button(6))
        seven_button.clicked.connect(lambda: self.action_button(7))
        eight_button.clicked.connect(lambda: self.action_button(8))
        nine_button.clicked.connect(lambda: self.action_button(9))
        mul_button.clicked.connect(lambda: self.action_button("mul"))
        division_button.clicked.connect(lambda: self.action_button("div"))
        plus_button.clicked.connect(lambda: self.action_button("plus"))
        minus_button.clicked.connect(lambda: self.action_button("minus"))
        point_button.clicked.connect(lambda: self.action_button("point"))
        left_par_button.clicked.connect(lambda: self.action_button("left_par"))
        right_par_button.clicked.connect(lambda: self.action_button("right_par"))
        delete_button.clicked.connect(self.action_del)
        clear_button.clicked.connect(self.action_clear)
        percent_button.clicked.connect(self.action_percent)
        binary_button.clicked.connect(self.action_binary)
        exponent_button.clicked.connect(lambda: self.action_button("exp"))
        pi_button.clicked.connect(lambda: self.action_button("pi"))
        func_switch_button.clicked.connect(self.action_switch)

    def action_switch(self):
        pass

    # Generate text on input field
    def action_button(self, param):
        switcher = {
            0: "0",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            "pi": "π",
            "exp": "e",
            "plus": "+",
            "minus": "-",
            "mul": "×",
            "div": "÷",
            "left_par": "(",
            "right_par": ")",
            "point": ".",
        }
        text = self.label.text()
        self.label.setText(text + str(switcher.get(param)))

    # clear a single symbol
    def action_del(self):
        text = self.label.text()
        self.label.setText(text[:len(text) - 1])

    def action_clear(self):
        self.label.setText("")

    def action_percent(self):
        text = int(self.label.text())
        result = math.BasicMath.percent(self, text)
        self.label.setText(str(result))

    def action_binary(self):
        text = int(self.label.text())
        result = math.BasicMath.binary(self, text)
        self.label.setText(str(result))


class Button(QPushButton):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.name = name
        self.setFont(QFont('Cascadia Mono', 18))
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(3)
        shadow.setColor(QColor("#A5A5A5"))
        self.setGraphicsEffect(shadow)


# Subclass of class Button for digit button
class DigitButton(Button):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.setStyleSheet("border-style: none; border-radius: 26px; background-color: #9893DA; color: #F2F6F5;")


# Subclass of class Button for math operation button
class MathOperationButton(Button):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.setStyleSheet("border-style: none; border-radius: 26px; background-color: #72727E; color: #242224;")


# Subclass of class Button for functional button
class FunctionButton(Button):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.setStyleSheet("border-style: none; border-radius: 26px; background-color: #797A9E; color: #F2F6F5;")


# Subclass of class Window for advanced math mode
class AdvancedMath(Window):
    def __init__(self):
        super().__init__()
        self.AdvancedMath.ui_components()
    def ui_components(self):
        # digit buttons:
        nine_button = DigitButton("9", self)
        nine_button.setGeometry(262, 183, 53, 53)

        eight_button = DigitButton("8", self)
        eight_button.setGeometry(199, 183, 53, 53)

        seven_button = DigitButton("7", self)
        seven_button.setGeometry(136, 183, 53, 53)

        six_button = DigitButton("6", self)
        six_button.setGeometry(262, 240, 53, 53)

        five_button = DigitButton("5", self)
        five_button.setGeometry(199, 240, 53, 53)

        four_button = DigitButton("4", self)
        four_button.setGeometry(136, 240, 53, 53)

        three_button = DigitButton("3", self)
        three_button.setGeometry(262, 297, 53, 53)

        two_button = DigitButton("2", self)
        two_button.setGeometry(199, 297, 53, 53)

        one_button = DigitButton("1", self)
        one_button.setGeometry(136, 297, 53, 53)

        null_button = DigitButton("0", self)
        null_button.setGeometry(199, 354, 53, 53)

        # math operation buttons:
        cosinus_button = MathOperationButton("cos", self)
        cosinus_button.setGeometry(325, 240, 53, 53)

        tan_button = MathOperationButton("tan", self)
        tan_button.setGeometry(325, 297, 53, 53)

        ctg_button = MathOperationButton("ctg", self)
        ctg_button.setGeometry(325, 354, 53, 53)

        sinus_button = MathOperationButton("sin", self)
        sinus_button.setGeometry(325, 183, 53, 53)

        greater_button = MathOperationButton(">", self)
        greater_button.setGeometry(73, 354, 53, 53)

        less_button = MathOperationButton("<", self)
        less_button.setGeometry(10, 354, 53, 53)

        binary_button = MathOperationButton("BIN", self)
        binary_button.setGeometry(10, 240, 53, 53)

        percent_button = MathOperationButton("%", self)
        percent_button.setGeometry(73, 240, 53, 53)

        equal_button = MathOperationButton("=", self)
        equal_button.setGeometry(262, 354, 53, 53)

        left_par_button = MathOperationButton("(", self)
        left_par_button.setGeometry(10, 183, 53, 53)

        pi_button = MathOperationButton("π", self)
        pi_button.setGeometry(10, 297, 53, 53)

        point_button = MathOperationButton(".", self)
        point_button.setGeometry(136, 354, 53, 53)

        right_par_button = MathOperationButton(")", self)
        right_par_button.setGeometry(73, 183, 53, 53)

        exponent_button = MathOperationButton("e", self)
        exponent_button.setGeometry(73, 297, 53, 53)

        # functional buttons:
        delete_button = FunctionButton("←", self)
        delete_button.setGeometry(73, 126, 53, 53)

        clear_button = FunctionButton("C", self)
        clear_button.setGeometry(10, 126, 53, 53)

        func_switch_button = FunctionButton("+ - \n × ÷", self)
        func_switch_button.setGeometry(325, 126, 53, 53)


App = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(App.exec())
