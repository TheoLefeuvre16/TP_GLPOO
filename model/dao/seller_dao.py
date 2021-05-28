from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.article import Article
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound

class SellerDAO(DAO):
    """
    Seller Mapping DAO
    """
    def __init__(self, database_session):
        super().__init__(database_session)

    def create_article(self, data:dict):
       try:
           article = Article(name=data.get('name'), price=data.get('price'),stock=data.get('stock'))
           self._database_session.add(article)
           self._database_session.flush()
       except IntegrityError:
           raise Error("Article already exists")
       return article