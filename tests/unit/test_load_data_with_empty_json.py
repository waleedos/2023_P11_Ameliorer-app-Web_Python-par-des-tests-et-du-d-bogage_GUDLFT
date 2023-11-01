import json
from server import load_clubs, load_competitions
import shutil  # Pour copier et restaurer les fichiers


def test_load_clubs_empty_file():
    # Sauvegarder le fichier clubs.json original
    shutil.copy('clubs.json', 'clubs_backup.json')

    # Créer un fichier clubs.json vide pour le test
    with open('clubs.json', 'w') as f:
        json.dump({'clubs': []}, f)

    # Appeler la fonction load_clubs et stocker le résultat
    clubs = load_clubs()

    # Vérifier que le résultat est une liste vide
    assert clubs == []

    # Restaurer le fichier clubs.json original
    shutil.copy('clubs_backup.json', 'clubs.json')


def test_load_competitions_empty_file():
    # Sauvegarder le fichier competitions.json original
    shutil.copy('competitions.json', 'competitions_backup.json')

    # Créer un fichier competitions.json vide pour le test
    with open('competitions.json', 'w') as f:
        json.dump({'competitions': []}, f)

    # Appeler la fonction load_competitions et stocker le résultat
    competitions = load_competitions()

    # Vérifier que le résultat est une liste vide
    assert competitions == []

    # Restaurer le fichier competitions.json original
    shutil.copy('competitions_backup.json', 'competitions.json')
