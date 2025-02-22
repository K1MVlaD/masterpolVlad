# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\AddNewOrders.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddNewZakaz(object):
    def setupUi(self, AddNewZakaz):
        AddNewZakaz.setObjectName("AddNewZakaz")
        AddNewZakaz.resize(362, 237)
        AddNewZakaz.setLayoutDirection(QtCore.Qt.LeftToRight)
        AddNewZakaz.setStyleSheet("background-color:#123456;")
        self.centralwidget = QtWidgets.QWidget(AddNewZakaz)
        self.centralwidget.setObjectName("centralwidget")
        self.namezakaza = QtWidgets.QLineEdit(self.centralwidget)
        self.namezakaza.setGeometry(QtCore.QRect(10, 10, 341, 31))
        font = QtGui.QFont()
        font.setFamily("\"Segoe UI Black\"")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.namezakaza.setFont(font)
        self.namezakaza.setStyleSheet("border: 0px;\n"
"max-width: 700px;\n"
"background-color: #666000;\n"
"")
        self.namezakaza.setInputMask("")
        self.namezakaza.setText("")
        self.namezakaza.setObjectName("namezakaza")
        self.idpart = QtWidgets.QLineEdit(self.centralwidget)
        self.idpart.setGeometry(QtCore.QRect(10, 50, 341, 31))
        font = QtGui.QFont()
        font.setFamily("\"Segoe UI Black\"")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.idpart.setFont(font)
        self.idpart.setStyleSheet("border: 0px;\n"
"max-width: 700px;\n"
"background-color: #666000;")
        self.idpart.setInputMask("")
        self.idpart.setText("")
        self.idpart.setObjectName("idpart")
        self.dobnewzakaz = QtWidgets.QPushButton(self.centralwidget)
        self.dobnewzakaz.setGeometry(QtCore.QRect(10, 180, 71, 31))
        self.dobnewzakaz.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dobnewzakaz.setStyleSheet("QPushButton {\n"
"background-color: 666000;\n"
"\n"
"border: 6px;\n"
"color:white;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(255, 195, 97);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 195, 97);\n"
"}\n"
"\n"
"")
        self.dobnewzakaz.setText("Внести")
        self.dobnewzakaz.setObjectName("dobnewzakaz")
        self.idprod = QtWidgets.QLineEdit(self.centralwidget)
        self.idprod.setGeometry(QtCore.QRect(10, 90, 341, 31))
        font = QtGui.QFont()
        font.setFamily("\"Segoe UI Black\"")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.idprod.setFont(font)
        self.idprod.setStyleSheet("border: 0px;\n"
"max-width: 700px;\n"
"background-color: #666000;")
        self.idprod.setInputMask("")
        self.idprod.setText("")
        self.idprod.setObjectName("idprod")
        self.kolichestvo = QtWidgets.QLineEdit(self.centralwidget)
        self.kolichestvo.setGeometry(QtCore.QRect(10, 130, 341, 31))
        font = QtGui.QFont()
        font.setFamily("\"Segoe UI Black\"")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.kolichestvo.setFont(font)
        self.kolichestvo.setStyleSheet("border: 0px;\n"
"max-width: 700px;\n"
"background-color: #666000;")
        self.kolichestvo.setInputMask("")
        self.kolichestvo.setText("")
        self.kolichestvo.setObjectName("kolichestvo")
        AddNewZakaz.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AddNewZakaz)
        self.statusbar.setObjectName("statusbar")
        AddNewZakaz.setStatusBar(self.statusbar)

        self.retranslateUi(AddNewZakaz)
        QtCore.QMetaObject.connectSlotsByName(AddNewZakaz)

    def retranslateUi(self, AddNewZakaz):
        _translate = QtCore.QCoreApplication.translate
        AddNewZakaz.setWindowTitle(_translate("AddNewZakaz", "Добавление нового заказа"))
        self.namezakaza.setPlaceholderText(_translate("AddNewZakaz", "Наименование"))
        self.idpart.setPlaceholderText(_translate("AddNewZakaz", "id партнёра"))
        self.idprod.setPlaceholderText(_translate("AddNewZakaz", "id продукта"))
        self.kolichestvo.setPlaceholderText(_translate("AddNewZakaz", "Количество"))
