# Importation de l'application Flask depuis le module 'server'.
from server import app
# Importation de pytest pour les tests.
import pytest


# Configuration de la fixture pour initialiser un client de test Flask.
@pytest.fixture
def client():
    app.config['TESTING'] = True  # Activation du mode de test pour l'application.
    with app.test_client() as client:
        yield client  # Fourniture du client de test pour les fonctions de test.


# Test pour vérifier les variables dans le template 'index.html'.
def test_variables_in_index_template(client):
    response = client.get('/')  # Envoi d'une requête GET à la racine de l'application.
    # Vérification que le texte attendu est présent dans la réponse.
    assert b'GUDLFT Registration Portal' in response.data  # Texte attendu du portail d'enregistrement.
    # Vérification que les instructions sont présentes dans la réponse.
    assert b'Please enter your secretary email to continue:' in response.data  # Instructions pour l'utilisateur.


# Test pour vérifier les variables dans le template 'welcome.html'.
def test_variables_in_welcome_template(client):
    # Envoi d'une requête POST pour simuler la connexion d'un utilisateur.
    client.post('/showSummary', data={'email': 'john@simplylift.co'})
    # Envoi d'une requête POST avec suivi des redirections.
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'}, follow_redirects=True)
    # Vérification que le message de bienvenue est correctement formaté avec l'email de l'utilisateur.
    assert b'Welcome, john@simplylift.co' in response.data  # Message de bienvenue attendu.
