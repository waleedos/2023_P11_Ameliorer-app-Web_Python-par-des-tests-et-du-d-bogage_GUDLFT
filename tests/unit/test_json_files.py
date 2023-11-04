# Importation des modules nécessaires pour le traitement JSON et les expressions régulières.
import json
import re


# Fonction pour vérifier si un fichier est un JSON valide.
def is_valid_json(json_file_path):
    try:
        # Tentative d'ouvrir et de charger le fichier JSON.
        with open(json_file_path, 'r') as f:
            json.load(f)
        return True  # Le fichier est un JSON valide.
    except json.JSONDecodeError:
        return False  # Le fichier n'est pas un JSON valide.


# Test pour confirmer que 'clubs.json' est un fichier JSON valide.
def test_clubs_json_format():
    assert is_valid_json('clubs.json'), "clubs.json is not a valid JSON file"


# Test pour confirmer que 'competitions.json' est un fichier JSON valide.
def test_competitions_json_format():
    assert is_valid_json('competitions.json'), "competitions.json is not a valid JSON file"


# Test pour s'assurer que 'clubs.json' contient tous les champs requis.
def test_clubs_json_fields():
    with open('clubs.json', 'r') as f:
        clubs = json.load(f)['clubs']
        for club in clubs:
            # Vérification de la présence de tous les champs nécessaires pour chaque club.
            assert 'name' in club, "Missing 'name' field in clubs.json"
            assert 'email' in club, "Missing 'email' field in clubs.json"
            assert 'points' in club, "Missing 'points' field in clubs.json"


# Test pour s'assurer que 'competitions.json' contient tous les champs requis.
def test_competitions_json_fields():
    with open('competitions.json', 'r') as f:
        competitions = json.load(f)['competitions']
        for competition in competitions:
            # Vérification de la présence de tous les champs nécessaires pour chaque compétition.
            assert 'name' in competition, "Missing 'name' field in competitions.json"
            assert 'date' in competition, "Missing 'date' field in competitions.json"
            assert 'numberOfPlaces' in competition, "Missing 'numberOfPlaces' field in competitions.json"


# Fonction pour valider le format d'une adresse e-mail.
def is_valid_email(email):
    # Expression régulière pour valider le format d'une adresse e-mail.
    regex = r'^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@][a-zA-Z0-9-]+([.][a-zA-Z0-9-]+)+$'
    return bool(re.search(regex, email))


# Test pour vérifier que les valeurs des points dans 'clubs.json' sont valides.
def test_clubs_json_points():
    with open('clubs.json', 'r') as f:
        clubs = json.load(f)['clubs']
        for club in clubs:
            # Vérification que les points sont des entiers non négatifs.
            assert isinstance(int(club['points']), int), f"Invalid points value for club {club['name']}"
            assert int(club['points']) >= 0, f"Negative points value for club {club['name']}"


# Test pour vérifier que les adresses e-mails dans 'clubs.json' sont au bon format.
def test_clubs_json_emails():
    with open('clubs.json', 'r') as f:
        clubs = json.load(f)['clubs']
        for club in clubs:
            # Vérification que l'e-mail respecte le format attendu.
            assert is_valid_email(club['email']), f"Invalid email format for club {club['name']}"
