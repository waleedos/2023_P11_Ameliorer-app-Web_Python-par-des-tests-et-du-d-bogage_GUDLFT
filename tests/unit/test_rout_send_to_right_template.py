from server import app
import pytest


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200  # Vérifie que la page se charge correctement
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data  # Vérifie que le texte
    # attendu est dans la page.


def test_show_summary_invalid_email(client):
    response = client.post('/showSummary', data={'email': 'invalid@email.com'})
    assert response.status_code == 200  # Vérifie que la page se charge correctement
    assert b'Sorry, that email wasn\'t found.' in response.data  # Vérifie que le message d'erreur est affiché


def test_book_invalid_competition_or_club(client):
    try:
        client.get('/book/InvalidCompetition/InvalidClub')
    except IndexError:
        assert True  # Une exception IndexError est attendue
    else:
        assert False  # Le test échoue si aucune exception n'est levée


def test_purchase_invalid_number_of_places(client):
    # Simuler une session avec des données de club et de compétition
    with client.session_transaction() as session:
        session['email'] = 'john@simplylift.co'
        session['club'] = 'Simply Lift'
        session['competition'] = 'Spring Festival'

    # Envoyer une requête POST avec un nombre de places invalide
    response = client.post('/purchasePlaces', data={'places': -1})

    # Vérifier si la réponse est une erreur 400 Bad Request
    assert response.status_code == 400
