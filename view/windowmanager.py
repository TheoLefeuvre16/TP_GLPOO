import acceuil
import guest_inscription
from view.Visiteur import billetterie
from PyQt5 import QtWidgets
import connection
from view.Visiteur import interface_visiteur_connecte

class WindowManager:

    def __init__(self, guest_database, visiteur_database):
        self.guest_database = guest_database
        self.visiteur_database = visiteur_database
        self.data_pers = {}
        self.data_guest = {}
        self.data_visiteur = {}
        self.guest_inscription_window = None
        self.visiteur_inscription_window = None
        self.main_widget = None

        # connection main page
        self.connection_widget = connection.QtWidgets.QWidget()
        self.ui_connection = connection.Ui_MainWindow()
        self.ui_connection.setupUi(self.connection_widget)
        #self.ui_connection.valider_connection.clicked.connect()
        self.ui_connection.inscription.clicked.connect(self.Inscription_window)
        self.connection_widget.show()


    # go back
    def previous_page_guest_inscription(self):
        self.guest_inscription_window.close()

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
            print("vendeur check")
           #self.statut_personne = "vendeur"
            #self.test_w = QtWidgets.QWidget()
            #self.ui_test = interface_visiteur_connecte.Ui_MainWindow()
            #print("to setup")
            #self.ui_test.setupUi(self.test_w, self.visiteur_database)
            #print("after setup")
            #self.test_w.show()


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


    def close_inscription(self):
        #self.confirm_data_window.close()
        self.guest_inscription_window.close()

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

