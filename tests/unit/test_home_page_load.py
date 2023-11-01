from server import app
import pytest


@pytest.fixture
def test_client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# ****** Test Home Page Load ****** #

def test_index_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data
