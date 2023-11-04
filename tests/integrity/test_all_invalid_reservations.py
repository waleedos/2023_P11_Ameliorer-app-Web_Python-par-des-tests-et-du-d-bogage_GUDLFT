# Importation de pytest pour les fixtures et du serveur pour l'application Flask et les fonctions
# de chargement des données.
import pytest
from server import app, load_clubs, load_competitions


# Configuration d'un client de test pour simuler des requêtes à l'application Flask.
@pytest.fixture
def test_client():
    app.config['TESTING'] = True  # Activer le mode test de Flask.
    with app.test_client() as client:
        yield client  # Renvoyer le client pour être utilisé dans les tests.


# Fixture pour configurer un ensemble de données de test à partir des fonctions de chargement.
@pytest.fixture
def database_fixture():
    # Charger les compétitions et les clubs à partir des fonctions définies dans le serveur.
    return {
        "competitions": load_competitions(),
        "clubs": load_clubs()
    }


# Test pour vérifier les scénarios de réservation invalide.
def test_invalid_booking(test_client, database_fixture):
    # Utiliser la première compétition et le premier club pour les tests.
    competition = database_fixture['competitions'][0]  # Première compétition.
    club = database_fixture['clubs'][0]['name']  # Nom du premier club.

    # Tentative de réservation avec un nombre de places supérieur à la disponibilité.
    response = test_client.post('/purchasePlaces', data={
        "club": club,
        "competition": competition["name"],
        "places": 100  # Nombre de places demandé trop élevé.
    }, follow_redirects=True)
    # Vérification de la présence du message d'erreur dans la réponse.
    assert b'You tried to book an invalid number of places, sorry' in response.data

    # Tentative de réservation avec un nombre de places supérieur aux points du club.
    response = test_client.post('/purchasePlaces', data={
        "club": club,
        "competition": competition["name"],
        "places": 20  # Nombre de places demandé dépasse les points du club.
    }, follow_redirects=True)
    # Vérification de la présence du message d'erreur dans la réponse.
    assert b'You tried to book an invalid number of places, sorry' in response.data

    # Tentative de réservation de plus de 12 places pour une compétition.
    response = test_client.post('/purchasePlaces', data={
        "club": club,
        "competition": competition["name"],
        "places": 13  # Plus de 12 places est invalide.
    }, follow_redirects=True)
    # Vérification de la présence du message d'erreur dans la réponse.
    assert b'You tried to book an invalid number of places, sorry' in response.data
