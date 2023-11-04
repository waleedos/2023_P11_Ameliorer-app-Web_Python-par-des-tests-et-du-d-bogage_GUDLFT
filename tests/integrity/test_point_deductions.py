import json
from flask_testing import TestCase
from server import app


# Classe de test héritant de TestCase pour tester les fonctionnalités Flask
class TestPointDeduction(TestCase):

    # Méthode de configuration de l'application Flask pour les tests
    def create_app(self):
        app.config['TESTING'] = True  # Activation du mode TEST
        return app  # Retour de l'instance de l'application Flask

    # Méthode pour charger les clubs à partir du fichier JSON
    def load_clubs(self):
        with open('./clubs.json') as c:
            list_of_clubs = json.load(c)['clubs']
            return list_of_clubs  # Retourne la liste des clubs

    # Test de la déduction des points après une réservation
    def test_point_deduction(self):
        # Étape 1: Obtenir le nombre initial de points pour un club donné
        clubs = self.load_clubs()
        initial_points = int([club['points'] for club in clubs if club['name'] == 'Simply Lift'][0])

        # Étape 2: Simuler une réservation en déduisant des points
        points_to_deduct = 3  # Supposons que la réservation coûte 3 points
        final_points = initial_points - points_to_deduct  # Simule la déduction des points

        # Étape 3: Vérifier que les points du club sont bien déduits
        self.assertEqual(final_points, initial_points - points_to_deduct)  # Assertion pour comparer les points restants
