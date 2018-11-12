from flask import jsonify, json

def test_get_parcel(test_client):
    """
<<<<<<< HEAD
    Given an API User
    When I submit a get to http://127.0.0.1:5000/api/v1/parcels/<parcelId>/
    Then the system is to return the Get request with specific parcel delivery order
=======
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
>>>>>>> 37f39ede0e30d7e8a6a3bc2c0d50d23708ad2b57
    """
    data={'parcelId': 4, 'item': 'laptop', 'weight': '3.9kg', 'userId': 1,\
        'commentDescription':'thanks', 'locationPicker': 'america',\
         'destination': 'kyengera', 'status': True }
<<<<<<< HEAD
    response = test_client.get('/api/v1/parcels/<int:1>')
    assert response.status_code, 200
    assert test_client.get('/api/v1/parcels/<int:1>',data = json.dumps(data))
=======
    response = test_client.get('/parcels/<int:1>')
    assert response.status_code, 200
    assert test_client.get('/parcels/<int:1>',data = json.dumps(data))
>>>>>>> 37f39ede0e30d7e8a6a3bc2c0d50d23708ad2b57
    
