from server import app
import pytest


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# ******************** TEST DE NAVIGATION ********************#

def test_navigation(client):
    # Utilisation d'un email valide existant dans le fichier clubs.json
    client.post('/showSummary', data={'email': 'john@simplylift.co'})

    # Test de navigation vers la table des clubs
    response = client.get('/club_table.html')
    assert response.status_code == 200

    # Test de navigation vers la page de déconnexion
    response = client.get('/logout')
    assert response.status_code == 302  # Attendu car il y a une redirection
