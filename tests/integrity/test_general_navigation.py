import pytest
from server import app


# Fixtures
@pytest.fixture
def test_client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# Test de navigation
def test_navigation(test_client):
    # Test 1: Accéder à la page d'accueil
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data

    # Test 2: Accéder à la page de tableau des clubs (club_table)
    response = test_client.get('/club_table.html')
    assert response.status_code == 200
    assert b'club_table' in response.data

    # Test 3: Accéder à une page qui n'existe pas (doit retourner 404)
    response = test_client.get('/non_existent_page')
    assert response.status_code == 404
