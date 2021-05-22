from model.mapping import Base
import uuid

from sqlalchemy import Column, String, UniqueConstraint , Integer

class Guest(Base):
    __tablename__ = 'guest'
    __table_args__ = (UniqueConstraint('horaires', 'lieu','id_personne'),)

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    horaires = Column(String(50), nullable=False)
    lieu = Column(String(50), nullable=False)
    id_personne = Column(Integer, nullable=False)

    def __repr__(self):
        return "<guest  n°%s (%s %s %d )>" % (self.id, self.horaires, self.lieu , self.id_personne)

    def to_dict(self):
        return {
            "id": self.id,
            "horaires": self.horaires,
            "lieu": self.lieu,
            "id_personne": self.id_personne,

        }
