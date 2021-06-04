import sys
import acceuil
import guest_inscription
import main_seller
import confirm_data
from controller import guest_controller, seller_controller
from model.database import DatabaseEngine
import billetterie
from PyQt5 import QtCore, QtGui, QtWidgets
from view import seller_menu, add_article
from controller.seller_controller import SellerController

'''
from controller.member_controller import MemberController
from model.database import DatabaseEngine
from PySide6.QtWidgets import QApplication
from vue.menu import MenuWindow
'''








class WindowManager:

    def __init__(self):
        self.data_pers = {}
        self.data_guest = {}
        self.data_visiteur = {}
        self.guest_inscription_window = None
        self.visiteur_inscription_window = None
        self.seller_inscription_window = None
        self.confirm_data_window = None

        #seller
        self.add_article_window = None
        self.del_article_window = None
        self.display_money = None
        self.display_stands = None

        # inscription main page
        self.main_widget = acceuil.QtWidgets.QWidget()
        self.ui = acceuil.Ui_acceuil()
        self.ui.setupUi(self.main_widget)
        self.ui.submit.clicked.connect(self.Inscriptions_splitter)
        self.main_widget.show()

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
                'id_seller': int(self.ui_article.lineEdit_3.text())+1
                }

        seller_controller.add_article(data)
        self.add_article_window.close()

    def close_add_window(self):
        self.add_article_window.close()

    # go back
    def previous_page_guest_inscription(self):
        self.guest_inscription_window.close()

    def Inscriptions_splitter(self):
        # Guest
        if self.ui.guest_choice.isChecked() is True:
            self.guest_inscription_window = guest_inscription.QtWidgets.QWidget()
            self.ui_guest = guest_inscription.Ui_Form()
            self.ui_guest.setupUi(self.guest_inscription_window)
            self.ui_guest.precedent_button.clicked.connect(self.previous_page_guest_inscription)
            self.ui_guest.submit_guest.clicked.connect(self.submit_inscription)
            self.statut_personne = "guest"
            self.guest_inscription_window.show()

        # Vendeur
        if self.ui.vendeur_choice.isChecked() is True:
            self.main_widget.close()
            self.seller_inscription_window = seller_menu.QtWidgets.QWidget()
            self.ui_seller = seller_menu.Ui_MainWindow()
            self.ui_seller.setupUi( self.seller_inscription_window)
            self.ui_seller.pushButton_2.clicked.connect(self.article_window)
            self.statut_personne = "vendeur"
            self.seller_inscription_window.show()

        # Visiteur
        if self.ui.visiteur_choice.isChecked() is True:
            print("select visiteur")
            self.statut_personne = "visiteur"
            #ouvrir une fenêtre de choix de billet
            self.visiteur_inscription_window = QtWidgets.QWidget()
            self.ui_visiteur = billetterie.Ui_MainWindow()
            print("print")
            self.ui_visiteur.setupUi(self.visiteur_inscription_window)
            self.ui_visiteur.valid_ticket.clicked.connect(self.submit_visiteur)
            print("setup ??")
            self.visiteur_inscription_window.show()

        print("out of inscription splitter")

    def close_inscription(self):
        #self.confirm_data_window.close()
        self.guest_inscription_window.close()

    def submit_inscription(self):
        print("submit_inscription")
        # guest data
        self.data_guest["horaires"] = self.ui_guest.time_visite.time()
        self.data_guest["lieu"] = self.ui_guest.visite_choice.currentText()

        # person data
        self.data_pers["firstname"] = self.ui.prenom_input.text()
        self.data_pers["lastname"] = self.ui.nom_input.text()
        self.data_pers["age"] = self.ui.comboBox.currentText()
        self.data_pers["email"] = self.ui.email_input.text()
        self.data_pers["mdp"] = self.ui.mdp_input.text()
        self.data_pers["statut"] = self.statut_personne
        print(self.data_guest)
        guest_database.create_guest(self.data_guest, self.data_pers)
        db = guest_database.list_guest()
        print("oui")
        print(db)
        self.close_inscription()
        self.main_widget.close()

    def submit_visiteur(self):
        print("submit visiteur")
        print("index : ", self.ui_visiteur.comboBox_billets.currentIndex())

        print(int(self.ui.comboBox.currentText()))
        if int(self.ui.comboBox.currentText()) <= 18 and self.ui_visiteur.comboBox_billets.currentIndex() == 0:
            print("ticket -18")
            self.data_visiteur["age"] = "0"
            self.data_visiteur["stand"] = "1"
            self.data_visiteur["guest"] = "1"
        if self.ui_visiteur.comboBox_billets.currentIndex() == 1:
            self.data_visiteur["age"] = "1"
            self.data_visiteur["guest"] = "1"
            self.data_visiteur["stand"] = "0"
        if self.ui_visiteur.comboBox_billets.currentIndex() == 2:
            self.data_visiteur["age"] = "1"
            self.data_visiteur["stand"] = "1"
            self.data_visiteur["guest"] = "0"
        if self.ui_visiteur.comboBox_billets.currentIndex() == 3:
            self.data_visiteur["age"] = "1"
            self.data_visiteur["stand"] = "1"
            self.data_visiteur["guest"] = "1"
        print("toprint")
        print("age " + self.data_visiteur["age"])
        print(" guest " + self.data_visiteur["guest"] + " stand " + self.data_visiteur["stand"])
        self.data_pers["firstname"] = self.ui.prenom_input.text()
        self.data_pers["lastname"] = self.ui.nom_input.text()
        self.data_pers["age"] = self.ui.comboBox.currentText()
        self.data_pers["email"] = self.ui.email_input.text()
        self.data_pers["mdp"] = self.ui.mdp_input.text()
        self.data_pers["statut"] = self.statut_personne



    def confirm_data_window_func (self):
        print("submit_inscription")
        # guest data
        print(self.ui_guest.visite_choice.currentText())
        print(self.data_guest)

        self.data_guest["horaires"] = self.ui_guest.time_visite.time()
        self.data_guest["lieu"] = self.ui_guest.visite_choice.currentText()
        print("test")
        print(self.data_guest)
        # person data
        self.data_pers["firstname"] = self.ui.prenom_input.text()
        self.data_pers["lastname"] = self.ui.nom_input.text()
        self.data_pers["age"] = self.ui.comboBox.currentText()
        self.data_pers["email"] = self.ui.email_input.text()
        self.data_pers["mdp"] = self.ui.mdp_input.text()
        self.data_pers["statut"] = self.statut_personne

        guest_database.create_guest(self.data_guest, self.data_pers)


        self.close_inscription()
        self.main_widget.close()



        self.confirm_data_window = confirm_data.QtWidgets.QWidget()
        self.ui_confirm_data = confirm_data.Ui_Form()
        self.ui_confirm_data.setupUi(self.confirm_data_window)
        self.confirm_data_window.show()
        self.ui_confirm_data.cancel_data.clicked.connect(self.close_inscription)
        self.ui_confirm_data.submit_data.clicked.connect(self.submit_inscription)
        self.ui_confirm_data.textBrowser.setText(
            "recap : \n\n" +
            self.ui.prenom_input.text()
            + " " + self.ui.nom_input.text() + "\n" +
            self.ui.comboBox.currentText() + " ans \n" +
            self.ui.email_input.text() + "\n" +
            "statut : " + self.statut_personne + "\n" +
            "-----------------------------------------\n"
        )


database_engine = DatabaseEngine(url='sqlite:///inscription.db')
database_engine.create_database()
guest_database = guest_controller.GuestController(database_engine)

seller_controller = SellerController(database_engine)


main_app = acceuil.QtWidgets.QApplication(sys.argv)

main_window = WindowManager()

exit(main_app.exec_())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyChakkjkjrm')
