from flask import Flask
from flask_restful import Api
from main_app.purchase_orders.resources import PurchaseOrders, PurchaseOrderById  # noqa
from main_app.purchase_orders_items.resources import PurchaseOrderItems


def create_app():
    app = Flask(__name__)
    api = Api(app=app)

    api.add_resource(PurchaseOrders, '/purchase_orders')
    api.add_resource(PurchaseOrderById, '/purchase_orders/<int:id>')
    api.add_resource(PurchaseOrderItems, '/purchase_orders/<int:id>/items')

    return app
