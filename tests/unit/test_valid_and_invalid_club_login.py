# Importation de l'application Flask et de pytest pour les tests.
from server import app
import pytest


# Configuration d'une fixture pour initialiser un client de test Flask.
@pytest.fixture
def test_client():
    app.config['TESTING'] = True  # Activation du mode de test pour l'application.
    with app.test_client() as client:
        yield client  # Mise à disposition du client de test pour les fonctions de test.


# Test pour vérifier le comportement de la connexion avec un club invalide.
def test_login_with_invalid_club(test_client):
    # Envoi d'une requête POST avec un e-mail de club invalide.
    response = test_client.post('/showSummary', data={'email': 'invalid@club.com'})
    # Vérification que le message d'erreur est présent dans la réponse.
    assert b"Sorry, that email wasn't found." in response.data


# Test pour vérifier le comportement de la connexion avec un club valide.
def test_login_with_valid_club(test_client):
    # Envoi d'une requête POST avec un e-mail de club valide.
    response = test_client.post('/showSummary', data={'email': 'john@simplylift.co'})
    # Vérification que le message de bienvenue est présent dans la réponse.
    assert b"Welcome," in response.data
