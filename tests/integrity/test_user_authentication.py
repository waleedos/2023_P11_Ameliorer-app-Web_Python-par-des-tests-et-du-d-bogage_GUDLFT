from flask_testing import TestCase
from server import app  # Assurez-vous que ce chemin d'importation est correct


# Classe de test héritant de TestCase pour tester les fonctionnalités Flask
class TestUserAuthentication(TestCase):

    # Méthode de configuration de l'application Flask pour les tests
    def create_app(self):
        app.config['TESTING'] = True  # Activation du mode TEST
        return app  # Retour de l'instance de l'application Flask

    # Test avec un e-mail valide
    def test_valid_email(self):
        # Effectuer une requête POST vers '/showSummary' avec un e-mail valide
        response = self.client.post("/showSummary", data={"email": "john@simplylift.co"})
        # Vérifier que le code de réponse HTTP est 200
        self.assert200(response)

    # Test avec un e-mail invalide
    def test_invalid_email(self):
        # Effectuer une requête POST vers '/showSummary' avec un e-mail invalide
        response = self.client.post("/showSummary", data={"email": "invalide@exemple.com"})

        # Imprimer les données de la réponse pour le débogage si nécessaire
        print("Response Data:", response.data)

        # Vérifier que le code de réponse HTTP est 200 car la page s'affiche avec un message d'erreur
        self.assert200(response)

        # Vérifier que le message d'erreur "Sorry, that email wasn't found." est présent dans les données de la réponse
        self.assertIn(b"Sorry, that email wasn't found.", response.data)
