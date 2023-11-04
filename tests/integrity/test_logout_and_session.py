# Import pytest for writing tests and app from server for the Flask application.
import pytest
from server import app, load_clubs, load_competitions


# Fixture to set up a test client for the Flask application.
@pytest.fixture
def test_client():
    app.config['TESTING'] = True  # Enable testing mode for Flask.
    with app.test_client() as client:
        yield client  # Provide the client to the test functions.


# Fixture to set up a sample database for tests.
@pytest.fixture
def database_fixture():
    # This fixture prepares a set of data for testing by loading some clubs and competitions.
    data = {
        "competition_1": load_competitions()[0],
        "competition_2": load_competitions()[1],
        "club_1": load_clubs()[0],
        "club_2": load_clubs()[1]
    }
    return data  # Return the prepared data.


# Test function to check the logout functionality and session management.
def test_logout_and_session(test_client, database_fixture):
    # Step 1: Simulate a login action.
    response = test_client.post('/showSummary', data={
        "email": "dany@austbuild.com"
    }, follow_redirects=True)
    assert b'Welcome' in response.data  # Ensure the login is successful by checking the response.

    # Step 2: Simulate a logout action.
    response = test_client.get('/logout', follow_redirects=True)
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data  # Check that the user is logged out.

    # Step 3: Try to access the 'showSummary' page without being logged in.
    response = test_client.post('/showSummary', data={
        "email": ""
    }, follow_redirects=True)
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data  # The user should be redirected
    # to the home page.
