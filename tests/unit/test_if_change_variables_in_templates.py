from server import app
import pytest


# Utilisation d'une fixture pour initialiser le client de test Flask
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# Test pour vérifier si les variables dans le template index.html sont correctement remplacées
def test_variables_in_index_template(client):
    response = client.get('/')
    assert b'GUDLFT Registration Portal' in response.data  # Remplacez par le texte réel
    assert b'Please enter your secretary email to continue:' in response.data  # Remplacez par le texte réel


# Test pour vérifier si les variables dans le template welcome.html sont correctement remplacées
def test_variables_in_welcome_template(client):
    client.post('/showSummary', data={'email': 'john@simplylift.co'})
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'}, follow_redirects=True)
    # Changé en POST
    assert b'Welcome, john@simplylift.co' in response.data  # Assurez-vous que ce texte est dans le template
