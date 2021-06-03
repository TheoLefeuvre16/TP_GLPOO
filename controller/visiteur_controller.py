import re

from controller.personne_controller import PersonneController
from model.dao.visiteur_dao import VisiteurDAO
from model.dao.personne_dao import PersonneDAO
from model.dao.guest_dao import GuestDAO
from model.dao.seller_dao import SellerDAO
from exceptions import Error, InvalidData


class VisiteurController(PersonneController):

    """
    Visiteur actions
    """
    panier = []

    def __init__(self, database_engine):
        super().__init__(database_engine)
        self._frames = []

    def create_visiteur(self, data_visiteur, data_personne):
        print("entering create_visiteur")
       # self._check_profile_data(data)
        try:
            with self._database_engine.new_session() as session:
                # Save member in database
                print("with ok")
                personne = PersonneDAO(session).create(data_personne)
                personne_data = personne.to_dict()
                print(personne_data)
                data_visiteur['id_personne'] = personne_data.get('id')
                print(data_visiteur)
                visiteur = VisiteurDAO(session).create(data_visiteur)
                visiteur_data = visiteur.to_dict()
                print(visiteur_data)
                print("exiting create_Visiteur")
                return visiteur_data
        except Error as e:
            # log error
            print("error in create_visiteur")
            raise e

    def update_visiteur(self, visiteur_id, visiteur_data):
        #self._check_profile_data(member_data, update=True)
        with self._database_engine.new_session() as session:
            visiteur_dao = VisiteurDAO(session)
            visiteur = visiteur_dao.get(visiteur_id)
            visiteur = visiteur_dao.update(visiteur, visiteur_data)
            return visiteur.to_dict()

    def delete_Visiteur(self, visiteur_id):

        with self._database_engine.new_session() as session:
            visiteur_dao = VisiteurDAO(session)
            visiteur = visiteur_dao.get(visiteur_id)
            visiteur_dao.delete(visiteur)

    def search_article(self, nom, vendeur): #nom de l'article
        with self._database_engine.new_session() as session:
            article = SellerDAO(session).get(nom)
            article_data = article.to_dict()
        return article_data


    #lister les stands = vendeurs
    def list_seller(self):

        with self._database_engine.new_session() as session:
            seller_dao = SellerDAO(session).get_all()
            return seller_dao.to_dict()

    #lister les lieux -> skip
    #afficher l'emploi du temps = lister les guests
    def list_guests(self):
        with self._database_engine.new_session() as session:
            guests = GuestDAO(session).get_all()
            guests_data = [guest.to_dict() for guest in guests]
        return guests_data

    def get_guests(self, guests_id):
        with self._database_engine.new_session() as session:
            guest = PersonneDAO(session).get(guests_id)
            guest_data = guest.to_dict()
        return guest_data

    #lister les articles d'un stand
    def list_article_from_seller(self, seller):
        # Query database
        with self._database_engine.new_session() as session:
            article_dao = SellerDAO(session)
            list_article = article_dao.get_by_seller(seller)
            return list_article.to_dict()

    def add_to_cart(self, nom, quantite):
        with self._database_engine.new_session() as session:
            article = SellerDAO(session).get_article(nom)
            article_dict = article.to_dict()
            if(article_dict.get("qte") >= quantite):
                tmp = []
                tmp.append(article_dict.get("nom"))
                tmp.append(quantite)
                self.panier.append(tmp)
                return 1
            return 0

    def remove_from_cart(self, index, quantite): #index dans le panier de l'article
        if self.panier[index][1] <= quantite:
            self.panier.remove(self.panier[index])
        else:
            self.panier[index][1] -= quantite

    def validate_cart(self):
        self.panier.clear()

    def show_cart(self):
        return self.panier