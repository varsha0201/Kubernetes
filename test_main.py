'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'TestSecret'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODI0NTI2NDMsIm5iZiI6MTU4MTI0MzA0MywiZW1haWwiOiJ2YXJzaGFtb2hpdGUwMjAxQGdtYWlsLmNvbSJ9.e613Wzm7mlCO0BVmyLbuN0mjo3G8CZdWF9CxLmYN_XM'
EMAIL = 'wolf@thedoor.com'
PASSWORD = 'huff-puff'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert False
    token = response.json['token']
    assert token is not None