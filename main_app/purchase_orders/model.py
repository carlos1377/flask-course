from main_app.db import db
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped


class PurchaseOrderModel(db.Model):
    __tablename__ = 'purchase_order'
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(500), nullable=False)

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
