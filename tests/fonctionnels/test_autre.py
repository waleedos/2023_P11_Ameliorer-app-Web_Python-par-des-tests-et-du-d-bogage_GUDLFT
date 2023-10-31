from server import app
import pytest


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# ******** Test fonctionnel de la validité des données du formulaire ********#


def test_form_data_validity(client):
    # Log in using a valid email
    client.post('/showSummary', data={'email': 'john@simplylift.co'})

    # Test for a negative number of places
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Festival',
        'places': '-1'
    }, follow_redirects=True)
    assert b'You tried to book an invalid number of places, sorry' in response.data

    # Test for zero places
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Festival',
        'places': '0'
    }, follow_redirects=True)
    assert b'You tried to book an invalid number of places, sorry' in response.data

    # Test for a number of places greater than available points
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Festival',
        'places': '100'
    }, follow_redirects=True)
    assert b'You tried to book an invalid number of places, sorry' in response.data

    # Test for a number of places as text
    with pytest.raises(ValueError):
        response = client.post('/purchasePlaces', data={
            'club': 'Simply Lift',
            'competition': 'Spring Festival',
            'places': 'texte'
        }, follow_redirects=True)
