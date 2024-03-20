def test_get_purchase_orders(test_client):
    response = test_client.get('/purchase_orders')
