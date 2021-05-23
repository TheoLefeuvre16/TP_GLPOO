from model.mapping import Base
import uuid


from sqlalchemy import Column, String, UniqueConstraint


class Article(Base):
    __tablename__ = 'articles'

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    name = Column(String(50), nullable=False)
    price = Column(String(50), nullable=False)

    stock = Column(String(256), nullable=False)
    id_seller = Column(String(10), nullable=False)

    def __repr__(self):
        return "<Article(%s %s€ - %s restant)>" % (self.name, self.price, self.stock)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "id_seller": self.id_seller
        }
