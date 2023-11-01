from server import load_competitions, load_clubs, update_places
import pytest


@pytest.fixture
def database_fixture():
    data = {"competition_1": load_competitions()[0],
            "competition_2": load_competitions()[1],
            "club_1": load_clubs()[0],
            "club_2": load_clubs()[1]}
    return data


def test_not_enough_points(database_fixture):
    places_required = 10
    return_value = update_places(database_fixture['competition_1'], places_required, database_fixture['club_2'])
    assert not return_value


def test_club_points_updated(database_fixture):
    club = database_fixture['club_1']
    places_required = 10
    expected_points = int(club['points']) - places_required
    update_places(database_fixture['competition_1'], places_required, club)
    assert int(club['points']) == expected_points
