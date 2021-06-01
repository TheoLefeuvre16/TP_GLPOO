"""

"""
from model.database import DatabaseEngine
from PySide6.QtWidgets import QApplication
from controller.seller_controller import SellerController
from view import seller_menu, add_article
import sys

class WindowManager:
    def __init__(self,seller_controller: SellerController):
        self.add_article_window = None
        self.del_article_window = None
        self.display_money = None
        self.display_stands = None

        self._seller_controller = seller_controller

        #main page
        self.main_widget = seller_menu.QtWidgets.QWidget()
        self.ui = seller_menu.Ui_MainWindow()
        self.ui.setupUi(self.main_widget)
        self.ui.pushButton_2.clicked.connect(self.article_window)
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
                'price': self.ui_article.lineEdit_2.text(),
                'stock': self.ui_article.lineEdit_3.text()
                }
        print(data)
        self._seller_controller.add_article(data)

    def close_add_window(self):
        self.add_article_window.close()
if __name__ == "__main__":
    database_engine = DatabaseEngine(url='sqlite:///articles.db')
    database_engine.create_database()
    seller_controller = SellerController(database_engine)


    app = seller_menu.QtWidgets.QApplication(sys.argv)
    main_window = WindowManager(seller_controller)
    exit(app.exec_())

    #widget = seller_menu.QtWidgets.QWidget()
    #ui = seller_menu.Ui_MainWindow()
    #ui.setupUi(widget)
    #widget.show()




