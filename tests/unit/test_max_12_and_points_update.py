from server import load_competitions, load_clubs, update_places
import pytest


@pytest.fixture
def database_fixture():
    data = {"competition_1": load_competitions()[0],
            "competition_2": load_competitions()[1],
            "club_1": load_clubs()[0],
            "club_2": load_clubs()[1]}
    return data


def test_more_than_12_places(database_fixture):
    places_required = 13
    return_value = update_places(database_fixture['competition_1'], places_required, database_fixture['club_1'])
    assert not return_value


def test_less_than_1_place(database_fixture):
    places_required = 0
    return_value = update_places(database_fixture['competition_1'], places_required, database_fixture['club_1'])
    assert not return_value


def test_10_places(database_fixture):
    places_required = 10
    return_value = update_places(database_fixture['competition_1'], places_required, database_fixture['club_1'])
    assert return_value
