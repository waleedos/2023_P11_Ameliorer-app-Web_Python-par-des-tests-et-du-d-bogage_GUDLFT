# Importation des fonctions nécessaires depuis le module 'server'.
from server import load_competitions, load_clubs, update_places
# Importation de pytest pour la création de fixtures de test.
import pytest


# Fixture pour configurer un ensemble de données pour les tests.
@pytest.fixture
def database_fixture():
    # Chargement et stockage des données des compétitions et des clubs pour les tests.
    data = {"competition_1": load_competitions()[0],
            "competition_2": load_competitions()[1],
            "club_1": load_clubs()[0],
            "club_2": load_clubs()[1]}
    return data  # Retour des données pour les tests.


# Test pour vérifier le comportement lorsque le club n'a pas assez de points.
def test_not_enough_points(database_fixture):
    places_required = 10  # Définir le nombre de places demandées.
    # Mise à jour des places et stockage de la valeur de retour pour un club avec des points insuffisants.
    return_value = update_places(database_fixture['competition_1'], places_required, database_fixture['club_2'])
    assert not return_value  # S'assurer que la mise à jour échoue si le club n'a pas assez de points.


# Test pour vérifier que les points du club sont mis à jour correctement après une réservation.
def test_club_points_updated(database_fixture):
    club = database_fixture['club_1']  # Sélection d'un club pour le test.
    places_required = 10  # Définir le nombre de places demandées.
    expected_points = int(club['points']) - places_required  # Calculer les points attendus après la mise à jour.
    # Exécuter la mise à jour des places.
    update_places(database_fixture['competition_1'], places_required, club)
    # Vérifier que les points du club sont maintenant égaux aux points attendus.
    assert int(club['points']) == expected_points
