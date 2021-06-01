from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.visiteur import Visiteur
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound


class VisiteurDAO(DAO):
    """
    Visiteur Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Visiteur).filter_by(id=id).order_by(Visiteur.id).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Visiteur).order_by(Visiteur.id).all()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        try:
            member = Visiteur(age=data.get('age'), guest=data.get('guest'), stand=data.get('stand'), id_personne=data.get('id_personne'))
            self._database_session.add(member)
            self._database_session.flush()
            print(member.to_dict())
        except IntegrityError:
            raise Error("Member already exists")
        return member

    def update(self, member: Visiteur, data: dict):
        if 'age' in data:
            member.age = data['age']
        if 'guest' in data:
            member.guest = data['guest']
        if 'stand' in data:
            member.guest = data['stand']
        if 'id_personne' in data:
            member.id_personne = data['id_personne']
        try:
            self._database_session.merge(member)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Error data may be malformed")
        return member

    def delete(self, entity):
        try:
            self._database_session.delete(entity)
        except SQLAlchemyError as e:
            raise Error(str(e))

    #ajouter les fonctions de remplissages du panier
    #cf TD fait avec coco