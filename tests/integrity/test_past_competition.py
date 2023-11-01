from server import app, load_competitions, load_clubs
import pytest

# ****** Test Booking for a past competition ****** #


@pytest.fixture
def test_client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def database_fixture():
    data = {
        "competition_1": load_competitions()[5],  # Assurez-vous que c'est une compétition future
        "competition_2": load_competitions()[1],  # Assurez-vous que c'est une compétition passée
        "club_1": load_clubs()[0],
        "club_2": load_clubs()[1]
    }
    return data


def test_booking_for_past_competition(test_client, database_fixture):
    competition = database_fixture['competition_2']  # Assumons que c'est la compétition passée
    club = database_fixture['club_1']['name']  # Utilisez le nom du club ici
    response = test_client.post(f'/book/{competition["name"]}/{club}')

    # Utilisation de la variable 'response' pour une assertion
    assert b"Selected competition is over" in response.data
