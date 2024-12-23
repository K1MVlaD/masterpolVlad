from BD import SQL
from avtorization import Ui_Login
from menu import Ui_Menu
from postacshiki import Ui_Suppliers
from dobnewpostavshik import Ui_AddNewSupplier
from partner import Ui_Partner
from zakazi import Ui_Zayavki
from dobnewpartner import Ui_AddNewPartner
from dobnewzakaz import Ui_AddNewZakaz
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import re
import sys


class Work(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.BD = SQL()
        self.ui_Login = QtWidgets.QMainWindow()
        self.ui_L = Ui_Login()
        self.ui_L.setupUi(self.ui_Login)
        self.ui_Login.show()
        self.ui_L.pushButton.clicked.connect(self.login)
        self.ui_Menu = QtWidgets.QMainWindow()
        self.ui_M = Ui_Menu()
        self.ui_M.setupUi(self.ui_Menu)
        self.ui_M.suppliersButton.clicked.connect(self.postavshiki)
        self.ui_M.partnerButton.clicked.connect(self.partneri)
        self.ui_M.suppliersButton_4.clicked.connect(self.zayavki)
        self.ui_Zayavki = QtWidgets.QMainWindow()
        self.ui_Z = Ui_Zayavki()
        self.ui_Z.setupUi(self.ui_Zayavki)
        self.ui_Z.dobnewzayavka.clicked.connect(self.dobzakazs)
        self.ui_AddNewOrder = QtWidgets.QMainWindow()
        self.ui_AddZ = Ui_AddNewZakaz()
        self.ui_AddZ.setupUi(self.ui_AddNewOrder)
        self.ui_AddZ.dobnewzakaz.clicked.connect(self.dobzakaz)
        self.ui_Suppliers = QtWidgets.QMainWindow()
        self.ui_S = Ui_Suppliers()
        self.ui_S.setupUi(self.ui_Suppliers)
        self.ui_S.addNewSupplierButton.clicked.connect(self.dobpostavshiki)
        self.ui_AddNewSupplier = QtWidgets.QMainWindow()
        self.ui_AddS = Ui_AddNewSupplier()
        self.ui_AddS.setupUi(self.ui_AddNewSupplier)
        self.ui_AddS.addNewSuppliers.clicked.connect(self.dobpostavshik)
        self.ui_Partner = QtWidgets.QMainWindow()
        self.ui_P = Ui_Partner()
        self.ui_P.setupUi(self.ui_Partner)
        self.ui_P.addNewPartnerButton.clicked.connect(self.dobpartneri)
        self.ui_AddNewPartner = QtWidgets.QMainWindow()
        self.ui_AddP = Ui_AddNewPartner()
        self.ui_AddP.setupUi(self.ui_AddNewPartner)
        self.ui_AddP.addNewPartnerButton.clicked.connect(self.dobpartner)
    def dobpostavshik(self):
        FIO = str(self.ui_AddS.FIOSuppliers.text())
        type = str(self.ui_AddS.typeSupplier.text())
        INN = str(self.ui_AddS.INNSuplier.text())
        self.BD.newpostavshik(FIO, type, INN)
        self.postavshikitabl()
        self.ui_AddNewSupplier.close()
    def dobzakaz(self):
        name = str(self.ui_AddZ.namezakaza.text())
        idpart = int(self.ui_AddZ.idpart.text())
        idprod = int(self.ui_AddZ.idprod.text())
        kol = int(self.ui_AddZ.kolichestvo.text())
        self.BD.dobzakaz(name, idpart, idprod, kol)
        self.zayavkitabl()
        self.ui_AddNewOrder.close()
    def dobpartner(self):
        name = str(self.ui_AddP.NameCompany.text())
        fio = str(self.ui_AddP.FIODirector.text())
        email = str(self.ui_AddP.email.text())
        num = str(self.ui_AddP.number.text())
        addres = str(self.ui_AddP.address.text())
        inn = str(self.ui_AddP.INN.text())
        rate = str(self.ui_AddP.rating.text())
        self.BD.dobpartner(name, fio, email, num, addres, inn, rate)
        self.partneritabl()
        self.ui_AddNewPartner.close()
    def zayavki(self):
        self.ui_Zayavki.show()
        self.zayavkitabl()
    def partneri(self):
        self.ui_Partner.show()
        self.partneritabl()
    def postavshiki(self):
        self.ui_Suppliers.show()
        self.postavshikitabl()
    def dobpartneri(self):
        self.ui_AddNewPartner.show()
    def dobpostavshiki(self):
        self.ui_AddNewSupplier.show()
    def dobzakazs(self):
        self.ui_AddNewOrder.show()
    def login(self):
        fio = str(self.ui_L.lineEdit.text())
        password = str(self.ui_L.lineEdit_2.text())
        itog = self.BD.login(fio, password)
        if itog:
            self.ui_Menu.show()
            self.ui_Login.close()
    def partneritabl(self):
        part = self.BD.pokaz_partneri()
        self.ui_P.tablePartner.clear()
        self.ui_P.tablePartner.setRowCount(len(part))
        self.ui_P.tablePartner.setSelectionMode(QtWidgets.QTableWidget.NoSelection)
        for i in range(len(part)):
            for j in range(9):
                self.ui_P.tablePartner.setItem(i, j, QtWidgets.QTableWidgetItem(str(part[i][j])))
        name = ['№', 'Тип', 'Название', 'Директор', 'Почта', 'Телефон', 'Адрес', 'ИНН', 'Рейтинг']
        self.ui_P.tablePartner.setHorizontalHeaderLabels(name)
    def postavshikitabl(self):
        post = self.BD.pokaz_postavshiki()
        self.ui_S.tableSuppliers.clear()
        self.ui_S.tableSuppliers.setRowCount(len(post))
        self.ui_S.tableSuppliers.setSelectionMode(QtWidgets.QTableWidget.NoSelection)
        for i in range(len(post)):
            for j in range(5):
                self.ui_S.tableSuppliers.setItem(i, j, QtWidgets.QTableWidgetItem(str(post[i][j])))
        name = ['№', 'ФИО', 'История', 'Тип', 'ИНН']
        self.ui_S.tableSuppliers.setHorizontalHeaderLabels(name)
    def zayavkitabl(self):
        zay = self.BD.pokaz_zakazi()
        self.ui_Z.tableZayavki.clear()
        self.ui_Z.tableZayavki.setRowCount(len(zay))
        self.ui_Z.tableZayavki.setSelectionMode(QtWidgets.QTableWidget.NoSelection)
        for i in range(len(zay)):
            for j in range(6):
                self.ui_Z.tableZayavki.setItem(i, j, QtWidgets.QTableWidgetItem(str(zay[i][j])))
        name = ['№', 'Название', 'Партнёр', 'Продукты', 'Количество', 'Статус']
        self.ui_Z.tableZayavki.setHorizontalHeaderLabels(name)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Work()
    myapp.show()
    sys.exit(app.exec())