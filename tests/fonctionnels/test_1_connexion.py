from server import app
import pytest
from server import check_date_validity, update_places


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# ******************** TEST DE LOGIN ********************#

def test_valid_login(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert b'Welcome' in response.data


# ******************** TEST DE NAVIGATION ********************#

def test_navigation(client):
    # Utilisation d'un email valide existant dans le fichier clubs.json
    client.post('/showSummary', data={'email': 'john@simplylift.co'})

    # Test de navigation vers la table des clubs
    response = client.get('/club_table.html')
    assert response.status_code == 200

    # Test de navigation vers la page de déconnexion
    response = client.get('/logout')
    assert response.status_code == 302  # Attendu car il y a une redirection


# ******************** TEST DE RÉSERVATION ********************#

def test_booking(client):
    # Étape 1 : Connexion avec un email valide existant dans le fichier clubs.json
    client.post('/showSummary', data={'email': 'john@simplylift.co'})

    # Étape 2 : Navigation vers la page de réservation pour une compétition et un club spécifiques
    response = client.get('/book/Spring Festival/Simply Lift')
    assert response.status_code == 200

    # Étape 3 : Finalisation de la réservation
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Festival',
        'places': '5'
    })
    assert b'Great-booking complete!' in response.data


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


# ******************** Test de la limite de points du club ********************#

def test_club_point_limit(client):
    # Étape 1 : Connexion avec un email valide existant dans le fichier clubs.json
    client.post('/showSummary', data={'email': 'john@simplylift.co'})

    # Étape 2 : Tenter de réserver plus de places que les points disponibles pour le club
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Festival',
        'places': '20'  # Supposons que le club ait moins de 20 points
    })
    assert b'You tried to book an invalid number of places, sorry' in response.data
