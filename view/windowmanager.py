import acceuil
import guest_inscription
from view.Visiteur import billetterie
from PyQt5 import QtWidgets
import connection
from view import seller_menu, add_article, seller_confirmation
from view.Visiteur import interface_visiteur_connecte

class WindowManager:

    def __init__(self, guest_database, visiteur_database,seller_database):
        self.guest_database = guest_database
        self.visiteur_database = visiteur_database
        self.seller_database = seller_database
        self.data_pers = {}
        self.data_guest = {}
        self.data_visiteur = {}
        self.data_seller = {}
        self.guest_inscription_window = None
        self.visiteur_inscription_window = None
        self.main_widget = None

        # connection main page
        self.connection_widget = connection.QtWidgets.QWidget()
        self.ui_connection = connection.Ui_MainWindow()
        self.ui_connection.setupUi(self.connection_widget)
        self.ui_connection.valider_connection.clicked.connect(self.valider_connexion)
        self.ui_connection.inscription.clicked.connect(self.Inscription_window)
        self.connection_widget.show()

        # seller
        self.add_article_window = None
        self.del_article_window = None
        self.display_money = None
        self.display_stands = None

    # go back
    def previous_page_guest_inscription(self):
        self.guest_inscription_window.close()
        self.seller_inscription_window = None

        self.confirm_data_window = None



        # inscription main page
    #connection
    def Inscription_window(self):

        self.main_widget = acceuil.QtWidgets.QWidget()
        self.ui = acceuil.Ui_Form()
        self.ui.setupUi(self.main_widget)
        self.ui.submit.clicked.connect(self.Inscriptions_splitter)
        self.main_widget.show()


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
            self.seller_inscription_window = seller_confirmation.QtWidgets.QWidget()
            self.ui_seller = seller_confirmation.Ui_MainWindow()
            self.ui_seller.setupUi(self.seller_inscription_window)
            self.ui_seller.pushButton.clicked.connect(self.submit_seller_inscription)
            self.seller_inscription_window.show()
            self.statut_personne = "vendeur"

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

        self.seller_database.add_article(data)
        self.add_article_window.close()

    def close_add_window(self):
        self.add_article_window.close()

    def close_inscription(self):
        #self.confirm_data_window.close()
        self.guest_inscription_window.close()

    def submit_seller_inscription(self):
        self.data_seller["money"] = 0
        # person data
        self.data_pers["firstname"] = self.ui.prenom_input.text()
        self.data_pers["lastname"] = self.ui.nom_input.text()
        self.data_pers["age"] = self.ui.comboBox.currentText()
        self.data_pers["email"] = self.ui.email_input.text()
        self.data_pers["mdp"] = self.ui.mdp_input.text()
        self.data_pers["statut"] = self.statut_personne
        self.seller_database.create_seller(self.data_seller, self.data_pers)

        self.seller_inscription_window.close()
        self.main_widget.close()

    def submit_inscription(self):
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
        self.guest_database.create_guest(self.data_guest, self.data_pers)
        db = self.guest_database.list_guest()

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
        self.visiteur_database.create_visiteur(self.data_visiteur, self.data_pers)
        print("tout roule")

    def valider_connexion(self):

        print(self.ui_connection.mail_input.text())
        mail_input = self.ui_connection.mail_input.text()
        mdp_input = self.ui_connection.mdp_input.text()

        db_guest = self.guest_database.list_guest()
        for member in db_guest:
            nom = self.visiteur_database.get_guests(member['id_personne'])
            if nom['email'] == mail_input and nom['mdp'] == mdp_input:
                print("connexion guest")#call la fonction de connexion

        db_visiteur = self.visiteur_database.list_visiteurs()
        for member in db_visiteur:
            nom = self.visiteur_database.get_guests(member['id_personne'])
            if nom['email'] == mail_input  and nom['mdp'] == mdp_input:
                print("connexion visiteur")#call la fonction de connexion

        db_seller = self.seller_database.list_sellers()
        for member in db_seller:
            nom = self.visiteur_database.get_guests(member['id_personne'])
            if nom['email'] == mail_input  and nom['mdp'] == mdp_input:
                print("connexion vendeur")#call la fonction de connexion
