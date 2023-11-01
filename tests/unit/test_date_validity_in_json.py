from datetime import datetime
import json
import warnings


def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        return True
    except ValueError:
        return False


def test_competitions_json_dates():
    with open('competitions.json', 'r') as f:
        competitions = json.load(f)['competitions']
        for competition in competitions:
            assert is_valid_date(competition['date']), f"Invalid date format for competition {competition['name']}"
            competition_date = datetime.strptime(competition['date'], "%Y-%m-%d %H:%M:%S")
            if competition_date <= datetime.now():
                warnings.warn(f"Date is in the past for competition {competition['name']}")
            else:
                assert True  # Date is in the future, so the test passes
