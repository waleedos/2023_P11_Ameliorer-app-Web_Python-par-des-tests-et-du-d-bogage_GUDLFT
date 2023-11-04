# Importation du module json pour la manipulation de fichiers JSON.
import json


# Test pour vérifier que le nombre de places dans 'competitions.json' est valide.
def test_competitions_json_number_of_places():
    # Ouverture et chargement du contenu du fichier 'competitions.json'.
    with open('competitions.json', 'r') as f:
        competitions = json.load(f)['competitions']  # Accès à la liste des compétitions.
        # Itération sur chaque compétition pour vérifier les champs.
        for competition in competitions:
            # Conversion de 'numberOfPlaces' en entier et stockage du nom pour le message d'erreur.
            num_places = int(competition['numberOfPlaces'])
            comp_name = competition['name']

            # Vérification que 'numberOfPlaces' est un entier.
            assert isinstance(num_places, int), \
                f"Invalid number of places for competition {comp_name}"

            # Vérification que 'numberOfPlaces' est un nombre non négatif.
            assert num_places >= 0, \
                f"Negative number of places for competition {comp_name}"
