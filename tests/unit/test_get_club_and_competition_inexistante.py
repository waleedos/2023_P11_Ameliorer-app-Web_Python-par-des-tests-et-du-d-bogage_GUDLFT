# Importation de la fonction depuis le module 'server'.
from server import get_club_and_competition


# Définition de la fonction de test pour un club et une compétition inexistants.
def test_get_club_and_competition_nonexistent():
    # Configuration des données de test avec des noms fictifs.
    club_name = 'Nonexistent Club'
    competition_name = 'Nonexistent Competition'

    # Appel de la fonction avec des données qui ne devraient pas exister.
    ok_flag, returned_club, returned_competition = get_club_and_competition(club_name, competition_name)

    # Vérification que la fonction retourne les valeurs attendues pour des entrées non existantes.
    assert ok_flag is False  # Le drapeau doit être False indiquant une recherche infructueuse.
    assert returned_club is None  # Aucun club ne devrait être retourné.
    assert returned_competition is None  # Aucune compétition ne devrait être retournée.
