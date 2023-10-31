from server import app
import pytest


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# ******** Test de la disponibilité des places dans une compétition ********#

def test_competition_availability(client):
    # Étape 1 : Connexion avec un email valide
    client.post('/showSummary', data={'email': 'john@simplylift.co'})

    # Étape 2 : Tenter de réserver une compétition sans places disponibles
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Fully Booked Competition',  # Supposons que cette compétition soit complète
        'places': '1'
    })
    assert b'You tried to book an invalid number of places, sorry' in response.data
