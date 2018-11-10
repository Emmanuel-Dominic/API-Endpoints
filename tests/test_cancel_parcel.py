from flask import jsonify, json

def test_cancel_parcels(test_client):
	assert test_client.get('/parcels/<int:parcelId>/cancel')
	data={'parcelId': 4, 'item': 'laptop', 'weight': '3.9kg', 'userId': 1,\
	        'commentDescription':'thanks', 'locationPicker': 'america',\
	         'destination': 'kyengera', 'status': False }
	response = test_client.put('/parcels/<int:1>/cancel', data=json.dumps(data))
	response.status_code == 200
	assert test_client.get('/parcels/<int:parcelId>/cancel').status_code == 404

