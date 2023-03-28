# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(389, 420)
        MainWindow.setStyleSheet("")
        self.Main = QtWidgets.QWidget(MainWindow)
        self.Main.setObjectName("Main")
        self.BasicFrame = QtWidgets.QFrame(self.Main)
        self.BasicFrame.setGeometry(QtCore.QRect(0, 0, 390, 420))
        self.BasicFrame.setStyleSheet("background-color: #F2F6F5;")
        self.BasicFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BasicFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BasicFrame.setObjectName("BasicFrame")
        self.EqualsButton = QtWidgets.QPushButton(self.BasicFrame)
        self.EqualsButton.setGeometry(QtCore.QRect(262, 354, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.EqualsButton.setFont(font)
        self.EqualsButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px; background-color: #72727E; color: #242224;\n"
"")
        self.EqualsButton.setObjectName("EqualsButton")
        self.MinusButton = QtWidgets.QPushButton(self.BasicFrame)
        self.MinusButton.setGeometry(QtCore.QRect(325, 354, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.MinusButton.setFont(font)
        self.MinusButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px; background-color: #72727E; color: #242224;\n"
"")
        self.MinusButton.setObjectName("MinusButton")
        self.LeftParButton = QtWidgets.QPushButton(self.BasicFrame)
        self.LeftParButton.setGeometry(QtCore.QRect(10, 183, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.LeftParButton.setFont(font)
        self.LeftParButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px; background-color: #72727E; color: #242224;\n"
"")
        self.LeftParButton.setObjectName("LeftParButton")
        self.FourButton = QtWidgets.QPushButton(self.BasicFrame)
        self.FourButton.setGeometry(QtCore.QRect(136, 240, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.FourButton.setFont(font)
        self.FourButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px;\n"
" background-color: #9893DA; color: #F2F6F5;")
        self.FourButton.setObjectName("FourButton")
        self.CommaButton = QtWidgets.QPushButton(self.BasicFrame)
        self.CommaButton.setGeometry(QtCore.QRect(136, 354, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.CommaButton.setFont(font)
        self.CommaButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px; background-color: #72727E; color: #242224;\n"
"")
        self.CommaButton.setObjectName("CommaButton")
        self.ProcentButton = QtWidgets.QPushButton(self.BasicFrame)
        self.ProcentButton.setGeometry(QtCore.QRect(73, 240, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.ProcentButton.setFont(font)
        self.ProcentButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px; background-color: #72727E; color: #242224;\n"
"")
        self.ProcentButton.setObjectName("ProcentButton")
        self.FunctionButton = QtWidgets.QPushButton(self.BasicFrame)
        self.FunctionButton.setGeometry(QtCore.QRect(325, 126, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.FunctionButton.setFont(font)
        self.FunctionButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px; background-color: #797A9E; color: #F2F6F5;\n"
"")
        self.FunctionButton.setObjectName("FunctionButton")
        self.SevenButton = QtWidgets.QPushButton(self.BasicFrame)
        self.SevenButton.setGeometry(QtCore.QRect(136, 183, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.SevenButton.setFont(font)
        self.SevenButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px;\n"
" background-color: #9893DA; color: #F2F6F5;")
        self.SevenButton.setObjectName("SevenButton")
        self.RightParButton = QtWidgets.QPushButton(self.BasicFrame)
        self.RightParButton.setGeometry(QtCore.QRect(73, 183, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.RightParButton.setFont(font)
        self.RightParButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px; background-color: #72727E; color: #242224;\n"
"")
        self.RightParButton.setObjectName("RightParButton")
        self.PiButton = QtWidgets.QPushButton(self.BasicFrame)
        self.PiButton.setGeometry(QtCore.QRect(10, 297, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.PiButton.setFont(font)
        self.PiButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px; background-color: #72727E; color: #242224;\n"
"")
        self.PiButton.setObjectName("PiButton")
        self.ThreeButton = QtWidgets.QPushButton(self.BasicFrame)
        self.ThreeButton.setGeometry(QtCore.QRect(262, 297, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.ThreeButton.setFont(font)
        self.ThreeButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px;\n"
" background-color: #9893DA; color: #F2F6F5;")
        self.ThreeButton.setObjectName("ThreeButton")
        self.FiveButton = QtWidgets.QPushButton(self.BasicFrame)
        self.FiveButton.setGeometry(QtCore.QRect(199, 240, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.FiveButton.setFont(font)
        self.FiveButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px;\n"
" background-color: #9893DA; color: #F2F6F5;")
        self.FiveButton.setObjectName("FiveButton")
        self.DeleteButton = QtWidgets.QPushButton(self.BasicFrame)
        self.DeleteButton.setGeometry(QtCore.QRect(73, 126, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.DeleteButton.setFont(font)
        self.DeleteButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px;\n"
" background-color: #797A9E; color: #F2F6F5;")
        self.DeleteButton.setObjectName("DeleteButton")
        self.XButton = QtWidgets.QPushButton(self.BasicFrame)
        self.XButton.setGeometry(QtCore.QRect(10, 240, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.XButton.setFont(font)
        self.XButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px; background-color: #72727E; color: #242224;\n"
"")
        self.XButton.setObjectName("XButton")
        self.NullButton = QtWidgets.QPushButton(self.BasicFrame)
        self.NullButton.setGeometry(QtCore.QRect(199, 354, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.NullButton.setFont(font)
        self.NullButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px;\n"
" background-color: #9893DA; color: #F2F6F5;")
        self.NullButton.setObjectName("NullButton")
        self.EButton = QtWidgets.QPushButton(self.BasicFrame)
        self.EButton.setGeometry(QtCore.QRect(73, 297, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.EButton.setFont(font)
        self.EButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px; background-color: #72727E; color: #242224;\n"
"")
        self.EButton.setObjectName("EButton")
        self.OneButton = QtWidgets.QPushButton(self.BasicFrame)
        self.OneButton.setGeometry(QtCore.QRect(136, 297, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.OneButton.setFont(font)
        self.OneButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px;\n"
" background-color: #9893DA; color: #F2F6F5;")
        self.OneButton.setObjectName("OneButton")
        self.MultiplicationButton = QtWidgets.QPushButton(self.BasicFrame)
        self.MultiplicationButton.setGeometry(QtCore.QRect(325, 240, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.MultiplicationButton.setFont(font)
        self.MultiplicationButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px; background-color: #72727E; color: #242224;\n"
"")
        self.MultiplicationButton.setObjectName("MultiplicationButton")
        self.NineButton = QtWidgets.QPushButton(self.BasicFrame)
        self.NineButton.setGeometry(QtCore.QRect(262, 183, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.NineButton.setFont(font)
        self.NineButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px;\n"
" background-color: #9893DA; color: #F2F6F5;")
        self.NineButton.setObjectName("NineButton")
        self.TwoButton = QtWidgets.QPushButton(self.BasicFrame)
        self.TwoButton.setGeometry(QtCore.QRect(199, 297, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.TwoButton.setFont(font)
        self.TwoButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px;\n"
" background-color: #9893DA; color: #F2F6F5;")
        self.TwoButton.setObjectName("TwoButton")
        self.SixButton = QtWidgets.QPushButton(self.BasicFrame)
        self.SixButton.setGeometry(QtCore.QRect(262, 240, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.SixButton.setFont(font)
        self.SixButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px;\n"
"background-color: #9893DA; color: #F2F6F5;")
        self.SixButton.setObjectName("SixButton")
        self.EightButton = QtWidgets.QPushButton(self.BasicFrame)
        self.EightButton.setGeometry(QtCore.QRect(199, 183, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.EightButton.setFont(font)
        self.EightButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px;\n"
" background-color: #9893DA; color: #F2F6F5;")
        self.EightButton.setObjectName("EightButton")
        self.ClearButton = QtWidgets.QPushButton(self.BasicFrame)
        self.ClearButton.setGeometry(QtCore.QRect(10, 126, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.ClearButton.setFont(font)
        self.ClearButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px;\n"
" background-color: #797A9E; color: #F2F6F5;")
        self.ClearButton.setObjectName("ClearButton")
        self.GreaterButton = QtWidgets.QPushButton(self.BasicFrame)
        self.GreaterButton.setGeometry(QtCore.QRect(73, 354, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.GreaterButton.setFont(font)
        self.GreaterButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px; background-color: #72727E; color: #242224;\n"
"")
        self.GreaterButton.setObjectName("GreaterButton")
        self.LessButton = QtWidgets.QPushButton(self.BasicFrame)
        self.LessButton.setGeometry(QtCore.QRect(10, 354, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.LessButton.setFont(font)
        self.LessButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px; background-color: #72727E; color: #242224;\n"
"")
        self.LessButton.setObjectName("LessButton")
        self.DivisionButton = QtWidgets.QPushButton(self.BasicFrame)
        self.DivisionButton.setGeometry(QtCore.QRect(325, 183, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.DivisionButton.setFont(font)
        self.DivisionButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px; background-color: #72727E; color: #242224;\n"
"")
        self.DivisionButton.setObjectName("DivisionButton")
        self.PlusButton = QtWidgets.QPushButton(self.BasicFrame)
        self.PlusButton.setGeometry(QtCore.QRect(325, 297, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(18)
        self.PlusButton.setFont(font)
        self.PlusButton.setStyleSheet("border-style: none;\n"
"border-radius: 26px; background-color: #72727E; color: #242224;\n"
"")
        self.PlusButton.setObjectName("PlusButton")
        self.Background = QtWidgets.QFrame(self.BasicFrame)
        self.Background.setGeometry(QtCore.QRect(0, 120, 390, 330))
        self.Background.setStyleSheet("background-color: #D9D9D9; border-radius: 30;")
        self.Background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Background.setObjectName("Background")
        self.Background.raise_()
        self.EqualsButton.raise_()
        self.MinusButton.raise_()
        self.LeftParButton.raise_()
        self.FourButton.raise_()
        self.CommaButton.raise_()
        self.ProcentButton.raise_()
        self.FunctionButton.raise_()
        self.SevenButton.raise_()
        self.RightParButton.raise_()
        self.PiButton.raise_()
        self.ThreeButton.raise_()
        self.FiveButton.raise_()
        self.DeleteButton.raise_()
        self.XButton.raise_()
        self.NullButton.raise_()
        self.EButton.raise_()
        self.OneButton.raise_()
        self.MultiplicationButton.raise_()
        self.NineButton.raise_()
        self.TwoButton.raise_()
        self.SixButton.raise_()
        self.EightButton.raise_()
        self.ClearButton.raise_()
        self.GreaterButton.raise_()
        self.LessButton.raise_()
        self.DivisionButton.raise_()
        self.PlusButton.raise_()
        MainWindow.setCentralWidget(self.Main)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.EqualsButton.setText(_translate("MainWindow", "="))
        self.MinusButton.setText(_translate("MainWindow", "-"))
        self.LeftParButton.setText(_translate("MainWindow", "("))
        self.FourButton.setText(_translate("MainWindow", "4"))
        self.CommaButton.setText(_translate("MainWindow", ","))
        self.ProcentButton.setText(_translate("MainWindow", "%"))
        self.FunctionButton.setText(_translate("MainWindow", "f"))
        self.SevenButton.setText(_translate("MainWindow", "7"))
        self.RightParButton.setText(_translate("MainWindow", ")"))
        self.PiButton.setText(_translate("MainWindow", "π"))
        self.ThreeButton.setText(_translate("MainWindow", "3"))
        self.FiveButton.setText(_translate("MainWindow", "5"))
        self.DeleteButton.setText(_translate("MainWindow", "<-"))
        self.XButton.setText(_translate("MainWindow", "X"))
        self.NullButton.setText(_translate("MainWindow", "0"))
        self.EButton.setText(_translate("MainWindow", "e"))
        self.OneButton.setText(_translate("MainWindow", "1"))
        self.MultiplicationButton.setText(_translate("MainWindow", "×"))
        self.NineButton.setText(_translate("MainWindow", "9"))
        self.TwoButton.setText(_translate("MainWindow", "2"))
        self.SixButton.setText(_translate("MainWindow", "6"))
        self.EightButton.setText(_translate("MainWindow", "8"))
        self.ClearButton.setText(_translate("MainWindow", "C"))
        self.GreaterButton.setText(_translate("MainWindow", ">"))
        self.LessButton.setText(_translate("MainWindow", "<"))
        self.DivisionButton.setText(_translate("MainWindow", ")"))
        self.PlusButton.setText(_translate("MainWindow", "+"))
