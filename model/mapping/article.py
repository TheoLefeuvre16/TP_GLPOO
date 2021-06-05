from model.mapping import Base
import uuid


from sqlalchemy import Column, String, UniqueConstraint, Integer


class Article(Base):
    __tablename__ = 'articles'
    __table_args__ = (UniqueConstraint('name'),)

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    name = Column(String(50), nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    id_seller = Column(String(50), nullable=False)

    def __repr__(self):
        return "<Article N° %s(%s %d€ - %d restant - vendeur : %s)>" % (self.id, self.name, self.price, self.stock, self.id_seller)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "id_seller": self.id_seller
        }
