# Importations de modules
import json
from flask import Flask, render_template, request, redirect, flash, url_for


# Fonctions pour charger les données
def load_clubs():
    with open('clubs.json') as c:
        list_of_clubs = json.load(c)['clubs']
        return list_of_clubs


def load_competitions():
    with open('competitions.json') as comps:
        list_of_competitions = json.load(comps)['competitions']
        return list_of_competitions


# Fonctions supplémentaires (provenant de la version de maintenant)
def get_club_and_competition(club: str, competition: str) -> (bool, dict, dict):
    competition = [c for c in competitions if c['name'] == competition]
    club = [c for c in clubs if c['name'] == club]
    if not competition or not club:
        return False, None, None
    return True, club[0], competition[0]


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


# Initialisation de l'application Flask
app = Flask(__name__)
app.secret_key = 'something_special'

competitions = load_competitions()
clubs = load_clubs()


# Vérification de l'email (provenant de la dernière version)
def check_email(email: str) -> dict:
    clubs_found = []
    for club in clubs:
        if club['email'] and club['email'] == email:
            clubs_found.append(club)
    if not clubs_found:
        return {}
    else:
        return clubs_found[0]


# Routes (fusionnées)
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


@app.route('/book/<competition>/<club>')
def book(competition, club):
    ok_flag, found_club, found_competition = get_club_and_competition(club, competition)
    if ok_flag:
        return render_template('booking.html', club=found_club, competition=found_competition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


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


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


# Lancement de l'application
if __name__ == '__main__':
    app.run(debug=True)
