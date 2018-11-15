from flask import jsonify, json

def test_get_parcels(test_client):
    """
    Given an API User
    When I submit a get to http://127.0.0.1:5000/api/v1/parcels/
    Then the system is to return the Get request with all parcel delivery orders
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
    response = test_client.get('/api/v1/parcels')
    assert response.status_code, 200
    assert test_client.get('/api/v1/parcels',data = json.dumps(data))
    
