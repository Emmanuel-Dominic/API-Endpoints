from flask import jsonify, json

def test_create_parcels(test_client):
    """
    Given an API user
	When I submit a post to http://127.0.0.1:5000/POST /parcels/
	Then an asset is created
	  And the system returns an http status code 201 created
	  And the system returns the URI for the created parcel
    """
    data={'item':'television','weight':'5.8kgs','userId': '1','commentDescription':'hello','locationPicker':'bwaise','destination':'wakiso'}
    assert test_client.get('/api/v1/parcels')
    response = test_client.post('/api/v1/parcels', data=json.dumps(data))
    assert response.status_code, 201
