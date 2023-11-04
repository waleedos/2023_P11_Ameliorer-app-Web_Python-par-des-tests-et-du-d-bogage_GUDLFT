# Importation des modules nécessaires pour le test de charge avec Locust.
from locust import HttpUser, task, between
import json
import random
from datetime import datetime
import os

# Définir le chemin de base pour accéder aux fichiers dans le répertoire parent.
BASE_PATH = os.path.dirname(os.path.dirname(__file__))


# Fonction pour charger les données à partir d'un fichier JSON.
def load_data_from_json(filename):
    # Construction du chemin absolu vers le fichier JSON souhaité.
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '../../', filename)
    with open(file_path, 'r') as file:
        data = json.load(file)  # Charger les données JSON depuis le fichier.
    return data


# Charger les données des clubs et des compétitions à partir des fichiers JSON.
clubs_data = load_data_from_json('clubs.json')['clubs']
competitions_data = load_data_from_json('competitions.json')['competitions']

# Sélectionner uniquement les compétitions futures avec des places disponibles.
future_competitions = [
    comp for comp in competitions_data
    if datetime.strptime(comp['date'], "%Y-%m-%d %H:%M:%S") > datetime.now()  # Vérifier que la date est future.
    and int(comp['numberOfPlaces']) > 0  # Vérifier qu'il y a des places disponibles.
]


# Définir une classe d'utilisateur pour les tests de charge avec Locust.
class GUDLFTUser(HttpUser):
    wait_time = between(1, 5)  # L'utilisateur attend entre 1 et 5 secondes entre les tâches.

    # Méthode appelée lors du démarrage de l'exécution des tâches de l'utilisateur.
    def on_start(self):
        # Sélectionner un club et une compétition de manière aléatoire pour l'utilisateur.
        self.club = random.choice(clubs_data)  # Choisir un club aléatoire.
        self.competition = random.choice(future_competitions)  # Choisir une compétition future aléatoire.

    # Tâche pour simuler la connexion et le chargement des compétitions.
    @task
    def login_and_load_competitions(self):
        # Se connecter en utilisant l'adresse e-mail du club sélectionné.
        self.client.post("/showSummary", data={"email": self.club['email']})

    # Tâche pour simuler la réservation de places.
    @task
    def book_places(self):
        # Récupérer les noms de la compétition et du club.
        competition_name = self.competition['name']
        club_name = self.club['name']
        # Choisir un nombre aléatoire de places à réserver, entre 1 et 5.
        places_to_book = str(random.randint(1, 5))

        # Envoyer une requête GET pour accéder à la page de réservation.
        self.client.get(f"/book/{competition_name}/{club_name}")
        # Envoyer une requête POST pour effectuer la réservation des places.
        self.client.post("/purchasePlaces", data={
            "club": club_name,
            "competition": competition_name,
            "places": places_to_book
        })
