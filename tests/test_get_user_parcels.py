from flask import jsonify, json

def test_user_parcels(test_client):
    """
    Given an API User
    When I submit a get to http://127.0.0.1:5000/api/v1/users/<userId>/parcels
    Then the system is to return the Get request with all parcel delivery orders by a specific user

    """
    data = {'parcelId': 4, 'item': 'laptop', 'weight': '3.9kg', 'userId': 1,\
        'commentDescription':'thanks', 'locationPicker': 'america',\
         'destination': 'kyengera', 'status': True }
    assert test_client.get('/api/v1/users/<int:userId>/parcels').status_code == 404
    response = test_client.post('/api/v1/users/<int:1>/parcels', data=json.dumps(data))
    assert response.status_code, 200