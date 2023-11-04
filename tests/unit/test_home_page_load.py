# Importation de l'application Flask depuis le module 'server'.
from server import app
# Importation de pytest pour les tests.
import pytest


# Configuration d'un client de test pour l'application Flask.
@pytest.fixture
def test_client():
    app.config['TESTING'] = True  # Activation du mode de test dans la configuration de l'app.
    with app.test_client() as client:
        yield client  # Fourniture du client de test pour les fonctions de test.


# Test du chargement de la page d'accueil.
def test_index_page(test_client):
    response = test_client.get('/')  # Envoi d'une requête GET à la racine de l'application.
    assert response.status_code == 200  # Vérification que le code de statut de la réponse est 200 (OK).
    # Vérification que le contenu de la réponse contient le texte attendu.
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data
