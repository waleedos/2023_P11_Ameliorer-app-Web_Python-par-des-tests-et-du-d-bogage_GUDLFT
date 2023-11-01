import pytest
from server import app, load_clubs, load_competitions


# Fixture pour le client de test
@pytest.fixture
def test_client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# Fixture pour les données de la base
@pytest.fixture
def database_fixture():
    data = {
        "competition_1": load_competitions()[0],
        "competition_2": load_competitions()[1],
        "club_1": load_clubs()[0],
        "club_2": load_clubs()[1]
    }
    return data


# Test de déconnexion et de session
def test_logout_and_session(test_client, database_fixture):
    # Étape 1: Simuler une connexion
    response = test_client.post('/showSummary', data={
        "email": "dany@austbuild.com"
    }, follow_redirects=True)
    assert b'Welcome' in response.data  # Assurez-vous que la connexion a réussi

    # Étape 2: Simuler une déconnexion
    response = test_client.get('/logout', follow_redirects=True)
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data

    # Étape 3: Tenter d'accéder à showSummary sans être connecté
    response = test_client.post('/showSummary', data={
        "email": ""
    }, follow_redirects=True)
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data
    # L'utilisateur devrait être redirigé vers la page d'accueil
