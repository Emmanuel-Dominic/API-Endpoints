from flask import jsonify, json

def test_get_parcel(test_client):
    """
    Given an API User
    When I submit a get to http://127.0.0.1:5000/api/v1/parcels/<parcelId>/
    Then the system is to return the Get request with specific parcel delivery order
    """
    data={'parcelId': 4, 'item': 'laptop', 'weight': '3.9kg', 'userId': 1,\
        'commentDescription':'thanks', 'locationPicker': 'america',\
         'destination': 'kyengera', 'status': True }
    response = test_client.get('/api/v1/parcels/<int:1>')
    assert response.status_code, 200
    assert test_client.get('/api/v1/parcels/<int:1>',data = json.dumps(data))
    
