from flask import jsonify, json

def test_create_parcels(test_client):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
    """
    data={'item':'television','weight':'5.8kgs','userId': '1','commentDescription':'hello','locationPicker':'bwaise','destination':'wakiso'}
    assert test_client.get('/parcels').status_code == 200
    response = test_client.post('/parcels', data=json.dumps(data))
    assert response.status_code, 201
