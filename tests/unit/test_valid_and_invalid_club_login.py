from server import app
import pytest


@pytest.fixture
def test_client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# ****** Test Invalid Club Login ****** #

def test_login_with_invalid_club(test_client):
    response = test_client.post('/showSummary', data={'email': 'invalid@club.com'})
    assert b"Sorry, that email wasn't found." in response.data


# ****** Test valid Club Login ****** #


def test_login_with_valid_club(test_client):
    response = test_client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert b"Welcome," in response.data
