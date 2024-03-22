import json


def test_get_items_by_purchase_order_id(test_client):
    response = test_client.get('/purchase_orders/1/items')

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['id'] == 1
    assert response.json[0]['description'] == 'Item do pedido 1'
    assert response.json[0]['price'] == 20.99


def test_get_item_by_purchase_order_id_not_found(test_client):
    id = 99999
    response = test_client.get(f'/purchase_orders/{id}/items')

    assert response.status_code == 200
    assert response.json['message'] == f'Pedido de ID {id} não encontrado'


def test_post_purchase_order_item(test_client):
    obj = {
        'id': 2,
        'description': 'Lorem ipsum',
        'price': 14.99,
    }

    response = test_client.post(
        '/purchase_order_items/1/items',
        data=json.dumps(obj),
        content_type='application/json'
    )

    assert response.status_code == 200
    assert response.json['id'] == 1
    assert len(response.json['items']) == 2
    assert response.json['items'][1]['id'] == obj['id']
    assert response.json['items'][1]['description'] == obj['description']
    assert response.json['items'][1]['price'] == obj['price']


def test_post_purchase_order_item_invalid_id(test_client):
    obj = {
        'description': 'Lorem ipsum',
        'price': 14.99,
    }

    response = test_client.post(
        '/purchase_order_items/1/items',
        data=json.dumps(obj),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['id'] == 'Informe um ID válido'


def test_post_purchase_order_item_invalid_description(test_client):
    obj = {
        'id': 2,
        'price': 14.99,
    }

    response = test_client.post(
        '/purchase_order_items/1/items',
        data=json.dumps(obj),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['description'] == 'Informe uma descrição válida'  # noqa


def test_post_purchase_order_item_invalid_price(test_client):
    obj = {
        'id': 2,
        'description': 'Lorem ipsum',
    }

    response = test_client.post(
        '/purchase_order_items/1/items',
        data=json.dumps(obj),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['price'] == 'Informe um preço válido'
