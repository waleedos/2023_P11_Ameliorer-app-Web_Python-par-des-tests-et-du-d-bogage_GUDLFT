import json


def test_competitions_json_number_of_places():
    with open('competitions.json', 'r') as f:
        competitions = json.load(f)['competitions']
        for competition in competitions:
            num_places = int(competition['numberOfPlaces'])
            comp_name = competition['name']

            assert isinstance(num_places, int), \
                f"Invalid number of places for competition {comp_name}"

            assert num_places >= 0, \
                f"Negative number of places for competition {comp_name}"
