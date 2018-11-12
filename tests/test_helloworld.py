from flask import jsonify, json

<<<<<<< HEAD
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
=======
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
>>>>>>> 37f39ede0e30d7e8a6a3bc2c0d50d23708ad2b57
