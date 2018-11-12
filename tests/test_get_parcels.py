from flask import jsonify, json

def test_get_parcels(test_client):
    """
<<<<<<< HEAD
    Given an API User
    When I submit a get to http://127.0.0.1:5000/api/v1/parcels/
    Then the system is to return the Get request with all parcel delivery orders
=======
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
>>>>>>> 37f39ede0e30d7e8a6a3bc2c0d50d23708ad2b57
    """
    data = {"ALL_PARCEL_ORDERS ":[{"commentDescription":"thanks",\
        "destination":"kyengera","item":"laptop","locationPicker":"america",\
        "parcelId":1,"status":True,"userId":2,"weight":"3.9kg"},\
        {"commentDescription":"thanks","destination":"kyengera","item":"laptop",\
        "locationPicker":"america","parcelId":2,"status":True,"userId":3,"weight":"3.9kg"},\
        {"commentDescription":"thanks","destination":"kyengera","item":"laptop4",\
        "locationPicker":"america","parcelId":3,"status":True,"userId":2,"weight":"3.9kg"},\
        {"commentDescription":"thanks","destination":"kyengera","item":"laptop",\
        "locationPicker":"america","parcelId":4,"status":True,"userId":1,\
        "weight":"3.9kg"}]}
<<<<<<< HEAD
    response = test_client.get('/api/v1/parcels')
    assert response.status_code, 200
    assert test_client.get('/api/v1/parcels',data = json.dumps(data))
=======
    response = test_client.get('/parcels')
    assert response.status_code, 200
    assert test_client.get('/parcels',data = json.dumps(data))
>>>>>>> 37f39ede0e30d7e8a6a3bc2c0d50d23708ad2b57
    
