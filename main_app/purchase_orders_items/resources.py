from flask import jsonify
from flask_restful import Resource, reqparse

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
    parser = reqparse.RequestParser()
    parser.add_argument(
        'id',
        type=int,
        required=True,
        help='Informe um ID válido'
    )
    parser.add_argument(
        'description',
        type=str,
        required=True,
        help='Informe uma descrição válida'
    )
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help='Informe um preço válido'
    )

    def get(self, id):
        for po in purchase_orders:
            if po['id'] == id:
                return jsonify(po['items'])
        return jsonify({'message': f'Pedido de ID {id} não encontrado'})

    def post(self, id):
        data = PurchaseOrderItems().parser.parse_args()

        for po in purchase_orders:
            if po['id'] == id:
                po['items'].append({
                    'id': data['id'],
                    'description': data['description'],
                    'price': data['price'],
                }
                )

                return jsonify(po)

        return jsonify({'message': f'Purchase order {id} não encontrado'})
