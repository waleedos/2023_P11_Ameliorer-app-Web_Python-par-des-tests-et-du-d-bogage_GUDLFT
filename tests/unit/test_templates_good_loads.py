# Importation de pytest pour les tests et de l'application Flask.
import pytest
from server import app


# Configuration d'une fixture pour initialiser un client de test Flask.
@pytest.fixture
def client():
    app.config['TESTING'] = True  # Activation du mode de test pour l'application.
    with app.test_client() as client:
        yield client  # Mise à disposition du client de test pour les fonctions de test.


# Test pour vérifier le contenu de la template de la page d'accueil.
def test_index_template(client):
    response = client.get('/')  # Envoi d'une requête GET à la page d'accueil.
    # Vérification que le message de bienvenue attendu est présent dans les données de réponse.
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data


# Test pour vérifier le contenu de la template de la table des clubs.
def test_club_table_template(client):
    response = client.get('/club_table.html')  # Envoi d'une requête GET à la route de la table des clubs.
    # Vérification que la description attendue est présente dans les données de réponse.
    assert b'Liste de tous les clubs avec leurs points disponibles' in response.data


# Test pour vérifier le contenu de la template de bienvenue après connexion.
def test_welcome_template(client):
    with client.session_transaction() as session:
        session['email'] = 'john@simplylift.co'  # Simulation d'une session avec un email spécifique.
    # Envoi d'une requête POST pour simuler l'accès à la page de résumé après connexion.
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    # Vérification que le message de bienvenue est présent dans les données de réponse.
    assert b'Welcome,' in response.data
