from flask_testing import TestCase
from server import app


class TestBookingFlow(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_booking_flow(self):
        # Étape 1 : Connectez-vous avec un e-mail de club valide
        response = self.client.post("/showSummary", data={"email": "marina@bodylift.fr"})
        print("Étape 1 - Réponse:", response.data)
        self.assert200(response)  # Vérifie que le code de statut HTTP est 200

        competition_name = "Texas She Lifts"
        club_name = "Bodylift France"
        response = self.client.get(f"/book/{competition_name}/{club_name}")
        print("Étape 2 - Réponse:", response.data)
        self.assert200(response)  # Vérifie que le code de statut HTTP est 200

        response = self.client.post(
            "/purchasePlaces",
            data={
                "club": "Bodylift France",
                "competition": "Texas She Lifts",
                "places": 1
            }
        )

        print("Étape 3 - Réponse:", response.data)  # Ajout d'une instruction print pour le débogage
        self.assert200(response)
        self.assertIn(b"Great-booking complete!", response.data)
