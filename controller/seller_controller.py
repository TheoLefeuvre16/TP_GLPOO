import re

from model.dao.seller_dao import SellerDAO
from exceptions import Error, InvalidData
from model.dao.personne_dao import PersonneDAO

class SellerController:
    """
    Seller actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine

    def add_article(self,data):
        try:
            with self._database_engine.new_session() as session:
                print("ajout article controler")
                article = SellerDAO(session).create_article(data)
                article_data = article.to_dict()

                return article_data
        except Error as e:
            raise e

    def list_articles(self):
        with self._database_engine.new_session() as session:
            articles = SellerDAO(session).get_all_articles()
            sellers_data = [article.to_dict() for article in articles]
        return sellers_data

    def list_article_from_seller(self, seller):
        # Query database
        with self._database_engine.new_session() as session:
            article_dao = SellerDAO(session).get_seller_article(seller)
            list_article = [article.to_dict() for article in article_dao]
            return list_article

    def get_article(self, guests_id):
        with self._database_engine.new_session() as session:
            article = SellerDAO(session).get_id_article(guests_id)
            article_data = article.to_dict()
        return article_data

    def delete_article(self, article_id):
        with self._database_engine.new_session() as session:
            article_dao = SellerDAO(session)
            article = article_dao.get_id_article(article_id)
            article_dao.delete(article)



    def create_seller(self, data_seller, data_personne):
        try:
            with self._database_engine.new_session() as session:
                personne = PersonneDAO(session).create(data_personne)
                personne_data = personne.to_dict()

                data_seller['id_personne'] = personne_data.get('id')
                print(personne_data.get('id'))
                seller = SellerDAO(session).create_seller(data_seller)
                print("apres create seller")
                seller_data = seller.to_dict()
                return seller_data
        except Error as e:
            raise e


    def list_sellers(self):
        with self._database_engine.new_session() as session:
            sellers = SellerDAO(session).get_all_sellers()
            sellers_data = [seller.to_dict() for seller in sellers]
        return sellers_data

    def get_seller(self, member_id):
        with self._database_engine.new_session() as session:
            seller = SellerDAO(session).get_id_seller(member_id)
            seller_data = seller.to_dict()
        return seller_data

    def delete_seller(self, guest_id):
        with self._database_engine.new_session() as session:
            seller_dao = SellerDAO(session)
            seller = seller_dao.get_id_seller(guest_id)
            seller_dao.delete(seller)







