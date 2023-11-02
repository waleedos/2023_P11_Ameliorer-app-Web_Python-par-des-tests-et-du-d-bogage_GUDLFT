from locust import HttpUser, task, between
import json
import random
from datetime import datetime
import os

# Chemin relatif pour remonter d'un niveau dans l'arborescence des dossiers
BASE_PATH = os.path.dirname(os.path.dirname(__file__))


# Fonction pour charger les données à partir d'un fichier JSON
def load_data_from_json(filename):
    # Construire le chemin absolu vers le fichier JSON
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '../../', filename)
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


# Charger les données des fichiers JSON
clubs_data = load_data_from_json('clubs.json')['clubs']
competitions_data = load_data_from_json('competitions.json')['competitions']


# Filtrer les compétitions futures avec des places disponibles
future_competitions = [
    comp for comp in competitions_data
    if datetime.strptime(comp['date'], "%Y-%m-%d %H:%M:%S") > datetime.now()
    and int(comp['numberOfPlaces']) > 0
]


class GUDLFTUser(HttpUser):
    wait_time = between(1, 5)  # L'utilisateur attend entre 1 et 5 secondes entre les tâches

    def on_start(self):
        """ Cette méthode est appelée quand un utilisateur commence à exécuter des tâches. """
        self.club = random.choice(clubs_data)  # Sélectionner un club aléatoirement
        self.competition = random.choice(future_competitions)  # Sélectionner une compétition future aléatoirement

    @task
    def login_and_load_competitions(self):
        # Se connecter avec un email aléatoire du club sélectionné
        self.client.post("/showSummary", data={"email": self.club['email']})

    @task
    def book_places(self):
        # Réserver des places pour une compétition aléatoire
        competition_name = self.competition['name']
        club_name = self.club['name']
        places_to_book = str(random.randint(1, 5))  # Réserver entre 1 et 5 places

        self.client.get(f"/book/{competition_name}/{club_name}")
        self.client.post("/purchasePlaces", data={
            "club": club_name,
            "competition": competition_name,
            "places": places_to_book
        })
