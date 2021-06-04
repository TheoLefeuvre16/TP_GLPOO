# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Sokaradian\skrd\ESIEA\GLPOO\TP_GLPOO\list_seller_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from view.Visiteur import list_article


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, visiteur_controller):
        self.database = visiteur_controller
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(347, 390)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.list_seller_widget = QtWidgets.QListWidget(self.centralwidget)
        self.list_seller_widget.setGeometry(QtCore.QRect(80, 50, 201, 192))
        self.list_seller_widget.setObjectName("list_seller_widget")

        self.valid_seller_button = QtWidgets.QPushButton(self.centralwidget)
        self.valid_seller_button.setGeometry(QtCore.QRect(130, 270, 91, 23))
        self.valid_seller_button.setObjectName("valid_seller_button")
        self.valid_seller_button.clicked.connect(self.clicked)
        self.listlayout = QtWidgets.QGridLayout()
        self.listwidget = QtWidgets.QListWidget()
        print("seller - half setup")
        self.member_mapping = {}
        self.layout = QtWidgets.QHBoxLayout()

        self.list()

        print("after list")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def list(self):
        print("call")
        index = 0
        print(self.database.list_seller())
        for member in self.database.list_seller():
            print(member['id_personne'])
            nom = self.database.get_seller(member['id_personne'])
            self.list_seller_widget.insertItem(index, "* %s" % (
                nom['firstname']))
            print("ici")
            self.member_mapping[index] = member
            index += 1

        self.list_seller_widget.clicked.connect(self.clicked)
        self.list_seller_widget.resize(self.list_seller_widget.sizeHint())
        self.list_seller_widget.move(0, 60)
        self.listlayout.addWidget(self.listwidget)
        self.layout.addLayout(self.listlayout)
        print("on en sort")

    def clicked(self):
        print(self.list_seller_widget.currentRow())
        print(self.member_mapping[self.list_seller_widget.currentRow()]['id'])
        print("vendeur - test")
        self.test_w = QtWidgets.QWidget()
        self.ui_test = list_article.Ui_MainWindow()
        self.ui_test.setupUi(self.test_w, self.database)
        self.test_w.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.valid_seller_button.setText(_translate("MainWindow", "Voir les articles"))
