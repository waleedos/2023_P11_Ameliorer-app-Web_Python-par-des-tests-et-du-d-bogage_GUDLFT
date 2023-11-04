# Importation des fonctions nécessaires depuis le module 'server' et de pytest pour les fixtures.
from server import load_competitions, load_clubs, check_date_validity
import pytest


# Fixture pour configurer un ensemble de données de test pour les fonctions de test.
@pytest.fixture
def database_fixture():
    # Chargement des compétitions et des clubs et sélection de données spécifiques pour les tests.
    data = {"competition_1": load_competitions()[5],  # On prend pour acquis que c'est une date valide.
            "competition_2": load_competitions()[1],  # On prend pour acquis que c'est une date invalide.
            "club_1": load_clubs()[0],
            "club_2": load_clubs()[1]}
    return data  # Retour des données pour les tests.


# Test pour vérifier le comportement de la fonction check_date_validity avec une date invalide.
def test_invalid_date(database_fixture):
    competition = database_fixture['competition_2']  # Sélection d'une compétition avec une date présumée invalide.
    # Vérification que la fonction retourne False pour une date invalide.
    assert not check_date_validity(competition)


# Test pour vérifier le comportement de la fonction check_date_validity avec une date valide.
def test_valid_date(database_fixture):
    competition = database_fixture['competition_1']  # Sélection d'une compétition avec une date présumée valide.
    # Vérification que la fonction retourne True pour une date valide.
    assert check_date_validity(competition)
