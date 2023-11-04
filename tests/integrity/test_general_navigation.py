# Importation du module pytest pour la gestion des tests et du module app pour l'application Flask.
import pytest
from server import app


# Création d'une fixture pour initialiser un client de test.
@pytest.fixture
def test_client():
    app.config['TESTING'] = True  # Activation du mode test pour l'application.
    with app.test_client() as client:
        yield client  # Fourniture du client de test pour les fonctions de test.


# Fonction pour tester la navigation dans l'application web.
def test_navigation(test_client):
    # Test 1: Accéder à la page d'accueil et vérifier la réponse.
    response = test_client.get('/')
    assert response.status_code == 200  # Vérification que la page d'accueil est accessible (code 200).
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data  # Vérification du contenu de
    # la page d'accueil.

    # Test 2: Accéder à la page du tableau des clubs et vérifier la réponse.
    response = test_client.get('/club_table.html')
    assert response.status_code == 200  # Vérification que la page du tableau des clubs est accessible (code 200).
    assert b'club_table' in response.data  # Vérification du contenu de la page du tableau des clubs.

    # Test 3: Essayer d'accéder à une page qui n'existe pas et vérifier la réponse.
    response = test_client.get('/non_existent_page')
    assert response.status_code == 404  # Vérification que le serveur retourne une erreur 404 pour une page inexistante.
