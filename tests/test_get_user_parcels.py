from flask import jsonify, json

def test_user_parcels(test_client):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
    """
    data = {'parcelId': 4, 'item': 'laptop', 'weight': '3.9kg', 'userId': 1,\
        'commentDescription':'thanks', 'locationPicker': 'america',\
         'destination': 'kyengera', 'status': True }
    assert test_client.get('/users/<int:userId>/parcels').status_code == 404
    response = test_client.post('/users/<int:1>/parcels', data=json.dumps(data))
    assert response.status_code, 200