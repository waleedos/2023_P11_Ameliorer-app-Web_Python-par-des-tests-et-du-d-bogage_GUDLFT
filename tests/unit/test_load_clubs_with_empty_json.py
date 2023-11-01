import json
from server import load_clubs
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
