from server import app, load_competitions, load_clubs
import pytest


# Définition de la fixture pour le client de test Flask
@pytest.fixture
def test_client():
    app.config['TESTING'] = True  # Activation du mode de test
    with app.test_client() as client:
        yield client  # Retour du client de test


# Définition de la fixture pour les données de test
@pytest.fixture
def database_fixture():
    data = {
        "competition_1": load_competitions()[5],  # Assurez-vous que c'est une compétition future
        "competition_2": load_competitions()[1],  # Assurez-vous que c'est une compétition passée
        "club_1": load_clubs()[0],
        "club_2": load_clubs()[1]
    }
    return data  # Retour des données de test


# Test pour vérifier la réservation pour une compétition passée
def test_booking_for_past_competition(test_client, database_fixture):
    competition = database_fixture['competition_2']  # Sélection de la compétition passée
    club = database_fixture['club_1']['name']  # Utilisation du nom du club pour la réservation
    response = test_client.post(f'/book/{competition["name"]}/{club}')  # Envoi de la requête de réservation
    assert b"Selected competition is over" in response.data  # Vérification du message d'erreur
