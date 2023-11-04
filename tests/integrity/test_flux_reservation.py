# Importation de la classe TestCase de flask_testing et de l'application Flask.
from flask_testing import TestCase
from server import app


# Création d'une classe de test pour le flux de réservation en héritant de TestCase.
class TestBookingFlow(TestCase):

    # Configuration de l'application pour les tests.
    def create_app(self):
        app.config['TESTING'] = True  # Activation du mode test.
        return app  # Renvoi de l'application configurée pour le test.

    # Test du flux de réservation complet.
    def test_booking_flow(self):
        # Étape 1 : Connexion avec un e-mail de club valide.
        response = self.client.post("/showSummary", data={"email": "marina@bodylift.fr"})
        # Affichage de la réponse pour le débogage.
        print("Étape 1 - Réponse:", response.data)
        # Vérification que la réponse est un succès (code HTTP 200).
        self.assert200(response)

        # Étape 2 : Accès à la page de réservation pour une compétition donnée et un club donné.
        competition_name = "Texas She Lifts"
        club_name = "Bodylift France"
        response = self.client.get(f"/book/{competition_name}/{club_name}")
        # Affichage de la réponse pour le débogage.
        print("Étape 2 - Réponse:", response.data)
        # Vérification que la réponse est un succès (code HTTP 200).
        self.assert200(response)

        # Étape 3 : Envoi de la demande de réservation de places pour la compétition.
        response = self.client.post(
            "/purchasePlaces",
            data={
                "club": "Bodylift France",
                "competition": "Texas She Lifts",
                "places": 1  # Nombre de places à réserver.
            }
        )
        # Affichage de la réponse pour le débogage.
        print("Étape 3 - Réponse:", response.data)
        # Vérification que la réponse est un succès (code HTTP 200) et que le message de confirmation est présent.
        self.assert200(response)
        self.assertIn(b"Great-booking complete!", response.data)
