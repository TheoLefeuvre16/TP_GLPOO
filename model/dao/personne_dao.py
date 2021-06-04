from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.personne import Personne
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound
import uuid

class PersonneDAO(DAO):
    """
    Personne Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Personne).filter_by(id=id).order_by(Personne.firstname).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Personne).order_by(Personne.firstname).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_name(self, firstname: str, lastname: str):
        try:
            return self._database_session.query(Personne).filter_by(firstname=firstname, lastname=lastname)\
                .order_by(Personne.firstname).one()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        try:
            member = Personne(id=str(uuid.uuid4()), firstname=data.get('firstname'), lastname=data.get('lastname'),age=data.get('age'), email=data.get('email'), statut=data.get('statut'), mdp=data.get("mdp"))
            print("flush broken ?")
            self._database_session.add(member)
            self._database_session.flush()
            print("ah non")
        except IntegrityError:
            raise Error("Member already exists")
        return member

    def update(self, member: Personne, data: dict):
        if 'firstname' in data:
            member.firstname = data['firstname']
        if 'lastname' in data:
            member.lastname = data['lastname']
        if 'age' in data:
            member.age = data['age']
        if 'email' in data:
            member.email = data['email']
        if 'statut' in data:
            member.statut = data['statut']
        if 'mdp' in data:
            member.mdp = data['mdp']
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