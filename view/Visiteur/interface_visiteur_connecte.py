# -*- coding: utf-8 -*-

#fenêtre à ouvrir lors de la connexion d'un visiteur

from PyQt5 import QtCore, QtGui, QtWidgets
from view.Visiteur import list_seller, list_guest, show_cart


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, visiteur_database):
        self.visiteur_database = visiteur_database
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(276, 268)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.guests_button = QtWidgets.QPushButton(self.centralwidget)
        self.guests_button.setGeometry(QtCore.QRect(90, 30, 75, 23))
        self.guests_button.setObjectName("guests_button")
        self.guests_button.clicked.connect(self.list_guests)

        self.sellers_button = QtWidgets.QPushButton(self.centralwidget)
        self.sellers_button.setGeometry(QtCore.QRect(90, 90, 75, 23))
        self.sellers_button.setObjectName("sellers_button")
        self.sellers_button.clicked.connect(self.list_sellers)

        self.cart_button = QtWidgets.QPushButton(self.centralwidget)
        self.cart_button.setGeometry(QtCore.QRect(90, 150, 75, 23))
        self.cart_button.setObjectName("cart_button")
        self.cart_button.clicked.connect(self.cart)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.guests_button.setText(_translate("MainWindow", "Invités"))
        self.sellers_button.setText(_translate("MainWindow", "Stands"))
        self.cart_button.setText(_translate("MainWindow", "Panier"))

    def list_guests(self):
    # creation de la fenêtre listant les invités
        self.guest_w = QtWidgets.QWidget()
        self.ui_guest = list_guest.Ui_MainWindow()
        self.ui_guest.setupUi(self.guest_w, self.visiteur_database)
        self.guest_w.show()

    def list_sellers(self):
        self.test_w = QtWidgets.QWidget()
        self.ui_test = list_seller.Ui_MainWindow()
        self.ui_test.setupUi(self.test_w, self.visiteur_database)
        self.test_w.show()

    def cart(self):
        self.cart_w = QtWidgets.QWidget()
        self.ui_cart = show_cart.Ui_MainWindow()
        self.ui_cart.setupUi(self.cart_w, self.visiteur_database)
        self.cart_w.show()
