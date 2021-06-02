from model.mapping import Base
import uuid

from sqlalchemy import Column, String, UniqueConstraint, Integer

class Seller(Base):
    __tablename__ = 'guest'
    __table_args__ = (UniqueConstraint('horaires', 'lieu','id_personne'),)

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)
    money = Column(Integer, nullable=False)

    def __repr__(self):
        return "<guest  n°%s (%s %s %d )>" % (self.id, self.horaires, self.lieu, self.id_personne)

    def to_dict(self):
        return {
            "id": self.id,
            "money": self.money,

        }
