from main_app.db import db
from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from typing_extensions import Annotated


intpk = Annotated[int, mapped_column(primary_key=True)]


class PurchaseOrderItemsModel(db.Model):
    __tablename__ = 'purchase_order_items'
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    price: Mapped[float] = mapped_column(Float(precision=2), nullable=False)
    purchase_order_id: Mapped[intpk] = mapped_column(
        ForeignKey('purchase_order.id'), nullable=False
    )

    def __init__(self, description, price, purchase_order_id):
        self.description = description
        self.price = price
        self.purchase_order_id = purchase_order_id

    def as_dict(self):
        return {c.name: getattr(c.name) for c in self.__table__.columns}

    @classmethod
    def find_by_purchase_order_id(cls, _purchase_order_id):
        return cls.query.filter_by(_purchase_order_id=_purchase_order_id).all()

    def save(self):
        db.session.add(self)
        db.session.commit()
