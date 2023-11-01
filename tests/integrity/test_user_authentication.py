from flask_testing import TestCase
from server import app  # Assurez-vous que ce chemin d'importation est correct


class TestUserAuthentication(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_valid_email(self):
        response = self.client.post("/showSummary", data={"email": "john@simplylift.co"})
        self.assert200(response)

    def test_invalid_email(self):
        response = self.client.post("/showSummary", data={"email": "invalide@exemple.com"})

        # Imprimez les données de la réponse pour le débogage
        print("Response Data:", response.data)

        # Vérifiez le code de statut
        self.assert200(response)  # Utilisez 200 ici pour correspondre au comportement actuel du serveur

        # Vérifiez le contenu de la réponse
        self.assertIn(b"Sorry, that email wasn't found.", response.data)
