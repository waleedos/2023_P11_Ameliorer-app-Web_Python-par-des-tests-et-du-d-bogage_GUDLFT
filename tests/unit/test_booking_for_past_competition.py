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
        "competition_1": load_competitions()[0],
        "competition_2": load_competitions()[1],
        "club_1": load_clubs()[0],
        "club_2": load_clubs()[1]
    }
    return data


def test_booking_for_past_competition(test_client, database_fixture):
    competition = database_fixture['competition_2']  # Assuming this is the past competition
    response = test_client.get('/book/' + competition['name'] + '/Simply Lift')
    assert b"Selected competition is over" in response.data
