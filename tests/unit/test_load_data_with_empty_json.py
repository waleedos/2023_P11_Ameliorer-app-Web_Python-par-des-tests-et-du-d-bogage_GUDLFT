# Importation des modules nécessaires.
import json
from server import load_clubs, load_competitions
import shutil  # Utilisé pour la gestion des fichiers.


# Test de la fonction load_clubs avec un fichier vide.
def test_load_clubs_empty_file():
    # Sauvegarde du fichier 'clubs.json' original.
    shutil.copy('clubs.json', 'clubs_backup.json')

    # Création d'un fichier 'clubs.json' vide pour le test.
    with open('clubs.json', 'w') as f:
        json.dump({'clubs': []}, f)

    # Chargement des clubs à partir du fichier modifié.
    clubs = load_clubs()

    # Vérification que la liste des clubs est vide.
    assert clubs == []

    # Restauration du fichier 'clubs.json' original.
    shutil.copy('clubs_backup.json', 'clubs.json')


# Test de la fonction load_competitions avec un fichier vide.
def test_load_competitions_empty_file():
    # Sauvegarde du fichier 'competitions.json' original.
    shutil.copy('competitions.json', 'competitions_backup.json')

    # Création d'un fichier 'competitions.json' vide pour le test.
    with open('competitions.json', 'w') as f:
        json.dump({'competitions': []}, f)

    # Chargement des compétitions à partir du fichier modifié.
    competitions = load_competitions()

    # Vérification que la liste des compétitions est vide.
    assert competitions == []

    # Restauration du fichier 'competitions.json' original.
    shutil.copy('competitions_backup.json', 'competitions.json')
