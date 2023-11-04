# Importation des modules nécessaires.
from datetime import datetime
import json
import warnings


# Définition de la fonction pour vérifier la validité d'une date.
def is_valid_date(date_str):
    try:
        # Tentative de conversion de la chaîne de caractères en date.
        datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        return True  # La date est valide.
    except ValueError:
        return False  # La date n'est pas valide.


# Test pour vérifier les dates dans le fichier 'competitions.json'.
def test_competitions_json_dates():
    # Ouverture et lecture du fichier 'competitions.json'.
    with open('competitions.json', 'r') as f:
        competitions = json.load(f)['competitions']  # Chargement des compétitions.
        for competition in competitions:
            # Vérification de la validité de la date de chaque compétition.
            assert is_valid_date(competition['date']), f"Invalid date format for competition {competition['name']}"
            # Conversion de la date de la compétition en objet datetime.
            competition_date = datetime.strptime(competition['date'], "%Y-%m-%d %H:%M:%S")
            # Avertissement si la date de la compétition est passée.
            if competition_date <= datetime.now():
                warnings.warn(f"Date is in the past for competition {competition['name']}")
            else:
                assert True  # La date est dans le futur, le test est réussi.
