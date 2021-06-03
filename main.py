import confirm_data
from controller import guest_controller, visiteur_controller
from model.database import DatabaseEngine
from view.Visiteur import billetterie
from PyQt5 import QtWidgets
import acceuil
import sys
from view.windowmanager import WindowManager

'''
from controller.member_controller import MemberController
from model.database import DatabaseEngine
from PySide6.QtWidgets import QApplication
from vue.menu import MenuWindow
'''

database_engine = DatabaseEngine(url='sqlite:///inscription.db')
database_engine.create_database()
guest_database = guest_controller.GuestController(database_engine)
visiteur_database = visiteur_controller.VisiteurController(database_engine)

main_app = acceuil.QtWidgets.QApplication(sys.argv)

main_window = WindowManager(guest_database, visiteur_database)

exit(main_app.exec_())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyChakkjkjrm')


 #creation de la fenêtre listant les invités
            #self.test_w = QtWidgets.QWidget()
            #self.ui_test = list_guest.Ui_MainWindow()
            #self.ui_test.setupUi(self.test_w, visiteur_database)
            #self.test_w.show()