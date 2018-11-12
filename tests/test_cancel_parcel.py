from flask import jsonify, json

def test_cancel_parcels(test_client):
<<<<<<< HEAD
	"""
		Given an API user
		When I submit a put to http://127.0.0.1:5000/api/v1/parcels/<parcelId>/cancel
		  And  the parcel delivery order has given the parcelId
		Then an asset is created
		  And the system returns an http status code 404 clients Bad Resquest
		  And the system returns the URI for the cancelled parcel
	"""
	data={'parcelId': 4, 'item': 'laptop', 'weight': '3.9kg', 'userId': 1,\
	        'commentDescription':'thanks', 'locationPicker': 'america',\
	         'destination': 'kyengera', 'status': False }
	response = test_client.put('/api/v1/parcels/<int:1>/cancel', data=json.dumps(data))
	response.status_code == 204
	assert test_client.get('/api/v1/parcels/<int:parcelId>/cancel').status_code == 404
=======
	assert test_client.get('/parcels/<int:parcelId>/cancel')
	data={'parcelId': 4, 'item': 'laptop', 'weight': '3.9kg', 'userId': 1,\
	        'commentDescription':'thanks', 'locationPicker': 'america',\
	         'destination': 'kyengera', 'status': False }
	response = test_client.put('/parcels/<int:1>/cancel', data=json.dumps(data))
	response.status_code == 200
	assert test_client.get('/parcels/<int:parcelId>/cancel').status_code == 404
>>>>>>> 37f39ede0e30d7e8a6a3bc2c0d50d23708ad2b57

