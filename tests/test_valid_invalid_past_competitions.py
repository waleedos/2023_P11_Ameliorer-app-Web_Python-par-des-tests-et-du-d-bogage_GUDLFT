from server import load_competitions, load_clubs, check_date_validity
import pytest


@pytest.fixture
def database_fixture():
    data = {"competition_1": load_competitions()[5],
            "competition_2": load_competitions()[1],
            "club_1": load_clubs()[0],
            "club_2": load_clubs()[1]}
    return data


def test_invalid_date(database_fixture):
    competition = database_fixture['competition_2']
    assert not check_date_validity(competition)


def test_valid_date(database_fixture):
    competition = database_fixture['competition_1']
    assert check_date_validity(competition)
