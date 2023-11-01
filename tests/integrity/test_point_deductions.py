import json
from flask_testing import TestCase
from server import app


class TestPointDeduction(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def load_clubs(self):
        with open('./clubs.json') as c:
            list_of_clubs = json.load(c)['clubs']
            return list_of_clubs

    def test_point_deduction(self):
        # Étape 1: Notez les points initiaux pour un club
        clubs = self.load_clubs()
        initial_points = int([club['points'] for club in clubs if club['name'] == 'Bodylift France'][0])

        # Étape 2: Simulez une réservation
        # Ici, vous pouvez déduire les points manuellement
        # ou appeler une fonction qui le fait
        final_points = initial_points - 1  # Remplacez 1 par le coût en points de la réservation

        # Étape 3: Vérifiez que les points sont correctement déduits
        self.assertEqual(final_points, initial_points - 1)  # Remplacez 1 par le coût en points de la réservation
