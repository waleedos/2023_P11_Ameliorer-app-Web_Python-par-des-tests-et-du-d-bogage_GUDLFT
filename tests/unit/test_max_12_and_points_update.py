# Importation des fonctions nécessaires depuis le module 'server'.
from server import load_competitions, load_clubs, update_places
# Importation de pytest pour les tests.
import pytest


# Fixture pour préparer un ensemble de données pour les tests.
@pytest.fixture
def database_fixture():
    # Chargement des données des premières compétitions et clubs.
    data = {"competition_1": load_competitions()[0],
            "competition_2": load_competitions()[1],
            "club_1": load_clubs()[0],
            "club_2": load_clubs()[1]}
    return data  # Retour des données chargées pour les tests.


# Test pour vérifier la mise à jour des places pour un nombre supérieur à 12.
def test_more_than_12_places(database_fixture):
    places_required = 13  # Définir le nombre de places demandées.
    # Tentative de mise à jour des places et stockage de la valeur de retour.
    return_value = update_places(database_fixture['competition_1'], places_required, database_fixture['club_1'])
    assert not return_value  # Vérification que la mise à jour est refusée.


# Test pour vérifier la mise à jour des places pour un nombre inférieur à 1.
def test_less_than_1_place(database_fixture):
    places_required = 0  # Définir le nombre de places demandées à zéro.
    # Tentative de mise à jour des places et stockage de la valeur de retour.
    return_value = update_places(database_fixture['competition_1'], places_required, database_fixture['club_1'])
    assert not return_value  # Vérification que la mise à jour est refusée.


# Test pour vérifier la mise à jour des places pour un nombre exact de 10.
def test_10_places(database_fixture):
    places_required = 10  # Définir le nombre de places demandées à dix.
    # Tentative de mise à jour des places et stockage de la valeur de retour.
    return_value = update_places(database_fixture['competition_1'], places_required, database_fixture['club_1'])
    assert return_value  # Vérification que la mise à jour est acceptée.
