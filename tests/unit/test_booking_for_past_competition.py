# Importation des éléments nécessaires depuis le module 'server'.
from server import app, load_competitions, load_clubs
# Importation de pytest pour les tests.
import pytest

# Section pour tester la réservation pour une compétition passée.
# ****** Test Booking for a past competition ****** #


# Configuration d'un client de test Flask.
@pytest.fixture
def test_client():
    app.config['TESTING'] = True  # Activer le mode test de Flask.
    with app.test_client() as client:
        yield client  # Fournir le client de test.


# Préparation des données de test.
@pytest.fixture
def database_fixture():
    # Chargement des compétitions et des clubs pour les tests.
    data = {
        "competition_1": load_competitions()[0],
        "competition_2": load_competitions()[1],
        "club_1": load_clubs()[0],
        "club_2": load_clubs()[1]
    }
    return data  # Retour des données de test.


# Test de réservation pour une compétition passée.
def test_booking_for_past_competition(test_client, database_fixture):
    competition = database_fixture['competition_2']  # Sélection d'une compétition passée.
    # Envoi d'une requête de réservation.
    response = test_client.get('/book/' + competition['name'] + '/Simply Lift')
    # Vérification que le message d'erreur attendu est dans la réponse.
    assert b"Selected competition is over" in response.data
