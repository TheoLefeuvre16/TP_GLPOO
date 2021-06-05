import confirm_data
from controller import guest_controller, visiteur_controller, admin_controller
from model.database import DatabaseEngine
from view.Visiteur import billetterie
from PyQt5 import QtWidgets
import connection
import sys
from view.windowmanager import WindowManager
from controller.seller_controller import SellerController

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
seller_database = SellerController(database_engine)
admin_database = admin_controller.AdminController(database_engine)
main_app = connection.QtWidgets.QApplication(sys.argv)

main_window = WindowManager(guest_database, visiteur_database,seller_database, admin_database)

exit(main_app.exec_())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyChakkjkjrm')
