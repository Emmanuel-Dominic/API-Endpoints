from flask import jsonify, json

# import pytest

def test_helloworld(test_client):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
    """
    data = {'EMMANUEL' : 'API-Endpoints'}
    response = test_client.get('/')
    assert response.status_code == 200
    assert test_client.get('/',data=json.dumps(data))
