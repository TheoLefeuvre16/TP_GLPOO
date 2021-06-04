from model.mapping import Base
import uuid

from sqlalchemy import Column, String, UniqueConstraint, Integer

class Visiteur(Base):
    __tablename__ = 'visiteur'
    __table_args__ = (UniqueConstraint('id_personne'),)
    #3 bools, 0 si mineur, 0 si son ticket ne donne pas acces aux guests, 0 pareil pour les stands

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    age = Column(Integer, nullable=False)
    guest = Column(Integer, nullable=False)
    stand = Column(Integer, nullable=False)
    id_personne = Column(Integer, nullable=False)

    def __repr__(self):
        return "<visiteur  n°%s (%d %d %d %s)>" % (self.id, self.age, self.guest, self.stand, self.id_personne)

    def to_dict(self):
        return {
            "id": self.id,
            "age": self.age,
            "guest": self.guest,
            "stand": self.stand,
            "id_personne": self.id_personne,

        }
