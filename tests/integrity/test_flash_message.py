from server import app, load_competitions, load_clubs
import pytest

# ****** Test Flash Messages ****** #


@pytest.fixture
def test_client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def database_fixture():
    data = {
        "competition_1": load_competitions()[0],  # Assurez-vous que c'est une compétition future
        "competition_2": load_competitions()[1],  # Assurez-vous que c'est une compétition passée
        "club_1": load_clubs()[0],
        "club_2": load_clubs()[1]
    }
    return data


def test_flash_messages(test_client, database_fixture):
    # Test pour une réservation réussie
    competition = database_fixture['competition_1']
    club = database_fixture['club_1']['name']
    response = test_client.post('/purchasePlaces', data={
        "club": club,
        "competition": competition["name"],
        "places": 1
    }, follow_redirects=True)
    assert b'Great-booking complete!' in response.data

    # Test pour une réservation invalide
    competition = database_fixture['competition_1']
    club = database_fixture['club_1']['name']
    response = test_client.post('/purchasePlaces', data={
        "club": club,
        "competition": competition["name"],
        "places": 20  # Un nombre invalide de places
    }, follow_redirects=True)
    assert b'You tried to book an invalid number of places, sorry' in response.data

    # Test pour une compétition passée
    competition = database_fixture['competition_2']
    club = database_fixture['club_1']['name']
    response = test_client.get(f'/book/{competition["name"]}/{club}', follow_redirects=True)
    assert b'Selected competition is over' in response.data
