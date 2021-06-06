from model.mapping import Base
import uuid


from sqlalchemy import Column, String, UniqueConstraint , Integer


class Personne(Base):
    __tablename__ = 'personne'
    __table_args__ = (UniqueConstraint('email'),)

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(256), nullable=False)
    statut = Column(String(50), nullable=False)
    mdp = Column(String(50), nullable=False)

    def __repr__(self):
        return "<Personne n°%s (%s %s %d %s %s %s)>" % (self.id, self.firstname, self.lastname.upper(),self.age, self.email , self.statut, self.mdp)

    def to_dict(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "age": self.age,
            "email": self.email,
            "statut": self.statut,
            "mdp": self.mdp
        }
