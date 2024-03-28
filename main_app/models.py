
from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from main_app.db import db
from typing import List


class PurchaseOrdersItemsModel(db.Model):
    __tablename__ = 'purchase_order_items'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    price: Mapped[float] = mapped_column(Float(precision=2), nullable=False)
    purchase_order_id: Mapped[int | None] = mapped_column(
        ForeignKey('purchase_order.id'), nullable=False
    )
    purchase_order: Mapped["PurchaseOrderModel"] = relationship(
        back_populates="purchase_orders_items"
    )

    def __init__(self, description, price, purchase_order_id):
        self.description = description
        self.price = price
        self.purchase_order_id = purchase_order_id

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def find_by_purchase_order_id(cls, _purchase_order_id):
        return cls.query.filter_by(_purchase_order_id=_purchase_order_id).all()

    def save(self):
        db.session.add(self)
        db.session.commit()


class PurchaseOrderModel(db.Model):
    __tablename__ = 'purchase_order'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    purchase_orders_items: Mapped[List["PurchaseOrdersItemsModel"]] = relationship(  # noqa
        back_populates='purchase_order'
    )

    def __init__(self, description) -> None:
        self.description = description

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id: int):
        return cls.query.filter_by(id=_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()


# intpk = Annotated[int, mapped_column(primary_key=True)]
