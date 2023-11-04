# Importations de modules
import json
from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime  # Ajouté pour la gestion du temps


# Fonctions pour charger les données: Ouvre le fichier clubs.json, extrait la liste des clubs et la renvoie.
def load_clubs():
    with open('clubs.json') as c:
        list_of_clubs = json.load(c)['clubs']
        return list_of_clubs


# Fonctions pour charger les données: Ouvre le fichier competitions.json, extrait la liste des compétitions et la
# renvoie.
def load_competitions():
    with open('competitions.json') as comps:
        list_of_competitions = json.load(comps)['competitions']
        return list_of_competitions


# Fonction pour vérifier la validité de la date: Vérifie si la date de la compétition est ultérieure à la date et à
# l'heure actuelles.
def check_date_validity(competition: dict) -> bool:
    current_time = datetime.now()
    competition_time_str = competition["date"]
    competition_time = datetime.strptime(competition_time_str, "%Y-%m-%d %H:%M:%S")
    return current_time < competition_time


# Fonctions supplémentaires: Cette fonction prend deux arguments : club et competition, qui sont des chaînes de
# caractères représentant respectivement le nom du club et le nom de la compétition que l'utilisateur souhaite
# rechercher. La fonction parcourt les listes de clubs et de compétitions préalablement chargées à partir des
# fichiers JSON pour trouver des correspondances en fonction des noms fournis. Si elle trouve à la fois un club
# et une compétition correspondants, elle renvoie un drapeau de réussite (True) et les informations du club et
# de la compétition sous forme de dictionnaires. Si aucune correspondance n'est trouvée pour le club ou la
# compétition, elle renvoie un drapeau d'échec (False) et None pour le club et la compétition.
def get_club_and_competition(club: str, competition: str) -> (bool, dict, dict):
    competition = [c for c in competitions if c['name'] == competition]
    club = [c for c in clubs if c['name'] == club]
    if not competition or not club:
        return False, None, None
    return True, club[0], competition[0]


# Fonction pour mettre à jour les places: update_places(competition: dict, places_required: int, club: dict) -> bool:
# Met à jour le nombre de places disponibles pour une compétition et le nombre de points du club en fonction du nombre
# de places requis.
def update_places(competition: dict, places_required: int, club: dict) -> bool:
    nbr_places = int(competition['numberOfPlaces'])
    club_nbr_points = int(club['points'])
    if (0 < places_required < 13) and (places_required <= club_nbr_points):
        competition_places = nbr_places - places_required
        if competition_places < 0:
            return False
        competition['numberOfPlaces'] = competition_places
        club_nbr_points = club_nbr_points - places_required
        club['points'] = str(club_nbr_points)
        return True
    else:
        return False


# Initialisation de l'application Flask: Crée une instance de l'application Flask, définit une clé secrète et charge
# les données des clubs et des compétitions à partir des fichiers JSON.
app = Flask(__name__)
app.secret_key = 'something_special'

competitions = load_competitions()
clubs = load_clubs()


# Vérification de l'email: Cette fonction prend une chaîne de caractères email comme argument.
# Elle parcourt la liste des clubs chargée précédemment à partir du fichier JSON pour rechercher un club qui a une
# adresse email correspondante à celle fournie. Si elle trouve un club avec une adresse email correspondante,
# elle renvoie les informations de ce club sous forme de dictionnaire. Si aucune correspondance n'est trouvée, elle
# renvoie un dictionnaire vide.
def check_email(email: str) -> dict:
    clubs_found = []
    for club in clubs:
        if club['email'] and club['email'] == email:
            clubs_found.append(club)
    if not clubs_found:
        return {}
    else:
        return clubs_found[0]


# ********************** Définition des routes de l'application ************************** #
# Routes : Les commentaires expliquent chaque route de l'application
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def show_summary():
    club = check_email(request.form['email'])
    if not club:
        return render_template('index.html', email_error=True)
    else:
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route("/book/<competition>/<club>", methods=['GET', 'POST'])
# cette route prend deux paramètres dynamiques <competition> et <club>. Ces paramètres seront extraits de l'URL
# lorsqu'un utilisateur accédera à cette route. avec les methodes http acceptées pour les requêtes GET et POST
def book(competition, club):
    foundClub = [c for c in clubs if c["name"] == club][0]
    foundCompetition = [c for c in competitions if c["name"] == competition][0]

    # Assurez-vous que la compétition n'appartient pas au passé...
    if not check_date_validity(foundCompetition):
        flash("Selected competition is over")
        return render_template("welcome.html", club=foundClub, competitions=competitions)

    if foundClub and foundCompetition:
        max_places = min(
            12, int(foundClub["points"]), int(foundCompetition["numberOfPlaces"])
        )
        return render_template(
            "booking.html",
            club=foundClub,
            competition=foundCompetition,
            max_places=max_places,
        )
    else:
        flash("Something went wrong-please try again")
        return render_template("welcome.html", club=club, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    ok_flag, club, competition = get_club_and_competition(request.form['club'], request.form['competition'])
    if not ok_flag:
        return redirect('/')
    places_required = int(request.form['places'])
    if update_places(competition, places_required, club):
        flash('Great-booking complete!')
    else:
        flash('You tried to book an invalid number of places, sorry')
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/club_table.html')
def club_table():
    return render_template('club_table.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


# Lancement de l'application: Cette section vérifie si le fichier est exécuté en tant que point d'entrée principal en
# utilisant # if __name__ == '__main__':. Si c'est le cas, l'application Flask est démarrée en mode débogage avec
# app.run(debug=True). Cela signifie que si vous exécutez ce fichier directement, l'application sera lancée et nous
# pourrons la tester localement en mode débogage.
if __name__ == '__main__':
    app.run(debug=True)
