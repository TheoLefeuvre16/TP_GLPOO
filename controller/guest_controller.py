import re

from controller.personne_controller import PersonneController
from model.dao.guest_dao import GuestDAO
from model.dao.personne_dao import PersonneDAO
from exceptions import Error, InvalidData
class GuestController(PersonneController):

    """
    Guest actions
    """

    def __init__(self, database_engine):
        super().__init__(database_engine)
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
        print("entering create_guest")
       # self._check_profile_data(data)
        try:
            with self._database_engine.new_session() as session:
                # Save member in database
                print("with ok")
                personne = PersonneDAO(session).create(data_personne)
                personne_data = personne.to_dict()
                print(personne_data)
                data_guest['id_personne'] = personne_data.get('id')
                guest = GuestDAO(session).create(data_guest)
                guest_data = guest.to_dict()
                print(guest_data)
                print("exiting create_guest")
                return guest_data
        except Error as e:
            # log error
            print("error in create_guest")
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

    def get_person(self, id):
        with self._database_engine.new_session() as session:
            guest = PersonneDAO(session).get(id)
            guest_data = guest.to_dict()
        return guest_data

