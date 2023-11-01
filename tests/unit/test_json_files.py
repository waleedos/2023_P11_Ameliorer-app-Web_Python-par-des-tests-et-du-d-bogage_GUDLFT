import json
import re


def is_valid_json(json_file_path):
    try:
        with open(json_file_path, 'r') as f:
            json.load(f)
        return True
    except json.JSONDecodeError:
        return False


def test_clubs_json_format():
    assert is_valid_json('clubs.json'), "clubs.json is not a valid JSON file"


def test_competitions_json_format():
    assert is_valid_json('competitions.json'), "competitions.json is not a valid JSON file"


def test_clubs_json_fields():
    with open('clubs.json', 'r') as f:
        clubs = json.load(f)['clubs']
        for club in clubs:
            assert 'name' in club, "Missing 'name' field in clubs.json"
            assert 'email' in club, "Missing 'email' field in clubs.json"
            assert 'points' in club, "Missing 'points' field in clubs.json"


def test_competitions_json_fields():
    with open('competitions.json', 'r') as f:
        competitions = json.load(f)['competitions']
        for competition in competitions:
            assert 'name' in competition, "Missing 'name' field in competitions.json"
            assert 'date' in competition, "Missing 'date' field in competitions.json"
            assert 'numberOfPlaces' in competition, "Missing 'numberOfPlaces' field in competitions.json"


def is_valid_email(email):
    regex = r'^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@][a-zA-Z0-9-]+([.][a-zA-Z0-9-]+)+$'
    return bool(re.search(regex, email))


def test_clubs_json_points():
    with open('clubs.json', 'r') as f:
        clubs = json.load(f)['clubs']
        for club in clubs:
            assert isinstance(int(club['points']), int), f"Invalid points value for club {club['name']}"
            assert int(club['points']) >= 0, f"Negative points value for club {club['name']}"


def test_clubs_json_emails():
    with open('clubs.json', 'r') as f:
        clubs = json.load(f)['clubs']
        for club in clubs:
            assert is_valid_email(club['email']), f"Invalid email format for club {club['name']}"
