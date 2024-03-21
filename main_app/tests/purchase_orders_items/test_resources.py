def test_get_items_by_purchase_order_id(test_client):
    response = test_client.get('/purchase_orders/<int:id>/items')

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['id'] == 1
    assert response.json[0]['description'] == 'Item do pedido 1'
    assert response.json[0]['price'] == 17.99
