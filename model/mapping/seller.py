from model.mapping import Base
import uuid

from sqlalchemy import Column, String, UniqueConstraint, Integer

class Seller(Base):
    __tablename__ = 'seller'
    __table_args__ = (UniqueConstraint('id_personne'),)

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)
    money = Column(Integer, nullable=False)
    id_personne = Column(Integer, nullable=False)

    def __repr__(self):
        return "<seller  n°%s, money : %d, idpersonne : %d>" % (self.id, self.money, self.id_personne)

    def to_dict(self):
        return {
            "id": self.id,
            "money": self.money,
            "id_personne": self.id_personne,

        }
