import pytest
from server import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_template(client):
    response = client.get('/')  # Correspond à la route de la page d'accueil
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data


def test_club_table_template(client):
    response = client.get('/club_table.html')  # Correspond à la route de la table des clubs
    assert b'Liste de tous les clubs avec leurs points disponibles' in response.data


def test_welcome_template(client):
    with client.session_transaction() as session:
        session['email'] = 'john@simplylift.co'  # Simuler une session
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})  # Correspond à la route
    # de la page de résumé
    assert b'Welcome,' in response.data
