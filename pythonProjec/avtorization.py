from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(800, 600)
        Login.setMinimumSize(QtCore.QSize(800, 600))
        Login.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\images/Мастер пол.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setStyleSheet("background-color: #123456;")
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 70, 721, 441))
        self.groupBox.setStyleSheet("background-color:#666000;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(230, 160, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: white;\n"
"border: 0;\n"
"\n"
"padding-bottom: 10px;\n"
"border-bottom: 1px solid black;")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 230, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: white;\n"
"border: 0;\n"
"\n"
"padding-bottom: 10px;\n"
"border-bottom: 1px solid black;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 20, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(100, 100))
        self.label.setMaximumSize(QtCore.QSize(100, 100))
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        self.label.setBaseSize(QtCore.QSize(90, 5))
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".\\images/Мастер пол.ico"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(280, 310, 121, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setStyleSheet("background-color: white;\n"
"\n"
"font: 87 10pt \\\"Segoe UI Black\\\";\\n\\;\n"
"border: 6px;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 151, 51))
        font = QtGui.QFont()
        font.setFamily("\"Segoe UI Black\"")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 87 16pt \\\"Segoe UI Black\\\";\\n\\;")
        self.label_2.setObjectName("label_2")
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Вход"))
        self.lineEdit.setPlaceholderText(_translate("Login", "Login"))
        self.lineEdit_2.setPlaceholderText(_translate("Login", "Password"))
        self.pushButton.setText(_translate("Login", "Войти"))
        self.label_2.setText(_translate("Login", "MASTER POL"))
