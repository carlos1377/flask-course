from flask import Flask, jsonify
from flask_restful import Api, Resource
from purchase_orders.routes import PurchaseOrders

app = Flask(__name__)
api = Api(app=app)


api.add_resource(PurchaseOrders, '/purchase_orders')

app.run(debug=True)
