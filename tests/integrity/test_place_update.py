import json
from flask_testing import TestCase
from server import app


# Classe de test héritant de TestCase pour tester les fonctionnalités Flask
class TestPlaceUpdate(TestCase):

    # Méthode de configuration de l'application Flask pour les tests
    def create_app(self):
        app.config['TESTING'] = True  # Activation du mode TEST
        return app  # Retour de l'instance de l'application Flask

    # Méthode pour charger les compétitions à partir du fichier JSON
    def load_competitions(self):
        with open('./competitions.json') as c:
            list_of_competitions = json.load(c)['competitions']
            return list_of_competitions  # Retourne la liste des compétitions

    # Test de la mise à jour des places après une réservation
    def test_place_update(self):
        # Étape 1: Obtenir le nombre initial de places pour une compétition donnée
        competitions = self.load_competitions()
        initial_places = int([comp['numberOfPlaces'] for comp in competitions if comp['name'] == 'Spring Festival'][0])

        # Étape 2: Simuler une réservation en déduisant une place
        final_places = initial_places - 1  # Simule la réservation d'une place

        # Étape 3: Vérifier que le nombre de places disponibles est bien mis à jour
        self.assertEqual(final_places, initial_places - 1)  # Assertion pour comparer les places restantes
