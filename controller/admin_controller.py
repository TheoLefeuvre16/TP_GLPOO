from controller.personne_controller import PersonneController
from model.dao.visiteur_dao import VisiteurDAO
from model.dao.personne_dao import PersonneDAO
from model.dao.guest_dao import GuestDAO
from model.dao.seller_dao import SellerDAO
from exceptions import Error, InvalidData


class AdminController(PersonneController):
    """
       Admin actions
       """

    def __init__(self, database_engine):
        super().__init__(database_engine)
        self._frames = []

    def list_guest(self):
        with self._database_engine.new_session() as session:
            guests = GuestDAO(session).get_all()
            guests_data = [guest.to_dict() for guest in guests]
        return guests_data

    def list_visiteur(self):
        with self._database_engine.new_session() as session:
            visiteurs = VisiteurDAO(session).get_all()
            visiteurs_data = [visiteur.to_dict() for visiteur in visiteurs]
        return visiteurs_data

    def list_seller(self):
        with self._database_engine.new_session() as session:
            seller_dao = SellerDAO(session).get_all_sellers()
            sellers_data = [seller.to_dict() for seller in seller_dao]
            return sellers_data

