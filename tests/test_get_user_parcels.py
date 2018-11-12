from flask import jsonify, json

def test_user_parcels(test_client):
    """
<<<<<<< HEAD
    Given an API User
    When I submit a get to http://127.0.0.1:5000/api/v1/users/<userId>/parcels
    Then the system is to return the Get request with all parcel delivery orders by a specific user

=======
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
>>>>>>> 37f39ede0e30d7e8a6a3bc2c0d50d23708ad2b57
    """
    data = {'parcelId': 4, 'item': 'laptop', 'weight': '3.9kg', 'userId': 1,\
        'commentDescription':'thanks', 'locationPicker': 'america',\
         'destination': 'kyengera', 'status': True }
<<<<<<< HEAD
    assert test_client.get('/api/v1/users/<int:userId>/parcels').status_code == 404
    response = test_client.post('/api/v1/users/<int:1>/parcels', data=json.dumps(data))
=======
    assert test_client.get('/users/<int:userId>/parcels').status_code == 404
    response = test_client.post('/users/<int:1>/parcels', data=json.dumps(data))
>>>>>>> 37f39ede0e30d7e8a6a3bc2c0d50d23708ad2b57
    assert response.status_code, 200