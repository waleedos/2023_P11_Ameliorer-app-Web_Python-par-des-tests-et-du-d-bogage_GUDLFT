from server import check_date_validity, update_places
from server import app
import pytest


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# ******************** TEST DE VÉRIFICATION DE L'EMAIL ********************#

def test_invalid_email(client):
    response = client.post('/showSummary', data={'email': 'invalid@simplylift.co'})
    assert b'Sorry, that email wasn\'t found.' in response.data


def test_valid_email(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert b'Welcome, john@simplylift.co' in response.data


# ******************** TEST DE VALIDITÉ DE LA DATE DE LA COMPÉTITION ********************#

def test_invalid_competition_date(client):
    competition = {'date': '2020-01-01 10:00:00'}  # Une date passée
    assert not check_date_validity(competition)


# ******************** TEST DE MISE À JOUR DES POINTS ET DES PLACES ********************#

def test_update_points_and_places(client):
    competition = {'numberOfPlaces': '10'}
    club = {'points': '15'}
    places_required = 5
    assert update_places(competition, places_required, club)
