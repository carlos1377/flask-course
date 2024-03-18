from flask import Flask, jsonify, request

app = Flask(__name__)


purchase_orders = [
    {
        'id': 1,
        'description': 'Pedido de compra 1',
        'items': [
            {
                'id': 1,
                'description': 'Item pedido 1',
                'price': 20.99
            }
        ]
    }
]

# GET purchase_orders
# GET purchase_orders_by_id
# POST purchase_orders
# GET purchase_orders_items
# POST purchase_orders_items


@app.route('/')
def index():
    return {'Hello': 'world'}


@app.route('/purchase_orders')
def get_purchase_orders():
    return jsonify(purchase_orders)


@app.route('/purchase_orders/<int:id>')
def get_purchase_orders_by_id(id: int):
    for po in purchase_orders:
        if po['id'] == id:
            return jsonify(po)
        return jsonify({
            'message': f'Pedido {id} não encontrado'
        })


@app.route('/purchase_orders', methods=['POST'])
def create_purchase_order():
    request_data = request.get_json()
    purchase_order = {
        'id': request_data['id'],
        'description': request_data['description'],
        'items': []
    }

    purchase_orders.append(purchase_order)

    return jsonify(purchase_order)


@app.route('/purchase_orders/<int:id>/items', methods=['POST'])
def create_purchase_orders_items(id: int):
    request_data = request.get_json()
    for po in purchase_orders:
        if po['id'] == id:
            po['items'].append({
                'id': request_data['id'],
                'description': request_data['description'],
                'price': request_data['price'],

            })
            return jsonify(po)
        return jsonify({
            'message': f'Pedido {id} não encontrado'
        })


@app.route('/purchase_orders/<int:id>/items')
def get_purchase_order_items(id: int):
    for po in purchase_orders:
        if po['id'] == id:
            return jsonify(po['items'])
    return jsonify({
        'message': f'Pedido {id} não encontrado'
    })


app.run(debug=True)
