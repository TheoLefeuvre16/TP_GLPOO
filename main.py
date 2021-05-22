import sys
import acceuil
import guest_inscription
import confirm_data
from controller import guest_controller
from model.database import DatabaseEngine

'''
from controller.member_controller import MemberController
from model.database import DatabaseEngine
from PySide6.QtWidgets import QApplication
from vue.menu import MenuWindow
'''








class WindowManager:

    def __init__(self):
        self.data_pers = None
        self.data_guest = None
        self.guest_inscription_window = None
        self.confirm_data_window = None

        # inscription main page
        self.main_widget = acceuil.QtWidgets.QWidget()
        self.ui = acceuil.Ui_acceuil()
        self.ui.setupUi(self.main_widget)
        self.ui.submit.clicked.connect(self.Inscriptions_splitter)
        self.main_widget.show()

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
            self.ui_guest.submit_guest.clicked.connect(self.confirm_data_window_func)
            self.statut_personne = "guest"
            self.guest_inscription_window.show()

        # Vendeur
        if self.ui.vendeur_choice.isChecked() is True:
            self.statut_personne = "vendeur"
        # Visiteur
        if self.ui.visiteur_choice.isChecked() is True:
            self.statut_personne = "visiteur"

    def close_inscription(self):
        self.confirm_data_window.close()
        self.guest_inscription_window.close()

    def submit_inscription(self):

        # guest data
        self.data_guest["horaires"] = self.ui_guest.time_visite.time()
        self.data_guest["lieu"] = self.ui_guest.visite_choice.currentText()

        # person data
        self.data_pers["firstname"] = self.ui.prenom_input.text()
        self.data_pers["lastname"] = self.ui.prenom_input.text()
        self.data_pers["age"] = self.ui.comboBox.currentText()
        self.data_pers["email"] = self.ui.email_input.text()
        self.data_pers["mdp"] = self.ui.mdp_input.text()
        self.data_pers["statut"] = self.statut_personne

        guest_database.create_guest(self.data_guest, self.data_pers)
        self.close_inscription()
        self.main_widget.close()




    def confirm_data_window_func (self):
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
main_app = acceuil.QtWidgets.QApplication(sys.argv)

main_window = WindowManager()

exit(main_app.exec_())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyChakkjkjrm')
