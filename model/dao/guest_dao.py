from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.guest import Guest
from model.dao.dao import DAO
import uuid
from exceptions import Error, ResourceNotFound


class GuestDAO(DAO):
    """
    Guest Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Guest).filter_by(id=id).order_by(Guest.id).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Guest).order_by(Guest.id).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_position(self, lieux: str):
        try:
            return self._database_session.query(Guest).filter_by(lieu=lieux)\
                .order_by(Guest.lieu).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_time(self, horaire: str):
        try:
            return self._database_session.query(Guest).filter_by(horaires=horaire)\
                .order_by(Guest.horaire).one()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        print("call create")
        try:

            #member = Guest(horaires=data.get('horaires'), lieu=data.get('lieu'),id_personne=data.get('id_personne'))
            member = Guest(id=str(uuid.uuid4()), horaires=data.get('horaires'), lieu=data.get('lieu'), id_personne=data.get('id_personne'))
            print("member :")
            print(type(data.get('horaires')))
            self._database_session.add(member)
            self._database_session.flush()
            print("flush")
            print(member.to_dict())
        except IntegrityError:
            raise Error("Member already exists")
        return member

    def update(self, member: Guest, data: dict):
        if 'horaires' in data:
            member.horaires = data['horaires']
        if 'lieu' in data:
            member.lieu = data['lieu']
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