from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.article import Article
from model.mapping.seller import Seller
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound
import uuid
class SellerDAO(DAO):
    """
    Seller Mapping DAO
    """
    def __init__(self, database_session):
        super().__init__(database_session)

    def create_article(self, data: dict):
       try:

           article = Article(id=str(uuid.uuid4()), name=data.get('name'), price=data.get('price'),stock=data.get('stock'),id_seller=data.get('id_seller'))
           self._database_session.add(article)
           self._database_session.flush()


       except IntegrityError:
           raise Error("Article already exists")
       return article

    def get_all_articles(self):
        try:
            return self._database_session.query(Article).order_by(Article.id).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_id_article(self, id):
        try:
            return self._database_session.query(Article).filter_by(id=id).order_by(Article.id).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_nom_article(self, nom):
        try:
            return self._database_session.query(Article).filter_by(name=nom).order_by(Article.id).one()
        except NoResultFound:
            raise ResourceNotFound()

    def create_seller(self, data: dict):
        try:
            member = Seller(id=str(uuid.uuid4()), money=0, id_personne=data.get('id_personne'))
            self._database_session.add(member)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Seller already exists")
        return member

    def get_all_sellers(self):
        try:
            return self._database_session.query(Seller).order_by(Seller.id).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_id_seller(self, id):
        try:
            return self._database_session.query(Seller).filter_by(id=id).order_by(Seller.id).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_seller_article(self, id):
        try:
            return self._database_session.query(Article).filter_by(id_seller=id).order_by(Article.id).all()
        except NoResultFound:
            raise ResourceNotFound()

    def delete(self, entity):
        try:
            self._database_session.delete(entity)
        except SQLAlchemyError as e:
            raise Error(str(e))