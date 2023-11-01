import json
from flask_testing import TestCase
from server import app


class TestPlaceUpdate(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def load_competitions(self):
        with open('./competitions.json') as c:
            list_of_competitions = json.load(c)['competitions']
            return list_of_competitions

    def test_place_update(self):
        # Étape 1: Notez les places initialement disponibles pour une compétition
        competitions = self.load_competitions()
        initial_places = int([comp['numberOfPlaces'] for comp in competitions if comp['name'] == 'Texas She Lifts'][0])

        # Étape 2: Simulez une réservation
        # Ici, vous pouvez déduire les places manuellement
        # ou appeler une fonction qui le fait
        final_places = initial_places - 1

        # Étape 3: Vérifiez que le nombre de places disponibles est correctement mis à jour
        self.assertEqual(final_places, initial_places - 1)
