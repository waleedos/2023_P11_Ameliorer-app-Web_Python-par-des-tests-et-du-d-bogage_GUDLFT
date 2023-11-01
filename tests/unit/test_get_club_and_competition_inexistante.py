from server import get_club_and_competition


# Définir la fonction de test
def test_get_club_and_competition_nonexistent():
    # Données de test
    club_name = 'Nonexistent Club'
    competition_name = 'Nonexistent Competition'

    # Appeler la fonction get_club_and_competition et stocker le résultat
    ok_flag, returned_club, returned_competition = get_club_and_competition(club_name, competition_name)

    # Vérifier que le résultat est False, None, None
    assert ok_flag is False
    assert returned_club is None
    assert returned_competition is None
