# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seller_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from view import add_article

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, seller_database, id_personne):
        self.seller_database = seller_database
        self._id_personne = id_personne
        self.index = 0

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(431, 253)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 40, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.article_window)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 90, 121, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.del_article_function)



        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 151, 16))
        self.label.setObjectName("label")

        self.list_article_widget = QtWidgets.QListWidget(self.centralwidget)
        self.list_article_widget.setGeometry(QtCore.QRect(20, 40, 256, 151))
        self.list_article_widget.setObjectName("textBrowser")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 210, 151, 16))
        self.label_2.setObjectName("label_2")

        self.listlayout = QtWidgets.QGridLayout()
        self.listwidget = QtWidgets.QListWidget()
        self.member_mapping = []
        self.layout = QtWidgets.QHBoxLayout()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.list_articles(self._id_personne)

    def list_articles(self, seller_id):
        self.index = 0
        for article in self.seller_database.list_article_from_seller(seller_id):
            if seller_id == article['id_seller']:
                if(article not in self.member_mapping):
                    self.list_article_widget.insertItem( self.index, "* %s" % (
                        article['name']))
                    self.member_mapping.append(article)
                    self.index += 1
        print("MAPPIIIING")
        print(self.member_mapping)

        self.listlayout.addWidget(self.listwidget)
        self.layout.addLayout(self.listlayout)

    def article_window(self):
        self.add_article_window = add_article.QtWidgets.QWidget()
        self.ui_article = add_article.Ui_MainWindow()
        self.ui_article.setupUi(self.add_article_window)
        self.ui_article.pushButton.clicked.connect(self.add_article_function)
        self.ui_article.pushButton_2.clicked.connect(self.close_add_window)
        self.add_article_window.show()

    def add_article_function(self):
        data = {'name': self.ui_article.lineEdit.text(),
                'price': int(self.ui_article.lineEdit_2.text()),
                'stock': int(self.ui_article.lineEdit_3.text()),
                'id_seller': self._id_personne,
                }
        self.seller_database.add_article(data)
        self.add_article_window.close()
        self.list_articles(self._id_personne)

    def del_article_function(self):
        try:
            id_article = self.member_mapping[self.list_article_widget.currentRow()]['id']
            item = self.list_article_widget.takeItem(self.list_article_widget.currentRow())
            self.list_article_widget.removeItemWidget(item)
            self.seller_database.delete_article(id_article)
        except:
            print("")


    def close_add_window(self):
        self.add_article_window.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Ajouter un article"))
        self.pushButton_3.setText(_translate("MainWindow", "Supprimer un article"))
        self.label.setText(_translate("MainWindow", "Mes articles"))
        self.label_2.setText(_translate("MainWindow", "Recettes : 0 €"))
