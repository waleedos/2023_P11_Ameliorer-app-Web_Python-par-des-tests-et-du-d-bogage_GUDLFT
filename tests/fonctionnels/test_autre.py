import json
import pytest
from server import app  # assuming 'app' is the Flask instance


@pytest.fixture
def test_client():
    """Fixture to create a Flask test client."""
    with app.test_client() as client:
        yield client


# ******* Test fonctionnel de la mise à jour des fichiers JSON **********#


@pytest.fixture
def data_before_test():
    """Fixture to load initial data from JSON files."""
    # Assuming that the JSON files exist and are in the correct format
    with open('clubs.json', 'r') as c:
        clubs_data = json.load(c)
    with open('competitions.json', 'r') as comps:
        competitions_data = json.load(comps)
    return clubs_data, competitions_data


def test_json_update_after_booking(test_client, data_before_test):
    """Test to verify JSON updates after a booking is made."""
    # Perform the booking operation, which should internally update the data
    response = test_client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Festival',
        'places': 5
    })
    assert response.status_code == 200

    # Now, you will need to assert that the data has been updated in memory
    # since you cannot check the actual JSON files (due to the absence of save_data_to_json)
    # You can potentially check the flash messages or the returned HTML for confirmation
    # If your function returns updated data, you can capture it from the response and compare
    # You may need to parse HTML or JSON from the response depending on what your endpoint returns

    # Example assertion (you'll need to replace this with actual logic to check response data)
    # assert 'Great-booking complete!' in response.get_data(as_text=True)
