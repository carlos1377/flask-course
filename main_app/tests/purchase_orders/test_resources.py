import json
import pytest
from flask import Flask


def test_get_purchase_orders(test_client):
    response = test_client.get('/purchase_orders')

    assert response.status_code == 200

    assert response.json[0]['id'] == 1
    assert len(response.json[0]['items']) == 1
    assert response.json[0]['items'][0]['id'] == 1


def test_post_purchase_orders(test_client):
    obj = {
        'id': 2,
        'description': 'Purchase Order 2',
    }

    response = test_client.post(
        '/purchase_orders',
        data=json.dumps(obj),
        content_type='application/json'
    )

    assert response.status_code == 200

    assert response.json['id'] == obj['id']
    assert response.json['description'] == obj['description']
    assert response.json['items'] == []


def test_post_purchase_orders_empty_id(test_client):
    response = test_client.post(
        '/purchase_orders',
        data=json.dumps({'description': 'teste'}),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['id'] == 'Informe um ID válido'


def test_post_purchase_orders_empty_description(test_client):
    response = test_client.post(
        '/purchase_orders',
        data=json.dumps({'id': 3}),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['description'] == 'Informe uma descrição válida'  # noqa


def test_get_purchase_orders_by_id(test_client: Flask):
    response = test_client.get('/purchase_orders/1')

    assert response.status_code == 200
    assert response.json['id'] == 1
    assert response.json['description'] == 'Pedido de compra 1'


def test_get_purchase_orders_by_id_invalid(test_client: Flask):
    id = 77777
    response = test_client.get(f'/purchase_orders/{id}')

    assert response.status_code == 200
    assert response.json['message'] == f'Pedido de ID {id} não encontrado'
