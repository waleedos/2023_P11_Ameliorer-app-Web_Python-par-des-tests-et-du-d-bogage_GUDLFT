# Importation de l'application Flask et de pytest pour les tests.
from server import app
import pytest


# Configuration d'une fixture pour initialiser un client de test Flask.
@pytest.fixture
def client():
    app.config['TESTING'] = True  # Activation du mode de test dans la configuration de l'application.
    with app.test_client() as client:
        yield client  # Fourniture du client de test pour les fonctions de test.


# Test de la route principale pour s'assurer qu'elle se charge correctement.
def test_index_route(client):
    response = client.get('/')  # Envoi d'une requête GET à la page d'accueil.
    assert response.status_code == 200  # Vérification du code de statut 200 (OK).
    # Vérification que le texte attendu est présent dans les données de la réponse.
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data


# Test pour vérifier la gestion d'un e-mail invalide dans le résumé.
def test_show_summary_invalid_email(client):
    # Envoi d'une requête POST avec un e-mail invalide.
    response = client.post('/showSummary', data={'email': 'invalid@email.com'})
    assert response.status_code == 200  # Vérification que la page se charge toujours correctement.
    # Vérification que le message d'erreur approprié est affiché.
    assert b'Sorry, that email wasn\'t found.' in response.data


# Test pour vérifier la gestion d'une compétition ou d'un club invalide lors de la réservation.
def test_book_invalid_competition_or_club(client):
    try:
        # Tentative d'accès à une route de réservation avec des valeurs invalides.
        client.get('/book/InvalidCompetition/InvalidClub')
    except IndexError:
        assert True  # L'exception IndexError est attendue ici.
    else:
        assert False  # Si aucune exception n'est levée, le test doit échouer.


# Test pour vérifier la gestion d'un nombre invalide de places à l'achat.
def test_purchase_invalid_number_of_places(client):
    # Simulation d'une session pour un utilisateur et une compétition spécifiques.
    with client.session_transaction() as session:
        session['email'] = 'john@simplylift.co'
        session['club'] = 'Simply Lift'
        session['competition'] = 'Spring Festival'
    # Envoi d'une requête POST avec un nombre de places invalide.
    response = client.post('/purchasePlaces', data={'places': -1})
    # Vérification que le serveur répond avec un code d'erreur 400 (Bad Request).
    assert response.status_code == 400
