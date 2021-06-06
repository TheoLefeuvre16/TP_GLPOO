import json
from view.Visiteur import billetterie
from PyQt5 import QtWidgets
from view import interface_seller_connecte
from view.assets import list_vendeur, guest_inscription, list_recette, list_stand, accueil_admin, list_invite, \
    connection, acceuil, seller_confirmation, list_visiteur, guest_window, schedule
from view.Visiteur import interface_visiteur_connecte


class WindowManager:

    # VARIABLES
    def __init__(self, guest_database, visiteur_database,seller_database, admin_database):
        self.guest_database = guest_database
        self.visiteur_database = visiteur_database
        self.seller_database = seller_database
        self.admin_database = admin_database
        self.data_pers = {}
        self.data_guest = {}
        self.data_visiteur = {}
        self.data_seller = {}
        self.guest_inscription_window = None
        self.visiteur_inscription_window = None

        self.list_visiteur_window = None
        self.list_seller_window = None
        self.list_guest_window = None
        self.list_stand_window = None
        self.list_recette_window = None
        self.list_schedule_window = None

        self.main_widget = None
        self.guest_page_window = None

        # connection main page
        self.connection_widget = connection.QtWidgets.QWidget()
        self.ui_connection = connection.Ui_MainWindow()
        self.ui_connection.setupUi(self.connection_widget)
        self.ui_connection.valider_connection.clicked.connect(self.valider_connexion)
        self.ui_connection.error_user.setVisible(False)
        self.ui_connection.inscription.clicked.connect(self.Inscription_window)
        self.connection_widget.show()

        # seller
        self.add_article_window = None
        self.del_article_window = None
        self.display_money = None
        self.display_stands = None



    # GO BACK
    def previous_page_guest_inscription(self):
        self.guest_inscription_window.close()
        self.seller_inscription_window = None

        self.confirm_data_window = None

    def previous_page_list_visiteur(self):
        self.list_visiteur_window.close()

    def previous_page_list_seller(self):
        self.list_seller_window.close()

    def previous_page_list_guest(self):
        self.list_guest_window.close()

    def previous_page_list_stand(self):
        self.list_stand_window.close()

    def previous_page_list_recette(self):
        self.list_recette_window.close()

    def previous_page_list_schedule(self):
        self.list_schedule_window.close()

    # MODE ADMIN
    def Mode_admin(self):
        self.main_widget = accueil_admin.QtWidgets.QWidget()
        self.ui_admin = accueil_admin.Ui_Form()
        self.ui_admin.setupUi(self.main_widget)
        print("issou2)")
        self.ui_admin.list_visiteur.clicked.connect(self.Print_visiteur_window)
        self.ui_admin.list_seller.clicked.connect(self.Print_seller_window)
        self.ui_admin.list_guest.clicked.connect(self.Print_guest_window)
        self.ui_admin.list_stand.clicked.connect(self.Print_stand_window)
        self.ui_admin.list_recette.clicked.connect(self.Print_recette_window)
        self.ui_admin.list_schedule.clicked.connect(self.Print_schedule_window)
        self.ui_admin.modify_schedule.clicked.connect(self.Print_schedule_window)
        self.main_widget.show()


    # AFFICHAGE DES LISTES
    def Print_schedule_window(self):
        self.list_schedule_window = schedule.QtWidgets.QWidget()
        self.ui_schedule = schedule.Ui_Form()
        self.ui_schedule.setupUi(self.list_schedule_window)
        self.ui_schedule.pushButton.clicked.connect(self.previous_page_list_schedule)

        self.list_schedule_window.show()

    def Print_recette_window(self):
        self.list_recette_window = list_recette.QtWidgets.QWidget()
        self.ui_recette = list_recette.Ui_Form()
        self.ui_recette.setupUi(self.list_recette_window)
        self.ui_recette.pushButton.clicked.connect(self.previous_page_list_recette)

        self.ui_recette.lcdNumber.display(157)


        self.list_recette_window.show()

    def Print_stand_window(self):
        self.list_stand_window = list_stand.QtWidgets.QWidget()
        self.ui_stand = list_stand.Ui_Form()
        self.ui_stand.setupUi(self.list_stand_window)
        self.ui_stand.pushButton.clicked.connect(self.previous_page_list_stand)

        db = self.admin_database.list_guest()
        for i in range(len(db)):
            list_text = json.dumps(db[i])
            self.ui_stand.plainTextEdit.insertPlainText("Stand n°" + str(i) + ":\n")
            self.ui_stand.plainTextEdit.insertPlainText(list_text + "\n\n")

        self.list_stand_window.show()

    def Print_guest_window(self):
        self.list_guest_window = list_invite.QtWidgets.QWidget()
        self.ui_guest = list_invite.Ui_Form()
        self.ui_guest.setupUi(self.list_guest_window)
        self.ui_guest.pushButton.clicked.connect(self.previous_page_list_guest)

        db = self.admin_database.list_guest()
        for i in range(len(db)):
            list_text = json.dumps(db[i])
            self.ui_guest.plainTextEdit.insertPlainText("Invite n°" + str(i) + ":\n")
            self.ui_guest.plainTextEdit.insertPlainText(list_text + "\n\n")

        self.list_guest_window.show()

    def Print_seller_window(self):
        self.list_seller_window = list_vendeur.QtWidgets.QWidget()
        self.ui_seller = list_vendeur.Ui_Form()
        self.ui_seller.setupUi(self.list_seller_window)
        self.ui_seller.pushButton.clicked.connect(self.previous_page_list_seller)

        db = self.admin_database.list_seller()
        for i in range(len(db)):
            list_text = json.dumps(db[i])
            self.ui_seller.plainTextEdit.insertPlainText("Vendeur n°" + str(i) + ":\n")
            self.ui_seller.plainTextEdit.insertPlainText(list_text + "\n\n")

        self.list_seller_window.show()

    def Print_visiteur_window(self):
        self.list_visiteur_window = list_visiteur.QtWidgets.QWidget()
        self.ui_visiteur = list_visiteur.Ui_Form()
        self.ui_visiteur.setupUi(self.list_visiteur_window)
        self.ui_visiteur.pushButton.clicked.connect(self.previous_page_list_visiteur)

        db = self.admin_database.list_visiteur()

        for i in range(len(db)):
            list_text = json.dumps(db[i])
            self.ui_visiteur.plainTextEdit.insertPlainText("Visiteur n°" + str(i) + ":\n")
            self.ui_visiteur.plainTextEdit.insertPlainText(list_text + "\n\n")

        self.list_visiteur_window.show()


    # INSCRIPTION

    # page principale
    def Inscription_window(self):

        self.main_widget = acceuil.QtWidgets.QWidget()
        self.ui = acceuil.Ui_Form()
        self.ui.setupUi(self.main_widget)
        self.ui.submit.clicked.connect(self.Inscriptions_splitter)
        self.ui.error_dupli.setVisible(False)
        self.main_widget.show()


    # redirection en fonction des  statuts
    def Inscriptions_splitter(self):

        # check
        db_visiteur = self.visiteur_database.list_visiteurs()
        for member in db_visiteur:
            nom = self.visiteur_database.get_guests(member['id_personne'])
            if nom["email"]  == self.ui.email_input.text():
                self.ui.error_dupli.setVisible(True)
                return
            else:
                self.ui.error_dupli.setVisible(False)

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


    # fermeture fenetre inscription
    def close_inscription(self):
        #self.confirm_data_window.close()

        if self.main_widget.isEnabled():
            self.main_widget.close()

    # vendeur
    def submit_seller_inscription(self):
        self.data_seller["money"] = 0
        # person data
        self.data_pers["firstname"] = self.ui.prenom_input.text()
        self.data_pers["lastname"] = self.ui.nom_input.text()
        self.data_pers["age"] = self.ui.comboBox.currentText()
        self.data_pers["email"] = self.ui.email_input.text()
        self.data_pers["mdp"] = self.ui.mdp_input.text()
        self.data_pers["statut"] = self.statut_personne
        self.seller_database.create_seller(self.data_seller,self.data_pers)
        self.seller_inscription_window.close()
        self.close_inscription()

    #guest
    def submit_inscription(self):
        # guest data
        self.data_guest["horaires"] = str(self.ui_guest.time_visite.time().toPyTime())
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

        self.guest_inscription_window.close()
        self.close_inscription()

    #visiteur
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

        self.visiteur_inscription_window.close()
        self.close_inscription()

        print("tout roule")

    # PAGE GUEST
    def guest_window(self , horaire, lieu):
        self.guest_page_window = guest_window.QtWidgets.QWidget()
        self.ui_guest_page = guest_window.Ui_Form()
        self.ui_guest_page.setupUi(self.guest_page_window)
        self.ui_guest_page.input_text.setText("Votre intervention est a " + horaire + " dans " + lieu)
        self.ui_guest_page.deco_button.clicked.connect(self.close_window_page)
        self.guest_page_window.show()


    def close_window_page(self):
        self.guest_page_window.close()

    # PAGE CONNECTION
    def valider_connexion(self):

        print(self.ui_connection.mail_input.text())
        self.ui_connection.error_user.setVisible(False)
        mail_input = self.ui_connection.mail_input.text()
        mdp_input = self.ui_connection.mdp_input.text()

        db_guest = self.guest_database.list_guest()

        #admin mode
        if "admin" == mail_input and "admin" == mdp_input:
            self.Mode_admin()
            return

        # guest
        for member in db_guest:
            nom = self.guest_database.get_person(member['id_personne'])
            if nom['email'] == mail_input and nom['mdp'] == mdp_input:
                print("connexion guest")
                self.guest_window(horaire=member['horaires'], lieu=member['lieu'])
                return

        #visiteur
        db_visiteur = self.visiteur_database.list_visiteurs()
        for member in db_visiteur:
            nom = self.visiteur_database.get_guests(member['id_personne'])
            if nom['email'] == mail_input  and nom['mdp'] == mdp_input:
                print("connexion visiteur")#call la fonction de connexion
                self.visiteur_connexion_window = QtWidgets.QWidget()
                self.ui_visiteur_connexion = interface_visiteur_connecte.Ui_MainWindow()
                print("print")
                self.ui_visiteur_connexion.setupUi(self.visiteur_connexion_window, self.visiteur_database)
                print("setup ??")
                self.visiteur_connexion_window.show()
                return

        # vendeur
        db_seller = self.seller_database.list_sellers()
        for member in db_seller:
            nom = self.visiteur_database.get_guests(member['id_personne'])
            if nom['email'] == mail_input  and nom['mdp'] == mdp_input:
                id_personne = member['id']
                print(id_personne)
                self.seller_connexion_window = QtWidgets.QWidget()
                self.ui_seller_connexion = interface_seller_connecte.Ui_MainWindow()
                print("print")
                self.ui_seller_connexion.setupUi(self.seller_connexion_window,self.seller_database,id_personne)
                print("setup ??")
                self.seller_connexion_window.show()
                return

        self.ui_connection.error_user.setVisible(True)