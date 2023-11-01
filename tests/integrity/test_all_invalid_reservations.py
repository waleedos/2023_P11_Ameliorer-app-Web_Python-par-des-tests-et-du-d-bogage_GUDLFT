import pytest
from server import app, load_clubs, load_competitions


# Fixtures
@pytest.fixture
def test_client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def database_fixture():
    return {
        "competitions": load_competitions(),
        "clubs": load_clubs()
    }


# Test de réservation invalide
def test_invalid_booking(test_client, database_fixture):
    # Initialisation des données
    competition = database_fixture['competitions'][0]  # Utilisation de la première compétition pour l'exemple
    club = database_fixture['clubs'][0]['name']  # Utilisation du premier club pour l'exemple

    # Test 1: Essayez de réserver plus de places que disponibles
    response = test_client.post('/purchasePlaces', data={
        "club": club,
        "competition": competition["name"],
        "places": 100  # Un nombre de places supérieur à celui disponible
    }, follow_redirects=True)
    assert b'You tried to book an invalid number of places, sorry' in response.data

    # Test 2: Essayez de réserver plus de places que les points du club
    response = test_client.post('/purchasePlaces', data={
        "club": club,
        "competition": competition["name"],
        "places": 20  # Un nombre de places supérieur aux points du club
    }, follow_redirects=True)
    assert b'You tried to book an invalid number of places, sorry' in response.data

    # Test 3: Essayez de réserver plus de 12 places par compétition
    response = test_client.post('/purchasePlaces', data={
        "club": club,
        "competition": competition["name"],
        "places": 13  # Un nombre de places supérieur à 12
    }, follow_redirects=True)
    assert b'You tried to book an invalid number of places, sorry' in response.data
