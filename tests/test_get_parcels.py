from flask import jsonify, json

def test_get_parcels(test_client):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
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
    response = test_client.get('/parcels')
    assert response.status_code, 200
    assert test_client.get('/parcels',data = json.dumps(data))
    
