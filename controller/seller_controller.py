import re

from model.dao.seller_dao import SellerDAO
from exceptions import Error, InvalidData

class SellerController:
    """
    Seller actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine

    def add_article(self,data):
        try:
            with self._database_engine.new_session() as session:
                article = SellerDAO(session).create_article(data)
                article_data = article.to_dict()
                return article_data
        except Error as e:
            raise e



    def list_sellers(self):
        with self._database_engine.new_session() as session:
            sellers = SellerDAO(session).get_all()
            sellers_data = [seller.to_dict() for seller in sellers]
        return sellers_data

    def get_seller(self, member_id):
        with self._database_engine.new_session() as session:
            seller = SellerDAO(session).get(member_id)
            seller_data = seller.to_dict()
        return seller_data

    def create_seller(self, data):

        self._check_profile_data(data)
        try:
            with self._database_engine.new_session() as session:
                # Save member in database
                seller = SellerDAO(session).create(data)
                seller_data = seller.to_dict()
                return seller_data
        except Error as e:
            # log error
            raise e

    def update_member(self, seller_id, seller_data):

        self._check_profile_data(seller_data, update=True)
        with self._database_engine.new_session() as session:
            seller_dao = SellerDAO(session)
            seller = seller_dao.get(seller_id)
            seller = seller_dao.update(seller, seller_data)
            return seller.to_dict()

    def delete_seller(self, member_id):

        with self._database_engine.new_session() as session:
            seller_dao = SellerDAO(session)
            seller = seller_dao.get(member_id)
            seller_dao.delete(seller)

    def search_seller(self, firstname, lastname):

        # Query database
        with self._database_engine.new_session() as session:
            seller_dao = SellerDAO(session)
            seller = seller_dao.get_by_name(firstname, lastname)
            return seller.to_dict()

    def _check_profile_data(self, data, update=False):
        name_pattern = re.compile("^[\S-]{2,50}$")
        type_pattern = re.compile("^(customer|seller)$")
        email_pattern = re.compile("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")
        mandatories = {
            'firstname': {"type": str, "regex": name_pattern},
            'lastname': {"type": str, "regex": name_pattern},
            'email': {"type": str, "regex": email_pattern},
            'type': {"type": str, "regex": type_pattern}
        }
        for mandatory, specs in mandatories.items():
            if not update:
                if mandatory not in data or data[mandatory] is None:
                    raise InvalidData("Missing value %s" % mandatory)
            else:
                if mandatory not in data:
                    continue
            value = data[mandatory]
            if "type" in specs and not isinstance(value, specs["type"]):
                raise InvalidData("Invalid type %s" % mandatory)
            if "regex" in specs and isinstance(value, str) and not re.match(specs["regex"], value):
                raise InvalidData("Invalid value %s" % mandatory)