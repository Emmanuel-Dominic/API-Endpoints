from flask import jsonify, json

def test_helloworld(test_client):
    """
    GIVEN a User model
    WHEN a User visits
    THEN welcome note is defined correctly
    """
    data = {'EMMANUEL' : 'API-Endpoints'}
    response = test_client.get('/api/v1/')
    assert response.status_code == 200
    assert test_client.get('/api/v1/',data=json.dumps(data))
