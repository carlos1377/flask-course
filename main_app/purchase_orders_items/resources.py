from flask import jsonify
from flask_restful import Resource

purchase_orders = [
    {
        'id': 1,
        'description': 'Pedido de compra 1',
        'items': [
            {
                'id': 1,
                'description': 'Item do pedido 1',
                'price': 20.99
            }
        ]
    }
]


class PurchaseOrderItems(Resource):
    def get(self, id):
        for po in purchase_orders:
            if po['id'] == id:
                return jsonify(po['items'])
        return jsonify({'message': f'Pedido de ID {id} não encontrado'})
