# Importation des modules nécessaires pour les tests.
from server import app, load_competitions, load_clubs
import pytest


# Configuration d'un client de test pour simuler les interactions avec l'application Flask.
@pytest.fixture
def test_client():
    app.config['TESTING'] = True  # Activation du mode test de Flask pour capturer les erreurs.
    with app.test_client() as client:
        yield client  # Renvoi du client de test pour utilisation dans les tests suivants.


# Préparation des données pour les tests à partir des fonctions de chargement des données.
@pytest.fixture
def database_fixture():
    data = {
        "competition_1": load_competitions()[0],  # Choisir une compétition future pour les tests.
        "competition_2": load_competitions()[1],  # Choisir une compétition passée pour vérifier la gestion des erreurs.
        "club_1": load_clubs()[0],
        "club_2": load_clubs()[1]
    }
    return data  # Renvoi du dictionnaire de données pour les tests.


# Test des messages flash pour différentes situations lors de la réservation.
def test_flash_messages(test_client, database_fixture):
    # Test d'une réservation réussie avec un message de confirmation.
    competition = database_fixture['competition_1']
    club = database_fixture['club_1']['name']
    response = test_client.post('/purchasePlaces', data={
        "club": club,
        "competition": competition["name"],
        "places": 1  # Réserver une place valide pour la compétition.
    }, follow_redirects=True)
    # Vérification de la présence du message de succès dans la réponse.
    assert b'Great-booking complete!' in response.data

    # Test d'une réservation invalide avec un message d'erreur.
    competition = database_fixture['competition_1']
    club = database_fixture['club_1']['name']
    response = test_client.post('/purchasePlaces', data={
        "club": club,
        "competition": competition["name"],
        "places": 20  # Tenter de réserver un nombre invalide de places.
    }, follow_redirects=True)
    # Vérification de la présence du message d'erreur dans la réponse.
    assert b'You tried to book an invalid number of places, sorry' in response.data

    # Test d'une tentative de réservation pour une compétition déjà passée avec message d'erreur correspondant.
    competition = database_fixture['competition_2']
    club = database_fixture['club_1']['name']
    response = test_client.get(f'/book/{competition["name"]}/{club}', follow_redirects=True)
    # Vérification que le message indiquant que la compétition est finie est bien présent.
    assert b'Selected competition is over' in response.data
