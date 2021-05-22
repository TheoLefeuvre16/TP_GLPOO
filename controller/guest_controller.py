import re

from model.dao.guest_dao import GuestDAO
from model.dao.personne_dao import PersonneDAO
from exceptions import Error, InvalidData


class GuestController:

    """
    Guest actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frames = []


    def list_guest(self):
        with self._database_engine.new_session() as session:
            guests = GuestDAO(session).get_all()
            guests_data = [guest.to_dict() for guest in guests]
        return guests_data

    def get_guests(self,guests_id):
        with self._database_engine.new_session() as session:
            guest = GuestDAO(session).get(guests_id)
            guest_data = guest.to_dict()
        return guest_data

    def create_guest(self, data_guest, data_personne):

       # self._check_profile_data(data)
        try:
            with self._database_engine.new_session() as session:
                # Save member in database
                personne = PersonneDAO(session).create(data_personne)
                personne_data = personne.to_dict()
                data_guest['id_personne'] = personne_data.get('id')
                guest = GuestDAO(session).create(data_guest)
                guest_data = guest.to_dict()

                return guest_data
        except Error as e:
            # log error
            raise e

    def update_guest(self, guest_id, guest_data):

        #self._check_profile_data(member_data, update=True)
        with self._database_engine.new_session() as session:
            guest_dao = GuestDAO(session)
            guest = guest_dao.get(guest_id)
            guest = guest_dao.update(guest, guest_data)
            return guest.to_dict()

    def delete_guest(self, guest_id):

        with self._database_engine.new_session() as session:
            guest_dao = GuestDAO(session)
            guest = guest_dao.get(guest_id)
            guest_dao.delete(guest)

    def search_time_guest(self, horaire):

        # Query database
        with self._database_engine.new_session() as session:
            guest_dao = GuestDAO(session)
            guest = guest_dao.get_by_time(horaire)
            return guest.to_dict()

