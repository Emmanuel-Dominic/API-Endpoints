from flask import jsonify, json

def test_create_parcels(test_client):
    """
<<<<<<< HEAD
    Given an API user
	When I submit a post to http://127.0.0.1:5000/POST /parcels/
	  And I have filled in
	  -parcelId
	  -item
	  -laptop
	  -weight
	  -userId
	  -commentDescription
	  -locationPicker
	  -destination
	  -status 
	Then an asset is created
	  And the system returns an http status code 201 created
	  And the system returns the URI for the created parcel
    """
    data={'item':'television','weight':'5.8kgs','userId': '1','commentDescription':'hello','locationPicker':'bwaise','destination':'wakiso'}
    assert test_client.get('/api/v1/parcels')
    response = test_client.post('/api/v1/parcels', data=json.dumps(data))
=======
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
    """
    data={'item':'television','weight':'5.8kgs','userId': '1','commentDescription':'hello','locationPicker':'bwaise','destination':'wakiso'}
    assert test_client.get('/parcels').status_code == 200
    response = test_client.post('/parcels', data=json.dumps(data))
>>>>>>> 37f39ede0e30d7e8a6a3bc2c0d50d23708ad2b57
    assert response.status_code, 201
