from model.dao.guest_dao import GuestDAO
from model.dao.personne_dao import PersonneDAO
from exceptions import Error, InvalidData

class PersonneController:

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frames = []