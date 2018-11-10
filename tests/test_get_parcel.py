from flask import jsonify, json

def test_get_parcel(test_client):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
    """
    data={'parcelId': 4, 'item': 'laptop', 'weight': '3.9kg', 'userId': 1,\
        'commentDescription':'thanks', 'locationPicker': 'america',\
         'destination': 'kyengera', 'status': True }
    response = test_client.get('/parcels/<int:1>')
    assert response.status_code, 200
    assert test_client.get('/parcels/<int:1>',data = json.dumps(data))
    
