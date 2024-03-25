from main_app.purchase_orders_items.resources import PurchaseOrderItems
from main_app.purchase_orders.resources import PurchaseOrders, PurchaseOrderById, HealthCheck  # noqa
from flask_restful import Api
from main_app.db import db
from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    api = Api(app=app)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    api.add_resource(PurchaseOrders, '/purchase_orders')
    api.add_resource(PurchaseOrderById, '/purchase_orders/<int:id>')
    api.add_resource(PurchaseOrderItems, '/purchase_orders/<int:id>/items')

    api.add_resource(HealthCheck, '/health-check')

    with app.app_context():
        db.create_all()

    return app
